# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.incident import Incident
from openapi_server.models.incident_list_result import IncidentListResult


pytestmark = pytest.mark.asyncio

async def test_alert_rule_incidents_get(client):
    """Test case for alert_rule_incidents_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/alertrules/{rule_name}/incidents/{incident_name}'.format(resource_group_name='resource_group_name_example', rule_name='rule_name_example', incident_name='incident_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alert_rule_incidents_list_by_alert_rule(client):
    """Test case for alert_rule_incidents_list_by_alert_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/alertrules/{rule_name}/incidents'.format(resource_group_name='resource_group_name_example', rule_name='rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

