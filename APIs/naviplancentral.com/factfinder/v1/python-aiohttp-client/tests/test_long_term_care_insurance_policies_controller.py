# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.long_term_care_insurance_policies_model import LongTermCareInsurancePoliciesModel
from openapi_server.models.long_term_care_insurance_policy_model import LongTermCareInsurancePolicyModel
from openapi_server.models.long_term_care_insurance_policy_with_id_model import LongTermCareInsurancePolicyWithIdModel


pytestmark = pytest.mark.asyncio

async def test_long_term_care_insurance_policies_delete_by_id(client):
    """Test case for long_term_care_insurance_policies_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/LongTermCareInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_care_insurance_policies_get_by_id(client):
    """Test case for long_term_care_insurance_policies_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LongTermCareInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_care_insurance_policies_get_long_term_care_insurance_policies_by_fact_finder_id_by_factfinderid(client):
    """Test case for long_term_care_insurance_policies_get_long_term_care_insurance_policies_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LongTermCareInsurancePolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_long_term_care_insurance_policies_post_by_model(client):
    """Test case for long_term_care_insurance_policies_post_by_model

    
    """
    model = {"factFinderId":1,"premium":5.962133916683182,"insured":"Client","description":"description","premiumFrequency":5,"benefitFrequency":6,"externalDestinationId":"externalDestinationId","benefit":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/LongTermCareInsurancePolicies',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_long_term_care_insurance_policies_put_by_id_model(client):
    """Test case for long_term_care_insurance_policies_put_by_id_model

    
    """
    model = {"factFinderId":1,"premium":5.962133916683182,"insured":"Client","description":"description","premiumFrequency":5,"benefitFrequency":6,"externalDestinationId":"externalDestinationId","benefit":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/LongTermCareInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

