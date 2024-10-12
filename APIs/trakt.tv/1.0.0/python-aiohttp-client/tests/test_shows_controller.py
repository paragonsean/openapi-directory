# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_a_single_show(client):
    """Test case for get_a_single_show

    Get a single show
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_people_for_a_show(client):
    """Test case for get_all_people_for_a_show

    Get all people for a show
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/people'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_show_aliases(client):
    """Test case for get_all_show_aliases

    Get all show aliases
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/aliases'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_show_certifications(client):
    """Test case for get_all_show_certifications

    Get all show certifications
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/certifications'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_show_comments(client):
    """Test case for get_all_show_comments

    Get all show comments
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/comments/{sort}'.format(id='game-of-thrones', sort='newest'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_show_translations(client):
    """Test case for get_all_show_translations

    Get all show translations
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/translations/{language}'.format(id='game-of-thrones', language='es'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_episode(client):
    """Test case for get_last_episode

    Get last episode
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/last_episode'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_containing_this_show(client):
    """Test case for get_lists_containing_this_show

    Get lists containing this show
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/lists/{type}/{sort}'.format(id='game-of-thrones', type='personal', sort='popular'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_next_episode(client):
    """Test case for get_next_episode

    Get next episode
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/next_episode'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_popular_shows(client):
    """Test case for get_popular_shows

    Get popular shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/popular',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recently_updated_show_trakt_ids(client):
    """Test case for get_recently_updated_show_trakt_ids

    Get recently updated show Trakt IDs
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/updates/id/{start_date}'.format(start_date='2020-11-27T00:00:00Z'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recently_updated_shows(client):
    """Test case for get_recently_updated_shows

    Get recently updated shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/updates/{start_date}'.format(start_date='2020-11-27T00:00:00Z'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_related_shows(client):
    """Test case for get_related_shows

    Get related shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/related'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_show_collection_progress(client):
    """Test case for get_show_collection_progress

    Get show collection progress
    """
    body = 'body_example'
    params = [('hidden', 'false'),
                    ('specials', 'false'),
                    ('count_specials', 'true')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/progress/collection'.format(id='game-of-thrones'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_show_ratings(client):
    """Test case for get_show_ratings

    Get show ratings
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/ratings'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_show_stats(client):
    """Test case for get_show_stats

    Get show stats
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/stats'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_show_studios(client):
    """Test case for get_show_studios

    Get show studios
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/studios'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_show_watched_progress(client):
    """Test case for get_show_watched_progress

    Get show watched progress
    """
    body = 'body_example'
    params = [('hidden', 'false'),
                    ('specials', 'false'),
                    ('count_specials', 'true')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/progress/watched'.format(id='game-of-thrones'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_most_anticipated_shows(client):
    """Test case for get_the_most_anticipated_shows

    Get the most anticipated shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/anticipated',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_most_collected_shows(client):
    """Test case for get_the_most_collected_shows

    Get the most collected shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/collected/{period}'.format(period='weekly'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_most_played_shows(client):
    """Test case for get_the_most_played_shows

    Get the most played shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/played/{period}'.format(period='weekly'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_most_recommended_shows(client):
    """Test case for get_the_most_recommended_shows

    Get the most recommended shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/recommended/{period}'.format(period='weekly'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_most_watched_shows(client):
    """Test case for get_the_most_watched_shows

    Get the most watched shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/watched/{period}'.format(period='weekly'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trending_shows(client):
    """Test case for get_trending_shows

    Get trending shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/trending',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_show_progress(client):
    """Test case for reset_show_progress

    Reset show progress
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/shows/{id}/progress/watched/reset'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shows_id_watching_get(client):
    """Test case for shows_id_watching_get

    Get users watching right now
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/watching'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_undo_reset_show_progress(client):
    """Test case for undo_reset_show_progress

    Undo reset show progress
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/shows/{id}/progress/watched/reset'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

