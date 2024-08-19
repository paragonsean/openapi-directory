# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.barcode import Barcode
from openapi_server.models.issuing_country import IssuingCountry
from openapi_server.models.product import Product
from openapi_server.models.verify_checksum import VerifyChecksum


pytestmark = pytest.mark.asyncio

async def test_barcode_image(client):
    """Test case for barcode_image

    Generate a PNG barcode image
    """
    params = [('op', 'op_example'),
                    ('ean', 56),
                    ('width', 102),
                    ('height', 50),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/barcode-image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_barcode_lookup(client):
    """Test case for barcode_lookup

    Look up an EAN
    """
    params = [('op', 'op_example'),
                    ('ean', 56),
                    ('language', 1),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/barcode-lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_barcode_prefix_search(client):
    """Test case for barcode_prefix_search

    Query the database for all barcodes with the same beginning
    """
    params = [('op', 'op_example'),
                    ('prefix', 'prefix_example'),
                    ('language', 1),
                    ('page', 0),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/barcode-prefix-search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_search(client):
    """Test case for category_search

    Search for products form a certain category
    """
    params = [('op', 'op_example'),
                    ('category', 56),
                    ('name', 'name_example'),
                    ('language', 99),
                    ('page', 0),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/category-search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issuing_country(client):
    """Test case for issuing_country

    Search for a issuing country of a barcode
    """
    params = [('op', 'op_example'),
                    ('ean', 56),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/issuing-country',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search(client):
    """Test case for product_search

    Search by product name
    """
    params = [('op', 'op_example'),
                    ('name', 'name_example'),
                    ('language', 99),
                    ('page', 0),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/product-search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_checksum(client):
    """Test case for verify_checksum

    Verify the checksum of an EAN code
    """
    params = [('op', 'op_example'),
                    ('ean', 56),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/verify-checksum',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

