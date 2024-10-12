# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_tod import ConfigTOD


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_get_args(client):
    """Test case for protocol_tod_get_args

    Show the agent's TOD argument structure
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/tod/get/args'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_get_config(client):
    """Test case for protocol_tod_get_config

    Show the agent's TOD configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/tod/get/config'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_get_statistics(client):
    """Test case for protocol_tod_get_statistics

    Show the agent's TOD statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/tod/get/statistics'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_get_stats_hdr(client):
    """Test case for protocol_tod_get_stats_hdr

    Show the TOD statistics headers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/protocol/msg/tod/get/stats_hdr',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_get_trace(client):
    """Test case for protocol_tod_get_trace

    Show the agent's TOD traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/tod/get/trace'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_gettime(client):
    """Test case for protocol_tod_gettime

    Retrieve TOD time
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/tod/gettime/server/{server_addr}/port/{port_num}/script/{script_name}/timeout/{time_sec}/retries/{num_retries}'.format(agent_num=56, server_addr='server_addr_example', port_num=56, script_name='script_name_example', time_sec=56, num_retries=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_set_config(client):
    """Test case for protocol_tod_set_config

    Set the agent's TOD configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/tod/set/config/{argument}/{value}'.format(agent_num=56, argument='argument_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_tod_set_trace(client):
    """Test case for protocol_tod_set_trace

    Set the agent's TOD traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/tod/set/trace/{enable_or_not}'.format(agent_num=56, enable_or_not='enable_or_not_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

