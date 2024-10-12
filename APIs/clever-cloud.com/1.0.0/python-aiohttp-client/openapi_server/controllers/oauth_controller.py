from typing import List, Dict
from aiohttp import web

from openapi_server.models.rights import Rights
from openapi_server import util


async def get_oauth_authorize_0(request: web.Request, oauth_token=None, cookie=None) -> web.Response:
    """get_oauth_authorize_0

    

    :param oauth_token: 
    :type oauth_token: str
    :param cookie: 
    :type cookie: str

    """
    return web.Response(status=200)


async def get_oauth_rights_0(request: web.Request, ) -> web.Response:
    """get_oauth_rights_0

    


    """
    return web.Response(status=200)


async def oauth_access_token_query_post_0(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """oauth_access_token_query_post_0

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)


async def oauth_request_token_query_post_0(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """oauth_request_token_query_post_0

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)


async def post_oauth_access_token_0(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """post_oauth_access_token_0

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)


async def post_oauth_authorize_0(request: web.Request, almighty=None, access_organisations=None, manage_organisations=None, manage_organisations_services=None, manage_organisations_applications=None, manage_organisations_members=None, access_organisations_bills=None, access_organisations_credit_count=None, access_organisations_consumption_statistics=None, access_personal_information=None, manage_personal_information=None, manage_ssh_keys=None, manage_services=None, manage_applications=None, access_bills=None, access_credit_count=None, access_consumption_statistics=None, cookie=None) -> web.Response:
    """post_oauth_authorize_0

    

    :param almighty: 
    :type almighty: str
    :param access_organisations: 
    :type access_organisations: str
    :param manage_organisations: 
    :type manage_organisations: str
    :param manage_organisations_services: 
    :type manage_organisations_services: str
    :param manage_organisations_applications: 
    :type manage_organisations_applications: str
    :param manage_organisations_members: 
    :type manage_organisations_members: str
    :param access_organisations_bills: 
    :type access_organisations_bills: str
    :param access_organisations_credit_count: 
    :type access_organisations_credit_count: str
    :param access_organisations_consumption_statistics: 
    :type access_organisations_consumption_statistics: str
    :param access_personal_information: 
    :type access_personal_information: str
    :param manage_personal_information: 
    :type manage_personal_information: str
    :param manage_ssh_keys: 
    :type manage_ssh_keys: str
    :param manage_services: 
    :type manage_services: str
    :param manage_applications: 
    :type manage_applications: str
    :param access_bills: 
    :type access_bills: str
    :param access_credit_count: 
    :type access_credit_count: str
    :param access_consumption_statistics: 
    :type access_consumption_statistics: str
    :param cookie: 
    :type cookie: str

    """
    return web.Response(status=200)


async def post_oauth_request_token_0(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """post_oauth_request_token_0

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)
