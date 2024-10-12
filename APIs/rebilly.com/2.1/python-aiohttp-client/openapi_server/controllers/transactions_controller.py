from typing import List, Dict
from aiohttp import web

from openapi_server.models.core_ready_to_pay import CoreReadyToPay
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.patch_transaction_request import PatchTransactionRequest
from openapi_server.models.payout_request import PayoutRequest
from openapi_server.models.ready_to_pay_methods_inner import ReadyToPayMethodsInner
from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_query import TransactionQuery
from openapi_server.models.transaction_refund import TransactionRefund
from openapi_server.models.transaction_request import TransactionRequest
from openapi_server.models.transaction_timeline import TransactionTimeline
from openapi_server.models.transaction_update import TransactionUpdate
from openapi_server import util


async def delete_transaction_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Delete a Transaction Timeline message

    Delete a Transaction Timeline message with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Transaction Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_transaction(request: web.Request, id, organization_id=None, expand=None) -> web.Response:
    """Retrieve a Transaction

    Retrieve a Transaction with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def get_transaction_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, q=None, sort=None, expand=None) -> web.Response:
    """Retrieve a list of transactions

    Retrieve a list of transactions. 

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
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    return web.Response(status=200)


async def get_transaction_timeline(request: web.Request, id, message_id, organization_id=None) -> web.Response:
    """Retrieve a transaction Timeline message

    Retrieve a timeline message with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param message_id: The Transaction Timeline message ID.
    :type message_id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_transaction_timeline_collection(request: web.Request, id, organization_id=None, limit=None, offset=None, filter=None) -> web.Response:
    """Retrieve a list of transaction timeline messages

    Retrieve a list of transaction timeline messages. 

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

    """
    return web.Response(status=200)


async def patch_transaction(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Update a transaction

    Update a transaction&#39;s custom fields. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Use the patch transaction request to modify custom fields.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PatchTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def post_payout(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a credit transaction

    Create a transaction of type &#x60;credit&#x60;. 

    :param body: Transaction resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = PayoutRequest.from_dict(body)
    return web.Response(status=200)


async def post_ready_to_pay(request: web.Request, organization_id=None, body=None) -> web.Response:
    """Ready to Pay

    Get available payment methods for a specific transaction or a purchase.  The payment methods order shown to a customer **SHOULD** be the same as the order in the response.  The list of available methods is generated from available [Gateway Accounts](https://user-api-docs.rebilly.com/tag/Gateway-Accounts) intersected with the last matched [Rules Engine](https://user-api-docs.rebilly.com/tag/Rules#operation/PutEventRule) &#x60;adjust-ready-to-pay&#x60; action on &#x60;ready-to-pay-requested&#x60; event.  If there were no actions matched for the specific request – all methods supported by the Gateway Accounts are sent.  To invert this behavior – place an all-matching rule at the very end of the &#x60;ready-to-pay-requested&#x60; event in Rules Engine with an empty &#x60;paymentMethods&#x60; property of the &#x60;adjust-ready-to-pay&#x60; action. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CoreReadyToPay.from_dict(body)
    return web.Response(status=200)


async def post_transaction(request: web.Request, body, organization_id=None, expand=None) -> web.Response:
    """Create a transaction

    Create a transaction of type &#x60;sale&#x60; or &#x60;authorize&#x60;. This endpoint supports two main styles of transactions:   1. A real-time decision and response.   2. User approval/interaction is required.  A real-time decision is very familiar.  You send a request, and inspect the &#x60;result&#x60; of the response for &#x60;approved&#x60; or &#x60;declined&#x60;.  However, many transactions, especially those for alternative methods, require the user to interact with a 3rd party.  You may be able to envision PayPal, for example, the user must give permission to complete the payment (or accept the billing agreement).  Even payment cards may require user approval in the case of 3D secure authentication.  In the event that approval is required, you will receive a response back and notice that the &#x60;result&#x60; is &#x60;unknown&#x60;.  You will find that the &#x60;status&#x60; is &#x60;waiting-approval&#x60;. And you will find in the &#x60;_links&#x60; section of the response a link for the &#x60;approvalUrl&#x60;.  In this case you would either open the &#x60;approvalUrl&#x60; in an iframe or in a pop (better workflow for mobile). 

    :param body: Transaction resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param expand: Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
    :type expand: str

    """
    body = TransactionRequest.from_dict(body)
    return web.Response(status=200)


async def post_transaction_query(request: web.Request, id, organization_id=None) -> web.Response:
    """Query a Transaction

    Query a Transaction with a specified identifier string. The query will contact the gateway account to find the result and amount/currency. The response should be analyzed.  If deemed appropriate, the transaction could be updated using the Transaction Update API. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def post_transaction_refund(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Refund a Transaction

    Refund a Transaction with specified identifier string. Note that the refund will be in the same currency as the original transaction. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Transaction resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = TransactionRefund.from_dict(body)
    return web.Response(status=200)


async def post_transaction_timeline(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create a transaction Timeline comment

    Create a transaction Timeline comment. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Transaction Timeline resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = TransactionTimeline.from_dict(body)
    return web.Response(status=200)


async def post_transaction_update(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Update a Transaction status

    Update a Transaction manually to completed status with given result with optional currency and amount.

    :param id: The resource identifier string.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = TransactionUpdate.from_dict(body)
    return web.Response(status=200)
