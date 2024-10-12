# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.buy_recommendation_response import BuyRecommendationResponse
from openapi_server.models.keyword_search_response import KeywordSearchResponse
from openapi_server.models.product_details_response import ProductDetailsResponse
from openapi_server.models.sort_option_response import SortOptionResponse


pytestmark = pytest.mark.asyncio

async def test_keyword_search(client):
    """Test case for keyword_search

    fetch results auf a keyword search on Amazon
    """
    params = [('keyword', 'keyword_example'),
                    ('domainCode', 'domain_code_example'),
                    ('sortBy', 'relevanceblender'),
                    ('numberOfProducts', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/amz/amazon-search-by-keyword',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_buy_recommendation(client):
    """Test case for request_buy_recommendation

    request buy recommendations to a given product
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/amz/amazon-lookup-buy-recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_product(client):
    """Test case for request_product

    lookup product information
    """
    params = [('url', 'url_example'),
                    ('size', 'size_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/amz/amazon-lookup-product',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sort_options(client):
    """Test case for sort_options

    request available sort options to use in keyword search
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/amz/sort-options',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

