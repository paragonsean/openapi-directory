# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_users_list(client):
    """Test case for apps_permissions_users_list

    
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
        path='/api/apps.permissions.users.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_permissions_users_request(client):
    """Test case for apps_permissions_users_request

    
    """
    params = [('token', 'token_example'),
                    ('scopes', 'scopes_example'),
                    ('trigger_id', 'trigger_id_example'),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/apps.permissions.users.request',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

