# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.o_auth2_permission_grant import OAuth2PermissionGrant


pytestmark = pytest.mark.asyncio

async def test_o_auth2_permission_grant_create(client):
    """Test case for o_auth2_permission_grant_create

    
    """
    body = {"clientId":"clientId","consentType":"consentType","expiryTime":"expiryTime","odata.type":"odata.type","principalId":"","resourceId":"resourceId","scope":"scope","startTime":"startTime"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{tenant_id}/oauth2PermissionGrants'.format(tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

