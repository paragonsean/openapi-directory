# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asn import ASN
from openapi_server.models.aggregate import Aggregate
from openapi_server.models.available_ip import AvailableIP
from openapi_server.models.available_prefix import AvailablePrefix
from openapi_server.models.available_vlan import AvailableVLAN
from openapi_server.models.fhrp_group import FHRPGroup
from openapi_server.models.fhrp_group_assignment import FHRPGroupAssignment
from openapi_server.models.ip_address import IPAddress
from openapi_server.models.ip_range import IPRange
from openapi_server.models.ipam_aggregates_list200_response import IpamAggregatesList200Response
from openapi_server.models.ipam_asns_list200_response import IpamAsnsList200Response
from openapi_server.models.ipam_fhrp_group_assignments_list200_response import IpamFhrpGroupAssignmentsList200Response
from openapi_server.models.ipam_fhrp_groups_list200_response import IpamFhrpGroupsList200Response
from openapi_server.models.ipam_ip_addresses_list200_response import IpamIpAddressesList200Response
from openapi_server.models.ipam_ip_ranges_list200_response import IpamIpRangesList200Response
from openapi_server.models.ipam_l2vpn_terminations_list200_response import IpamL2vpnTerminationsList200Response
from openapi_server.models.ipam_l2vpns_list200_response import IpamL2vpnsList200Response
from openapi_server.models.ipam_prefixes_list200_response import IpamPrefixesList200Response
from openapi_server.models.ipam_rirs_list200_response import IpamRirsList200Response
from openapi_server.models.ipam_roles_list200_response import IpamRolesList200Response
from openapi_server.models.ipam_route_targets_list200_response import IpamRouteTargetsList200Response
from openapi_server.models.ipam_service_templates_list200_response import IpamServiceTemplatesList200Response
from openapi_server.models.ipam_services_list200_response import IpamServicesList200Response
from openapi_server.models.ipam_vlan_groups_list200_response import IpamVlanGroupsList200Response
from openapi_server.models.ipam_vlans_list200_response import IpamVlansList200Response
from openapi_server.models.ipam_vrfs_list200_response import IpamVrfsList200Response
from openapi_server.models.l2_vpn import L2VPN
from openapi_server.models.l2_vpn_termination import L2VPNTermination
from openapi_server.models.prefix import Prefix
from openapi_server.models.prefix_length import PrefixLength
from openapi_server.models.rir import RIR
from openapi_server.models.role import Role
from openapi_server.models.route_target import RouteTarget
from openapi_server.models.service import Service
from openapi_server.models.service_template import ServiceTemplate
from openapi_server.models.vlan import VLAN
from openapi_server.models.vlan_group import VLANGroup
from openapi_server.models.vrf import VRF
from openapi_server.models.writable_asn import WritableASN
from openapi_server.models.writable_aggregate import WritableAggregate
from openapi_server.models.writable_available_ip import WritableAvailableIP
from openapi_server.models.writable_create_available_vlan import WritableCreateAvailableVLAN
from openapi_server.models.writable_fhrp_group_assignment import WritableFHRPGroupAssignment
from openapi_server.models.writable_ip_address import WritableIPAddress
from openapi_server.models.writable_ip_range import WritableIPRange
from openapi_server.models.writable_l2_vpn import WritableL2VPN
from openapi_server.models.writable_l2_vpn_termination import WritableL2VPNTermination
from openapi_server.models.writable_prefix import WritablePrefix
from openapi_server.models.writable_route_target import WritableRouteTarget
from openapi_server.models.writable_service import WritableService
from openapi_server.models.writable_service_template import WritableServiceTemplate
from openapi_server.models.writable_vlan import WritableVLAN
from openapi_server.models.writable_vrf import WritableVRF


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_bulk_delete(client):
    """Test case for ipam_aggregates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/aggregates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_bulk_partial_update(client):
    """Test case for ipam_aggregates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"date_added":"2000-01-23","rir":6,"id":0,"family":"family","tenant":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/aggregates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_bulk_update(client):
    """Test case for ipam_aggregates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"date_added":"2000-01-23","rir":6,"id":0,"family":"family","tenant":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/aggregates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_aggregates_create(client):
    """Test case for ipam_aggregates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"date_added":"2000-01-23","rir":6,"id":0,"family":"family","tenant":1}
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
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('family', 3.4),
                    ('prefix', 'prefix_example'),
                    ('rir_id', 'rir_id_example'),
                    ('rir', 'rir_example'),
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
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('rir_id__n', 'rir_id__n_example'),
                    ('rir__n', 'rir__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"date_added":"2000-01-23","rir":6,"id":0,"family":"family","tenant":1}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"date_added":"2000-01-23","rir":6,"id":0,"family":"family","tenant":1}
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

async def test_ipam_asns_bulk_delete(client):
    """Test case for ipam_asns_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/asns/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_bulk_partial_update(client):
    """Test case for ipam_asns_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"description":"description","provider_count":1,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rir":5,"id":6,"asn":343953089,"tenant":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/asns/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_bulk_update(client):
    """Test case for ipam_asns_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"description":"description","provider_count":1,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rir":5,"id":6,"asn":343953089,"tenant":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/asns/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_create(client):
    """Test case for ipam_asns_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"description":"description","provider_count":1,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rir":5,"id":6,"asn":343953089,"tenant":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/asns/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_delete(client):
    """Test case for ipam_asns_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/asns/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_list(client):
    """Test case for ipam_asns_list

    
    """
    params = [('id', 'id_example'),
                    ('asn', 'asn_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('rir_id', 'rir_id_example'),
                    ('rir', 'rir_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('asn__n', 'asn__n_example'),
                    ('asn__lte', 'asn__lte_example'),
                    ('asn__lt', 'asn__lt_example'),
                    ('asn__gte', 'asn__gte_example'),
                    ('asn__gt', 'asn__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('rir_id__n', 'rir_id__n_example'),
                    ('rir__n', 'rir__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/asns/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_partial_update(client):
    """Test case for ipam_asns_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"description":"description","provider_count":1,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rir":5,"id":6,"asn":343953089,"tenant":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/asns/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_read(client):
    """Test case for ipam_asns_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/asns/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_asns_update(client):
    """Test case for ipam_asns_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":5,"description":"description","provider_count":1,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"rir":5,"id":6,"asn":343953089,"tenant":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/asns/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_bulk_delete(client):
    """Test case for ipam_fhrp_group_assignments_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/fhrp-group-assignments/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_bulk_partial_update(client):
    """Test case for ipam_fhrp_group_assignments_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","interface_id":2147483647,"created":"2000-01-23T04:56:07.000+00:00","display":"display","id":6,"interface":"{}","interface_type":"interface_type","priority":152,"url":"https://openapi-generator.tech","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/fhrp-group-assignments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_bulk_update(client):
    """Test case for ipam_fhrp_group_assignments_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","interface_id":2147483647,"created":"2000-01-23T04:56:07.000+00:00","display":"display","id":6,"interface":"{}","interface_type":"interface_type","priority":152,"url":"https://openapi-generator.tech","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/fhrp-group-assignments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_create(client):
    """Test case for ipam_fhrp_group_assignments_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","interface_id":2147483647,"created":"2000-01-23T04:56:07.000+00:00","display":"display","id":6,"interface":"{}","interface_type":"interface_type","priority":152,"url":"https://openapi-generator.tech","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/fhrp-group-assignments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_delete(client):
    """Test case for ipam_fhrp_group_assignments_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/fhrp-group-assignments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_list(client):
    """Test case for ipam_fhrp_group_assignments_list

    
    """
    params = [('id', 'id_example'),
                    ('group_id', 'group_id_example'),
                    ('interface_type', 'interface_type_example'),
                    ('interface_id', 'interface_id_example'),
                    ('priority', 'priority_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('device', 'device_example'),
                    ('device_id', 'device_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('interface_type__n', 'interface_type__n_example'),
                    ('interface_id__n', 'interface_id__n_example'),
                    ('interface_id__lte', 'interface_id__lte_example'),
                    ('interface_id__lt', 'interface_id__lt_example'),
                    ('interface_id__gte', 'interface_id__gte_example'),
                    ('interface_id__gt', 'interface_id__gt_example'),
                    ('priority__n', 'priority__n_example'),
                    ('priority__lte', 'priority__lte_example'),
                    ('priority__lt', 'priority__lt_example'),
                    ('priority__gte', 'priority__gte_example'),
                    ('priority__gt', 'priority__gt_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/fhrp-group-assignments/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_partial_update(client):
    """Test case for ipam_fhrp_group_assignments_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","interface_id":2147483647,"created":"2000-01-23T04:56:07.000+00:00","display":"display","id":6,"interface":"{}","interface_type":"interface_type","priority":152,"url":"https://openapi-generator.tech","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/fhrp-group-assignments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_read(client):
    """Test case for ipam_fhrp_group_assignments_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/fhrp-group-assignments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_group_assignments_update(client):
    """Test case for ipam_fhrp_group_assignments_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","interface_id":2147483647,"created":"2000-01-23T04:56:07.000+00:00","display":"display","id":6,"interface":"{}","interface_type":"interface_type","priority":152,"url":"https://openapi-generator.tech","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/fhrp-group-assignments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_bulk_delete(client):
    """Test case for ipam_fhrp_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/fhrp-groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_bulk_partial_update(client):
    """Test case for ipam_fhrp_groups_bulk_partial_update

    
    """
    body = {"auth_type":"plaintext","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","ip_addresses":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"display":"display","description":"description","auth_key":"auth_key","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"vrrp2","group_id":19750,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/fhrp-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_bulk_update(client):
    """Test case for ipam_fhrp_groups_bulk_update

    
    """
    body = {"auth_type":"plaintext","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","ip_addresses":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"display":"display","description":"description","auth_key":"auth_key","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"vrrp2","group_id":19750,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/fhrp-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_create(client):
    """Test case for ipam_fhrp_groups_create

    
    """
    body = {"auth_type":"plaintext","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","ip_addresses":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"display":"display","description":"description","auth_key":"auth_key","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"vrrp2","group_id":19750,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/fhrp-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_delete(client):
    """Test case for ipam_fhrp_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/fhrp-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_list(client):
    """Test case for ipam_fhrp_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('group_id', 'group_id_example'),
                    ('name', 'name_example'),
                    ('auth_key', 'auth_key_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('protocol', 'protocol_example'),
                    ('auth_type', 'auth_type_example'),
                    ('related_ip', 'related_ip_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group_id__lte', 'group_id__lte_example'),
                    ('group_id__lt', 'group_id__lt_example'),
                    ('group_id__gte', 'group_id__gte_example'),
                    ('group_id__gt', 'group_id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('auth_key__n', 'auth_key__n_example'),
                    ('auth_key__ic', 'auth_key__ic_example'),
                    ('auth_key__nic', 'auth_key__nic_example'),
                    ('auth_key__iew', 'auth_key__iew_example'),
                    ('auth_key__niew', 'auth_key__niew_example'),
                    ('auth_key__isw', 'auth_key__isw_example'),
                    ('auth_key__nisw', 'auth_key__nisw_example'),
                    ('auth_key__ie', 'auth_key__ie_example'),
                    ('auth_key__nie', 'auth_key__nie_example'),
                    ('auth_key__empty', 'auth_key__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('protocol__n', 'protocol__n_example'),
                    ('auth_type__n', 'auth_type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/fhrp-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_partial_update(client):
    """Test case for ipam_fhrp_groups_partial_update

    
    """
    body = {"auth_type":"plaintext","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","ip_addresses":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"display":"display","description":"description","auth_key":"auth_key","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"vrrp2","group_id":19750,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/fhrp-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_read(client):
    """Test case for ipam_fhrp_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/fhrp-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_fhrp_groups_update(client):
    """Test case for ipam_fhrp_groups_update

    
    """
    body = {"auth_type":"plaintext","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","ip_addresses":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"display":"display","description":"description","auth_key":"auth_key","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"vrrp2","group_id":19750,"name":"name","id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/fhrp-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_bulk_delete(client):
    """Test case for ipam_ip_addresses_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/ip-addresses/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_bulk_partial_update(client):
    """Test case for ipam_ip_addresses_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","role":"loopback","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","assigned_object_type":"assigned_object_type","vrf":5,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","dns_name":"dns_name","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"nat_outside":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"id":6,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/ip-addresses/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_bulk_update(client):
    """Test case for ipam_ip_addresses_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","role":"loopback","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","assigned_object_type":"assigned_object_type","vrf":5,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","dns_name":"dns_name","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"nat_outside":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"id":6,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/ip-addresses/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_addresses_create(client):
    """Test case for ipam_ip_addresses_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","role":"loopback","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","assigned_object_type":"assigned_object_type","vrf":5,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","dns_name":"dns_name","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"nat_outside":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"id":6,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
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
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('family', 3.4),
                    ('parent', 'parent_example'),
                    ('address', 'address_example'),
                    ('mask_length', 3.4),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('present_in_vrf_id', 'present_in_vrf_id_example'),
                    ('present_in_vrf', 'present_in_vrf_example'),
                    ('device', 'device_example'),
                    ('device_id', 'device_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('interface', 'interface_example'),
                    ('interface_id', 'interface_id_example'),
                    ('vminterface', 'vminterface_example'),
                    ('vminterface_id', 'vminterface_id_example'),
                    ('fhrpgroup_id', 'fhrpgroup_id_example'),
                    ('assigned_to_interface', 'assigned_to_interface_example'),
                    ('status', 'status_example'),
                    ('role', 'role_example'),
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
                    ('dns_name__empty', 'dns_name__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('vrf_id__n', 'vrf_id__n_example'),
                    ('vrf__n', 'vrf__n_example'),
                    ('interface__n', 'interface__n_example'),
                    ('interface_id__n', 'interface_id__n_example'),
                    ('vminterface__n', 'vminterface__n_example'),
                    ('vminterface_id__n', 'vminterface_id__n_example'),
                    ('fhrpgroup_id__n', 'fhrpgroup_id__n_example'),
                    ('status__n', 'status__n_example'),
                    ('role__n', 'role__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","role":"loopback","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","assigned_object_type":"assigned_object_type","vrf":5,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","dns_name":"dns_name","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"nat_outside":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"id":6,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","role":"loopback","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","assigned_object_type":"assigned_object_type","vrf":5,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","dns_name":"dns_name","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"nat_outside":[{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"},{"address":"address","display":"display","id":5,"family":4,"url":"https://openapi-generator.tech"}],"id":6,"family":"family","tenant":5,"nat_inside":1,"status":"active"}
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

async def test_ipam_ip_ranges_available_ips_create(client):
    """Test case for ipam_ip_ranges_available_ips_create

    
    """
    body = {"address":"address","family":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/ip-ranges/{id}/available-ips'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_available_ips_list(client):
    """Test case for ipam_ip_ranges_available_ips_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/ip-ranges/{id}/available-ips'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_bulk_delete(client):
    """Test case for ipam_ip_ranges_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/ip-ranges/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_bulk_partial_update(client):
    """Test case for ipam_ip_ranges_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"size":5,"children":0,"start_address":"start_address","end_address":"end_address","id":6,"family":"family","tenant":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/ip-ranges/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_bulk_update(client):
    """Test case for ipam_ip_ranges_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"size":5,"children":0,"start_address":"start_address","end_address":"end_address","id":6,"family":"family","tenant":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/ip-ranges/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_create(client):
    """Test case for ipam_ip_ranges_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"size":5,"children":0,"start_address":"start_address","end_address":"end_address","id":6,"family":"family","tenant":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/ip-ranges/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_delete(client):
    """Test case for ipam_ip_ranges_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/ip-ranges/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_list(client):
    """Test case for ipam_ip_ranges_list

    
    """
    params = [('id', 'id_example'),
                    ('description', 'description_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('family', 3.4),
                    ('start_address', 'start_address_example'),
                    ('end_address', 'end_address_example'),
                    ('contains', 'contains_example'),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('status', 'status_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('vrf_id__n', 'vrf_id__n_example'),
                    ('vrf__n', 'vrf__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('status__n', 'status__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/ip-ranges/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_partial_update(client):
    """Test case for ipam_ip_ranges_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"size":5,"children":0,"start_address":"start_address","end_address":"end_address","id":6,"family":"family","tenant":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/ip-ranges/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_read(client):
    """Test case for ipam_ip_ranges_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/ip-ranges/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_ip_ranges_update(client):
    """Test case for ipam_ip_ranges_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":1,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"size":5,"children":0,"start_address":"start_address","end_address":"end_address","id":6,"family":"family","tenant":5,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/ip-ranges/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_bulk_delete(client):
    """Test case for ipam_l2vpn_terminations_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/l2vpn-terminations/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_bulk_partial_update(client):
    """Test case for ipam_l2vpn_terminations_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn":1,"assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","assigned_object_type":"assigned_object_type","id":6,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/l2vpn-terminations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_bulk_update(client):
    """Test case for ipam_l2vpn_terminations_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn":1,"assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","assigned_object_type":"assigned_object_type","id":6,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/l2vpn-terminations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_create(client):
    """Test case for ipam_l2vpn_terminations_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn":1,"assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","assigned_object_type":"assigned_object_type","id":6,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/l2vpn-terminations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_delete(client):
    """Test case for ipam_l2vpn_terminations_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/l2vpn-terminations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_list(client):
    """Test case for ipam_l2vpn_terminations_list

    
    """
    params = [('id', 'id_example'),
                    ('assigned_object_type_id', 'assigned_object_type_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('l2vpn_id', 'l2vpn_id_example'),
                    ('l2vpn', 'l2vpn_example'),
                    ('region', 'region_example'),
                    ('region_id', 'region_id_example'),
                    ('site', 'site_example'),
                    ('site_id', 'site_id_example'),
                    ('device', 'device_example'),
                    ('device_id', 'device_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('interface', 'interface_example'),
                    ('interface_id', 'interface_id_example'),
                    ('vminterface', 'vminterface_example'),
                    ('vminterface_id', 'vminterface_id_example'),
                    ('vlan', 'vlan_example'),
                    ('vlan_vid', 3.4),
                    ('vlan_id', 'vlan_id_example'),
                    ('assigned_object_type', 'assigned_object_type_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('assigned_object_type_id__n', 'assigned_object_type_id__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('l2vpn_id__n', 'l2vpn_id__n_example'),
                    ('l2vpn__n', 'l2vpn__n_example'),
                    ('device__n', 'device__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('virtual_machine__n', 'virtual_machine__n_example'),
                    ('virtual_machine_id__n', 'virtual_machine_id__n_example'),
                    ('interface__n', 'interface__n_example'),
                    ('interface_id__n', 'interface_id__n_example'),
                    ('vminterface__n', 'vminterface__n_example'),
                    ('vminterface_id__n', 'vminterface_id__n_example'),
                    ('vlan__n', 'vlan__n_example'),
                    ('vlan_vid__n', 3.4),
                    ('vlan_vid__lte', 3.4),
                    ('vlan_vid__lt', 3.4),
                    ('vlan_vid__gte', 3.4),
                    ('vlan_vid__gt', 3.4),
                    ('vlan_id__n', 'vlan_id__n_example'),
                    ('assigned_object_type__n', 'assigned_object_type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/l2vpn-terminations/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_partial_update(client):
    """Test case for ipam_l2vpn_terminations_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn":1,"assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","assigned_object_type":"assigned_object_type","id":6,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/l2vpn-terminations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_read(client):
    """Test case for ipam_l2vpn_terminations_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/l2vpn-terminations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpn_terminations_update(client):
    """Test case for ipam_l2vpn_terminations_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn":1,"assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","assigned_object_type":"assigned_object_type","id":6,"assigned_object_id":2147483647,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/l2vpn-terminations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_bulk_delete(client):
    """Test case for ipam_l2vpns_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/l2vpns/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_bulk_partial_update(client):
    """Test case for ipam_l2vpns_bulk_partial_update

    
    """
    body = {"identifier":-2147483648,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":"vpws","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[5,5],"export_targets":[0,0],"name":"name","id":6,"slug":"slug","tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/l2vpns/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_bulk_update(client):
    """Test case for ipam_l2vpns_bulk_update

    
    """
    body = {"identifier":-2147483648,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":"vpws","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[5,5],"export_targets":[0,0],"name":"name","id":6,"slug":"slug","tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/l2vpns/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_create(client):
    """Test case for ipam_l2vpns_create

    
    """
    body = {"identifier":-2147483648,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":"vpws","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[5,5],"export_targets":[0,0],"name":"name","id":6,"slug":"slug","tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/l2vpns/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_delete(client):
    """Test case for ipam_l2vpns_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/l2vpns/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_list(client):
    """Test case for ipam_l2vpns_list

    
    """
    params = [('id', 'id_example'),
                    ('identifier', 'identifier_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('type', 'type_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('import_target_id', 'import_target_id_example'),
                    ('import_target', 'import_target_example'),
                    ('export_target_id', 'export_target_id_example'),
                    ('export_target', 'export_target_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('identifier__n', 'identifier__n_example'),
                    ('identifier__lte', 'identifier__lte_example'),
                    ('identifier__lt', 'identifier__lt_example'),
                    ('identifier__gte', 'identifier__gte_example'),
                    ('identifier__gt', 'identifier__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('import_target_id__n', 'import_target_id__n_example'),
                    ('import_target__n', 'import_target__n_example'),
                    ('export_target_id__n', 'export_target_id__n_example'),
                    ('export_target__n', 'export_target__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/l2vpns/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_partial_update(client):
    """Test case for ipam_l2vpns_partial_update

    
    """
    body = {"identifier":-2147483648,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":"vpws","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[5,5],"export_targets":[0,0],"name":"name","id":6,"slug":"slug","tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/l2vpns/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_read(client):
    """Test case for ipam_l2vpns_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/l2vpns/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_l2vpns_update(client):
    """Test case for ipam_l2vpns_update

    
    """
    body = {"identifier":-2147483648,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":"vpws","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[5,5],"export_targets":[0,0],"name":"name","id":6,"slug":"slug","tenant":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/l2vpns/{id}'.format(id=56),
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

async def test_ipam_prefixes_available_ips_list(client):
    """Test case for ipam_prefixes_available_ips_list

    
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
    body = {"prefix_length":0}
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

async def test_ipam_prefixes_available_prefixes_list(client):
    """Test case for ipam_prefixes_available_prefixes_list

    
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

async def test_ipam_prefixes_bulk_delete(client):
    """Test case for ipam_prefixes_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/prefixes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_bulk_partial_update(client):
    """Test case for ipam_prefixes_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","_depth":0,"description":"description","is_pool":True,"vrf":9,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mark_utilized":True,"site":5,"vlan":7,"children":6,"id":1,"family":"family","tenant":2,"status":"container"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/prefixes/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_bulk_update(client):
    """Test case for ipam_prefixes_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","_depth":0,"description":"description","is_pool":True,"vrf":9,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mark_utilized":True,"site":5,"vlan":7,"children":6,"id":1,"family":"family","tenant":2,"status":"container"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/prefixes/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_prefixes_create(client):
    """Test case for ipam_prefixes_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","_depth":0,"description":"description","is_pool":True,"vrf":9,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mark_utilized":True,"site":5,"vlan":7,"children":6,"id":1,"family":"family","tenant":2,"status":"container"}
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
                    ('mark_utilized', 'mark_utilized_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('family', 3.4),
                    ('prefix', 'prefix_example'),
                    ('within', 'within_example'),
                    ('within_include', 'within_include_example'),
                    ('contains', 'contains_example'),
                    ('depth', 'depth_example'),
                    ('children', 'children_example'),
                    ('mask_length', 'mask_length_example'),
                    ('mask_length__gte', 3.4),
                    ('mask_length__lte', 3.4),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('present_in_vrf_id', 'present_in_vrf_id_example'),
                    ('present_in_vrf', 'present_in_vrf_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('vlan_id', 'vlan_id_example'),
                    ('vlan_vid', 3.4),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('status', 'status_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('depth__n', 'depth__n_example'),
                    ('depth__lte', 'depth__lte_example'),
                    ('depth__lt', 'depth__lt_example'),
                    ('depth__gte', 'depth__gte_example'),
                    ('depth__gt', 'depth__gt_example'),
                    ('children__n', 'children__n_example'),
                    ('children__lte', 'children__lte_example'),
                    ('children__lt', 'children__lt_example'),
                    ('children__gte', 'children__gte_example'),
                    ('children__gt', 'children__gt_example'),
                    ('vrf_id__n', 'vrf_id__n_example'),
                    ('vrf__n', 'vrf__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('vlan_id__n', 'vlan_id__n_example'),
                    ('vlan_vid__n', 3.4),
                    ('vlan_vid__lte', 3.4),
                    ('vlan_vid__lt', 3.4),
                    ('vlan_vid__gte', 3.4),
                    ('vlan_vid__gt', 3.4),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('status__n', 'status__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","_depth":0,"description":"description","is_pool":True,"vrf":9,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mark_utilized":True,"site":5,"vlan":7,"children":6,"id":1,"family":"family","tenant":2,"status":"container"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","prefix":"prefix","display":"display","_depth":0,"description":"description","is_pool":True,"vrf":9,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mark_utilized":True,"site":5,"vlan":7,"children":6,"id":1,"family":"family","tenant":2,"status":"container"}
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

async def test_ipam_rirs_bulk_delete(client):
    """Test case for ipam_rirs_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/rirs/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_bulk_partial_update(client):
    """Test case for ipam_rirs_bulk_partial_update

    
    """
    body = {"is_private":True,"last_updated":"2000-01-23T04:56:07.000+00:00","aggregate_count":6,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/rirs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_bulk_update(client):
    """Test case for ipam_rirs_bulk_update

    
    """
    body = {"is_private":True,"last_updated":"2000-01-23T04:56:07.000+00:00","aggregate_count":6,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/rirs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_rirs_create(client):
    """Test case for ipam_rirs_create

    
    """
    body = {"is_private":True,"last_updated":"2000-01-23T04:56:07.000+00:00","aggregate_count":6,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
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
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"is_private":True,"last_updated":"2000-01-23T04:56:07.000+00:00","aggregate_count":6,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
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
    body = {"is_private":True,"last_updated":"2000-01-23T04:56:07.000+00:00","aggregate_count":6,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
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

async def test_ipam_roles_bulk_delete(client):
    """Test case for ipam_roles_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/roles/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_bulk_partial_update(client):
    """Test case for ipam_roles_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":18471,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":5,"name":"name","prefix_count":1,"id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_bulk_update(client):
    """Test case for ipam_roles_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":18471,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":5,"name":"name","prefix_count":1,"id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_roles_create(client):
    """Test case for ipam_roles_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":18471,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":5,"name":"name","prefix_count":1,"id":6,"slug":"slug"}
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
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":18471,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":5,"name":"name","prefix_count":1,"id":6,"slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","weight":18471,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":5,"name":"name","prefix_count":1,"id":6,"slug":"slug"}
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

async def test_ipam_route_targets_bulk_delete(client):
    """Test case for ipam_route_targets_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/route-targets/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_bulk_partial_update(client):
    """Test case for ipam_route_targets_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"tenant":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/route-targets/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_bulk_update(client):
    """Test case for ipam_route_targets_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"tenant":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/route-targets/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_create(client):
    """Test case for ipam_route_targets_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"tenant":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/route-targets/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_delete(client):
    """Test case for ipam_route_targets_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/route-targets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_list(client):
    """Test case for ipam_route_targets_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('importing_vrf_id', 'importing_vrf_id_example'),
                    ('importing_vrf', 'importing_vrf_example'),
                    ('exporting_vrf_id', 'exporting_vrf_id_example'),
                    ('exporting_vrf', 'exporting_vrf_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('importing_vrf_id__n', 'importing_vrf_id__n_example'),
                    ('importing_vrf__n', 'importing_vrf__n_example'),
                    ('exporting_vrf_id__n', 'exporting_vrf_id__n_example'),
                    ('exporting_vrf__n', 'exporting_vrf__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/route-targets/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_partial_update(client):
    """Test case for ipam_route_targets_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"tenant":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/route-targets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_read(client):
    """Test case for ipam_route_targets_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/route-targets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_route_targets_update(client):
    """Test case for ipam_route_targets_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"tenant":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/route-targets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_bulk_delete(client):
    """Test case for ipam_service_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/service-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_bulk_partial_update(client):
    """Test case for ipam_service_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"ports":[39501,39501],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/service-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_bulk_update(client):
    """Test case for ipam_service_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"ports":[39501,39501],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/service-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_create(client):
    """Test case for ipam_service_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"ports":[39501,39501],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/service-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_delete(client):
    """Test case for ipam_service_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/service-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_list(client):
    """Test case for ipam_service_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('protocol', 'protocol_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('port', 3.4),
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
                    ('name__empty', 'name__empty_example'),
                    ('protocol__n', 'protocol__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/service-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_partial_update(client):
    """Test case for ipam_service_templates_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"ports":[39501,39501],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/service-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_read(client):
    """Test case for ipam_service_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/service-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_service_templates_update(client):
    """Test case for ipam_service_templates_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","protocol":"tcp","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":0,"ports":[39501,39501],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/service-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_bulk_delete(client):
    """Test case for ipam_services_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/services/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_bulk_partial_update(client):
    """Test case for ipam_services_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ports":[39073,39073],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"tcp","ipaddresses":[1,1],"name":"name","virtual_machine":5,"id":6,"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/services/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_bulk_update(client):
    """Test case for ipam_services_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ports":[39073,39073],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"tcp","ipaddresses":[1,1],"name":"name","virtual_machine":5,"id":6,"device":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/services/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_services_create(client):
    """Test case for ipam_services_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ports":[39073,39073],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"tcp","ipaddresses":[1,1],"name":"name","virtual_machine":5,"id":6,"device":0}
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
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('ipaddress_id', 'ipaddress_id_example'),
                    ('ipaddress', 'ipaddress_example'),
                    ('port', 3.4),
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
                    ('name__empty', 'name__empty_example'),
                    ('protocol__n', 'protocol__n_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('virtual_machine_id__n', 'virtual_machine_id__n_example'),
                    ('virtual_machine__n', 'virtual_machine__n_example'),
                    ('ipaddress_id__n', 'ipaddress_id__n_example'),
                    ('ipaddress__n', 'ipaddress__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ports":[39073,39073],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"tcp","ipaddresses":[1,1],"name":"name","virtual_machine":5,"id":6,"device":0}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ports":[39073,39073],"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"protocol":"tcp","ipaddresses":[1,1],"name":"name","virtual_machine":5,"id":6,"device":0}
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

async def test_ipam_vlan_groups_available_vlans_create(client):
    """Test case for ipam_vlan_groups_available_vlans_create

    
    """
    body = {"site":6,"role":0,"custom_fields":"{}","name":"name","description":"description","tenant":1,"status":"active","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ipam/vlan-groups/{id}/available-vlans'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_available_vlans_list(client):
    """Test case for ipam_vlan_groups_available_vlans_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ipam/vlan-groups/{id}/available-vlans'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_bulk_delete(client):
    """Test case for ipam_vlan_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/vlan-groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_bulk_partial_update(client):
    """Test case for ipam_vlan_groups_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","max_vid":600,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","min_vid":2441,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":2,"scope_id":5,"scope":"{}","name":"name","id":6,"scope_type":"scope_type","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/vlan-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_bulk_update(client):
    """Test case for ipam_vlan_groups_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","max_vid":600,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","min_vid":2441,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":2,"scope_id":5,"scope":"{}","name":"name","id":6,"scope_type":"scope_type","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/vlan-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlan_groups_create(client):
    """Test case for ipam_vlan_groups_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","max_vid":600,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","min_vid":2441,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":2,"scope_id":5,"scope":"{}","name":"name","id":6,"scope_type":"scope_type","slug":"slug"}
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
                    ('min_vid', 'min_vid_example'),
                    ('max_vid', 'max_vid_example'),
                    ('description', 'description_example'),
                    ('scope_id', 'scope_id_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('scope_type', 'scope_type_example'),
                    ('region', 3.4),
                    ('sitegroup', 3.4),
                    ('site', 3.4),
                    ('location', 3.4),
                    ('rack', 3.4),
                    ('clustergroup', 3.4),
                    ('cluster', 3.4),
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
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('min_vid__n', 'min_vid__n_example'),
                    ('min_vid__lte', 'min_vid__lte_example'),
                    ('min_vid__lt', 'min_vid__lt_example'),
                    ('min_vid__gte', 'min_vid__gte_example'),
                    ('min_vid__gt', 'min_vid__gt_example'),
                    ('max_vid__n', 'max_vid__n_example'),
                    ('max_vid__lte', 'max_vid__lte_example'),
                    ('max_vid__lt', 'max_vid__lt_example'),
                    ('max_vid__gte', 'max_vid__gte_example'),
                    ('max_vid__gt', 'max_vid__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('scope_id__n', 'scope_id__n_example'),
                    ('scope_id__lte', 'scope_id__lte_example'),
                    ('scope_id__lt', 'scope_id__lt_example'),
                    ('scope_id__gte', 'scope_id__gte_example'),
                    ('scope_id__gt', 'scope_id__gt_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('scope_type__n', 'scope_type__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","max_vid":600,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","min_vid":2441,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":2,"scope_id":5,"scope":"{}","name":"name","id":6,"scope_type":"scope_type","slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","max_vid":600,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","min_vid":2441,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":2,"scope_id":5,"scope":"{}","name":"name","id":6,"scope_type":"scope_type","slug":"slug"}
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

async def test_ipam_vlans_bulk_delete(client):
    """Test case for ipam_vlans_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/vlans/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_bulk_partial_update(client):
    """Test case for ipam_vlans_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","l2vpn_termination":"l2vpn_termination","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/vlans/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_bulk_update(client):
    """Test case for ipam_vlans_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","l2vpn_termination":"l2vpn_termination","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/vlans/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vlans_create(client):
    """Test case for ipam_vlans_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","l2vpn_termination":"l2vpn_termination","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
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
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('status', 'status_example'),
                    ('available_on_device', 'available_on_device_example'),
                    ('available_on_virtualmachine', 'available_on_virtualmachine_example'),
                    ('l2vpn_id', 'l2vpn_id_example'),
                    ('l2vpn', 'l2vpn_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('status__n', 'status__n_example'),
                    ('l2vpn_id__n', 'l2vpn_id__n_example'),
                    ('l2vpn__n', 'l2vpn__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","l2vpn_termination":"l2vpn_termination","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","l2vpn_termination":"l2vpn_termination","role":5,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vid":2891,"site":5,"name":"name","prefix_count":1,"id":6,"tenant":2,"group":0,"status":"active"}
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

async def test_ipam_vrfs_bulk_delete(client):
    """Test case for ipam_vrfs_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/ipam/vrfs/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_bulk_partial_update(client):
    """Test case for ipam_vrfs_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","ipaddress_count":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[1,1],"rd":"rd","export_targets":[0,0],"name":"name","enforce_unique":True,"prefix_count":5,"id":6,"tenant":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/ipam/vrfs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_bulk_update(client):
    """Test case for ipam_vrfs_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","ipaddress_count":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[1,1],"rd":"rd","export_targets":[0,0],"name":"name","enforce_unique":True,"prefix_count":5,"id":6,"tenant":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ipam/vrfs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ipam_vrfs_create(client):
    """Test case for ipam_vrfs_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","ipaddress_count":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[1,1],"rd":"rd","export_targets":[0,0],"name":"name","enforce_unique":True,"prefix_count":5,"id":6,"tenant":2}
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
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('import_target_id', 'import_target_id_example'),
                    ('import_target', 'import_target_example'),
                    ('export_target_id', 'export_target_id_example'),
                    ('export_target', 'export_target_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('rd__n', 'rd__n_example'),
                    ('rd__ic', 'rd__ic_example'),
                    ('rd__nic', 'rd__nic_example'),
                    ('rd__iew', 'rd__iew_example'),
                    ('rd__niew', 'rd__niew_example'),
                    ('rd__isw', 'rd__isw_example'),
                    ('rd__nisw', 'rd__nisw_example'),
                    ('rd__ie', 'rd__ie_example'),
                    ('rd__nie', 'rd__nie_example'),
                    ('rd__empty', 'rd__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('import_target_id__n', 'import_target_id__n_example'),
                    ('import_target__n', 'import_target__n_example'),
                    ('export_target_id__n', 'export_target_id__n_example'),
                    ('export_target__n', 'export_target__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","ipaddress_count":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[1,1],"rd":"rd","export_targets":[0,0],"name":"name","enforce_unique":True,"prefix_count":5,"id":6,"tenant":2}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","url":"https://openapi-generator.tech","ipaddress_count":5,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"import_targets":[1,1],"rd":"rd","export_targets":[0,0],"name":"name","enforce_unique":True,"prefix_count":5,"id":6,"tenant":2}
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

