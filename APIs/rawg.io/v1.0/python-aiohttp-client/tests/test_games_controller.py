# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.game_single import GameSingle
from openapi_server.models.games_development_team_list200_response import GamesDevelopmentTeamList200Response
from openapi_server.models.games_list200_response import GamesList200Response
from openapi_server.models.games_screenshots_list200_response import GamesScreenshotsList200Response
from openapi_server.models.games_stores_list200_response import GamesStoresList200Response
from openapi_server.models.movie import Movie
from openapi_server.models.parent_achievement import ParentAchievement
from openapi_server.models.reddit import Reddit
from openapi_server.models.twitch import Twitch
from openapi_server.models.youtube import Youtube


pytestmark = pytest.mark.asyncio

async def test_games_achievements_read(client):
    """Test case for games_achievements_read

    Get a list of game achievements.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{id}/achievements'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_additions_list(client):
    """Test case for games_additions_list

    Get a list of DLC's for the game, GOTY and other editions, companion apps, etc.
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{game_pk}/additions'.format(game_pk='game_pk_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_development_team_list(client):
    """Test case for games_development_team_list

    Get a list of individual creators that were part of the development team.
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{game_pk}/development-team'.format(game_pk='game_pk_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_game_series_list(client):
    """Test case for games_game_series_list

    Get a list of games that are part of the same series.
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{game_pk}/game-series'.format(game_pk='game_pk_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_list(client):
    """Test case for games_list

    Get a list of games.
    """
    params = [('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('search_precise', True),
                    ('search_exact', True),
                    ('parent_platforms', 'parent_platforms_example'),
                    ('platforms', 'platforms_example'),
                    ('stores', 'stores_example'),
                    ('developers', 'developers_example'),
                    ('publishers', 'publishers_example'),
                    ('genres', 'genres_example'),
                    ('tags', 'tags_example'),
                    ('creators', 'creators_example'),
                    ('dates', 'dates_example'),
                    ('updated', 'updated_example'),
                    ('platforms_count', 56),
                    ('metacritic', 'metacritic_example'),
                    ('exclude_collection', 56),
                    ('exclude_additions', True),
                    ('exclude_parents', True),
                    ('exclude_game_series', True),
                    ('exclude_stores', 'exclude_stores_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_movies_read(client):
    """Test case for games_movies_read

    Get a list of game trailers.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{id}/movies'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_parent_games_list(client):
    """Test case for games_parent_games_list

    Get a list of parent games for DLC's and editions.
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{game_pk}/parent-games'.format(game_pk='game_pk_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_read(client):
    """Test case for games_read

    Get details of the game.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_reddit_read(client):
    """Test case for games_reddit_read

    Get a list of most recent posts from the game's subreddit.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{id}/reddit'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_screenshots_list(client):
    """Test case for games_screenshots_list

    Get screenshots for the game.
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{game_pk}/screenshots'.format(game_pk='game_pk_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_stores_list(client):
    """Test case for games_stores_list

    Get links to the stores that sell the game.
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{game_pk}/stores'.format(game_pk='game_pk_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_suggested_read(client):
    """Test case for games_suggested_read

    Get a list of visually similar games, available only for business and enterprise API users.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{id}/suggested'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_twitch_read(client):
    """Test case for games_twitch_read

    Get streams on Twitch associated with the game, available only for business and enterprise API users.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{id}/twitch'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_youtube_read(client):
    """Test case for games_youtube_read

    Get videos from YouTube associated with the game, available only for business and enterprise API users.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/games/{id}/youtube'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

