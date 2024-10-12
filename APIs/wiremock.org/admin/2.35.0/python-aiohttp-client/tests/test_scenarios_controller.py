# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_scenarios_get200_response import AdminScenariosGet200Response


pytestmark = pytest.mark.asyncio

async def test_admin_scenarios_get(client):
    """Test case for admin_scenarios_get

    Get all scenarios
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/scenarios',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_scenarios_reset_post(client):
    """Test case for admin_scenarios_reset_post

    Reset the state of all scenarios
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/__admin/scenarios/reset',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

