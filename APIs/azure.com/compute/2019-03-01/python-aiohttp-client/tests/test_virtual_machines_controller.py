# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_machine import VirtualMachine
from openapi_server.models.virtual_machine_capture_parameters import VirtualMachineCaptureParameters
from openapi_server.models.virtual_machine_capture_result import VirtualMachineCaptureResult
from openapi_server.models.virtual_machine_instance_view import VirtualMachineInstanceView
from openapi_server.models.virtual_machine_list_result import VirtualMachineListResult
from openapi_server.models.virtual_machine_reimage_parameters import VirtualMachineReimageParameters
from openapi_server.models.virtual_machine_size_list_result import VirtualMachineSizeListResult
from openapi_server.models.virtual_machine_update import VirtualMachineUpdate


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

async def test_virtual_machines_convert_to_managed_disks(client):
    """Test case for virtual_machines_convert_to_managed_disks

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/convertToManagedDisks'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_create_or_update(client):
    """Test case for virtual_machines_create_or_update

    
    """
    parameters = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"resources":[{"properties":{"settings":"{}","instanceView":{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},"autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}},{"properties":{"settings":"{}","instanceView":{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},"autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}],"zones":["zones","zones"],"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher"},"properties":{"availabilitySet":{"id":"id"},"hardwareProfile":{"vmSize":"Basic_A0"},"vmId":"vmId","proximityPlacementGroup":{"id":"id"},"provisioningState":"provisioningState","priority":"Regular","licenseType":"licenseType","virtualMachineScaleSet":{"id":"id"},"instanceView":{"disks":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"encryptionSettings":[{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}},{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}]},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"encryptionSettings":[{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}},{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}]}],"hyperVGeneration":"V1","maintenanceRedeployStatus":{"isCustomerInitiatedMaintenanceAllowed":True,"maintenanceWindowEndTime":"2000-01-23T04:56:07.000+00:00","maintenanceWindowStartTime":"2000-01-23T04:56:07.000+00:00","lastOperationMessage":"lastOperationMessage","preMaintenanceWindowStartTime":"2000-01-23T04:56:07.000+00:00","preMaintenanceWindowEndTime":"2000-01-23T04:56:07.000+00:00","lastOperationResultCode":"None"},"osName":"osName","vmAgent":{"vmAgentVersion":"vmAgentVersion","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"extensionHandlers":[{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}}]},"rdpThumbPrint":"rdpThumbPrint","extensions":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"}],"osVersion":"osVersion","computerName":"computerName","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"bootDiagnostics":{"consoleScreenshotBlobUri":"consoleScreenshotBlobUri","serialConsoleLogBlobUri":"serialConsoleLogBlobUri","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},"platformUpdateDomain":1,"platformFaultDomain":6},"billingProfile":{"maxPrice":0.8008281904610115},"storageProfile":{"dataDisks":[{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"lun":5,"toBeDetached":True,"managedDisk":{"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":5},{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"lun":5,"toBeDetached":True,"managedDisk":{"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":5}],"imageReference":{"offer":"offer","publisher":"publisher","sku":"sku","version":"version"},"osDisk":{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"managedDisk":{"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","osType":"Windows","diffDiskSettings":{"option":"Local"},"diskSizeGB":2,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}},"host":{"id":"id"},"diagnosticsProfile":{"bootDiagnostics":{"storageUri":"storageUri","enabled":True}},"networkProfile":{"networkInterfaces":[{"properties":{"primary":True}},{"properties":{"primary":True}}]},"additionalCapabilities":{"ultraSSDEnabled":True},"evictionPolicy":"Deallocate","osProfile":{"adminUsername":"adminUsername","allowExtensionOperations":True,"computerName":"computerName","linuxConfiguration":{"disablePasswordAuthentication":True,"provisionVMAgent":True,"ssh":{"publicKeys":[{"path":"path","keyData":"keyData"},{"path":"path","keyData":"keyData"}]}},"customData":"customData","windowsConfiguration":{"additionalUnattendContent":[{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"},{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"}],"provisionVMAgent":True,"timeZone":"timeZone","winRM":{"listeners":[{"protocol":"Http","certificateUrl":"certificateUrl"},{"protocol":"Http","certificateUrl":"certificateUrl"}]},"enableAutomaticUpdates":True},"secrets":[{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}},{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}}],"adminPassword":"adminPassword"}}}
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

async def test_virtual_machines_instance_view(client):
    """Test case for virtual_machines_instance_view

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/instanceView'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
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

async def test_virtual_machines_list_by_location(client):
    """Test case for virtual_machines_list_by_location

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/virtualMachines'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_perform_maintenance(client):
    """Test case for virtual_machines_perform_maintenance

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/performMaintenance'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_power_off(client):
    """Test case for virtual_machines_power_off

    
    """
    params = [('skipShutdown', False),
                    ('api-version', 'api_version_example')]
    headers = { 
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

async def test_virtual_machines_reimage(client):
    """Test case for virtual_machines_reimage

    
    """
    parameters = {"tempDisk":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/reimage'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_restart(client):
    """Test case for virtual_machines_restart

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
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
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/start'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_update(client):
    """Test case for virtual_machines_update

    
    """
    parameters = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"zones":["zones","zones"],"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher"},"properties":{"availabilitySet":{"id":"id"},"hardwareProfile":{"vmSize":"Basic_A0"},"vmId":"vmId","proximityPlacementGroup":{"id":"id"},"provisioningState":"provisioningState","priority":"Regular","licenseType":"licenseType","virtualMachineScaleSet":{"id":"id"},"instanceView":{"disks":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"encryptionSettings":[{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}},{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}]},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"encryptionSettings":[{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}},{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}]}],"hyperVGeneration":"V1","maintenanceRedeployStatus":{"isCustomerInitiatedMaintenanceAllowed":True,"maintenanceWindowEndTime":"2000-01-23T04:56:07.000+00:00","maintenanceWindowStartTime":"2000-01-23T04:56:07.000+00:00","lastOperationMessage":"lastOperationMessage","preMaintenanceWindowStartTime":"2000-01-23T04:56:07.000+00:00","preMaintenanceWindowEndTime":"2000-01-23T04:56:07.000+00:00","lastOperationResultCode":"None"},"osName":"osName","vmAgent":{"vmAgentVersion":"vmAgentVersion","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"extensionHandlers":[{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}}]},"rdpThumbPrint":"rdpThumbPrint","extensions":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"}],"osVersion":"osVersion","computerName":"computerName","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"bootDiagnostics":{"consoleScreenshotBlobUri":"consoleScreenshotBlobUri","serialConsoleLogBlobUri":"serialConsoleLogBlobUri","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},"platformUpdateDomain":1,"platformFaultDomain":6},"billingProfile":{"maxPrice":0.8008281904610115},"storageProfile":{"dataDisks":[{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"lun":5,"toBeDetached":True,"managedDisk":{"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":5},{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"lun":5,"toBeDetached":True,"managedDisk":{"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":5}],"imageReference":{"offer":"offer","publisher":"publisher","sku":"sku","version":"version"},"osDisk":{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"managedDisk":{"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","osType":"Windows","diffDiskSettings":{"option":"Local"},"diskSizeGB":2,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}},"host":{"id":"id"},"diagnosticsProfile":{"bootDiagnostics":{"storageUri":"storageUri","enabled":True}},"networkProfile":{"networkInterfaces":[{"properties":{"primary":True}},{"properties":{"primary":True}}]},"additionalCapabilities":{"ultraSSDEnabled":True},"evictionPolicy":"Deallocate","osProfile":{"adminUsername":"adminUsername","allowExtensionOperations":True,"computerName":"computerName","linuxConfiguration":{"disablePasswordAuthentication":True,"provisionVMAgent":True,"ssh":{"publicKeys":[{"path":"path","keyData":"keyData"},{"path":"path","keyData":"keyData"}]}},"customData":"customData","windowsConfiguration":{"additionalUnattendContent":[{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"},{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"}],"provisionVMAgent":True,"timeZone":"timeZone","winRM":{"listeners":[{"protocol":"Http","certificateUrl":"certificateUrl"},{"protocol":"Http","certificateUrl":"certificateUrl"}]},"enableAutomaticUpdates":True},"secrets":[{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}},{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}}],"adminPassword":"adminPassword"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

