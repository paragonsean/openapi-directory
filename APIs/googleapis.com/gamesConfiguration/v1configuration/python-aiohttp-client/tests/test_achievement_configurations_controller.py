# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.achievement_configuration import AchievementConfiguration
from openapi_server.models.achievement_configuration_list_response import AchievementConfigurationListResponse


pytestmark = pytest.mark.asyncio

async def test_games_configuration_achievement_configurations_delete(client):
    """Test case for games_configuration_achievement_configurations_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/games/v1configuration/achievements/{achievement_id}'.format(achievement_id='achievement_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_achievement_configurations_get(client):
    """Test case for games_configuration_achievement_configurations_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/games/v1configuration/achievements/{achievement_id}'.format(achievement_id='achievement_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_achievement_configurations_insert(client):
    """Test case for games_configuration_achievement_configurations_insert

    
    """
    body = {"achievementType":"ACHIEVEMENT_TYPE_UNSPECIFIED","stepsToUnlock":1,"initialState":"INITIAL_STATE_UNSPECIFIED","kind":"kind","draft":{"pointValue":0,"kind":"kind","sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"description":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"id":"id","published":{"pointValue":0,"kind":"kind","sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"description":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"token":"token"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/games/v1configuration/applications/{application_id}/achievements'.format(application_id='application_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_achievement_configurations_list(client):
    """Test case for games_configuration_achievement_configurations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/games/v1configuration/applications/{application_id}/achievements'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_achievement_configurations_update(client):
    """Test case for games_configuration_achievement_configurations_update

    
    """
    body = {"achievementType":"ACHIEVEMENT_TYPE_UNSPECIFIED","stepsToUnlock":1,"initialState":"INITIAL_STATE_UNSPECIFIED","kind":"kind","draft":{"pointValue":0,"kind":"kind","sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"description":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"id":"id","published":{"pointValue":0,"kind":"kind","sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"description":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"token":"token"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/games/v1configuration/achievements/{achievement_id}'.format(achievement_id='achievement_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

