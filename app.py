"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, jsonify, current_app
from functools import wraps
from google_spreadsheet.api import SpreadsheetAPI


################
## Decorators ##
################
def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            print func(*args, **kwargs).data
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)

    return decorated_function


##################
## app function ##
##################
def update_metadata(app):
    worksheet = app.spreadsheet_api.get_worksheet(app.config['GDOCS_KEYS_OF_METASHEET'] , 'od6')

    meta_sheet = dict()
    for r in worksheet.get_rows():
        meta_sheet[r['machine']] = r

    app.meta_sheet = meta_sheet


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.spreadsheet_api = SpreadsheetAPI(app.config['GDOCS_USERNAME'], app.config['GDOCS_PASSWORD'], 'http://localhost')

    update_metadata(app)

    return {'app': app}


######################
## INIT APPLICATION ##
######################
appInstance = create_app('conf.Config')

app = appInstance['app']
# database = appInstance['database']


########################
# Before request Hooks #
########################
@app.before_first_request
def nat():
    app.spreadsheet_api = SpreadsheetAPI(app.config['GDOCS_USERNAME'], app.config['GDOCS_PASSWORD'], 'http://localhost')


@app.before_request
def before_request():
    app.spreadsheet_key = request.args.get('spreadsheet_key', app.config['GDOCS_FALLBACK_SHEET_KEY'])
    app.worksheet_key = request.args.get('worksheet_key', 'od6')


##################################
# Routing for your application.  #
##################################

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/sheets')
@jsonp
def get_data():
    api = app.spreadsheet_api

    worksheet = api.get_worksheet(app.spreadsheet_key, app.worksheet_key)
    worksheets = [sheet[1] for sheet in api.list_worksheets(app.spreadsheet_key)]

    rows = worksheet.get_rows()
    output = dict(data=rows, meta=request.args, worksheets=worksheets)

    return jsonify(output)


@app.route('/debug', methods=['POST', 'GET'])
def debug():
    if request.method == 'POST':
        return jsonify(request.form)
    else:
        return jsonify(request.args)

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
