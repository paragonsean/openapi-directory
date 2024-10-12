# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.best_podcasts_response import BestPodcastsResponse
from openapi_server.models.curated_list_full import CuratedListFull
from openapi_server.models.episode_full import EpisodeFull
from openapi_server.models.episode_simple import EpisodeSimple
from openapi_server.models.get_curated_podcasts_response import GetCuratedPodcastsResponse
from openapi_server.models.get_episode_recommendations_response import GetEpisodeRecommendationsResponse
from openapi_server.models.get_episodes_in_batch_response import GetEpisodesInBatchResponse
from openapi_server.models.get_genres_response import GetGenresResponse
from openapi_server.models.get_languages_response import GetLanguagesResponse
from openapi_server.models.get_podcast_recommendations_response import GetPodcastRecommendationsResponse
from openapi_server.models.get_podcasts_in_batch_response import GetPodcastsInBatchResponse
from openapi_server.models.get_regions_response import GetRegionsResponse
from openapi_server.models.podcast_full import PodcastFull


pytestmark = pytest.mark.asyncio

async def test_get_best_podcasts(client):
    """Test case for get_best_podcasts

    Fetch a list of best podcasts by genre
    """
    params = [('genre_id', 'genre_id_example'),
                    ('page', 56),
                    ('region', 'us'),
                    ('publisher_region', 'publisher_region_example'),
                    ('language', 'language_example'),
                    ('sort', recent_added_first),
                    ('safe_mode', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/best_podcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_curated_podcast_by_id(client):
    """Test case for get_curated_podcast_by_id

    Fetch a curated list of podcasts by id
    """
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/curated_podcasts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_curated_podcasts(client):
    """Test case for get_curated_podcasts

    Fetch curated lists of podcasts
    """
    params = [('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/curated_podcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_episode_by_id(client):
    """Test case for get_episode_by_id

    Fetch detailed meta data for an episode by id
    """
    params = [('show_transcript', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/episodes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_episode_recommendations(client):
    """Test case for get_episode_recommendations

    Fetch recommendations for an episode
    """
    params = [('safe_mode', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/episodes/{id}/recommendations'.format(id='254444fa6cf64a43a95292a70eb6869b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_episodes_in_batch(client):
    """Test case for get_episodes_in_batch

    Batch fetch basic meta data for episodes
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    data = {
        'ids': 'ids_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v2/episodes',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genres(client):
    """Test case for get_genres

    Fetch a list of podcast genres
    """
    params = [('top_level_only', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/genres',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_languages(client):
    """Test case for get_languages

    Fetch a list of supported languages for podcasts
    """
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/languages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_by_id(client):
    """Test case for get_podcast_by_id

    Fetch detailed meta data and episodes for a podcast by id
    """
    params = [('next_episode_pub_date', 1479154463000),
                    ('sort', recent_first)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/{id}'.format(id='4d3fe717742d4963a85562e9f84d8c79'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_recommendations(client):
    """Test case for get_podcast_recommendations

    Fetch recommendations for a podcast
    """
    params = [('safe_mode', 0)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/{id}/recommendations'.format(id='25212ac3c53240a880dd5032e547047b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_podcasts_in_batch(client):
    """Test case for get_podcasts_in_batch

    Batch fetch basic meta data for podcasts
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    data = {
        'ids': 'ids_example',
        'itunes_ids': 'itunes_ids_example',
        'next_episode_pub_date': 56,
        'rsses': 'rsses_example',
        'show_latest_episodes': 0,
        'spotify_ids': 'spotify_ids_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v2/podcasts',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_regions(client):
    """Test case for get_regions

    Fetch a list of supported countries/regions for best podcasts
    """
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/regions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_just_listen(client):
    """Test case for just_listen

    Fetch a random podcast episode
    """
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/just_listen',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

