import os
from utils import file_path
from typing import Literal
from dotenv import load_dotenv, find_dotenv
import utils
import dotenv

context: Literal['bstack', 'local_real', 'local_emulator'] = os.getenv('context', 'local_real')

load_dotenv(find_dotenv(f'.env.{context}'))

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723/')
udid = os.getenv('udid', 'd6ae07b4')

options_local={
        'app': file_path.abs_path_from_project('app-alpha-universal-release.apk'),
        'appWaitActivity': 'org.wikipedia.*',
        'udid': udid
    }

options_bs={
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://ce6db1b9b9e83c1c736280ed028d9c05cb88fe98",
        'bstack:options': {
            "projectName": "Mobile Tests Lesson 22",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack android_test",
            "userName": f'{login}',
            "accessKey": f'{password}'
        }
    }
if context == 'bstack' :
    options_cfg=options_bs
else :
    options_cfg=options_local