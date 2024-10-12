# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recovery_walk_response import RecoveryWalkResponse
from openapi_server.models.vm_scale_set_convert_to_single_placement_group_input import VMScaleSetConvertToSinglePlacementGroupInput
from openapi_server.models.virtual_machine_scale_set import VirtualMachineScaleSet
from openapi_server.models.virtual_machine_scale_set_instance_view import VirtualMachineScaleSetInstanceView
from openapi_server.models.virtual_machine_scale_set_list_os_upgrade_history import VirtualMachineScaleSetListOSUpgradeHistory
from openapi_server.models.virtual_machine_scale_set_list_result import VirtualMachineScaleSetListResult
from openapi_server.models.virtual_machine_scale_set_list_skus_result import VirtualMachineScaleSetListSkusResult
from openapi_server.models.virtual_machine_scale_set_list_with_link_result import VirtualMachineScaleSetListWithLinkResult
from openapi_server.models.virtual_machine_scale_set_reimage_parameters import VirtualMachineScaleSetReimageParameters
from openapi_server.models.virtual_machine_scale_set_update import VirtualMachineScaleSetUpdate
from openapi_server.models.virtual_machine_scale_set_vm_instance_ids import VirtualMachineScaleSetVMInstanceIDs
from openapi_server.models.virtual_machine_scale_set_vm_instance_required_ids import VirtualMachineScaleSetVMInstanceRequiredIDs


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_convert_to_single_placement_group(client):
    """Test case for virtual_machine_scale_sets_convert_to_single_placement_group

    
    """
    parameters = {"activePlacementGroupId":"activePlacementGroupId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/convertToSinglePlacementGroup'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_create_or_update(client):
    """Test case for virtual_machine_scale_sets_create_or_update

    
    """
    parameters = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"sku":{"tier":"tier","name":"name","capacity":1},"zones":["zones","zones"],"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher"},"properties":{"zoneBalance":True,"overprovision":True,"platformFaultDomainCount":0,"scaleInPolicy":{"rules":["Default","Default"]},"proximityPlacementGroup":{"id":"id"},"automaticRepairsPolicy":{"gracePeriod":"gracePeriod","enabled":True},"provisioningState":"provisioningState","doNotRunExtensionsOnOverprovisionedVMs":True,"upgradePolicy":{"automaticOSUpgradePolicy":{"disableAutomaticRollback":True,"enableAutomaticOSUpgrade":True},"mode":"Automatic","rollingUpgradePolicy":{"maxUnhealthyInstancePercent":18,"pauseTimeBetweenBatches":"pauseTimeBetweenBatches","maxBatchInstancePercent":62,"maxUnhealthyUpgradedInstancePercent":59}},"singlePlacementGroup":True,"virtualMachineProfile":{"licenseType":"licenseType","extensionProfile":{"extensions":[{"name":"name","type":"type","properties":{"settings":"{}","autoUpgradeMinorVersion":True,"publisher":"publisher","provisionAfterExtensions":["provisionAfterExtensions","provisionAfterExtensions"],"provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}},{"name":"name","type":"type","properties":{"settings":"{}","autoUpgradeMinorVersion":True,"publisher":"publisher","provisionAfterExtensions":["provisionAfterExtensions","provisionAfterExtensions"],"provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}]},"billingProfile":{"maxPrice":0.8008281904610115},"storageProfile":{"dataDisks":[{"diskMBpsReadWrite":7,"lun":3,"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"diskIOPSReadWrite":2,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":9},{"diskMBpsReadWrite":7,"lun":3,"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"diskIOPSReadWrite":2,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":9}],"imageReference":{"offer":"offer","exactVersion":"exactVersion","publisher":"publisher","sku":"sku","version":"version"},"osDisk":{"image":{"uri":"uri"},"vhdContainers":["vhdContainers","vhdContainers"],"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"name":"name","osType":"Windows","diffDiskSettings":{"option":"Local"},"diskSizeGB":2}},"diagnosticsProfile":{"bootDiagnostics":{"storageUri":"storageUri","enabled":True}},"networkProfile":{"healthProbe":{"id":"id"},"networkInterfaceConfigurations":[{"name":"name","properties":{"ipConfigurations":[{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}},{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}}],"dnsSettings":{"dnsServers":["dnsServers","dnsServers"]},"enableAcceleratedNetworking":True,"enableIPForwarding":True,"networkSecurityGroup":{"id":"id"},"primary":True}},{"name":"name","properties":{"ipConfigurations":[{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}},{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":5,"publicIPPrefix":{"id":"id"},"ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}}],"dnsSettings":{"dnsServers":["dnsServers","dnsServers"]},"enableAcceleratedNetworking":True,"enableIPForwarding":True,"networkSecurityGroup":{"id":"id"},"primary":True}}]},"scheduledEventsProfile":{"terminateNotificationProfile":{"notBeforeTimeout":"notBeforeTimeout","enable":True}},"priority":"Regular","evictionPolicy":"Deallocate","osProfile":{"adminUsername":"adminUsername","linuxConfiguration":{"disablePasswordAuthentication":True,"provisionVMAgent":True,"ssh":{"publicKeys":[{"path":"path","keyData":"keyData"},{"path":"path","keyData":"keyData"}]}},"customData":"customData","computerNamePrefix":"computerNamePrefix","windowsConfiguration":{"additionalUnattendContent":[{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"},{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"}],"provisionVMAgent":True,"timeZone":"timeZone","winRM":{"listeners":[{"protocol":"Http","certificateUrl":"certificateUrl"},{"protocol":"Http","certificateUrl":"certificateUrl"}]},"enableAutomaticUpdates":True},"secrets":[{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}},{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}}],"adminPassword":"adminPassword"}},"additionalCapabilities":{"ultraSSDEnabled":True},"uniqueId":"uniqueId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_deallocate(client):
    """Test case for virtual_machine_scale_sets_deallocate

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/deallocate'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_delete(client):
    """Test case for virtual_machine_scale_sets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_delete_instances(client):
    """Test case for virtual_machine_scale_sets_delete_instances

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/delete'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_force_recovery_service_fabric_platform_update_domain_walk(client):
    """Test case for virtual_machine_scale_sets_force_recovery_service_fabric_platform_update_domain_walk

    
    """
    params = [('api-version', 'api_version_example'),
                    ('platformUpdateDomain', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/forceRecoveryServiceFabricPlatformUpdateDomainWalk'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_get(client):
    """Test case for virtual_machine_scale_sets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_get_instance_view(client):
    """Test case for virtual_machine_scale_sets_get_instance_view

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/instanceView'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_get_os_upgrade_history(client):
    """Test case for virtual_machine_scale_sets_get_os_upgrade_history

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/osUpgradeHistory'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_list(client):
    """Test case for virtual_machine_scale_sets_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_list_all(client):
    """Test case for virtual_machine_scale_sets_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/virtualMachineScaleSets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_list_skus(client):
    """Test case for virtual_machine_scale_sets_list_skus

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/skus'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_perform_maintenance(client):
    """Test case for virtual_machine_scale_sets_perform_maintenance

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/performMaintenance'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_power_off(client):
    """Test case for virtual_machine_scale_sets_power_off

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('skipShutdown', False),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/poweroff'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_redeploy(client):
    """Test case for virtual_machine_scale_sets_redeploy

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/redeploy'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_reimage(client):
    """Test case for virtual_machine_scale_sets_reimage

    
    """
    vm_scale_set_reimage_input = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/reimage'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_scale_set_reimage_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_reimage_all(client):
    """Test case for virtual_machine_scale_sets_reimage_all

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/reimageall'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_restart(client):
    """Test case for virtual_machine_scale_sets_restart

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/restart'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_start(client):
    """Test case for virtual_machine_scale_sets_start

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/start'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_update(client):
    """Test case for virtual_machine_scale_sets_update

    
    """
    parameters = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"sku":{"tier":"tier","name":"name","capacity":1},"plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher"},"properties":{"upgradePolicy":{"automaticOSUpgradePolicy":{"disableAutomaticRollback":True,"enableAutomaticOSUpgrade":True},"mode":"Automatic","rollingUpgradePolicy":{"maxUnhealthyInstancePercent":18,"pauseTimeBetweenBatches":"pauseTimeBetweenBatches","maxBatchInstancePercent":62,"maxUnhealthyUpgradedInstancePercent":59}},"overprovision":True,"scaleInPolicy":{"rules":["Default","Default"]},"proximityPlacementGroup":{"id":"id"},"automaticRepairsPolicy":{"gracePeriod":"gracePeriod","enabled":True},"singlePlacementGroup":True,"virtualMachineProfile":{"licenseType":"licenseType","extensionProfile":{"extensions":[{"name":"name","type":"type","properties":{"settings":"{}","autoUpgradeMinorVersion":True,"publisher":"publisher","provisionAfterExtensions":["provisionAfterExtensions","provisionAfterExtensions"],"provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}},{"name":"name","type":"type","properties":{"settings":"{}","autoUpgradeMinorVersion":True,"publisher":"publisher","provisionAfterExtensions":["provisionAfterExtensions","provisionAfterExtensions"],"provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}]},"billingProfile":{"maxPrice":0.8008281904610115},"storageProfile":{"dataDisks":[{"diskMBpsReadWrite":7,"lun":3,"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"diskIOPSReadWrite":2,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":9},{"diskMBpsReadWrite":7,"lun":3,"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"diskIOPSReadWrite":2,"name":"name","caching":"None","createOption":"FromImage","diskSizeGB":9}],"imageReference":{"offer":"offer","exactVersion":"exactVersion","publisher":"publisher","sku":"sku","version":"version"},"osDisk":{"image":{"uri":"uri"},"vhdContainers":["vhdContainers","vhdContainers"],"managedDisk":{"diskEncryptionSet":{"id":"id"},"storageAccountType":"Standard_LRS"},"writeAcceleratorEnabled":True,"caching":"None","diskSizeGB":6}},"diagnosticsProfile":{"bootDiagnostics":{"storageUri":"storageUri","enabled":True}},"networkProfile":{"healthProbe":{"id":"id"},"networkInterfaceConfigurations":[{"name":"name","properties":{"ipConfigurations":[{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":0}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}},{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":0}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}}],"dnsSettings":{"dnsServers":["dnsServers","dnsServers"]},"enableAcceleratedNetworking":True,"enableIPForwarding":True,"networkSecurityGroup":{"id":"id"},"primary":True}},{"name":"name","properties":{"ipConfigurations":[{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":0}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}},{"name":"name","properties":{"applicationGatewayBackendAddressPools":[{"id":"id"},{"id":"id"}],"loadBalancerInboundNatPools":[{"id":"id"},{"id":"id"}],"subnet":{"id":"id"},"publicIPAddressConfiguration":{"name":"name","properties":{"dnsSettings":{"domainNameLabel":"domainNameLabel"},"idleTimeoutInMinutes":0}},"applicationSecurityGroups":[{"id":"id"},{"id":"id"}],"privateIPAddressVersion":"IPv4","loadBalancerBackendAddressPools":[{"id":"id"},{"id":"id"}],"primary":True}}],"dnsSettings":{"dnsServers":["dnsServers","dnsServers"]},"enableAcceleratedNetworking":True,"enableIPForwarding":True,"networkSecurityGroup":{"id":"id"},"primary":True}}]},"scheduledEventsProfile":{"terminateNotificationProfile":{"notBeforeTimeout":"notBeforeTimeout","enable":True}},"osProfile":{"linuxConfiguration":{"disablePasswordAuthentication":True,"provisionVMAgent":True,"ssh":{"publicKeys":[{"path":"path","keyData":"keyData"},{"path":"path","keyData":"keyData"}]}},"customData":"customData","windowsConfiguration":{"additionalUnattendContent":[{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"},{"passName":"OobeSystem","componentName":"Microsoft-Windows-Shell-Setup","content":"content","settingName":"AutoLogon"}],"provisionVMAgent":True,"timeZone":"timeZone","winRM":{"listeners":[{"protocol":"Http","certificateUrl":"certificateUrl"},{"protocol":"Http","certificateUrl":"certificateUrl"}]},"enableAutomaticUpdates":True},"secrets":[{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}},{"vaultCertificates":[{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"},{"certificateUrl":"certificateUrl","certificateStore":"certificateStore"}],"sourceVault":{"id":"id"}}]}},"additionalCapabilities":{"ultraSSDEnabled":True},"doNotRunExtensionsOnOverprovisionedVMs":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_sets_update_instances(client):
    """Test case for virtual_machine_scale_sets_update_instances

    
    """
    vm_instance_ids = {"instanceIds":["instanceIds","instanceIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/manualupgrade'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vm_instance_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

