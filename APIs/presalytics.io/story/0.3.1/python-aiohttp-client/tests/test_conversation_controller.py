# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message import Message
from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_story_id_messages_get(client):
    """Test case for story_id_messages_get

    Conversation: List Conversation Messages
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/messages'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_messages_post(client):
    """Test case for story_id_messages_post

    Conversation: Send a Message
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/{id}/messages'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

