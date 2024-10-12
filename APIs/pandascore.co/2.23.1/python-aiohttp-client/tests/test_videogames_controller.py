# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter_over_leagues import FilterOverLeagues
from openapi_server.models.filter_over_series import FilterOverSeries
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.filter_over_short_videogame_versions import FilterOverShortVideogameVersions
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.league import League
from openapi_server.models.range_over_leagues import RangeOverLeagues
from openapi_server.models.range_over_series import RangeOverSeries
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.range_over_short_videogame_versions import RangeOverShortVideogameVersions
from openapi_server.models.search_over_leagues import SearchOverLeagues
from openapi_server.models.search_over_series import SearchOverSeries
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.search_over_short_videogame_versions import SearchOverShortVideogameVersions
from openapi_server.models.serie import Serie
from openapi_server.models.short_tournament import ShortTournament
from openapi_server.models.short_videogame_version import ShortVideogameVersion
from openapi_server.models.videogame import Videogame
from openapi_server.models.videogame_idor_slug import VideogameIDOrSlug


pytestmark = pytest.mark.asyncio

async def test_get_videogames(client):
    """Test case for get_videogames

    List videogames
    """
    params = [('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/videogames',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videogames_videogame_id_or_slug(client):
    """Test case for get_videogames_videogame_id_or_slug

    Get a videogame
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/videogames/{videogame_id_or_slug}'.format(videogame_id_or_slug=openapi_server.VideogameIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videogames_videogame_id_or_slug_leagues(client):
    """Test case for get_videogames_videogame_id_or_slug_leagues

    
    """
    params = [('search', openapi_server.SearchOverLeagues()),
                    ('sort', ['[\"name\",\"-modified_at\"]']),
                    ('range', openapi_server.RangeOverLeagues()),
                    ('filter', openapi_server.FilterOverLeagues()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/videogames/{videogame_id_or_slug}/leagues'.format(videogame_id_or_slug=openapi_server.VideogameIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videogames_videogame_id_or_slug_series(client):
    """Test case for get_videogames_videogame_id_or_slug_series

    List series for a videogame
    """
    params = [('filter', openapi_server.FilterOverSeries()),
                    ('search', openapi_server.SearchOverSeries()),
                    ('sort', ['[\"year\",\"-modified_at\"]']),
                    ('range', openapi_server.RangeOverSeries()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/videogames/{videogame_id_or_slug}/series'.format(videogame_id_or_slug=openapi_server.VideogameIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videogames_videogame_id_or_slug_tournaments(client):
    """Test case for get_videogames_videogame_id_or_slug_tournaments

    Get tournaments for a videogame
    """
    params = [('filter', openapi_server.FilterOverShortTournaments()),
                    ('range', openapi_server.RangeOverShortTournaments()),
                    ('sort', ['sort_example']),
                    ('search', openapi_server.SearchOverShortTournaments()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/videogames/{videogame_id_or_slug}/tournaments'.format(videogame_id_or_slug=openapi_server.VideogameIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videogames_videogame_id_or_slug_versions(client):
    """Test case for get_videogames_videogame_id_or_slug_versions

    List videogame versions
    """
    params = [('filter', openapi_server.FilterOverShortVideogameVersions()),
                    ('range', openapi_server.RangeOverShortVideogameVersions()),
                    ('sort', ['sort_example']),
                    ('search', openapi_server.SearchOverShortVideogameVersions()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/videogames/{videogame_id_or_slug}/versions'.format(videogame_id_or_slug=openapi_server.VideogameIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

