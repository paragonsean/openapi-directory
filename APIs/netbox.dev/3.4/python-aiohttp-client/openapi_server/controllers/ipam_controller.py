from typing import List, Dict
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
from openapi_server import util


async def ipam_aggregates_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_aggregates_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_aggregates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_aggregates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableAggregate.from_dict(body)
    return web.Response(status=200)


async def ipam_aggregates_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_aggregates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableAggregate.from_dict(body)
    return web.Response(status=200)


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


async def ipam_aggregates_list(request: web.Request, id=None, date_added=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, family=None, prefix=None, rir_id=None, rir=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, date_added__n=None, date_added__lte=None, date_added__lt=None, date_added__gte=None, date_added__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, rir_id__n=None, rir__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_aggregates_list

    

    :param id: 
    :type id: str
    :param date_added: 
    :type date_added: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param family: 
    :type family: 
    :param prefix: 
    :type prefix: str
    :param rir_id: 
    :type rir_id: str
    :param rir: 
    :type rir: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param rir_id__n: 
    :type rir_id__n: str
    :param rir__n: 
    :type rir__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def ipam_asns_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_asns_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_asns_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_asns_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableASN.from_dict(body)
    return web.Response(status=200)


async def ipam_asns_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_asns_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableASN.from_dict(body)
    return web.Response(status=200)


async def ipam_asns_create(request: web.Request, body) -> web.Response:
    """ipam_asns_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableASN.from_dict(body)
    return web.Response(status=200)


async def ipam_asns_delete(request: web.Request, id) -> web.Response:
    """ipam_asns_delete

    

    :param id: A unique integer value identifying this ASN.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_asns_list(request: web.Request, id=None, asn=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, rir_id=None, rir=None, site_id=None, site=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, asn__n=None, asn__lte=None, asn__lt=None, asn__gte=None, asn__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, rir_id__n=None, rir__n=None, site_id__n=None, site__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_asns_list

    

    :param id: 
    :type id: str
    :param asn: 
    :type asn: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param rir_id: 
    :type rir_id: str
    :param rir: 
    :type rir: str
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
    :param asn__n: 
    :type asn__n: str
    :param asn__lte: 
    :type asn__lte: str
    :param asn__lt: 
    :type asn__lt: str
    :param asn__gte: 
    :type asn__gte: str
    :param asn__gt: 
    :type asn__gt: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param rir_id__n: 
    :type rir_id__n: str
    :param rir__n: 
    :type rir__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_asns_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_asns_partial_update

    

    :param id: A unique integer value identifying this ASN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableASN.from_dict(body)
    return web.Response(status=200)


async def ipam_asns_read(request: web.Request, id) -> web.Response:
    """ipam_asns_read

    

    :param id: A unique integer value identifying this ASN.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_asns_update(request: web.Request, id, body) -> web.Response:
    """ipam_asns_update

    

    :param id: A unique integer value identifying this ASN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableASN.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_fhrp_group_assignments_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_fhrp_group_assignments_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFHRPGroupAssignment.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_fhrp_group_assignments_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFHRPGroupAssignment.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_create(request: web.Request, body) -> web.Response:
    """ipam_fhrp_group_assignments_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableFHRPGroupAssignment.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_delete(request: web.Request, id) -> web.Response:
    """ipam_fhrp_group_assignments_delete

    

    :param id: A unique integer value identifying this FHRP group assignment.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_list(request: web.Request, id=None, group_id=None, interface_type=None, interface_id=None, priority=None, created=None, last_updated=None, device=None, device_id=None, virtual_machine=None, virtual_machine_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, group_id__n=None, interface_type__n=None, interface_id__n=None, interface_id__lte=None, interface_id__lt=None, interface_id__gte=None, interface_id__gt=None, priority__n=None, priority__lte=None, priority__lt=None, priority__gte=None, priority__gt=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_fhrp_group_assignments_list

    

    :param id: 
    :type id: str
    :param group_id: 
    :type group_id: str
    :param interface_type: 
    :type interface_type: str
    :param interface_id: 
    :type interface_id: str
    :param priority: 
    :type priority: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param device: 
    :type device: str
    :param device_id: 
    :type device_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param virtual_machine_id: 
    :type virtual_machine_id: str
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
    :param group_id__n: 
    :type group_id__n: str
    :param interface_type__n: 
    :type interface_type__n: str
    :param interface_id__n: 
    :type interface_id__n: str
    :param interface_id__lte: 
    :type interface_id__lte: str
    :param interface_id__lt: 
    :type interface_id__lt: str
    :param interface_id__gte: 
    :type interface_id__gte: str
    :param interface_id__gt: 
    :type interface_id__gt: str
    :param priority__n: 
    :type priority__n: str
    :param priority__lte: 
    :type priority__lte: str
    :param priority__lt: 
    :type priority__lt: str
    :param priority__gte: 
    :type priority__gte: str
    :param priority__gt: 
    :type priority__gt: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_fhrp_group_assignments_partial_update

    

    :param id: A unique integer value identifying this FHRP group assignment.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableFHRPGroupAssignment.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_read(request: web.Request, id) -> web.Response:
    """ipam_fhrp_group_assignments_read

    

    :param id: A unique integer value identifying this FHRP group assignment.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_fhrp_group_assignments_update(request: web.Request, id, body) -> web.Response:
    """ipam_fhrp_group_assignments_update

    

    :param id: A unique integer value identifying this FHRP group assignment.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableFHRPGroupAssignment.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_groups_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_fhrp_groups_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_fhrp_groups_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_fhrp_groups_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = FHRPGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_groups_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_fhrp_groups_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = FHRPGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_groups_create(request: web.Request, body) -> web.Response:
    """ipam_fhrp_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = FHRPGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_groups_delete(request: web.Request, id) -> web.Response:
    """ipam_fhrp_groups_delete

    

    :param id: A unique integer value identifying this FHRP group.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_fhrp_groups_list(request: web.Request, id=None, group_id=None, name=None, auth_key=None, created=None, last_updated=None, q=None, tag=None, protocol=None, auth_type=None, related_ip=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, group_id__n=None, group_id__lte=None, group_id__lt=None, group_id__gte=None, group_id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, auth_key__n=None, auth_key__ic=None, auth_key__nic=None, auth_key__iew=None, auth_key__niew=None, auth_key__isw=None, auth_key__nisw=None, auth_key__ie=None, auth_key__nie=None, auth_key__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, protocol__n=None, auth_type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_fhrp_groups_list

    

    :param id: 
    :type id: str
    :param group_id: 
    :type group_id: str
    :param name: 
    :type name: str
    :param auth_key: 
    :type auth_key: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param protocol: 
    :type protocol: str
    :param auth_type: 
    :type auth_type: str
    :param related_ip: 
    :type related_ip: str
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
    :param group_id__n: 
    :type group_id__n: str
    :param group_id__lte: 
    :type group_id__lte: str
    :param group_id__lt: 
    :type group_id__lt: str
    :param group_id__gte: 
    :type group_id__gte: str
    :param group_id__gt: 
    :type group_id__gt: str
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
    :param name__empty: 
    :type name__empty: str
    :param auth_key__n: 
    :type auth_key__n: str
    :param auth_key__ic: 
    :type auth_key__ic: str
    :param auth_key__nic: 
    :type auth_key__nic: str
    :param auth_key__iew: 
    :type auth_key__iew: str
    :param auth_key__niew: 
    :type auth_key__niew: str
    :param auth_key__isw: 
    :type auth_key__isw: str
    :param auth_key__nisw: 
    :type auth_key__nisw: str
    :param auth_key__ie: 
    :type auth_key__ie: str
    :param auth_key__nie: 
    :type auth_key__nie: str
    :param auth_key__empty: 
    :type auth_key__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param protocol__n: 
    :type protocol__n: str
    :param auth_type__n: 
    :type auth_type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_fhrp_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_fhrp_groups_partial_update

    

    :param id: A unique integer value identifying this FHRP group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = FHRPGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_fhrp_groups_read(request: web.Request, id) -> web.Response:
    """ipam_fhrp_groups_read

    

    :param id: A unique integer value identifying this FHRP group.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_fhrp_groups_update(request: web.Request, id, body) -> web.Response:
    """ipam_fhrp_groups_update

    

    :param id: A unique integer value identifying this FHRP group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = FHRPGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_addresses_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_ip_addresses_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_ip_addresses_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_ip_addresses_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPAddress.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_addresses_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_ip_addresses_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPAddress.from_dict(body)
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


async def ipam_ip_addresses_list(request: web.Request, id=None, dns_name=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, family=None, parent=None, address=None, mask_length=None, vrf_id=None, vrf=None, present_in_vrf_id=None, present_in_vrf=None, device=None, device_id=None, virtual_machine=None, virtual_machine_id=None, interface=None, interface_id=None, vminterface=None, vminterface_id=None, fhrpgroup_id=None, assigned_to_interface=None, status=None, role=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, dns_name__n=None, dns_name__ic=None, dns_name__nic=None, dns_name__iew=None, dns_name__niew=None, dns_name__isw=None, dns_name__nisw=None, dns_name__ie=None, dns_name__nie=None, dns_name__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, vrf_id__n=None, vrf__n=None, interface__n=None, interface_id__n=None, vminterface__n=None, vminterface_id__n=None, fhrpgroup_id__n=None, status__n=None, role__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_ip_addresses_list

    

    :param id: 
    :type id: str
    :param dns_name: 
    :type dns_name: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
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
    :param present_in_vrf_id: 
    :type present_in_vrf_id: str
    :param present_in_vrf: 
    :type present_in_vrf: str
    :param device: 
    :type device: str
    :param device_id: 
    :type device_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param interface: 
    :type interface: str
    :param interface_id: 
    :type interface_id: str
    :param vminterface: 
    :type vminterface: str
    :param vminterface_id: 
    :type vminterface_id: str
    :param fhrpgroup_id: 
    :type fhrpgroup_id: str
    :param assigned_to_interface: 
    :type assigned_to_interface: str
    :param status: 
    :type status: str
    :param role: 
    :type role: str
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
    :param dns_name__empty: 
    :type dns_name__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
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
    :param interface__n: 
    :type interface__n: str
    :param interface_id__n: 
    :type interface_id__n: str
    :param vminterface__n: 
    :type vminterface__n: str
    :param vminterface_id__n: 
    :type vminterface_id__n: str
    :param fhrpgroup_id__n: 
    :type fhrpgroup_id__n: str
    :param status__n: 
    :type status__n: str
    :param role__n: 
    :type role__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def ipam_ip_ranges_available_ips_create(request: web.Request, id, body) -> web.Response:
    """ipam_ip_ranges_available_ips_create

    

    :param id: A unique integer value identifying this IP address.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableAvailableIP.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_ranges_available_ips_list(request: web.Request, id) -> web.Response:
    """ipam_ip_ranges_available_ips_list

    

    :param id: A unique integer value identifying this IP address.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_ip_ranges_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_ip_ranges_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_ip_ranges_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_ip_ranges_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPRange.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_ranges_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_ip_ranges_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPRange.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_ranges_create(request: web.Request, body) -> web.Response:
    """ipam_ip_ranges_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPRange.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_ranges_delete(request: web.Request, id) -> web.Response:
    """ipam_ip_ranges_delete

    

    :param id: A unique integer value identifying this IP range.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_ip_ranges_list(request: web.Request, id=None, description=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, created=None, last_updated=None, q=None, tag=None, family=None, start_address=None, end_address=None, contains=None, vrf_id=None, vrf=None, role_id=None, role=None, status=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, vrf_id__n=None, vrf__n=None, role_id__n=None, role__n=None, status__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_ip_ranges_list

    

    :param id: 
    :type id: str
    :param description: 
    :type description: str
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
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param family: 
    :type family: 
    :param start_address: 
    :type start_address: str
    :param end_address: 
    :type end_address: str
    :param contains: 
    :type contains: str
    :param vrf_id: 
    :type vrf_id: str
    :param vrf: 
    :type vrf: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param status: 
    :type status: str
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
    :param description__empty: 
    :type description__empty: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param vrf_id__n: 
    :type vrf_id__n: str
    :param vrf__n: 
    :type vrf__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param status__n: 
    :type status__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_ip_ranges_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_ip_ranges_partial_update

    

    :param id: A unique integer value identifying this IP range.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPRange.from_dict(body)
    return web.Response(status=200)


async def ipam_ip_ranges_read(request: web.Request, id) -> web.Response:
    """ipam_ip_ranges_read

    

    :param id: A unique integer value identifying this IP range.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_ip_ranges_update(request: web.Request, id, body) -> web.Response:
    """ipam_ip_ranges_update

    

    :param id: A unique integer value identifying this IP range.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableIPRange.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpn_terminations_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_l2vpn_terminations_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_l2vpn_terminations_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_l2vpn_terminations_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPNTermination.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpn_terminations_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_l2vpn_terminations_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPNTermination.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpn_terminations_create(request: web.Request, body) -> web.Response:
    """ipam_l2vpn_terminations_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPNTermination.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpn_terminations_delete(request: web.Request, id) -> web.Response:
    """ipam_l2vpn_terminations_delete

    

    :param id: A unique integer value identifying this L2VPN termination.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_l2vpn_terminations_list(request: web.Request, id=None, assigned_object_type_id=None, created=None, last_updated=None, q=None, tag=None, l2vpn_id=None, l2vpn=None, region=None, region_id=None, site=None, site_id=None, device=None, device_id=None, virtual_machine=None, virtual_machine_id=None, interface=None, interface_id=None, vminterface=None, vminterface_id=None, vlan=None, vlan_vid=None, vlan_id=None, assigned_object_type=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, assigned_object_type_id__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, l2vpn_id__n=None, l2vpn__n=None, device__n=None, device_id__n=None, virtual_machine__n=None, virtual_machine_id__n=None, interface__n=None, interface_id__n=None, vminterface__n=None, vminterface_id__n=None, vlan__n=None, vlan_vid__n=None, vlan_vid__lte=None, vlan_vid__lt=None, vlan_vid__gte=None, vlan_vid__gt=None, vlan_id__n=None, assigned_object_type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_l2vpn_terminations_list

    

    :param id: 
    :type id: str
    :param assigned_object_type_id: 
    :type assigned_object_type_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param l2vpn_id: 
    :type l2vpn_id: str
    :param l2vpn: 
    :type l2vpn: str
    :param region: 
    :type region: str
    :param region_id: 
    :type region_id: str
    :param site: 
    :type site: str
    :param site_id: 
    :type site_id: str
    :param device: 
    :type device: str
    :param device_id: 
    :type device_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param interface: 
    :type interface: str
    :param interface_id: 
    :type interface_id: str
    :param vminterface: 
    :type vminterface: str
    :param vminterface_id: 
    :type vminterface_id: str
    :param vlan: 
    :type vlan: str
    :param vlan_vid: 
    :type vlan_vid: 
    :param vlan_id: 
    :type vlan_id: str
    :param assigned_object_type: 
    :type assigned_object_type: str
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
    :param assigned_object_type_id__n: 
    :type assigned_object_type_id__n: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param l2vpn_id__n: 
    :type l2vpn_id__n: str
    :param l2vpn__n: 
    :type l2vpn__n: str
    :param device__n: 
    :type device__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param virtual_machine__n: 
    :type virtual_machine__n: str
    :param virtual_machine_id__n: 
    :type virtual_machine_id__n: str
    :param interface__n: 
    :type interface__n: str
    :param interface_id__n: 
    :type interface_id__n: str
    :param vminterface__n: 
    :type vminterface__n: str
    :param vminterface_id__n: 
    :type vminterface_id__n: str
    :param vlan__n: 
    :type vlan__n: str
    :param vlan_vid__n: 
    :type vlan_vid__n: 
    :param vlan_vid__lte: 
    :type vlan_vid__lte: 
    :param vlan_vid__lt: 
    :type vlan_vid__lt: 
    :param vlan_vid__gte: 
    :type vlan_vid__gte: 
    :param vlan_vid__gt: 
    :type vlan_vid__gt: 
    :param vlan_id__n: 
    :type vlan_id__n: str
    :param assigned_object_type__n: 
    :type assigned_object_type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_l2vpn_terminations_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_l2vpn_terminations_partial_update

    

    :param id: A unique integer value identifying this L2VPN termination.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPNTermination.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpn_terminations_read(request: web.Request, id) -> web.Response:
    """ipam_l2vpn_terminations_read

    

    :param id: A unique integer value identifying this L2VPN termination.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_l2vpn_terminations_update(request: web.Request, id, body) -> web.Response:
    """ipam_l2vpn_terminations_update

    

    :param id: A unique integer value identifying this L2VPN termination.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPNTermination.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpns_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_l2vpns_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_l2vpns_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_l2vpns_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPN.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpns_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_l2vpns_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPN.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpns_create(request: web.Request, body) -> web.Response:
    """ipam_l2vpns_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPN.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpns_delete(request: web.Request, id) -> web.Response:
    """ipam_l2vpns_delete

    

    :param id: A unique integer value identifying this L2VPN.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_l2vpns_list(request: web.Request, id=None, identifier=None, name=None, slug=None, type=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, import_target_id=None, import_target=None, export_target_id=None, export_target=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, identifier__n=None, identifier__lte=None, identifier__lt=None, identifier__gte=None, identifier__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, type__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, import_target_id__n=None, import_target__n=None, export_target_id__n=None, export_target__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_l2vpns_list

    

    :param id: 
    :type id: str
    :param identifier: 
    :type identifier: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param type: 
    :type type: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param import_target_id: 
    :type import_target_id: str
    :param import_target: 
    :type import_target: str
    :param export_target_id: 
    :type export_target_id: str
    :param export_target: 
    :type export_target: str
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
    :param identifier__n: 
    :type identifier__n: str
    :param identifier__lte: 
    :type identifier__lte: str
    :param identifier__lt: 
    :type identifier__lt: str
    :param identifier__gte: 
    :type identifier__gte: str
    :param identifier__gt: 
    :type identifier__gt: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
    :param type__n: 
    :type type__n: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param import_target_id__n: 
    :type import_target_id__n: str
    :param import_target__n: 
    :type import_target__n: str
    :param export_target_id__n: 
    :type export_target_id__n: str
    :param export_target__n: 
    :type export_target__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_l2vpns_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_l2vpns_partial_update

    

    :param id: A unique integer value identifying this L2VPN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPN.from_dict(body)
    return web.Response(status=200)


async def ipam_l2vpns_read(request: web.Request, id) -> web.Response:
    """ipam_l2vpns_read

    

    :param id: A unique integer value identifying this L2VPN.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_l2vpns_update(request: web.Request, id, body) -> web.Response:
    """ipam_l2vpns_update

    

    :param id: A unique integer value identifying this L2VPN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableL2VPN.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_ips_create(request: web.Request, id, body) -> web.Response:
    """ipam_prefixes_available_ips_create

    

    :param id: A unique integer value identifying this IP address.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableAvailableIP.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_ips_list(request: web.Request, id) -> web.Response:
    """ipam_prefixes_available_ips_list

    

    :param id: A unique integer value identifying this IP address.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_prefixes_available_prefixes_create(request: web.Request, id, body) -> web.Response:
    """ipam_prefixes_available_prefixes_create

    

    :param id: A unique integer value identifying this prefix.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PrefixLength.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_available_prefixes_list(request: web.Request, id) -> web.Response:
    """ipam_prefixes_available_prefixes_list

    

    :param id: A unique integer value identifying this prefix.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_prefixes_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_prefixes_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_prefixes_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_prefixes_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
    return web.Response(status=200)


async def ipam_prefixes_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_prefixes_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritablePrefix.from_dict(body)
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


async def ipam_prefixes_list(request: web.Request, id=None, is_pool=None, mark_utilized=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, family=None, prefix=None, within=None, within_include=None, contains=None, depth=None, children=None, mask_length=None, mask_length__gte=None, mask_length__lte=None, vrf_id=None, vrf=None, present_in_vrf_id=None, present_in_vrf=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, vlan_id=None, vlan_vid=None, role_id=None, role=None, status=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, depth__n=None, depth__lte=None, depth__lt=None, depth__gte=None, depth__gt=None, children__n=None, children__lte=None, children__lt=None, children__gte=None, children__gt=None, vrf_id__n=None, vrf__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, vlan_id__n=None, vlan_vid__n=None, vlan_vid__lte=None, vlan_vid__lt=None, vlan_vid__gte=None, vlan_vid__gt=None, role_id__n=None, role__n=None, status__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_prefixes_list

    

    :param id: 
    :type id: str
    :param is_pool: 
    :type is_pool: str
    :param mark_utilized: 
    :type mark_utilized: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
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
    :param depth: 
    :type depth: str
    :param children: 
    :type children: str
    :param mask_length: 
    :type mask_length: str
    :param mask_length__gte: 
    :type mask_length__gte: 
    :param mask_length__lte: 
    :type mask_length__lte: 
    :param vrf_id: 
    :type vrf_id: str
    :param vrf: 
    :type vrf: str
    :param present_in_vrf_id: 
    :type present_in_vrf_id: str
    :param present_in_vrf: 
    :type present_in_vrf: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param depth__n: 
    :type depth__n: str
    :param depth__lte: 
    :type depth__lte: str
    :param depth__lt: 
    :type depth__lt: str
    :param depth__gte: 
    :type depth__gte: str
    :param depth__gt: 
    :type depth__gt: str
    :param children__n: 
    :type children__n: str
    :param children__lte: 
    :type children__lte: str
    :param children__lt: 
    :type children__lt: str
    :param children__gte: 
    :type children__gte: str
    :param children__gt: 
    :type children__gt: str
    :param vrf_id__n: 
    :type vrf_id__n: str
    :param vrf__n: 
    :type vrf__n: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param vlan_id__n: 
    :type vlan_id__n: str
    :param vlan_vid__n: 
    :type vlan_vid__n: 
    :param vlan_vid__lte: 
    :type vlan_vid__lte: 
    :param vlan_vid__lt: 
    :type vlan_vid__lt: 
    :param vlan_vid__gte: 
    :type vlan_vid__gte: 
    :param vlan_vid__gt: 
    :type vlan_vid__gt: 
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param status__n: 
    :type status__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def ipam_rirs_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_rirs_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_rirs_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_rirs_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = RIR.from_dict(body)
    return web.Response(status=200)


async def ipam_rirs_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_rirs_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = RIR.from_dict(body)
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


async def ipam_rirs_list(request: web.Request, id=None, name=None, slug=None, is_private=None, description=None, created=None, last_updated=None, q=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_rirs_list

    

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
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def ipam_roles_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_roles_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_roles_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_roles_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Role.from_dict(body)
    return web.Response(status=200)


async def ipam_roles_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_roles_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Role.from_dict(body)
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


async def ipam_roles_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_roles_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def ipam_route_targets_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_route_targets_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_route_targets_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_route_targets_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRouteTarget.from_dict(body)
    return web.Response(status=200)


async def ipam_route_targets_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_route_targets_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRouteTarget.from_dict(body)
    return web.Response(status=200)


async def ipam_route_targets_create(request: web.Request, body) -> web.Response:
    """ipam_route_targets_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableRouteTarget.from_dict(body)
    return web.Response(status=200)


async def ipam_route_targets_delete(request: web.Request, id) -> web.Response:
    """ipam_route_targets_delete

    

    :param id: A unique integer value identifying this route target.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_route_targets_list(request: web.Request, id=None, name=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, importing_vrf_id=None, importing_vrf=None, exporting_vrf_id=None, exporting_vrf=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, importing_vrf_id__n=None, importing_vrf__n=None, exporting_vrf_id__n=None, exporting_vrf__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_route_targets_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param importing_vrf_id: 
    :type importing_vrf_id: str
    :param importing_vrf: 
    :type importing_vrf: str
    :param exporting_vrf_id: 
    :type exporting_vrf_id: str
    :param exporting_vrf: 
    :type exporting_vrf: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param importing_vrf_id__n: 
    :type importing_vrf_id__n: str
    :param importing_vrf__n: 
    :type importing_vrf__n: str
    :param exporting_vrf_id__n: 
    :type exporting_vrf_id__n: str
    :param exporting_vrf__n: 
    :type exporting_vrf__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_route_targets_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_route_targets_partial_update

    

    :param id: A unique integer value identifying this route target.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRouteTarget.from_dict(body)
    return web.Response(status=200)


async def ipam_route_targets_read(request: web.Request, id) -> web.Response:
    """ipam_route_targets_read

    

    :param id: A unique integer value identifying this route target.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_route_targets_update(request: web.Request, id, body) -> web.Response:
    """ipam_route_targets_update

    

    :param id: A unique integer value identifying this route target.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableRouteTarget.from_dict(body)
    return web.Response(status=200)


async def ipam_service_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_service_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_service_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_service_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableServiceTemplate.from_dict(body)
    return web.Response(status=200)


async def ipam_service_templates_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_service_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableServiceTemplate.from_dict(body)
    return web.Response(status=200)


async def ipam_service_templates_create(request: web.Request, body) -> web.Response:
    """ipam_service_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableServiceTemplate.from_dict(body)
    return web.Response(status=200)


async def ipam_service_templates_delete(request: web.Request, id) -> web.Response:
    """ipam_service_templates_delete

    

    :param id: A unique integer value identifying this service template.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_service_templates_list(request: web.Request, id=None, name=None, protocol=None, created=None, last_updated=None, q=None, tag=None, port=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, protocol__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_service_templates_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param protocol: 
    :type protocol: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param port: 
    :type port: 
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
    :param name__empty: 
    :type name__empty: str
    :param protocol__n: 
    :type protocol__n: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def ipam_service_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """ipam_service_templates_partial_update

    

    :param id: A unique integer value identifying this service template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableServiceTemplate.from_dict(body)
    return web.Response(status=200)


async def ipam_service_templates_read(request: web.Request, id) -> web.Response:
    """ipam_service_templates_read

    

    :param id: A unique integer value identifying this service template.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_service_templates_update(request: web.Request, id, body) -> web.Response:
    """ipam_service_templates_update

    

    :param id: A unique integer value identifying this service template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableServiceTemplate.from_dict(body)
    return web.Response(status=200)


async def ipam_services_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_services_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_services_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_services_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableService.from_dict(body)
    return web.Response(status=200)


async def ipam_services_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_services_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableService.from_dict(body)
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


async def ipam_services_list(request: web.Request, id=None, name=None, protocol=None, description=None, created=None, last_updated=None, q=None, tag=None, device_id=None, device=None, virtual_machine_id=None, virtual_machine=None, ipaddress_id=None, ipaddress=None, port=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, protocol__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, device_id__n=None, device__n=None, virtual_machine_id__n=None, virtual_machine__n=None, ipaddress_id__n=None, ipaddress__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_services_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param protocol: 
    :type protocol: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param virtual_machine_id: 
    :type virtual_machine_id: str
    :param virtual_machine: 
    :type virtual_machine: str
    :param ipaddress_id: 
    :type ipaddress_id: str
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: 
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
    :param name__empty: 
    :type name__empty: str
    :param protocol__n: 
    :type protocol__n: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param virtual_machine_id__n: 
    :type virtual_machine_id__n: str
    :param virtual_machine__n: 
    :type virtual_machine__n: str
    :param ipaddress_id__n: 
    :type ipaddress_id__n: str
    :param ipaddress__n: 
    :type ipaddress__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def ipam_vlan_groups_available_vlans_create(request: web.Request, id, body) -> web.Response:
    """ipam_vlan_groups_available_vlans_create

    

    :param id: A unique integer value identifying this VLAN.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCreateAvailableVLAN.from_dict(body)
    return web.Response(status=200)


async def ipam_vlan_groups_available_vlans_list(request: web.Request, id) -> web.Response:
    """ipam_vlan_groups_available_vlans_list

    

    :param id: A unique integer value identifying this VLAN.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vlan_groups_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_vlan_groups_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_vlan_groups_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_vlan_groups_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = VLANGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_vlan_groups_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_vlan_groups_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = VLANGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_vlan_groups_create(request: web.Request, body) -> web.Response:
    """ipam_vlan_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = VLANGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_vlan_groups_delete(request: web.Request, id) -> web.Response:
    """ipam_vlan_groups_delete

    

    :param id: A unique integer value identifying this VLAN group.
    :type id: int

    """
    return web.Response(status=200)


async def ipam_vlan_groups_list(request: web.Request, id=None, name=None, slug=None, min_vid=None, max_vid=None, description=None, scope_id=None, created=None, last_updated=None, q=None, tag=None, scope_type=None, region=None, sitegroup=None, site=None, location=None, rack=None, clustergroup=None, cluster=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, min_vid__n=None, min_vid__lte=None, min_vid__lt=None, min_vid__gte=None, min_vid__gt=None, max_vid__n=None, max_vid__lte=None, max_vid__lt=None, max_vid__gte=None, max_vid__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, scope_id__n=None, scope_id__lte=None, scope_id__lt=None, scope_id__gte=None, scope_id__gt=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, scope_type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_vlan_groups_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param min_vid: 
    :type min_vid: str
    :param max_vid: 
    :type max_vid: str
    :param description: 
    :type description: str
    :param scope_id: 
    :type scope_id: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param scope_type: 
    :type scope_type: str
    :param region: 
    :type region: 
    :param sitegroup: 
    :type sitegroup: 
    :param site: 
    :type site: 
    :param location: 
    :type location: 
    :param rack: 
    :type rack: 
    :param clustergroup: 
    :type clustergroup: 
    :param cluster: 
    :type cluster: 
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
    :param min_vid__n: 
    :type min_vid__n: str
    :param min_vid__lte: 
    :type min_vid__lte: str
    :param min_vid__lt: 
    :type min_vid__lt: str
    :param min_vid__gte: 
    :type min_vid__gte: str
    :param min_vid__gt: 
    :type min_vid__gt: str
    :param max_vid__n: 
    :type max_vid__n: str
    :param max_vid__lte: 
    :type max_vid__lte: str
    :param max_vid__lt: 
    :type max_vid__lt: str
    :param max_vid__gte: 
    :type max_vid__gte: str
    :param max_vid__gt: 
    :type max_vid__gt: str
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
    :param description__empty: 
    :type description__empty: str
    :param scope_id__n: 
    :type scope_id__n: str
    :param scope_id__lte: 
    :type scope_id__lte: str
    :param scope_id__lt: 
    :type scope_id__lt: str
    :param scope_id__gte: 
    :type scope_id__gte: str
    :param scope_id__gt: 
    :type scope_id__gt: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param scope_type__n: 
    :type scope_type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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
    body = VLANGroup.from_dict(body)
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
    body = VLANGroup.from_dict(body)
    return web.Response(status=200)


async def ipam_vlans_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_vlans_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_vlans_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_vlans_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLAN.from_dict(body)
    return web.Response(status=200)


async def ipam_vlans_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_vlans_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVLAN.from_dict(body)
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


async def ipam_vlans_list(request: web.Request, id=None, vid=None, name=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, region_id=None, region=None, site_group_id=None, site_group=None, site_id=None, site=None, group_id=None, group=None, role_id=None, role=None, status=None, available_on_device=None, available_on_virtualmachine=None, l2vpn_id=None, l2vpn=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, vid__n=None, vid__lte=None, vid__lt=None, vid__gte=None, vid__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, region_id__n=None, region__n=None, site_group_id__n=None, site_group__n=None, site_id__n=None, site__n=None, group_id__n=None, group__n=None, role_id__n=None, role__n=None, status__n=None, l2vpn_id__n=None, l2vpn__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_vlans_list

    

    :param id: 
    :type id: str
    :param vid: 
    :type vid: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_group: 
    :type site_group: str
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
    :param available_on_device: 
    :type available_on_device: str
    :param available_on_virtualmachine: 
    :type available_on_virtualmachine: str
    :param l2vpn_id: 
    :type l2vpn_id: str
    :param l2vpn: 
    :type l2vpn: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
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
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_group__n: 
    :type site_group__n: str
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
    :param l2vpn_id__n: 
    :type l2vpn_id__n: str
    :param l2vpn__n: 
    :type l2vpn__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def ipam_vrfs_bulk_delete(request: web.Request, ) -> web.Response:
    """ipam_vrfs_bulk_delete

    


    """
    return web.Response(status=200)


async def ipam_vrfs_bulk_partial_update(request: web.Request, body) -> web.Response:
    """ipam_vrfs_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVRF.from_dict(body)
    return web.Response(status=200)


async def ipam_vrfs_bulk_update(request: web.Request, body) -> web.Response:
    """ipam_vrfs_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableVRF.from_dict(body)
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


async def ipam_vrfs_list(request: web.Request, id=None, name=None, rd=None, enforce_unique=None, description=None, created=None, last_updated=None, q=None, tag=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, import_target_id=None, import_target=None, export_target_id=None, export_target=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, rd__n=None, rd__ic=None, rd__nic=None, rd__iew=None, rd__niew=None, rd__isw=None, rd__nisw=None, rd__ie=None, rd__nie=None, rd__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, import_target_id__n=None, import_target__n=None, export_target_id__n=None, export_target__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """ipam_vrfs_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param rd: 
    :type rd: str
    :param enforce_unique: 
    :type enforce_unique: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param import_target_id: 
    :type import_target_id: str
    :param import_target: 
    :type import_target: str
    :param export_target_id: 
    :type export_target_id: str
    :param export_target: 
    :type export_target: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param rd__empty: 
    :type rd__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param import_target_id__n: 
    :type import_target_id__n: str
    :param import_target__n: 
    :type import_target__n: str
    :param export_target_id__n: 
    :type export_target_id__n: str
    :param export_target__n: 
    :type export_target__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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
