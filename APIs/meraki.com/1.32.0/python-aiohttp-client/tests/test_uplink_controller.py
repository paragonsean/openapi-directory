# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_cellular_gateway_uplink_statuses200_response_inner import GetOrganizationCellularGatewayUplinkStatuses200ResponseInner
from openapi_server.models.update_network_cellular_gateway_uplink_request import UpdateNetworkCellularGatewayUplinkRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_cellular_gateway_uplink_1(client):
    """Test case for get_network_cellular_gateway_uplink_1

    Returns the uplink settings for your MG network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/cellularGateway/uplink'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_cellular_gateway_uplink_statuses_1(client):
    """Test case for get_organization_cellular_gateway_uplink_statuses_1

    List the uplink status of every Meraki MG cellular gateway in the organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('iccids', ['iccids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/cellularGateway/uplink/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_cellular_gateway_uplink_1(client):
    """Test case for update_network_cellular_gateway_uplink_1

    Updates the uplink settings for your MG network.
    """
    body = openapi_server.UpdateNetworkCellularGatewayUplinkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/cellularGateway/uplink'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

