# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource import Resource


pytestmark = pytest.mark.asyncio

async def test_get_resource(client):
    """Test case for get_resource

    Get Resource
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/resources/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_resources_by_service(client):
    """Test case for get_resources_by_service

    Get Resources by Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/resources/service/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

