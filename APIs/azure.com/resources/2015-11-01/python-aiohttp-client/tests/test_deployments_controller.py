# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_extended import DeploymentExtended
from openapi_server.models.deployment_list_result import DeploymentListResult
from openapi_server.models.deployment_validate_result import DeploymentValidateResult
from openapi_server.models.template_hash_result import TemplateHashResult


pytestmark = pytest.mark.asyncio

async def test_deployments_calculate_template_hash(client):
    """Test case for deployments_calculate_template_hash

    
    """
    template = None
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Resources/calculateTemplateHash',
        headers=headers,
        json=template,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_cancel(client):
    """Test case for deployments_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}/cancel'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_check_existence(client):
    """Test case for deployments_check_existence

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_create_or_update(client):
    """Test case for deployments_create_or_update

    
    """
    parameters = {"properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_delete(client):
    """Test case for deployments_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_get(client):
    """Test case for deployments_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list(client):
    """Test case for deployments_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_validate(client):
    """Test case for deployments_validate

    
    """
    parameters = {"properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}/validate'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

