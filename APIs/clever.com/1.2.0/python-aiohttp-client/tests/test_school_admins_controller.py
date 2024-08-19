# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.school_admin_response import SchoolAdminResponse
from openapi_server.models.school_admins_response import SchoolAdminsResponse
from openapi_server.models.schools_response import SchoolsResponse


pytestmark = pytest.mark.asyncio

async def test_get_school_admin(client):
    """Test case for get_school_admin

    
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/school_admins/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_school_admins(client):
    """Test case for get_school_admins

    
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
        path='/v1.2/school_admins',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schools_for_school_admin(client):
    """Test case for get_schools_for_school_admin

    
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
        path='/v1.2/school_admins/{id}/schools'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

