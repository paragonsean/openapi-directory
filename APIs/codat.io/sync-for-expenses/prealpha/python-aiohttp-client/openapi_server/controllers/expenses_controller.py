from typing import List, Dict
from aiohttp import web

from openapi_server.models.attachment import Attachment
from openapi_server.models.create_expense_request import CreateExpenseRequest
from openapi_server.models.create_expense_response import CreateExpenseResponse
from openapi_server import util


async def create_expense_dataset(request: web.Request, company_id, body=None) -> web.Response:
    """Create expense-transactions

    Create an expense transaction

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateExpenseRequest.from_dict(body)
    return web.Response(status=200)


async def upload_attachment(request: web.Request, company_id, transaction_id, sync_id) -> web.Response:
    """Upload attachment

    Creates an attachment in the accounting software against the given transactionId

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param transaction_id: The unique identifier for your SMB&#39;s transaction.
    :type transaction_id: str
    :type transaction_id: str
    :param sync_id: Unique identifier for a sync.
    :type sync_id: str
    :type sync_id: str

    """
    return web.Response(status=200)
