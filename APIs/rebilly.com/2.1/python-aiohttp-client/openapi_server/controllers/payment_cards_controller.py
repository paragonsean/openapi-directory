from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.payment_card import PaymentCard
from openapi_server.models.payment_card_update_plain import PaymentCardUpdatePlain
from openapi_server.models.post_payment_card_request import PostPaymentCardRequest
from openapi_server import util


async def get_payment_card(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a Payment Card

    Retrieve a Payment Card with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_payment_card_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, sort=None, q=None, expand=None) -> web.Response:
    """Retrieve a list of Payment Cards

    Retrieve a list of Payments Cards. 

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
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def patch_payment_card(request: web.Request, id, organization_id=None, body=None) -> web.Response:
    """Update a payment card&#39;s values

    Update any of the payment card&#39;s values except for the pan. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param body: Payment card.
    :type body: dict | bytes

    """
    body = PaymentCardUpdatePlain.from_dict(body)
    return web.Response(status=200)


async def post_payment_card(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a Payment Card

    Create a Payment Card. 

    :param body: PaymentCard resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PostPaymentCardRequest.from_dict(body)
    return web.Response(status=200)


async def post_payment_card_deactivation(request: web.Request, id, organization_id=None) -> web.Response:
    """Deactivate a Payment Card

    Deactivate a Payment Card. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def put_payment_card(request: web.Request, id, organization_id=None, body=None) -> web.Response:
    """Create a payment card with predefined ID

    

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param body: Payment card.
    :type body: dict | bytes

    """
    body = PostPaymentCardRequest.from_dict(body)
    return web.Response(status=200)
