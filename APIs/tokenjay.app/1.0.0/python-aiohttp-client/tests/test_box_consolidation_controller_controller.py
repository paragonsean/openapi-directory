# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.mosaik_app import MosaikApp


pytestmark = pytest.mark.asyncio

async def test_ep_consolidate(client):
    """Test case for ep_consolidate

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/mosaik/boxconsolidation/consolidate/{p2pkaddress}'.format(p2pkaddress='p2pkaddress_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_main_app1(client):
    """Test case for main_app1

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/mosaik/boxconsolidation/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

