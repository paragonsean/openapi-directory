# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server.models.product_policy_list_by_product200_response import ProductPolicyListByProduct200Response
from openapi_server.models.product_policy_list_by_product200_response_value_inner import ProductPolicyListByProduct200ResponseValueInner


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_product_policy_create_or_update(client):
    """Test case for product_policy_create_or_update

    
    """
    parameters = openapi_server.ProductPolicyListByProduct200ResponseValueInner()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/products/{product_id}/policies/{policy_id}'.format(product_id='product_id_example', policy_id='policy_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_policy_delete(client):
    """Test case for product_policy_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/products/{product_id}/policies/{policy_id}'.format(product_id='product_id_example', policy_id='policy_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_policy_get(client):
    """Test case for product_policy_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/products/{product_id}/policies/{policy_id}'.format(product_id='product_id_example', policy_id='policy_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_policy_list_by_product(client):
    """Test case for product_policy_list_by_product

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/products/{product_id}/policies'.format(product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

