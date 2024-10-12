# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.graph_error import GraphError


pytestmark = pytest.mark.asyncio

async def test_o_auth2_permission_grant_delete(client):
    """Test case for o_auth2_permission_grant_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{tenant_id}/oauth2PermissionGrants/{object_id}'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

