# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apply_policy_all_nodes200_response import ApplyPolicyAllNodes200Response
from openapi_server.models.change_pending_node_status200_response import ChangePendingNodeStatus200Response
from openapi_server.models.change_pending_node_status_request import ChangePendingNodeStatusRequest
from openapi_server.models.create_nodes200_response import CreateNodes200Response
from openapi_server.models.delete_node200_response import DeleteNode200Response
from openapi_server.models.get_nodes_status200_response import GetNodesStatus200Response
from openapi_server.models.list_accepted_nodes200_response import ListAcceptedNodes200Response
from openapi_server.models.list_pending_nodes200_response import ListPendingNodes200Response
from openapi_server.models.node_add_inner import NodeAddInner
from openapi_server.models.node_details200_response import NodeDetails200Response
from openapi_server.models.node_inherited_properties200_response import NodeInheritedProperties200Response
from openapi_server.models.node_settings import NodeSettings
from openapi_server.models.update_node200_response import UpdateNode200Response


pytestmark = pytest.mark.asyncio

async def test_apply_policy(client):
    """Test case for apply_policy

    Trigger an agent run
    """
    headers = { 
        'Accept': 'text/plain',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/nodes/{node_id}/applyPolicy'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apply_policy_all_nodes(client):
    """Test case for apply_policy_all_nodes

    Trigger an agent run on all nodes
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/nodes/applyPolicy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_pending_node_status(client):
    """Test case for change_pending_node_status

    Update pending Node status
    """
    body = openapi_server.ChangePendingNodeStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/nodes/pending/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_nodes(client):
    """Test case for create_nodes

    Create one or several new nodes
    """
    body = [openapi_server.NodeAddInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/nodes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_node(client):
    """Test case for delete_node

    Delete a node
    """
    params = [('mode', move)]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/nodes/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nodes_status(client):
    """Test case for get_nodes_status

    Get nodes acceptation status
    """
    params = [('ids', 'default')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/nodes/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_accepted_nodes(client):
    """Test case for list_accepted_nodes

    List managed nodes
    """
    params = [('include', 'default'),
                    ('query', None),
                    ('where', None),
                    ('composition', and),
                    ('select', 'node')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/nodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pending_nodes(client):
    """Test case for list_pending_nodes

    List pending nodes
    """
    params = [('include', 'default'),
                    ('query', None),
                    ('where', None),
                    ('composition', and),
                    ('select', 'node')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/nodes/pending',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_node_details(client):
    """Test case for node_details

    Get information about a node
    """
    params = [('include', 'default')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/nodes/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_node_inherited_properties(client):
    """Test case for node_inherited_properties

    Get inherited node properties for a node
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/nodes/{node_id}/inheritedProperties'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_node(client):
    """Test case for update_node

    Update node settings and properties
    """
    body = openapi_server.NodeSettings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/nodes/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

