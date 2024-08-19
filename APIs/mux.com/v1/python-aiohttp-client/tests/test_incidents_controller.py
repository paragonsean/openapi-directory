# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.incident_response import IncidentResponse
from openapi_server.models.list_incidents_response import ListIncidentsResponse
from openapi_server.models.list_related_incidents_response import ListRelatedIncidentsResponse


pytestmark = pytest.mark.asyncio

async def test_get_incident(client):
    """Test case for get_incident

    Get an Incident
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/incidents/{incident_id}'.format(incident_id='abcd1234'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_incidents(client):
    """Test case for list_incidents

    List Incidents
    """
    params = [('limit', 25),
                    ('page', 1),
                    ('order_by', 'order_by_example'),
                    ('order_direction', 'order_direction_example'),
                    ('status', 'status_example'),
                    ('severity', 'severity_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/incidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_related_incidents(client):
    """Test case for list_related_incidents

    List Related Incidents
    """
    params = [('limit', 25),
                    ('page', 1),
                    ('order_by', 'order_by_example'),
                    ('order_direction', 'order_direction_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/incidents/{incident_id}/related'.format(incident_id='abcd1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

