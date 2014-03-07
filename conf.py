import os

class Config(object):
    DEBUG = True
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')

    GDOCS_USERNAME = os.environ.get('GDOCS_USERNAME') or "nat.wrw@gmail.com"
    GDOCS_PASSWORD = os.environ.get('GDOCS_PASSWORD') or "yxafbjpgqidckxpc"
    GDOCS_FALLBACK_SHEET_KEY = os.environ.get("GDOCS_FALLBACK_SHEET_KEY") or "0Av03mDBecdQEdHlMWXZqV01MV3RZb0J0ejJIaFRFbkE"
    GDOCS_KEYS_OF_METASHEET = os.environ.get('GDOCS_KEYS_OF_METASHEET') or "0Av03mDBecdQEdHlMWXZqV01MV3RZb0J0ejJIaFRFbkE"
