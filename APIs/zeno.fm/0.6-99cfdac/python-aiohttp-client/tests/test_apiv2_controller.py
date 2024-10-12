# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.country import Country
from openapi_server.models.language import Language
from openapi_server.models.podcast import Podcast
from openapi_server.models.podcast_category import PodcastCategory
from openapi_server.models.podcast_episode import PodcastEpisode
from openapi_server.models.podcast_episode_list import PodcastEpisodeList
from openapi_server.models.podcast_search_params import PodcastSearchParams
from openapi_server.models.podcast_search_results import PodcastSearchResults
from openapi_server.models.station_genre import StationGenre
from openapi_server.models.station_list import StationList
from openapi_server.models.station_search_params import StationSearchParams
from openapi_server.models.station_search_results import StationSearchResults


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_podcast(client):
    """Test case for create_podcast

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'API_Key': 'special-key',
    }
    data = FormData()
    data.add_field('file_logo', '/path/to/file')
    data.add_field('podcast', openapi_server.Podcast())
    response = await client.request(
        method='POST',
        path='/api/v2/podcasts/create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_podcast_episode(client):
    """Test case for create_podcast_episode

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'API_Key': 'special-key',
    }
    data = FormData()
    data.add_field('episode', openapi_server.PodcastEpisode())
    data.add_field('file_logo', '/path/to/file')
    data.add_field('file_media', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v2/podcasts/{podcast_key}/episodes/create'.format(podcast_key='podcast_key_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_podcast(client):
    """Test case for delete_podcast

    
    """
    headers = { 
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/podcasts/{podcast_key}'.format(podcast_key='podcast_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_podcast1(client):
    """Test case for delete_podcast1

    
    """
    headers = { 
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/podcasts/{podcast_key}/episodes/{episode_key}'.format(podcast_key='podcast_key_example', episode_key='episode_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partner_aggregator_stations(client):
    """Test case for get_partner_aggregator_stations

    
    """
    params = [('page', '1'),
                    ('hitsPerPage', '10')]
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/stations/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast(client):
    """Test case for get_podcast

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/{podcast_key}'.format(podcast_key='podcast_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_categories(client):
    """Test case for get_podcast_categories

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_countries(client):
    """Test case for get_podcast_countries

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_episode(client):
    """Test case for get_podcast_episode

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/{podcast_key}/episodes/{episode_key}'.format(podcast_key='podcast_key_example', episode_key='episode_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_episodes(client):
    """Test case for get_podcast_episodes

    
    """
    params = [('limit', '10'),
                    ('offset', '0')]
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/{podcast_key}/episodes'.format(podcast_key='podcast_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_languages(client):
    """Test case for get_podcast_languages

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/languages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_station_countries(client):
    """Test case for get_station_countries

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/stations/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_station_genres(client):
    """Test case for get_station_genres

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/stations/genres',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_station_languages(client):
    """Test case for get_station_languages

    
    """
    headers = { 
        'Accept': '*/*',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/stations/languages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_podcasts(client):
    """Test case for search_podcasts

    
    """
    body = {"hitsPerPage":81,"query":"query","filters":{"country":["country","country"],"podcastType":"podcasts","language":["language","language"],"category":["category","category"]},"page":1}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/podcasts/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_stations(client):
    """Test case for search_stations

    
    """
    body = {"hitsPerPage":81,"query":"query","filters":{"country":["country","country"],"genre":["genre","genre"],"language":["language","language"]},"page":1}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'API_Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/stations/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_podcast(client):
    """Test case for update_podcast

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'API_Key': 'special-key',
    }
    data = FormData()
    data.add_field('file_logo', '/path/to/file')
    data.add_field('podcast', openapi_server.Podcast())
    response = await client.request(
        method='PUT',
        path='/api/v2/podcasts/{podcast_key}'.format(podcast_key='podcast_key_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_podcast_episode(client):
    """Test case for update_podcast_episode

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'API_Key': 'special-key',
    }
    data = FormData()
    data.add_field('episode', openapi_server.PodcastEpisode())
    data.add_field('file_logo', '/path/to/file')
    response = await client.request(
        method='PUT',
        path='/api/v2/podcasts/{podcast_key}/episodes/{episode_key}'.format(podcast_key='podcast_key_example', episode_key='episode_key_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

