# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.point_info import PointInfo
from openapi_server.models.usage import Usage


pytestmark = pytest.mark.asyncio

async def test_by_point(client):
    """Test case for by_point

    Query by coordinates (SRID 4326 - decimal degrees)
    """
    params = [('school_search_radius', 56),
                    ('park_search_radius', 56)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/@{lat},{lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_by_postcode(client):
    """Test case for by_postcode

    Query by postcode
    """
    params = [('school_search_radius', 56),
                    ('park_search_radius', 56)]
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/postcodes/{postcode}'.format(postcode='postcode_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usage(client):
    """Test case for usage

    Get usage in current month
    """
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/usage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

