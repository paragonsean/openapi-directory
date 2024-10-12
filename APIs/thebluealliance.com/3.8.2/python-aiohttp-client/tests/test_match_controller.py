# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.match import Match
from openapi_server.models.match_simple import MatchSimple
from openapi_server.models.zebra import Zebra


pytestmark = pytest.mark.asyncio

async def test_get_event_match_timeseries_0(client):
    """Test case for get_event_match_timeseries_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/matches/timeseries'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_matches_0(client):
    """Test case for get_event_matches_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/matches'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_matches_keys_0(client):
    """Test case for get_event_matches_keys_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/matches/keys'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_matches_simple_0(client):
    """Test case for get_event_matches_simple_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/matches/simple'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_match(client):
    """Test case for get_match

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/match/{match_key}'.format(match_key='match_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_match_simple(client):
    """Test case for get_match_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/match/{match_key}/simple'.format(match_key='match_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_match_timeseries(client):
    """Test case for get_match_timeseries

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/match/{match_key}/timeseries'.format(match_key='match_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_match_zebra(client):
    """Test case for get_match_zebra

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/match/{match_key}/zebra_motionworks'.format(match_key='match_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_event_matches_1(client):
    """Test case for get_team_event_matches_1

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/event/{event_key}/matches'.format(team_key='team_key_example', event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_event_matches_keys_1(client):
    """Test case for get_team_event_matches_keys_1

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/event/{event_key}/matches/keys'.format(team_key='team_key_example', event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_event_matches_simple_1(client):
    """Test case for get_team_event_matches_simple_1

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/event/{event_key}/matches/simple'.format(team_key='team_key_example', event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_matches_by_year_0(client):
    """Test case for get_team_matches_by_year_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/matches/{year}'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_matches_by_year_keys_0(client):
    """Test case for get_team_matches_by_year_keys_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/matches/{year}/keys'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_matches_by_year_simple_0(client):
    """Test case for get_team_matches_by_year_simple_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/matches/{year}/simple'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

