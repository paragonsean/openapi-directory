from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_rns_pub_subscriptions_subscription_id_conversation_message_get200_response_inner import ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner
from openapi_server.models.simulate_response_vo import SimulateResponseVO
from openapi_server.models.subscription_group_request import SubscriptionGroupRequest
from openapi_server.models.subscription_group_response import SubscriptionGroupResponse
from openapi_server.models.subscription_thin_item_request import SubscriptionThinItemRequest
from openapi_server.models.subscription_update_request_v3 import SubscriptionUpdateRequestV3
from openapi_server.models.update_item_input import UpdateItemInput
from openapi_server import util


async def api_rns_pub_subscriptions_get(request: web.Request, content_type, accept, customer_email=None, status=None, address_id=None, payment_id=None, plan_id=None, next_purchase_date=None, original_order_id=None, page=None, size=None) -> web.Response:
    """List subscriptions

    List subscriptions filtering by some arguments.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param customer_email: Customer that owns the subscription. Defaults to the current logged user.
    :type customer_email: str
    :param status: Current subscription status
    :type status: str
    :param address_id: Id from the address used as shipping address
    :type address_id: str
    :param payment_id: Id from the payment used as payment method
    :type payment_id: str
    :param plan_id: Id from the plan that the subscription belongs to
    :type plan_id: str
    :param next_purchase_date: Date for the next cycle
    :type next_purchase_date: str
    :param original_order_id: Id from the order that generated the subscription
    :type original_order_id: str
    :param page: Page used for pagination
    :type page: int
    :param size: Page size used for pagination
    :type size: int

    """
    return web.Response(status=200)


async def api_rns_pub_subscriptions_id_get(request: web.Request, id, content_type, accept) -> web.Response:
    """Get subscription details

    Retrieve a specific subscription by its ID.

    :param id: ID from the target subscription.
    :type id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_rns_pub_subscriptions_id_items_item_id_delete(request: web.Request, id, item_id, content_type, accept) -> web.Response:
    """Remove items from a subscription.

    Removes a specific item from a given subscription

    :param id: Id from the target subscription
    :type id: str
    :param item_id: Id from the subscription item that will be removed
    :type item_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_rns_pub_subscriptions_id_items_item_id_patch(request: web.Request, id, item_id, content_type, accept, body=None) -> web.Response:
    """Edit items on a subscription.

    Edit a given item on a specific subscription

    :param id: Id from the target subscription
    :type id: str
    :param item_id: Id from the target item
    :type item_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateItemInput.from_dict(body)
    return web.Response(status=200)


async def api_rns_pub_subscriptions_id_items_post(request: web.Request, id, content_type, accept, body=None) -> web.Response:
    """Add item to subscription

    Add a new item to a given subscription.

    :param id: ID from the target subscription
    :type id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionThinItemRequest.from_dict(body)
    return web.Response(status=200)


async def api_rns_pub_subscriptions_id_patch(request: web.Request, id, content_type, accept, body=None) -> web.Response:
    """Update subscription

    Update a specific subscription.

    :param id: ID from the given subscription.
    :type id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionUpdateRequestV3.from_dict(body)
    return web.Response(status=200)


async def api_rns_pub_subscriptions_id_simulate_post(request: web.Request, id, content_type, accept) -> web.Response:
    """Calculate the current prices for a specific subscription

    Simulates an order made by the specific subscription on checkout and retrieves the current price for items and shipping.

    :param id: Id from the target subscription
    :type id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_rns_pub_subscriptions_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create subscription

    Create a new subscription.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionGroupRequest.from_dict(body)
    return web.Response(status=200)


async def api_rns_pub_subscriptions_simulate_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Calculate the current prices for the provided subscription template

    Simulates an order made by subscriptions on checkout and retrieves the current price for items and shipping.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionGroupRequest.from_dict(body)
    return web.Response(status=200)


async def api_rns_pub_subscriptions_subscription_id_conversation_message_get(request: web.Request, subscription_id, content_type, accept) -> web.Response:
    """Get conversation messages

    Retrieve all conversation messages sent to a customer regarding a given subscription.

    :param subscription_id: ID of the subscription.
    :type subscription_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
