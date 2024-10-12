# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_historical_balances_response import AccountHistoricalBalancesResponse
from openapi_server.models.account_response import AccountResponse
from openapi_server.models.create_account_request import CreateAccountRequest
from openapi_server.models.created_account_response import CreatedAccountResponse
from openapi_server.models.evaluate_address_request import EvaluateAddressRequest
from openapi_server.models.evaluate_address_response import EvaluateAddressResponse
from openapi_server.models.update_account_request import UpdateAccountRequest
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_create_manual_account(client):
    """Test case for create_manual_account

    Add Manual Account
    """
    body = {"account":{"includeInNetWorth":"includeInNetWorth","address":{"zip":"zip","country":"country","address3":"address3","address2":"address2","city":"city","sourceType":"sourceType","address1":"address1","street":"street","state":"state","type":"HOME"},"accountName":"accountName","accountType":"accountType","dueDate":"dueDate","memo":"memo","homeValue":{"amount":0.8008281904610115,"currency":"AUD"},"accountNumber":"accountNumber","frequency":"DAILY","amountDue":{"amount":0.8008281904610115,"currency":"AUD"},"balance":{"amount":0.8008281904610115,"currency":"AUD"},"nickname":"nickname","valuationType":"SYSTEM"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_account(client):
    """Test case for delete_account

    Delete Account
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts/{account_id}'.format(account_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_evaluate_address(client):
    """Test case for evaluate_address

    Evaluate Address
    """
    body = {"address":{"zip":"zip","country":"country","address3":"address3","address2":"address2","city":"city","sourceType":"sourceType","address1":"address1","street":"street","state":"state","type":"HOME"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts/evaluateAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Get Account Details
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{account_id}'.format(account_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_accounts(client):
    """Test case for get_all_accounts

    Get Accounts
    """
    params = [('accountId', 'account_id_example'),
                    ('container', 'container_example'),
                    ('include', 'include_example'),
                    ('providerAccountId', 'provider_account_id_example'),
                    ('requestId', 'request_id_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_historical_balances(client):
    """Test case for get_historical_balances

    Get Historical Balances
    """
    params = [('accountId', 'account_id_example'),
                    ('fromDate', 'from_date_example'),
                    ('includeCF', True),
                    ('interval', 'interval_example'),
                    ('skip', 56),
                    ('toDate', 'to_date_example'),
                    ('top', 56)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/accounts/historicalBalances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account(client):
    """Test case for update_account

    Update Account
    """
    body = {"account":{"container":"bank","includeInNetWorth":"includeInNetWorth","address":{"zip":"zip","country":"country","address3":"address3","address2":"address2","city":"city","sourceType":"sourceType","address1":"address1","street":"street","state":"state","type":"HOME"},"accountName":"accountName","dueDate":"dueDate","memo":"memo","homeValue":{"amount":0.8008281904610115,"currency":"AUD"},"accountNumber":"accountNumber","frequency":"DAILY","accountStatus":"ACTIVE","amountDue":{"amount":0.8008281904610115,"currency":"AUD"},"balance":{"amount":0.8008281904610115,"currency":"AUD"},"isEbillEnrolled":"isEbillEnrolled","nickname":"nickname"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/accounts/{account_id}'.format(account_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

