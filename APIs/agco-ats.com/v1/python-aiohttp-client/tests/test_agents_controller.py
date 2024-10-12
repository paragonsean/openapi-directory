# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_agent import APIPagedResponseBuildSystemSharedDTOAgent
from openapi_server.models.build_system_shared_dto_activity_run import BuildSystemSharedDTOActivityRun
from openapi_server.models.build_system_shared_dto_agent import BuildSystemSharedDTOAgent
from openapi_server.models.build_system_shared_dto_agent_status import BuildSystemSharedDTOAgentStatus


pytestmark = pytest.mark.asyncio

async def test_agents_delete_agent(client):
    """Test case for agents_delete_agent

    Delete an Agent
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/agents/{agent_id}'.format(agent_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agents_get_agent_activity_run(client):
    """Test case for agents_get_agent_activity_run

    Get an Agent's ActivityRun
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/agents/{agent_id}/ActivityRun'.format(agent_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agents_get_agent_async(client):
    """Test case for agents_get_agent_async

    Get Agent
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/agents/{agent_id}'.format(agent_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agents_get_agents(client):
    """Test case for agents_get_agents

    Get Agents
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/agents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agents_get_current_agent_activity_run(client):
    """Test case for agents_get_current_agent_activity_run

    Get the ActivityRun of Agent associated with the current user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/agents/Current/ActivityRun',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agents_get_current_agent_async(client):
    """Test case for agents_get_current_agent_async

    Get Agent associated with the current user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/agents/Current',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_agents_post_agent(client):
    """Test case for agents_post_agent

    Create an Agent
    """
    body = openapi_server.BuildSystemSharedDTOAgent()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/agents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_agents_put_agent(client):
    """Test case for agents_put_agent

    Update an Agent
    """
    body = openapi_server.BuildSystemSharedDTOAgent()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/agents/{agent_id}'.format(agent_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_agents_put_agent_activity_run(client):
    """Test case for agents_put_agent_activity_run

    Update the ActivityRun assigned to the Agent.
    """
    body = openapi_server.BuildSystemSharedDTOActivityRun()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/agents/{agent_id}/ActivityRun'.format(agent_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_agents_put_agent_status(client):
    """Test case for agents_put_agent_status

    Update an Agent
    """
    body = openapi_server.BuildSystemSharedDTOAgentStatus()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/agents/{agent_id}/Status'.format(agent_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

