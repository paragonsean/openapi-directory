# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain_service import DomainService
from openapi_server.models.domain_service_list_result import DomainServiceListResult
from openapi_server.models.operation_entity_list_result import OperationEntityListResult


pytestmark = pytest.mark.asyncio

async def test_domain_service_operations_list(client):
    """Test case for domain_service_operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.AAD/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_services_create_or_update(client):
    """Test case for domain_services_create_or_update

    Create or Update Domain Service (PUT Resource)
    """
    domain_service = {"properties":{"filteredSync":"Enabled","ldapsSettings":{"certificateNotAfter":"2000-01-23T04:56:07.000+00:00","externalAccessIpAddress":"externalAccessIpAddress","pfxCertificatePassword":"pfxCertificatePassword","certificateThumbprint":"certificateThumbprint","publicCertificate":"publicCertificate","ldaps":"Enabled","pfxCertificate":"pfxCertificate","externalAccess":"Enabled"},"subnetId":"subnetId","vnetSiteId":"vnetSiteId","domainControllerIpAddress":["domainControllerIpAddress","domainControllerIpAddress"],"domainSecuritySettings":{"tlsV1":"Enabled","ntlmV1":"Enabled","syncNtlmPasswords":"Enabled"},"healthAlerts":[{"severity":"severity","issue":"issue","lastDetected":"2000-01-23T04:56:07.000+00:00","name":"name","raised":"2000-01-23T04:56:07.000+00:00","id":"id","resolutionUri":"resolutionUri"},{"severity":"severity","issue":"issue","lastDetected":"2000-01-23T04:56:07.000+00:00","name":"name","raised":"2000-01-23T04:56:07.000+00:00","id":"id","resolutionUri":"resolutionUri"}],"provisioningState":"provisioningState","notificationSettings":{"notifyDcAdmins":"Enabled","additionalRecipients":["additionalRecipients","additionalRecipients"],"notifyGlobalAdmins":"Enabled"},"serviceStatus":"serviceStatus","domainName":"domainName","healthLastEvaluated":"2000-01-23T04:56:07.000+00:00","tenantId":"tenantId","healthMonitors":[{"name":"name","details":"details","id":"id"},{"name":"name","details":"details","id":"id"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AAD/domainServices/{domain_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_service_name='domain_service_name_example'),
        headers=headers,
        json=domain_service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_services_delete(client):
    """Test case for domain_services_delete

    Delete Domain Service (DELETE Resource)
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AAD/domainServices/{domain_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_service_name='domain_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_services_get(client):
    """Test case for domain_services_get

    Get Domain Service
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AAD/domainServices/{domain_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_service_name='domain_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_services_list(client):
    """Test case for domain_services_list

    List Domain Services in Subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AAD/domainServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_services_list_by_resource_group(client):
    """Test case for domain_services_list_by_resource_group

    List Domain Services in Resource Group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AAD/domainServices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domain_services_update(client):
    """Test case for domain_services_update

    Update Domain Service (PATCH Resource)
    """
    domain_service = {"properties":{"filteredSync":"Enabled","ldapsSettings":{"certificateNotAfter":"2000-01-23T04:56:07.000+00:00","externalAccessIpAddress":"externalAccessIpAddress","pfxCertificatePassword":"pfxCertificatePassword","certificateThumbprint":"certificateThumbprint","publicCertificate":"publicCertificate","ldaps":"Enabled","pfxCertificate":"pfxCertificate","externalAccess":"Enabled"},"subnetId":"subnetId","vnetSiteId":"vnetSiteId","domainControllerIpAddress":["domainControllerIpAddress","domainControllerIpAddress"],"domainSecuritySettings":{"tlsV1":"Enabled","ntlmV1":"Enabled","syncNtlmPasswords":"Enabled"},"healthAlerts":[{"severity":"severity","issue":"issue","lastDetected":"2000-01-23T04:56:07.000+00:00","name":"name","raised":"2000-01-23T04:56:07.000+00:00","id":"id","resolutionUri":"resolutionUri"},{"severity":"severity","issue":"issue","lastDetected":"2000-01-23T04:56:07.000+00:00","name":"name","raised":"2000-01-23T04:56:07.000+00:00","id":"id","resolutionUri":"resolutionUri"}],"provisioningState":"provisioningState","notificationSettings":{"notifyDcAdmins":"Enabled","additionalRecipients":["additionalRecipients","additionalRecipients"],"notifyGlobalAdmins":"Enabled"},"serviceStatus":"serviceStatus","domainName":"domainName","healthLastEvaluated":"2000-01-23T04:56:07.000+00:00","tenantId":"tenantId","healthMonitors":[{"name":"name","details":"details","id":"id"},{"name":"name","details":"details","id":"id"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.AAD/domainServices/{domain_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_service_name='domain_service_name_example'),
        headers=headers,
        json=domain_service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

