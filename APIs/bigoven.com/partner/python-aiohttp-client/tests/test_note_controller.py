# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api2_controllers_web_api_note_controller_note_request import API2ControllersWebAPINoteControllerNoteRequest
from openapi_server.models.big_oven_model_api2_recipe_note import BigOvenModelAPI2RecipeNote
from openapi_server.models.big_oven_model_api_recipe_note import BigOvenModelAPIRecipeNote
from openapi_server.models.big_oven_model_api_recipe_note_list import BigOvenModelAPIRecipeNoteList


pytestmark = pytest.mark.asyncio

async def test_note_delete(client):
    """Test case for note_delete

    Delete a review                  do a DELETE Http request of /note/{ID}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/recipe/{recipe_id}/note/{note_id}'.format(recipe_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_note_get(client):
    """Test case for note_get

    Get a given note. Make sure you're passing authentication information in the header for the user who owns the note.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/note/{note_id}'.format(recipe_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_note_get_notes(client):
    """Test case for note_get_notes

    recipe/100/notes
    """
    params = [('pg', 56),
                    ('rpp', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/notes'.format(recipe_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_note_post(client):
    """Test case for note_post

    HTTP POST a new note into the system.
    """
    body = openapi_server.API2ControllersWebAPINoteControllerNoteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/{recipe_id}/note'.format(recipe_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_note_put(client):
    """Test case for note_put

    HTTP PUT (update) a Recipe note (RecipeNote).
    """
    body = openapi_server.API2ControllersWebAPINoteControllerNoteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/recipe/{recipe_id}/note/{note_id}'.format(recipe_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

