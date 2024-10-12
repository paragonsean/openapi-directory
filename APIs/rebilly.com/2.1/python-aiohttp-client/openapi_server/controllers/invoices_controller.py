from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_issue import InvoiceIssue
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.invoice_reissue import InvoiceReissue
from openapi_server.models.invoice_timeline import InvoiceTimeline
from openapi_server.models.invoice_transaction import InvoiceTransaction
from openapi_server.models.invoice_transaction_allocation import InvoiceTransactionAllocation
from openapi_server import util


async def delete_invoice_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Delete an Invoice Timeline message

    Delete an Invoice Timeline message with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Invoice Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_customer_upcoming_invoice_collection(request: web.Request, id, organization_id=None, expand=None) -> web.Response:
    """Retrieve customer&#39;s upcoming invoices

    Retrieve a list of upcoming invoices from the subscriptions which belong to. the given customer. The endpoint is temporary before upcoming invoices get a complete integration. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def get_invoice(request: web.Request, id, organization_id=None, accept=None, expand=None) -> web.Response:
    """Retrieve an invoice

    Retrieve an invoice with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param accept: The response media type.
    :type accept: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def get_invoice_collection(request: web.Request, organization_id=None, filter=None, sort=None, limit=None, offset=None, q=None, expand=None) -> web.Response:
    """Retrieve a list of invoices

    Retrieve a list of invoices. 

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


async def get_invoice_item_collection(request: web.Request, id, organization_id=None, limit=None, offset=None, expand=None) -> web.Response:
    """Retrieve invoice items

    Retrieve an invoice items with specified invoice identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def get_invoice_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Retrieve an Invoice Timeline message

    Retrieve a invoice message with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Invoice Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_invoice_timeline_collection(request: web.Request, id, organization_id=None, limit=None, offset=None, filter=None, sort=None, q=None) -> web.Response:
    """Retrieve a list of invoice timeline messages

    Retrieve a list of invoice timeline messages. 

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


async def get_invoice_transaction_allocation_collection(request: web.Request, id, organization_id=None, limit=None, offset=None) -> web.Response:
    """Get transaction amounts allocated to an invoice

    Get the precise amounts from a transaction allocated as invoice payments.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int

    """
    return web.Response(status=200)


async def post_invoice(request: web.Request, body, organization_id=None) -> web.Response:
    """Create an invoice

    Create an invoice. 

    :param body: Invoice resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Invoice.from_dict(body)
    return web.Response(status=200)


async def post_invoice_abandonment(request: web.Request, id, organization_id=None) -> web.Response:
    """Abandon an invoice

    Abandon an invoice with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_invoice_issuance(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Issue an invoice

    Issue an invoice with specified identifier string. It must be in &#x60;draft&#x60; status. 

    :param id: The resource identifier string.
    :type id: str
    :param body: InvoiceIssue resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = InvoiceIssue.from_dict(body)
    return web.Response(status=200)


async def post_invoice_item(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create an invoice item

    Create an invoice item. 

    :param id: The resource identifier string.
    :type id: str
    :param body: InvoiceItem resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = InvoiceItem.from_dict(body)
    return web.Response(status=200)


async def post_invoice_recalculation(request: web.Request, id, organization_id=None) -> web.Response:
    """Recalculate an invoice

    Recalculate an invoice with specified identifier string. It will recalculate shipping rates, taxes, discounts. It is useful when coupon was revoked or customer redeemed coupon after invoice was issued and you want to apply it to this invoice. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_invoice_reissuance(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Reissue an invoice

    Reissue an invoice with specified identifier string. It must be issued. (status must be &#x60;unpaid&#x60; or &#x60;past-due&#x60;). 

    :param id: The resource identifier string.
    :type id: str
    :param body: InvoiceReissue resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = InvoiceReissue.from_dict(body)
    return web.Response(status=200)


async def post_invoice_timeline(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create an invoice Timeline comment

    Create an invoice Timeline comment. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Invoice Timeline resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = InvoiceTimeline.from_dict(body)
    return web.Response(status=200)


async def post_invoice_transaction(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Apply a transaction to an invoice

    Apply a transaction to an invoice. The invoice must be unpaid. The transaction must have a non-zero unused amount (not fully applied to other invoices). 

    :param id: The resource identifier string.
    :type id: str
    :param body: InvoiceTransaction resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = InvoiceTransaction.from_dict(body)
    return web.Response(status=200)


async def post_invoice_void(request: web.Request, id, organization_id=None) -> web.Response:
    """Void an invoice

    Void an invoice with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def put_invoice(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create or update an invoice with predefined ID

    Create or update an invoice with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Invoice resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Invoice.from_dict(body)
    return web.Response(status=200)
