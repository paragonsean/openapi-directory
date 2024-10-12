# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.numbers_v1_porting_bulk_portability import NumbersV1PortingBulkPortability


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_porting_bulk_portability(client):
    """Test case for create_porting_bulk_portability

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'phone_numbers': ['phone_numbers_example']
        }
    response = await client.request(
        method='POST',
        path='/v1/Porting/Portability',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_porting_bulk_portability(client):
    """Test case for fetch_porting_bulk_portability

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Porting/Portability/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

