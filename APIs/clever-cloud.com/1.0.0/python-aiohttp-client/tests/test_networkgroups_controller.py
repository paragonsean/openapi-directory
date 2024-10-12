# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schema1 import Schema1
from openapi_server.models.schema2 import Schema2


pytestmark = pytest.mark.asyncio

async def test_create_network_group_1(client):
    """Test case for create_network_group_1

    Create Network Group
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups'.format(owner_id='owner_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_group_external_peer_1(client):
    """Test case for create_network_group_external_peer_1

    Add external peer
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/external-peers'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_group_member_1(client):
    """Test case for create_network_group_member_1

    Add member
    """
    body = openapi_server.Schema2()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_1(client):
    """Test case for delete_network_group_1

    Delete Network Group
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_external_peer_1(client):
    """Test case for delete_network_group_external_peer_1

    Remove external peer
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/external-peers/{peer_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_member_1(client):
    """Test case for delete_network_group_member_1

    Remove member
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members/{member_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', member_id='member_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_network_group_peer_1(client):
    """Test case for delete_network_group_peer_1

    Remove peer
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_1(client):
    """Test case for get_network_group_1

    Get Network Group
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_member_1(client):
    """Test case for get_network_group_member_1

    Get member
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members/{member_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', member_id='member_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_peer_1(client):
    """Test case for get_network_group_peer_1

    Get peer
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_stream_1(client):
    """Test case for get_network_group_stream_1

    Network Group SSE
    """
    body = None
    headers = { 
        'Accept': 'text/event-stream',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/stream'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_wire_guard_configuration_1(client):
    """Test case for get_network_group_wire_guard_configuration_1

    Get WireGuard® configuration
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}/wireguard/configuration'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_network_group_wire_guard_configuration_stream_1(client):
    """Test case for get_network_group_wire_guard_configuration_stream_1

    Get WireGuard® configuration
    """
    body = None
    headers = { 
        'Accept': 'text/event-stream',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers/{peer_id}/wireguard/configuration/stream'.format(owner_id='owner_id_example', network_group_id='network_group_id_example', peer_id='peer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_list_network_group_members_1(client):
    """Test case for list_network_group_members_1

    List members
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/members'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_list_network_group_peers_1(client):
    """Test case for list_network_group_peers_1

    List peers
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups/{network_group_id}/peers'.format(owner_id='owner_id_example', network_group_id='network_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_list_network_groups_1(client):
    """Test case for list_network_groups_1

    List Network Groups
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/v4/networkgroups/organisations/{owner_id}/networkgroups'.format(owner_id='owner_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

