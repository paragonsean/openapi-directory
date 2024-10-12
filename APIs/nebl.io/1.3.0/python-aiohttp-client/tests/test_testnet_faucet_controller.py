# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_faucet_response import GetFaucetResponse


pytestmark = pytest.mark.asyncio

async def test_testnet_get_faucet(client):
    """Test case for testnet_get_faucet

    Withdraws testnet NEBL to the specified address
    """
    params = [('address', 'address_example'),
                    ('amount', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/testnet/faucet',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

