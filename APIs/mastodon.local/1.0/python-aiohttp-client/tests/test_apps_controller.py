# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v1_apps_post200_response import ApiV1AppsPost200Response
from openapi_server.models.api_v1_apps_post_request import ApiV1AppsPostRequest
from openapi_server.models.application import Application
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_apps_post(client):
    """Test case for api_v1_apps_post

    
    """
    body = openapi_server.ApiV1AppsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/apps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_apps_verify_credentials_get(client):
    """Test case for api_v1_apps_verify_credentials_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apps/verify_credentials',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

