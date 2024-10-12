# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_account_trades_get200_response_inner import AccountsAccountTradesGet200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_accounts_account_trades_get(client):
    """Test case for accounts_account_trades_get

    Returns trades in account
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/accounts/{account}/trades'.format(account='account_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

