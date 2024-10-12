# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.colors import Colors


pytestmark = pytest.mark.asyncio

async def test_calendar_colors_get(client):
    """Test case for calendar_colors_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendar/v3/colors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

