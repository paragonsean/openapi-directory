# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_proxy import ConfigPROXY


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_get_args(client):
    """Test case for protocol_proxy_get_args

    Show the agent's PROXY argument structure
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/get/args'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_get_config(client):
    """Test case for protocol_proxy_get_config

    Show the agent's PROXY configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/get/config'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_get_statistics(client):
    """Test case for protocol_proxy_get_statistics

    Show the agent's PROXY statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/get/statistics'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_get_stats_hdr(client):
    """Test case for protocol_proxy_get_stats_hdr

    Show the PROXY statistics headers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/protocol/msg/proxy/get/stats_hdr',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_get_trace(client):
    """Test case for protocol_proxy_get_trace

    Show the agent's PROXY traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/get/trace'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_port_add(client):
    """Test case for protocol_proxy_port_add

    Add individual proxy target on the agent and the simulator host
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/port/add/{port}/{target}/{target_port}'.format(agent_num=56, port=56, target='target_example', target_port=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_port_isstarted(client):
    """Test case for protocol_proxy_port_isstarted

    Check individual target
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/port/isStarted/{port}'.format(agent_num=56, port=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_port_list(client):
    """Test case for protocol_proxy_port_list

    List all proxy targets
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/port/list'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_port_remove(client):
    """Test case for protocol_proxy_port_remove

    Remove individual proxy target on the agent and the simulator host
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/port/remove/{port}'.format(agent_num=56, port=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_port_start(client):
    """Test case for protocol_proxy_port_start

    Start additional target
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/port/start/{port}'.format(agent_num=56, port=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_port_stop(client):
    """Test case for protocol_proxy_port_stop

    Stop additional target
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/port/stop/{port}'.format(agent_num=56, port=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_set_config(client):
    """Test case for protocol_proxy_set_config

    Set the agent's PROXY configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/set/config/{argument}/{value}'.format(agent_num=56, argument='argument_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_proxy_set_trace(client):
    """Test case for protocol_proxy_set_trace

    Set the agent's PROXY traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/proxy/set/trace/{enable_or_not}'.format(agent_num=56, enable_or_not='enable_or_not_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

