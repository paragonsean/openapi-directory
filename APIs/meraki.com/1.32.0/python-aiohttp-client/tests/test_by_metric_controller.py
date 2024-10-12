# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server.models.get_network_sensor_alerts_overview_by_metric200_response_inner import GetNetworkSensorAlertsOverviewByMetric200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_alerts_current_overview_by_metric_4(client):
    """Test case for get_network_sensor_alerts_current_overview_by_metric_4

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


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_alerts_overview_by_metric_3(client):
    """Test case for get_network_sensor_alerts_overview_by_metric_3

    Return an overview of alert occurrences over a timespan, by metric
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('interval', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sensor/alerts/overview/byMetric'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

