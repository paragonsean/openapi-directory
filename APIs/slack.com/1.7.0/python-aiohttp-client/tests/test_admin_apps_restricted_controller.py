# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_admin_apps_restricted_list(client):
    """Test case for admin_apps_restricted_list

    
    """
    params = [('token', 'token_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('team_id', 'team_id_example'),
                    ('enterprise_id', 'enterprise_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.apps.restricted.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

