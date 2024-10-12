from typing import List, Dict
from aiohttp import web

from openapi_server.models.keys_api_find200_response import KeysApiFind200Response
from openapi_server.models.products_api_count200_response import ProductsApiCount200Response
from openapi_server.models.products_api_find_request import ProductsApiFindRequest
from openapi_server.models.subscription_view import SubscriptionView
from openapi_server.models.subscriptions_api_count_request import SubscriptionsApiCountRequest
from openapi_server.models.subscriptions_api_find200_response import SubscriptionsApiFind200Response
from openapi_server.models.subscriptions_api_put_subscription_request import SubscriptionsApiPutSubscriptionRequest
from openapi_server import util


async def subscriptions_api_count(request: web.Request, body) -> web.Response:
    """subscriptions_api_count

    

    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionsApiCountRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_delete_subscription(request: web.Request, x_api_key, serial, keep) -> web.Response:
    """subscriptions_api_delete_subscription

    

    :param x_api_key: 
    :type x_api_key: str
    :param serial: 
    :type serial: str
    :param keep: 
    :type keep: bool

    """
    return web.Response(status=200)


async def subscriptions_api_delete_subscription2(request: web.Request, x_api_key, serial, keep) -> web.Response:
    """subscriptions_api_delete_subscription2

    

    :param x_api_key: 
    :type x_api_key: str
    :param serial: 
    :type serial: str
    :param keep: 
    :type keep: bool

    """
    return web.Response(status=200)


async def subscriptions_api_disable(request: web.Request, body) -> web.Response:
    """subscriptions_api_disable

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiFindRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_disable2(request: web.Request, body) -> web.Response:
    """subscriptions_api_disable2

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiFindRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_enable(request: web.Request, body) -> web.Response:
    """subscriptions_api_enable

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiFindRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_enable2(request: web.Request, body) -> web.Response:
    """subscriptions_api_enable2

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiFindRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_find(request: web.Request, body) -> web.Response:
    """subscriptions_api_find

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiFindRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_list(request: web.Request, body, page=None) -> web.Response:
    """subscriptions_api_list

    

    :param body: 
    :type body: dict | bytes
    :param page: 
    :type page: int

    """
    body = ProductsApiFindRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_put_subscription(request: web.Request, body) -> web.Response:
    """subscriptions_api_put_subscription

    

    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionsApiPutSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_put_subscription2(request: web.Request, body) -> web.Response:
    """subscriptions_api_put_subscription2

    

    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionsApiPutSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def subscriptions_api_save(request: web.Request, body) -> web.Response:
    """subscriptions_api_save

    

    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionsApiPutSubscriptionRequest.from_dict(body)
    return web.Response(status=200)
