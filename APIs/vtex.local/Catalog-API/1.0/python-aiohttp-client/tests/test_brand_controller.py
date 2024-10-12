# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.brand_create_update import BrandCreateUpdate
from openapi_server.models.brand_get import BrandGet
from openapi_server.models.brand_list_per_page200_response import BrandListPerPage200Response


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_brand_brand_id_delete(client):
    """Test case for api_catalog_pvt_brand_brand_id_delete

    Delete Brand
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/brand/{brand_id}'.format(brand_id='123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_brand_brand_id_get(client):
    """Test case for api_catalog_pvt_brand_brand_id_get

    Get Brand and context
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/brand/{brand_id}'.format(brand_id='123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_brand_brand_id_put(client):
    """Test case for api_catalog_pvt_brand_brand_id_put

    Update Brand
    """
    body = {"Active":True,"AdWordsRemarketingCode":"","Id":2000013,"Keywords":"orma","LinkId":null,"LomadeeCampaignCode":"","MenuHome":True,"Name":"Orma Carbono2","Score":null,"SiteTitle":"Orma Carbon2","Text":"Orma Carbon2"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog/pvt/brand/{brand_id}'.format(brand_id='123'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_brand_post(client):
    """Test case for api_catalog_pvt_brand_post

    Create Brand
    """
    body = {"Active":True,"AdWordsRemarketingCode":"","Id":2000013,"Keywords":"orma","LinkId":null,"LomadeeCampaignCode":"","MenuHome":True,"Name":"Orma Carbono2","Score":null,"SiteTitle":"Orma Carbon2","Text":"Orma Carbon2"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/brand',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_brand(client):
    """Test case for brand

    Get Brand
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/brand/{brand_id}'.format(brand_id='123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_brand_list(client):
    """Test case for brand_list

    Get Brand List
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/brand/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_brand_list_per_page(client):
    """Test case for brand_list_per_page

    Get Brand List Per Page
    """
    params = [('pageSize', 5),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/brand/pagedlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

