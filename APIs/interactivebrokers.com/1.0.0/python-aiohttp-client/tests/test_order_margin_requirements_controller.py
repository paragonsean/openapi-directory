# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_account_order_impact_post200_response import AccountsAccountOrderImpactPost200Response
from openapi_server.models.accounts_account_order_impact_post_request import AccountsAccountOrderImpactPostRequest


pytestmark = pytest.mark.asyncio

async def test_accounts_account_order_impact_post(client):
    """Test case for accounts_account_order_impact_post

    Return margin impact info
    """
    body = openapi_server.AccountsAccountOrderImpactPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tradingapi/v1/accounts/{account}/order_impact'.format(account='account_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

