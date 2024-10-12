# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_sensor_alerts_profile_request import CreateNetworkSensorAlertsProfileRequest
from openapi_server.models.get_device_sensor_relationships200_response_inner import GetDeviceSensorRelationships200ResponseInner
from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server.models.get_network_sensor_alerts_overview_by_metric200_response_inner import GetNetworkSensorAlertsOverviewByMetric200ResponseInner
from openapi_server.models.get_network_sensor_alerts_profiles200_response_inner import GetNetworkSensorAlertsProfiles200ResponseInner
from openapi_server.models.get_network_sensor_relationships200_response_inner import GetNetworkSensorRelationships200ResponseInner
from openapi_server.models.get_organization_sensor_readings_history200_response_inner import GetOrganizationSensorReadingsHistory200ResponseInner
from openapi_server.models.get_organization_sensor_readings_latest200_response_inner import GetOrganizationSensorReadingsLatest200ResponseInner
from openapi_server.models.update_device_sensor_relationships_request import UpdateDeviceSensorRelationshipsRequest
from openapi_server.models.update_network_sensor_alerts_profile_request import UpdateNetworkSensorAlertsProfileRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_sensor_alerts_profile(client):
    """Test case for create_network_sensor_alerts_profile

    Creates a sensor alert profile for a network.
    """
    body = openapi_server.CreateNetworkSensorAlertsProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sensor/alerts/profiles'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_sensor_alerts_profile(client):
    """Test case for delete_network_sensor_alerts_profile

    Deletes a sensor alert profile from a network.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/sensor/alerts/profiles/{id}'.format(network_id='network_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_sensor_relationships(client):
    """Test case for get_device_sensor_relationships

    List the sensor roles for a given sensor or camera device.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/sensor/relationships'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_alerts_current_overview_by_metric(client):
    """Test case for get_network_sensor_alerts_current_overview_by_metric

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

async def test_get_network_sensor_alerts_overview_by_metric(client):
    """Test case for get_network_sensor_alerts_overview_by_metric

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


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_alerts_profile(client):
    """Test case for get_network_sensor_alerts_profile

    Show details of a sensor alert profile for a network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sensor/alerts/profiles/{id}'.format(network_id='network_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_alerts_profiles(client):
    """Test case for get_network_sensor_alerts_profiles

    Lists all sensor alert profiles for a network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sensor/alerts/profiles'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_relationships(client):
    """Test case for get_network_sensor_relationships

    List the sensor roles for devices in a given network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sensor/relationships'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_sensor_readings_history(client):
    """Test case for get_organization_sensor_readings_history

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

async def test_get_organization_sensor_readings_latest(client):
    """Test case for get_organization_sensor_readings_latest

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


pytestmark = pytest.mark.asyncio

async def test_update_device_sensor_relationships(client):
    """Test case for update_device_sensor_relationships

    Assign one or more sensor roles to a given sensor or camera device.
    """
    body = openapi_server.UpdateDeviceSensorRelationshipsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/sensor/relationships'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_sensor_alerts_profile(client):
    """Test case for update_network_sensor_alerts_profile

    Updates a sensor alert profile for a network.
    """
    body = openapi_server.UpdateNetworkSensorAlertsProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/sensor/alerts/profiles/{id}'.format(network_id='network_id_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

