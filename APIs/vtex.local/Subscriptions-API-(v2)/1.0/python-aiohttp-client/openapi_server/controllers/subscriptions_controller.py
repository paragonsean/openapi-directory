from typing import List, Dict
from aiohttp import web

from openapi_server.models.insert_addressesfor_subscription_request import InsertAddressesforSubscriptionRequest
from openapi_server.models.update_subscriptionsby_subscription_id_request import UpdateSubscriptionsbySubscriptionIdRequest
from openapi_server import util


async def cancel_subscriptionsby_subscription_id(request: web.Request, accept, content_type, subscription_id) -> web.Response:
    """Cancel Subscriptions by SubscriptionId

    Cancels all Subscriptions of a subscription group. This operation does not have a rollback. Once cancelled, it cannot be re-activated

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param subscription_id: Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def get_subscription_list(request: web.Request, content_type, accept) -> web.Response:
    """Get Subscription List

    Retrieves a list of Subscriptions linked to your store.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def getfrequencyoptionsbysubscription_id(request: web.Request, content_type, accept, subscription_id) -> web.Response:
    """Get frequency options by subscriptionId

    Lists frequency options for the Subscription, filtering by &#x60;subscriptionId&#x60;.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param subscription_id: Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def getsubscriptionby_id(request: web.Request, content_type, accept, subscription_id) -> web.Response:
    """Retrieve subscription by ID

    Lists Subscription&#39;s details, searching by &#x60;subscriptionId&#x60;.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param subscription_id: Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def getsubscriptionstocustomer(request: web.Request, customer_id, content_type, accept) -> web.Response:
    """Retrieve customer&#39;s subscriptions

    Retrieves details of a given customer&#39;s subscriptions, searching by that customer&#39;s &#x60;customerId&#x60;.

    :param customer_id: Customer ID.
    :type customer_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def insert_addressesfor_subscription(request: web.Request, subscription_id, content_type, accept, body) -> web.Response:
    """Insert Addresses for Subscription

    Inserts address&#39;s information to complement the Subscription details.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: list | bytes

    """
    body = [InsertAddressesforSubscriptionRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_subscriptionsby_subscription_id(request: web.Request, subscription_id, content_type, accept, body) -> web.Response:
    """Update Subscriptions by SubscriptionId

    Update, add or alter information of a given Subscription, filtering by &#x60;subscriptionId&#x60;.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSubscriptionsbySubscriptionIdRequest.from_dict(body)
    return web.Response(status=200)
