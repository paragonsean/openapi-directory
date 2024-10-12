# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_get_cluster(client):
    """Test case for get_cluster

    Show cluster details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/clusters/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datacenter(client):
    """Test case for get_datacenter

    Show vCenter datacenter details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vc-datacenters/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_datastore(client):
    """Test case for get_datastore

    Show datastore details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/datastores/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_distributed_virtual_portgroup(client):
    """Test case for get_distributed_virtual_portgroup

    Show distributed virtual portgroup details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/distributed-virtual-portgroups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_distributed_virtual_switch(client):
    """Test case for get_distributed_virtual_switch

    Show distributed virtual switch details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/distributed-virtual-switches/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_firewall(client):
    """Test case for get_firewall

    Show firewall details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/firewalls/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_firewall_rule(client):
    """Test case for get_firewall_rule

    Show firewall rule details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/firewall-rules/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_flow(client):
    """Test case for get_flow

    Show flow details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/flows/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_flows(client):
    """Test case for get_flows

    List flows
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/flows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_folder(client):
    """Test case for get_folder

    Show folder details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/folders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_host(client):
    """Test case for get_host

    Show host details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/hosts/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ip_set(client):
    """Test case for get_ip_set

    Show ip set details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/ip-sets/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_layer2_network(client):
    """Test case for get_layer2_network

    Show layer2 network details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/layer2-networks/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_name(client):
    """Test case for get_name

    Get name of an entity
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/names/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_names(client):
    """Test case for get_names

    Get names for entities
    """
    body = {"entities":[{"time":0,"entity_id":"entity_id"},{"time":0,"entity_id":"entity_id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/entities/names',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nsx_manager(client):
    """Test case for get_nsx_manager

    Show nsx manager details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/nsx-managers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_problem_event(client):
    """Test case for get_problem_event

    Show problem details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/problems/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_security_group(client):
    """Test case for get_security_group

    Show security group details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/security-groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_security_tag(client):
    """Test case for get_security_tag

    Show security tag details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/security-tags/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service(client):
    """Test case for get_service

    Show service details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/services/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_group(client):
    """Test case for get_service_group

    Show service group details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/service-groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcenter_manager(client):
    """Test case for get_vcenter_manager

    Show vCenter manager details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vcenter-managers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vm(client):
    """Test case for get_vm

    Show vm details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vms/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmknic(client):
    """Test case for get_vmknic

    Show vmknic details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vmknics/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vnic(client):
    """Test case for get_vnic

    Show vnic details
    """
    params = [('time', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vnics/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_clusters(client):
    """Test case for list_clusters

    List clusters
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/clusters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_datacenters(client):
    """Test case for list_datacenters

    List vCenter datacenters
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vc-datacenters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_datastores(client):
    """Test case for list_datastores

    List datastores
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/datastores',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_distributed_virtual_portgroups(client):
    """Test case for list_distributed_virtual_portgroups

    List distributed virtual portgroups
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/distributed-virtual-portgroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_distributed_virtual_switches(client):
    """Test case for list_distributed_virtual_switches

    List distributed virtual switches
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/distributed-virtual-switches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_firewall_rules(client):
    """Test case for list_firewall_rules

    List firewall rules
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/firewall-rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_firewalls(client):
    """Test case for list_firewalls

    List firewalls
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/firewalls',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_folders(client):
    """Test case for list_folders

    List folders
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/folders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hosts(client):
    """Test case for list_hosts

    List hosts
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/hosts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_ip_sets(client):
    """Test case for list_ip_sets

    List ip sets
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/ip-sets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_layer2_networks(client):
    """Test case for list_layer2_networks

    List layer2 networks
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/layer2-networks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_nsx_managers(client):
    """Test case for list_nsx_managers

    List nsx managers
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/nsx-managers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_problem_events(client):
    """Test case for list_problem_events

    List problems
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/problems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_security_groups(client):
    """Test case for list_security_groups

    List security groups
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/security-groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_security_tags(client):
    """Test case for list_security_tags

    List security tags
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/security-tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_groups(client):
    """Test case for list_service_groups

    List service groups
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/service-groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_services(client):
    """Test case for list_services

    List services
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vcenter_managers(client):
    """Test case for list_vcenter_managers

    List vCenter managers
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vcenter-managers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vmknics(client):
    """Test case for list_vmknics

    List vmknics
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vmknics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vms(client):
    """Test case for list_vms

    List vms
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vnics(client):
    """Test case for list_vnics

    List vnics
    """
    params = [('size', 10),
                    ('cursor', 'cursor_example'),
                    ('start_time', 3.4),
                    ('end_time', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/entities/vnics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

