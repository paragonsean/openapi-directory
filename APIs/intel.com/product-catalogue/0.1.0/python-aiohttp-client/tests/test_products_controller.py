# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.complete_codename_lsit import CompleteCodenameLsit
from openapi_server.models.detailed_ordering_level_info import DetailedOrderingLevelInfo
from openapi_server.models.detailed_product_information import DetailedProductInformation
from openapi_server.models.product_listing_level_info import ProductListingLevelInfo
from openapi_server.models.unsuccessful_operation import UnsuccessfulOperation


pytestmark = pytest.mark.asyncio

async def test_get_code_name(client):
    """Test case for get_code_name

    5. Get list of codename details for Intel products.
    """
    params = [('locale_geo_id', 'locale_geo_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ClientId': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/products/get-codename',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_info(client):
    """Test case for get_product_info

    2. Get complete product info with product id.
    """
    params = [('locale_geo_id', 'locale_geo_id_example'),
                    ('product_id', 'product_id_example'),
                    ('include_reference', 'include_reference_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ClientId': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/products/get-products-info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_list(client):
    """Test case for get_product_list

    1. Find products by product id or category id
    """
    params = [('locale_geo_id', 'locale_geo_id_example'),
                    ('category_id', 'category_id_example'),
                    ('product_id', 'product_id_example'),
                    ('highlights', 'highlights_example'),
                    ('sort', 'sort_example'),
                    ('filters', 'filters_example'),
                    ('per_page', 56),
                    ('page_no', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ClientId': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/products/get-products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getorderinginfo(client):
    """Test case for getorderinginfo

    3. Get ordering info for product id's requested.
    """
    params = [('product_id', 'product_id_example'),
                    ('locale_geo_id', 'locale_geo_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ClientId': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/products/get-ordering-info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

