from typing import List, Dict
from aiohttp import web

from openapi_server.models.additemsubscription_group_id_request import AdditemsubscriptionGroupIdRequest
from openapi_server.models.insert_addressesbygroup_id_request import InsertAddressesbygroupIdRequest
from openapi_server.models.update_subscriptionbygroup_id_request import UpdateSubscriptionbygroupIdRequest
from openapi_server import util


async def additemsubscription_group_id(request: web.Request, group_id, accept, content_type, body) -> web.Response:
    """Add Subscription item by groupId

    Adds an SKU to a given Subscription, filtering by groupId.

    :param group_id: Group ID.
    :type group_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AdditemsubscriptionGroupIdRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_subscriptionbygroup_id(request: web.Request, accept, content_type, group_id) -> web.Response:
    """Cancel Subscription by groupId

    Cancels Subscription by &#x60;groupId&#x60;

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def get_allsubscriptiongroup(request: web.Request, content_type, accept) -> web.Response:
    """List All subscription groups

    Retrieves all subscription groups in your store.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def get_configsubscriptionsgroup(request: web.Request, content_type, accept, group_id) -> web.Response:
    """List Subscription group&#39;s Configuration

    Retrieves details about a given subscription group&#39;s configuration, filtering by groupId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def get_conversation_messagebygroup_id(request: web.Request, content_type, accept, group_id) -> web.Response:
    """Get Conversation Message by groupId

    Retrieves the conversation of a given Subscription group, filtering by groupId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def get_nextpurchase(request: web.Request, content_type, accept, date_str) -> web.Response:
    """Get Next purchase

    Lists details of a given subscription group&#39;s next purchase, filtering by dateStr.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param date_str: Reference date that retrieves all next purchases, starting from the dateStr inserted. Must be in the format of {{yyyyMMdd}}
    :type date_str: str

    """
    return web.Response(status=200)


async def get_simulatebysubscription_group(request: web.Request, content_type, accept, group_id) -> web.Response:
    """Get Simulation by subscription-group

    Retrieves Subscription simulations, filtering by groupId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def get_subscriptionbygroup_id(request: web.Request, content_type, accept, group_id) -> web.Response:
    """Get Subscription by groupId

    Lists Subscription details, filtering by &#x60;groupId&#x60;.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def getaddressesbygroup_id(request: web.Request, content_type, accept, group_id) -> web.Response:
    """Get addresses by groupId

    Lists addresses linked to a given Subscription group, filtering by groupId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def getfrequencyoptionsbygroup_id(request: web.Request, content_type, accept, group_id) -> web.Response:
    """Get frequency options by groupId

    Lists frequency options of a given Subscription group, filtering by groupId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def getpayment_systembygroup_id(request: web.Request, content_type, accept, group_id) -> web.Response:
    """Get payment System by groupId

    Retrieves payment system&#39;s information of a given Subscription group, filtering by groupId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def getsubscriptiongrouplist(request: web.Request, content_type, accept) -> web.Response:
    """Get subscription group list

    Retrieves a list of Subscription groups in your store.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def getwillcreatebygroup_id(request: web.Request, content_type, accept, group_id) -> web.Response:
    """List &#39;Will create&#39; by groupId

    Retrieves Subscription groups listed as &#39;will create&#39;, filtering by groupId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param group_id: Group ID.
    :type group_id: str

    """
    return web.Response(status=200)


async def insert_addressesbygroup_id(request: web.Request, group_id, accept, content_type, body) -> web.Response:
    """Insert Addresses by groupId

    Insert address information of a given Subscription group, filtering by groupId.

    :param group_id: Group ID.
    :type group_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = InsertAddressesbygroupIdRequest.from_dict(body)
    return web.Response(status=200)


async def retrysubscriptionbygroup_id(request: web.Request, groupid, instance_id, accept, content_type) -> web.Response:
    """Retry subscription by groupId

    Permits the retry of a Subscription group, via API, filtering by groupId and instanceId.

    :param groupid: Group ID.
    :type groupid: str
    :param instance_id: Instance ID.
    :type instance_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def update_subscriptionbygroup_id(request: web.Request, group_id, body) -> web.Response:
    """Update Subscription by groupId

    Updates a Subscription by &#x60;groupId&#x60;.

    :param group_id: Group ID.
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSubscriptionbygroupIdRequest.from_dict(body)
    return web.Response(status=200)
