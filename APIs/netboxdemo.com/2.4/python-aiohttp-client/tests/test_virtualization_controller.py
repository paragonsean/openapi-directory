# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_group import ClusterGroup
from openapi_server.models.cluster_type import ClusterType
from openapi_server.models.dcim_interfaces_list200_response import DcimInterfacesList200Response
from openapi_server.models.interface import Interface
from openapi_server.models.virtual_machine import VirtualMachine
from openapi_server.models.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from openapi_server.models.virtualization_cluster_groups_list200_response import VirtualizationClusterGroupsList200Response
from openapi_server.models.virtualization_cluster_types_list200_response import VirtualizationClusterTypesList200Response
from openapi_server.models.virtualization_clusters_list200_response import VirtualizationClustersList200Response
from openapi_server.models.virtualization_virtual_machines_list200_response import VirtualizationVirtualMachinesList200Response
from openapi_server.models.writable_cluster import WritableCluster
from openapi_server.models.writable_interface import WritableInterface
from openapi_server.models.writable_virtual_machine import WritableVirtualMachine


pytestmark = pytest.mark.asyncio

async def test_virtualization_choices_list(client):
    """Test case for virtualization_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_choices_read(client):
    """Test case for virtualization_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/_choices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_create(client):
    """Test case for virtualization_cluster_groups_create

    
    """
    body = {"name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","site":1,"comments":"comments","created":"2000-01-23","custom_fields":"{}","name":"name","id":6,"type":5,"group":0,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('type_id', 'type_id_example'),
                    ('type', 'type_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","site":1,"comments":"comments","created":"2000-01-23","custom_fields":"{}","name":"name","id":6,"type":5,"group":0,"tags":["tags","tags"]}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","site":1,"comments":"comments","created":"2000-01-23","custom_fields":"{}","name":"name","id":6,"type":5,"group":0,"tags":["tags","tags"]}
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
    body = {"is_connected":"is_connected","interface_connection":"interface_connection","untagged_vlan":3,"description":"description","enabled":True,"mgmt_only":True,"mtu":46277,"tags":["tags","tags"],"mode":2,"tagged_vlans":[9,9],"lag":5,"mac_address":"mac_address","circuit_termination":0,"name":"name","id":5,"device":6,"form_factor":1}
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
    params = [('name', 'name_example'),
                    ('enabled', 'enabled_example'),
                    ('mtu', 3.4),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('mac_address', 'mac_address_example'),
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
    body = {"is_connected":"is_connected","interface_connection":"interface_connection","untagged_vlan":3,"description":"description","enabled":True,"mgmt_only":True,"mtu":46277,"tags":["tags","tags"],"mode":2,"tagged_vlans":[9,9],"lag":5,"mac_address":"mac_address","circuit_termination":0,"name":"name","id":5,"device":6,"form_factor":1}
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
    body = {"is_connected":"is_connected","interface_connection":"interface_connection","untagged_vlan":3,"description":"description","enabled":True,"mgmt_only":True,"mtu":46277,"tags":["tags","tags"],"mode":2,"tagged_vlans":[9,9],"lag":5,"mac_address":"mac_address","circuit_termination":0,"name":"name","id":5,"device":6,"form_factor":1}
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
    body = {"cluster":0,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","memory":1280358508,"role":9,"created":"2000-01-23","custom_fields":"{}","primary_ip":"primary_ip","vcpus":13583,"platform":5,"tags":["tags","tags"],"disk":1294386358,"site":"site","local_context_data":"local_context_data","name":"name","id":1,"primary_ip6":7,"tenant":2,"primary_ip4":2,"status":3}
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
    params = [('name', 'name_example'),
                    ('cluster', 'cluster_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('status', 'status_example'),
                    ('cluster_group_id', 'cluster_group_id_example'),
                    ('cluster_group', 'cluster_group_example'),
                    ('cluster_type_id', 'cluster_type_id_example'),
                    ('cluster_type', 'cluster_type_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('region_id', 3.4),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('tag', 'tag_example'),
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
    body = {"cluster":0,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","memory":1280358508,"role":9,"created":"2000-01-23","custom_fields":"{}","primary_ip":"primary_ip","vcpus":13583,"platform":5,"tags":["tags","tags"],"disk":1294386358,"site":"site","local_context_data":"local_context_data","name":"name","id":1,"primary_ip6":7,"tenant":2,"primary_ip4":2,"status":3}
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
    body = {"cluster":0,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","memory":1280358508,"role":9,"created":"2000-01-23","custom_fields":"{}","primary_ip":"primary_ip","vcpus":13583,"platform":5,"tags":["tags","tags"],"disk":1294386358,"site":"site","local_context_data":"local_context_data","name":"name","id":1,"primary_ip6":7,"tenant":2,"primary_ip4":2,"status":3}
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

