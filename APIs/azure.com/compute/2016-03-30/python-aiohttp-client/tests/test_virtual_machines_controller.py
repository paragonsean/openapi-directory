# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.virtual_machine import VirtualMachine
from openapi_server.models.virtual_machine_capture_parameters import VirtualMachineCaptureParameters
from openapi_server.models.virtual_machine_capture_result import VirtualMachineCaptureResult
from openapi_server.models.virtual_machine_list_result import VirtualMachineListResult
from openapi_server.models.virtual_machine_size_list_result import VirtualMachineSizeListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_capture(client):
    """Test case for virtual_machines_capture

    
    """
    parameters = {"overwriteVhds":True,"vhdPrefix":"vhdPrefix","destinationContainerName":"destinationContainerName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/capture'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_create_or_update(client):
    """Test case for virtual_machines_create_or_update

    
    """
    parameters = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"resources":[{"properties":{"settings":"{}","instanceView":{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},"autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}},{"properties":{"settings":"{}","instanceView":{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},"autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}],"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher"},"properties":{"availabilitySet":{"id":"id"},"licenseType":"licenseType","instanceView":{"extensions":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"}],"disks":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}]},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}]}],"statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"bootDiagnostics":{"consoleScreenshotBlobUri":"consoleScreenshotBlobUri","serialConsoleLogBlobUri":"serialConsoleLogBlobUri"},"platformUpdateDomain":6,"vmAgent":{"vmAgentVersion":"vmAgentVersion","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"extensionHandlers":[{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}}]},"platformFaultDomain":0,"rdpThumbPrint":"rdpThumbPrint"},"hardwareProfile":{"vmSize":"Basic_A0"},"vmId":"vmId","storageProfile":{"dataDisks":[{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"lun":5,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":1},{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"lun":5,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":1}],"imageReference":{"offer":"offer","publisher":"publisher","sku":"sku","version":"version"},"osDisk":{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"name":"name","osType":"Windows","diskSizeGB":5,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}},"diagnosticsProfile":{"bootDiagnostics":{"storageUri":"storageUri","enabled":True}},"networkProfile":{"networkInterfaces":[{"properties":{"primary":True}},{"properties":{"primary":True}}]},"provisioningState":"provisioningState","osProfile":{"adminUsername":"adminUsername","computerName":"computerName","linuxConfiguration":{"disablePasswordAuthentication":True,"ssh":{"publicKeys":[{"path":"path","keyData":"keyData"},{"path":"path","keyData":"keyData"}]}},"customData":"customData","windowsConfiguration":{"additionalUnattendContent":[{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"},{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"}],"provisionVMAgent":True,"timeZone":"timeZone","winRM":{"listeners":[{"protocol":"Http","certificateUrl":"certificateUrl"},{"protocol":"Http","certificateUrl":"certificateUrl"}]},"enableAutomaticUpdates":True},"secrets":[{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}},{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}}],"adminPassword":"adminPassword"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_deallocate(client):
    """Test case for virtual_machines_deallocate

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/deallocate'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_delete(client):
    """Test case for virtual_machines_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_generalize(client):
    """Test case for virtual_machines_generalize

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/generalize'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_get(client):
    """Test case for virtual_machines_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_list(client):
    """Test case for virtual_machines_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_list_all(client):
    """Test case for virtual_machines_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/virtualMachines'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_list_available_sizes(client):
    """Test case for virtual_machines_list_available_sizes

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/vmSizes'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_power_off(client):
    """Test case for virtual_machines_power_off

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/powerOff'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_redeploy(client):
    """Test case for virtual_machines_redeploy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/redeploy'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_restart(client):
    """Test case for virtual_machines_restart

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/restart'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_start(client):
    """Test case for virtual_machines_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/start'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

