# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_machine_scale_set_vm import VirtualMachineScaleSetVM
from openapi_server.models.virtual_machine_scale_set_vm_instance_view import VirtualMachineScaleSetVMInstanceView
from openapi_server.models.virtual_machine_scale_set_vm_list_result import VirtualMachineScaleSetVMListResult
from openapi_server.models.virtual_machine_scale_set_vm_reimage_parameters import VirtualMachineScaleSetVMReimageParameters


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_deallocate(client):
    """Test case for virtual_machine_scale_set_vms_deallocate

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/deallocate'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_delete(client):
    """Test case for virtual_machine_scale_set_vms_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_get(client):
    """Test case for virtual_machine_scale_set_vms_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_get_instance_view(client):
    """Test case for virtual_machine_scale_set_vms_get_instance_view

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/instanceView'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_list(client):
    """Test case for virtual_machine_scale_set_vms_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_perform_maintenance(client):
    """Test case for virtual_machine_scale_set_vms_perform_maintenance

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/performMaintenance'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_power_off(client):
    """Test case for virtual_machine_scale_set_vms_power_off

    
    """
    params = [('skipShutdown', False),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/poweroff'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_redeploy(client):
    """Test case for virtual_machine_scale_set_vms_redeploy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/redeploy'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_reimage(client):
    """Test case for virtual_machine_scale_set_vms_reimage

    
    """
    vm_scale_set_vm_reimage_input = {"tempDisk":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/reimage'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_scale_set_vm_reimage_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_reimage_all(client):
    """Test case for virtual_machine_scale_set_vms_reimage_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/reimageall'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_restart(client):
    """Test case for virtual_machine_scale_set_vms_restart

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/restart'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_start(client):
    """Test case for virtual_machine_scale_set_vms_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/start'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_update(client):
    """Test case for virtual_machine_scale_set_vms_update

    
    """
    parameters = {"instanceId":"instanceId","resources":[{"properties":{"settings":"{}","instanceView":{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},"autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}},{"properties":{"settings":"{}","instanceView":{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},"autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}],"sku":{"tier":"tier","name":"name","capacity":1},"zones":["zones","zones"],"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher"},"properties":{"availabilitySet":{"id":"id"},"hardwareProfile":{"vmSize":"Basic_A0"},"vmId":"vmId","provisioningState":"provisioningState","latestModelApplied":True,"licenseType":"licenseType","instanceView":{"extensions":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"}],"disks":[{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"encryptionSettings":[{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}},{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}]},{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"encryptionSettings":[{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}},{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}]}],"vmHealth":{"status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},"placementGroupId":"placementGroupId","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"bootDiagnostics":{"consoleScreenshotBlobUri":"consoleScreenshotBlobUri","serialConsoleLogBlobUri":"serialConsoleLogBlobUri","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},"maintenanceRedeployStatus":{"isCustomerInitiatedMaintenanceAllowed":True,"maintenanceWindowEndTime":"2000-01-23T04:56:07.000+00:00","maintenanceWindowStartTime":"2000-01-23T04:56:07.000+00:00","lastOperationMessage":"lastOperationMessage","preMaintenanceWindowStartTime":"2000-01-23T04:56:07.000+00:00","preMaintenanceWindowEndTime":"2000-01-23T04:56:07.000+00:00","lastOperationResultCode":"None"},"platformUpdateDomain":6,"vmAgent":{"vmAgentVersion":"vmAgentVersion","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"extensionHandlers":[{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},{"type":"type","typeHandlerVersion":"typeHandlerVersion","status":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}}]},"platformFaultDomain":0,"rdpThumbPrint":"rdpThumbPrint"},"modelDefinitionApplied":"modelDefinitionApplied","storageProfile":{"dataDisks":[{"image":{"uri":"uri"},"diskMBpsReadWrite":5,"vhd":{"uri":"uri"},"lun":7,"toBeDetached":True,"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"diskIOPSReadWrite":5,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":2},{"image":{"uri":"uri"},"diskMBpsReadWrite":5,"vhd":{"uri":"uri"},"lun":7,"toBeDetached":True,"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"diskIOPSReadWrite":5,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":2}],"imageReference":{"offer":"offer","exactVersion":"exactVersion","publisher":"publisher","sku":"sku","version":"version"},"osDisk":{"image":{"uri":"uri"},"vhd":{"uri":"uri"},"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","osType":"Windows","diffDiskSettings":{"option":"Local"},"diskSizeGB":9,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}},"diagnosticsProfile":{"bootDiagnostics":{"storageUri":"storageUri","enabled":True}},"networkProfile":{"networkInterfaces":[{"properties":{"primary":True}},{"properties":{"primary":True}}]},"protectionPolicy":{"protectFromScaleIn":True,"protectFromScaleSetActions":True},"networkProfileConfiguration":{"networkInterfaceConfigurations":[{"name":"name","properties":{"ipConfigurations":[{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}},{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}}],"dnsSettings":{"dnsServers":["dnsServers","dnsServers"]},"enableAcceleratedNetworking":True,"enableIPForwarding":True,"networkSecurityGroup":{"id":"id"},"primary":True}},{"name":"name","properties":{"ipConfigurations":[{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}},{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}}],"dnsSettings":{"dnsServers":["dnsServers","dnsServers"]},"enableAcceleratedNetworking":True,"enableIPForwarding":True,"networkSecurityGroup":{"id":"id"},"primary":True}}]},"additionalCapabilities":{"ultraSSDEnabled":True},"osProfile":{"adminUsername":"adminUsername","allowExtensionOperations":True,"computerName":"computerName","linuxConfiguration":{"disablePasswordAuthentication":True,"provisionVMAgent":True,"ssh":{"publicKeys":[{"path":"path","keyData":"keyData"},{"path":"path","keyData":"keyData"}]}},"customData":"customData","requireGuestProvisionSignal":True,"windowsConfiguration":{"additionalUnattendContent":[{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"},{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"}],"provisionVMAgent":True,"timeZone":"timeZone","winRM":{"listeners":[{"protocol":"Http","certificateUrl":"certificateUrl"},{"protocol":"Http","certificateUrl":"certificateUrl"}]},"enableAutomaticUpdates":True},"secrets":[{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}},{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}}],"adminPassword":"adminPassword"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

