# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_products200_response import AvailableProducts200Response
from openapi_server.models.available_products_request import AvailableProductsRequest
from openapi_server.models.product200_response import Product200Response
from openapi_server.models.product_photos200_response import ProductPhotos200Response
from openapi_server.models.product_reviews200_response import ProductReviews200Response
from openapi_server.models.search_freetext200_response import SearchFreetext200Response
from openapi_server.models.search_freetext_request import SearchFreetextRequest
from openapi_server.models.search_products200_response import SearchProducts200Response
from openapi_server.models.search_products_codes200_response import SearchProductsCodes200Response
from openapi_server.models.search_products_codes_request import SearchProductsCodesRequest
from openapi_server.models.search_products_request import SearchProductsRequest


pytestmark = pytest.mark.asyncio

async def test_available_products(client):
    """Test case for available_products

    /available/products
    """
    body = {"currencyCode":"USD","endDate":"2020-12-31","numAdults":1,"productCodes":["5010SYDNEY","2280SUN","9169P50"],"startDate":"2020-12-21"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/available/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product(client):
    """Test case for product

    /product
    """
    params = [('currencyCode', 'currency_code_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('voucherOption', 'voucher_option_example'),
                    ('code', '5010SYDNEY'),
                    ('showUnavailable', false),
                    ('excludeTourGradeAvailability', True)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/product',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_photos(client):
    """Test case for product_photos

    /product/photos
    """
    params = [('topX', '1-3'),
                    ('code', '5010SYDNEY'),
                    ('showUnavailable', false)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/product/photos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_reviews(client):
    """Test case for product_reviews

    /product/reviews
    """
    params = [('sortOrder', 'sort_order_example'),
                    ('topX', '1-3'),
                    ('code', '5010SYDNEY'),
                    ('showUnavailable', false)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/product/reviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_freetext(client):
    """Test case for search_freetext

    /search/freetext
    """
    body = {"currencyCode":"EUR","destId":684,"searchTypes":["ATTRACTION","RECOMMENDATION"],"text":"grand","topX":"1-3"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/search/freetext',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_products(client):
    """Test case for search_products

    /search/products
    """
    body = {"destId":684,"sortOrder":"REVIEW_AVG_RATING_D","subCatId":26052,"topX":"1-3"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/search/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_products_codes(client):
    """Test case for search_products_codes

    /search/products/codes
    """
    body = {"currencyCode":"USD","productCodes":["123457890"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/search/products/codes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

