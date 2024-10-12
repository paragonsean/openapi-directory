# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.display_preferences_dto import DisplayPreferencesDto


pytestmark = pytest.mark.asyncio

async def test_get_display_preferences(client):
    """Test case for get_display_preferences

    Get Display Preferences.
    """
    params = [('userId', 'user_id_example'),
                    ('client', 'client_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/DisplayPreferences/{display_preferences_id}'.format(display_preferences_id='display_preferences_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_display_preferences(client):
    """Test case for update_display_preferences

    Update Display Preferences.
    """
    body = {"RememberSorting":True,"RememberIndexing":True,"PrimaryImageWidth":6,"ScrollDirection":"Horizontal","IndexBy":"IndexBy","ShowBackdrop":True,"SortBy":"SortBy","ShowSidebar":True,"SortOrder":"Ascending","PrimaryImageHeight":0,"Id":"Id","Client":"Client","CustomPrefs":{"key":"CustomPrefs"},"ViewType":"ViewType"}
    params = [('userId', 'user_id_example'),
                    ('client', 'client_example')]
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DisplayPreferences/{display_preferences_id}'.format(display_preferences_id='display_preferences_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

