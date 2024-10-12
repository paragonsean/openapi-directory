# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.area_model import AreaModel
from openapi_server.models.area_model_results import AreaModelResults


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_area_areas_area_idget(client):
    """Test case for v2_tier2_short_name_area_areas_area_idget

    Get a specific area given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/area/areas/{area_id}'.format(short_name='short_name_example', area_id='area_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_area_areas_get(client):
    """Test case for v2_tier2_short_name_area_areas_get

    A collection of all the areas for a company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/area/areas'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

