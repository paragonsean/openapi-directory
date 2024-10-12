# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.filter_over_players import FilterOverPlayers
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.match import Match
from openapi_server.models.player import Player
from openapi_server.models.player_idor_slug import PlayerIDOrSlug
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.range_over_players import RangeOverPlayers
from openapi_server.models.search_over_matches import SearchOverMatches
from openapi_server.models.search_over_players import SearchOverPlayers


pytestmark = pytest.mark.asyncio

async def test_get_players(client):
    """Test case for get_players

    List players
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
        path='/players',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_players_player_id_or_slug(client):
    """Test case for get_players_player_id_or_slug

    Get a player
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/players/{player_id_or_slug}'.format(player_id_or_slug=openapi_server.PlayerIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_players_player_id_or_slug_matches(client):
    """Test case for get_players_player_id_or_slug_matches

    Get matches for a player
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
        path='/players/{player_id_or_slug}/matches'.format(player_id_or_slug=openapi_server.PlayerIDOrSlug()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

