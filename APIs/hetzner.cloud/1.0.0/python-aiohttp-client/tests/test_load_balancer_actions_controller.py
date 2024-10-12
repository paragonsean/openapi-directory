# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.add_target_request import AddTargetRequest
from openapi_server.models.change_loadbalancer_dns_ptr_request import ChangeLoadbalancerDnsPtrRequest
from openapi_server.models.change_type_request import ChangeTypeRequest
from openapi_server.models.load_balancer_service import LoadBalancerService
from openapi_server.models.load_balancers_id_actions_attach_to_network_post_request import LoadBalancersIdActionsAttachToNetworkPostRequest
from openapi_server.models.load_balancers_id_actions_change_algorithm_post_request import LoadBalancersIdActionsChangeAlgorithmPostRequest
from openapi_server.models.load_balancers_id_actions_change_protection_post_request import LoadBalancersIdActionsChangeProtectionPostRequest
from openapi_server.models.load_balancers_id_actions_delete_service_post_request import LoadBalancersIdActionsDeleteServicePostRequest
from openapi_server.models.load_balancers_id_actions_detach_from_network_post_request import LoadBalancersIdActionsDetachFromNetworkPostRequest
from openapi_server.models.remove_target_request import RemoveTargetRequest


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_action_id_get(client):
    """Test case for load_balancers_id_actions_action_id_get

    Get an Action for a Load Balancer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/load_balancers/{id}/actions/{action_id}'.format(id=56, action_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_add_service_post(client):
    """Test case for load_balancers_id_actions_add_service_post

    Add Service
    """
    body = {"protocol":"https","listen_port":443,"destination_port":80,"http":{"redirect_http":True,"sticky_sessions":True,"certificates":[897],"cookie_lifetime":300,"cookie_name":"HCLBSTICKY"},"health_check":{"retries":3,"protocol":"http","port":4711,"http":{"path":"/","response":"{\"status\": \"ok\"}","domain":"example.com","status_codes":["2??","3??"],"tls":False},"interval":15,"timeout":10},"proxyprotocol":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/add_service'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_add_target_post(client):
    """Test case for load_balancers_id_actions_add_target_post

    Add Target
    """
    body = {"use_private_ip":True,"server":{"id":80},"label_selector":{"selector":"env=prod"},"ip":{"ip":"203.0.113.1"},"type":"server"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/add_target'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_attach_to_network_post(client):
    """Test case for load_balancers_id_actions_attach_to_network_post

    Attach a Load Balancer to a Network
    """
    body = openapi_server.LoadBalancersIdActionsAttachToNetworkPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/attach_to_network'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_change_algorithm_post(client):
    """Test case for load_balancers_id_actions_change_algorithm_post

    Change Algorithm
    """
    body = openapi_server.LoadBalancersIdActionsChangeAlgorithmPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/change_algorithm'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_change_dns_ptr_post(client):
    """Test case for load_balancers_id_actions_change_dns_ptr_post

    Change reverse DNS entry for this Load Balancer
    """
    body = {"ip":"1.2.3.4","dns_ptr":"lb1.example.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/change_dns_ptr'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_change_protection_post(client):
    """Test case for load_balancers_id_actions_change_protection_post

    Change Load Balancer Protection
    """
    body = openapi_server.LoadBalancersIdActionsChangeProtectionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/change_protection'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_change_type_post(client):
    """Test case for load_balancers_id_actions_change_type_post

    Change the Type of a Load Balancer
    """
    body = {"load_balancer_type":"lb21"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/change_type'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_delete_service_post(client):
    """Test case for load_balancers_id_actions_delete_service_post

    Delete Service
    """
    body = openapi_server.LoadBalancersIdActionsDeleteServicePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/delete_service'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_detach_from_network_post(client):
    """Test case for load_balancers_id_actions_detach_from_network_post

    Detach a Load Balancer from a Network
    """
    body = openapi_server.LoadBalancersIdActionsDetachFromNetworkPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/detach_from_network'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_disable_public_interface_post(client):
    """Test case for load_balancers_id_actions_disable_public_interface_post

    Disable the public interface of a Load Balancer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/disable_public_interface'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_enable_public_interface_post(client):
    """Test case for load_balancers_id_actions_enable_public_interface_post

    Enable the public interface of a Load Balancer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/enable_public_interface'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_get(client):
    """Test case for load_balancers_id_actions_get

    Get all Actions for a Load Balancer
    """
    params = [('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/load_balancers/{id}/actions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_remove_target_post(client):
    """Test case for load_balancers_id_actions_remove_target_post

    Remove Target
    """
    body = {"server":{"id":80},"label_selector":{"selector":"env=prod"},"ip":{"ip":"203.0.113.1"},"type":"server"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/remove_target'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_balancers_id_actions_update_service_post(client):
    """Test case for load_balancers_id_actions_update_service_post

    Update Service
    """
    body = {"protocol":"https","listen_port":443,"destination_port":80,"http":{"redirect_http":True,"sticky_sessions":True,"certificates":[897],"cookie_lifetime":300,"cookie_name":"HCLBSTICKY"},"health_check":{"retries":3,"protocol":"http","port":4711,"http":{"path":"/","response":"{\"status\": \"ok\"}","domain":"example.com","status_codes":["2??","3??"],"tls":False},"interval":15,"timeout":10},"proxyprotocol":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/load_balancers/{id}/actions/update_service'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

