# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_balance import AccountBalance
from openapi_server.models.error_authentication_failed_account_balance import ErrorAuthenticationFailedAccountBalance
from openapi_server.models.success import Success
from openapi_server.models.top_up_account_balance401_response import TopUpAccountBalance401Response


pytestmark = pytest.mark.asyncio

async def test_get_account_balance(client):
    """Test case for get_account_balance

    Get Account Balance
    """
    params = [('api_key', 'abcd1234'),
                    ('api_secret', 'ABCDEFGH01234abc')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/account/get-balance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_top_up_account_balance(client):
    """Test case for top_up_account_balance

    Top Up Account Balance
    """
    params = [('api_key', 'abcd1234'),
                    ('api_secret', 'ABCDEFGH01234abc')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'trx': 'trx_example'
        }
    response = await client.request(
        method='POST',
        path='/account/top-up',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

