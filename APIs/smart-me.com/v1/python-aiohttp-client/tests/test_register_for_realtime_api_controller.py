# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.register_realtime_api_data import RegisterRealtimeApiData


pytestmark = pytest.mark.asyncio

async def test_register_for_realtime_api_delete(client):
    """Test case for register_for_realtime_api_delete

    Deletes a realtime API registration.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/RegisterForRealtimeApi/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_for_realtime_api_get(client):
    """Test case for register_for_realtime_api_get

    Gets all registrations for the Realtime API.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/RegisterForRealtimeApi',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_register_for_realtime_api_post(client):
    """Test case for register_for_realtime_api_post

    Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud.               More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx
    """
    body = {"BasicAuthUsername":"BasicAuthUsername","ApiUrl":"ApiUrl","SerialNumber":"SerialNumber","RegistrationType":"Disabled","Id":"Id","BasicAuthPassword":"BasicAuthPassword","MeterId":"MeterId"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/RegisterForRealtimeApi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

