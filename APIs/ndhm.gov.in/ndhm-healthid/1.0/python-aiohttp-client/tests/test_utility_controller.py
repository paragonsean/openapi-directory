# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.district_dto import DistrictDTO
from openapi_server.models.states_dto import StatesDTO


pytestmark = pytest.mark.asyncio

async def test_get_districts_in_state_using_get(client):
    """Test case for get_districts_in_state_using_get

    Get a list of districts in a given  State as per LGD.
    """
    params = [('stateCode', 'state_code_example')]
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ha/lgd/districts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_states_using_get(client):
    """Test case for get_states_using_get

    Get a list of states as per LGD.
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ha/lgd/states',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

