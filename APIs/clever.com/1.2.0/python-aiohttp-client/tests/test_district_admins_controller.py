# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.district_admin_response import DistrictAdminResponse
from openapi_server.models.district_admins_response import DistrictAdminsResponse
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_get_district_admin(client):
    """Test case for get_district_admin

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/district_admins/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_district_admins(client):
    """Test case for get_district_admins

    
    """
    params = [('starting_after', 'starting_after_example'),
                    ('ending_before', 'ending_before_example'),
                    ('show_links', 'show_links_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.2/district_admins',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

