# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.applicable_schedule import ApplicableSchedule
from openapi_server.models.apply_artifacts_request import ApplyArtifactsRequest
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.data_disk_properties import DataDiskProperties
from openapi_server.models.detach_data_disk_properties import DetachDataDiskProperties
from openapi_server.models.lab_virtual_machine import LabVirtualMachine
from openapi_server.models.lab_virtual_machine_fragment import LabVirtualMachineFragment
from openapi_server.models.response_with_continuation_lab_virtual_machine import ResponseWithContinuationLabVirtualMachine


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_add_data_disk(client):
    """Test case for virtual_machines_add_data_disk

    
    """
    data_disk_properties = {"existingLabDiskId":"existingLabDiskId","hostCaching":"None","attachNewDataDiskOptions":{"diskName":"diskName","diskSizeGiB":0,"diskType":"Standard"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}/addDataDisk'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=data_disk_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_apply_artifacts(client):
    """Test case for virtual_machines_apply_artifacts

    
    """
    apply_artifacts_request = {"artifacts":[{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"},{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"}]}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}/applyArtifacts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=apply_artifacts_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_claim(client):
    """Test case for virtual_machines_claim

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}/claim'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_create_or_update(client):
    """Test case for virtual_machines_create_or_update

    
    """
    lab_virtual_machine = {"properties":{"labVirtualNetworkId":"labVirtualNetworkId","notes":"notes","createdByUser":"createdByUser","allowClaim":True,"labSubnetName":"labSubnetName","disallowPublicIpAddress":True,"password":"password","environmentId":"environmentId","computeId":"computeId","ownerObjectId":"ownerObjectId","osType":"osType","artifacts":[{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"},{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"}],"expirationDate":"2000-01-23T04:56:07.000+00:00","uniqueIdentifier":"uniqueIdentifier","createdByUserId":"createdByUserId","applicableSchedule":{"properties":{"labVmsStartup":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}},"labVmsShutdown":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}}}},"virtualMachineCreationSource":"FromCustomImage","fqdn":"fqdn","computeVm":{"networkInterfaceId":"networkInterfaceId","osType":"osType","dataDiskIds":["dataDiskIds","dataDiskIds"],"statuses":[{"code":"code","displayStatus":"displayStatus","message":"message"},{"code":"code","displayStatus":"displayStatus","message":"message"}],"dataDisks":[{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":5,"diskUri":"diskUri"},{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":5,"diskUri":"diskUri"}],"osDiskId":"osDiskId","vmSize":"vmSize"},"provisioningState":"provisioningState","userName":"userName","artifactDeploymentStatus":{"deploymentStatus":"deploymentStatus","artifactsApplied":0,"totalArtifacts":6},"createdDate":"2000-01-23T04:56:07.000+00:00","isAuthenticationWithSshKey":True,"size":"size","sshKey":"sshKey","networkInterface":{"subnetId":"subnetId","publicIpAddress":"publicIpAddress","dnsName":"dnsName","publicIpAddressId":"publicIpAddressId","virtualNetworkId":"virtualNetworkId","rdpAuthority":"rdpAuthority","privateIpAddress":"privateIpAddress","sshAuthority":"sshAuthority","sharedPublicIpAddressConfiguration":{"inboundNatRules":[{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2},{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2}]}},"galleryImageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"storageType":"storageType","customImageId":"customImageId","ownerUserPrincipalName":"ownerUserPrincipalName"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=lab_virtual_machine,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_delete(client):
    """Test case for virtual_machines_delete

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_detach_data_disk(client):
    """Test case for virtual_machines_detach_data_disk

    
    """
    detach_data_disk_properties = {"existingLabDiskId":"existingLabDiskId"}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}/detachDataDisk'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=detach_data_disk_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_get(client):
    """Test case for virtual_machines_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_list(client):
    """Test case for virtual_machines_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_list_applicable_schedules(client):
    """Test case for virtual_machines_list_applicable_schedules

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}/listApplicableSchedules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_start(client):
    """Test case for virtual_machines_start

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_stop(client):
    """Test case for virtual_machines_stop

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_update(client):
    """Test case for virtual_machines_update

    
    """
    lab_virtual_machine = {"properties":{"labVirtualNetworkId":"labVirtualNetworkId","notes":"notes","createdByUser":"createdByUser","allowClaim":True,"labSubnetName":"labSubnetName","disallowPublicIpAddress":True,"password":"password","environmentId":"environmentId","ownerObjectId":"ownerObjectId","osType":"osType","artifacts":[{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"},{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"}],"expirationDate":"2000-01-23T04:56:07.000+00:00","uniqueIdentifier":"uniqueIdentifier","createdByUserId":"createdByUserId","applicableSchedule":{"properties":{"labVmsStartup":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}},"labVmsShutdown":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}}}},"virtualMachineCreationSource":"FromCustomImage","fqdn":"fqdn","computeVm":{"networkInterfaceId":"networkInterfaceId","osType":"osType","dataDiskIds":["dataDiskIds","dataDiskIds"],"statuses":[{"code":"code","displayStatus":"displayStatus","message":"message"},{"code":"code","displayStatus":"displayStatus","message":"message"}],"dataDisks":[{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":1,"diskUri":"diskUri"},{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":1,"diskUri":"diskUri"}],"osDiskId":"osDiskId","vmSize":"vmSize"},"provisioningState":"provisioningState","userName":"userName","artifactDeploymentStatus":{"deploymentStatus":"deploymentStatus","artifactsApplied":0,"totalArtifacts":6},"createdDate":"2000-01-23T04:56:07.000+00:00","isAuthenticationWithSshKey":True,"size":"size","sshKey":"sshKey","networkInterface":{"subnetId":"subnetId","publicIpAddress":"publicIpAddress","dnsName":"dnsName","publicIpAddressId":"publicIpAddressId","virtualNetworkId":"virtualNetworkId","rdpAuthority":"rdpAuthority","privateIpAddress":"privateIpAddress","sshAuthority":"sshAuthority","sharedPublicIpAddressConfiguration":{"inboundNatRules":[{"backendPort":5,"transportProtocol":"Tcp","frontendPort":5},{"backendPort":5,"transportProtocol":"Tcp","frontendPort":5}]}},"galleryImageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"storageType":"storageType","customImageId":"customImageId","ownerUserPrincipalName":"ownerUserPrincipalName"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/virtualmachines/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=lab_virtual_machine,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

