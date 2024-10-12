# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_trust_product_evaluation_response import ListTrustProductEvaluationResponse
from openapi_server.models.trusthub_v1_trust_product_trust_product_evaluation import TrusthubV1TrustProductTrustProductEvaluation


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_trust_product_evaluation(client):
    """Test case for create_trust_product_evaluation

    
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
        path='/v1/TrustProducts/{trust_product_sid}/Evaluations'.format(trust_product_sid='trust_product_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_trust_product_evaluation(client):
    """Test case for fetch_trust_product_evaluation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/TrustProducts/{trust_product_sid}/Evaluations/{sid}'.format(trust_product_sid='trust_product_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_trust_product_evaluation(client):
    """Test case for list_trust_product_evaluation

    
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
        path='/v1/TrustProducts/{trust_product_sid}/Evaluations'.format(trust_product_sid='trust_product_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

