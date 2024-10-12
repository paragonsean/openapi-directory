# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_category_category_id_put_request import ApiCatalogPvtCategoryCategoryIdPutRequest
from openapi_server.models.category import Category
from openapi_server.models.create_category_request import CreateCategoryRequest
from openapi_server.models.get_category_tree import GetCategoryTree


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_category_category_id_get(client):
    """Test case for api_catalog_pvt_category_category_id_get

    Get Category by ID
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
        path='/api/catalog/pvt/category/{category_id}'.format(category_id=9289),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_category_category_id_put(client):
    """Test case for api_catalog_pvt_category_category_id_put

    Update Category
    """
    body = openapi_server.ApiCatalogPvtCategoryCategoryIdPutRequest()
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
        path='/api/catalog/pvt/category/{category_id}'.format(category_id=9289),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_category_post(client):
    """Test case for api_catalog_pvt_category_post

    Create Category
    """
    body = {"ActiveStoreFrontLink":True,"AdWordsRemarketingCode":null,"Description":"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.","FatherCategoryId":null,"GlobalCategoryId":800,"IsActive":True,"Keywords":"Kitchen, Laundry, Appliances","LomadeeCampaignCode":null,"Name":"Home Appliances","Score":null,"ShowBrandFilter":True,"ShowInStoreFront":True,"StockKeepingUnitSelectionMode":"SPECIFICATION","Title":"Home Appliances"}
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
        path='/api/catalog/pvt/category',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_tree(client):
    """Test case for category_tree

    Get Category Tree
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
        path='/api/catalog_system/pub/category/tree/{category_levels}'.format(category_levels='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

