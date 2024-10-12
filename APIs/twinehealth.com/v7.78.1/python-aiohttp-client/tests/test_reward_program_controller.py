# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_program_request import CreateRewardProgramRequest
from openapi_server.models.create_reward_program_response import CreateRewardProgramResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse
from openapi_server.models.fetch_reward_program_response import FetchRewardProgramResponse
from openapi_server.models.fetch_reward_programs_response import FetchRewardProgramsResponse


pytestmark = pytest.mark.asyncio

async def test_create_reward_program(client):
    """Test case for create_reward_program

    Create a reward program
    """
    body = openapi_server.CreateRewardProgramRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/reward_program',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_program(client):
    """Test case for fetch_reward_program

    Get a reward program
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_program/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_program_group(client):
    """Test case for fetch_reward_program_group

    Get group for a reward program
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_program/{id}/group'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_programs(client):
    """Test case for fetch_reward_programs

    List reward programs
    """
    params = [('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_program',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

