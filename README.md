# Configurations #

if you are using [heroku's foreman](https://devcenter.heroku.com/articles/procfile) you should add your google docs credentials that is 

    GDOCS_USERNAME=example@gmail.com
    GDOCS_PASSWORD=examplepassword
    GDOCS_META_SHEET=spreadsheet_key

respectively.

if not, you should config the default value in `config.py`

# Examples #


## curl ##

    now=`date +"%m-%d-%y|%H:%M"

    curl -d "machine=temperature-sensor&time=$now&temp=20.00&humid=30.00" http://localhost:5000/endpoint


# Getting started? #

1. install [foreman](https://github.com/ddollar/foreman)
2. foreman start
3. enjoy!