# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_sandbox import CreateSandbox
from openapi_server.models.sandbox import Sandbox


pytestmark = pytest.mark.asyncio

async def test_create_sandbox(client):
    """Test case for create_sandbox

    createSandbox
    """
    body = {"parentSandboxName":"parentSandboxName","commitBaseTemplate":True,"name":"name","description":"description","ownerOrganisationName":"ownerOrganisationName","transportType":"HTTP"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1/sandboxes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sandbox(client):
    """Test case for delete_sandbox

    deleteSandbox
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/1/sandboxes/{sandbox_name}'.format(sandbox_name='sandbox_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sandbox_state(client):
    """Test case for delete_sandbox_state

    deleteSandboxState
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/1/sandboxes/{sandbox_name}/state'.format(sandbox_name='sandbox_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fork_sandbox(client):
    """Test case for fork_sandbox

    forkSandbox
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/1/sandboxes/{sandbox_name}/fork'.format(sandbox_name='sandbox_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sandbox(client):
    """Test case for get_sandbox

    getSandbox
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/1/sandboxes/{sandbox_name}'.format(sandbox_name='sandbox_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sandbox_state(client):
    """Test case for get_sandbox_state

    getSandboxState
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/1/sandboxes/{sandbox_name}/state'.format(sandbox_name='sandbox_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sandboxes(client):
    """Test case for get_sandboxes

    getSandboxes
    """
    params = [('filterType', 'filter_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/1/sandboxes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_sandbox(client):
    """Test case for update_sandbox

    updateSandbox
    """
    body = {"proxyStatus":"STARTED","runtimeVersion":"VERSION_1","sandboxUrl":"sandboxUrl","description":"description","apiDefinition":"None","childSandboxes":[null,null],"ipWhitelist":["ipWhitelist","ipWhitelist"],"configuredRoutes":[{"defaultLatency":2402,"loadLatency":18082,"path":"path","routeConfig":{"path":"path","latencyMultiplier":5,"method":"method","errorStrategy":"NONE","latencyMs":5,"latencyType":"NONE"},"activeLatency":True,"method":"method","transport":"transport","loadThreshold":14,"activeErrorOverride":True,"properties":{"key":"properties"},"errorOverrideType":"NONE"},{"defaultLatency":2402,"loadLatency":18082,"path":"path","routeConfig":{"path":"path","latencyMultiplier":5,"method":"method","errorStrategy":"NONE","latencyMs":5,"latencyType":"NONE"},"activeLatency":True,"method":"method","transport":"transport","loadThreshold":14,"activeErrorOverride":True,"properties":{"key":"properties"},"errorOverrideType":"NONE"}],"name":"name","transportType":"HTTP","hasRepository":True,"id":"id","stackType":"JavaScript","gitUrl":"gitUrl","properties":{"key":"{}"},"gitAccessToken":"gitAccessToken"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/1/sandboxes/{sandbox_name}'.format(sandbox_name='sandbox_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

