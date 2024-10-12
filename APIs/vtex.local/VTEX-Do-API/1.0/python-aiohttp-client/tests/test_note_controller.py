# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_note_request import NewNoteRequest


pytestmark = pytest.mark.asyncio

async def test_get_note(client):
    """Test case for get_note

    Retrieve Note
    """
    params = [('reason', 'data-validation')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/notes/{note_id}'.format(note_id='654321cba'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notesbyorder_id(client):
    """Test case for get_notesbyorder_id

    Get Notes by orderId
    """
    params = [('target.id', '1172452900788-01'),
                    ('perPage', 20),
                    ('page', 3),
                    ('reason', 'data-validation')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/notes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_new_note(client):
    """Test case for new_note

    Create Note
    """
    body = {"domain":"domain","description":"description","target":{"id":"id","type":"type","url":"url"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/notes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

