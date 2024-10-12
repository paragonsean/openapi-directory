from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_subscription_request import ActivateSubscriptionRequest
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.create_subscription_request import CreateSubscriptionRequest
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.subscription_index import SubscriptionIndex
from openapi_server.models.subscription_push_reporting import SubscriptionPushReporting
from openapi_server import util


async def activate_subscription(request: web.Request, id, body=None) -> web.Response:
    """Activate a subscription to the orders

    At this moment, BeezUP will ensure that your callback url is respecting this specification:  - https://api.beezup.com/swaggerhub/apis/BeezUP/public_marketplaces_orders_subscriptions_consumer-dev/1.0#/Subscriptions/Verification  After that we will send you the orders related to your subscription, respecting this specification:  - https://api.beezup.com/swaggerhub/apis/BeezUP/public_marketplaces_orders_subscriptions_consumer-dev/1.0#/Subscriptions/PushOrders 

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActivateSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def create_subscription(request: web.Request, id, body) -> web.Response:
    """Creates a subscription to the orders

    Please take a look at this sequence diagram to understand the subscription process to follow [here](https://www.websequencediagrams.com/files/render?link&#x3D;SBYbeIc8NGshk6ooCbmjoBLIMl4fIGO1xjJbPBQAglBo0n6BwEReh7NXQiPSjOTX)

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_subscription(request: web.Request, id) -> web.Response:
    """Deactivate a subscription to the orders

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_subscription(request: web.Request, id) -> web.Response:
    """Delete a subscription to the orders

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_subscription(request: web.Request, id) -> web.Response:
    """Get a subscription to the orders

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_subscription_list(request: web.Request, ) -> web.Response:
    """Get the subscription list

    


    """
    return web.Response(status=200)


async def get_subscription_push_reporting(request: web.Request, id, page_number=None, page_size=None) -> web.Response:
    """Get the push reporting related to this subscription

    

    :param id: 
    :type id: str
    :param page_number: 
    :type page_number: int
    :param page_size: 
    :type page_size: int

    """
    return web.Response(status=200)


async def retry_push_orders(request: web.Request, id) -> web.Response:
    """Force retry push orders immediatly

    In case your subscription consumption is unavailable and your subscription is still active you can ask to retry immediatly to push orders instead of waiting the next scheduled retry date

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
