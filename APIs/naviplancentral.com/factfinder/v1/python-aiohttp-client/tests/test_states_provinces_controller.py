# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.state_province_model import StateProvinceModel
from openapi_server.models.states_provinces_model import StatesProvincesModel


pytestmark = pytest.mark.asyncio

async def test_states_provinces_get_by_country(client):
    """Test case for states_provinces_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/StatesProvinces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_states_provinces_get_by_id(client):
    """Test case for states_provinces_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/StatesProvinces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

