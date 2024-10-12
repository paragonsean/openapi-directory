# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.air_rest_services_metadata_get200_response import AirRestServicesMetadataGet200Response


pytestmark = pytest.mark.asyncio

async def test_air_rest_services_metadata_get(client):
    """Test case for air_rest_services_metadata_get

    Clean Air Act Metadata Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/air_rest_services.metadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_air_rest_services_metadata_post(client):
    """Test case for air_rest_services_metadata_post

    Clean Air Act Metadata Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/air_rest_services.metadata',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

