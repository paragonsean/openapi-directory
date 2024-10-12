# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.game_center_enabled_version_compatible_versions_linkages_request import GameCenterEnabledVersionCompatibleVersionsLinkagesRequest
from openapi_server.models.game_center_enabled_version_compatible_versions_linkages_response import GameCenterEnabledVersionCompatibleVersionsLinkagesResponse
from openapi_server.models.game_center_enabled_versions_response import GameCenterEnabledVersionsResponse


pytestmark = pytest.mark.asyncio

async def test_game_center_enabled_versions_compatible_versions_create_to_many_relationship(client):
    """Test case for game_center_enabled_versions_compatible_versions_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"gameCenterEnabledVersions"},{"id":"id","type":"gameCenterEnabledVersions"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_game_center_enabled_versions_compatible_versions_delete_to_many_relationship(client):
    """Test case for game_center_enabled_versions_compatible_versions_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"gameCenterEnabledVersions"},{"id":"id","type":"gameCenterEnabledVersions"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_game_center_enabled_versions_compatible_versions_get_to_many_related(client):
    """Test case for game_center_enabled_versions_compatible_versions_get_to_many_related

    
    """
    params = [('filter[platform]', ['filter_platform_example']),
                    ('filter[versionString]', ['filter_version_string_example']),
                    ('filter[app]', ['filter_app_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[gameCenterEnabledVersions]', ['fields_game_center_enabled_versions_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/gameCenterEnabledVersions/{id}/compatibleVersions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_game_center_enabled_versions_compatible_versions_get_to_many_relationship(client):
    """Test case for game_center_enabled_versions_compatible_versions_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_game_center_enabled_versions_compatible_versions_replace_to_many_relationship(client):
    """Test case for game_center_enabled_versions_compatible_versions_replace_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"gameCenterEnabledVersions"},{"id":"id","type":"gameCenterEnabledVersions"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

