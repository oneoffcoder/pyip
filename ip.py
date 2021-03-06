import requests
import re
import smtplib, ssl
import time
import argparse
import sys
from argparse import RawTextHelpFormatter

def parse_args(args):
    """
    Parses arguments.
    :param args: Arguments.
    :return: Arguments.
    """
    parser = argparse.ArgumentParser('IP Locator', epilog='One-Off Coder, http://www.oneoffcoder.com', formatter_class=RawTextHelpFormatter)
    
    parser.add_argument('-u', '--url', default='https://myexternalip.com/raw', required=False, help="""the URL of the site to get your external IP (default: https://myexternalip.com/raw)
    Other sites that may work.
        - https://www.ipchicken.com
        - https://myexternalip.com/raw
    """)
    parser.add_argument('-m', '--max_emails', default=-1, type=int, required=False, help='maximum emails; set to -1 for indefinite (default: -1)')
    parser.add_argument('-s', '--sleep', default=3600, type=int, required=False, help='seconds between checking/sending IP in email (default: 3600)')
    parser.add_argument('-e', '--email', required=True, help='gmail email address')
    parser.add_argument('-p', '--password', required=True, help='gmail email password')
    parser.add_argument('--subject', default='IP Address', required=False, help='email subject line modifier (default: IP Address)')
    parser.add_argument('--version', action='version', version='%(prog)s v0.0.1')

    return parser.parse_args(args)

def get_html(url):
    """
    Gets the HTML content from the specified URL.
    :param url: URL.
    :return: HTML content.
    """
    resp = requests.get(url)
    content = resp.text
    return content

def get_ip(content):
    """
    Gets the IP address(es) from the content.
    :param content: HTML content.
    :return: A pipe-delimited string of all IP addresses found.
    """
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    res = re.findall(pattern, content)
    return ' | '.join(res)


def send_email(ip, subject, email, pw):
    """
    Sends email.
    :param ip: IP address.
    :param subject: Email subject line.
    :param email: Email.
    :param pw: Password.
    """
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(email, pw)
        message = 'Subject: {}\n\n{}'.format(subject, ip)
        server.sendmail(email, email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()

args = parse_args(sys.argv[1:])

url = args.url
subject = args.subject
email = args.email
pw = args.password
max_emails = args.max_emails
sleep = args.sleep

counter = 1
while True:
    content = get_html(url)
    ip = get_ip(content)
    send_email(ip, subject, email, pw)
    print('{}: {} : done'.format(counter, ip))
    counter = counter + 1

    if max_emails > 0 and counter >= max_emails:
        break
    else:
        time.sleep(sleep)