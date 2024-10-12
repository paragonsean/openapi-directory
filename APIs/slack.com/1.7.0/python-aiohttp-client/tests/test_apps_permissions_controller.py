# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_permissions_info_error_schema import AppsPermissionsInfoErrorSchema
from openapi_server.models.apps_permissions_info_schema import AppsPermissionsInfoSchema
from openapi_server.models.apps_permissions_request_error_schema import AppsPermissionsRequestErrorSchema
from openapi_server.models.apps_permissions_request_schema import AppsPermissionsRequestSchema


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_info(client):
    """Test case for apps_permissions_info

    
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_request(client):
    """Test case for apps_permissions_request

    
    """
    params = [('token', 'token_example'),
                    ('scopes', 'scopes_example'),
                    ('trigger_id', 'trigger_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.request',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

