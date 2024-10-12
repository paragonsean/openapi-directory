from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_issue import InvoiceIssue
from openapi_server.models.order_timeline import OrderTimeline
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_cancellation import SubscriptionCancellation
from openapi_server.models.subscription_change import SubscriptionChange
from openapi_server.models.subscription_invoice import SubscriptionInvoice
from openapi_server.models.subscription_reactivation import SubscriptionReactivation
from openapi_server import util


async def delete_subscription_cancellation(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a cancellation

    Delete an order&#39;s cancellation. Only draft can be deleted.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_subscription_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Delete an Order Timeline message

    Delete an Order Timeline message with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Order Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_subscription(request: web.Request, id, organization_id=None, expand=None) -> web.Response:
    """Retrieve an order

    Retrieve an order with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def get_subscription_cancellation(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve an order сancellation

    Retrieve an order сancellation with specified identifier string.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_subscription_cancellation_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, sort=None) -> web.Response:
    """Retrieve a list of cancellations

    Retrieve a list of cancellations for all subscriptions.

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

    """
    return web.Response(status=200)


async def get_subscription_collection(request: web.Request, organization_id=None, filter=None, sort=None, limit=None, offset=None, q=None, expand=None) -> web.Response:
    """Retrieve a list of orders

    Retrieve a list of orders. 

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
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def get_subscription_reactivation(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve an order reactivation

    Retrieve an order reactivation with specified identifier string.

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_subscription_reactivation_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, sort=None) -> web.Response:
    """Retrieve a list of reactivations

    Retrieve a list of reactivations for all subscriptions.

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

    """
    return web.Response(status=200)


async def get_subscription_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Retrieve an Order Timeline message

    Retrieve a order message with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Order Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_subscription_timeline_collection(request: web.Request, id, organization_id=None, limit=None, offset=None, filter=None, sort=None, q=None) -> web.Response:
    """Retrieve a list of order timeline messages

    Retrieve a list of order timeline messages. 

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


async def get_subscription_upcoming_invoice_collection(request: web.Request, id, organization_id=None, expand=None) -> web.Response:
    """Retrieve subscription order&#39;s upcoming invoice

    Retrieve an upcoming invoice from the specified subscription order. The endpoint is temporary before upcoming invoices get a complete integration. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def post_subscription(request: web.Request, body, organization_id=None, expand=None) -> web.Response:
    """Create an order

    Create an order. Consider using the upsert. operation to accomplish this task. 

    :param body: Order resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    body = Subscription.from_dict(body)
    return web.Response(status=200)


async def post_subscription_cancellation(request: web.Request, body, organization_id=None) -> web.Response:
    """Cancel an order

    Cancel an order or preview the cancellation parameters before that.

    :param body: Cancellation resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = SubscriptionCancellation.from_dict(body)
    return web.Response(status=200)


async def post_subscription_interim_invoice(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Issue an interim invoice for a subscription order

    Issue an interim invoice for a subscription, typically used in conjunction. with plan changes and pro rata adjustments. This process creates an invoice, adds the subscription&#39;s line items to the invoice, and issues the invoice, and applies payment to it if a transaction id is supplied. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Issue an interim invoice.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = SubscriptionInvoice.from_dict(body)
    return web.Response(status=200)


async def post_subscription_items_change(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Change an order&#39;s items

    Change an order&#39;s items or quantities and designate when and if there should be pro-rata credits given. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Change items request.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = SubscriptionChange.from_dict(body)
    return web.Response(status=200)


async def post_subscription_reactivation(request: web.Request, body, organization_id=None) -> web.Response:
    """Reactivate an order

    Reactivate a subscription.

    :param body: Reactivation resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = SubscriptionReactivation.from_dict(body)
    return web.Response(status=200)


async def post_subscription_timeline(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create an order Timeline comment

    Create an order Timeline comment. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Order Timeline resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = OrderTimeline.from_dict(body)
    return web.Response(status=200)


async def post_upcoming_invoice_issuance(request: web.Request, id, invoice_id, body, organization_id=None) -> web.Response:
    """Issue an upcoming invoice for early pay

    Issue an upcoming invoice with specified identifier string for early pay. 

    :param id: The resource identifier string.
    :type id: str
    :param invoice_id: The Upcoming Invoice ID.
    :type invoice_id: str
    :param body: InvoiceIssue resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = InvoiceIssue.from_dict(body)
    return web.Response(status=200)


async def put_subscription(request: web.Request, id, body, organization_id=None, expand=None) -> web.Response:
    """Upsert an order with predefined ID

    Create or update an order with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Order resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    body = Subscription.from_dict(body)
    return web.Response(status=200)


async def put_subscription_cancellation(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Cancel an order

    Cancel a subscription.

    :param id: The resource identifier string.
    :type id: str
    :param body: Cancellation resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = SubscriptionCancellation.from_dict(body)
    return web.Response(status=200)
