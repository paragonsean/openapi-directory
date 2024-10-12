from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_transaction_out import CancelTransactionOut
from openapi_server.models.confirm_transaction_in import ConfirmTransactionIn
from openapi_server.models.confirm_transaction_out import ConfirmTransactionOut
from openapi_server.models.create_transaction_in import CreateTransactionIn
from openapi_server.models.create_transaction_out import CreateTransactionOut
from openapi_server.models.get_transaction_out import GetTransactionOut
from openapi_server.models.list_transactions_out import ListTransactionsOut
from openapi_server.models.unconfirm_transaction_in import UnconfirmTransactionIn
from openapi_server.models.unconfirm_transaction_out import UnconfirmTransactionOut
from openapi_server.models.update_transaction_in import UpdateTransactionIn
from openapi_server.models.update_transaction_out import UpdateTransactionOut
from openapi_server import util


async def cancel_transaction(request: web.Request, key) -> web.Response:
    """Delete transaction

    

    :param key: Transaction key
    :type key: str

    """
    return web.Response(status=200)


async def confirm_transaction(request: web.Request, key, input) -> web.Response:
    """Confirm transaction

    

    :param key: Transaction key.
    :type key: str
    :param input: Input
    :type input: dict | bytes

    """
    input = ConfirmTransactionIn.from_dict(input)
    return web.Response(status=200)


async def create_transaction(request: web.Request, input) -> web.Response:
    """Store transaction

    

    :param input: Input
    :type input: dict | bytes

    """
    input = CreateTransactionIn.from_dict(input)
    return web.Response(status=200)


async def get_transaction(request: web.Request, key) -> web.Response:
    """Retrieve transaction data.

    

    :param key: Transaction key
    :type key: str

    """
    return web.Response(status=200)


async def list_transactions(request: web.Request, filter_text=None, offset=None, has_note=None, key_or_custom_id=None, currency_code=None, order_date_to=None, sort_reverse=None, limit=None, invoice_number=None, tax_country_codes=None, statuses=None, original_transaction_key=None, order_date_from=None, total_amount_greater_than=None, format=None, total_amount_less_than=None, tax_country_code=None) -> web.Response:
    """Browse transactions

    

    :param filter_text: Filtering expression
    :type filter_text: str
    :param offset: Offset
    :type offset: int
    :param has_note: Return only transactions with a note field set.
    :type has_note: bool
    :param key_or_custom_id: Taxamo provided transaction key or custom id
    :type key_or_custom_id: str
    :param currency_code: Three letter ISO currency code.
    :type currency_code: str
    :param order_date_to: Order date to in yyyy-MM-dd format.
    :type order_date_to: str
    :param sort_reverse: If true, results are sorted in descending order.
    :type sort_reverse: bool
    :param limit: Limit (no more than 1000, defaults to 100).
    :type limit: int
    :param invoice_number: Transaction invoice number.
    :type invoice_number: str
    :param tax_country_codes: Comma separated list of two letter ISO tax country codes.
    :type tax_country_codes: str
    :param statuses: Comma separated list of of transaction statuses. &#39;N&#39; - unconfirmed transaction, &#39;C&#39; - confirmed transaction.
    :type statuses: str
    :param original_transaction_key: Taxamo provided original transaction key
    :type original_transaction_key: str
    :param order_date_from: Order date from in yyyy-MM-dd format.
    :type order_date_from: str
    :param total_amount_greater_than: Return only transactions with total amount greater than given number. Transactions with total amount equal to a given number (e.g. 0) are not returned.
    :type total_amount_greater_than: str
    :param format: Output format - supports &#39;csv&#39; value for this operation.
    :type format: str
    :param total_amount_less_than: Return only transactions with total amount less than a given number. Transactions with total amount equal to a given number (e.g. 1) are not returned.
    :type total_amount_less_than: str
    :param tax_country_code: Two letter ISO tax country code.
    :type tax_country_code: str

    """
    return web.Response(status=200)


async def unconfirm_transaction(request: web.Request, key, input) -> web.Response:
    """Un-confirm the transaction

    

    :param key: Transaction key.
    :type key: str
    :param input: Input
    :type input: dict | bytes

    """
    input = UnconfirmTransactionIn.from_dict(input)
    return web.Response(status=200)


async def update_transaction(request: web.Request, key, input) -> web.Response:
    """Update transaction

    

    :param key: Transaction key.
    :type key: str
    :param input: Input
    :type input: dict | bytes

    """
    input = UpdateTransactionIn.from_dict(input)
    return web.Response(status=200)
