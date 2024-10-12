# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.disability_insurance_policies_model import DisabilityInsurancePoliciesModel
from openapi_server.models.disability_insurance_policy_model import DisabilityInsurancePolicyModel
from openapi_server.models.disability_insurance_policy_with_id_model import DisabilityInsurancePolicyWithIdModel


pytestmark = pytest.mark.asyncio

async def test_disability_insurance_policies_delete_by_id(client):
    """Test case for disability_insurance_policies_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/DisabilityInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disability_insurance_policies_get_by_id(client):
    """Test case for disability_insurance_policies_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/DisabilityInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disability_insurance_policies_get_disability_insurance_policies_by_fact_finder_id_by_factfinderid(client):
    """Test case for disability_insurance_policies_get_disability_insurance_policies_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/DisabilityInsurancePolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_disability_insurance_policies_post_by_model(client):
    """Test case for disability_insurance_policies_post_by_model

    
    """
    model = {"factFinderId":1,"premium":5.637376656633329,"insured":"Client","benefitType":"Dollar","policyType":5,"description":"description","premiumFrequency":2,"benefitFrequency":6,"externalDestinationId":"externalDestinationId","benefit":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/DisabilityInsurancePolicies',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_disability_insurance_policies_put_by_id_model(client):
    """Test case for disability_insurance_policies_put_by_id_model

    
    """
    model = {"factFinderId":1,"premium":5.637376656633329,"insured":"Client","benefitType":"Dollar","policyType":5,"description":"description","premiumFrequency":2,"benefitFrequency":6,"externalDestinationId":"externalDestinationId","benefit":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/DisabilityInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

