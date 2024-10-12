# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.district_list import DistrictList
from openapi_server.models.district_ranking import DistrictRanking
from openapi_server.models.event import Event
from openapi_server.models.event_district_points import EventDistrictPoints
from openapi_server.models.event_simple import EventSimple
from openapi_server.models.team import Team
from openapi_server.models.team_simple import TeamSimple


pytestmark = pytest.mark.asyncio

async def test_get_district_events(client):
    """Test case for get_district_events

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/district/{district_key}/events'.format(district_key='district_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_district_events_keys(client):
    """Test case for get_district_events_keys

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/district/{district_key}/events/keys'.format(district_key='district_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_district_events_simple(client):
    """Test case for get_district_events_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/district/{district_key}/events/simple'.format(district_key='district_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_district_rankings(client):
    """Test case for get_district_rankings

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/district/{district_key}/rankings'.format(district_key='district_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_district_teams(client):
    """Test case for get_district_teams

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/district/{district_key}/teams'.format(district_key='district_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_district_teams_keys(client):
    """Test case for get_district_teams_keys

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/district/{district_key}/teams/keys'.format(district_key='district_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_district_teams_simple(client):
    """Test case for get_district_teams_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/district/{district_key}/teams/simple'.format(district_key='district_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_districts_by_year(client):
    """Test case for get_districts_by_year

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/districts/{year}'.format(year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_district_points_0(client):
    """Test case for get_event_district_points_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/district_points'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_districts_0(client):
    """Test case for get_team_districts_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/districts'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

