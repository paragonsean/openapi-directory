# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_settings_update_response import ListSettingsUpdateResponse
from openapi_server.models.settings_update_enum_status import SettingsUpdateEnumStatus


pytestmark = pytest.mark.asyncio

async def test_list_settings_update(client):
    """Test case for list_settings_update

    
    """
    params = [('Sim', 'sim_example'),
                    ('Status', openapi_server.SettingsUpdateEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/SettingsUpdates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

