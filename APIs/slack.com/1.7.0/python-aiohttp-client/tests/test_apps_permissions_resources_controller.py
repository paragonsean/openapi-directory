# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_permissions_resources_list_error_schema import AppsPermissionsResourcesListErrorSchema
from openapi_server.models.apps_permissions_resources_list_success_schema import AppsPermissionsResourcesListSuccessSchema


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_resources_list(client):
    """Test case for apps_permissions_resources_list

    
    """
    params = [('token', 'token_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.resources.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

