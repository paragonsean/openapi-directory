# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_opportunities200_ok import GetCharactersCharacterIdOpportunities200Ok
from openapi_server.models.get_opportunities_groups_group_id_ok import GetOpportunitiesGroupsGroupIdOk
from openapi_server.models.get_opportunities_tasks_task_id_ok import GetOpportunitiesTasksTaskIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_opportunities(client):
    """Test case for get_characters_character_id_opportunities

    Get a character's completed tasks
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/opportunities'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_opportunities_groups(client):
    """Test case for get_opportunities_groups

    Get opportunities groups
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/opportunities/groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_opportunities_groups_group_id(client):
    """Test case for get_opportunities_groups_group_id

    Get opportunities group
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/opportunities/groups/{group_id}'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_opportunities_tasks(client):
    """Test case for get_opportunities_tasks

    Get opportunities tasks
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/opportunities/tasks/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_opportunities_tasks_task_id(client):
    """Test case for get_opportunities_tasks_task_id

    Get opportunities task
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/opportunities/tasks/{task_id}'.format(task_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

