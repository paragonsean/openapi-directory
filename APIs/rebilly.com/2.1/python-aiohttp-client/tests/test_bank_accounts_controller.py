# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bank_account import BankAccount
from openapi_server.models.bank_account_update_plain import BankAccountUpdatePlain
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.post_bank_account_request import PostBankAccountRequest


pytestmark = pytest.mark.asyncio

async def test_get_bank_account(client):
    """Test case for get_bank_account

    Retrieve a Bank Account
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bank-accounts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bank_account_collection(client):
    """Test case for get_bank_account_collection

    Retrieve a list of bank accounts
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('q', 'q_example'),
                    ('sort', ['sort_example']),
                    ('filter', 'filter_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bank-accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_bank_account(client):
    """Test case for patch_bank_account

    Update a bank account's values
    """
    body = {"customFields":{"foo":"bar"},"accountType":"checking","bankName":"bankName","billingAddress":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bank-accounts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_bank_account(client):
    """Test case for post_bank_account

    Create a Bank Account
    """
    body = openapi_server.PostBankAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bank-accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_bank_account_deactivation(client):
    """Test case for post_bank_account_deactivation

    Deactivate a Bank Account
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bank-accounts/{id}/deactivation'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_bank_account(client):
    """Test case for put_bank_account

    Create a Bank Account with predefined ID
    """
    body = openapi_server.PostBankAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/bank-accounts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

