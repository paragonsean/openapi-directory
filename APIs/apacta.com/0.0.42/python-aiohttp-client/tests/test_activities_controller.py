# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activities_get200_response import ActivitiesGet200Response
from openapi_server.models.activities_post_request import ActivitiesPostRequest
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError


pytestmark = pytest.mark.asyncio

async def test_activities_activity_id_delete(client):
    """Test case for activities_activity_id_delete

    Delete an activity
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/activities/{activity_id}'.format(activity_id='activity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_activity_id_put(client):
    """Test case for activities_activity_id_put

    Edit an activity
    """
    body = openapi_server.ActivitiesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/activities/{activity_id}'.format(activity_id='activity_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_bulk_delete_delete(client):
    """Test case for activities_bulk_delete_delete

    Bulk delete activities
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/activities/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_get(client):
    """Test case for activities_get

    Get a list of activities
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/activities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_post(client):
    """Test case for activities_post

    Create an activity
    """
    body = openapi_server.ActivitiesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/activities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

