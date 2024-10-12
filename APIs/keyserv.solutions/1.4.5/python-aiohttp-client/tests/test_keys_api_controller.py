# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.keys_api_current200_response import KeysApiCurrent200Response
from openapi_server.models.keys_api_expiry200_response import KeysApiExpiry200Response
from openapi_server.models.keys_api_find200_response import KeysApiFind200Response


pytestmark = pytest.mark.asyncio

async def test_keys_api_current(client):
    """Test case for keys_api_current

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/KeysApi/Current/{serial}'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keys_api_custom(client):
    """Test case for keys_api_custom

    
    """
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/v1/KeysApi/Custom/{serial}'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keys_api_expiry(client):
    """Test case for keys_api_expiry

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/KeysApi/Expiry/{serial}'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keys_api_find(client):
    """Test case for keys_api_find

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/KeysApi/Find/{serial}'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

