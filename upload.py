#!/usr/bin/python
import os
import sys
from auth import authenticate

currentPath = os.getcwd()

client = authenticate()

argu_len = len(sys.argv)
argu_str = str(sys.argv)

# print("argument length = {0}\n".format(argu_len))
# print("arguments is {0}\n".format(argu_str))

# get the file's path
if argu_len > 1:
    file_path = currentPath + "/{0}".format(sys.argv[1])
    # print "the file's path is {0}".format(file_path)
    response = client.upload_from_path(file_path, anon=False)
    print response['link']