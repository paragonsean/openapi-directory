# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.patch_payload import PatchPayload
from openapi_server.models.virtual_machine import VirtualMachine
from openapi_server.models.virtual_machine_list_response import VirtualMachineListResponse
from openapi_server.models.virtual_machine_stop_mode import VirtualMachineStopMode


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_create_or_update(client):
    """Test case for virtual_machines_create_or_update

    Implements virtual machine PUT method
    """
    virtual_machine_request = {"name":"name","location":"location","id":"id","type":"type","properties":{"guestOSType":"linux","vmwaretools":"vmwaretools","amountOfRam":0,"disks":[{"virtualDiskId":"virtualDiskId","totalSize":7,"controllerId":"controllerId","independenceMode":"persistent","virtualDiskName":"virtualDiskName"},{"virtualDiskId":"virtualDiskId","totalSize":7,"controllerId":"controllerId","independenceMode":"persistent","virtualDiskName":"virtualDiskName"}],"exposeToGuestVM":True,"customization":{"hostName":"hostName","password":"password","policyId":"policyId","dnsServers":[null,null],"username":"username"},"vmId":"vmId","publicIP":"publicIP","numberOfCores":6,"provisioningState":"provisioningState","templateId":"templateId","guestOS":"guestOS","password":"password","folder":"folder","vSphereNetworks":["vSphereNetworks","vSphereNetworks"],"dnsname":"dnsname","nics":[{"macAddress":"macAddress","customization":{"allocation":"static","primaryWinsServer":"primaryWinsServer","secondaryWinsServer":"secondaryWinsServer","ipAddress":"ipAddress","dnsServers":[null,null],"gateway":[null,null],"mask":"mask"},"virtualNicName":"virtualNicName","nicType":"E1000","powerOnBoot":True,"ipAddresses":["ipAddresses","ipAddresses"],"virtualNicId":"virtualNicId","network":{"name":"name","location":"location","id":"id","type":"type","properties":{"privateCloudId":"privateCloudId"},"assignable":True}},{"macAddress":"macAddress","customization":{"allocation":"static","primaryWinsServer":"primaryWinsServer","secondaryWinsServer":"secondaryWinsServer","ipAddress":"ipAddress","dnsServers":[null,null],"gateway":[null,null],"mask":"mask"},"virtualNicName":"virtualNicName","nicType":"E1000","powerOnBoot":True,"ipAddresses":["ipAddresses","ipAddresses"],"virtualNicId":"virtualNicId","network":{"name":"name","location":"location","id":"id","type":"type","properties":{"privateCloudId":"privateCloudId"},"assignable":True}}],"controllers":[{"name":"name","subType":"subType","id":"id","type":"type"},{"name":"name","subType":"subType","id":"id","type":"type"}],"privateCloudId":"privateCloudId","resourcePool":{"name":"name","privateCloudId":"privateCloudId","location":"location","id":"id","type":"type","properties":{"fullName":"fullName"}},"status":"running","username":"username"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'referer': 'referer_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtual_machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        json=virtual_machine_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_delete(client):
    """Test case for virtual_machines_delete

    Implements virtual machine DELETE method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'referer': 'referer_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtual_machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_get(client):
    """Test case for virtual_machines_get

    Implements virtual machine GET method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtual_machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_list_by_resource_group(client):
    """Test case for virtual_machines_list_by_resource_group

    Implements list virtual machine within RG method
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/virtualMachines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_list_by_subscription(client):
    """Test case for virtual_machines_list_by_subscription

    Implements list virtual machine within subscription method
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/virtualMachines'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_start(client):
    """Test case for virtual_machines_start

    Implements a start method for a virtual machine
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'referer': 'referer_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtual_machine_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_stop(client):
    """Test case for virtual_machines_stop

    Implements shutdown, poweroff, and suspend method for a virtual machine
    """
    m = {"mode":"reboot"}
    params = [('mode', 'mode_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'referer': 'referer_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtual_machine_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        json=m,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machines_update(client):
    """Test case for virtual_machines_update

    Implements virtual machine PATCH method
    """
    virtual_machine_request = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/virtualMachines/{virtual_machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_machine_name='virtual_machine_name_example'),
        headers=headers,
        json=virtual_machine_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

