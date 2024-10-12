# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_revoke_error_schema import AuthRevokeErrorSchema
from openapi_server.models.auth_revoke_schema import AuthRevokeSchema
from openapi_server.models.auth_test_error_schema import AuthTestErrorSchema
from openapi_server.models.auth_test_success_schema import AuthTestSuccessSchema


pytestmark = pytest.mark.asyncio

async def test_auth_revoke(client):
    """Test case for auth_revoke

    
    """
    params = [('token', 'token_example'),
                    ('test', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/auth.revoke',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_test(client):
    """Test case for auth_test

    
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/auth.test',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

