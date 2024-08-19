# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.district_response import DistrictResponse
from openapi_server.models.not_found import NotFound
from openapi_server.models.school_response import SchoolResponse
from openapi_server.models.section_response import SectionResponse
from openapi_server.models.sections_response import SectionsResponse
from openapi_server.models.students_response import StudentsResponse
from openapi_server.models.teacher_response import TeacherResponse
from openapi_server.models.teachers_response import TeachersResponse


pytestmark = pytest.mark.asyncio

async def test_get_district_for_section(client):
    """Test case for get_district_for_section

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/sections/{id}/district'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_school_for_section(client):
    """Test case for get_school_for_section

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/sections/{id}/school'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_section(client):
    """Test case for get_section

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/sections/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sections(client):
    """Test case for get_sections

    
    """
    params = [('limit', 56),
                    ('starting_after', 'starting_after_example'),
                    ('ending_before', 'ending_before_example'),
                    ('where', 'where_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/sections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_students_for_section(client):
    """Test case for get_students_for_section

    
    """
    params = [('limit', 56),
                    ('starting_after', 'starting_after_example'),
                    ('ending_before', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/sections/{id}/students'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teacher_for_section(client):
    """Test case for get_teacher_for_section

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/sections/{id}/teacher'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teachers_for_section(client):
    """Test case for get_teachers_for_section

    
    """
    params = [('limit', 56),
                    ('starting_after', 'starting_after_example'),
                    ('ending_before', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/sections/{id}/teachers'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

