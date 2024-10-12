# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.life_insurance_policy_type_model import LifeInsurancePolicyTypeModel
from openapi_server.models.life_insurance_policy_types_model import LifeInsurancePolicyTypesModel


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policy_types_get_by_country(client):
    """Test case for life_insurance_policy_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifeInsurancePolicyTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policy_types_get_by_id(client):
    """Test case for life_insurance_policy_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifeInsurancePolicyTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

