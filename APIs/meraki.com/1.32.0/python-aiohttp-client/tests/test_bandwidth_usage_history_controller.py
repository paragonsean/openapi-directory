# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_clients_bandwidth_usage_history200_response_inner import GetOrganizationClientsBandwidthUsageHistory200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_clients_bandwidth_usage_history_2(client):
    """Test case for get_network_clients_bandwidth_usage_history_2

    Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/bandwidthUsageHistory'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_clients_bandwidth_usage_history_2(client):
    """Test case for get_organization_clients_bandwidth_usage_history_2

    Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/clients/bandwidthUsageHistory'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

