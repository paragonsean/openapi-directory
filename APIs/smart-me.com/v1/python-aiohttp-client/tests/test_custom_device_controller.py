# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_device_to_post import CustomDeviceToPost


pytestmark = pytest.mark.asyncio

async def test_api_custom_device_id_get(client):
    """Test case for api_custom_device_id_get

    Gets a Custom Device by it's ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/CustomDevice/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_device_get(client):
    """Test case for custom_device_get

    Gets all Custom Devices
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/CustomDevice',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_custom_device_post(client):
    """Test case for custom_device_post

    Creates or updates a Custom Device or updates it's values.
    """
    body = {"Serial":0,"Values":[{"Value":6.027456183070403,"Name":"Name"},{"Value":6.027456183070403,"Name":"Name"}],"ValueDate":"2000-01-23T04:56:07.000+00:00","Id":"Id","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/CustomDevice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

