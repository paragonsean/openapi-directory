# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hana_instance import HanaInstance
from openapi_server.models.hana_instances_list_result import HanaInstancesListResult
from openapi_server.models.operation_list import OperationList
from openapi_server.models.sap_monitor import SapMonitor
from openapi_server.models.sap_monitor_list_result import SapMonitorListResult
from openapi_server.models.tags import Tags


pytestmark = pytest.mark.asyncio

async def test_hana_instances_create(client):
    """Test case for hana_instances_create

    Creates a SAP HANA instance.
    """
    hana_instance_parameter = {"properties":{"powerState":"starting","hardwareProfile":{"hanaInstanceSize":"S72m","hardwareType":"Cisco_UCS"},"storageProfile":{"osDisks":[{"lun":6,"name":"name","diskSizeGB":0},{"lun":6,"name":"name","diskSizeGB":0}],"nfsIpAddress":"nfsIpAddress"},"networkProfile":{"networkInterfaces":[{"ipAddress":"ipAddress"},{"ipAddress":"ipAddress"}],"circuitId":"circuitId"},"proximityPlacementGroup":"proximityPlacementGroup","provisioningState":"Accepted","hanaInstanceId":"hanaInstanceId","hwRevision":"hwRevision","partnerNodeId":"partnerNodeId","osProfile":{"sshPublicKey":"sshPublicKey","computerName":"computerName","osType":"osType","version":"version"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances/{hana_instance_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', hana_instance_name='hana_instance_name_example'),
        headers=headers,
        json=hana_instance_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_delete(client):
    """Test case for hana_instances_delete

    Deletes a SAP HANA instance.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances/{hana_instance_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', hana_instance_name='hana_instance_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_get(client):
    """Test case for hana_instances_get

    Gets properties of a SAP HANA instance.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances/{hana_instance_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', hana_instance_name='hana_instance_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_list(client):
    """Test case for hana_instances_list

    Gets a list of SAP HANA instances in the specified subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HanaOnAzure/hanaInstances'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_list_by_resource_group(client):
    """Test case for hana_instances_list_by_resource_group

    Gets a list of SAP HANA instances in the specified subscription and the resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_restart(client):
    """Test case for hana_instances_restart

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances/{hana_instance_name}/restart'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', hana_instance_name='hana_instance_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_shutdown(client):
    """Test case for hana_instances_shutdown

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances/{hana_instance_name}/shutdown'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', hana_instance_name='hana_instance_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_start(client):
    """Test case for hana_instances_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances/{hana_instance_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', hana_instance_name='hana_instance_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hana_instances_update(client):
    """Test case for hana_instances_update

    Patches the Tags field of a SAP HANA instance.
    """
    tags_parameter = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/hanaInstances/{hana_instance_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', hana_instance_name='hana_instance_name_example'),
        headers=headers,
        json=tags_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.HanaOnAzure/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sap_monitors_create(client):
    """Test case for sap_monitors_create

    Creates a SAP monitor.
    """
    sap_monitor_parameter = {"properties":{"hanaDbName":"hanaDbName","logAnalyticsWorkspaceArmId":"logAnalyticsWorkspaceArmId","hanaSubnet":"hanaSubnet","managedResourceGroupName":"managedResourceGroupName","provisioningState":"Accepted","logAnalyticsWorkspaceSharedKey":"logAnalyticsWorkspaceSharedKey","keyVaultId":"keyVaultId","hanaDbPassword":"hanaDbPassword","hanaDbSqlPort":0,"hanaDbUsername":"hanaDbUsername","hanaHostname":"hanaHostname","logAnalyticsWorkspaceId":"logAnalyticsWorkspaceId","hanaDbPasswordKeyVaultUrl":"hanaDbPasswordKeyVaultUrl","hanaDbCredentialsMsiId":"hanaDbCredentialsMsiId","enableCustomerAnalytics":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/sapMonitors/{sap_monitor_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', sap_monitor_name='sap_monitor_name_example'),
        headers=headers,
        json=sap_monitor_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sap_monitors_delete(client):
    """Test case for sap_monitors_delete

    Deletes a SAP monitor.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/sapMonitors/{sap_monitor_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', sap_monitor_name='sap_monitor_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sap_monitors_get(client):
    """Test case for sap_monitors_get

    Gets properties of a SAP monitor.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/sapMonitors/{sap_monitor_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', sap_monitor_name='sap_monitor_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sap_monitors_list(client):
    """Test case for sap_monitors_list

    Gets a list of SAP monitors in the specified subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HanaOnAzure/sapMonitors'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sap_monitors_update(client):
    """Test case for sap_monitors_update

    Patches the Tags field of a SAP monitor.
    """
    tags_parameter = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HanaOnAzure/sapMonitors/{sap_monitor_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', sap_monitor_name='sap_monitor_name_example'),
        headers=headers,
        json=tags_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

