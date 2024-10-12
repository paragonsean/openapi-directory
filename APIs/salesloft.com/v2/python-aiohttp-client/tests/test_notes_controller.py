# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.note import Note
from openapi_server.models.person import Person


pytestmark = pytest.mark.asyncio

async def test_v2_notes_id_json_delete(client):
    """Test case for v2_notes_id_json_delete

    Delete a note
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/notes/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_notes_id_json_get(client):
    """Test case for v2_notes_id_json_get

    Fetch a note
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/notes/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_notes_id_json_put(client):
    """Test case for v2_notes_id_json_put

    Update a note
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'call_id': 56,
        'content': 'content_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/notes/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_notes_json_get(client):
    """Test case for v2_notes_json_get

    List notes
    """
    params = [('associated_with_type', 'associated_with_type_example'),
                    ('associated_with_id', 56),
                    ('updated_at', ['updated_at_example']),
                    ('ids', [56]),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/notes.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_notes_json_post(client):
    """Test case for v2_notes_json_post

    Create a note
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'associated_with_id': 56,
        'associated_with_type': 'associated_with_type_example',
        'call_id': 56,
        'content': 'content_example',
        'skip_crm_sync': True,
        'subject': 'subject_example',
        'user_guid': 'user_guid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/notes.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

