#!/usr/bin/python3

# Live host detection tool
# Written by Cody Skinner
# github.com/wskinner74
# Twitter: @TheCodySkinner

import requests, argparse, sys, time
from requests.exceptions import ConnectionError, TooManyRedirects

code200 = []
code404 = []
code503 = []

def banner():
    print("""
         _     _             _   _           _       
        | |   (_)_   _____  | | | | ___  ___| |_ ___ 
        | |   | \ \ / / _ \ | |_| |/ _ \/ __| __/ __|
        | |___| |\ V /  __/ |  _  | (_) \__ \ |_\__ \\
        |_____|_| \_/ \___| |_| |_|\___/|___/\__|___/
                   Live Host Detection Tool
                   Written by: Cody Skinner
                        @TheCodySkinner
                        
    Please wait, this can take some time for large lists
        """)
    return None

def argument_parse():
    #parse cmd line arguments
    parser = argparse.ArgumentParser(description='Check status of hosts in domain list')
    parser.add_argument('input_file', help='Input file with domain list')
    parser.add_argument('-v', '--verbose', help="Verbose output", action="store_true")
    parser.add_argument('-s', '--add_schema', help="Add 'http://' and 'https://' to items in list", action="store_true")
    args = parser.parse_args()
    return args.input_file, args.verbose, args.add_schema

def getlist(url_file):
    #open list of addresses
    read = open(url_file, 'r')
    lines = read.readlines()
    length = len(lines)
    return lines, length

def check_url(url):
    #check URL status
    try:
        r = requests.get(url, timeout=5)
    except ConnectionError:
        return None
    except TooManyRedirects:
        return None
    else:
        return r.status_code

def it_list(url_list):
    #iterate through list
    i = 0
    for item in url_list:
        # Code for progress bar:
        #progress(i, length, status='Progress')
        #time.sleep(0.5)
        if add_schema:
            pitem = 'http://' + item.rstrip()
            sitem = 'https://' + item.rstrip()
            pcode = check_url(pitem)
            if pcode:
                if verbose:
                    print(pitem + ": " + str(pcode))
                if pcode == 200:
                    code200.append(pitem)
                if pcode == 404:
                    code404.append(pitem)
                if pcode == 503:
                    code503.append(pitem)
            scode = check_url(sitem)
            if scode:
                if verbose:
                    print(sitem + ": " + str(scode))
                if scode == 200:
                    code200.append(sitem)
                if scode == 404:
                    code404.append(sitem)
                if scode == 503:
                    code503.append(sitem)
        else:
            item = item.rstrip()
            code = check_url(item)
            if code:
                if verbose:
                    print(item + ": " + str(code))
                if code == 200:
                    code200.append(item)
                if code == 404:
                    code404.append(item)
                if code == 503:
                    code503.append(item)
        i += 1
    return None

def display():
    print("\n\nURLs with code 200:")
    for i in code200:
        print(i)
    print('\n\nURLs with code 404:')
    for i in code404:
        print(i)
    print('\n\nURLs with code 503:')
    for i in code503:
        print(i)
    return None

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.1 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('\r[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

# Entry point
banner()
url_file, verbose, add_schema = argument_parse()
url_list, length = getlist(url_file)
it_list(url_list)
display()
