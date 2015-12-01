#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    This is the authenticate module for imgur using ImgurClient.
'''
import base64
import os
from imgurpython import ImgurClient
from helpers import get_input, get_config

def authenticate():
    """
    :rtype: client object
    """
    # result = os.getcwd()
    src_path = os.path.dirname(os.path.abspath(__file__))
    auth_path = "{0}/auth.ini".format(src_path)

    config = get_config()
    # config.read('auth.ini')
    config.read(auth_path)
    client_id = config.get('credentials','client_id')
    client_secret = config.get('credentials', 'client_secret')
    refresh_token = config.get('credentials', 'refresh_token')
    access_token = config.get('credentials', 'access_token')

    client = ImgurClient(client_id, client_secret)
    if not refresh_token:
        # print 'not refresh token'
        authorization_url = client.get_auth_url('pin')
        # print("Go to the following URL: {0}".format(authorization_url))

        pin = get_input("Enter the pin code: ")

        # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
        credentials = client.authorize(pin, 'pin')

        # Store the refresh_token
        new_refresh_token = credentials['refresh_token']
        config.set('credentials', 'refresh_token', value=new_refresh_token)
        refresh_token = new_refresh_token
        with open(auth_path, 'wb') as configfile:
            config.write(configfile)

    if refresh_token and not access_token:
        # print 'refresh token but not access token'
        # print 'refresh token: {0}'.format(refresh_token)
        client.set_user_auth(access_token, refresh_token)
        # client = ImgurClient(client_id, client_secret, refresh_token)
        if not client.auth:
            print 'no auth!!!'
        if client.auth:
            print "there is a client.auth"
            client.auth.refresh()
            new_access_token = client.auth.current_access_token
            print 'new access token: {0}'.format(new_access_token)
            config.set('credentials', 'access_token', value=new_access_token)
            print 'writing access token'
            with open(auth_path, 'wb') as configfile:
                config.write(configfile)
            access_token = new_access_token

    if refresh_token and access_token:
        # print 'refresh token and access token'
        client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    return client


# method_list = [method for method in dir(client) if callable(getattr(client, method))]

if __name__ == '__main__':
    client = authenticate()
    images = client.get_account_images('me')
    print "Current # of images: {0}".format(len(images))

    path = '/Users/TonyChol/Dropbox/5.Personal/Photos/avatars/照片-1.jpg'
    response = client.upload_from_path(path, anon=False)
    print response['link']