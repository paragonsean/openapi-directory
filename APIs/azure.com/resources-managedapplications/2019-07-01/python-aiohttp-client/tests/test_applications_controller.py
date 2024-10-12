# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_applications_create_or_update(client):
    """Test case for applications_create_or_update

    
    """
    parameters = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"customerSupport":{"phone":"phone","contactName":"contactName","email":"email"},"outputs":"{}","jitAccessPolicy":{"jitApprovers":[{"displayName":"displayName","id":"id","type":"user"},{"displayName":"displayName","id":"id","type":"user"}],"jitApprovalMode":"NotSpecified","jitAccessEnabled":True,"maximumJitAccessDuration":"maximumJitAccessDuration"},"updatedBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"billingDetails":{"resourceUsageId":"resourceUsageId"},"authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"publisherTenantId":"publisherTenantId","managementMode":"NotSpecified","provisioningState":"NotSpecified","applicationDefinitionId":"applicationDefinitionId","createdBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"managedResourceGroupId":"managedResourceGroupId","supportUrls":{"governmentCloud":"governmentCloud","publicAzure":"publicAzure"},"parameters":"{}","artifacts":[{"name":"NotSpecified","type":"NotSpecified","uri":"uri"},{"name":"NotSpecified","type":"NotSpecified","uri":"uri"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_create_or_update_by_id(client):
    """Test case for applications_create_or_update_by_id

    
    """
    parameters = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"customerSupport":{"phone":"phone","contactName":"contactName","email":"email"},"outputs":"{}","jitAccessPolicy":{"jitApprovers":[{"displayName":"displayName","id":"id","type":"user"},{"displayName":"displayName","id":"id","type":"user"}],"jitApprovalMode":"NotSpecified","jitAccessEnabled":True,"maximumJitAccessDuration":"maximumJitAccessDuration"},"updatedBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"billingDetails":{"resourceUsageId":"resourceUsageId"},"authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"publisherTenantId":"publisherTenantId","managementMode":"NotSpecified","provisioningState":"NotSpecified","applicationDefinitionId":"applicationDefinitionId","createdBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"managedResourceGroupId":"managedResourceGroupId","supportUrls":{"governmentCloud":"governmentCloud","publicAzure":"publicAzure"},"parameters":"{}","artifacts":[{"name":"NotSpecified","type":"NotSpecified","uri":"uri"},{"name":"NotSpecified","type":"NotSpecified","uri":"uri"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_delete(client):
    """Test case for applications_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_delete_by_id(client):
    """Test case for applications_delete_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_get(client):
    """Test case for applications_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_get_by_id(client):
    """Test case for applications_get_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list_by_resource_group(client):
    """Test case for applications_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list_by_subscription(client):
    """Test case for applications_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Solutions/applications'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_refresh_permissions(client):
    """Test case for applications_refresh_permissions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}/refreshPermissions'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_update(client):
    """Test case for applications_update

    
    """
    parameters = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"customerSupport":{"phone":"phone","contactName":"contactName","email":"email"},"outputs":"{}","jitAccessPolicy":{"jitApprovers":[{"displayName":"displayName","id":"id","type":"user"},{"displayName":"displayName","id":"id","type":"user"}],"jitApprovalMode":"NotSpecified","jitAccessEnabled":True,"maximumJitAccessDuration":"maximumJitAccessDuration"},"updatedBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"billingDetails":{"resourceUsageId":"resourceUsageId"},"authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"publisherTenantId":"publisherTenantId","managementMode":"NotSpecified","provisioningState":"NotSpecified","applicationDefinitionId":"applicationDefinitionId","createdBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"managedResourceGroupId":"managedResourceGroupId","supportUrls":{"governmentCloud":"governmentCloud","publicAzure":"publicAzure"},"parameters":"{}","artifacts":[{"name":"NotSpecified","type":"NotSpecified","uri":"uri"},{"name":"NotSpecified","type":"NotSpecified","uri":"uri"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_update_by_id(client):
    """Test case for applications_update_by_id

    
    """
    parameters = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"customerSupport":{"phone":"phone","contactName":"contactName","email":"email"},"outputs":"{}","jitAccessPolicy":{"jitApprovers":[{"displayName":"displayName","id":"id","type":"user"},{"displayName":"displayName","id":"id","type":"user"}],"jitApprovalMode":"NotSpecified","jitAccessEnabled":True,"maximumJitAccessDuration":"maximumJitAccessDuration"},"updatedBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"billingDetails":{"resourceUsageId":"resourceUsageId"},"authorizations":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"publisherTenantId":"publisherTenantId","managementMode":"NotSpecified","provisioningState":"NotSpecified","applicationDefinitionId":"applicationDefinitionId","createdBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"managedResourceGroupId":"managedResourceGroupId","supportUrls":{"governmentCloud":"governmentCloud","publicAzure":"publicAzure"},"parameters":"{}","artifacts":[{"name":"NotSpecified","type":"NotSpecified","uri":"uri"},{"name":"NotSpecified","type":"NotSpecified","uri":"uri"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

