#!/usr/bin/python
import os
import sys
import getopt
from auth import authenticate


def display_result_urls(res_url_list):
    """
    Helper function to display the result.

     :arg:
        res_url_list: A list for the result url(s)
    :rtype: None
    """
    if len(res_url_list) <= 1:
        print "The result url is:"
        print res_url_list[0]
    else:
        print "The result urls are:"
        for url in res_url_list:
            print url

def display_markdown_urls(res_url_list):
    """
    Helper function to display the result
    urls in markdown formatted.
    :param res_url_list:
    :return: None
    """
    if len(res_url_list) <= 1:
        print "The result url is:"
        print("![]({0})".format(res_url_list[0]))
    else: # len() = 2 or more
        print "The result urls are:"
        for url in res_url_list:
            print("![]({0})".format(url))


def main(argv):
    """
    :arg:
        argv: The argument list which we **chop it off**
              and pass the rest of the list
    :rtype: None
    """
    try:
        # ops is the parsed options, args is the remaining argumentss
        ops, args = getopt.getopt(argv, "hcodm", ["help", "copy", "open","markdown"])
    except getopt.GetoptError:
        print "Arguments Error"
        sys.exit(2)

    if not args:
        print "Please specify your images to upload."
        sys.exit()

    markdown_flag = False
    client = authenticate()
    current_path = os.getcwd()
    res_url_list = []
    print "Uploading images..."
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
        elif opt in ("-m", "--markdown"):
            markdown_flag = True
        elif opt in ("-c", "--copy"):
            import pyperclip as pc
            if markdown_flag:
                markdown_list = map(lambda x: "![](" + x + ")", res_url_list)
                text_to_copy = " ".join(markdown_list)
            else:
                text_to_copy = " ".join(res_url_list)
            pc.copy(text_to_copy)
            print("The result url(s) is copied!")
        elif opt in ("-o", "--open"):
            import webbrowser as wb
            for res_url in res_url_list:
                wb.open_new_tab(res_url)

    if markdown_flag:
        display_markdown_urls(res_url_list)
    else:
        display_result_urls(res_url_list)

if __name__ == '__main__':
    main(sys.argv[1:])
