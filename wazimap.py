# pull in the default wazimap settings
from wazimap.settings import *  #NOQA

# install this app before Wazimap
INSTALLED_APPS = ['wazimap_ex'] + INSTALLED_APPS

WAZIMAP['name'] = 'Wazimap Example'

WAZIMAP['url'] = 'http://wazimap.example.com'
WAZIMAP['country_code'] = 'EX'
