# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.formula import Formula
from openapi_server.models.response_with_continuation_formula import ResponseWithContinuationFormula


pytestmark = pytest.mark.asyncio

async def test_formulas_create_or_update(client):
    """Test case for formulas_create_or_update

    
    """
    formula = {"properties":{"author":"author","vm":{"labVmId":"labVmId"},"formulaContent":{"name":"name","location":"location","properties":{"labVirtualNetworkId":"labVirtualNetworkId","notes":"notes","createdByUser":"createdByUser","allowClaim":True,"labSubnetName":"labSubnetName","bulkCreationParameters":{"instanceCount":1},"disallowPublicIpAddress":True,"password":"password","environmentId":"environmentId","ownerObjectId":"ownerObjectId","osType":"osType","artifacts":[{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"},{"vmExtensionStatusMessage":"vmExtensionStatusMessage","artifactId":"artifactId","deploymentStatusMessage":"deploymentStatusMessage","installTime":"2000-01-23T04:56:07.000+00:00","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"status":"status"}],"expirationDate":"2000-01-23T04:56:07.000+00:00","uniqueIdentifier":"uniqueIdentifier","createdByUserId":"createdByUserId","applicableSchedule":{"properties":{"labVmsStartup":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}},"labVmsShutdown":{"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"webhookUrl":"webhookUrl","status":"Disabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}}}},"virtualMachineCreationSource":"FromCustomImage","fqdn":"fqdn","computeVm":{"networkInterfaceId":"networkInterfaceId","osType":"osType","dataDiskIds":["dataDiskIds","dataDiskIds"],"statuses":[{"code":"code","displayStatus":"displayStatus","message":"message"},{"code":"code","displayStatus":"displayStatus","message":"message"}],"dataDisks":[{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":5,"diskUri":"diskUri"},{"managedDiskId":"managedDiskId","name":"name","diskSizeGiB":5,"diskUri":"diskUri"}],"osDiskId":"osDiskId","vmSize":"vmSize"},"provisioningState":"provisioningState","userName":"userName","artifactDeploymentStatus":{"deploymentStatus":"deploymentStatus","artifactsApplied":0,"totalArtifacts":6},"createdDate":"2000-01-23T04:56:07.000+00:00","isAuthenticationWithSshKey":True,"size":"size","sshKey":"sshKey","networkInterface":{"subnetId":"subnetId","publicIpAddress":"publicIpAddress","dnsName":"dnsName","publicIpAddressId":"publicIpAddressId","virtualNetworkId":"virtualNetworkId","rdpAuthority":"rdpAuthority","privateIpAddress":"privateIpAddress","sshAuthority":"sshAuthority","sharedPublicIpAddressConfiguration":{"inboundNatRules":[{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2},{"backendPort":5,"transportProtocol":"Tcp","frontendPort":2}]}},"galleryImageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"storageType":"storageType","customImageId":"customImageId","ownerUserPrincipalName":"ownerUserPrincipalName"},"tags":{"key":"tags"}},"osType":"osType","description":"description","provisioningState":"provisioningState","creationDate":"2000-01-23T04:56:07.000+00:00","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=formula,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formulas_delete(client):
    """Test case for formulas_delete

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formulas_get(client):
    """Test case for formulas_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formulas_list(client):
    """Test case for formulas_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

