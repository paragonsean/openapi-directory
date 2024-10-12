# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.note import Note


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_notes_get(client):
    """Test case for workspace_slug_members_member_slug_notes_get

    Get the member's notes
    """
    params = [('page', 'page_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/members/{member_slug}/notes'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_notes_id_put(client):
    """Test case for workspace_slug_members_member_slug_notes_id_put

    Update a note
    """
    body = openapi_server.Note()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/{workspace_slug}/members/{member_slug}/notes/{id}'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_notes_post(client):
    """Test case for workspace_slug_members_member_slug_notes_post

    Create a note
    """
    body = openapi_server.Note()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{workspace_slug}/members/{member_slug}/notes'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

