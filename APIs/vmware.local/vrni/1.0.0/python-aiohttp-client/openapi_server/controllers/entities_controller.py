from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.base_firewall_rule import BaseFirewallRule
from openapi_server.models.base_ip_set import BaseIPSet
from openapi_server.models.base_l2_network import BaseL2Network
from openapi_server.models.base_nsx_manager import BaseNSXManager
from openapi_server.models.base_security_group import BaseSecurityGroup
from openapi_server.models.base_service import BaseService
from openapi_server.models.base_service_group import BaseServiceGroup
from openapi_server.models.base_virtual_machine import BaseVirtualMachine
from openapi_server.models.base_vnic import BaseVnic
from openapi_server.models.cluster import Cluster
from openapi_server.models.datastore import Datastore
from openapi_server.models.distributed_virtual_portgroup import DistributedVirtualPortgroup
from openapi_server.models.distributed_virtual_switch import DistributedVirtualSwitch
from openapi_server.models.entity_name import EntityName
from openapi_server.models.flow import Flow
from openapi_server.models.folder import Folder
from openapi_server.models.host import Host
from openapi_server.models.names_request import NamesRequest
from openapi_server.models.names_response import NamesResponse
from openapi_server.models.paged_list_response_with_time import PagedListResponseWithTime
from openapi_server.models.problem_event import ProblemEvent
from openapi_server.models.security_tag import SecurityTag
from openapi_server.models.vc_datacenter import VCDatacenter
from openapi_server.models.v_center_manager import VCenterManager
from openapi_server.models.vmknic import Vmknic
from openapi_server import util


async def get_cluster(request: web.Request, id, time=None) -> web.Response:
    """Show cluster details

    Show cluster details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_datacenter(request: web.Request, id, time=None) -> web.Response:
    """Show vCenter datacenter details

    Show vCenter datacenter details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_datastore(request: web.Request, id, time=None) -> web.Response:
    """Show datastore details

    Show datastore details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_distributed_virtual_portgroup(request: web.Request, id, time=None) -> web.Response:
    """Show distributed virtual portgroup details

    Show distributed virtual portgroup details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_distributed_virtual_switch(request: web.Request, id, time=None) -> web.Response:
    """Show distributed virtual switch details

    Show distributed virtual switch details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_firewall(request: web.Request, id, time=None) -> web.Response:
    """Show firewall details

    Show firewall details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_firewall_rule(request: web.Request, id, time=None) -> web.Response:
    """Show firewall rule details

    Show firewall rule details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_flow(request: web.Request, id, time=None) -> web.Response:
    """Show flow details

    Show flow details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_flows(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List flows

    List flows

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def get_folder(request: web.Request, id, time=None) -> web.Response:
    """Show folder details

    Show folder details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_host(request: web.Request, id, time=None) -> web.Response:
    """Show host details

    Show host details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_ip_set(request: web.Request, id, time=None) -> web.Response:
    """Show ip set details

    Show ip set details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_layer2_network(request: web.Request, id, time=None) -> web.Response:
    """Show layer2 network details

    Show layer2 network details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_name(request: web.Request, id, time=None) -> web.Response:
    """Get name of an entity

    Get name of an entity

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_names(request: web.Request, body) -> web.Response:
    """Get names for entities

    Get names for entities.Limit of 1000 entities in a single request.

    :param body: Names Request
    :type body: dict | bytes

    """
    body = NamesRequest.from_dict(body)
    return web.Response(status=200)


async def get_nsx_manager(request: web.Request, id, time=None) -> web.Response:
    """Show nsx manager details

    Show nsx manager details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_problem_event(request: web.Request, id, time=None) -> web.Response:
    """Show problem details

    Show problem event details.

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_security_group(request: web.Request, id, time=None) -> web.Response:
    """Show security group details

    Show security group details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_security_tag(request: web.Request, id, time=None) -> web.Response:
    """Show security tag details

    Show security tag details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_service(request: web.Request, id, time=None) -> web.Response:
    """Show service details

    Show service details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_service_group(request: web.Request, id, time=None) -> web.Response:
    """Show service group details

    Show service group details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_vcenter_manager(request: web.Request, id, time=None) -> web.Response:
    """Show vCenter manager details

    Show vCenter manager details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_vm(request: web.Request, id, time=None) -> web.Response:
    """Show vm details

    Show vm details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_vmknic(request: web.Request, id, time=None) -> web.Response:
    """Show vmknic details

    Show vmknic details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def get_vnic(request: web.Request, id, time=None) -> web.Response:
    """Show vnic details

    Show vnic details

    :param id: entity id
    :type id: str
    :param time: time in epoch seconds
    :type time: int

    """
    return web.Response(status=200)


async def list_clusters(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List clusters

    List clusters

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_datacenters(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List vCenter datacenters

    List vCenter datacenters

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_datastores(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List datastores

    List datastores

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_distributed_virtual_portgroups(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List distributed virtual portgroups

    List distributed virtual portgroups

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_distributed_virtual_switches(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List distributed virtual switches

    List distributed virtual switches

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_firewall_rules(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List firewall rules

    List firewall rules

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_firewalls(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List firewalls

    List firewalls

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_folders(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List folders

    List folders

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_hosts(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List hosts

    List hosts

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_ip_sets(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List ip sets

    List ip sets

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_layer2_networks(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List layer2 networks

    List layer2 networks

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_nsx_managers(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List nsx managers

    List nsx managers

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_problem_events(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List problems

    List problem events.

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_security_groups(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List security groups

    List security groups

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_security_tags(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List security tags

    List security tags

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_service_groups(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List service groups

    List service groups

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_services(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List services

    List services

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_vcenter_managers(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List vCenter managers

    List vCenter managers

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_vmknics(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List vmknics

    List vmknics

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_vms(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List vms

    List vms

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)


async def list_vnics(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List vnics

    List vnics

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)
