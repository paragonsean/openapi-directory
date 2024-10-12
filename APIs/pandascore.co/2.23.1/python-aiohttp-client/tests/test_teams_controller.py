# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter_over_leagues import FilterOverLeagues
from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_series import FilterOverSeries
from openapi_server.models.filter_over_short_tournaments import FilterOverShortTournaments
from openapi_server.models.filter_over_teams import FilterOverTeams
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.league import League
from openapi_server.models.match import Match
from openapi_server.models.range_over_leagues import RangeOverLeagues
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_series import RangeOverSeries
from openapi_server.models.range_over_short_tournaments import RangeOverShortTournaments
from openapi_server.models.range_over_teams import RangeOverTeams
from openapi_server.models.search_over_leagues import SearchOverLeagues
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_series import SearchOverSeries
from openapi_server.models.search_over_short_tournaments import SearchOverShortTournaments
from openapi_server.models.search_over_teams import SearchOverTeams
from openapi_server.models.serie import Serie
from openapi_server.models.short_tournament import ShortTournament
from openapi_server.models.team import Team
from openapi_server.models.team_idor_slug import TeamIDOrSlug


pytestmark = pytest.mark.asyncio

async def test_get_teams(client):
    """Test case for get_teams

    List teams
    """
    params = [('filter', openapi_server.FilterOverTeams()),
                    ('search', openapi_server.SearchOverTeams()),
                    ('sort', ['[\"name\"]']),
                    ('range', openapi_server.RangeOverTeams()),
                    ('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_team_id_or_slug(client):
    """Test case for get_teams_team_id_or_slug

    Get a team
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams/{team_id_or_slug}'.format(team_id_or_slug=openapi_server.TeamIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_team_id_or_slug_leagues(client):
    """Test case for get_teams_team_id_or_slug_leagues

    Get leagues for a team
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
        path='/teams/{team_id_or_slug}/leagues'.format(team_id_or_slug=openapi_server.TeamIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_team_id_or_slug_matches(client):
    """Test case for get_teams_team_id_or_slug_matches

    Get matches for team
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
        path='/teams/{team_id_or_slug}/matches'.format(team_id_or_slug=openapi_server.TeamIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_team_id_or_slug_series(client):
    """Test case for get_teams_team_id_or_slug_series

    Get series for a team
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
        path='/teams/{team_id_or_slug}/series'.format(team_id_or_slug=openapi_server.TeamIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_team_id_or_slug_tournaments(client):
    """Test case for get_teams_team_id_or_slug_tournaments

    Get tournaments for a team
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
        path='/teams/{team_id_or_slug}/tournaments'.format(team_id_or_slug=openapi_server.TeamIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

