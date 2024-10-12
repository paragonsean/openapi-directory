# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ip_address_entity import IpAddressEntity
from openapi_server.models.public_ip_address_entity import PublicIpAddressEntity


pytestmark = pytest.mark.asyncio

async def test_get_ip_addresses(client):
    """Test case for get_ip_addresses

    List IP Addresses associated with the current site
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/ip_addresses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ip_addresses_exavault_reserved(client):
    """Test case for get_ip_addresses_exavault_reserved

    List all possible public ExaVault IP addresses
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/ip_addresses/exavault-reserved',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ip_addresses_reserved(client):
    """Test case for get_ip_addresses_reserved

    List all possible public IP addresses
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/ip_addresses/reserved',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

