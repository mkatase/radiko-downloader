#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# version 0.1.0 2020-11-18 new creation
# version 0.2.0 2020-12-06 deleted download_player(), create_key()
#                          deleted teardown()
#                          modified create_partial_key()
#                          added day handling in set_title()
# version 0.3.0 2021-01-01 modified station_id for regular expression
# version 0.4.0 2023-04-26 modified modfied auth url

import argparse
import base64
import os
import re
import subprocess
from datetime import datetime, timedelta
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

from spinner import Spinner, spinner_decorator


class Radiko:

    auth_key = 'bcd151073c03b352e1ef2fd66c32209da9ca0afa'
    fms1_url = 'https://radiko.jp/v2/api/auth1'
    fms2_url = 'https://radiko.jp/v2/api/auth2'

    def __init__(self, url):
        self.url = url
        self.spinner = Spinner()

        self.stream_url = None
        self.station_id = None
        self.ft = None
        self.to = None
        self.auth_token = None
        self.key_offset = None
        self.key_length = None
        self.partial_key = None
        self.auth_response_body = None
        self.area_id = None
        self.title = None

    @spinner_decorator('Obtaining streaming url... ', 'done')
    def set_basic_info(self):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get(self.url)
        html = driver.page_source.encode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')
        hidden_input = soup.find('input', id='share-url')
        try:
            self.stream_url = str(hidden_input['value'])
        except TypeError:
            print('hidden_input is empty !! Try again !!')
            exit()

        pat = r'station_id=(?P<station_id>[A-Z]+.*)&ft=(?P<ft>[0-9]+)&to=(?P<to>[0-9]+)'
        match = re.search(pat, self.stream_url)
        if match:
            self.station_id = match.group('station_id')
            self.ft = match.group('ft')
            self.to = match.group('to')
    
    def authenticate(self):
        @spinner_decorator('Authenticating with auth1_fms... ', 'done')
        def auth1():
            headers = {
                'X-Radiko-App': 'pc_html5',
                'X-Radiko-App-Version': '0.0.1',
                'X-Radiko-User': 'test-stream',
                'X-Radiko-Device': 'pc'
            }
            r = requests.get(url=self.fms1_url, headers=headers)
            
            if r.status_code == 200:
                response_headers = r.headers
                self.auth_token = response_headers['x-radiko-authtoken']
                self.key_offset = int(response_headers['x-radiko-keyoffset'])
                self.key_length = int(response_headers['x-radiko-keylength'])
            else:
                print(' Status Code := {}'.format(r.status_code))
        
        @spinner_decorator('Creating partial key file... ', 'done')
        def create_partial_key():
            tmp_key = self.auth_key[self.key_offset: self.key_offset + self.key_length]
            self.partial_key = base64.b64encode(tmp_key.encode('utf-8')).decode('utf-8')
        
        @spinner_decorator('Authenticating with auth2_fms... ', 'done')
        def auth2():
            headers ={
                'X-Radiko-User': 'test-stream',
                'X-Radiko-Device': 'pc',
                'X-Radiko-Authtoken': '{}'.format(self.auth_token),
                'X-Radiko-Partialkey': '{}'.format(self.partial_key),
            }
            r = requests.get(url=self.fms2_url, headers=headers)

            if r.status_code == 200:
                self.auth_response_body = r.text
        
        auth1()
        create_partial_key()
        auth2()
    
    def set_area_id(self):
        area = self.auth_response_body.strip().split(',')
        self.area_id = area[0]
    
    @spinner_decorator('Obtainig file title... ', 'done')
    def set_title(self):
        try:
            datetime_api_url = 'http://radiko.jp/v3/program/date/{}/{}.xml'.format(self.ft[:8], self.area_id)
            r = requests.get(url=datetime_api_url)
            if r.status_code == 200:
                channels_xml = r.content
                tree = ET.fromstring(channels_xml)
                station = tree.find('.//station[@id="{}"]'.format(self.station_id))
                prog = station.find('.//prog[@ft="{}"]'.format(self.ft))
                to = prog.attrib['to']
        except AttributeError:
            n = datetime.strptime(self.ft[:8], '%Y%m%d')
            d = n - timedelta(days=1)
            datetime_api_url = 'http://radiko.jp/v3/program/date/{}/{}.xml'.format(d.strftime('%Y%m%d'), self.area_id)
            r = requests.get(url=datetime_api_url)
            if r.status_code == 200:
                channels_xml = r.content
                tree = ET.fromstring(channels_xml)
                station = tree.find('.//station[@id="{}"]'.format(self.station_id))
                prog = station.find('.//prog[@ft="{}"]'.format(self.ft))
                to = prog.attrib['to']

        self.title = prog.find('.//title').text.replace(' ', '_').replace('　', '_')

    def setup(self):
        self.set_basic_info()
        self.authenticate()
        self.set_area_id()
        self.set_title()
    
    def download(self):
        self.setup()
        
        cmd = (
            'ffmpeg '
            '-loglevel fatal '
            '-n -headers "X-Radiko-AuthToken: {}" '
            '-i "{}" '
            '-vn -acodec copy "{}.aac"'.format(
                self.auth_token,
                self.stream_url,
                self.ft[:8] + ' - ' + self.title
            )
        )
        print('Downloading {}.aac... '.format(self.title), end='')
        self.spinner.start()
        subprocess.call(cmd, shell=True)
        self.spinner.stop()
        print('done!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('url')
    args = parser.parse_args()
    
    url = args.url
    radiko = Radiko(url)
    radiko.download()
