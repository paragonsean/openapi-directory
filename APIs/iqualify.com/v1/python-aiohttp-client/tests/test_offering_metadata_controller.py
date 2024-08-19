# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.courses_content_id_metadata_category_put_request import CoursesContentIdMetadataCategoryPutRequest
from openapi_server.models.courses_content_id_metadata_level_put_request import CoursesContentIdMetadataLevelPutRequest
from openapi_server.models.courses_content_id_metadata_tags_put_request import CoursesContentIdMetadataTagsPutRequest
from openapi_server.models.courses_content_id_metadata_topic_put_request import CoursesContentIdMetadataTopicPutRequest
from openapi_server.models.error import Error
from openapi_server.models.offering_metadata_response import OfferingMetadataResponse


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_metadata_category_put(client):
    """Test case for offerings_offering_id_metadata_category_put

    Update offering category metadata
    """
    body = openapi_server.CoursesContentIdMetadataCategoryPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/offerings/{offering_id}/metadata/category'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_metadata_level_put(client):
    """Test case for offerings_offering_id_metadata_level_put

    Update offering level metadata
    """
    body = openapi_server.CoursesContentIdMetadataLevelPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/offerings/{offering_id}/metadata/level'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_metadata_tags_put(client):
    """Test case for offerings_offering_id_metadata_tags_put

    Update offering tags metadata
    """
    body = openapi_server.CoursesContentIdMetadataTagsPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/offerings/{offering_id}/metadata/tags'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_metadata_topic_put(client):
    """Test case for offerings_offering_id_metadata_topic_put

    Update offering topic metadata
    """
    body = openapi_server.CoursesContentIdMetadataTopicPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/offerings/{offering_id}/metadata/topic'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

