# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_customer_profile_evaluation_response import ListCustomerProfileEvaluationResponse
from openapi_server.models.trusthub_v1_customer_profile_customer_profile_evaluation import TrusthubV1CustomerProfileCustomerProfileEvaluation


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_customer_profile_evaluation(client):
    """Test case for create_customer_profile_evaluation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'policy_sid': 'policy_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/CustomerProfiles/{customer_profile_sid}/Evaluations'.format(customer_profile_sid='customer_profile_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_customer_profile_evaluation(client):
    """Test case for fetch_customer_profile_evaluation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CustomerProfiles/{customer_profile_sid}/Evaluations/{sid}'.format(customer_profile_sid='customer_profile_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_customer_profile_evaluation(client):
    """Test case for list_customer_profile_evaluation

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CustomerProfiles/{customer_profile_sid}/Evaluations'.format(customer_profile_sid='customer_profile_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

