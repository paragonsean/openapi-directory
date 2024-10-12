# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.o_auth2_permission_grant_list_result import OAuth2PermissionGrantListResult


pytestmark = pytest.mark.asyncio

async def test_o_auth2_permission_grant_list(client):
    """Test case for o_auth2_permission_grant_list

    
    """
    params = [('$filter', 'clientId+eq+'61ed44c3-5a1d-4639-a215-07f25129c6c3'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/oauth2PermissionGrants'.format(tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

