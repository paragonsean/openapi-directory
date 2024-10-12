# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_session_request import CreateSessionRequest
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.session import Session


pytestmark = pytest.mark.asyncio

async def test_session_id_delete(client):
    """Test case for session_id_delete

    Sessions: Delete by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/story/sessions/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_session_id_get(client):
    """Test case for session_id_get

    Sessions: Get
    """
    params = [('include_relationships', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/sessions/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_session_post(client):
    """Test case for story_id_session_post

    Sessions: Create a Session
    """
    body = openapi_server.CreateSessionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/{id}/sessions'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_sessions_get(client):
    """Test case for story_id_sessions_get

    Sessions: List Story Sessions
    """
    params = [('include_relationships', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/sessions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

