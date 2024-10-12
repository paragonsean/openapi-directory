# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_site_metadata(client):
    """Test case for get_site_metadata

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/metadata'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_site_metadata(client):
    """Test case for update_site_metadata

    
    """
    metadata = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/metadata'.format(site_id='site_id_example'),
        headers=headers,
        json=metadata,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

