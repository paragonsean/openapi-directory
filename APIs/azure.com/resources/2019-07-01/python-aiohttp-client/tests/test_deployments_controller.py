# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_export_result import DeploymentExportResult
from openapi_server.models.deployment_extended import DeploymentExtended
from openapi_server.models.deployment_list_result import DeploymentListResult
from openapi_server.models.deployment_validate_result import DeploymentValidateResult
from openapi_server.models.deployment_what_if import DeploymentWhatIf
from openapi_server.models.template_hash_result import TemplateHashResult
from openapi_server.models.what_if_operation_result import WhatIfOperationResult


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

    Cancels a currently running template deployment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
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

async def test_deployments_cancel_at_management_group_scope(client):
    """Test case for deployments_cancel_at_management_group_scope

    Cancels a currently running template deployment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}/cancel'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_cancel_at_scope(client):
    """Test case for deployments_cancel_at_scope

    Cancels a currently running template deployment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}/cancel'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_cancel_at_subscription_scope(client):
    """Test case for deployments_cancel_at_subscription_scope

    Cancels a currently running template deployment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}/cancel'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_cancel_at_tenant_scope(client):
    """Test case for deployments_cancel_at_tenant_scope

    Cancels a currently running template deployment.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}/cancel'.format(deployment_name='deployment_name_example'),
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
        'Accept': 'application/json',
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

async def test_deployments_check_existence_at_management_group_scope(client):
    """Test case for deployments_check_existence_at_management_group_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_check_existence_at_scope(client):
    """Test case for deployments_check_existence_at_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_check_existence_at_subscription_scope(client):
    """Test case for deployments_check_existence_at_subscription_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_check_existence_at_tenant_scope(client):
    """Test case for deployments_check_existence_at_tenant_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_create_or_update(client):
    """Test case for deployments_create_or_update

    Deploys resources to a resource group.
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
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

async def test_deployments_create_or_update_at_management_group_scope(client):
    """Test case for deployments_create_or_update_at_management_group_scope

    Deploys resources at management group scope.
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_create_or_update_at_scope(client):
    """Test case for deployments_create_or_update_at_scope

    Deploys resources at a given scope.
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_create_or_update_at_subscription_scope(client):
    """Test case for deployments_create_or_update_at_subscription_scope

    Deploys resources at subscription scope.
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_create_or_update_at_tenant_scope(client):
    """Test case for deployments_create_or_update_at_tenant_scope

    Deploys resources at tenant scope.
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_delete(client):
    """Test case for deployments_delete

    Deletes a deployment from the deployment history.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
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

async def test_deployments_delete_at_management_group_scope(client):
    """Test case for deployments_delete_at_management_group_scope

    Deletes a deployment from the deployment history.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_delete_at_scope(client):
    """Test case for deployments_delete_at_scope

    Deletes a deployment from the deployment history.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_delete_at_subscription_scope(client):
    """Test case for deployments_delete_at_subscription_scope

    Deletes a deployment from the deployment history.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_delete_at_tenant_scope(client):
    """Test case for deployments_delete_at_tenant_scope

    Deletes a deployment from the deployment history.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_export_template(client):
    """Test case for deployments_export_template

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}/exportTemplate'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_export_template_at_management_group_scope(client):
    """Test case for deployments_export_template_at_management_group_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}/exportTemplate'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_export_template_at_scope(client):
    """Test case for deployments_export_template_at_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}/exportTemplate'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_export_template_at_subscription_scope(client):
    """Test case for deployments_export_template_at_subscription_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}/exportTemplate'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_export_template_at_tenant_scope(client):
    """Test case for deployments_export_template_at_tenant_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}/exportTemplate'.format(deployment_name='deployment_name_example'),
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

async def test_deployments_get_at_management_group_scope(client):
    """Test case for deployments_get_at_management_group_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_get_at_scope(client):
    """Test case for deployments_get_at_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_get_at_subscription_scope(client):
    """Test case for deployments_get_at_subscription_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_get_at_tenant_scope(client):
    """Test case for deployments_get_at_tenant_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list_at_management_group_scope(client):
    """Test case for deployments_list_at_management_group_scope

    
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
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list_at_scope(client):
    """Test case for deployments_list_at_scope

    
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
        path='/{scope}/providers/Microsoft.Resources/deployments'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list_at_subscription_scope(client):
    """Test case for deployments_list_at_subscription_scope

    
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list_at_tenant_scope(client):
    """Test case for deployments_list_at_tenant_scope

    
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
        path='/providers/Microsoft.Resources/deployments/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list_by_resource_group(client):
    """Test case for deployments_list_by_resource_group

    
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
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
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


pytestmark = pytest.mark.asyncio

async def test_deployments_validate_at_management_group_scope(client):
    """Test case for deployments_validate_at_management_group_scope

    
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}/validate'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_validate_at_scope(client):
    """Test case for deployments_validate_at_scope

    
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}/validate'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_validate_at_subscription_scope(client):
    """Test case for deployments_validate_at_subscription_scope

    
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}/validate'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_validate_at_tenant_scope(client):
    """Test case for deployments_validate_at_tenant_scope

    
    """
    parameters = {"location":"location","properties":{"mode":"Incremental","parametersLink":{"contentVersion":"contentVersion","uri":"uri"},"template":"{}","onErrorDeployment":{"deploymentName":"deploymentName","type":"LastSuccessful"},"templateLink":{"contentVersion":"contentVersion","uri":"uri"},"parameters":"{}","debugSetting":{"detailLevel":"detailLevel"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}/validate'.format(deployment_name='deployment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_what_if(client):
    """Test case for deployments_what_if

    
    """
    parameters = {"location":"location","properties":{"whatIfSettings":{"resultFormat":"ResourceIdOnly"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Resources/deployments/{deployment_name}/whatIf'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_what_if_at_subscription_scope(client):
    """Test case for deployments_what_if_at_subscription_scope

    
    """
    parameters = {"location":"location","properties":{"whatIfSettings":{"resultFormat":"ResourceIdOnly"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}/whatIf'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

