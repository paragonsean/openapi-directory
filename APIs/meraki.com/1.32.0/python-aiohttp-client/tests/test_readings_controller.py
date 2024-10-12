# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_sensor_readings_history200_response_inner import GetOrganizationSensorReadingsHistory200ResponseInner
from openapi_server.models.get_organization_sensor_readings_latest200_response_inner import GetOrganizationSensorReadingsLatest200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_sensor_readings_history_1(client):
    """Test case for get_organization_sensor_readings_history_1

    Return all reported readings from sensors in a given timespan, sorted by timestamp
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('metrics', ['metrics_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sensor/readings/history'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_sensor_readings_latest_1(client):
    """Test case for get_organization_sensor_readings_latest_1

    Return the latest available reading for each metric from each sensor, sorted by sensor serial
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('metrics', ['metrics_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sensor/readings/latest'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

