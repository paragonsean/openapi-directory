# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_organization_request import PatchOrganizationRequest


pytestmark = pytest.mark.asyncio

async def test_get_organization(client):
    """Test case for get_organization

    
    """
    params = [('include_locations', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations(client):
    """Test case for get_organizations

    
    """
    params = [('paginate_limit', 20),
                    ('paginate_page', 'paginate_page_example'),
                    ('paginate_enabled', True),
                    ('sort_by', 'createdAt'),
                    ('sort_order', desc),
                    ('createdAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('createdAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('include_locations', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_organization(client):
    """Test case for patch_organization

    
    """
    body = openapi_server.PatchOrganizationRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/organizations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

