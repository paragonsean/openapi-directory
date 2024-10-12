# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_alerts_current_overview_by_metric_2(client):
    """Test case for get_network_sensor_alerts_current_overview_by_metric_2

    Return an overview of currently alerting sensors by metric
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sensor/alerts/current/overview/byMetric'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

