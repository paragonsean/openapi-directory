# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.disability_insurance_policy_type_model import DisabilityInsurancePolicyTypeModel
from openapi_server.models.disability_insurance_policy_types_model import DisabilityInsurancePolicyTypesModel


pytestmark = pytest.mark.asyncio

async def test_disability_insurance_policy_types_get_by_country(client):
    """Test case for disability_insurance_policy_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/DisabilityInsurancePolicyTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disability_insurance_policy_types_get_by_id(client):
    """Test case for disability_insurance_policy_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/DisabilityInsurancePolicyTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

