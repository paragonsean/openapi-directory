# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.episode import Episode
from openapi_server.models.last_available_season import LastAvailableSeason
from openapi_server.models.post_result import PostResult
from openapi_server.models.show_status import ShowStatus
from openapi_server.models.tv_information import TVInformation
from openapi_server.models.tv_information_post import TVInformationPost
from openapi_server.models.tv_show_seasons import TVShowSeasons


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_tv_show_post(client):
    """Test case for add_tv_show_post

    Add new show to database
    """
    value = {"AccessToken":"AccessToken","EpisodeCount":"EpisodeCount","ShowImage":"ShowImage","ShowStatus":"ShowStatus","Title":"Title","EpisodeRuntime":"EpisodeRuntime","Genres":"Genres","Seasons":"Seasons","ImdbID":"ImdbID","PremierYear":"PremierYear","Synopsis":"Synopsis"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/AddTVShow',
        headers=headers,
        json=value,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episodes_by_id_get(client):
    """Test case for episodes_by_id_get

    Gets all episodes for selected ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Episodes/ByID/{access_token}/{id}'.format(access_token='access_token_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episodes_by_season_get(client):
    """Test case for episodes_by_season_get

    Gets list of episodes for specified imdbID and Season number
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Episodes/BySeason/{access_token}/{id}/{season}'.format(access_token='access_token_example', id='id_example', season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episodes_get(client):
    """Test case for episodes_get

    Gets all episodes for selected show
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Episodes/ByShowName/{access_token}/{showname}'.format(access_token='access_token_example', showname='showname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episodes_last_available_season_get(client):
    """Test case for episodes_last_available_season_get

    Returns last available season number in database, based on passed imdbID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Episodes/LatestSeason/{access_token}/{id}'.format(access_token='access_token_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episodes_last_available_seasonby_name_get(client):
    """Test case for episodes_last_available_seasonby_name_get

    Gets latest season number based on show name
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Episodes/LatestSeason/Show/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episodes_season_count_get(client):
    """Test case for episodes_season_count_get

    Returns number of available seasons and episodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Episodes/SeasonCount/{access_token}/{id}'.format(access_token='access_token_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_status_get(client):
    """Test case for show_status_get

    Returns status of queried show (query can be IMDB, TVDB, or showname)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Status/{access_token}/{query}'.format(access_token='access_token_example', query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_t_v_show_by_name_get(client):
    """Test case for t_v_show_by_name_get

    Returns results based on query, result set limited to 5 records
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/TV/ByName/{access_token}/{query}'.format(access_token='access_token_example', query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_t_v_show_id_get(client):
    """Test case for t_v_show_id_get

    Returns TVShow information based on IMDBid
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/TV/ByID/{accesstoken}/{imdb_id}'.format(accesstoken='accesstoken_example', imdb_id='imdb_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

