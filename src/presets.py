#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate default config"""

import os
from os import path
import textwrap

from .helpers import FilesHelper, FoldersHelper


IMAGEFILES = [
    'favicon_ico_16px.ico',
    'favicon_png_1600px.png',
    'favicon_svg_scalable.svg',
    'preview_png_500px.png',
]


class Presets:
    """Generate presets"""
    args = lambda: None
    args.preset = ''
    info = {}

    def assets(self):
        """Generate images files to attach to the preset settings"""
        realpath = path.join(path.dirname(path.realpath(__file__)), 'assets')
        destination_folder = ''.join(self.args.preset.split('/')[0:-1])
        for filename in IMAGEFILES:
            filepath = path.join(realpath, filename)
            destination = path.join(destination_folder, filename)
            FilesHelper.copy_file(filepath, destination)

    def settings(self):
        """Generate config file in indented JSON format"""
        string = textwrap.dedent(f"""\
            {{
                'comment':  {{
                    'About':            '{('Config file used by python '
                                           'cushead CLI')}',
                    'Format':           'JSON',
                    'Git':              '{self.info['source']}',
                    'Documentation':    '{self.info['documentation']}'
                }},
                'required': {{
                    'static_url':       '/static/'
                }},
                'recommended': {{
                    'favicon_ico':      './favicon_ico_16px.ico',
                    'favicon_png':      './favicon_png_1600px.png',
                    'favicon_svg':      './favicon_svg_scalable.svg',
                    'preview_png':      './preview_png_500px.png'
                }},
                'default': {{
                    'general': {{
                        'content-type':     'text/html; charset=utf-8',
                        'X-UA-Compatible':  'ie=edge',
                        'viewport':         '{('width=device-width, '
                                               'initial-scale=1')}',
                        'language':         'en',
                        'territory':        'US',
                        'clean_url':        'microsoft.com',
                        'protocol':         'https://',
                        'robots':           'index, follow'
                    }},
                    'basic': {{
                        'title':            'Microsoft',
                        'description':      'Technology Solutions',
                        'subject':          'Home Page',
                        'keywords':         'Microsoft, Windows',
                        'background_color': '#0000FF',
                        'author':           'Lucas Vazquez'
                    }},
                    'social_media': {{
                        'facebook_app_id':  '123456',
                        'twitter_user_@':   '@Microsoft',
                        'twitter_user_id':  '123456'
                    }}
                }},
                'progressive_web_apps': {{
                    'dir':              'ltr',
                    'start_url':        '/',
                    'orientation':      'landscape',
                    'scope':            '/',
                    'display':          'browser',
                    'platform':        'web',
                    'applications':     [
                        {{
                            'platform':     'play',
                            'url':          '{('https://play.google.com/store/'
                                               'apps/details?id=com.example'
                                               '.app')}',
                            'id':           'com.example.app'
                        }},
                        {{
                            'platform':     'itunes',
                            'url':          '{('https://itunes.apple.com/app/'
                                            'example-app/id123456')}'
                        }}
                    ]
                }}
            }}""")
        string = string.replace('\'', '"')
        folderpath = path.dirname(self.args.preset)
        FoldersHelper.create_folder(folderpath)
        FilesHelper.write_file(self.args.preset, string)
