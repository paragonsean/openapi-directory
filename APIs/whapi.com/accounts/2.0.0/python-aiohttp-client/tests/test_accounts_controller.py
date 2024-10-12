# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_balance import AccountBalance
from openapi_server.models.account_errors import AccountErrors
from openapi_server.models.accounts import Accounts
from openapi_server.models.get_payments import GetPayments


pytestmark = pytest.mark.asyncio

async def test_get_balance(client):
    """Test case for get_balance

    Get a customers account balance
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('languageAsPerTerritory', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/accounts/account/balance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_details(client):
    """Test case for get_details

    Retrieves details of a customers account
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('languageAsPerTerritory', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/accounts/account',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments(client):
    """Test case for get_payments

    Gets a customer's account payments
    """
    params = [('page', 1.0),
                    ('pageSize', 100.0),
                    ('dateFrom', 'date_from_example'),
                    ('dateTo', 'date_to_example'),
                    ('sort', 'date,asc'),
                    ('transactionType', 'transaction_type_example'),
                    ('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('languageAsPerTerritory', 'true')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
        'territory': 'territory_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/accounts/account/payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

