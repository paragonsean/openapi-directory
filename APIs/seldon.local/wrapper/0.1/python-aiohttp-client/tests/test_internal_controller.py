# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.feedback import Feedback
from openapi_server.models.seldon_message import SeldonMessage
from openapi_server.models.seldon_message_list import SeldonMessageList


pytestmark = pytest.mark.asyncio

async def test_aggregate(client):
    """Test case for aggregate

    
    """
    params = [('body', openapi_server.SeldonMessageList())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/aggregate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_aggregate2(client):
    """Test case for aggregate2

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        '_json': openapi_server.SeldonMessageList()
        }
    response = await client.request(
        method='POST',
        path='/aggregate',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_route(client):
    """Test case for route

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        '_json': openapi_server.SeldonMessage()
        }
    response = await client.request(
        method='POST',
        path='/route',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route2(client):
    """Test case for route2

    
    """
    params = [('json', openapi_server.SeldonMessage())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/route',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_send_feedback(client):
    """Test case for send_feedback

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        '_json': openapi_server.Feedback()
        }
    response = await client.request(
        method='POST',
        path='/send-feedback',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_feedback2(client):
    """Test case for send_feedback2

    
    """
    params = [('json', openapi_server.Feedback())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/send-feedback',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_transform_input(client):
    """Test case for transform_input

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        '_json': openapi_server.SeldonMessage()
        }
    response = await client.request(
        method='POST',
        path='/transform-input',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_input2(client):
    """Test case for transform_input2

    
    """
    params = [('json', openapi_server.SeldonMessage())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/transform-input',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_transform_input3(client):
    """Test case for transform_input3

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        '_json': openapi_server.SeldonMessage()
        }
    response = await client.request(
        method='POST',
        path='/predict',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_input4(client):
    """Test case for transform_input4

    
    """
    params = [('json', openapi_server.SeldonMessage())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/predict',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_transform_output(client):
    """Test case for transform_output

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        '_json': openapi_server.SeldonMessage()
        }
    response = await client.request(
        method='POST',
        path='/transform-output',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transform_output2(client):
    """Test case for transform_output2

    
    """
    params = [('json', openapi_server.SeldonMessage())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/transform-output',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

