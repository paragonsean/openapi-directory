# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter_over_teams import FilterOverTeams
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.range_over_teams import RangeOverTeams
from openapi_server.models.search_over_teams import SearchOverTeams
from openapi_server.models.team import Team
from openapi_server.models.tournament_idor_slug import TournamentIDOrSlug


pytestmark = pytest.mark.asyncio

async def test_get_tournaments_tournament_id_or_slug_teams(client):
    """Test case for get_tournaments_tournament_id_or_slug_teams

    Get teams for a tournament
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
        path='/tournaments/{tournament_id_or_slug}/teams'.format(tournament_id_or_slug=openapi_server.TournamentIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

