# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_projects_format_get200_response import ApiProjectsFormatGet200Response
from openapi_server.models.project import Project


pytestmark = pytest.mark.asyncio

async def test_api_get(client):
    """Test case for api_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/api',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_projects_format_get(client):
    """Test case for api_projects_format_get

    
    """
    params = [('updatedSince', '2013-10-20'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/projects{.format}'.format(format2='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_projects_id_format_get(client):
    """Test case for api_projects_id_format_get

    
    """
    params = [('format', xml)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/projects/{id_format}'.format(id=56, format2='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

