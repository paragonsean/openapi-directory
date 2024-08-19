# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_course_mappings_externalcourse_external_course_id_get(client):
    """Test case for course_mappings_externalcourse_external_course_id_get

    Find course mappings by externalCourseId
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/course-mappings/externalcourse/{external_course_id}'.format(external_course_id='external_course_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_course_mappings_get(client):
    """Test case for course_mappings_get

    Find course mappings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/course-mappings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_course_mappings_offering_id_external_course_id_delete(client):
    """Test case for course_mappings_offering_id_external_course_id_delete

    Remove course mapping
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/course-mappings/{offering_id}/{external_course_id}'.format(offering_id='offering_id_example', external_course_id='external_course_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_course_mappings_offering_id_external_course_id_put(client):
    """Test case for course_mappings_offering_id_external_course_id_put

    Add course mapping
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/course-mappings/{offering_id}/{external_course_id}'.format(offering_id='offering_id_example', external_course_id='external_course_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_course_mappings_offering_id_get(client):
    """Test case for course_mappings_offering_id_get

    Find course mappings by offeringId
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/course-mappings/{offering_id}'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

