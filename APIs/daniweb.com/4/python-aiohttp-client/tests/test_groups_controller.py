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
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.endpoint_delete_groups_id_memberships import EndpointDeleteGroupsIDMemberships
from openapi_server.models.endpoint_delete_groups_messages_id import EndpointDeleteGroupsMessagesID
from openapi_server.models.endpoint_get_groups import EndpointGetGroups
from openapi_server.models.endpoint_get_groups_id import EndpointGetGroupsID
from openapi_server.models.endpoint_get_groups_id_memberships import EndpointGetGroupsIDMemberships
from openapi_server.models.endpoint_get_groups_id_messages import EndpointGetGroupsIDMessages
from openapi_server.models.endpoint_get_groups_id_statuses import EndpointGetGroupsIDStatuses
from openapi_server.models.endpoint_get_groups_messages_id import EndpointGetGroupsMessagesID
from openapi_server.models.endpoint_get_groups_messages_id_metadata import EndpointGetGroupsMessagesIDMetadata
from openapi_server.models.endpoint_get_groups_messages_id_metadata_collections import EndpointGetGroupsMessagesIDMetadataCollections
from openapi_server.models.endpoint_get_groups_statuses import EndpointGetGroupsStatuses
from openapi_server.models.endpoint_patch_groups_id import EndpointPatchGroupsID
from openapi_server.models.endpoint_patch_groups_id_memberships import EndpointPatchGroupsIDMemberships
from openapi_server.models.endpoint_post_groups import EndpointPostGroups
from openapi_server.models.endpoint_post_groups_id_memberships import EndpointPostGroupsIDMemberships
from openapi_server.models.endpoint_post_groups_id_messages import EndpointPostGroupsIDMessages
from openapi_server.models.endpoint_post_groups_id_schedules import EndpointPostGroupsIDSchedules
from openapi_server.models.endpoint_post_groups_messages_id_metadata import EndpointPostGroupsMessagesIDMetadata
from openapi_server.models.endpoint_post_groups_messages_metadata_filters import EndpointPostGroupsMessagesMetadataFilters
from openapi_server.models.endpoint_post_groups_schedules import EndpointPostGroupsSchedules


pytestmark = pytest.mark.asyncio

async def test_groups_get(client):
    """Test case for groups_get

    
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
        path='/connect/api/v4/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_id_memberships_delete(client):
    """Test case for groups_id_memberships_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/connect/api/v4/groups/{id}/memberships'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_id_memberships_get(client):
    """Test case for groups_id_memberships_get

    
    """
    params = [('moderators_only', False),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/groups/{id}/memberships'.format(id=[56]),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_id_memberships_patch(client):
    """Test case for groups_id_memberships_patch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('moderator', False)
    data.add_field('user_id', 56)
    response = await client.request(
        method='PATCH',
        path='/connect/api/v4/groups/{id}/memberships'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_id_memberships_post(client):
    """Test case for groups_id_memberships_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('passphrase', 'passphrase_example')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/connect/api/v4/groups/{id}/memberships'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_id_messages_get(client):
    """Test case for groups_id_messages_get

    
    """
    params = [('gt_message_id', 56),
                    ('exclude_self', False),
                    ('include_deleted', False),
                    ('date', '_date_example'),
                    ('bubbled', False),
                    ('record_seen', False),
                    ('timeout', 0),
                    ('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/groups/{id}/messages'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_id_messages_post(client):
    """Test case for groups_id_messages_post

    
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
    data.add_field('text_emoticons', False)
    data.add_field('text_raw', 'text_raw_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/groups/{id}/messages'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_id_schedules_post(client):
    """Test case for groups_id_schedules_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('_date', '_date_example')
    data.add_field('limit', 50)
    data.add_field('offset', 0)
    data.add_field('roll_up', False)
    data.add_field('sort', desc)
    response = await client.request(
        method='POST',
        path='/connect/api/v4/groups/{id}/schedules'.format(id=[56]),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_id_statuses_get(client):
    """Test case for groups_id_statuses_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/groups/{id}/statuses'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_idget(client):
    """Test case for groups_idget

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/groups/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_idpatch(client):
    """Test case for groups_idpatch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('name', 'name_example')
    data.add_field('passphrase', 'passphrase_example')
    data.add_field('privacy', 'privacy_example')
    data.add_field('slug', 'slug_example')
    response = await client.request(
        method='PATCH',
        path='/connect/api/v4/groups/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_messages_id_metadata_collections_get(client):
    """Test case for groups_messages_id_metadata_collections_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/groups/messages/{id}/metadata/collections'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_messages_id_metadata_get(client):
    """Test case for groups_messages_id_metadata_get

    
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
        path='/connect/api/v4/groups/messages/{id}/metadata'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_messages_id_metadata_post(client):
    """Test case for groups_messages_id_metadata_post

    
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
        path='/connect/api/v4/groups/messages/{id}/metadata'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_messages_iddelete(client):
    """Test case for groups_messages_iddelete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/connect/api/v4/groups/messages/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_messages_idget(client):
    """Test case for groups_messages_idget

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/groups/messages/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_messages_metadata_filters_post(client):
    """Test case for groups_messages_metadata_filters_post

    
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
        path='/connect/api/v4/groups/messages/metadata/filters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_post(client):
    """Test case for groups_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('name', 'name_example')
    data.add_field('passphrase', 'passphrase_example')
    data.add_field('privacy', 'privacy_example')
    data.add_field('slug', 'slug_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/groups',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_groups_schedules_post(client):
    """Test case for groups_schedules_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('_date', '_date_example')
    data.add_field('limit', 50)
    data.add_field('offset', 0)
    data.add_field('roll_up', False)
    data.add_field('sort', desc)
    response = await client.request(
        method='POST',
        path='/connect/api/v4/groups/schedules',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_statuses_get(client):
    """Test case for groups_statuses_get

    
    """
    params = [('existing_membership', False),
                    ('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/groups/statuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

