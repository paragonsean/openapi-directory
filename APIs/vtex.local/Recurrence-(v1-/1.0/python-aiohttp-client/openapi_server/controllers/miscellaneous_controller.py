from typing import List, Dict
from aiohttp import web

from openapi_server.models.addrecurrenceitem_request import AddrecurrenceitemRequest
from openapi_server.models.reindexrecurrence_request import ReindexrecurrenceRequest
from openapi_server.models.updatepartialrecurrence_request import UpdatepartialrecurrenceRequest
from openapi_server.models.updaterecurrence_request import UpdaterecurrenceRequest
from openapi_server.models.updaterecurrencesettings_request import UpdaterecurrencesettingsRequest
from openapi_server import util


async def addrecurrenceitem(request: web.Request, content_type, accept, recurrence_id, body) -> web.Response:
    """Add Subscription item

    Adds an item to a Subscription (formerly Recurrence).

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param recurrence_id: 
    :type recurrence_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [AddrecurrenceitemRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def get_recurrencebyemail(request: web.Request, content_type, accept, email=None, cycle_status=None) -> web.Response:
    """Get Subscriptions

    Retrieves a given Subscription (formerly recurrence). There are three options of filtering your Subscruptions v1. It&#39;s possible to get a list of all Subscriptions v1, by not adding any query params to your request, and simply executing a call to the url. It is also possible to list the Subscriptions by email, filtering by the email query param. And finnally, it is possible to list recurrences with failures on the last execution cycle, filtering by the cycleStatus query param.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param email: If you wish to list tasks by email, insert the desired user&#39;s email.
    :type email: str
    :param cycle_status: If you wish to list tasks by Subscriptions with failures on the last execution cycle, insert the desired cycleStatus.
    :type cycle_status: str

    """
    return web.Response(status=200)


async def get_recurrencebyrecurrence_id(request: web.Request, content_type, accept, recurrence_id) -> web.Response:
    """Get Subscription by recurrenceId

    Retrieves a given Subscription (formerly recurrence) by recurrenceId.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param recurrence_id: 
    :type recurrence_id: str

    """
    return web.Response(status=200)


async def getpaymentaccounts(request: web.Request, recurrenceid, content_type, accept) -> web.Response:
    """Get payment accounts

    Lists payment accounts of a given Subscription (formerly Recurrence) by recurrenceId.

    :param recurrenceid: 
    :type recurrenceid: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def getrecurrenceaddresses(request: web.Request, content_type, accept, recurrence_id) -> web.Response:
    """Get Subscription addresses

    Retrieves the addresses attached to a given subscription (formerly recurrence) by recurrenceId.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param recurrence_id: 
    :type recurrence_id: str

    """
    return web.Response(status=200)


async def getrecurrencesettings(request: web.Request, content_type, accept) -> web.Response:
    """Get Subscription settings

    Retrieves your store&#39;s Subscriptions&#39; (formerly recurrence) settings.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def getselfrecurrence(request: web.Request, content_type, accept) -> web.Response:
    """Get self Subscription

    Lists details of your self Subscription (formerly Recurrence).

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def reindexrecurrence(request: web.Request, recurrence_id, content_type, accept, body) -> web.Response:
    """Reindex Subscription

    Alters the frequency of a given Subscription (formerly Recurrence) by changing period and interval.

    :param recurrence_id: 
    :type recurrence_id: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: list | bytes

    """
    body = [ReindexrecurrenceRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def updatepartialrecurrence(request: web.Request, recurrence_id, content_type, accept, body) -> web.Response:
    """Update partial Subscription

    Updates partial information of a given subscription (formerly Recurrence).

    :param recurrence_id: 
    :type recurrence_id: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatepartialrecurrenceRequest.from_dict(body)
    return web.Response(status=200)


async def updaterecurrence(request: web.Request, content_type, accept, body) -> web.Response:
    """Update Subscription

    Updates details of a given Subscription (formerly recurrence).

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdaterecurrenceRequest.from_dict(body)
    return web.Response(status=200)


async def updaterecurrencesettings(request: web.Request, content_type, accept, body) -> web.Response:
    """Update Subscription settings

    Updates the Subscriptions&#39; (formerly Recurrence) settings of your store by salesChannel and defaultSLA.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdaterecurrencesettingsRequest.from_dict(body)
    return web.Response(status=200)
