# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_ipmi import ConfigIPMI


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_get_args(client):
    """Test case for protocol_ipmi_get_args

    Show the agent's IPMI argument structure
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/get/args'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_get_attr(client):
    """Test case for protocol_ipmi_get_attr

    Show the outgoing message's attributes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/get/{attr}'.format(agent_num=56, attr='attr_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_get_config(client):
    """Test case for protocol_ipmi_get_config

    Show the agent's IPMI configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/get/config'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_get_statistics(client):
    """Test case for protocol_ipmi_get_statistics

    Show the agent's IPMI statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/get/statistics'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_get_stats_hdr(client):
    """Test case for protocol_ipmi_get_stats_hdr

    Show the IPMI statistics headers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/protocol/msg/ipmi/get/stats_hdr',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_get_trace(client):
    """Test case for protocol_ipmi_get_trace

    Show the agent's IPMI traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/get/trace'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_set_attr(client):
    """Test case for protocol_ipmi_set_attr

    Set the outgoing message's attributes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/set/{attr}/{value}'.format(agent_num=56, attr='attr_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_set_config(client):
    """Test case for protocol_ipmi_set_config

    Set the agent's IPMI configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/set/config/{argument}/{value}'.format(agent_num=56, argument='argument_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_ipmi_set_trace(client):
    """Test case for protocol_ipmi_set_trace

    Set the agent's IPMI traffic tracing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/ipmi/set/trace/{enable_or_not}'.format(agent_num=56, enable_or_not='enable_or_not_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

