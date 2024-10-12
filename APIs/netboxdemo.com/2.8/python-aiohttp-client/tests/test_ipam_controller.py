# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate import Aggregate
from openapi_server.models.available_ip import AvailableIP
from openapi_server.models.available_prefix import AvailablePrefix
from openapi_server.models.ip_address import IPAddress
from openapi_server.models.ipam_aggregates_list200_response import IpamAggregatesList200Response
from openapi_server.models.ipam_ip_addresses_list200_response import IpamIpAddressesList200Response
from openapi_server.models.ipam_prefixes_list200_response import IpamPrefixesList200Response
from openapi_server.models.ipam_rirs_list200_response import IpamRirsList200Response
from openapi_server.models.ipam_roles_list200_response import IpamRolesList200Response
from openapi_server.models.ipam_services_list200_response import IpamServicesList200Response
from openapi_server.models.ipam_vlan_groups_list200_response import IpamVlanGroupsList200Response
from openapi_server.models.ipam_vlans_list200_response import IpamVlansList200Response
from openapi_server.models.ipam_vrfs_list200_response import IpamVrfsList200Response
from openapi_server.models.prefix import Prefix
from openapi_server.models.rir import RIR
from openapi_server.models.role import Role
from openapi_server.models.service import Service
from openapi_server.models.vlan import VLAN
from openapi_server.models.vlan_group import VLANGroup
from openapi_server.models.vrf import VRF
from openapi_server.models.writable_aggregate import WritableAggregate
from openapi_server.models.writable_available_ip import WritableAvailableIP
from openapi_server.models.writable_ip_address import WritableIPAddress
from openapi_server.models.writable_prefix import WritablePrefix
from openapi_server.models.writable_service import WritableService
from openapi_server.models.writable_vlan import WritableVLAN
from openapi_server.models.writable_vlan_group import WritableVLANGroup
from openapi_server.models.writable_vrf import WritableVRF


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_create(client):
    """Test case for ipam_aggregates_create

    
    """
    body = {"date_added":"2000-01-23","last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","rir":6,"id":0,"family":"family","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/aggregates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_delete(client):
    """Test case for ipam_aggregates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/aggregates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_list(client):
    """Test case for ipam_aggregates_list

    
    """
    params = [('id', 'id_example'),
                    ('date_added', 'date_added_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('family', 3.4),
                    ('prefix', 'prefix_example'),
                    ('rir_id', 'rir_id_example'),
                    ('rir', 'rir_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('date_added__n', 'date_added__n_example'),
                    ('date_added__lte', 'date_added__lte_example'),
                    ('date_added__lt', 'date_added__lt_example'),
                    ('date_added__gte', 'date_added__gte_example'),
                    ('date_added__gt', 'date_added__gt_example'),
                    ('rir_id__n', 'rir_id__n_example'),
                    ('rir__n', 'rir__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/aggregates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_partial_update(client):
    """Test case for ipam_aggregates_partial_update

    
    """
    body = {"date_added":"2000-01-23","last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","rir":6,"id":0,"family":"family","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/aggregates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_read(client):
    """Test case for ipam_aggregates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/aggregates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_update(client):
    """Test case for ipam_aggregates_update

    
    """
    body = {"date_added":"2000-01-23","last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","rir":6,"id":0,"family":"family","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/aggregates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_create(client):
    """Test case for ipam_ip_addresses_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","role":"loopback","created":"2000-01-23","custom_fields":"{}","description":"description","vrf":2,"interface":6,"dns_name":"dns_name","tags":["tags","tags"],"nat_outside":5,"id":0,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/ip-addresses/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_delete(client):
    """Test case for ipam_ip_addresses_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/ip-addresses/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_list(client):
    """Test case for ipam_ip_addresses_list

    
    """
    params = [('id', 'id_example'),
                    ('dns_name', 'dns_name_example'),
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
                    ('family', 3.4),
                    ('parent', 'parent_example'),
                    ('address', 'address_example'),
                    ('mask_length', 3.4),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('device', 'device_example'),
                    ('device_id', 'device_id_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('interface', 'interface_example'),
                    ('interface_id', 'interface_id_example'),
                    ('assigned_to_interface', 'assigned_to_interface_example'),
                    ('status', 'status_example'),
                    ('role', 'role_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('dns_name__n', 'dns_name__n_example'),
                    ('dns_name__ic', 'dns_name__ic_example'),
                    ('dns_name__nic', 'dns_name__nic_example'),
                    ('dns_name__iew', 'dns_name__iew_example'),
                    ('dns_name__niew', 'dns_name__niew_example'),
                    ('dns_name__isw', 'dns_name__isw_example'),
                    ('dns_name__nisw', 'dns_name__nisw_example'),
                    ('dns_name__ie', 'dns_name__ie_example'),
                    ('dns_name__nie', 'dns_name__nie_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('vrf_id__n', 'vrf_id__n_example'),
                    ('vrf__n', 'vrf__n_example'),
                    ('virtual_machine_id__n', 'virtual_machine_id__n_example'),
                    ('virtual_machine__n', 'virtual_machine__n_example'),
                    ('interface__n', 'interface__n_example'),
                    ('interface_id__n', 'interface_id__n_example'),
                    ('status__n', 'status__n_example'),
                    ('role__n', 'role__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/ip-addresses/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_partial_update(client):
    """Test case for ipam_ip_addresses_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","role":"loopback","created":"2000-01-23","custom_fields":"{}","description":"description","vrf":2,"interface":6,"dns_name":"dns_name","tags":["tags","tags"],"nat_outside":5,"id":0,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/ip-addresses/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_read(client):
    """Test case for ipam_ip_addresses_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/ip-addresses/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_update(client):
    """Test case for ipam_ip_addresses_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","role":"loopback","created":"2000-01-23","custom_fields":"{}","description":"description","vrf":2,"interface":6,"dns_name":"dns_name","tags":["tags","tags"],"nat_outside":5,"id":0,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/ip-addresses/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_available_ips_create(client):
    """Test case for ipam_prefixes_available_ips_create

    
    """
    body = {"address":"address","family":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/prefixes/{id}/available-ips'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_available_ips_read(client):
    """Test case for ipam_prefixes_available_ips_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/prefixes/{id}/available-ips'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_available_prefixes_create(client):
    """Test case for ipam_prefixes_available_prefixes_create

    A convenience method for returning available child prefixes within a parent.
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":6,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":2,"tags":["tags","tags"],"site":1,"vlan":5,"id":0,"family":"family","tenant":5,"status":"container"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/prefixes/{id}/available-prefixes'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_available_prefixes_read(client):
    """Test case for ipam_prefixes_available_prefixes_read

    A convenience method for returning available child prefixes within a parent.
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/prefixes/{id}/available-prefixes'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_create(client):
    """Test case for ipam_prefixes_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":6,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":2,"tags":["tags","tags"],"site":1,"vlan":5,"id":0,"family":"family","tenant":5,"status":"container"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/prefixes/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_delete(client):
    """Test case for ipam_prefixes_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/prefixes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_list(client):
    """Test case for ipam_prefixes_list

    
    """
    params = [('id', 'id_example'),
                    ('is_pool', 'is_pool_example'),
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
                    ('family', 3.4),
                    ('prefix', 'prefix_example'),
                    ('within', 'within_example'),
                    ('within_include', 'within_include_example'),
                    ('contains', 'contains_example'),
                    ('mask_length', 3.4),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('vlan_id', 'vlan_id_example'),
                    ('vlan_vid', 3.4),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('vrf_id__n', 'vrf_id__n_example'),
                    ('vrf__n', 'vrf__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('vlan_id__n', 'vlan_id__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('status__n', 'status__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/prefixes/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_partial_update(client):
    """Test case for ipam_prefixes_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":6,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":2,"tags":["tags","tags"],"site":1,"vlan":5,"id":0,"family":"family","tenant":5,"status":"container"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/prefixes/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_read(client):
    """Test case for ipam_prefixes_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/prefixes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_update(client):
    """Test case for ipam_prefixes_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":6,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":2,"tags":["tags","tags"],"site":1,"vlan":5,"id":0,"family":"family","tenant":5,"status":"container"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/prefixes/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_create(client):
    """Test case for ipam_rirs_create

    
    """
    body = {"is_private":True,"aggregate_count":6,"name":"name","description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/rirs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_delete(client):
    """Test case for ipam_rirs_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/rirs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_list(client):
    """Test case for ipam_rirs_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('is_private', 'is_private_example'),
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
        path='/api/ipam/rirs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_partial_update(client):
    """Test case for ipam_rirs_partial_update

    
    """
    body = {"is_private":True,"aggregate_count":6,"name":"name","description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/rirs/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_read(client):
    """Test case for ipam_rirs_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/rirs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_update(client):
    """Test case for ipam_rirs_update

    
    """
    body = {"is_private":True,"aggregate_count":6,"name":"name","description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/rirs/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_create(client):
    """Test case for ipam_roles_create

    
    """
    body = {"name":"name","description":"description","weight":18471,"prefix_count":1,"id":6,"slug":"slug","vlan_count":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_delete(client):
    """Test case for ipam_roles_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_list(client):
    """Test case for ipam_roles_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
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
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_partial_update(client):
    """Test case for ipam_roles_partial_update

    
    """
    body = {"name":"name","description":"description","weight":18471,"prefix_count":1,"id":6,"slug":"slug","vlan_count":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_read(client):
    """Test case for ipam_roles_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_update(client):
    """Test case for ipam_roles_update

    
    """
    body = {"name":"name","description":"description","weight":18471,"prefix_count":1,"id":6,"slug":"slug","vlan_count":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_create(client):
    """Test case for ipam_services_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","ipaddresses":[1,1],"port":39073,"created":"2000-01-23","custom_fields":"{}","name":"name","virtual_machine":5,"description":"description","id":6,"device":0,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/services/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_delete(client):
    """Test case for ipam_services_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/services/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_list(client):
    """Test case for ipam_services_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('protocol', 'protocol_example'),
                    ('port', 'port_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
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
                    ('protocol__n', 'protocol__n_example'),
                    ('port__n', 'port__n_example'),
                    ('port__lte', 'port__lte_example'),
                    ('port__lt', 'port__lt_example'),
                    ('port__gte', 'port__gte_example'),
                    ('port__gt', 'port__gt_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_machine_id__n', 'virtual_machine_id__n_example'),
                    ('virtual_machine__n', 'virtual_machine__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/services/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_partial_update(client):
    """Test case for ipam_services_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","ipaddresses":[1,1],"port":39073,"created":"2000-01-23","custom_fields":"{}","name":"name","virtual_machine":5,"description":"description","id":6,"device":0,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/services/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_read(client):
    """Test case for ipam_services_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/services/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_update(client):
    """Test case for ipam_services_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","ipaddresses":[1,1],"port":39073,"created":"2000-01-23","custom_fields":"{}","name":"name","virtual_machine":5,"description":"description","id":6,"device":0,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/services/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_create(client):
    """Test case for ipam_vlan_groups_create

    
    """
    body = {"site":6,"name":"name","description":"description","id":0,"slug":"slug","vlan_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/vlan-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_delete(client):
    """Test case for ipam_vlan_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/vlan-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_list(client):
    """Test case for ipam_vlan_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
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
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/vlan-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_partial_update(client):
    """Test case for ipam_vlan_groups_partial_update

    
    """
    body = {"site":6,"name":"name","description":"description","id":0,"slug":"slug","vlan_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/vlan-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_read(client):
    """Test case for ipam_vlan_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/vlan-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_update(client):
    """Test case for ipam_vlan_groups_update

    
    """
    body = {"site":6,"name":"name","description":"description","id":0,"slug":"slug","vlan_count":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/vlan-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_create(client):
    """Test case for ipam_vlans_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","tags":["tags","tags"],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/vlans/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_delete(client):
    """Test case for ipam_vlans_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/vlans/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_list(client):
    """Test case for ipam_vlans_list

    
    """
    params = [('id', 'id_example'),
                    ('vid', 'vid_example'),
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
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('vid__n', 'vid__n_example'),
                    ('vid__lte', 'vid__lte_example'),
                    ('vid__lt', 'vid__lt_example'),
                    ('vid__gte', 'vid__gte_example'),
                    ('vid__gt', 'vid__gt_example'),
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
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('status__n', 'status__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/vlans/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_partial_update(client):
    """Test case for ipam_vlans_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","tags":["tags","tags"],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/vlans/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_read(client):
    """Test case for ipam_vlans_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/vlans/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_update(client):
    """Test case for ipam_vlans_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","tags":["tags","tags"],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/vlans/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_create(client):
    """Test case for ipam_vrfs_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","ipaddress_count":6,"tags":["tags","tags"],"rd":"rd","name":"name","enforce_unique":True,"prefix_count":1,"id":0,"tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/vrfs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_delete(client):
    """Test case for ipam_vrfs_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/vrfs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_list(client):
    """Test case for ipam_vrfs_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('rd', 'rd_example'),
                    ('enforce_unique', 'enforce_unique_example'),
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
                    ('rd__n', 'rd__n_example'),
                    ('rd__ic', 'rd__ic_example'),
                    ('rd__nic', 'rd__nic_example'),
                    ('rd__iew', 'rd__iew_example'),
                    ('rd__niew', 'rd__niew_example'),
                    ('rd__isw', 'rd__isw_example'),
                    ('rd__nisw', 'rd__nisw_example'),
                    ('rd__ie', 'rd__ie_example'),
                    ('rd__nie', 'rd__nie_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/vrfs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_partial_update(client):
    """Test case for ipam_vrfs_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","ipaddress_count":6,"tags":["tags","tags"],"rd":"rd","name":"name","enforce_unique":True,"prefix_count":1,"id":0,"tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/vrfs/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_read(client):
    """Test case for ipam_vrfs_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/vrfs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_update(client):
    """Test case for ipam_vrfs_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","ipaddress_count":6,"tags":["tags","tags"],"rd":"rd","name":"name","enforce_unique":True,"prefix_count":1,"id":0,"tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/vrfs/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

