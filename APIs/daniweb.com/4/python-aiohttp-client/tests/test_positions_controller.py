# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.endpoint_delete_positions_id import EndpointDeletePositionsID
from openapi_server.models.endpoint_patch_positions_id import EndpointPatchPositionsID
from openapi_server.models.endpoint_post_positions import EndpointPostPositions


pytestmark = pytest.mark.asyncio

async def test_positions_iddelete(client):
    """Test case for positions_iddelete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/connect/api/v4/positions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_positions_idpatch(client):
    """Test case for positions_idpatch

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('category', 'category_example')
    data.add_field('end_date', 'end_date_example')
    data.add_field('organization', 'organization_example')
    data.add_field('organization_size', 'organization_size_example')
    data.add_field('position', 'position_example')
    data.add_field('role', 'role_example')
    data.add_field('start_date', 'start_date_example')
    data.add_field('summary', 'summary_example')
    data.add_field('url', 'url_example')
    response = await client.request(
        method='PATCH',
        path='/connect/api/v4/positions/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_positions_post(client):
    """Test case for positions_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('category', 'category_example')
    data.add_field('end_date', 'end_date_example')
    data.add_field('organization', 'organization_example')
    data.add_field('organization_size', 'organization_size_example')
    data.add_field('position', 'position_example')
    data.add_field('role', 'role_example')
    data.add_field('start_date', 'start_date_example')
    data.add_field('summary', 'summary_example')
    data.add_field('url', 'url_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/positions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

