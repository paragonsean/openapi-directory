# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.site_type_layer import SiteTypeLayer
from openapi_server.models.site_type_response import SiteTypeResponse


pytestmark = pytest.mark.asyncio

async def test_site_types_get_sites_for_public_facing_api(client):
    """Test case for site_types_get_sites_for_public_facing_api

    Returns the layer metadata for the LayerId specified.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/sitetypes/{site_type_id}/sites'.format(site_type_id=56, version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_site_types_index(client):
    """Test case for site_types_index

    Return list of site types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/sitetypes'.format(version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

