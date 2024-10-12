from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.key import Key
from openapi_server.models.transaction_id import TransactionId
from openapi_server import util


async def delete_github_link_0(request: web.Request, ) -> web.Response:
    """delete_github_link_0

    


    """
    return web.Response(status=200)


async def get_github_0(request: web.Request, ) -> web.Response:
    """get_github_0

    


    """
    return web.Response(status=200)


async def get_github_applications_1(request: web.Request, ) -> web.Response:
    """get_github_applications_1

    


    """
    return web.Response(status=200)


async def get_github_callback_0(request: web.Request, code=None, state=None, error=None, error_description=None, error_uri=None, cookie=None) -> web.Response:
    """get_github_callback_0

    

    :param code: 
    :type code: str
    :param state: 
    :type state: str
    :param error: 
    :type error: str
    :param error_description: 
    :type error_description: str
    :param error_uri: 
    :type error_uri: str
    :param cookie: 
    :type cookie: str

    """
    return web.Response(status=200)


async def get_github_emails_0(request: web.Request, ) -> web.Response:
    """get_github_emails_0

    


    """
    return web.Response(status=200)


async def get_github_keys_0(request: web.Request, ) -> web.Response:
    """get_github_keys_0

    


    """
    return web.Response(status=200)


async def get_github_link_0(request: web.Request, transaction_id=None, redirect_url=None) -> web.Response:
    """get_github_link_0

    

    :param transaction_id: From GET /github
    :type transaction_id: str
    :param redirect_url: 
    :type redirect_url: str

    """
    return web.Response(status=200)


async def get_github_login_0(request: web.Request, redirect_url=None, from_authorize=None) -> web.Response:
    """get_github_login_0

    

    :param redirect_url: 
    :type redirect_url: str
    :param from_authorize: 
    :type from_authorize: str

    """
    return web.Response(status=200)


async def get_github_signup_0(request: web.Request, redirect_url=None, from_authorize=None) -> web.Response:
    """get_github_signup_0

    

    :param redirect_url: 
    :type redirect_url: str
    :param from_authorize: 
    :type from_authorize: str

    """
    return web.Response(status=200)


async def get_github_username_0(request: web.Request, ) -> web.Response:
    """get_github_username_0

    


    """
    return web.Response(status=200)


async def post_github_redeploy_0(request: web.Request, user_agent=None, x_github_event=None, x_hub_signature=None) -> web.Response:
    """post_github_redeploy_0

    

    :param user_agent: 
    :type user_agent: str
    :param x_github_event: 
    :type x_github_event: str
    :param x_hub_signature: 
    :type x_hub_signature: str

    """
    return web.Response(status=200)


async def post_github_signup_0(request: web.Request, transaction_id=None, name=None, other_id=None, other_email=None, password=None, auto_link=None, terms=None) -> web.Response:
    """post_github_signup_0

    

    :param transaction_id: 
    :type transaction_id: str
    :param name: 
    :type name: str
    :param other_id: 
    :type other_id: str
    :param other_email: 
    :type other_email: str
    :param password: 
    :type password: str
    :param auto_link: 
    :type auto_link: str
    :param terms: 
    :type terms: str

    """
    return web.Response(status=200)
