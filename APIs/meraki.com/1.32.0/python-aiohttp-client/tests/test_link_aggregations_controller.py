# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_switch_link_aggregation_request import CreateNetworkSwitchLinkAggregationRequest
from openapi_server.models.update_network_switch_link_aggregation_request import UpdateNetworkSwitchLinkAggregationRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_link_aggregation_1(client):
    """Test case for create_network_switch_link_aggregation_1

    Create a link aggregation group
    """
    body = openapi_server.CreateNetworkSwitchLinkAggregationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/linkAggregations'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_link_aggregation_1(client):
    """Test case for delete_network_switch_link_aggregation_1

    Split a link aggregation group into separate ports
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}'.format(network_id='network_id_example', link_aggregation_id='link_aggregation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_link_aggregations_1(client):
    """Test case for get_network_switch_link_aggregations_1

    List link aggregation groups
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/linkAggregations'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_link_aggregation_1(client):
    """Test case for update_network_switch_link_aggregation_1

    Update a link aggregation group
    """
    body = openapi_server.UpdateNetworkSwitchLinkAggregationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}'.format(network_id='network_id_example', link_aggregation_id='link_aggregation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

