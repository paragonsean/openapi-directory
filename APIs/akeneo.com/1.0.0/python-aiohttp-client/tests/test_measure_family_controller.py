# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.measure_families import MeasureFamilies
from openapi_server.models.measure_families_get200_response import MeasureFamiliesGet200Response
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_measure_families_get(client):
    """Test case for measure_families_get

    Get a measure family
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/measure-families/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_measure_families_get_list(client):
    """Test case for measure_families_get_list

    Get list of measure familiy
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/measure-families',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

