# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.fetch_action_response import FetchActionResponse
from openapi_server.models.mosaik_app import MosaikApp


pytestmark = pytest.mark.asyncio

async def test_get_burning_transaction(client):
    """Test case for get_burning_transaction

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/mosaik/tokenburn/get/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_main_app(client):
    """Test case for main_app

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/mosaik/tokenburn',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prepare_transaction(client):
    """Test case for prepare_transaction

    
    """
    body = None
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mosaik/tokenburn/prepare',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

