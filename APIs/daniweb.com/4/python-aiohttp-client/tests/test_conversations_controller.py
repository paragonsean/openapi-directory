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

from openapi_server.models.endpoint_get_conversations_id import EndpointGetConversationsID
from openapi_server.models.endpoint_get_conversations_id_messages import EndpointGetConversationsIDMessages
from openapi_server.models.endpoint_get_conversations_id_statuses import EndpointGetConversationsIDStatuses
from openapi_server.models.endpoint_get_conversations_statuses import EndpointGetConversationsStatuses
from openapi_server.models.endpoint_patch_conversations_id_statuses import EndpointPatchConversationsIDStatuses
from openapi_server.models.endpoint_post_conversations_id_messages import EndpointPostConversationsIDMessages
from openapi_server.models.endpoint_post_conversations_id_schedules import EndpointPostConversationsIDSchedules
from openapi_server.models.endpoint_post_conversations_id_searches import EndpointPostConversationsIDSearches
from openapi_server.models.endpoint_post_conversations_schedules import EndpointPostConversationsSchedules
from openapi_server.models.endpoint_post_conversations_searches import EndpointPostConversationsSearches


pytestmark = pytest.mark.asyncio

async def test_conversations_id_messages_get(client):
    """Test case for conversations_id_messages_get

    
    """
    params = [('gt_message_id', 56),
                    ('exclude_self', False),
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
        path='/connect/api/v4/conversations/{id}/messages'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_conversations_id_messages_post(client):
    """Test case for conversations_id_messages_post

    
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
        path='/connect/api/v4/conversations/{id}/messages'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_conversations_id_schedules_post(client):
    """Test case for conversations_id_schedules_post

    
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
        path='/connect/api/v4/conversations/{id}/schedules'.format(id=[56]),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_conversations_id_searches_post(client):
    """Test case for conversations_id_searches_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('_date', '_date_example')
    data.add_field('gt_message_id', 56)
    data.add_field('limit', 50)
    data.add_field('offset', 0)
    data.add_field('query', 'query_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/conversations/{id}/searches'.format(id=[56]),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_id_statuses_get(client):
    """Test case for conversations_id_statuses_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/conversations/{id}/statuses'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_conversations_id_statuses_patch(client):
    """Test case for conversations_id_statuses_patch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('archived_status', True)
    response = await client.request(
        method='PATCH',
        path='/connect/api/v4/conversations/{id}/statuses'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_idget(client):
    """Test case for conversations_idget

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/conversations/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_conversations_schedules_post(client):
    """Test case for conversations_schedules_post

    
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
        path='/connect/api/v4/conversations/schedules',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_conversations_searches_post(client):
    """Test case for conversations_searches_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('_date', '_date_example')
    data.add_field('gt_message_id', 56)
    data.add_field('limit', 50)
    data.add_field('offset', 0)
    data.add_field('query', 'query_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/conversations/searches',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_statuses_get(client):
    """Test case for conversations_statuses_get

    
    """
    params = [('filter', 'filter_example'),
                    ('include_archived', False),
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
        path='/connect/api/v4/conversations/statuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

