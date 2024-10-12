# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.adult_content_post_request import AdultContentPostRequest
from openapi_server.models.task import Task


pytestmark = pytest.mark.asyncio

async def test_adult_content_post(client):
    """Test case for adult_content_post

    Image contains nudity or sexually explicit content? [ image_url -> id ]
    """
    body = openapi_server.AdultContentPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.1/adult_content',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adult_content_task_id_get(client):
    """Test case for adult_content_task_id_get

    Gets the adult_content task [ id -> adult content task ]
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.1/adult_content/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detect_object_post(client):
    """Test case for detect_object_post

    What is that object? [ image_url -> id ]
    """
    body = openapi_server.AdultContentPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.1/detect_object',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detect_object_task_id_get(client):
    """Test case for detect_object_task_id_get

    Gets the detect_object task [ id -> detect object task]
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.1/detect_object/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_age_post(client):
    """Test case for face_age_post

    How old is the person in the image? [ image_url -> id ]
    """
    body = openapi_server.AdultContentPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.1/face_age',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_age_task_id_get(client):
    """Test case for face_age_task_id_get

    Gets the face_age task [ id -> face age task ]
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.1/face_age/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_post(client):
    """Test case for face_post

    Find all faces in the image [ image_url -> id ]
    """
    body = openapi_server.AdultContentPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.1/face',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_face_task_id_get(client):
    """Test case for face_task_id_get

    Gets the face task [ id -> face task ]
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.1/face/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

