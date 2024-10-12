# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.windows_hosting import WindowsHosting
from openapi_server.models.windows_hosting_detail import WindowsHostingDetail


pytestmark = pytest.mark.asyncio

async def test_get_windows_hosting(client):
    """Test case for get_windows_hosting

    Windows hosting detail
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/windowshostings/{domain_name}'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_windows_hostings(client):
    """Test case for get_windows_hostings

    Overview of windows hostings
    """
    params = [('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/windowshostings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

