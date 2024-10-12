# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.course_meta_response import CourseMetaResponse
from openapi_server.models.courses_content_id_metadata_category_put_request import CoursesContentIdMetadataCategoryPutRequest
from openapi_server.models.courses_content_id_metadata_level_put_request import CoursesContentIdMetadataLevelPutRequest
from openapi_server.models.courses_content_id_metadata_tags_put_request import CoursesContentIdMetadataTagsPutRequest
from openapi_server.models.courses_content_id_metadata_topic_put_request import CoursesContentIdMetadataTopicPutRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_courses_content_id_metadata_category_put(client):
    """Test case for courses_content_id_metadata_category_put

    Update course category
    """
    body = openapi_server.CoursesContentIdMetadataCategoryPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/courses/{content_id}/metadata/category'.format(content_id='content_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_courses_content_id_metadata_level_put(client):
    """Test case for courses_content_id_metadata_level_put

    Update course level
    """
    body = openapi_server.CoursesContentIdMetadataLevelPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/courses/{content_id}/metadata/level'.format(content_id='content_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_courses_content_id_metadata_tags_put(client):
    """Test case for courses_content_id_metadata_tags_put

    Update course tags
    """
    body = openapi_server.CoursesContentIdMetadataTagsPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/courses/{content_id}/metadata/tags'.format(content_id='content_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_courses_content_id_metadata_topic_put(client):
    """Test case for courses_content_id_metadata_topic_put

    Update course topic
    """
    body = openapi_server.CoursesContentIdMetadataTopicPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/courses/{content_id}/metadata/topic'.format(content_id='content_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

