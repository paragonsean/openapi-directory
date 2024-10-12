# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.export_resource_usage_parameters import ExportResourceUsageParameters
from openapi_server.models.generate_upload_uri_parameter import GenerateUploadUriParameter
from openapi_server.models.generate_upload_uri_response import GenerateUploadUriResponse
from openapi_server.models.import_lab_virtual_machine_request import ImportLabVirtualMachineRequest
from openapi_server.models.lab import Lab
from openapi_server.models.lab_fragment import LabFragment
from openapi_server.models.lab_list import LabList
from openapi_server.models.lab_vhd_list import LabVhdList
from openapi_server.models.lab_virtual_machine_creation_parameter import LabVirtualMachineCreationParameter


pytestmark = pytest.mark.asyncio

async def test_labs_claim_any_vm(client):
    """Test case for labs_claim_any_vm

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/claimAnyVm'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_create_environment(client):
    """Test case for labs_create_environment

    
    """
    lab_virtual_machine_creation_parameter = {"name":"name","location":"location","properties":{"labVirtualNetworkId":"labVirtualNetworkId","notes":"notes","lastKnownPowerState":"lastKnownPowerState","createdByUser":"createdByUser","scheduleParameters":[{"name":"name","location":"location","properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"notificationLocale":"notificationLocale","emailRecipient":"emailRecipient","webhookUrl":"webhookUrl","status":"Enabled"},"status":"Enabled"},"tags":{"key":"tags"}},{"name":"name","location":"location","properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"notificationLocale":"notificationLocale","emailRecipient":"emailRecipient","webhookUrl":"webhookUrl","status":"Enabled"},"status":"Enabled"},"tags":{"key":"tags"}}],"allowClaim":True,"labSubnetName":"labSubnetName","bulkCreationParameters":{"instanceCount":1},"disallowPublicIpAddress":True,"password":"password","environmentId":"environmentId","computeId":"computeId","ownerObjectId":"ownerObjectId","osType":"osType","planId":"planId","artifacts":[{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactTitle":"artifactTitle","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"},{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactTitle":"artifactTitle","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"}],"expirationDate":"2000-01-23T04:56:07.000+00:00","createdByUserId":"createdByUserId","virtualMachineCreationSource":"FromCustomImage","fqdn":"fqdn","userName":"userName","artifactDeploymentStatus":{"deploymentStatus":"deploymentStatus","artifactsApplied":0,"totalArtifacts":6},"createdDate":"2000-01-23T04:56:07.000+00:00","isAuthenticationWithSshKey":True,"size":"size","sshKey":"sshKey","networkInterface":{"subnetId":"subnetId","publicIpAddress":"publicIpAddress","dnsName":"dnsName","publicIpAddressId":"publicIpAddressId","virtualNetworkId":"virtualNetworkId","rdpAuthority":"rdpAuthority","privateIpAddress":"privateIpAddress","sshAuthority":"sshAuthority","sharedPublicIpAddressConfiguration":{"inboundNatRules":[{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2},{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2}]}},"galleryImageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"storageType":"storageType","dataDiskParameters":[{"existingLabDiskId":"existingLabDiskId","hostCaching":"None","attachNewDataDiskOptions":{"diskName":"diskName","diskSizeGiB":5,"diskType":"Standard"}},{"existingLabDiskId":"existingLabDiskId","hostCaching":"None","attachNewDataDiskOptions":{"diskName":"diskName","diskSizeGiB":5,"diskType":"Standard"}}],"customImageId":"customImageId","ownerUserPrincipalName":"ownerUserPrincipalName"},"tags":{"key":"tags"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/createEnvironment'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=lab_virtual_machine_creation_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_create_or_update(client):
    """Test case for labs_create_or_update

    
    """
    lab = {"properties":{"loadBalancerId":"loadBalancerId","artifactsStorageAccount":"artifactsStorageAccount","labStorageType":"Standard","vmCreationResourceGroup":"vmCreationResourceGroup","provisioningState":"provisioningState","premiumDataDiskStorageAccount":"premiumDataDiskStorageAccount","extendedProperties":{"key":"extendedProperties"},"createdDate":"2000-01-23T04:56:07.000+00:00","defaultStorageAccount":"defaultStorageAccount","publicIpId":"publicIpId","vaultName":"vaultName","premiumDataDisks":"Disabled","defaultPremiumStorageAccount":"defaultPremiumStorageAccount","environmentPermission":"Reader","mandatoryArtifactsResourceIdsWindows":["mandatoryArtifactsResourceIdsWindows","mandatoryArtifactsResourceIdsWindows"],"mandatoryArtifactsResourceIdsLinux":["mandatoryArtifactsResourceIdsLinux","mandatoryArtifactsResourceIdsLinux"],"support":{"markdown":"markdown","enabled":"Enabled"},"networkSecurityGroupId":"networkSecurityGroupId","announcement":{"expired":True,"markdown":"markdown","provisioningState":"provisioningState","title":"title","enabled":"Enabled","expirationDate":"2000-01-23T04:56:07.000+00:00","uniqueIdentifier":"uniqueIdentifier"},"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=lab,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_delete(client):
    """Test case for labs_delete

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_export_resource_usage(client):
    """Test case for labs_export_resource_usage

    
    """
    export_resource_usage_parameters = {"blobStorageAbsoluteSasUri":"blobStorageAbsoluteSasUri","usageStartDate":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/exportResourceUsage'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=export_resource_usage_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_generate_upload_uri(client):
    """Test case for labs_generate_upload_uri

    
    """
    generate_upload_uri_parameter = {"blobName":"blobName"}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/generateUploadUri'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=generate_upload_uri_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_get(client):
    """Test case for labs_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_import_virtual_machine(client):
    """Test case for labs_import_virtual_machine

    
    """
    import_lab_virtual_machine_request = {"sourceVirtualMachineResourceId":"sourceVirtualMachineResourceId","destinationVirtualMachineName":"destinationVirtualMachineName"}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/importVirtualMachine'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=import_lab_virtual_machine_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_list_by_resource_group(client):
    """Test case for labs_list_by_resource_group

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_list_by_subscription(client):
    """Test case for labs_list_by_subscription

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DevTestLab/labs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_list_vhds(client):
    """Test case for labs_list_vhds

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}/listVhds'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_update(client):
    """Test case for labs_update

    
    """
    lab = {"properties":{"extendedProperties":{"key":"extendedProperties"},"premiumDataDisks":"Disabled","labStorageType":"Standard","environmentPermission":"Reader","mandatoryArtifactsResourceIdsWindows":["mandatoryArtifactsResourceIdsWindows","mandatoryArtifactsResourceIdsWindows"],"mandatoryArtifactsResourceIdsLinux":["mandatoryArtifactsResourceIdsLinux","mandatoryArtifactsResourceIdsLinux"],"support":{"markdown":"markdown","enabled":"Enabled"},"announcement":{"expired":True,"markdown":"markdown","title":"title","enabled":"Enabled","expirationDate":"2000-01-23T04:56:07.000+00:00"}}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=lab,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

