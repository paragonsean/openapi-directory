# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_public_v1_maintenancemode_start_post_request import ApiPublicV1MaintenancemodeStartPostRequest
from openapi_server.models.maintenance_mode_state import MaintenanceModeState


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_maintenancemode_get(client):
    """Test case for api_public_v1_maintenancemode_get

    Get an organization's current maintenance mode state
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/maintenancemode',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_maintenancemode_maintenancemodeid_end_put(client):
    """Test case for api_public_v1_maintenancemode_maintenancemodeid_end_put

    End maintenance mode for routing keys
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api-public/v1/maintenancemode/{maintenancemodeid}/end'.format(maintenancemodeid='maintenancemodeid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_maintenancemode_start_post(client):
    """Test case for api_public_v1_maintenancemode_start_post

    Start maintenance mode for routing keys
    """
    body = openapi_server.ApiPublicV1MaintenancemodeStartPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/maintenancemode/start',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

