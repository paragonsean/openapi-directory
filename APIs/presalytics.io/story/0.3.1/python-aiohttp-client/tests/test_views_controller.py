# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.required_parameters_to_create_a_view import RequiredParametersToCreateAView
from openapi_server.models.view import View


pytestmark = pytest.mark.asyncio

async def test_sessions_id_views_get(client):
    """Test case for sessions_id_views_get

    Views: List Session Views
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/sessions/{session_id}/views'.format(session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sessions_id_views_post(client):
    """Test case for sessions_id_views_post

    Views: Create A Session View
    """
    body = openapi_server.RequiredParametersToCreateAView()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/sessions/{session_id}/views'.format(session_id='session_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_id_delete(client):
    """Test case for views_id_delete

    Views: Delete by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/story/views/{view_id}'.format(view_id='view_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_id_get(client):
    """Test case for views_id_get

    Views: Get View
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/views/{view_id}'.format(view_id='view_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

