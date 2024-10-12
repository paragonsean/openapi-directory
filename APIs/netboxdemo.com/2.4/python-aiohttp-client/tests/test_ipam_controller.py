# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aggregate import Aggregate
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
    body = {"date_added":"2000-01-23","last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","rir":1,"id":6,"family":0,"tags":["tags","tags"]}
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
    params = [('family', 'family_example'),
                    ('date_added', 'date_added_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('rir_id', 'rir_id_example'),
                    ('rir', 'rir_example'),
                    ('tag', 'tag_example'),
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
    body = {"date_added":"2000-01-23","last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","rir":1,"id":6,"family":0,"tags":["tags","tags"]}
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
    body = {"date_added":"2000-01-23","last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","rir":1,"id":6,"family":0,"tags":["tags","tags"]}
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

async def test_ipam_choices_list(client):
    """Test case for ipam_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_choices_read(client):
    """Test case for ipam_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/_choices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_create(client):
    """Test case for ipam_ip_addresses_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","role":2,"created":"2000-01-23","custom_fields":"{}","description":"description","vrf":3,"interface":1,"tags":["tags","tags"],"nat_outside":5,"id":6,"family":0,"tenant":9,"nat_inside":5,"status":7}
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
    params = [('family', 'family_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('parent', 'parent_example'),
                    ('address', 'address_example'),
                    ('mask_length', 3.4),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('device', 'device_example'),
                    ('device_id', 3.4),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('interface_id', 'interface_id_example'),
                    ('status', 'status_example'),
                    ('role', 'role_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","role":2,"created":"2000-01-23","custom_fields":"{}","description":"description","vrf":3,"interface":1,"tags":["tags","tags"],"nat_outside":5,"id":6,"family":0,"tenant":9,"nat_inside":5,"status":7}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","role":2,"created":"2000-01-23","custom_fields":"{}","description":"description","vrf":3,"interface":1,"tags":["tags","tags"],"nat_outside":5,"id":6,"family":0,"tenant":9,"nat_inside":5,"status":7}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":9,"tags":["tags","tags"],"site":5,"vlan":7,"id":6,"family":0,"tenant":2,"status":5}
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

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":9,"tags":["tags","tags"],"site":5,"vlan":7,"id":6,"family":0,"tenant":2,"status":5}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":9,"tags":["tags","tags"],"site":5,"vlan":7,"id":6,"family":0,"tenant":2,"status":5}
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
    params = [('family', 'family_example'),
                    ('is_pool', 'is_pool_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('within', 'within_example'),
                    ('within_include', 'within_include_example'),
                    ('contains', 'contains_example'),
                    ('mask_length', 3.4),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('vlan_id', 'vlan_id_example'),
                    ('vlan_vid', 3.4),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":9,"tags":["tags","tags"],"site":5,"vlan":7,"id":6,"family":0,"tenant":2,"status":5}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","prefix":"prefix","description":"description","is_pool":True,"vrf":9,"tags":["tags","tags"],"site":5,"vlan":7,"id":6,"family":0,"tenant":2,"status":5}
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
    body = {"is_private":True,"name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('is_private', 'is_private_example'),
                    ('id__in', 'id__in_example'),
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
    body = {"is_private":True,"name":"name","id":6,"slug":"slug"}
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
    body = {"is_private":True,"name":"name","id":6,"slug":"slug"}
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
    body = {"name":"name","weight":4803,"id":6,"slug":"slug"}
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
        path='/api/ipam/roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_partial_update(client):
    """Test case for ipam_roles_partial_update

    
    """
    body = {"name":"name","weight":4803,"id":6,"slug":"slug"}
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
    body = {"name":"name","weight":4803,"id":6,"slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":5,"ipaddresses":[1,1],"port":39073,"created":"2000-01-23","custom_fields":"{}","name":"name","virtual_machine":2,"description":"description","id":6,"device":0}
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
    params = [('name', 'name_example'),
                    ('protocol', 'protocol_example'),
                    ('port', 3.4),
                    ('q', 'q_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":5,"ipaddresses":[1,1],"port":39073,"created":"2000-01-23","custom_fields":"{}","name":"name","virtual_machine":2,"description":"description","id":6,"device":0}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":5,"ipaddresses":[1,1],"port":39073,"created":"2000-01-23","custom_fields":"{}","name":"name","virtual_machine":2,"description":"description","id":6,"device":0}
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
    body = {"site":6,"name":"name","id":0,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
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
    body = {"site":6,"name":"name","id":0,"slug":"slug"}
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
    body = {"site":6,"name":"name","id":0,"slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","tags":["tags","tags"],"vid":2891,"site":5,"name":"name","id":6,"tenant":2,"group":0,"status":5}
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
    params = [('vid', 3.4),
                    ('name', 'name_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","tags":["tags","tags"],"vid":2891,"site":5,"name":"name","id":6,"tenant":2,"group":0,"status":5}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","description":"description","display_name":"display_name","tags":["tags","tags"],"vid":2891,"site":5,"name":"name","id":6,"tenant":2,"group":0,"status":5}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rd":"rd","created":"2000-01-23","custom_fields":"{}","name":"name","description":"description","enforce_unique":True,"id":0,"display_name":"display_name","tenant":6,"tags":["tags","tags"]}
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
    params = [('name', 'name_example'),
                    ('rd', 'rd_example'),
                    ('enforce_unique', 'enforce_unique_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rd":"rd","created":"2000-01-23","custom_fields":"{}","name":"name","description":"description","enforce_unique":True,"id":0,"display_name":"display_name","tenant":6,"tags":["tags","tags"]}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","rd":"rd","created":"2000-01-23","custom_fields":"{}","name":"name","description":"description","enforce_unique":True,"id":0,"display_name":"display_name","tenant":6,"tags":["tags","tags"]}
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

