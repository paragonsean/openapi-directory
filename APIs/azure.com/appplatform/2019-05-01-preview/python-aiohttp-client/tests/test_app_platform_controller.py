# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_resource import AppResource
from openapi_server.models.app_resource_collection import AppResourceCollection
from openapi_server.models.available_operations import AvailableOperations
from openapi_server.models.binding_resource import BindingResource
from openapi_server.models.binding_resource_collection import BindingResourceCollection
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment_resource import DeploymentResource
from openapi_server.models.deployment_resource_collection import DeploymentResourceCollection
from openapi_server.models.log_file_url_response import LogFileUrlResponse
from openapi_server.models.name_availability import NameAvailability
from openapi_server.models.name_availability_parameters import NameAvailabilityParameters
from openapi_server.models.regenerate_test_key_request_payload import RegenerateTestKeyRequestPayload
from openapi_server.models.resource_upload_definition import ResourceUploadDefinition
from openapi_server.models.service_resource import ServiceResource
from openapi_server.models.service_resource_list import ServiceResourceList
from openapi_server.models.test_keys import TestKeys


pytestmark = pytest.mark.asyncio

async def test_apps_create_or_update(client):
    """Test case for apps_create_or_update

    
    """
    app_resource = {"properties":{"persistentDisk":{"mountPath":"mountPath","sizeInGB":4,"usedInGB":30},"public":True,"createdTime":"2000-01-23T04:56:07.000+00:00","temporaryDisk":{"mountPath":"mountPath","sizeInGB":0},"provisioningState":"Succeeded","activeDeploymentName":"activeDeploymentName","url":"url"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example'),
        headers=headers,
        json=app_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_delete(client):
    """Test case for apps_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get(client):
    """Test case for apps_get

    
    """
    params = [('syncStatus', 'sync_status_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_resource_upload_url(client):
    """Test case for apps_get_resource_upload_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/getResourceUploadUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list(client):
    """Test case for apps_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_update(client):
    """Test case for apps_update

    
    """
    app_resource = {"properties":{"persistentDisk":{"mountPath":"mountPath","sizeInGB":4,"usedInGB":30},"public":True,"createdTime":"2000-01-23T04:56:07.000+00:00","temporaryDisk":{"mountPath":"mountPath","sizeInGB":0},"provisioningState":"Succeeded","activeDeploymentName":"activeDeploymentName","url":"url"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example'),
        headers=headers,
        json=app_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bindings_create_or_update(client):
    """Test case for bindings_create_or_update

    
    """
    binding_resource = {"properties":{"createdAt":"createdAt","resourceId":"resourceId","bindingParameters":{"key":"{}"},"resourceName":"resourceName","generatedProperties":"generatedProperties","key":"key","resourceType":"resourceType","updatedAt":"updatedAt"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/bindings/{binding_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', binding_name='binding_name_example'),
        headers=headers,
        json=binding_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bindings_delete(client):
    """Test case for bindings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/bindings/{binding_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', binding_name='binding_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bindings_get(client):
    """Test case for bindings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/bindings/{binding_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', binding_name='binding_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bindings_list(client):
    """Test case for bindings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/bindings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bindings_update(client):
    """Test case for bindings_update

    
    """
    binding_resource = {"properties":{"createdAt":"createdAt","resourceId":"resourceId","bindingParameters":{"key":"{}"},"resourceName":"resourceName","generatedProperties":"generatedProperties","key":"key","resourceType":"resourceType","updatedAt":"updatedAt"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/bindings/{binding_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', binding_name='binding_name_example'),
        headers=headers,
        json=binding_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_create_or_update(client):
    """Test case for deployments_create_or_update

    
    """
    deployment_resource = {"properties":{"instances":[{"reason":"reason","discoveryStatus":"discoveryStatus","name":"name","status":"status"},{"reason":"reason","discoveryStatus":"discoveryStatus","name":"name","status":"status"}],"appName":"appName","active":True,"createdTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"Creating","source":{"artifactSelector":"artifactSelector","relativePath":"relativePath","type":"Jar","version":"version"},"deploymentSettings":{"runtimeVersion":"Java_8","environmentVariables":{"key":"environmentVariables"},"instanceCount":12,"cpu":1,"memoryInGB":2,"jvmOptions":"jvmOptions"},"status":"Unknown"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
        headers=headers,
        json=deployment_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_delete(client):
    """Test case for deployments_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_get_log_file_url(client):
    """Test case for deployments_get_log_file_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}/getLogFileUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list(client):
    """Test case for deployments_list

    
    """
    params = [('version', ['version_example']),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_list_cluster_all_deployments(client):
    """Test case for deployments_list_cluster_all_deployments

    
    """
    params = [('version', ['version_example']),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/deployments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_restart(client):
    """Test case for deployments_restart

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}/restart'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_start(client):
    """Test case for deployments_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_stop(client):
    """Test case for deployments_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_update(client):
    """Test case for deployments_update

    
    """
    deployment_resource = {"properties":{"instances":[{"reason":"reason","discoveryStatus":"discoveryStatus","name":"name","status":"status"},{"reason":"reason","discoveryStatus":"discoveryStatus","name":"name","status":"status"}],"appName":"appName","active":True,"createdTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"Creating","source":{"artifactSelector":"artifactSelector","relativePath":"relativePath","type":"Jar","version":"version"},"deploymentSettings":{"runtimeVersion":"Java_8","environmentVariables":{"key":"environmentVariables"},"instanceCount":12,"cpu":1,"memoryInGB":2,"jvmOptions":"jvmOptions"},"status":"Unknown"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/apps/{app_name}/deployments/{deployment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', app_name='app_name_example', deployment_name='deployment_name_example'),
        headers=headers,
        json=deployment_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.AppPlatform/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_check_name_availability(client):
    """Test case for services_check_name_availability

    
    """
    availability_parameters = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AppPlatform/locations/{location}/checkNameAvailability'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=availability_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_create_or_update(client):
    """Test case for services_create_or_update

    
    """
    resource = {"properties":{"trace":{"appInsightInstrumentationKey":"appInsightInstrumentationKey","state":"NotAvailable","error":{"code":"code","message":"message"},"enabled":True},"provisioningState":"Creating","serviceId":"serviceId","version":0,"configServerProperties":{"configServer":{"gitProperty":{"privateKey":"privateKey","password":"password","repositories":[{"privateKey":"privateKey","password":"password","strictHostKeyChecking":True,"searchPaths":["searchPaths","searchPaths"],"name":"name","pattern":["pattern","pattern"],"hostKey":"hostKey","label":"label","hostKeyAlgorithm":"hostKeyAlgorithm","uri":"uri","username":"username"},{"privateKey":"privateKey","password":"password","strictHostKeyChecking":True,"searchPaths":["searchPaths","searchPaths"],"name":"name","pattern":["pattern","pattern"],"hostKey":"hostKey","label":"label","hostKeyAlgorithm":"hostKeyAlgorithm","uri":"uri","username":"username"}],"strictHostKeyChecking":True,"searchPaths":["searchPaths","searchPaths"],"hostKey":"hostKey","label":"label","hostKeyAlgorithm":"hostKeyAlgorithm","uri":"uri","username":"username"}},"state":"NotAvailable","error":{"code":"code","message":"message"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        json=resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_delete(client):
    """Test case for services_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_disable_test_endpoint(client):
    """Test case for services_disable_test_endpoint

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/disableTestEndpoint'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_enable_test_endpoint(client):
    """Test case for services_enable_test_endpoint

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/enableTestEndpoint'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get(client):
    """Test case for services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list(client):
    """Test case for services_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_by_subscription(client):
    """Test case for services_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AppPlatform/Spring'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_test_keys(client):
    """Test case for services_list_test_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/listTestKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_regenerate_test_key(client):
    """Test case for services_regenerate_test_key

    
    """
    regenerate_test_key_request = {"keyType":"Primary"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}/regenerateTestKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        json=regenerate_test_key_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_update(client):
    """Test case for services_update

    
    """
    resource = {"properties":{"trace":{"appInsightInstrumentationKey":"appInsightInstrumentationKey","state":"NotAvailable","error":{"code":"code","message":"message"},"enabled":True},"provisioningState":"Creating","serviceId":"serviceId","version":0,"configServerProperties":{"configServer":{"gitProperty":{"privateKey":"privateKey","password":"password","repositories":[{"privateKey":"privateKey","password":"password","strictHostKeyChecking":True,"searchPaths":["searchPaths","searchPaths"],"name":"name","pattern":["pattern","pattern"],"hostKey":"hostKey","label":"label","hostKeyAlgorithm":"hostKeyAlgorithm","uri":"uri","username":"username"},{"privateKey":"privateKey","password":"password","strictHostKeyChecking":True,"searchPaths":["searchPaths","searchPaths"],"name":"name","pattern":["pattern","pattern"],"hostKey":"hostKey","label":"label","hostKeyAlgorithm":"hostKeyAlgorithm","uri":"uri","username":"username"}],"strictHostKeyChecking":True,"searchPaths":["searchPaths","searchPaths"],"hostKey":"hostKey","label":"label","hostKeyAlgorithm":"hostKeyAlgorithm","uri":"uri","username":"username"}},"state":"NotAvailable","error":{"code":"code","message":"message"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AppPlatform/Spring/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        json=resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

