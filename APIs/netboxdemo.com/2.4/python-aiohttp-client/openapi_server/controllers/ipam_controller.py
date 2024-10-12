from typing import List, Dict
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
from openapi_server import util


async def ipam_aggregates_create(request: web.Request, body) -> web.Response:
    """ipam_aggregates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableAggregate.from_dict(body)
    return web.Response(status=200)


async def ipam_aggregates_delete(request: web.Request, id) -> web.Response:
    """ipam_aggregates_delete

    

    :param id: A unique integer value identifying this aggregate.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_aggregates_list(request: web.Request, family=None, date_added=None, id__in=None, q=None, rir_id=None, rir=None, tag=None, limit=None, offset=None) -> web.Response:
    """ipam_aggregates_list

    

    :param family: 
    :type family: str
    :param date_added: 
    :type date_added: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param rir_id: 
    :type rir_id: str
    :param rir: 
    :type rir: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_aggregates_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_aggregates_partial_update

    

    :param id: A unique integer value identifying this aggregate.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableAggregate.from_dict(body)
    return web.Response(status=200)


async def ipam_aggregates_read(request: web.Request, id) -> web.Response:
    """ipam_aggregates_read

    

    :param id: A unique integer value identifying this aggregate.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_aggregates_update(request: web.Request, id, body) -> web.Response:
    """ipam_aggregates_update

    

    :param id: A unique integer value identifying this aggregate.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableAggregate.from_dict(body)
    return web.Response(status=200)


async def ipam_choices_list(request: web.Request, ) -> web.Response:
    """ipam_choices_list

    


    """
    return web.Response(status=200)


async def ipam_choices_read(request: web.Request, id) -> web.Response:
    """ipam_choices_read

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def ipam_ip_addresses_create(request: web.Request, body) -> web.Response:
    """ipam_ip_addresses_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPAddress.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_addresses_delete(request: web.Request, id) -> web.Response:
    """ipam_ip_addresses_delete

    

    :param id: A unique integer value identifying this IP address.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_ip_addresses_list(request: web.Request, family=None, id__in=None, q=None, parent=None, address=None, mask_length=None, vrf_id=None, vrf=None, tenant_id=None, tenant=None, device=None, device_id=None, virtual_machine_id=None, virtual_machine=None, interface_id=None, status=None, role=None, tag=None, limit=None, offset=None) -> web.Response:
    """ipam_ip_addresses_list

    

    :param family: 
    :type family: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param parent: 
    :type parent: str
    :param address: 
    :type address: str
    :param mask_length: 
    :type mask_length: 
    :param vrf_id: 
    :type vrf_id: str
    :param vrf: 
    :type vrf: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param device: 
    :type device: str
    :param device_id: 
    :type device_id: 
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param interface_id: 
    :type interface_id: str
    :param status: 
    :type status: str
    :param role: 
    :type role: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_ip_addresses_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_ip_addresses_partial_update

    

    :param id: A unique integer value identifying this IP address.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPAddress.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_addresses_read(request: web.Request, id) -> web.Response:
    """ipam_ip_addresses_read

    

    :param id: A unique integer value identifying this IP address.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_ip_addresses_update(request: web.Request, id, body) -> web.Response:
    """ipam_ip_addresses_update

    

    :param id: A unique integer value identifying this IP address.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPAddress.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_ips_create(request: web.Request, id, body) -> web.Response:
    """ipam_prefixes_available_ips_create

    A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

    :param id: A unique integer value identifying this prefix.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_ips_read(request: web.Request, id) -> web.Response:
    """ipam_prefixes_available_ips_read

    A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

    :param id: A unique integer value identifying this prefix.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_prefixes_available_prefixes_create(request: web.Request, id, body) -> web.Response:
    """ipam_prefixes_available_prefixes_create

    A convenience method for returning available child prefixes within a parent.

    :param id: A unique integer value identifying this prefix.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_prefixes_read(request: web.Request, id) -> web.Response:
    """ipam_prefixes_available_prefixes_read

    A convenience method for returning available child prefixes within a parent.

    :param id: A unique integer value identifying this prefix.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_prefixes_create(request: web.Request, body) -> web.Response:
    """ipam_prefixes_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_delete(request: web.Request, id) -> web.Response:
    """ipam_prefixes_delete

    

    :param id: A unique integer value identifying this prefix.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_prefixes_list(request: web.Request, family=None, is_pool=None, id__in=None, q=None, within=None, within_include=None, contains=None, mask_length=None, vrf_id=None, vrf=None, tenant_id=None, tenant=None, site_id=None, site=None, vlan_id=None, vlan_vid=None, role_id=None, role=None, status=None, tag=None, limit=None, offset=None) -> web.Response:
    """ipam_prefixes_list

    

    :param family: 
    :type family: str
    :param is_pool: 
    :type is_pool: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param within: 
    :type within: str
    :param within_include: 
    :type within_include: str
    :param contains: 
    :type contains: str
    :param mask_length: 
    :type mask_length: 
    :param vrf_id: 
    :type vrf_id: str
    :param vrf: 
    :type vrf: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param vlan_id: 
    :type vlan_id: str
    :param vlan_vid: 
    :type vlan_vid: 
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param status: 
    :type status: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_prefixes_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_prefixes_partial_update

    

    :param id: A unique integer value identifying this prefix.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_read(request: web.Request, id) -> web.Response:
    """ipam_prefixes_read

    

    :param id: A unique integer value identifying this prefix.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_prefixes_update(request: web.Request, id, body) -> web.Response:
    """ipam_prefixes_update

    

    :param id: A unique integer value identifying this prefix.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
    return web.Response(status=200)


async def ipam_rirs_create(request: web.Request, body) -> web.Response:
    """ipam_rirs_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = RIR.from_dict(body)
    return web.Response(status=200)


async def ipam_rirs_delete(request: web.Request, id) -> web.Response:
    """ipam_rirs_delete

    

    :param id: A unique integer value identifying this RIR.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_rirs_list(request: web.Request, name=None, slug=None, is_private=None, id__in=None, limit=None, offset=None) -> web.Response:
    """ipam_rirs_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param is_private: 
    :type is_private: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_rirs_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_rirs_partial_update

    

    :param id: A unique integer value identifying this RIR.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RIR.from_dict(body)
    return web.Response(status=200)


async def ipam_rirs_read(request: web.Request, id) -> web.Response:
    """ipam_rirs_read

    

    :param id: A unique integer value identifying this RIR.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_rirs_update(request: web.Request, id, body) -> web.Response:
    """ipam_rirs_update

    

    :param id: A unique integer value identifying this RIR.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RIR.from_dict(body)
    return web.Response(status=200)


async def ipam_roles_create(request: web.Request, body) -> web.Response:
    """ipam_roles_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = Role.from_dict(body)
    return web.Response(status=200)


async def ipam_roles_delete(request: web.Request, id) -> web.Response:
    """ipam_roles_delete

    

    :param id: A unique integer value identifying this role.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_roles_list(request: web.Request, name=None, slug=None, limit=None, offset=None) -> web.Response:
    """ipam_roles_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_roles_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_roles_partial_update

    

    :param id: A unique integer value identifying this role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Role.from_dict(body)
    return web.Response(status=200)


async def ipam_roles_read(request: web.Request, id) -> web.Response:
    """ipam_roles_read

    

    :param id: A unique integer value identifying this role.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_roles_update(request: web.Request, id, body) -> web.Response:
    """ipam_roles_update

    

    :param id: A unique integer value identifying this role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Role.from_dict(body)
    return web.Response(status=200)


async def ipam_services_create(request: web.Request, body) -> web.Response:
    """ipam_services_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableService.from_dict(body)
    return web.Response(status=200)


async def ipam_services_delete(request: web.Request, id) -> web.Response:
    """ipam_services_delete

    

    :param id: A unique integer value identifying this service.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_services_list(request: web.Request, name=None, protocol=None, port=None, q=None, device_id=None, device=None, virtual_machine_id=None, virtual_machine=None, tag=None, limit=None, offset=None) -> web.Response:
    """ipam_services_list

    

    :param name: 
    :type name: str
    :param protocol: 
    :type protocol: str
    :param port: 
    :type port: 
    :param q: 
    :type q: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_services_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_services_partial_update

    

    :param id: A unique integer value identifying this service.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableService.from_dict(body)
    return web.Response(status=200)


async def ipam_services_read(request: web.Request, id) -> web.Response:
    """ipam_services_read

    

    :param id: A unique integer value identifying this service.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_services_update(request: web.Request, id, body) -> web.Response:
    """ipam_services_update

    

    :param id: A unique integer value identifying this service.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableService.from_dict(body)
    return web.Response(status=200)


async def ipam_vlan_groups_create(request: web.Request, body) -> web.Response:
    """ipam_vlan_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLANGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_vlan_groups_delete(request: web.Request, id) -> web.Response:
    """ipam_vlan_groups_delete

    

    :param id: A unique integer value identifying this VLAN group.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vlan_groups_list(request: web.Request, name=None, slug=None, site_id=None, site=None, limit=None, offset=None) -> web.Response:
    """ipam_vlan_groups_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_vlan_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_vlan_groups_partial_update

    

    :param id: A unique integer value identifying this VLAN group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLANGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_vlan_groups_read(request: web.Request, id) -> web.Response:
    """ipam_vlan_groups_read

    

    :param id: A unique integer value identifying this VLAN group.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vlan_groups_update(request: web.Request, id, body) -> web.Response:
    """ipam_vlan_groups_update

    

    :param id: A unique integer value identifying this VLAN group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLANGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_vlans_create(request: web.Request, body) -> web.Response:
    """ipam_vlans_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLAN.from_dict(body)
    return web.Response(status=200)


async def ipam_vlans_delete(request: web.Request, id) -> web.Response:
    """ipam_vlans_delete

    

    :param id: A unique integer value identifying this VLAN.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vlans_list(request: web.Request, vid=None, name=None, id__in=None, q=None, site_id=None, site=None, group_id=None, group=None, tenant_id=None, tenant=None, role_id=None, role=None, status=None, tag=None, limit=None, offset=None) -> web.Response:
    """ipam_vlans_list

    

    :param vid: 
    :type vid: 
    :param name: 
    :type name: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param status: 
    :type status: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_vlans_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_vlans_partial_update

    

    :param id: A unique integer value identifying this VLAN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLAN.from_dict(body)
    return web.Response(status=200)


async def ipam_vlans_read(request: web.Request, id) -> web.Response:
    """ipam_vlans_read

    

    :param id: A unique integer value identifying this VLAN.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vlans_update(request: web.Request, id, body) -> web.Response:
    """ipam_vlans_update

    

    :param id: A unique integer value identifying this VLAN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLAN.from_dict(body)
    return web.Response(status=200)


async def ipam_vrfs_create(request: web.Request, body) -> web.Response:
    """ipam_vrfs_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVRF.from_dict(body)
    return web.Response(status=200)


async def ipam_vrfs_delete(request: web.Request, id) -> web.Response:
    """ipam_vrfs_delete

    

    :param id: A unique integer value identifying this VRF.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vrfs_list(request: web.Request, name=None, rd=None, enforce_unique=None, id__in=None, q=None, tenant_id=None, tenant=None, tag=None, limit=None, offset=None) -> web.Response:
    """ipam_vrfs_list

    

    :param name: 
    :type name: str
    :param rd: 
    :type rd: str
    :param enforce_unique: 
    :type enforce_unique: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_vrfs_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_vrfs_partial_update

    

    :param id: A unique integer value identifying this VRF.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVRF.from_dict(body)
    return web.Response(status=200)


async def ipam_vrfs_read(request: web.Request, id) -> web.Response:
    """ipam_vrfs_read

    

    :param id: A unique integer value identifying this VRF.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vrfs_update(request: web.Request, id, body) -> web.Response:
    """ipam_vrfs_update

    

    :param id: A unique integer value identifying this VRF.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableVRF.from_dict(body)
    return web.Response(status=200)
