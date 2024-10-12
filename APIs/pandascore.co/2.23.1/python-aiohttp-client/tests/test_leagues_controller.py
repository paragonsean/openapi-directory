# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter_over_leagues import FilterOverLeagues
from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_series import FilterOverSeries
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.league import League
from openapi_server.models.league_idor_slug import LeagueIDOrSlug
from openapi_server.models.match import Match
from openapi_server.models.range_over_leagues import RangeOverLeagues
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_series import RangeOverSeries
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.search_over_leagues import SearchOverLeagues
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_series import SearchOverSeries
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.serie import Serie
from openapi_server.models.short_tournament import ShortTournament


pytestmark = pytest.mark.asyncio

async def test_get_leagues(client):
    """Test case for get_leagues

    List leagues
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
        path='/leagues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leagues_league_id_or_slug(client):
    """Test case for get_leagues_league_id_or_slug

    Get a league
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/leagues/{league_id_or_slug}'.format(league_id_or_slug=openapi_server.LeagueIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leagues_league_id_or_slug_matches(client):
    """Test case for get_leagues_league_id_or_slug_matches

    Get matches for a league
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
        path='/leagues/{league_id_or_slug}/matches'.format(league_id_or_slug=openapi_server.LeagueIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leagues_league_id_or_slug_matches_past(client):
    """Test case for get_leagues_league_id_or_slug_matches_past

    Get past matches for league
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
        path='/leagues/{league_id_or_slug}/matches/past'.format(league_id_or_slug=openapi_server.LeagueIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leagues_league_id_or_slug_matches_running(client):
    """Test case for get_leagues_league_id_or_slug_matches_running

    Get running matches for league
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
        path='/leagues/{league_id_or_slug}/matches/running'.format(league_id_or_slug=openapi_server.LeagueIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leagues_league_id_or_slug_matches_upcoming(client):
    """Test case for get_leagues_league_id_or_slug_matches_upcoming

    Get upcoming matches for league
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
        path='/leagues/{league_id_or_slug}/matches/upcoming'.format(league_id_or_slug=openapi_server.LeagueIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leagues_league_id_or_slug_series(client):
    """Test case for get_leagues_league_id_or_slug_series

    List series of a league
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
        path='/leagues/{league_id_or_slug}/series'.format(league_id_or_slug=openapi_server.LeagueIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leagues_league_id_or_slug_tournaments(client):
    """Test case for get_leagues_league_id_or_slug_tournaments

    Get tournaments for a league
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
        path='/leagues/{league_id_or_slug}/tournaments'.format(league_id_or_slug=openapi_server.LeagueIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

