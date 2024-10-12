# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_supporting_relationship_request import AddSupportingRelationshipRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_goal_relationship200_response import GetGoalRelationship200Response
from openapi_server.models.get_goal_relationships200_response import GetGoalRelationships200Response
from openapi_server.models.remove_supporting_relationship_request import RemoveSupportingRelationshipRequest
from openapi_server.models.update_goal_relationship_request import UpdateGoalRelationshipRequest


pytestmark = pytest.mark.asyncio

async def test_add_supporting_relationship(client):
    """Test case for add_supporting_relationship

    Add a supporting goal relationship
    """
    body = openapi_server.AddSupportingRelationshipRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/goals/{goal_gid}/addSupportingRelationship'.format(goal_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_goal_relationship(client):
    """Test case for get_goal_relationship

    Get a goal relationship
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/goal_relationships/{goal_relationship_gid}'.format(goal_relationship_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_goal_relationships(client):
    """Test case for get_goal_relationships

    Get goal relationships
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('supported_goal', '12345'),
                    ('resource_subtype', 'subgoal')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/goal_relationships',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_supporting_relationship(client):
    """Test case for remove_supporting_relationship

    Removes a supporting goal relationship
    """
    body = openapi_server.RemoveSupportingRelationshipRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/goals/{goal_gid}/removeSupportingRelationship'.format(goal_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_goal_relationship(client):
    """Test case for update_goal_relationship

    Update a goal relationship
    """
    body = openapi_server.UpdateGoalRelationshipRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/1.0/goal_relationships/{goal_relationship_gid}'.format(goal_relationship_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

