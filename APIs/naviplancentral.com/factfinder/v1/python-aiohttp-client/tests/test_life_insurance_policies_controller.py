# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.life_insurance_policies_model import LifeInsurancePoliciesModel
from openapi_server.models.life_insurance_policy_model import LifeInsurancePolicyModel
from openapi_server.models.life_insurance_policy_subaccount_model import LifeInsurancePolicySubaccountModel
from openapi_server.models.life_insurance_policy_subaccount_with_id_model import LifeInsurancePolicySubaccountWithIdModel
from openapi_server.models.life_insurance_policy_subaccounts_model import LifeInsurancePolicySubaccountsModel
from openapi_server.models.life_insurance_policy_with_id_model import LifeInsurancePolicyWithIdModel


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policies_delete_by_id(client):
    """Test case for life_insurance_policies_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/LifeInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policies_delete_subaccount_by_lifeinsurancepolicyid_id(client):
    """Test case for life_insurance_policies_delete_subaccount_by_lifeinsurancepolicyid_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/LifeInsurancePolicies/{life_insurance_policy_id}/Subaccounts/{id}'.format(life_insurance_policy_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policies_get_by_id(client):
    """Test case for life_insurance_policies_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifeInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policies_get_life_insurance_policies_by_fact_finder_id_by_factfinderid(client):
    """Test case for life_insurance_policies_get_life_insurance_policies_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifeInsurancePolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policies_get_subaccount_by_lifeinsurancepolicyid_id(client):
    """Test case for life_insurance_policies_get_subaccount_by_lifeinsurancepolicyid_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifeInsurancePolicies/{life_insurance_policy_id}/Subaccounts/{id}'.format(life_insurance_policy_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_life_insurance_policies_get_subaccounts_by_lifeinsurancepolicyid(client):
    """Test case for life_insurance_policies_get_subaccounts_by_lifeinsurancepolicyid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/LifeInsurancePolicies/{life_insurance_policy_id}/Subaccounts'.format(life_insurance_policy_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_life_insurance_policies_post_by_model(client):
    """Test case for life_insurance_policies_post_by_model

    
    """
    model = {"factFinderId":1,"premium":7.061401241503109,"beneficiary":"Client","insured":"Client","generalAccountMarketValue":5.637376656633329,"policyType":2,"description":"description","beneficiaryDependentId":0,"externalDestinationId":"externalDestinationId","payer":"Client","benefit":6.027456183070403,"frequency":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/LifeInsurancePolicies',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_life_insurance_policies_post_subaccount_by_lifeinsurancepolicyid_model(client):
    """Test case for life_insurance_policies_post_subaccount_by_lifeinsurancepolicyid_model

    
    """
    model = {"symbol":"symbol","description":"description","marketValue":0.8008281904610115,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/LifeInsurancePolicies/{life_insurance_policy_id}/Subaccounts'.format(life_insurance_policy_id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_life_insurance_policies_put_by_id_model(client):
    """Test case for life_insurance_policies_put_by_id_model

    
    """
    model = {"factFinderId":1,"premium":7.061401241503109,"beneficiary":"Client","insured":"Client","generalAccountMarketValue":5.637376656633329,"policyType":2,"description":"description","beneficiaryDependentId":0,"externalDestinationId":"externalDestinationId","payer":"Client","benefit":6.027456183070403,"frequency":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/LifeInsurancePolicies/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_life_insurance_policies_put_subaccount_by_lifeinsurancepolicyid_id_model(client):
    """Test case for life_insurance_policies_put_subaccount_by_lifeinsurancepolicyid_id_model

    
    """
    model = {"symbol":"symbol","description":"description","marketValue":0.8008281904610115,"externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/LifeInsurancePolicies/{life_insurance_policy_id}/Subaccounts/{id}'.format(life_insurance_policy_id=56, id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

