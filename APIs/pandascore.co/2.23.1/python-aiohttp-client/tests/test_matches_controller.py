# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter_over_matches import FilterOverMatches
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.live import Live
from openapi_server.models.match import Match
from openapi_server.models.match_idor_slug import MatchIDOrSlug
from openapi_server.models.match_opponents_object import MatchOpponentsObject
from openapi_server.models.range_over_matches import RangeOverMatches
from openapi_server.models.search_over_matches import SearchOverMatches


pytestmark = pytest.mark.asyncio

async def test_get_lives(client):
    """Test case for get_lives

    List lives matches
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
        path='/lives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matches(client):
    """Test case for get_matches

    List matches
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
        path='/matches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matches_match_id_or_slug(client):
    """Test case for get_matches_match_id_or_slug

    Get a match
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/matches/{match_id_or_slug}'.format(match_id_or_slug=openapi_server.MatchIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matches_match_id_or_slug_opponents(client):
    """Test case for get_matches_match_id_or_slug_opponents

    Get match's opponents
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/matches/{match_id_or_slug}/opponents'.format(match_id_or_slug=openapi_server.MatchIDOrSlug()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matches_past(client):
    """Test case for get_matches_past

    Get past matches
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
        path='/matches/past',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matches_running(client):
    """Test case for get_matches_running

    Get running matches
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
        path='/matches/running',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matches_upcoming(client):
    """Test case for get_matches_upcoming

    Get upcoming matches
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
        path='/matches/upcoming',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

