# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.site_response import SiteResponse


pytestmark = pytest.mark.asyncio

async def test_sites_index(client):
    """Test case for sites_index

    Get a list of sites
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/sites'.format(version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vversion_sites_site_ids_get(client):
    """Test case for vversion_sites_site_ids_get

    Get selected sites
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/sites/{site_ids}'.format(site_ids='site_ids_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

