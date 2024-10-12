# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audio import Audio
from openapi_server.models.audio_data_list import AudioDataList
from openapi_server.models.audio_search_results import AudioSearchResults
from openapi_server.models.audio_url import AudioUrl
from openapi_server.models.collection import Collection
from openapi_server.models.collection_create_request import CollectionCreateRequest
from openapi_server.models.collection_create_response import CollectionCreateResponse
from openapi_server.models.collection_data_list import CollectionDataList
from openapi_server.models.collection_item_data_list import CollectionItemDataList
from openapi_server.models.collection_item_request import CollectionItemRequest
from openapi_server.models.collection_update_request import CollectionUpdateRequest
from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.genre_list import GenreList
from openapi_server.models.instrument_list import InstrumentList
from openapi_server.models.license_audio_request import LicenseAudioRequest
from openapi_server.models.license_audio_result_data_list import LicenseAudioResultDataList
from openapi_server.models.mood_list import MoodList


pytestmark = pytest.mark.asyncio

async def test_add_track_collection_items(client):
    """Test case for add_track_collection_items

    Add audio tracks to collections
    """
    body = {"items":[{"added_time":"2020-05-29T12:10:22-05:00","id":"1690105108","media_type":"image"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/audio/collections/{id}/items'.format(id='48433115'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_track_collection(client):
    """Test case for create_track_collection

    Create audio collections
    """
    body = {"name":"Test Collection 19cf"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/audio/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_track_collection(client):
    """Test case for delete_track_collection

    Delete audio collections
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/audio/collections/{id}'.format(id='48433111'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_track_collection_items(client):
    """Test case for delete_track_collection_items

    Remove audio tracks from collections
    """
    params = [('item_id', ['[\"76688182\",\"40005859\"]'])]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/audio/collections/{id}/items'.format(id='48433119'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_tracks(client):
    """Test case for download_tracks

    Download audio tracks
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/audio/licenses/{id}/downloads'.format(id='e123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_track(client):
    """Test case for get_track

    Get details about audio tracks
    """
    params = [('view', full),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/{id}'.format(id=442583),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_track_collection(client):
    """Test case for get_track_collection

    Get the details of audio collections
    """
    params = [('embed', ['embed_example']),
                    ('share_code', 'share_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/collections/{id}'.format(id='48433107'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_track_collection_items(client):
    """Test case for get_track_collection_items

    Get the contents of audio collections
    """
    params = [('page', 1),
                    ('per_page', 100),
                    ('share_code', 'share_code_example'),
                    ('sort', oldest)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/collections/{id}/items'.format(id='126351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_track_collection_list(client):
    """Test case for get_track_collection_list

    List audio collections
    """
    params = [('page', 1),
                    ('per_page', 100),
                    ('embed', ['share_code'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_track_license_list(client):
    """Test case for get_track_license_list

    List audio licenses
    """
    params = [('audio_id', '1'),
                    ('license', '48433107'),
                    ('page', 1),
                    ('per_page', 20),
                    ('sort', newest),
                    ('username', 'aUniqueUsername'),
                    ('start_date', '2021-03-29T13:25:13.521Z'),
                    ('end_date', '2021-03-29T13:25:13.521Z'),
                    ('download_availability', all),
                    ('team_history', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_track_list(client):
    """Test case for get_track_list

    List audio tracks
    """
    params = [('id', ['[\"442583\",\"434750\"]']),
                    ('view', minimal),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_license_track(client):
    """Test case for license_track

    License audio tracks
    """
    body = {"audio":[{"audio_id":"591623","license":"audio_platform","metadata":{"customer_id":"12345"}}]}
    params = [('license', 'audio_platform'),
                    ('search_id', 'p5S6QwRikdFJTHXwsoiqTg')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/audio/licenses',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_genres(client):
    """Test case for list_genres

    List audio genres
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/genres',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_instruments(client):
    """Test case for list_instruments

    List audio instruments
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/instruments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_moods(client):
    """Test case for list_moods

    List audio moods
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/moods',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_track_collection(client):
    """Test case for rename_track_collection

    Rename audio collections
    """
    body = {"name":"My collection with a new name"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/audio/collections/{id}'.format(id='48433107'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_tracks(client):
    """Test case for search_tracks

    Search for tracks
    """
    params = [('artists', ['artists_example']),
                    ('bpm', 56),
                    ('bpm_from', 80),
                    ('bpm_to', 120),
                    ('duration', 180),
                    ('duration_from', 30),
                    ('duration_to', 180),
                    ('genre', ['[\"Classical\",\"Holiday\"]']),
                    ('is_instrumental', true),
                    ('instruments', ['[\"Trumpet\",\"Percussion\"]']),
                    ('moods', ['[\"Confident\",\"Playful\"]']),
                    ('page', 1),
                    ('per_page', 20),
                    ('query', 'drum'),
                    ('sort', 'score'),
                    ('sort_order', desc),
                    ('vocal_description', 'female'),
                    ('view', minimal),
                    ('fields', 'fields_example'),
                    ('library', premier),
                    ('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/audio/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

