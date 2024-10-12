# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_schema import ResourceSchema
from openapi_server.models.service_provider_configs import ServiceProviderConfigs


pytestmark = pytest.mark.asyncio

async def test_get_service_provider_configs(client):
    """Test case for get_service_provider_configs

    Get Service Provider Configurations
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/identity/v1/ServiceProviderConfigs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_schema(client):
    """Test case for get_user_schema

    Get User Schema
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/identity/v1/Schemas/Users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

