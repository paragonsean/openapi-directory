# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bank_account import BankAccount
from openapi_server.models.bank_account_list import BankAccountList
from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse


pytestmark = pytest.mark.asyncio

async def test_create_bank_account(client):
    """Test case for create_bank_account

    Create a bank account
    """
    body = {"account_number":"account_number","account_number_iban":"account_number_iban","name":"name","currency":"AUD","id":6,"need_qr":False,"swift":"swift"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/bank-accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bank_account(client):
    """Test case for delete_bank_account

    Delete a bank account
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/bank-accounts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bank_account(client):
    """Test case for get_bank_account

    Retrieve a bank account
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/bank-accounts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bank_account(client):
    """Test case for list_bank_account

    List all bank account
    """
    params = [('page', 56),
                    ('per_page', 25)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/bank-accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_bank_account(client):
    """Test case for update_bank_account

    Update a bank account
    """
    body = {"account_number":"account_number","account_number_iban":"account_number_iban","name":"name","currency":"AUD","id":6,"need_qr":False,"swift":"swift"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/bank-accounts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

