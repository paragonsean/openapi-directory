# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.load_balancer_types_get200_response import LoadBalancerTypesGet200Response
from openapi_server.models.load_balancer_types_id_get200_response import LoadBalancerTypesIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_load_balancer_types_get(client):
    """Test case for load_balancer_types_get

    Get all Load Balancer Types
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/load_balancer_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancer_types_id_get(client):
    """Test case for load_balancer_types_id_get

    Get a Load Balancer Type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/load_balancer_types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

