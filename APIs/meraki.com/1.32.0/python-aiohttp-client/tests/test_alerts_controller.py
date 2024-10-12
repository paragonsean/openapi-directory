# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_sensor_alerts_profile_request import CreateNetworkSensorAlertsProfileRequest
from openapi_server.models.create_organization_alerts_profile_request import CreateOrganizationAlertsProfileRequest
from openapi_server.models.get_network_alerts_history200_response_inner import GetNetworkAlertsHistory200ResponseInner
from openapi_server.models.get_network_health_alerts200_response_inner import GetNetworkHealthAlerts200ResponseInner
from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server.models.get_network_sensor_alerts_overview_by_metric200_response_inner import GetNetworkSensorAlertsOverviewByMetric200ResponseInner
from openapi_server.models.get_network_sensor_alerts_profiles200_response_inner import GetNetworkSensorAlertsProfiles200ResponseInner
from openapi_server.models.update_network_alerts_settings_request import UpdateNetworkAlertsSettingsRequest
from openapi_server.models.update_network_sensor_alerts_profile_request import UpdateNetworkSensorAlertsProfileRequest
from openapi_server.models.update_organization_alerts_profile_request import UpdateOrganizationAlertsProfileRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_sensor_alerts_profile_1(client):
    """Test case for create_network_sensor_alerts_profile_1

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

async def test_create_organization_alerts_profile_1(client):
    """Test case for create_organization_alerts_profile_1

    Create an organization-wide alert configuration
    """
    body = openapi_server.CreateOrganizationAlertsProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/alerts/profiles'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_sensor_alerts_profile_1(client):
    """Test case for delete_network_sensor_alerts_profile_1

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

async def test_delete_organization_alerts_profile_1(client):
    """Test case for delete_organization_alerts_profile_1

    Removes an organization-wide alert config
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/alerts/profiles/{alert_config_id}'.format(organization_id='organization_id_example', alert_config_id='alert_config_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_alerts_history_1(client):
    """Test case for get_network_alerts_history_1

    Return the alert history for this network
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/alerts/history'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_alerts_settings_1(client):
    """Test case for get_network_alerts_settings_1

    Return the alert configuration for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/alerts/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_health_alerts_2(client):
    """Test case for get_network_health_alerts_2

    Return all global alerts on this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/health/alerts'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sensor_alerts_current_overview_by_metric_1(client):
    """Test case for get_network_sensor_alerts_current_overview_by_metric_1

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

async def test_get_network_sensor_alerts_overview_by_metric_1(client):
    """Test case for get_network_sensor_alerts_overview_by_metric_1

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

async def test_get_network_sensor_alerts_profile_1(client):
    """Test case for get_network_sensor_alerts_profile_1

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

async def test_get_network_sensor_alerts_profiles_1(client):
    """Test case for get_network_sensor_alerts_profiles_1

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

async def test_get_organization_alerts_profiles_1(client):
    """Test case for get_organization_alerts_profiles_1

    List all organization-wide alert configurations
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/alerts/profiles'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_alerts_settings_1(client):
    """Test case for update_network_alerts_settings_1

    Update the alert configuration for this network
    """
    body = openapi_server.UpdateNetworkAlertsSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/alerts/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_sensor_alerts_profile_1(client):
    """Test case for update_network_sensor_alerts_profile_1

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


pytestmark = pytest.mark.asyncio

async def test_update_organization_alerts_profile_1(client):
    """Test case for update_organization_alerts_profile_1

    Update an organization-wide alert config
    """
    body = openapi_server.UpdateOrganizationAlertsProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/alerts/profiles/{alert_config_id}'.format(organization_id='organization_id_example', alert_config_id='alert_config_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

