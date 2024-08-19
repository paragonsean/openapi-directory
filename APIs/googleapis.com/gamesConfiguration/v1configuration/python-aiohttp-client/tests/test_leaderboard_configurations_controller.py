# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.leaderboard_configuration import LeaderboardConfiguration
from openapi_server.models.leaderboard_configuration_list_response import LeaderboardConfigurationListResponse


pytestmark = pytest.mark.asyncio

async def test_games_configuration_leaderboard_configurations_delete(client):
    """Test case for games_configuration_leaderboard_configurations_delete

    
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
        path='/games/v1configuration/leaderboards/{leaderboard_id}'.format(leaderboard_id='leaderboard_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_leaderboard_configurations_get(client):
    """Test case for games_configuration_leaderboard_configurations_get

    
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
        path='/games/v1configuration/leaderboards/{leaderboard_id}'.format(leaderboard_id='leaderboard_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_leaderboard_configurations_insert(client):
    """Test case for games_configuration_leaderboard_configurations_insert

    
    """
    body = {"kind":"kind","draft":{"kind":"kind","scoreFormat":{"numberFormatType":"NUMBER_FORMAT_TYPE_UNSPECIFIED","numDecimalPlaces":0,"suffix":{"zero":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"other":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"one":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"few":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"many":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"two":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]}},"currencyCode":"currencyCode"},"sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"scoreOrder":"SCORE_ORDER_UNSPECIFIED","id":"id","published":{"kind":"kind","scoreFormat":{"numberFormatType":"NUMBER_FORMAT_TYPE_UNSPECIFIED","numDecimalPlaces":0,"suffix":{"zero":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"other":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"one":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"few":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"many":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"two":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]}},"currencyCode":"currencyCode"},"sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"scoreMax":"scoreMax","scoreMin":"scoreMin","token":"token"}
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
        path='/games/v1configuration/applications/{application_id}/leaderboards'.format(application_id='application_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_leaderboard_configurations_list(client):
    """Test case for games_configuration_leaderboard_configurations_list

    
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
        path='/games/v1configuration/applications/{application_id}/leaderboards'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_configuration_leaderboard_configurations_update(client):
    """Test case for games_configuration_leaderboard_configurations_update

    
    """
    body = {"kind":"kind","draft":{"kind":"kind","scoreFormat":{"numberFormatType":"NUMBER_FORMAT_TYPE_UNSPECIFIED","numDecimalPlaces":0,"suffix":{"zero":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"other":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"one":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"few":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"many":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"two":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]}},"currencyCode":"currencyCode"},"sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"scoreOrder":"SCORE_ORDER_UNSPECIFIED","id":"id","published":{"kind":"kind","scoreFormat":{"numberFormatType":"NUMBER_FORMAT_TYPE_UNSPECIFIED","numDecimalPlaces":0,"suffix":{"zero":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"other":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"one":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"few":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"many":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"two":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]}},"currencyCode":"currencyCode"},"sortRank":6,"name":{"kind":"kind","translations":[{"kind":"kind","locale":"locale","value":"value"},{"kind":"kind","locale":"locale","value":"value"}]},"iconUrl":"iconUrl"},"scoreMax":"scoreMax","scoreMin":"scoreMin","token":"token"}
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
        path='/games/v1configuration/leaderboards/{leaderboard_id}'.format(leaderboard_id='leaderboard_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

