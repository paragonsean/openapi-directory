# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_ekm_list_original_connected_channel_info(client):
    """Test case for admin_conversations_ekm_list_original_connected_channel_info

    
    """
    params = [('token', 'token_example'),
                    ('channel_ids', 'channel_ids_example'),
                    ('team_ids', 'team_ids_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.ekm.listOriginalConnectedChannelInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

