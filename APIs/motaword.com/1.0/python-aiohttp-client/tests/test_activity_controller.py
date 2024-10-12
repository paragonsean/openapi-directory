# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_list import ActivityList
from openapi_server.models.comment import Comment
from openapi_server.models.comment_list import CommentList
from openapi_server.models.error import Error
from openapi_server.models.new_sales_activity import NewSalesActivity
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.sales_activities import SalesActivities
from openapi_server.models.sales_activity_type import SalesActivityType


pytestmark = pytest.mark.asyncio

async def test_get_activities(client):
    """Test case for get_activities

    Monitor project activities
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/activities'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_activity(client):
    """Test case for get_activity

    View an activity
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/activities/{activity_id}'.format(project_id=74, activity_id=6879),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_activity_comments(client):
    """Test case for get_activity_comments

    View activity comments
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/activities/{activity_id}/comments'.format(project_id=74, activity_id=6879),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments(client):
    """Test case for get_comments

    View all project comments
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/comments'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sales_activities(client):
    """Test case for get_sales_activities

    Get sales activities for a project
    """
    params = [('excludeOwner', 'exclude_owner_example'),
                    ('type', openapi_server.SalesActivityType())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/sales/activities'.format(id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_insert_sales_activity(client):
    """Test case for insert_sales_activity

    Insert sales activity for a project
    """
    body = {"subject":"subject","type":"type","timestamp":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/sales/activities'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_submit_comment(client):
    """Test case for submit_comment

    Submit comment to an activity
    """
    body = {"comment":"comment","links":{"activity":{"href":"href"},"self":{"href":"href"},"project":{"href":"href"}},"id":6,"commented_at":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{project_id}/activities/{activity_id}'.format(project_id=74, activity_id=6879),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

