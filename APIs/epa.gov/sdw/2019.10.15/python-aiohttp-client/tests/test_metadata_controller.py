# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sdw_rest_services_metadata_get200_response import SdwRestServicesMetadataGet200Response


pytestmark = pytest.mark.asyncio

async def test_sdw_rest_services_metadata_get(client):
    """Test case for sdw_rest_services_metadata_get

    Safe Drinking Water Act (SDWA) Metadata Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/sdw_rest_services.metadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_sdw_rest_services_metadata_post(client):
    """Test case for sdw_rest_services_metadata_post

    Safe Drinking Water Act (SDWA) Metadata Service
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
        path='/echo/sdw_rest_services.metadata',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

