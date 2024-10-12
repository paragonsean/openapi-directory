from typing import List, Dict
from aiohttp import web

from openapi_server.models.extended_subscription_response_model import ExtendedSubscriptionResponseModel
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.user_response_model import UserResponseModel
from openapi_server import util


async def get_user_info_v1_user_get(request: web.Request, xi_api_key=None) -> web.Response:
    """Get User Info

    Gets information about the user

    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)


async def get_user_subscription_info_v1_user_subscription_get(request: web.Request, xi_api_key=None) -> web.Response:
    """Get User Subscription Info

    Gets extended information about the users subscription

    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)
