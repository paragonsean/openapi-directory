# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_author_using_get200_response import CreateAuthorUsingGET200Response
from openapi_server.models.get_author_name_using_get200_response import GetAuthorNameUsingGET200Response
from openapi_server.models.list_all_pads_using_get200_response import ListAllPadsUsingGET200Response
from openapi_server.models.list_sessions_of_author_using_get200_response import ListSessionsOfAuthorUsingGET200Response


pytestmark = pytest.mark.asyncio

async def test_create_author_if_not_exists_for_using_get(client):
    """Test case for create_author_if_not_exists_for_using_get

    this functions helps you to map your application author ids to Etherpad author ids
    """
    params = [('authorMapper', 'author_mapper_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createAuthorIfNotExistsFor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_author_if_not_exists_for_using_post(client):
    """Test case for create_author_if_not_exists_for_using_post

    this functions helps you to map your application author ids to Etherpad author ids
    """
    params = [('authorMapper', 'author_mapper_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createAuthorIfNotExistsFor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_author_using_get(client):
    """Test case for create_author_using_get

    creates a new author
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/createAuthor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_author_using_post(client):
    """Test case for create_author_using_post

    creates a new author
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/createAuthor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_author_name_using_get(client):
    """Test case for get_author_name_using_get

    Returns the Author Name of the author
    """
    params = [('authorID', 'author_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/getAuthorName',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_author_name_using_post(client):
    """Test case for get_author_name_using_post

    Returns the Author Name of the author
    """
    params = [('authorID', 'author_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/getAuthorName',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pads_of_author_using_get(client):
    """Test case for list_pads_of_author_using_get

    returns an array of all pads this author contributed to
    """
    params = [('authorID', 'author_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listPadsOfAuthor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pads_of_author_using_post(client):
    """Test case for list_pads_of_author_using_post

    returns an array of all pads this author contributed to
    """
    params = [('authorID', 'author_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listPadsOfAuthor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sessions_of_author_using_get(client):
    """Test case for list_sessions_of_author_using_get

    returns all sessions of an author
    """
    params = [('authorID', 'author_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/listSessionsOfAuthor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sessions_of_author_using_post(client):
    """Test case for list_sessions_of_author_using_post

    returns all sessions of an author
    """
    params = [('authorID', 'author_id_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/listSessionsOfAuthor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

