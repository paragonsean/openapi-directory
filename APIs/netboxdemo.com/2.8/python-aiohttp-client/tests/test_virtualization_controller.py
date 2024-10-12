# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_group import ClusterGroup
from openapi_server.models.cluster_type import ClusterType
from openapi_server.models.virtual_machine_interface import VirtualMachineInterface
from openapi_server.models.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from openapi_server.models.virtualization_cluster_groups_list200_response import VirtualizationClusterGroupsList200Response
from openapi_server.models.virtualization_cluster_types_list200_response import VirtualizationClusterTypesList200Response
from openapi_server.models.virtualization_clusters_list200_response import VirtualizationClustersList200Response
from openapi_server.models.virtualization_interfaces_list200_response import VirtualizationInterfacesList200Response
from openapi_server.models.virtualization_virtual_machines_list200_response import VirtualizationVirtualMachinesList200Response
from openapi_server.models.writable_cluster import WritableCluster
from openapi_server.models.writable_virtual_machine_interface import WritableVirtualMachineInterface
from openapi_server.models.writable_virtual_machine_with_config_context import WritableVirtualMachineWithConfigContext


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_create(client):
    """Test case for virtualization_cluster_groups_create

    
    """
    body = {"name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/cluster-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_delete(client):
    """Test case for virtualization_cluster_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_list(client):
    """Test case for virtualization_cluster_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/cluster-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_partial_update(client):
    """Test case for virtualization_cluster_groups_partial_update

    
    """
    body = {"name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_read(client):
    """Test case for virtualization_cluster_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_update(client):
    """Test case for virtualization_cluster_groups_update

    
    """
    body = {"name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_create(client):
    """Test case for virtualization_cluster_types_create

    
    """
    body = {"name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/cluster-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_delete(client):
    """Test case for virtualization_cluster_types_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_list(client):
    """Test case for virtualization_cluster_types_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/cluster-types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_partial_update(client):
    """Test case for virtualization_cluster_types_partial_update

    
    """
    body = {"name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_read(client):
    """Test case for virtualization_cluster_types_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_update(client):
    """Test case for virtualization_cluster_types_update

    
    """
    body = {"name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_create(client):
    """Test case for virtualization_clusters_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","type":2,"tags":["tags","tags"],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/clusters/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_delete(client):
    """Test case for virtualization_clusters_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_list(client):
    """Test case for virtualization_clusters_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('type_id', 'type_id_example'),
                    ('type', 'type_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('type_id__n', 'type_id__n_example'),
                    ('type__n', 'type__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/clusters/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_partial_update(client):
    """Test case for virtualization_clusters_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","type":2,"tags":["tags","tags"],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_read(client):
    """Test case for virtualization_clusters_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_update(client):
    """Test case for virtualization_clusters_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","type":2,"tags":["tags","tags"],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_create(client):
    """Test case for virtualization_interfaces_create

    
    """
    body = {"mode":"access","tagged_vlans":[1,1],"untagged_vlan":5,"mac_address":"mac_address","name":"name","virtual_machine":5,"description":"description","id":0,"type":"virtual","enabled":True,"mtu":39501,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/interfaces/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_delete(client):
    """Test case for virtualization_interfaces_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_list(client):
    """Test case for virtualization_interfaces_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('enabled', 'enabled_example'),
                    ('mtu', 'mtu_example'),
                    ('q', 'q_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('mac_address', 'mac_address_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('mtu__n', 'mtu__n_example'),
                    ('mtu__lte', 'mtu__lte_example'),
                    ('mtu__lt', 'mtu__lt_example'),
                    ('mtu__gte', 'mtu__gte_example'),
                    ('mtu__gt', 'mtu__gt_example'),
                    ('virtual_machine_id__n', 'virtual_machine_id__n_example'),
                    ('virtual_machine__n', 'virtual_machine__n_example'),
                    ('mac_address__n', 'mac_address__n_example'),
                    ('mac_address__ic', 'mac_address__ic_example'),
                    ('mac_address__nic', 'mac_address__nic_example'),
                    ('mac_address__iew', 'mac_address__iew_example'),
                    ('mac_address__niew', 'mac_address__niew_example'),
                    ('mac_address__isw', 'mac_address__isw_example'),
                    ('mac_address__nisw', 'mac_address__nisw_example'),
                    ('mac_address__ie', 'mac_address__ie_example'),
                    ('mac_address__nie', 'mac_address__nie_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/interfaces/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_partial_update(client):
    """Test case for virtualization_interfaces_partial_update

    
    """
    body = {"mode":"access","tagged_vlans":[1,1],"untagged_vlan":5,"mac_address":"mac_address","name":"name","virtual_machine":5,"description":"description","id":0,"type":"virtual","enabled":True,"mtu":39501,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_read(client):
    """Test case for virtualization_interfaces_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_update(client):
    """Test case for virtualization_interfaces_update

    
    """
    body = {"mode":"access","tagged_vlans":[1,1],"untagged_vlan":5,"mac_address":"mac_address","name":"name","virtual_machine":5,"description":"description","id":0,"type":"virtual","enabled":True,"mtu":39501,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_create(client):
    """Test case for virtualization_virtual_machines_create

    
    """
    body = {"cluster":0,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","memory":1280358508,"role":9,"config_context":{"key":"config_context"},"created":"2000-01-23","custom_fields":"{}","primary_ip":"primary_ip","vcpus":6642,"platform":5,"tags":["tags","tags"],"disk":1294386358,"site":"site","local_context_data":"local_context_data","name":"name","id":1,"primary_ip6":7,"tenant":3,"primary_ip4":2,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/virtual-machines/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_delete(client):
    """Test case for virtualization_virtual_machines_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_list(client):
    """Test case for virtualization_virtual_machines_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('cluster', 'cluster_example'),
                    ('vcpus', 'vcpus_example'),
                    ('memory', 'memory_example'),
                    ('disk', 'disk_example'),
                    ('local_context_data', 'local_context_data_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('status', 'status_example'),
                    ('cluster_group_id', 'cluster_group_id_example'),
                    ('cluster_group', 'cluster_group_example'),
                    ('cluster_type_id', 'cluster_type_id_example'),
                    ('cluster_type', 'cluster_type_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('mac_address', 'mac_address_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('cluster__n', 'cluster__n_example'),
                    ('vcpus__n', 'vcpus__n_example'),
                    ('vcpus__lte', 'vcpus__lte_example'),
                    ('vcpus__lt', 'vcpus__lt_example'),
                    ('vcpus__gte', 'vcpus__gte_example'),
                    ('vcpus__gt', 'vcpus__gt_example'),
                    ('memory__n', 'memory__n_example'),
                    ('memory__lte', 'memory__lte_example'),
                    ('memory__lt', 'memory__lt_example'),
                    ('memory__gte', 'memory__gte_example'),
                    ('memory__gt', 'memory__gt_example'),
                    ('disk__n', 'disk__n_example'),
                    ('disk__lte', 'disk__lte_example'),
                    ('disk__lt', 'disk__lt_example'),
                    ('disk__gte', 'disk__gte_example'),
                    ('disk__gt', 'disk__gt_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('status__n', 'status__n_example'),
                    ('cluster_group_id__n', 'cluster_group_id__n_example'),
                    ('cluster_group__n', 'cluster_group__n_example'),
                    ('cluster_type_id__n', 'cluster_type_id__n_example'),
                    ('cluster_type__n', 'cluster_type__n_example'),
                    ('cluster_id__n', 'cluster_id__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('platform_id__n', 'platform_id__n_example'),
                    ('platform__n', 'platform__n_example'),
                    ('mac_address__n', 'mac_address__n_example'),
                    ('mac_address__ic', 'mac_address__ic_example'),
                    ('mac_address__nic', 'mac_address__nic_example'),
                    ('mac_address__iew', 'mac_address__iew_example'),
                    ('mac_address__niew', 'mac_address__niew_example'),
                    ('mac_address__isw', 'mac_address__isw_example'),
                    ('mac_address__nisw', 'mac_address__nisw_example'),
                    ('mac_address__ie', 'mac_address__ie_example'),
                    ('mac_address__nie', 'mac_address__nie_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/virtual-machines/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_partial_update(client):
    """Test case for virtualization_virtual_machines_partial_update

    
    """
    body = {"cluster":0,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","memory":1280358508,"role":9,"config_context":{"key":"config_context"},"created":"2000-01-23","custom_fields":"{}","primary_ip":"primary_ip","vcpus":6642,"platform":5,"tags":["tags","tags"],"disk":1294386358,"site":"site","local_context_data":"local_context_data","name":"name","id":1,"primary_ip6":7,"tenant":3,"primary_ip4":2,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_read(client):
    """Test case for virtualization_virtual_machines_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_update(client):
    """Test case for virtualization_virtual_machines_update

    
    """
    body = {"cluster":0,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","memory":1280358508,"role":9,"config_context":{"key":"config_context"},"created":"2000-01-23","custom_fields":"{}","primary_ip":"primary_ip","vcpus":6642,"platform":5,"tags":["tags","tags"],"disk":1294386358,"site":"site","local_context_data":"local_context_data","name":"name","id":1,"primary_ip6":7,"tenant":3,"primary_ip4":2,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

