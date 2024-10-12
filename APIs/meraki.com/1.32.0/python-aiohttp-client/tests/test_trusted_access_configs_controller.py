# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sm_trusted_access_configs200_response_inner import GetNetworkSmTrustedAccessConfigs200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_trusted_access_configs_1(client):
    """Test case for get_network_sm_trusted_access_configs_1

    List Trusted Access Configs
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
        path='/api/v1/networks/{network_id}/sm/trustedAccessConfigs'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

