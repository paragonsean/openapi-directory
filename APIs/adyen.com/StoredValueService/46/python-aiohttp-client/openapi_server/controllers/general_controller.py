from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.stored_value_balance_check_request import StoredValueBalanceCheckRequest
from openapi_server.models.stored_value_balance_check_response import StoredValueBalanceCheckResponse
from openapi_server.models.stored_value_balance_merge_request import StoredValueBalanceMergeRequest
from openapi_server.models.stored_value_balance_merge_response import StoredValueBalanceMergeResponse
from openapi_server.models.stored_value_issue_request import StoredValueIssueRequest
from openapi_server.models.stored_value_issue_response import StoredValueIssueResponse
from openapi_server.models.stored_value_load_request import StoredValueLoadRequest
from openapi_server.models.stored_value_load_response import StoredValueLoadResponse
from openapi_server.models.stored_value_status_change_request import StoredValueStatusChangeRequest
from openapi_server.models.stored_value_status_change_response import StoredValueStatusChangeResponse
from openapi_server.models.stored_value_void_request import StoredValueVoidRequest
from openapi_server.models.stored_value_void_response import StoredValueVoidResponse
from openapi_server import util


async def post_change_status(request: web.Request, body=None) -> web.Response:
    """Changes the status of the payment method.

    Changes the status of the provided payment method to the specified status.

    :param body: 
    :type body: dict | bytes

    """
    body = StoredValueStatusChangeRequest.from_dict(body)
    return web.Response(status=200)


async def post_check_balance(request: web.Request, body=None) -> web.Response:
    """Checks the balance.

    Checks the balance of the provided payment method.

    :param body: 
    :type body: dict | bytes

    """
    body = StoredValueBalanceCheckRequest.from_dict(body)
    return web.Response(status=200)


async def post_issue(request: web.Request, body=None) -> web.Response:
    """Issues a new card.

    Issues a new card of the given payment method.

    :param body: 
    :type body: dict | bytes

    """
    body = StoredValueIssueRequest.from_dict(body)
    return web.Response(status=200)


async def post_load(request: web.Request, body=None) -> web.Response:
    """Loads the payment method.

    Loads the payment method with the specified funds.

    :param body: 
    :type body: dict | bytes

    """
    body = StoredValueLoadRequest.from_dict(body)
    return web.Response(status=200)


async def post_merge_balance(request: web.Request, body=None) -> web.Response:
    """Merge the balance of two cards.

    Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

    :param body: 
    :type body: dict | bytes

    """
    body = StoredValueBalanceMergeRequest.from_dict(body)
    return web.Response(status=200)


async def post_void_transaction(request: web.Request, body=None) -> web.Response:
    """Voids a transaction.

    Voids the referenced stored value transaction.

    :param body: 
    :type body: dict | bytes

    """
    body = StoredValueVoidRequest.from_dict(body)
    return web.Response(status=200)
