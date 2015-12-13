#!/usr/bin/python
import os
import sys
import getopt
from auth import authenticate


def display_result_urls(res_url_list):
    if len(res_url_list) <= 1:
        print "The url is copied into the clipboard."
        print "The result url is:"
    else:
        print "The urls are copied into the clipboard."
        print "The result urls are:"
        for res_url in res_url_list:
            print res_url

def main(argv):
    try:
        # ops is the parsed options, args is the remaining argumentss
        ops, args = getopt.getopt(argv, "hcod", ["help", "copy", "open"])
    except getopt.GetoptError:
        print "Arguments Error"
        sys.exit(2)

    if not args:
        print "Please specify your images to upload."
        sys.exit()

    client = authenticate()
    current_path = os.getcwd()
    res_url_list = []
    for file_name in args:
        file_path = current_path + "/{0}".format(file_name)
        response = client.upload_from_path(file_path, anon=False)
        res_url_list.append(str(response['link']))

    for opt, arg in ops:
        if opt in ("-h", "--help"):
            print "Need som help"
            sys.exit()
        elif opt == "-d":
            print "The client is currently in Debug mode"
        elif opt in ("-c", "--copy"):
            import pyperclip as pc
            text_to_copy = " ".join(res_url_list)
            pc.copy(text_to_copy)
        elif opt in ("-o", "--open"):
            import webbrowser as wb
            for res_url in res_url_list:
                wb.open_new_tab(res_url)
    display_result_urls(res_url_list)

if __name__ == '__main__':
    main(sys.argv[1:])