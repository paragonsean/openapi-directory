# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.award import Award
from openapi_server.models.elimination_alliance import EliminationAlliance
from openapi_server.models.event import Event
from openapi_server.models.event_district_points import EventDistrictPoints
from openapi_server.models.event_insights import EventInsights
from openapi_server.models.event_oprs import EventOPRs
from openapi_server.models.event_ranking import EventRanking
from openapi_server.models.event_simple import EventSimple
from openapi_server.models.match import Match
from openapi_server.models.match_simple import MatchSimple
from openapi_server.models.team import Team
from openapi_server.models.team_event_status import TeamEventStatus
from openapi_server.models.team_simple import TeamSimple


pytestmark = pytest.mark.asyncio

async def test_get_district_events_0(client):
    """Test case for get_district_events_0

    
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

async def test_get_district_events_keys_0(client):
    """Test case for get_district_events_keys_0

    
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

async def test_get_district_events_simple_0(client):
    """Test case for get_district_events_simple_0

    
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

async def test_get_event(client):
    """Test case for get_event

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_alliances(client):
    """Test case for get_event_alliances

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/alliances'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_awards(client):
    """Test case for get_event_awards

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/awards'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_district_points(client):
    """Test case for get_event_district_points

    
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

async def test_get_event_insights(client):
    """Test case for get_event_insights

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/insights'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_match_timeseries(client):
    """Test case for get_event_match_timeseries

    
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

async def test_get_event_matches(client):
    """Test case for get_event_matches

    
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

async def test_get_event_matches_keys(client):
    """Test case for get_event_matches_keys

    
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

async def test_get_event_matches_simple(client):
    """Test case for get_event_matches_simple

    
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

async def test_get_event_oprs(client):
    """Test case for get_event_oprs

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/oprs'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_predictions(client):
    """Test case for get_event_predictions

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/predictions'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_rankings(client):
    """Test case for get_event_rankings

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/rankings'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_simple(client):
    """Test case for get_event_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/simple'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_teams(client):
    """Test case for get_event_teams

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/teams'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_teams_keys(client):
    """Test case for get_event_teams_keys

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/teams/keys'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_teams_simple(client):
    """Test case for get_event_teams_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/teams/simple'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_teams_statuses(client):
    """Test case for get_event_teams_statuses

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/event/{event_key}/teams/statuses'.format(event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_by_year(client):
    """Test case for get_events_by_year

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/{year}'.format(year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_by_year_keys(client):
    """Test case for get_events_by_year_keys

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/{year}/keys'.format(year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_by_year_simple(client):
    """Test case for get_events_by_year_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events/{year}/simple'.format(year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_event_awards_0(client):
    """Test case for get_team_event_awards_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/event/{event_key}/awards'.format(team_key='team_key_example', event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_event_matches_0(client):
    """Test case for get_team_event_matches_0

    
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

async def test_get_team_event_matches_keys_0(client):
    """Test case for get_team_event_matches_keys_0

    
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

async def test_get_team_event_matches_simple_0(client):
    """Test case for get_team_event_matches_simple_0

    
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

async def test_get_team_event_status_0(client):
    """Test case for get_team_event_status_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/event/{event_key}/status'.format(team_key='team_key_example', event_key='event_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_events_0(client):
    """Test case for get_team_events_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/events'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_events_by_year_0(client):
    """Test case for get_team_events_by_year_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/events/{year}'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_events_by_year_keys_0(client):
    """Test case for get_team_events_by_year_keys_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/events/{year}/keys'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_events_by_year_simple_0(client):
    """Test case for get_team_events_by_year_simple_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/events/{year}/simple'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_events_keys_0(client):
    """Test case for get_team_events_keys_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/events/keys'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_events_simple_0(client):
    """Test case for get_team_events_simple_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/events/simple'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_events_statuses_by_year_1(client):
    """Test case for get_team_events_statuses_by_year_1

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/events/{year}/statuses'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

