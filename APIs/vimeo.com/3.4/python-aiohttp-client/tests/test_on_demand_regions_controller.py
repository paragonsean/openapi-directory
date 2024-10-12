# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_vod_regions_request import DeleteVodRegionsRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_region import OnDemandRegion
from openapi_server.models.set_vod_regions_request import SetVodRegionsRequest


pytestmark = pytest.mark.asyncio

async def test_add_vod_region(client):
    """Test case for add_vod_region

    Add a specific region to an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/ondemand/pages/{ondemand_id}/regions/{country}'.format(country='US', ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vod_region(client):
    """Test case for delete_vod_region

    Remove a specific region from an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ondemand/pages/{ondemand_id}/regions/{country}'.format(country='US', ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vod_regions(client):
    """Test case for delete_vod_regions

    Remove a list of regions from an On Demand page
    """
    body = openapi_server.DeleteVodRegionsRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Content-Type': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ondemand/pages/{ondemand_id}/regions'.format(ondemand_id=61326),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_region(client):
    """Test case for get_region

    Get a specific On Demand region
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/regions/{country}'.format(country='US'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_regions(client):
    """Test case for get_regions

    Get all the On Demand regions
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/regions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_region(client):
    """Test case for get_vod_region

    Get a specific region of an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/regions/{country}'.format(country='US', ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_regions(client):
    """Test case for get_vod_regions

    Get all the regions of an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/regions'.format(ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_vod_regions(client):
    """Test case for set_vod_regions

    Add a list of regions to an On Demand page
    """
    body = openapi_server.SetVodRegionsRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.region+json',
        'Content-Type': 'application/vnd.vimeo.ondemand.region+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/ondemand/pages/{ondemand_id}/regions'.format(ondemand_id=61326),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

