# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.critical_illness_insurance_policy_type_model import CriticalIllnessInsurancePolicyTypeModel
from openapi_server.models.critical_illness_insurance_policy_types_model import CriticalIllnessInsurancePolicyTypesModel


pytestmark = pytest.mark.asyncio

async def test_critical_illness_insurance_policy_types_get_by_country(client):
    """Test case for critical_illness_insurance_policy_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/CriticalIllnessInsurancePolicyTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_critical_illness_insurance_policy_types_get_by_id(client):
    """Test case for critical_illness_insurance_policy_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/CriticalIllnessInsurancePolicyTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

