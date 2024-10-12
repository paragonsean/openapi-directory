# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    get client filters
    """
    params = [('api_key', 'api_key_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'text/csv',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/client/configure/get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_set(client):
    """Test case for set

    set client filters
    """
    params = [('api_key', 'api_key_example'),
                    ('country', 'country_example')]
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('csvfile', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v2/client/configure/set',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

