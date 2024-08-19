# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.holiday400_response import Holiday400Response
from openapi_server.models.province200_response import Province200Response
from openapi_server.models.provinces200_response import Provinces200Response


pytestmark = pytest.mark.asyncio

async def test_province(client):
    """Test case for province

    Get a province or territory by abbreviation
    """
    params = [('year', 2023),
                    ('optional', false)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/provinces/{province_id}'.format(province_id='MB'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provinces(client):
    """Test case for provinces

    Get all provinces
    """
    params = [('year', 2023),
                    ('optional', false)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/provinces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

