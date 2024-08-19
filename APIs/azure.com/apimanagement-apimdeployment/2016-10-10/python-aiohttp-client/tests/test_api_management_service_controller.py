# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_management_service_backup_restore_parameters import ApiManagementServiceBackupRestoreParameters
from openapi_server.models.api_management_service_check_name_availability_parameters import ApiManagementServiceCheckNameAvailabilityParameters
from openapi_server.models.api_management_service_get_sso_token_result import ApiManagementServiceGetSsoTokenResult
from openapi_server.models.api_management_service_list_result import ApiManagementServiceListResult
from openapi_server.models.api_management_service_manage_deployments_parameters import ApiManagementServiceManageDeploymentsParameters
from openapi_server.models.api_management_service_name_availability_result import ApiManagementServiceNameAvailabilityResult
from openapi_server.models.api_management_service_resource import ApiManagementServiceResource
from openapi_server.models.api_management_service_update_hostname_parameters import ApiManagementServiceUpdateHostnameParameters
from openapi_server.models.api_management_service_update_parameters import ApiManagementServiceUpdateParameters
from openapi_server.models.api_management_service_upload_certificate_parameters import ApiManagementServiceUploadCertificateParameters
from openapi_server.models.certificate_information import CertificateInformation
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_api_management_services_apply_network_configuration_updates(client):
    """Test case for api_management_services_apply_network_configuration_updates

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/applynetworkconfigurationupdates'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_backup(client):
    """Test case for api_management_services_backup

    
    """
    parameters = {"accessKey":"accessKey","containerName":"containerName","storageAccount":"storageAccount","backupName":"backupName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/backup'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_check_name_availability(client):
    """Test case for api_management_services_check_name_availability

    
    """
    parameters = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ApiManagement/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_create_or_update(client):
    """Test case for api_management_services_create_or_update

    
    """
    parameters = {"etag":"etag","sku":{"name":"Developer","capacity":6},"properties":{"additionalLocations":[{"staticIPs":["staticIPs","staticIPs"],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"location":"location","skuType":"Developer","skuUnitCount":0},{"staticIPs":["staticIPs","staticIPs"],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"location":"location","skuType":"Developer","skuUnitCount":0}],"provisioningState":"provisioningState","scmUrl":"scmUrl","customProperties":{"key":"customProperties"},"addresserEmail":"addresserEmail","staticIPs":["staticIPs","staticIPs"],"targetProvisioningState":"targetProvisioningState","publisherName":"publisherName","createdAtUtc":"2000-01-23T04:56:07.000+00:00","portalUrl":"portalUrl","hostnameConfigurations":[{"hostname":"hostname","certificate":{"subject":"subject","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00"},"type":"Proxy"},{"hostname":"hostname","certificate":{"subject":"subject","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00"},"type":"Proxy"}],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"vpnType":"None","publisherEmail":"publisherEmail","managementApiUrl":"managementApiUrl","runtimeUrl":"runtimeUrl"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_delete(client):
    """Test case for api_management_services_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_get(client):
    """Test case for api_management_services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_get_sso_token(client):
    """Test case for api_management_services_get_sso_token

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/getssotoken'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_list(client):
    """Test case for api_management_services_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ApiManagement/service'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_list_by_resource_group(client):
    """Test case for api_management_services_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_manage_deployments(client):
    """Test case for api_management_services_manage_deployments

    
    """
    parameters = {"vpnConfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"location":"location","vpnType":"None","additionalLocations":[{"staticIPs":["staticIPs","staticIPs"],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"location":"location","skuType":"Developer","skuUnitCount":0},{"staticIPs":["staticIPs","staticIPs"],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"location":"location","skuType":"Developer","skuUnitCount":0}],"skuType":"Developer","skuUnitCount":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/managedeployments'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_restore(client):
    """Test case for api_management_services_restore

    
    """
    parameters = {"accessKey":"accessKey","containerName":"containerName","storageAccount":"storageAccount","backupName":"backupName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/restore'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_update(client):
    """Test case for api_management_services_update

    
    """
    parameters = {"sku":{"name":"Developer","capacity":6},"properties":{"additionalLocations":[{"staticIPs":["staticIPs","staticIPs"],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"location":"location","skuType":"Developer","skuUnitCount":0},{"staticIPs":["staticIPs","staticIPs"],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"location":"location","skuType":"Developer","skuUnitCount":0}],"provisioningState":"provisioningState","scmUrl":"scmUrl","customProperties":{"key":"customProperties"},"addresserEmail":"addresserEmail","staticIPs":["staticIPs","staticIPs"],"targetProvisioningState":"targetProvisioningState","publisherName":"publisherName","createdAtUtc":"2000-01-23T04:56:07.000+00:00","portalUrl":"portalUrl","hostnameConfigurations":[{"hostname":"hostname","certificate":{"subject":"subject","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00"},"type":"Proxy"},{"hostname":"hostname","certificate":{"subject":"subject","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00"},"type":"Proxy"}],"vpnconfiguration":{"subnetResourceId":"subnetResourceId","location":"location","vnetid":"vnetid","subnetname":"subnetname"},"vpnType":"None","publisherEmail":"publisherEmail","managementApiUrl":"managementApiUrl","runtimeUrl":"runtimeUrl"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_update_hostname(client):
    """Test case for api_management_services_update_hostname

    
    """
    parameters = {"update":[{"hostname":"hostname","certificate":{"subject":"subject","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00"},"type":"Proxy"},{"hostname":"hostname","certificate":{"subject":"subject","thumbprint":"thumbprint","expiry":"2000-01-23T04:56:07.000+00:00"},"type":"Proxy"}],"delete":["Proxy","Proxy"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/updatehostname'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_management_services_upload_certificate(client):
    """Test case for api_management_services_upload_certificate

    
    """
    parameters = {"certificate":"certificate","certificate_password":"certificate_password","type":"Proxy"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/uploadcertificate'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

