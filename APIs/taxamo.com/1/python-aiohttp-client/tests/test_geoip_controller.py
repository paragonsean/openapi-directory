# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.locate_given_ip_out import LocateGivenIPOut
from openapi_server.models.locate_my_ip_out import LocateMyIPOut


pytestmark = pytest.mark.asyncio

async def test_locate_given_ip(client):
    """Test case for locate_given_ip

    Locate provided IP
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/geoip/{ip}'.format(ip='ip_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locate_my_ip(client):
    """Test case for locate_my_ip

    Locate IP
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/geoip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

