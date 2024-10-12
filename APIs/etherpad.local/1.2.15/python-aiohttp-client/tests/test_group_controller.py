# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_group_using_get200_response import CreateGroupUsingGET200Response
from openapi_server.models.list_all_groups_using_get200_response import ListAllGroupsUsingGET200Response
from openapi_server.models.list_all_pads_using_get200_response import ListAllPadsUsingGET200Response
from openapi_server.models.list_sessions_of_author_using_get200_response import ListSessionsOfAuthorUsingGET200Response


pytestmark = pytest.mark.asyncio

async def test_create_group_if_not_exists_for_using_get(client):
    """Test case for create_group_if_not_exists_for_using_get

    this functions helps you to map your application group ids to Etherpad group ids
    """
    params = [('groupMapper', 'group_mapper_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createGroupIfNotExistsFor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group_if_not_exists_for_using_post(client):
    """Test case for create_group_if_not_exists_for_using_post

    this functions helps you to map your application group ids to Etherpad group ids
    """
    params = [('groupMapper', 'group_mapper_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createGroupIfNotExistsFor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group_pad_using_get(client):
    """Test case for create_group_pad_using_get

    creates a new pad in this group
    """
    params = [('groupID', 'group_id_example'),
                    ('padName', 'pad_name_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createGroupPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group_pad_using_post(client):
    """Test case for create_group_pad_using_post

    creates a new pad in this group
    """
    params = [('groupID', 'group_id_example'),
                    ('padName', 'pad_name_example'),
                    ('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createGroupPad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group_using_get(client):
    """Test case for create_group_using_get

    creates a new group
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createGroup',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group_using_post(client):
    """Test case for create_group_using_post

    creates a new group
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createGroup',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group_using_get(client):
    """Test case for delete_group_using_get

    deletes a group
    """
    params = [('groupID', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/deleteGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group_using_post(client):
    """Test case for delete_group_using_post

    deletes a group
    """
    params = [('groupID', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/deleteGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_groups_using_get(client):
    """Test case for list_all_groups_using_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listAllGroups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_groups_using_post(client):
    """Test case for list_all_groups_using_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listAllGroups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pads_using_get(client):
    """Test case for list_pads_using_get

    returns all pads of this group
    """
    params = [('groupID', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listPads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pads_using_post(client):
    """Test case for list_pads_using_post

    returns all pads of this group
    """
    params = [('groupID', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listPads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sessions_of_group_using_get(client):
    """Test case for list_sessions_of_group_using_get

    
    """
    params = [('groupID', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listSessionsOfGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sessions_of_group_using_post(client):
    """Test case for list_sessions_of_group_using_post

    
    """
    params = [('groupID', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listSessionsOfGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

