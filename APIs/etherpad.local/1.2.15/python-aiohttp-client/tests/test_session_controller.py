# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_session_using_get200_response import CreateSessionUsingGET200Response
from openapi_server.models.get_session_info_using_get200_response import GetSessionInfoUsingGET200Response


pytestmark = pytest.mark.asyncio

async def test_create_session_using_get(client):
    """Test case for create_session_using_get

    creates a new session. validUntil is an unix timestamp in seconds
    """
    params = [('groupID', 'group_id_example'),
                    ('authorID', 'author_id_example'),
                    ('validUntil', 'valid_until_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createSession',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_session_using_post(client):
    """Test case for create_session_using_post

    creates a new session. validUntil is an unix timestamp in seconds
    """
    params = [('groupID', 'group_id_example'),
                    ('authorID', 'author_id_example'),
                    ('validUntil', 'valid_until_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createSession',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_session_using_get(client):
    """Test case for delete_session_using_get

    deletes a session
    """
    params = [('sessionID', 'session_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/deleteSession',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_session_using_post(client):
    """Test case for delete_session_using_post

    deletes a session
    """
    params = [('sessionID', 'session_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/deleteSession',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session_info_using_get(client):
    """Test case for get_session_info_using_get

    returns informations about a session
    """
    params = [('sessionID', 'session_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getSessionInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session_info_using_post(client):
    """Test case for get_session_info_using_post

    returns informations about a session
    """
    params = [('sessionID', 'session_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getSessionInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

