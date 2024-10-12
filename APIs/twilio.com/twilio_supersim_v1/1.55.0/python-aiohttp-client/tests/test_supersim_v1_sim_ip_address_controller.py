# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sim_ip_address_response import ListSimIpAddressResponse


pytestmark = pytest.mark.asyncio

async def test_list_sim_ip_address(client):
    """Test case for list_sim_ip_address

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Sims/{sim_sid}/IpAddresses'.format(sim_sid='sim_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

