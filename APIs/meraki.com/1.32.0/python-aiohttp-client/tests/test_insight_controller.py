# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_insight_monitored_media_server_request import CreateOrganizationInsightMonitoredMediaServerRequest
from openapi_server.models.get_network_insight_application_health_by_time200_response_inner import GetNetworkInsightApplicationHealthByTime200ResponseInner
from openapi_server.models.get_organization_insight_applications200_response_inner import GetOrganizationInsightApplications200ResponseInner
from openapi_server.models.get_organization_insight_monitored_media_servers200_response_inner import GetOrganizationInsightMonitoredMediaServers200ResponseInner
from openapi_server.models.update_organization_insight_monitored_media_server_request import UpdateOrganizationInsightMonitoredMediaServerRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_insight_monitored_media_server(client):
    """Test case for create_organization_insight_monitored_media_server

    Add a media server to be monitored for this organization
    """
    body = openapi_server.CreateOrganizationInsightMonitoredMediaServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/insight/monitoredMediaServers'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_insight_monitored_media_server(client):
    """Test case for delete_organization_insight_monitored_media_server

    Delete a monitored media server from this organization
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}'.format(organization_id='organization_id_example', monitored_media_server_id='monitored_media_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_insight_application_health_by_time(client):
    """Test case for get_network_insight_application_health_by_time

    Get application health by time
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/insight/applications/{application_id}/healthByTime'.format(network_id='network_id_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_insight_applications(client):
    """Test case for get_organization_insight_applications

    List all Insight tracked applications
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/insight/applications'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_insight_monitored_media_server(client):
    """Test case for get_organization_insight_monitored_media_server

    Return a monitored media server for this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}'.format(organization_id='organization_id_example', monitored_media_server_id='monitored_media_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_insight_monitored_media_servers(client):
    """Test case for get_organization_insight_monitored_media_servers

    List the monitored media servers for this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/insight/monitoredMediaServers'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_insight_monitored_media_server(client):
    """Test case for update_organization_insight_monitored_media_server

    Update a monitored media server for this organization
    """
    body = openapi_server.UpdateOrganizationInsightMonitoredMediaServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/insight/monitoredMediaServers/{monitored_media_server_id}'.format(organization_id='organization_id_example', monitored_media_server_id='monitored_media_server_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

