import os

class Config(object):
    DEBUG            = True
    LOG_LEVEL        = os.environ.get('LOG_LEVEL', 'DEBUG')
    APP_VERSION      = 0.2
    GDOCS_USERNAME   = os.environ.get('GDOCS_USERNAME')   or ""
    GDOCS_PASSWORD   = os.environ.get('GDOCS_PASSWORD')   or ""
    GDOCS_META_SHEET = os.environ.get('GDOCS_META_SHEET') or ""
