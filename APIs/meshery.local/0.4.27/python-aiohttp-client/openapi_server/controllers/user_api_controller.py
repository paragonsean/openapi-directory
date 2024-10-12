from typing import List, Dict
from aiohttp import web

from openapi_server.models.performance_test_config import PerformanceTestConfig
from openapi_server.models.preference import Preference
from openapi_server import util


async def id_delete_load_preferences(request: web.Request, uuid=None) -> web.Response:
    """Handle DELETE request for load test preferences

    Used for deleting load test preferences

    :param uuid: 
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def id_get_load_preferences(request: web.Request, uuid=None) -> web.Response:
    """Handle GET request for load test preferences

    Used for fetching load test preferences

    :param uuid: 
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def id_get_token_provider(request: web.Request, ) -> web.Response:
    """Handle GET request for tokens

    Returns token from the actual provider in a file resposese: 200:


    """
    return web.Response(status=200)


async def id_get_user_login(request: web.Request, ) -> web.Response:
    """Handlers GET request for User login

    Redirects user for auth or issues session


    """
    return web.Response(status=200)


async def id_get_user_logout(request: web.Request, ) -> web.Response:
    """Handlers GET request for User logout

    Redirects user for auth or issues session


    """
    return web.Response(status=200)


async def id_get_user_test_prefs(request: web.Request, ) -> web.Response:
    """Handle GET for User Load Test Preferences

    Returns User Load Test Preferences


    """
    return web.Response(status=200)


async def id_post_load_preferences(request: web.Request, body=None) -> web.Response:
    """Handle POST request for load test preferences

    Used for persisting load test preferences

    :param body: 
    :type body: dict | bytes

    """
    body = PerformanceTestConfig.from_dict(body)
    return web.Response(status=200)


async def id_post_token_provider(request: web.Request, ) -> web.Response:
    """Handle POST request for tokens

    Receives token from the actual provider resposese: 200:


    """
    return web.Response(status=200)


async def id_post_user_test_prefs(request: web.Request, ) -> web.Response:
    """Handle GET for User Load Test Preferences

    Updates User Load Test Preferences


    """
    return web.Response(status=200)
