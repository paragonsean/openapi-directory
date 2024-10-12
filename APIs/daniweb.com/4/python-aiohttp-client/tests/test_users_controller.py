# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.endpoint_get_users import EndpointGetUsers
from openapi_server.models.endpoint_get_users_id import EndpointGetUsersID
from openapi_server.models.endpoint_get_users_id_groups import EndpointGetUsersIDGroups
from openapi_server.models.endpoint_get_users_id_groups_messages import EndpointGetUsersIDGroupsMessages
from openapi_server.models.endpoint_get_users_id_metadata import EndpointGetUsersIDMetadata
from openapi_server.models.endpoint_get_users_id_metadata_collections import EndpointGetUsersIDMetadataCollections
from openapi_server.models.endpoint_get_users_id_positions import EndpointGetUsersIDPositions
from openapi_server.models.endpoint_get_users_id_synergies import EndpointGetUsersIDSynergies
from openapi_server.models.endpoint_get_users_nearby import EndpointGetUsersNearby
from openapi_server.models.endpoint_patch_users import EndpointPatchUsers
from openapi_server.models.endpoint_patch_users_id_synergies import EndpointPatchUsersIDSynergies
from openapi_server.models.endpoint_post_users_id_messages import EndpointPostUsersIDMessages
from openapi_server.models.endpoint_post_users_id_metadata import EndpointPostUsersIDMetadata
from openapi_server.models.endpoint_post_users_invites import EndpointPostUsersInvites
from openapi_server.models.endpoint_post_users_metadata_filters import EndpointPostUsersMetadataFilters
from openapi_server.models.endpoint_post_users_searches import EndpointPostUsersSearches


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    params = [('filter', connections),
                    ('order_by', id),
                    ('bubbled', False),
                    ('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_0(client):
    """Test case for users_get_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/~',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_groups_get(client):
    """Test case for users_id_groups_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/{id}/groups'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_groups_messages_get(client):
    """Test case for users_id_groups_messages_get

    
    """
    params = [('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/{id}/groups/messages'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_id_messages_post(client):
    """Test case for users_id_messages_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('bubbled', False)
    data.add_field('metadata_0_key', 'metadata_0_key_example')
    data.add_field('metadata_0_privacy', 'metadata_0_privacy_example')
    data.add_field('metadata_0_values', ['metadata_0_values_example'])
    data.add_field('metadata_1_key', 'metadata_1_key_example')
    data.add_field('metadata_1_privacy', 'metadata_1_privacy_example')
    data.add_field('metadata_1_values', ['metadata_1_values_example'])
    data.add_field('metadata_2_key', 'metadata_2_key_example')
    data.add_field('metadata_2_privacy', 'metadata_2_privacy_example')
    data.add_field('metadata_2_values', ['metadata_2_values_example'])
    data.add_field('text_emoticons', False)
    data.add_field('text_raw', 'text_raw_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/users/{id}/messages'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_metadata_collections_get(client):
    """Test case for users_id_metadata_collections_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/{id}/metadata/collections'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_metadata_get(client):
    """Test case for users_id_metadata_get

    
    """
    params = [('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/{id}/metadata'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_id_metadata_post(client):
    """Test case for users_id_metadata_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('metadata_0_key', 'metadata_0_key_example')
    data.add_field('metadata_0_privacy', 'metadata_0_privacy_example')
    data.add_field('metadata_0_values', ['metadata_0_values_example'])
    data.add_field('metadata_1_key', 'metadata_1_key_example')
    data.add_field('metadata_1_privacy', 'metadata_1_privacy_example')
    data.add_field('metadata_1_values', ['metadata_1_values_example'])
    data.add_field('metadata_2_key', 'metadata_2_key_example')
    data.add_field('metadata_2_privacy', 'metadata_2_privacy_example')
    data.add_field('metadata_2_values', ['metadata_2_values_example'])
    response = await client.request(
        method='POST',
        path='/connect/api/v4/users/{id}/metadata'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_positions_get(client):
    """Test case for users_id_positions_get

    
    """
    params = [('bubbled', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/{id}/positions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_synergies_get(client):
    """Test case for users_id_synergies_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/{id}/synergies'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_id_synergies_patch(client):
    """Test case for users_id_synergies_patch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('relationship_muted', True)
    data.add_field('relationship_skipped', True)
    response = await client.request(
        method='PATCH',
        path='/connect/api/v4/users/{id}/synergies'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_idget(client):
    """Test case for users_idget

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_invites_post(client):
    """Test case for users_invites_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('csv', '/path/to/file')
    data.add_field('emails', ['emails_example'])
    response = await client.request(
        method='POST',
        path='/connect/api/v4/users/invites',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_metadata_filters_post(client):
    """Test case for users_metadata_filters_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('limit', 50)
    data.add_field('metadata_0_key', 'metadata_0_key_example')
    data.add_field('metadata_0_values', ['metadata_0_values_example'])
    data.add_field('metadata_1_key', 'metadata_1_key_example')
    data.add_field('metadata_1_values', ['metadata_1_values_example'])
    data.add_field('metadata_2_key', 'metadata_2_key_example')
    data.add_field('metadata_2_values', ['metadata_2_values_example'])
    data.add_field('offset', 0)
    response = await client.request(
        method='POST',
        path='/connect/api/v4/users/metadata/filters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_nearby_get(client):
    """Test case for users_nearby_get

    
    """
    params = [('latitude', 3.4),
                    ('longitude', 3.4),
                    ('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/users/nearby',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_patch(client):
    """Test case for users_patch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('company', 'company_example')
    data.add_field('company_size', 'company_size_example')
    data.add_field('first_name', 'first_name_example')
    data.add_field('goals', ['goals_example'])
    data.add_field('headline', 'headline_example')
    data.add_field('industry', 'industry_example')
    data.add_field('introduction', 'introduction_example')
    data.add_field('job_position', 'job_position_example')
    data.add_field('last_name', 'last_name_example')
    data.add_field('location_importance', 'location_importance_example')
    data.add_field('match_tags', ['match_tags_example'])
    data.add_field('pitch', 'pitch_example')
    data.add_field('tags', ['tags_example'])
    data.add_field('targeted_industry', 'targeted_industry_example')
    data.add_field('url', 'url_example')
    response = await client.request(
        method='PATCH',
        path='/connect/api/v4/users/~',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_users_searches_post(client):
    """Test case for users_searches_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('active_within_x_days', 56)
    data.add_field('audience_ids', [56])
    data.add_field('bubbled', False)
    data.add_field('exclude_connections', False)
    data.add_field('exclude_matches', False)
    data.add_field('exclude_muted', False)
    data.add_field('exclude_skipped', False)
    data.add_field('geo_latitude', 3.4)
    data.add_field('geo_longitude', 3.4)
    data.add_field('geo_miles_away', 3.4)
    data.add_field('group_id', 56)
    data.add_field('limit', 50)
    data.add_field('location_city_query', 'location_city_query_example')
    data.add_field('location_city_weight', 56)
    data.add_field('location_country_query', 'location_country_query_example')
    data.add_field('location_country_weight', 56)
    data.add_field('location_region_query', 'location_region_query_example')
    data.add_field('location_region_weight', 56)
    data.add_field('metadata_0_key', 'metadata_0_key_example')
    data.add_field('metadata_0_query', 'metadata_0_query_example')
    data.add_field('metadata_0_weight', 56)
    data.add_field('metadata_1_key', 'metadata_1_key_example')
    data.add_field('metadata_1_query', 'metadata_1_query_example')
    data.add_field('metadata_1_weight', 56)
    data.add_field('metadata_2_key', 'metadata_2_key_example')
    data.add_field('metadata_2_query', 'metadata_2_query_example')
    data.add_field('metadata_2_weight', 56)
    data.add_field('offset', 0)
    data.add_field('position_organization_query', 'position_organization_query_example')
    data.add_field('position_organization_weight', 56)
    data.add_field('position_role_query', 'position_role_query_example')
    data.add_field('position_role_weight', 56)
    data.add_field('position_summary_query', 'position_summary_query_example')
    data.add_field('position_summary_weight', 56)
    data.add_field('profile_first_name_query', 'profile_first_name_query_example')
    data.add_field('profile_first_name_weight', 56)
    data.add_field('profile_goals_query', 'profile_goals_query_example')
    data.add_field('profile_goals_weight', 'profile_goals_weight_example')
    data.add_field('profile_headline_query', 'profile_headline_query_example')
    data.add_field('profile_headline_weight', 56)
    data.add_field('profile_industry_query', 'profile_industry_query_example')
    data.add_field('profile_industry_weight', 56)
    data.add_field('profile_last_name_query', 'profile_last_name_query_example')
    data.add_field('profile_last_name_weight', 56)
    data.add_field('profile_pitch_query', 'profile_pitch_query_example')
    data.add_field('profile_pitch_weight', 56)
    response = await client.request(
        method='POST',
        path='/connect/api/v4/users/searches',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

