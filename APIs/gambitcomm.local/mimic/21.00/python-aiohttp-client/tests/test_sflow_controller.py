# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_sflow import ConfigSFLOW


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_get_args(client):
    """Test case for protocol_sflow_get_args

    Show the agent's SFLOW argument structure
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/get/args'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_get_config(client):
    """Test case for protocol_sflow_get_config

    Show the agent's SFLOW configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/get/config'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_get_statistics(client):
    """Test case for protocol_sflow_get_statistics

    Show the agent's SFLOW statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/get/statistics'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_get_stats_hdr(client):
    """Test case for protocol_sflow_get_stats_hdr

    Show the SFLOW statistics headers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/protocol/msg/sflow/get/stats_hdr',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_get_trace(client):
    """Test case for protocol_sflow_get_trace

    Show the agent's SFLOW traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/get/trace'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_halt(client):
    """Test case for protocol_sflow_halt

    Halt SFLOW traffic
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/halt'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_reload(client):
    """Test case for protocol_sflow_reload

    Reload SFLOW configuration before resuming traffic
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/reload'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_resume(client):
    """Test case for protocol_sflow_resume

    Resuming traffic
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/resume'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_set_config(client):
    """Test case for protocol_sflow_set_config

    Set the agent's SFLOW configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/set/config/{argument}/{value}'.format(agent_num=56, argument='argument_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_sflow_set_trace(client):
    """Test case for protocol_sflow_set_trace

    Set the agent's SFLOW traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/sflow/set/trace/{enable_or_not}'.format(agent_num=56, enable_or_not='enable_or_not_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

