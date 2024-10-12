# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.income_type_model import IncomeTypeModel
from openapi_server.models.income_types_model import IncomeTypesModel


pytestmark = pytest.mark.asyncio

async def test_income_types_get_by_country(client):
    """Test case for income_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/IncomeTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_income_types_get_by_id(client):
    """Test case for income_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/IncomeTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

