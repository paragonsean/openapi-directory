# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aquifers_files_list200_response import AquifersFilesList200Response
from openapi_server.models.well_detail import WellDetail
from openapi_server.models.well_tag_search import WellTagSearch
from openapi_server.models.wells_list200_response import WellsList200Response


pytestmark = pytest.mark.asyncio

async def test_wells_files_list(client):
    """Test case for wells_files_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/wells/{tag}/files'.format(tag='tag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wells_list(client):
    """Test case for wells_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/wells/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wells_read(client):
    """Test case for wells_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/wells/{well_tag_number}'.format(well_tag_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wells_tags_list(client):
    """Test case for wells_tags_list

    
    """
    params = [('search', 'search_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/wells/tags/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

