from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.patch_payment_instrument_request import PatchPaymentInstrumentRequest
from openapi_server.models.payment_instrument2 import PaymentInstrument2
from openapi_server.models.post_payment_instrument_request import PostPaymentInstrumentRequest
from openapi_server import util


async def get_payment_instrument(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a Payment Instrument

    Retrieve a payment instrument by ID. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_payment_instrument_collection(request: web.Request, organization_id=None, filter=None, sort=None, limit=None, offset=None, q=None, expand=None) -> web.Response:
    """Retrieve a list of payment instruments

    Retrieve a list of payment instruments. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param q: The partial search of the text fields.
    :type q: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def patch_payment_instrument(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Update a Payment Instrument&#39;s values

    Update allowed payment instrument&#39;s values.

    :param id: The resource identifier string.
    :type id: str
    :param body: PaymentInstrument resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PatchPaymentInstrumentRequest.from_dict(body)
    return web.Response(status=200)


async def post_payment_instrument(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a Payment Instrument

    Create a payment instrument. If such payment card or bank account payment instrument already exists then updates it instead. 

    :param body: PaymentInstrument resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PostPaymentInstrumentRequest.from_dict(body)
    return web.Response(status=200)


async def post_payment_instrument_deactivation(request: web.Request, id, organization_id=None) -> web.Response:
    """Deactivate a payment instrument

    Deactivate a payment instrument. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)
