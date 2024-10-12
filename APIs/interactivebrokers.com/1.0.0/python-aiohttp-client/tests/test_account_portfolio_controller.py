# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_account_positions_get200_response_inner import AccountsAccountPositionsGet200ResponseInner
from openapi_server.models.accounts_account_summary_get200_response import AccountsAccountSummaryGet200Response
from openapi_server.models.accounts_get200_response import AccountsGet200Response


pytestmark = pytest.mark.asyncio

async def test_accounts_account_positions_get(client):
    """Test case for accounts_account_positions_get

    Account Positions
    """
    headers = { 
        'Accept': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/accounts/{account}/positions'.format(account='account_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_summary_get(client):
    """Test case for accounts_account_summary_get

    Account Values Summary
    """
    headers = { 
        'Accept': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/accounts/{account}/summary'.format(account='account_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get(client):
    """Test case for accounts_get

    Brokerage Accounts
    """
    params = [('account', 'account_example')]
    headers = { 
        'Accept': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

