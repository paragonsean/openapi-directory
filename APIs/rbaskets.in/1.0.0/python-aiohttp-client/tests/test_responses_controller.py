# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.response import Response


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_responses_method_get(client):
    """Test case for api_baskets_name_responses_method_get

    Get response settings
    """
    headers = { 
        'Accept': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/baskets/{name}/responses/{method}'.format(name='name_example', method='method_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_responses_method_put(client):
    """Test case for api_baskets_name_responses_method_put

    Update response settings
    """
    response = {"headers":{"Accept":["application/json","application/xml"],"Connection":["close"],"Content-Type":["application/json"]},"is_template":False,"body":"Success","status":200}
    headers = { 
        'Content-Type': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/baskets/{name}/responses/{method}'.format(name='name_example', method='method_example'),
        headers=headers,
        json=response,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_responses_method_get(client):
    """Test case for baskets_name_responses_method_get

    Get response settings
    """
    headers = { 
        'Accept': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/baskets/{name}/responses/{method}'.format(name='name_example', method='method_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_responses_method_put(client):
    """Test case for baskets_name_responses_method_put

    Update response settings
    """
    response = {"headers":{"Accept":["application/json","application/xml"],"Connection":["close"],"Content-Type":["application/json"]},"is_template":False,"body":"Success","status":200}
    headers = { 
        'Content-Type': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/baskets/{name}/responses/{method}'.format(name='name_example', method='method_example'),
        headers=headers,
        json=response,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

