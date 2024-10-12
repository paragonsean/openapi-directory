# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_splash_login_attempts(client):
    """Test case for get_network_splash_login_attempts

    List the splash login attempts for a network
    """
    params = [('ssidNumber', 56),
                    ('loginIdentifier', 'login_identifier_example'),
                    ('timespan', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/splashLoginAttempts'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

