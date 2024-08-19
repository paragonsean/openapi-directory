# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_deployment_resource_entity import ProductDeploymentResourceEntity
from openapi_server.models.product_deployments_boot_strap_request import ProductDeploymentsBootStrapRequest
from openapi_server.models.product_deployments_deploy_request import ProductDeploymentsDeployRequest
from openapi_server.models.product_deployments_list import ProductDeploymentsList
from openapi_server.models.product_deployments_unlock_request import ProductDeploymentsUnlockRequest


pytestmark = pytest.mark.asyncio

async def test_product_deployments_boot_strap(client):
    """Test case for product_deployments_boot_strap

    
    """
    bootstrap_action_parameter = openapi_server.ProductDeploymentsBootStrapRequest()
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{product_id}/bootstrap'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        json=bootstrap_action_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_deployments_deploy(client):
    """Test case for product_deployments_deploy

    
    """
    deploy_action_parameter = openapi_server.ProductDeploymentsDeployRequest()
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{product_id}/deploy'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        json=deploy_action_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_deployments_get(client):
    """Test case for product_deployments_get

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{product_id}'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_deployments_list(client):
    """Test case for product_deployments_list

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_deployments_lock(client):
    """Test case for product_deployments_lock

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{product_id}/lock'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_deployments_remove(client):
    """Test case for product_deployments_remove

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{product_id}/remove'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_deployments_rotate_secrets(client):
    """Test case for product_deployments_rotate_secrets

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{product_id}/rotateSecrets'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_deployments_unlock(client):
    """Test case for product_deployments_unlock

    
    """
    unlock_action_parameter = openapi_server.ProductDeploymentsUnlockRequest()
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{product_id}/unlock'.format(subscription_id='subscription_id_example', product_id='product_id_example'),
        headers=headers,
        json=unlock_action_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

