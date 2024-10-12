from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_timeline_custom_event import CustomerTimelineCustomEvent
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.lead_source import LeadSource
from openapi_server import util


async def delete_customer(request: web.Request, id, target_customer_id, organization_id=None) -> web.Response:
    """Merge and delete a customer

    Merge one duplicate customer to another target customer and delete the. former.

    :param id: The resource identifier string.
    :type id: str
    :param target_customer_id: The customer identifier to get the data of the deleted duplicate customer.
    :type target_customer_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_customer_lead_source(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a Lead Source for a customer

    Delete a Lead Source that belongs to a certain customer. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_customer(request: web.Request, id, organization_id=None, expand=None, fields=None) -> web.Response:
    """Retrieve a customer

    Retrieve a customer with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str
    :param fields: Limit the returned fields to the list specified, separated by comma. Note that id is always returned.
    :type fields: str

    """
    return web.Response(status=200)


async def get_customer_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, q=None, expand=None, fields=None, sort=None) -> web.Response:
    """Retrieve a list of customers

    Retrieve a list of customers. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param q: The partial search of the text fields.
    :type q: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str
    :param fields: Limit the returned fields to the list specified, separated by comma. Note that id is always returned.
    :type fields: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def get_customer_lead_source(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a customer&#39;s Lead Source

    Retrieve a Lead Source of given customer. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_customer(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a customer (without an ID)

    Create a customer without a predefined ID. The customer&#39;s primary address will be used as the default address for payment instruments, subscriptions and invoices if none are provided.  If you wish to create the customer with a predefined ID (which we recommend to prevent duplication), you may use our &#x60;PUT&#x60; request described below.  Read our guide to [preventing duplicates](https://api-guides.rebilly.com/core-concepts/preventing-duplicates) to understand more. 

    :param body: Customer resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Customer.from_dict(body)
    return web.Response(status=200)


async def post_customer_timeline_custom_event_type(request: web.Request, body, organization_id=None) -> web.Response:
    """Create Customer Timeline custom event type

    Create Customer Timeline custom event type. 

    :param body: Customer Timeline Custom Event Type resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = CustomerTimelineCustomEvent.from_dict(body)
    return web.Response(status=200)


async def put_customer(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Upsert a customer with predefined ID

    Create or update (upsert) a customer with predefined identifier string. Read our guide to [preventing duplicates](https://api-guides.rebilly.com/core-concepts/preventing-duplicates) to understand more. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Customer resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Customer.from_dict(body)
    return web.Response(status=200)


async def put_customer_lead_source(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create a Lead Source for a customer

    Create a Lead Source for a customer. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Lead Source resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = LeadSource.from_dict(body)
    return web.Response(status=200)
