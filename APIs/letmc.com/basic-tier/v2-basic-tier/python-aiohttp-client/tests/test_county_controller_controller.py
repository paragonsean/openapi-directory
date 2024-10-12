# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branch_model_results import BranchModelResults
from openapi_server.models.county_model import CountyModel
from openapi_server.models.county_model_results import CountyModelResults


pytestmark = pytest.mark.asyncio

async def test_county_controller_get_counties_branches(client):
    """Test case for county_controller_get_counties_branches

    A collection of branches that manage a specific county
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/county/counties/{county_id}/branches'.format(short_name='short_name_example', county_id='county_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_county_counties_county_idget(client):
    """Test case for v2_tier2_short_name_county_counties_county_idget

    Get a specific county given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/county/counties/{county_id}'.format(short_name='short_name_example', county_id='county_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_county_counties_get(client):
    """Test case for v2_tier2_short_name_county_counties_get

    A collection of all counties available for a company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/county/counties'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

