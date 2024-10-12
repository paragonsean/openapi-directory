# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_policies_by_client200_response_inner import GetNetworkPoliciesByClient200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_policies_by_client_2(client):
    """Test case for get_network_policies_by_client_2

    Get policies for all clients with policies
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/policies/byClient'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

