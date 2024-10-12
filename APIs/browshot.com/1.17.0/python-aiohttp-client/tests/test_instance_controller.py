# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.instance import Instance
from openapi_server.models.instance_error import InstanceError
from openapi_server.models.instance_list import InstanceList


pytestmark = pytest.mark.asyncio

async def test_get_instance_info(client):
    """Test case for get_instance_info

    Get information about an instance
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/instance/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instances_info(client):
    """Test case for get_instances_info

    Get all instances
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/instance/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

