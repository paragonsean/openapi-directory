# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_range_info import DeleteRangeInfo
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.schedule_info import ScheduleInfo
from openapi_server.models.team_duty_summary_info import TeamDutySummaryInfo


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_duty_reports_file_name_get(client):
    """Test case for teams_team_id_duty_reports_file_name_get

    Download duty report with a specific fileName
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/dutyReports/{file_name}'.format(team_id='team_id_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_duty_reports_get(client):
    """Test case for teams_team_id_duty_reports_get

    Get Information about downloadable reports
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/dutyReports'.format(team_id='team_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_dutysummary_get(client):
    """Test case for teams_team_id_dutysummary_get

    Get duty assistant info for a team
    """
    params = [('lastTwoDuties', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/dutysummary'.format(team_id='team_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_schedules_delete_range_post(client):
    """Test case for teams_team_id_schedules_delete_range_post

    Delete duty schedules in range
    """
    body = {"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/teams/{team_id}/schedules/deleteRange'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_schedules_duty_id_delete(client):
    """Test case for teams_team_id_schedules_duty_id_delete

    Delete a specific duty.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/teams/{team_id}/schedules/{duty_id}'.format(team_id='team_id_example', duty_id='duty_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_schedules_get(client):
    """Test case for teams_team_id_schedules_get

    Returns information about all duties that belong to the team.
    """
    params = [('UserId', 'user_id_example'),
                    ('MinDate', '2013-10-20T19:20:30+01:00'),
                    ('Limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/schedules'.format(team_id='team_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_schedules_multiple_post(client):
    """Test case for teams_team_id_schedules_multiple_post

    Save multiple schedules. It is possible to override existing schedules if you wish
    """
    body = {"options":0,"start":"2000-01-23T04:56:07.000+00:00","end":"2000-01-23T04:56:07.000+00:00","id":"id","userId":"userId"}
    params = [('overrideExisting', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/teams/{team_id}/schedules/multiple'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_teams_team_id_schedules_post(client):
    """Test case for teams_team_id_schedules_post

    Create/Update given duty schedule.
    """
    body = {"options":0,"start":"2000-01-23T04:56:07.000+00:00","end":"2000-01-23T04:56:07.000+00:00","id":"id","userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/teams/{team_id}/schedules'.format(team_id='team_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_team_id_schedules_schedule_id_get(client):
    """Test case for teams_team_id_schedules_schedule_id_get

    Returns information of the duty schedule with the specified Id.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/teams/{team_id}/schedules/{schedule_id}'.format(team_id='team_id_example', schedule_id='schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

