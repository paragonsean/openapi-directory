# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_secret import ProductSecret
from openapi_server.models.product_secrets_list import ProductSecretsList
from openapi_server.models.secret_parameters import SecretParameters


pytestmark = pytest.mark.asyncio

async def test_product_secrets_get(client):
    """Test case for product_secrets_get

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{product_id}/secrets/{secret_name}'.format(subscription_id='subscription_id_example', product_id='product_id_example', secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_secrets_import(client):
    """Test case for product_secrets_import

    
    """
    secret_parameters = {"password":"password","pfxPassword":"pfxPassword","secretValue":"secretValue","pfxFileName":"pfxFileName","symmetricKey":"symmetricKey"}
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{product_id}/secrets/{secret_name}/import'.format(subscription_id='subscription_id_example', product_id='product_id_example', secret_name='secret_name_example'),
        headers=headers,
        json=secret_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_secrets_list(client):
    """Test case for product_secrets_list

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productPackages/{product_id}/secrets'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_secrets_validate(client):
    """Test case for product_secrets_validate

    
    """
    secret_parameters = {"password":"password","pfxPassword":"pfxPassword","secretValue":"secretValue","pfxFileName":"pfxFileName","symmetricKey":"symmetricKey"}
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{product_id}/secrets/{secret_name}/validate'.format(subscription_id='subscription_id_example', product_id='product_id_example', secret_name='secret_name_example'),
        headers=headers,
        json=secret_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

