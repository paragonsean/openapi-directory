# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.liability_type_model import LiabilityTypeModel
from openapi_server.models.liability_types_model import LiabilityTypesModel


pytestmark = pytest.mark.asyncio

async def test_liability_types_get_by_country(client):
    """Test case for liability_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LiabilityTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_liability_types_get_by_id(client):
    """Test case for liability_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LiabilityTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

