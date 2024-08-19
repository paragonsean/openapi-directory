# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.baudrate import Baudrate
from openapi_server.models.hat import Hat


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/mbus/get/{device}/{baudrate}/{address}'.format(device='ttyAMA0', baudrate=openapi_server.Baudrate(), address='48'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multi(client):
    """Test case for get_multi

    
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/mbus/getMulti/{device}/{baudrate}/{address}/{maxframes}'.format(device='ttyAMA0', baudrate=openapi_server.Baudrate(), address='48', maxframes=16),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hat(client):
    """Test case for hat

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/mbus/hat',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hat_off(client):
    """Test case for hat_off

    
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/mbus/hat/off',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hat_on(client):
    """Test case for hat_on

    
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/mbus/hat/on',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mbus_api(client):
    """Test case for mbus_api

    
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/mbus/api',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scan(client):
    """Test case for scan

    
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/mbus/scan/{device}/{baudrate}'.format(device='ttyAMA0', baudrate=openapi_server.Baudrate()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

