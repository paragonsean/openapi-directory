from typing import List, Dict
from aiohttp import web

from openapi_server.models.creditor_account import CreditorAccount
from openapi_server.models.creditor_account_write import CreditorAccountWrite
from openapi_server.models.creditor_account_write_request import CreditorAccountWriteRequest
from openapi_server.models.paginated_creditor_account_list import PaginatedCreditorAccountList
from openapi_server.models.paginated_payment_read_list import PaginatedPaymentReadList
from openapi_server.models.payment_read import PaymentRead
from openapi_server.models.payment_read_request import PaymentReadRequest
from openapi_server.models.payment_write import PaymentWrite
from openapi_server.models.payment_write_request import PaymentWriteRequest
from openapi_server import util


async def create_payment(request: web.Request, body) -> web.Response:
    """create_payment

    Create payment

    :param body: 
    :type body: dict | bytes

    """
    body = PaymentWriteRequest.from_dict(body)
    return web.Response(status=200)


async def delete_periodic_payment(request: web.Request, id) -> web.Response:
    """delete_periodic_payment

    Delete periodic payment

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def list_minimum_required_fields_for_institution(request: web.Request, institution_id) -> web.Response:
    """list_minimum_required_fields_for_institution

    List minimum required fields for institution

    :param institution_id: 
    :type institution_id: str

    """
    return web.Response(status=200)


async def list_payments(request: web.Request, limit=None, offset=None) -> web.Response:
    """list_payments

    Retrieve all payments belonging to the company

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def payments_creditors_create(request: web.Request, body) -> web.Response:
    """payments_creditors_create

    API endpoints related to creditor accounts.

    :param body: 
    :type body: dict | bytes

    """
    body = CreditorAccountWriteRequest.from_dict(body)
    return web.Response(status=200)


async def payments_creditors_destroy(request: web.Request, id) -> web.Response:
    """payments_creditors_destroy

    API endpoints related to creditor accounts.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def payments_creditors_list(request: web.Request, account=None, address_country=None, agent=None, currency=None, limit=None, name=None, offset=None, type=None) -> web.Response:
    """payments_creditors_list

    API endpoints related to creditor accounts.

    :param account: 
    :type account: str
    :param address_country: 
    :type address_country: str
    :param agent: 
    :type agent: str
    :param currency: 
    :type currency: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param name: 
    :type name: str
    :param offset: The initial index from which to return the results.
    :type offset: int
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def payments_creditors_retrieve(request: web.Request, id) -> web.Response:
    """payments_creditors_retrieve

    API endpoints related to creditor accounts.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def payments_submit_create(request: web.Request, id, body) -> web.Response:
    """payments_submit_create

    Initiate the payment on bank&#39;s side.  Complete the payment and return payment details as a response.

    :param id: 
    :type id: str
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentReadRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_all_payment_creditor_accounts(request: web.Request, ) -> web.Response:
    """retrieve_all_payment_creditor_accounts

    Retrieve all payment creditor accounts


    """
    return web.Response(status=200)


async def retrieve_payment(request: web.Request, id) -> web.Response:
    """retrieve_payment

    Retrieve payment

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
