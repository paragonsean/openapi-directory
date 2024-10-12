# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_players import FilterOverPlayers
from openapi_server.models.filter_over_series import FilterOverSeries
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.match import Match
from openapi_server.models.player import Player
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_players import RangeOverPlayers
from openapi_server.models.range_over_series import RangeOverSeries
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_players import SearchOverPlayers
from openapi_server.models.search_over_series import SearchOverSeries
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.serie import Serie
from openapi_server.models.serie_idor_slug import SerieIDOrSlug
from openapi_server.models.short_tournament import ShortTournament


pytestmark = pytest.mark.asyncio

async def test_get_series(client):
    """Test case for get_series

    List series
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
        path='/series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_past(client):
    """Test case for get_series_past

    Get past series
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
        path='/series/past',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_running(client):
    """Test case for get_series_running

    Get running series
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
        path='/series/running',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_serie_id_or_slug(client):
    """Test case for get_series_serie_id_or_slug

    Get a serie
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/series/{serie_id_or_slug}'.format(serie_id_or_slug=openapi_server.SerieIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_serie_id_or_slug_matches(client):
    """Test case for get_series_serie_id_or_slug_matches

    Get matches for a serie
    """
    params = [('filter', openapi_server.FilterOverMatches()),
                    ('search', openapi_server.SearchOverMatches()),
                    ('sort', ['[\"tournament_id\",\"scheduled_at\"]']),
                    ('range', openapi_server.RangeOverMatches()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/series/{serie_id_or_slug}/matches'.format(serie_id_or_slug=openapi_server.SerieIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_serie_id_or_slug_matches_past(client):
    """Test case for get_series_serie_id_or_slug_matches_past

    Get past matches for serie
    """
    params = [('filter', openapi_server.FilterOverMatches()),
                    ('search', openapi_server.SearchOverMatches()),
                    ('sort', ['[\"tournament_id\",\"scheduled_at\"]']),
                    ('range', openapi_server.RangeOverMatches()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/series/{serie_id_or_slug}/matches/past'.format(serie_id_or_slug=openapi_server.SerieIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_serie_id_or_slug_matches_running(client):
    """Test case for get_series_serie_id_or_slug_matches_running

    Get running matches for serie
    """
    params = [('filter', openapi_server.FilterOverMatches()),
                    ('search', openapi_server.SearchOverMatches()),
                    ('sort', ['[\"tournament_id\",\"scheduled_at\"]']),
                    ('range', openapi_server.RangeOverMatches()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/series/{serie_id_or_slug}/matches/running'.format(serie_id_or_slug=openapi_server.SerieIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_serie_id_or_slug_matches_upcoming(client):
    """Test case for get_series_serie_id_or_slug_matches_upcoming

    Get upcoming matches for serie
    """
    params = [('filter', openapi_server.FilterOverMatches()),
                    ('search', openapi_server.SearchOverMatches()),
                    ('sort', ['[\"tournament_id\",\"scheduled_at\"]']),
                    ('range', openapi_server.RangeOverMatches()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/series/{serie_id_or_slug}/matches/upcoming'.format(serie_id_or_slug=openapi_server.SerieIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_serie_id_or_slug_players(client):
    """Test case for get_series_serie_id_or_slug_players

    Get players for a serie
    """
    params = [('filter', openapi_server.FilterOverPlayers()),
                    ('search', openapi_server.SearchOverPlayers()),
                    ('sort', ['[\"last_name\"]']),
                    ('range', openapi_server.RangeOverPlayers()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/series/{serie_id_or_slug}/players'.format(serie_id_or_slug='serie_id_or_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_serie_id_or_slug_tournaments(client):
    """Test case for get_series_serie_id_or_slug_tournaments

    Get tournaments for a serie
    """
    params = [('filter', openapi_server.FilterOverShortTournaments()),
                    ('search', openapi_server.SearchOverShortTournaments()),
                    ('sort', ['[\"serie_id\",\"-begin_at\"]']),
                    ('range', openapi_server.RangeOverShortTournaments()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/series/{serie_id_or_slug}/tournaments'.format(serie_id_or_slug=openapi_server.SerieIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_upcoming(client):
    """Test case for get_series_upcoming

    Get upcoming series
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
        path='/series/upcoming',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

