# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cwa_rest_services_metadata_get200_response import CwaRestServicesMetadataGet200Response


pytestmark = pytest.mark.asyncio

async def test_cwa_rest_services_metadata_get(client):
    """Test case for cwa_rest_services_metadata_get

    Clean Water Act (CWA) Metadata Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/cwa_rest_services.metadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_cwa_rest_services_metadata_post(client):
    """Test case for cwa_rest_services_metadata_post

    Clean Water Act (CWA) Metadata Service
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
        path='/echo/cwa_rest_services.metadata',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

