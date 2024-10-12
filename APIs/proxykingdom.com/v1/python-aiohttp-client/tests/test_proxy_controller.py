# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.proxy import Proxy


pytestmark = pytest.mark.asyncio

async def test_proxy_get(client):
    """Test case for proxy_get

    Gets a random proxy for chosen parameters.
    """
    params = [('Token', 'token_example'),
                    ('Address', 'address_example'),
                    ('Port', 'port_example'),
                    ('Protocol', 'protocol_example'),
                    ('AccessType', 'access_type_example'),
                    ('ResponseTime', 'response_time_example'),
                    ('IsSsl', 'is_ssl_example'),
                    ('Uptime', 'uptime_example'),
                    ('Country', 'country_example'),
                    ('Continent', 'continent_example'),
                    ('Timezone', 'timezone_example'),
                    ('LastTested', 'last_tested_example')]
    headers = { 
        'Accept': 'application/json',
        'correlation_id': '049d3e5c-f02a-4568-a1f4-7bd182668b1b',
    }
    response = await client.request(
        method='GET',
        path='/proxy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

