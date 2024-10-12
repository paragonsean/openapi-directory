# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aquifers_files_list200_response import AquifersFilesList200Response
from openapi_server.models.person_list import PersonList
from openapi_server.models.person_name import PersonName


pytestmark = pytest.mark.asyncio

async def test_drillers_files_list(client):
    """Test case for drillers_files_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/drillers/{person_guid}/files'.format(person_guid='person_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drillers_list(client):
    """Test case for drillers_list

    
    """
    params = [('search', 'search_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/drillers/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drillers_names_list(client):
    """Test case for drillers_names_list

    
    """
    params = [('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/drillers/names/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

