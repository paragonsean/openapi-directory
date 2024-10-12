# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.co2 import CO2
from openapi_server.models.co2_list200_response import Co2List200Response


pytestmark = pytest.mark.asyncio

async def test_co2_list(client):
    """Test case for co2_list

    
    """
    params = [('ppm', 3.4),
                    ('date', '_date_example'),
                    ('date__range', 'date__range_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/co2/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_co2_read(client):
    """Test case for co2_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/co2/{_date}'.format(_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

