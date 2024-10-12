# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.message_entity import MessageEntity


pytestmark = pytest.mark.asyncio

async def test_delete_messages_id(client):
    """Test case for delete_messages_id

    Delete Message
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/messages/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_messages(client):
    """Test case for get_messages

    List Messages
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('project_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_messages_id(client):
    """Test case for get_messages_id

    Show Message
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/messages/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_messages_id(client):
    """Test case for patch_messages_id

    Update Message
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    data.add_field('project_id', 56)
    data.add_field('subject', 'subject_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/messages/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_messages(client):
    """Test case for post_messages

    Create Message
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    data.add_field('project_id', 56)
    data.add_field('subject', 'subject_example')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/messages',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

