# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.area_response import AreaResponse


pytestmark = pytest.mark.asyncio

async def test_areas_get(client):
    """Test case for areas_get

    Returns list of areas
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/areas'.format(version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vversion_areas_area_ids_get(client):
    """Test case for vversion_areas_area_ids_get

    Returns details of selected area
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/areas/{area_ids}'.format(area_ids='area_ids_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

