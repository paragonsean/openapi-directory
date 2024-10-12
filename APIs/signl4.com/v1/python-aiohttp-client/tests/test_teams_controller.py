# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_settings import AlertSettings
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.event_source_endpoint_info import EventSourceEndpointInfo
from openapi_server.models.team_info import TeamInfo
from openapi_server.models.team_profile import TeamProfile
from openapi_server.models.team_setup_progress import TeamSetupProgress


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_teams_get(client):
    """Test case for subscriptions_subscription_id_teams_get

    Get infos for all teams of the subscription.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}/teams'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_get(client):
    """Test case for teams_get

    Get infos of all teams.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_alert_reports_file_name_get(client):
    """Test case for teams_team_id_alert_reports_file_name_get

    Returns Alert Report
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/alertReports/{file_name}'.format(team_id='team_id_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_alert_reports_get(client):
    """Test case for teams_team_id_alert_reports_get

    Get information about downloadable alert reports
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/alertReports'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_alert_settings_get(client):
    """Test case for teams_team_id_alert_settings_get

    Gets alert settings of a specific team.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/alertSettings'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_alert_settings_post(client):
    """Test case for teams_team_id_alert_settings_post

    Sets alert settings of a specific team.
    """
    body = {"filterMode":6,"responseMode":5,"persistentNotificicationMode":5,"optOutMode":1,"responseTime":2,"filterAction":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/teams/{team_id}/alertSettings'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_event_sources_get(client):
    """Test case for teams_team_id_event_sources_get

    Gets event sources of a specific team.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/eventSources'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_get(client):
    """Test case for teams_team_id_get

    Gets infos of a specific team.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_profile_put(client):
    """Test case for teams_team_id_profile_put

    Updates team profile of a team
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/teams/{team_id}/profile'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_setup_progress_get(client):
    """Test case for teams_team_id_setup_progress_get

    Gets setup progress of a specific team.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/setupProgress'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

