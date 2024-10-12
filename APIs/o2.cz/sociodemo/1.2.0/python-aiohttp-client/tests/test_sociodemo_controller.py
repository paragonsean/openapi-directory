# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count_result import CountResult
from openapi_server.models.error_result import ErrorResult


pytestmark = pytest.mark.asyncio

async def test_age(client):
    """Test case for age

    Presence in a location aggregated by age
    """
    params = [('ageGroup', '2'),
                    ('occurenceType', '1'),
                    ('hour', '10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/sociodemo/sandbox/api/age/{location}'.format(location='127752'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender(client):
    """Test case for gender

    Presence in a location aggregated by gender
    """
    params = [('g', '1'),
                    ('occurenceType', '1'),
                    ('hour', '10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/sociodemo/sandbox/api/gender/{location}'.format(location='127752'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

