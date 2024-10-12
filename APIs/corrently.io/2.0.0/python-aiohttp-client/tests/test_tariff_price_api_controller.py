# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.componentsh0 import Componentsh0
from openapi_server.models.tariffh0 import Tariffh0


pytestmark = pytest.mark.asyncio

async def test_tariff_slph0(client):
    """Test case for tariff_slph0

    Energy Tariff information
    """
    params = [('zipcode', 'zipcode_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/tariff/slph0',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tariffcomponents(client):
    """Test case for tariffcomponents

    Energy Tariff price components
    """
    params = [('zipcode', 'zipcode_example'),
                    ('email', 'email_example'),
                    ('kwha', 56),
                    ('milliseconds', 56),
                    ('wh', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/tariff/components',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

