# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_embed_preset_alt1_request import EditEmbedPresetAlt1Request
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.presets import Presets


pytestmark = pytest.mark.asyncio

async def test_edit_embed_preset(client):
    """Test case for edit_embed_preset

    Edit an embed preset
    """
    body = openapi_server.EditEmbedPresetAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.preset+json',
        'Content-Type': 'application/vnd.vimeo.preset+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users/{user_id}/presets/{preset_id}'.format(preset_id=12345, user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_embed_preset_alt1(client):
    """Test case for edit_embed_preset_alt1

    Edit an embed preset
    """
    body = openapi_server.EditEmbedPresetAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.preset+json',
        'Content-Type': 'application/vnd.vimeo.preset+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/me/presets/{preset_id}'.format(preset_id=12345),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_embed_preset(client):
    """Test case for get_embed_preset

    Get a specific embed preset
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.preset+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/presets/{preset_id}'.format(preset_id=12345, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_embed_preset_alt1(client):
    """Test case for get_embed_preset_alt1

    Get a specific embed preset
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.preset+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/presets/{preset_id}'.format(preset_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_embed_presets(client):
    """Test case for get_embed_presets

    Get all the embed presets that a user has created
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.preset+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/presets'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_embed_presets_alt1(client):
    """Test case for get_embed_presets_alt1

    Get all the embed presets that a user has created
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.preset+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/presets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

