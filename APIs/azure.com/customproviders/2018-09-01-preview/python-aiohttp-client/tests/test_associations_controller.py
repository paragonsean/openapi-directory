# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server.models.associations_list import AssociationsList
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_associations_create_or_update(client):
    """Test case for associations_create_or_update

    
    """
    association = {"name":"name","id":"id","type":"type","properties":{"targetResourceId":"targetResourceId","provisioningState":"Accepted"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.CustomProviders/associations/{association_name}'.format(scope='scope_example', association_name='association_name_example'),
        headers=headers,
        json=association,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_associations_delete(client):
    """Test case for associations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.CustomProviders/associations/{association_name}'.format(scope='scope_example', association_name='association_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_associations_get(client):
    """Test case for associations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CustomProviders/associations/{association_name}'.format(scope='scope_example', association_name='association_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_associations_list_all(client):
    """Test case for associations_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CustomProviders/associations'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

