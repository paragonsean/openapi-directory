# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.datacenters_get200_response import DatacentersGet200Response
from openapi_server.models.datacenters_id_get200_response import DatacentersIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_datacenters_get(client):
    """Test case for datacenters_get

    Get all Datacenters
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/datacenters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datacenters_id_get(client):
    """Test case for datacenters_id_get

    Get a Datacenter
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/datacenters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

