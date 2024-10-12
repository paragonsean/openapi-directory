# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.active_incident_list import ActiveIncidentList
from openapi_server.models.incident_list import IncidentList
from openapi_server.models.on_call_log import OnCallLog


pytestmark = pytest.mark.asyncio

async def test_api_reporting_v1_incidents_get(client):
    """Test case for api_reporting_v1_incidents_get

    Get/search incident history
    """
    params = [('offset', 0.0),
                    ('limit', 20.0),
                    ('entityId', 'entity_id_example'),
                    ('incidentNumber', 'incident_number_example'),
                    ('startedAfter', 'started_after_example'),
                    ('startedBefore', 'started_before_example'),
                    ('host', 'host_example'),
                    ('service', 'service_example'),
                    ('currentPhase', 'current_phase_example')]
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-reporting/v1/incidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_reporting_v1_team_team_oncall_log_get(client):
    """Test case for api_reporting_v1_team_team_oncall_log_get

    A list of shift changes for a team
    """
    params = [('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('userName', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-reporting/v1/team/{team}/oncall/log'.format(team='team_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_reporting_v2_incidents_get(client):
    """Test case for api_reporting_v2_incidents_get

    Get/search incident history
    """
    params = [('offset', 0.0),
                    ('limit', 20.0),
                    ('entityId', 'entity_id_example'),
                    ('incidentNumber', 'incident_number_example'),
                    ('startedAfter', 'started_after_example'),
                    ('startedBefore', 'started_before_example'),
                    ('host', 'host_example'),
                    ('service', 'service_example'),
                    ('currentPhase', 'current_phase_example'),
                    ('routingKey', 'routing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-reporting/v2/incidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

