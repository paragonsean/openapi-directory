# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_get_apps import EndpointGetApps
from openapi_server.models.endpoint_get_apps_id import EndpointGetAppsID


pytestmark = pytest.mark.asyncio

async def test_apps_get(client):
    """Test case for apps_get

    
    """
    params = [('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_idget(client):
    """Test case for apps_idget

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/apps/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

