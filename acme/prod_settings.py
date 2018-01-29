import dj_database_url
from .settings import *
DEBUG = False
TEMPLATE_DEBUG = False

DATABASE['default'] = dj_database_url.config()


SECRET_KEY = '2g5_c8vsy4r%_snk0u6z@lk)f##k_fu(p2)iqv=(@fsl5cqc!*'

ALLOWED_HOSTS = ['lyd-acme.herokuapp.com']