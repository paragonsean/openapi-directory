# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.award import Award
from openapi_server.models.district_list import DistrictList
from openapi_server.models.district_ranking import DistrictRanking
from openapi_server.models.event import Event
from openapi_server.models.event_simple import EventSimple
from openapi_server.models.match import Match
from openapi_server.models.match_simple import MatchSimple
from openapi_server.models.media import Media
from openapi_server.models.team import Team
from openapi_server.models.team_event_status import TeamEventStatus
from openapi_server.models.team_robot import TeamRobot
from openapi_server.models.team_simple import TeamSimple


pytestmark = pytest.mark.asyncio

async def test_get_district_rankings_0(client):
    """Test case for get_district_rankings_0

    
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

async def test_get_district_teams_0(client):
    """Test case for get_district_teams_0

    
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

async def test_get_district_teams_keys_0(client):
    """Test case for get_district_teams_keys_0

    
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

async def test_get_district_teams_simple_0(client):
    """Test case for get_district_teams_simple_0

    
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

async def test_get_event_teams_0(client):
    """Test case for get_event_teams_0

    
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

async def test_get_event_teams_keys_0(client):
    """Test case for get_event_teams_keys_0

    
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

async def test_get_event_teams_simple_0(client):
    """Test case for get_event_teams_simple_0

    
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

async def test_get_event_teams_statuses_0(client):
    """Test case for get_event_teams_statuses_0

    
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

async def test_get_team(client):
    """Test case for get_team

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_awards(client):
    """Test case for get_team_awards

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/awards'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_awards_by_year(client):
    """Test case for get_team_awards_by_year

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/awards/{year}'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_districts(client):
    """Test case for get_team_districts

    
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


pytestmark = pytest.mark.asyncio

async def test_get_team_event_awards(client):
    """Test case for get_team_event_awards

    
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

async def test_get_team_event_matches(client):
    """Test case for get_team_event_matches

    
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

async def test_get_team_event_matches_keys(client):
    """Test case for get_team_event_matches_keys

    
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

async def test_get_team_event_matches_simple(client):
    """Test case for get_team_event_matches_simple

    
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

async def test_get_team_event_status(client):
    """Test case for get_team_event_status

    
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

async def test_get_team_events(client):
    """Test case for get_team_events

    
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

async def test_get_team_events_by_year(client):
    """Test case for get_team_events_by_year

    
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

async def test_get_team_events_by_year_keys(client):
    """Test case for get_team_events_by_year_keys

    
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

async def test_get_team_events_by_year_simple(client):
    """Test case for get_team_events_by_year_simple

    
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

async def test_get_team_events_keys(client):
    """Test case for get_team_events_keys

    
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

async def test_get_team_events_simple(client):
    """Test case for get_team_events_simple

    
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

async def test_get_team_events_statuses_by_year_0(client):
    """Test case for get_team_events_statuses_by_year_0

    
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


pytestmark = pytest.mark.asyncio

async def test_get_team_matches_by_year(client):
    """Test case for get_team_matches_by_year

    
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

async def test_get_team_matches_by_year_keys(client):
    """Test case for get_team_matches_by_year_keys

    
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

async def test_get_team_matches_by_year_simple(client):
    """Test case for get_team_matches_by_year_simple

    
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


pytestmark = pytest.mark.asyncio

async def test_get_team_media_by_tag(client):
    """Test case for get_team_media_by_tag

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/media/tag/{media_tag}'.format(team_key='team_key_example', media_tag='media_tag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_media_by_tag_year(client):
    """Test case for get_team_media_by_tag_year

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/media/tag/{media_tag}/{year}'.format(team_key='team_key_example', media_tag='media_tag_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_media_by_year(client):
    """Test case for get_team_media_by_year

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/media/{year}'.format(team_key='team_key_example', year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_robots(client):
    """Test case for get_team_robots

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/robots'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_simple(client):
    """Test case for get_team_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/simple'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_social_media(client):
    """Test case for get_team_social_media

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/social_media'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_years_participated(client):
    """Test case for get_team_years_participated

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/team/{team_key}/years_participated'.format(team_key='team_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams(client):
    """Test case for get_teams

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{page_num}'.format(page_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_by_year(client):
    """Test case for get_teams_by_year

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{year}/{page_num}'.format(year=56, page_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_by_year_keys(client):
    """Test case for get_teams_by_year_keys

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{year}/{page_num}/keys'.format(year=56, page_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_by_year_simple(client):
    """Test case for get_teams_by_year_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{year}/{page_num}/simple'.format(year=56, page_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_keys(client):
    """Test case for get_teams_keys

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{page_num}/keys'.format(page_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams_simple(client):
    """Test case for get_teams_simple

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/teams/{page_num}/simple'.format(page_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

