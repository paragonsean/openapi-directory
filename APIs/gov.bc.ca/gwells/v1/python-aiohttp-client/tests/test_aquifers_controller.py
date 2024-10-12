# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aquifer import Aquifer
from openapi_server.models.aquifer_serializer_basic import AquiferSerializerBasic
from openapi_server.models.aquifers_files_list200_response import AquifersFilesList200Response
from openapi_server.models.aquifers_list200_response import AquifersList200Response


pytestmark = pytest.mark.asyncio

async def test_aquifers_files_list(client):
    """Test case for aquifers_files_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifers/{aquifer_id}/files'.format(aquifer_id='aquifer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifers_list(client):
    """Test case for aquifers_list

    
    """
    params = [('aquifer_id', 3.4),
                    ('ordering', 'ordering_example'),
                    ('search', 'search_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifers/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifers_names_list(client):
    """Test case for aquifers_names_list

    
    """
    params = [('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifers/names/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifers_read(client):
    """Test case for aquifers_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifers/{aquifer_id}'.format(aquifer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

