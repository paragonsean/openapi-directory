# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_collection import GroupCollection
from openapi_server.models.group_contract import GroupContract
from openapi_server.models.group_create_parameters import GroupCreateParameters
from openapi_server.models.group_get_default_response import GroupGetDefaultResponse
from openapi_server.models.group_update_parameters import GroupUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_group_create_or_update(client):
    """Test case for group_create_or_update

    
    """
    parameters = {"name":"name","description":"description","externalId":"externalId","type":"custom"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_delete(client):
    """Test case for group_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_get(client):
    """Test case for group_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_list(client):
    """Test case for group_list

    
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
        path='/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_update(client):
    """Test case for group_update

    
    """
    parameters = {"name":"name","description":"description","externalId":"externalId","type":"custom"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

