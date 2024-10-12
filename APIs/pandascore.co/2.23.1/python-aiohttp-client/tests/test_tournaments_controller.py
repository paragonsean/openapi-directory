# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bracket import Bracket
from openapi_server.models.filter_over_brackets import FilterOverBrackets
from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_players import FilterOverPlayers
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.match import Match
from openapi_server.models.player import Player
from openapi_server.models.range_over_brackets import RangeOverBrackets
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_players import RangeOverPlayers
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.search_over_brackets import SearchOverBrackets
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_players import SearchOverPlayers
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.short_tournament import ShortTournament
from openapi_server.models.standing import Standing
from openapi_server.models.tournament import Tournament
from openapi_server.models.tournament_idor_slug import TournamentIDOrSlug
from openapi_server.models.tournament_rosters import TournamentRosters


pytestmark = pytest.mark.asyncio

async def test_get_tournaments(client):
    """Test case for get_tournaments

    List tournaments
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
        path='/tournaments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_past(client):
    """Test case for get_tournaments_past

    Get past tournaments
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
        path='/tournaments/past',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_running(client):
    """Test case for get_tournaments_running

    Get running tournaments
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
        path='/tournaments/running',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_tournament_id_or_slug(client):
    """Test case for get_tournaments_tournament_id_or_slug

    Get a tournament
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tournaments/{tournament_id_or_slug}'.format(tournament_id_or_slug=openapi_server.TournamentIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_tournament_id_or_slug_brackets(client):
    """Test case for get_tournaments_tournament_id_or_slug_brackets

    Get a tournament's brackets
    """
    params = [('filter', openapi_server.FilterOverBrackets()),
                    ('range', openapi_server.RangeOverBrackets()),
                    ('sort', ['sort_example']),
                    ('search', openapi_server.SearchOverBrackets()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tournaments/{tournament_id_or_slug}/brackets'.format(tournament_id_or_slug=openapi_server.TournamentIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_tournament_id_or_slug_matches(client):
    """Test case for get_tournaments_tournament_id_or_slug_matches

    Get matches for tournament
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
        path='/tournaments/{tournament_id_or_slug}/matches'.format(tournament_id_or_slug=openapi_server.TournamentIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_tournament_id_or_slug_players(client):
    """Test case for get_tournaments_tournament_id_or_slug_players

    Get players for a tournament
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
        path='/tournaments/{tournament_id_or_slug}/players'.format(tournament_id_or_slug='tournament_id_or_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_tournament_id_or_slug_rosters(client):
    """Test case for get_tournaments_tournament_id_or_slug_rosters

    Get rosters for a tournament
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tournaments/{tournament_id_or_slug}/rosters'.format(tournament_id_or_slug=openapi_server.TournamentIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_tournament_id_or_slug_standings(client):
    """Test case for get_tournaments_tournament_id_or_slug_standings

    Get tournament standings
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
        path='/tournaments/{tournament_id_or_slug}/standings'.format(tournament_id_or_slug=openapi_server.TournamentIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_upcoming(client):
    """Test case for get_tournaments_upcoming

    Get upcoming tournaments
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
        path='/tournaments/upcoming',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

