# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activation_response import ActivationResponse
from openapi_server.models.course_meta_response import CourseMetaResponse
from openapi_server.models.course_response import CourseResponse
from openapi_server.models.courses_root_content_id_permissions_user_email_post201_response import CoursesRootContentIdPermissionsUserEmailPost201Response
from openapi_server.models.error import Error
from openapi_server.models.permission_to_be_granted_to_the_user import PermissionToBeGrantedToTheUser
from openapi_server.models.user_permission import UserPermission


pytestmark = pytest.mark.asyncio

async def test_courses_content_id_activations_get(client):
    """Test case for courses_content_id_activations_get

    Find activations for a contentId
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{content_id}/activations'.format(content_id='content_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_courses_content_id_get(client):
    """Test case for courses_content_id_get

    Find course by contentId
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{content_id}'.format(content_id='content_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_courses_content_id_permissions_get(client):
    """Test case for courses_content_id_permissions_get

    Find users who have access to the contentId provided
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{content_id}/permissions'.format(content_id='content_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_courses_get(client):
    """Test case for courses_get

    Find courses
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_courses_root_content_id_permissions_user_email_post(client):
    """Test case for courses_root_content_id_permissions_user_email_post

    Update course access
    """
    body = openapi_server.PermissionToBeGrantedToTheUser()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{root_content_id}/permissions/{user_email}'.format(root_content_id='root_content_id_example', user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

