# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster_health_policy import ClusterHealthPolicy
from openapi_server.models.deactivation_intent_description import DeactivationIntentDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.node_health import NodeHealth
from openapi_server.models.node_info import NodeInfo
from openapi_server.models.node_load_info import NodeLoadInfo
from openapi_server.models.paged_node_info_list import PagedNodeInfoList
from openapi_server.models.restart_node_description import RestartNodeDescription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_disable_node(client):
    """Test case for disable_node

    Deactivate a Service Fabric cluster node with the specified deactivation intent.
    """
    deactivation_intent_description = openapi_server.DeactivationIntentDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/Deactivate'.format(node_name='node_name_example'),
        headers=headers,
        json=deactivation_intent_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_node(client):
    """Test case for enable_node

    Activate a Service Fabric cluster node which is currently deactivated.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/Activate'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_health(client):
    """Test case for get_node_health

    Gets the health of a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetHealth'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_node_health_using_policy(client):
    """Test case for get_node_health_using_policy

    Gets the health of a Service Fabric node, by using the specified health policy.
    """
    cluster_health_policy = openapi_server.ClusterHealthPolicy()
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/GetHealth'.format(node_name='node_name_example'),
        headers=headers,
        json=cluster_health_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_info(client):
    """Test case for get_node_info

    Gets the information about a specific node in the Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_info_list(client):
    """Test case for get_node_info_list

    Gets the list of nodes in the Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('NodeStatusFilter', default),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_node_load_info(client):
    """Test case for get_node_load_info

    Gets the load information of a Service Fabric node.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Nodes/{node_name}/$/GetLoadInformation'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_node_state(client):
    """Test case for remove_node_state

    Notifies Service Fabric that the persisted state on a node has been permanently removed or lost.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/RemoveNodeState'.format(node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_node_health(client):
    """Test case for report_node_health

    Sends a health report on the Service Fabric node.
    """
    health_information = openapi_server.HealthInformation()
    params = [('api-version', 6.0),
                    ('Immediate', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/ReportHealth'.format(node_name='node_name_example'),
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_restart_node(client):
    """Test case for restart_node

    Restarts a Service Fabric cluster node.
    """
    restart_node_description = openapi_server.RestartNodeDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Nodes/{node_name}/$/Restart'.format(node_name='node_name_example'),
        headers=headers,
        json=restart_node_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

