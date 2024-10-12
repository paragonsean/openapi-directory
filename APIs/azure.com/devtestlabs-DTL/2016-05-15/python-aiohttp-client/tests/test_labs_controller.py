# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.export_resource_usage_parameters import ExportResourceUsageParameters
from openapi_server.models.generate_upload_uri_parameter import GenerateUploadUriParameter
from openapi_server.models.generate_upload_uri_response import GenerateUploadUriResponse
from openapi_server.models.lab import Lab
from openapi_server.models.lab_fragment import LabFragment
from openapi_server.models.lab_virtual_machine_creation_parameter import LabVirtualMachineCreationParameter
from openapi_server.models.response_with_continuation_lab import ResponseWithContinuationLab
from openapi_server.models.response_with_continuation_lab_vhd import ResponseWithContinuationLabVhd


pytestmark = pytest.mark.asyncio

async def test_labs_claim_any_vm(client):
    """Test case for labs_claim_any_vm

    
    """
    params = [('api-version', '2016-05-15')]
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
    lab_virtual_machine_creation_parameter = {"name":"name","location":"location","properties":{"labVirtualNetworkId":"labVirtualNetworkId","notes":"notes","createdByUser":"createdByUser","allowClaim":True,"labSubnetName":"labSubnetName","bulkCreationParameters":{"instanceCount":1},"disallowPublicIpAddress":True,"password":"password","environmentId":"environmentId","ownerObjectId":"ownerObjectId","osType":"osType","artifacts":[{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"},{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"}],"expirationDate":"2000-01-23T04:56:07.000+00:00","uniqueIdentifier":"uniqueIdentifier","createdByUserId":"createdByUserId","applicableSchedule":{"properties":{"labVmsStartup":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}},"labVmsShutdown":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}}}},"virtualMachineCreationSource":"FromCustomImage","fqdn":"fqdn","computeVm":{"networkInterfaceId":"networkInterfaceId","osType":"osType","dataDiskIds":["dataDiskIds","dataDiskIds"],"statuses":[{"code":"code","displayStatus":"displayStatus","message":"message"},{"code":"code","displayStatus":"displayStatus","message":"message"}],"dataDisks":[{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":5,"diskUri":"diskUri"},{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":5,"diskUri":"diskUri"}],"osDiskId":"osDiskId","vmSize":"vmSize"},"provisioningState":"provisioningState","userName":"userName","artifactDeploymentStatus":{"deploymentStatus":"deploymentStatus","artifactsApplied":0,"totalArtifacts":6},"createdDate":"2000-01-23T04:56:07.000+00:00","isAuthenticationWithSshKey":True,"size":"size","sshKey":"sshKey","networkInterface":{"subnetId":"subnetId","publicIpAddress":"publicIpAddress","dnsName":"dnsName","publicIpAddressId":"publicIpAddressId","virtualNetworkId":"virtualNetworkId","rdpAuthority":"rdpAuthority","privateIpAddress":"privateIpAddress","sshAuthority":"sshAuthority","sharedPublicIpAddressConfiguration":{"inboundNatRules":[{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2},{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2}]}},"galleryImageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"storageType":"storageType","customImageId":"customImageId","ownerUserPrincipalName":"ownerUserPrincipalName"},"tags":{"key":"tags"}}
    params = [('api-version', '2016-05-15')]
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
    lab = {"properties":{"artifactsStorageAccount":"artifactsStorageAccount","createdDate":"2000-01-23T04:56:07.000+00:00","defaultStorageAccount":"defaultStorageAccount","vaultName":"vaultName","premiumDataDisks":"Disabled","defaultPremiumStorageAccount":"defaultPremiumStorageAccount","labStorageType":"Standard","provisioningState":"provisioningState","premiumDataDiskStorageAccount":"premiumDataDiskStorageAccount","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
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
    params = [('api-version', '2016-05-15')]
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
    params = [('api-version', '2016-05-15')]
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
    params = [('api-version', '2016-05-15')]
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
                    ('api-version', '2016-05-15')]
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

async def test_labs_list_by_resource_group(client):
    """Test case for labs_list_by_resource_group

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2016-05-15')]
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
                    ('api-version', '2016-05-15')]
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
    params = [('api-version', '2016-05-15')]
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
    lab = {"properties":{"premiumDataDisks":"Disabled","labStorageType":"Standard","provisioningState":"provisioningState","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
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

