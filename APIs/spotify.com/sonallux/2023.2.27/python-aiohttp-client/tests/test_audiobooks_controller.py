# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audiobook_object import AudiobookObject
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_audiobooks200_response import GetMultipleAudiobooks200Response
from openapi_server.models.paging_saved_audiobook_object import PagingSavedAudiobookObject
from openapi_server.models.paging_simplified_chapter_object import PagingSimplifiedChapterObject


pytestmark = pytest.mark.asyncio

async def test_check_users_saved_audiobooks(client):
    """Test case for check_users_saved_audiobooks

    Check User's Saved Audiobooks 
    """
    params = [('ids', '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/audiobooks/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_audiobook(client):
    """Test case for get_an_audiobook

    Get an Audiobook 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audiobooks/{id}'.format(id='7iHfbu1YPACw6oZPAFJtqe'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audiobook_chapters(client):
    """Test case for get_audiobook_chapters

    Get Audiobook Chapters 
    """
    params = [('market', 'ES'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audiobooks/{id}/chapters'.format(id='7iHfbu1YPACw6oZPAFJtqe'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_audiobooks(client):
    """Test case for get_multiple_audiobooks

    Get Several Audiobooks 
    """
    params = [('ids', '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe'),
                    ('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audiobooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_audiobooks(client):
    """Test case for get_users_saved_audiobooks

    Get User's Saved Audiobooks 
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/audiobooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_audiobooks_user(client):
    """Test case for remove_audiobooks_user

    Remove User's Saved Audiobooks 
    """
    params = [('ids', '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/audiobooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_audiobooks_user(client):
    """Test case for save_audiobooks_user

    Save Audiobooks for Current User 
    """
    params = [('ids', '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/audiobooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

