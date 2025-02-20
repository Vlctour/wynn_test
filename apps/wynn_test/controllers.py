"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.url_signer import URLSigner
from .models import get_user_email
import requests

url_signer = URLSigner(session)
user_uuid = '47259efb-0900-419a-a76c-fdc95c0a2ddf'

@action('index')
@action.uses('index.html', db, auth, url_signer)
def index():
    return dict(
        # COMPLETE: return here any signed URLs you need.
        my_callback_url = URL('my_callback', signer=url_signer),
        wynn_call_url = URL('wynn_call'),
        get_head_url = URL('get_head'),
    )

@action('my_callback')
@action.uses() # Add here things like db, auth, etc.
def my_callback():
    # The return value should be a dictionary that will be sent as JSON.
    return dict(my_value=3)

@action('wynn_call', method='GET')
@action.uses()
def wynn_call():
    test_url = f"https://api.wynncraft.com/v3/player/{user_uuid}"
    response = requests.get(test_url)
    data=None
    if response and response.status_code == 200:
        data=response.json()
        # print("testing prints")
        # print("name is:", data)
    else:
        print("ERROR in wynn call api")
    return dict(player=data)

@action('get_head', method='GET')
@action.uses()
def get_head():
    # url = f"https://mc-heads.net/head/{user_uuid}"
    # response = requests.get(url)
    # data=None
    # if response and response.status_code == 200:
    #     data=response.json()['url']
    # else:
    #     print("ERROR getting player head")
    # return dict(head=data)
    return dict(head=None)