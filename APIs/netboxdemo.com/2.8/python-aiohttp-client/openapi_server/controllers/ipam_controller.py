from typing import List, Dict
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


async def ipam_aggregates_list(request: web.Request, id=None, date_added=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, family=None, prefix=None, rir_id=None, rir=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, date_added__n=None, date_added__lte=None, date_added__lt=None, date_added__gte=None, date_added__gt=None, rir_id__n=None, rir__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """ipam_aggregates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param date_added: 
    :type date_added: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param family: 
    :type family: 
    :param prefix: 
    :type prefix: str
    :param rir_id: 
    :type rir_id: str
    :param rir: 
    :type rir: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param date_added__n: 
    :type date_added__n: str
    :param date_added__lte: 
    :type date_added__lte: str
    :param date_added__lt: 
    :type date_added__lt: str
    :param date_added__gte: 
    :type date_added__gte: str
    :param date_added__gt: 
    :type date_added__gt: str
    :param rir_id__n: 
    :type rir_id__n: str
    :param rir__n: 
    :type rir__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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


async def ipam_ip_addresses_list(request: web.Request, id=None, dns_name=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, family=None, parent=None, address=None, mask_length=None, vrf_id=None, vrf=None, device=None, device_id=None, virtual_machine_id=None, virtual_machine=None, interface=None, interface_id=None, assigned_to_interface=None, status=None, role=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, dns_name__n=None, dns_name__ic=None, dns_name__nic=None, dns_name__iew=None, dns_name__niew=None, dns_name__isw=None, dns_name__nisw=None, dns_name__ie=None, dns_name__nie=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, vrf_id__n=None, vrf__n=None, virtual_machine_id__n=None, virtual_machine__n=None, interface__n=None, interface_id__n=None, status__n=None, role__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """ipam_ip_addresses_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param dns_name: 
    :type dns_name: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param family: 
    :type family: 
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
    :param device: 
    :type device: str
    :param device_id: 
    :type device_id: str
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param interface: 
    :type interface: str
    :param interface_id: 
    :type interface_id: str
    :param assigned_to_interface: 
    :type assigned_to_interface: str
    :param status: 
    :type status: str
    :param role: 
    :type role: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param dns_name__n: 
    :type dns_name__n: str
    :param dns_name__ic: 
    :type dns_name__ic: str
    :param dns_name__nic: 
    :type dns_name__nic: str
    :param dns_name__iew: 
    :type dns_name__iew: str
    :param dns_name__niew: 
    :type dns_name__niew: str
    :param dns_name__isw: 
    :type dns_name__isw: str
    :param dns_name__nisw: 
    :type dns_name__nisw: str
    :param dns_name__ie: 
    :type dns_name__ie: str
    :param dns_name__nie: 
    :type dns_name__nie: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param vrf_id__n: 
    :type vrf_id__n: str
    :param vrf__n: 
    :type vrf__n: str
    :param virtual_machine_id__n: 
    :type virtual_machine_id__n: str
    :param virtual_machine__n: 
    :type virtual_machine__n: str
    :param interface__n: 
    :type interface__n: str
    :param interface_id__n: 
    :type interface_id__n: str
    :param status__n: 
    :type status__n: str
    :param role__n: 
    :type role__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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

    A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

    :param id: A unique integer value identifying this prefix.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableAvailableIP.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_ips_read(request: web.Request, id) -> web.Response:
    """ipam_prefixes_available_ips_read

    A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

    :param id: A unique integer value identifying this prefix.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_prefixes_available_prefixes_create(request: web.Request, id, body) -> web.Response:
    """A convenience method for returning available child prefixes within a parent.

    The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

    :param id: A unique integer value identifying this prefix.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_prefixes_read(request: web.Request, id) -> web.Response:
    """A convenience method for returning available child prefixes within a parent.

    The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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


async def ipam_prefixes_list(request: web.Request, id=None, is_pool=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, family=None, prefix=None, within=None, within_include=None, contains=None, mask_length=None, vrf_id=None, vrf=None, region_id=None, region=None, site_id=None, site=None, vlan_id=None, vlan_vid=None, role_id=None, role=None, status=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, vrf_id__n=None, vrf__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, vlan_id__n=None, role_id__n=None, role__n=None, status__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """ipam_prefixes_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param is_pool: 
    :type is_pool: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param family: 
    :type family: 
    :param prefix: 
    :type prefix: str
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
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
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
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param vrf_id__n: 
    :type vrf_id__n: str
    :param vrf__n: 
    :type vrf__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param vlan_id__n: 
    :type vlan_id__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param status__n: 
    :type status__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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


async def ipam_rirs_list(request: web.Request, id=None, name=None, slug=None, is_private=None, description=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, limit=None, offset=None) -> web.Response:
    """ipam_rirs_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param is_private: 
    :type is_private: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
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

    Call to super to allow for caching

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


async def ipam_roles_list(request: web.Request, id=None, name=None, slug=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, limit=None, offset=None) -> web.Response:
    """ipam_roles_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
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

    Call to super to allow for caching

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


async def ipam_services_list(request: web.Request, id=None, name=None, protocol=None, port=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, device_id=None, device=None, virtual_machine_id=None, virtual_machine=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, protocol__n=None, port__n=None, port__lte=None, port__lt=None, port__gte=None, port__gt=None, device_id__n=None, device__n=None, virtual_machine_id__n=None, virtual_machine__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """ipam_services_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param protocol: 
    :type protocol: str
    :param port: 
    :type port: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
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
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param protocol__n: 
    :type protocol__n: str
    :param port__n: 
    :type port__n: str
    :param port__lte: 
    :type port__lte: str
    :param port__lt: 
    :type port__lt: str
    :param port__gte: 
    :type port__gte: str
    :param port__gt: 
    :type port__gt: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_machine_id__n: 
    :type virtual_machine_id__n: str
    :param virtual_machine__n: 
    :type virtual_machine__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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


async def ipam_vlan_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, q=None, region_id=None, region=None, site_id=None, site=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, limit=None, offset=None) -> web.Response:
    """ipam_vlan_groups_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
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

    Call to super to allow for caching

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


async def ipam_vlans_list(request: web.Request, id=None, vid=None, name=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, region_id=None, region=None, site_id=None, site=None, group_id=None, group=None, role_id=None, role=None, status=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, vid__n=None, vid__lte=None, vid__lt=None, vid__gte=None, vid__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, group_id__n=None, group__n=None, role_id__n=None, role__n=None, status__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """ipam_vlans_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param vid: 
    :type vid: str
    :param name: 
    :type name: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param status: 
    :type status: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param vid__n: 
    :type vid__n: str
    :param vid__lte: 
    :type vid__lte: str
    :param vid__lt: 
    :type vid__lt: str
    :param vid__gte: 
    :type vid__gte: str
    :param vid__gt: 
    :type vid__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param status__n: 
    :type status__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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


async def ipam_vrfs_list(request: web.Request, id=None, name=None, rd=None, enforce_unique=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, rd__n=None, rd__ic=None, rd__nic=None, rd__iew=None, rd__niew=None, rd__isw=None, rd__nisw=None, rd__ie=None, rd__nie=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """ipam_vrfs_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param rd: 
    :type rd: str
    :param enforce_unique: 
    :type enforce_unique: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param rd__n: 
    :type rd__n: str
    :param rd__ic: 
    :type rd__ic: str
    :param rd__nic: 
    :type rd__nic: str
    :param rd__iew: 
    :type rd__iew: str
    :param rd__niew: 
    :type rd__niew: str
    :param rd__isw: 
    :type rd__isw: str
    :param rd__nisw: 
    :type rd__nisw: str
    :param rd__ie: 
    :type rd__ie: str
    :param rd__nie: 
    :type rd__nie: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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
