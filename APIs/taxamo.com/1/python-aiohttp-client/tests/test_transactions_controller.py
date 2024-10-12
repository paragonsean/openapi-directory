# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_cancel_transaction(client):
    """Test case for cancel_transaction

    Delete transaction
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/transactions/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_transaction(client):
    """Test case for confirm_transaction

    Confirm transaction
    """
    input = openapi_server.ConfirmTransactionIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{key}/confirm'.format(key='key_example'),
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_transaction(client):
    """Test case for create_transaction

    Store transaction
    """
    input = openapi_server.CreateTransactionIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions',
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction(client):
    """Test case for get_transaction

    Retrieve transaction data.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transactions/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transactions(client):
    """Test case for list_transactions

    Browse transactions
    """
    params = [('filter_text', 'filter_text_example'),
                    ('offset', 56),
                    ('has_note', True),
                    ('key_or_custom_id', 'key_or_custom_id_example'),
                    ('currency_code', 'currency_code_example'),
                    ('order_date_to', 'order_date_to_example'),
                    ('sort_reverse', True),
                    ('limit', 56),
                    ('invoice_number', 'invoice_number_example'),
                    ('tax_country_codes', 'tax_country_codes_example'),
                    ('statuses', 'statuses_example'),
                    ('original_transaction_key', 'original_transaction_key_example'),
                    ('order_date_from', 'order_date_from_example'),
                    ('total_amount_greater_than', 'total_amount_greater_than_example'),
                    ('format', 'format_example'),
                    ('total_amount_less_than', 'total_amount_less_than_example'),
                    ('tax_country_code', 'tax_country_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unconfirm_transaction(client):
    """Test case for unconfirm_transaction

    Un-confirm the transaction
    """
    input = openapi_server.UnconfirmTransactionIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{key}/unconfirm'.format(key='key_example'),
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_transaction(client):
    """Test case for update_transaction

    Update transaction
    """
    input = openapi_server.UpdateTransactionIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transactions/{key}'.format(key='key_example'),
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

