# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pico_loadmanagement_group_dto import PicoLoadmanagementGroupDto


pytestmark = pytest.mark.asyncio

async def test_api_pico_loadmanagementgroup_get(client):
    """Test case for api_pico_loadmanagementgroup_get

    GET: api/pico/loadmanagementgroup                            Returns all available load management groups
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/pico/loadmanagementgroup',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pico_loadmanagement_group_get(client):
    """Test case for pico_loadmanagement_group_get

    GET: api/pico/loadmanagementgroup                            Returns a pico load management group by it's id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/pico/loadmanagementgroup/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

