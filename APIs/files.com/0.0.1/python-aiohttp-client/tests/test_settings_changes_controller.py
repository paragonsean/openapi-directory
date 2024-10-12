# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.settings_change_entity import SettingsChangeEntity


pytestmark = pytest.mark.asyncio

async def test_get_settings_changes(client):
    """Test case for get_settings_changes

    List Settings Changes
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('api_key_id', 'api_key_id_example'),
                    ('user_id', 'user_id_example'),
                    ('filter', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/settings_changes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

