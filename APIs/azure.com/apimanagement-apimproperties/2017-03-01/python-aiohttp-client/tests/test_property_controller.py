# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.property_collection import PropertyCollection
from openapi_server.models.property_contract import PropertyContract
from openapi_server.models.property_get_default_response import PropertyGetDefaultResponse
from openapi_server.models.property_update_parameters import PropertyUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_property_create_or_update(client):
    """Test case for property_create_or_update

    
    """
    parameters = {"id":"id"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/properties/{prop_id}'.format(prop_id='prop_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_delete(client):
    """Test case for property_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/properties/{prop_id}'.format(prop_id='prop_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_get(client):
    """Test case for property_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/properties/{prop_id}'.format(prop_id='prop_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_list(client):
    """Test case for property_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_update(client):
    """Test case for property_update

    
    """
    parameters = {"name":"name","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/properties/{prop_id}'.format(prop_id='prop_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

