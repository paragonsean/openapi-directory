# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_syslog import ConfigSYSLOG
from openapi_server.models.syslog_msg import SyslogMsg


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_get_args(client):
    """Test case for protocol_syslog_get_args

    Show the agent's SYSLOG argument structure
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/get/args'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_get_attr(client):
    """Test case for protocol_syslog_get_attr

    Show the outgoing message's attributes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/get/{attr}'.format(agent_num=56, attr='attr_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_get_config(client):
    """Test case for protocol_syslog_get_config

    Show the agent's SYSLOG configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/get/config'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_get_statistics(client):
    """Test case for protocol_syslog_get_statistics

    Show the agent's SYSLOG statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/get/statistics'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_get_stats_hdr(client):
    """Test case for protocol_syslog_get_stats_hdr

    Show the SYSLOG statistics headers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/protocol/msg/syslog/get/stats_hdr',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_get_trace(client):
    """Test case for protocol_syslog_get_trace

    Show the agent's SYSLOG traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/get/trace'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_send(client):
    """Test case for protocol_syslog_send

    Set the agent's SYSLOG traffic tracing
    """
    body = {"sequence":"sequence","hostname":"hostname","message":"message","separator":"separator","timestamp":"timestamp"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/send/{pri}'.format(agent_num=56, pri=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_set_attr(client):
    """Test case for protocol_syslog_set_attr

    Set the outgoing message's attributes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/set/{attr}/{value}'.format(agent_num=56, attr='attr_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_set_config(client):
    """Test case for protocol_syslog_set_config

    Set the agent's SYSLOG configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/set/config/{argument}/{value}'.format(agent_num=56, argument='argument_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_syslog_set_trace(client):
    """Test case for protocol_syslog_set_trace

    Set the agent's SYSLOG traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/syslog/set/trace/{enable_or_not}'.format(agent_num=56, enable_or_not='enable_or_not_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

