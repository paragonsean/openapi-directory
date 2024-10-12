from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def login_and_get_bearer_token(request: web.Request, email=None, password=None) -> web.Response:
    """Login and get bearer token

    Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

    :param email: The same email you use for our platform.
    :type email: str
    :param password: The password email you use for our platform.
    :type password: str

    """
    return web.Response(status=200)


async def logout(request: web.Request, email=None) -> web.Response:
    """Logout

    Once you are done, call this endpoint to lock your account!

    :param email: The same email you use for our platform.
    :type email: str

    """
    return web.Response(status=200)


async def register(request: web.Request, first_name=None, last_name=None, company_name=None, shop_url=None, email=None, store_name=None, store_url=None, password=None, fromuser=None) -> web.Response:
    """Register

    Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

    :param first_name: required
    :type first_name: str
    :param last_name: required
    :type last_name: str
    :param company_name: required
    :type company_name: str
    :param shop_url: required
    :type shop_url: str
    :param email: required
    :type email: str
    :param store_name: required
    :type store_name: str
    :param store_url: required
    :type store_url: str
    :param password: required
    :type password: str
    :param fromuser: required (always 1)
    :type fromuser: str

    """
    return web.Response(status=200)


async def register_and_create_store_connection_for_woo_commerce(request: web.Request, first_name=None, last_name=None, company_name=None, shop_url=None, email=None, store_name=None, store_url=None, password=None, fromuser=None, api_url=None, consumer_key=None, consumer_secret=None) -> web.Response:
    """Register and Create Store Connection for WooCommerce

    Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

    :param first_name: required
    :type first_name: str
    :param last_name: required
    :type last_name: str
    :param company_name: required
    :type company_name: str
    :param shop_url: required
    :type shop_url: str
    :param email: required
    :type email: str
    :param store_name: required
    :type store_name: str
    :param store_url: required
    :type store_url: str
    :param password: required
    :type password: str
    :param fromuser: required (always 1)
    :type fromuser: str
    :param api_url: required
    :type api_url: str
    :param consumer_key: required
    :type consumer_key: str
    :param consumer_secret: required
    :type consumer_secret: str

    """
    return web.Response(status=200)
