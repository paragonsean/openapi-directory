from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_timeline import CustomerTimeline
from openapi_server.models.customer_timeline_custom_event import CustomerTimelineCustomEvent
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server import util


async def delete_customer_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Delete a Customer Timeline message

    Delete a Customer Timeline message with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Customer Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_customer_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Retrieve a customer Timeline message

    Retrieve a customer message with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Customer Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_customer_timeline_collection(request: web.Request, id, organization_id=None, limit=None, offset=None, filter=None, sort=None, q=None) -> web.Response:
    """Retrieve a list of customer timeline messages

    Retrieve a list of customer timeline messages. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]
    :param q: The partial search of the text fields.
    :type q: str

    """
    return web.Response(status=200)


async def get_customer_timeline_custom_event_type(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve customer timeline custom event type with specified identifier string

    Retrieve customer timeline custom event type. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_customer_timeline_custom_event_type_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None) -> web.Response:
    """Retrieve a list of customer timeline custom event types

    Retrieve a list of customer timeline custom event types. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str

    """
    return web.Response(status=200)


async def get_customer_timeline_event_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None) -> web.Response:
    """Retrieve a list of customer timeline messages for all customers

    Retrieve a list of customer timeline messages for all customers. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str

    """
    return web.Response(status=200)


async def post_customer_timeline(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create a customer Timeline comment or custom defined event

    Create a customer Timeline comment or custom defined event. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Customer Timeline resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = CustomerTimeline.from_dict(body)
    return web.Response(status=200)
