# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.fda_application import FDAApplication
from openapi_server.models.fda_application_list import FDAApplicationList


pytestmark = pytest.mark.asyncio

async def test_get_fda_application(client):
    """Test case for get_fda_application

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/fda_applications/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_fda_applications(client):
    """Test case for list_fda_applications

    
    """
    params = [('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/fda_applications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

