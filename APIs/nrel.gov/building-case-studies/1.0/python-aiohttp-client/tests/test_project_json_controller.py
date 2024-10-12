# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_document(client):
    """Test case for document

    Project Details
    """
    params = [('api_key', 'DEMO_KEY')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/building-case-studies/project/{project_id_output_format}'.format(output_format=json, project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project(client):
    """Test case for project

    A filterable list of projects.
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('search', 'search_example'),
                    ('portal', 'portal_example'),
                    ('page', 56),
                    ('city', 'city_example'),
                    ('province', 'province_example'),
                    ('region', 'region_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/building-case-studies/project.{output_format}'.format(output_format=xml),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

