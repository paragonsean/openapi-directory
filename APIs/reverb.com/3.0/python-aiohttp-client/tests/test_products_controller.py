# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.products_reviews_id_put_request import ProductsReviewsIdPutRequest


pytestmark = pytest.mark.asyncio

async def test_products_reviews_id_get(client):
    """Test case for products_reviews_id_get

    View a review
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/products/reviews/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_reviews_id_put(client):
    """Test case for products_reviews_id_put

    Update a review
    """
    body = openapi_server.ProductsReviewsIdPutRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/products/reviews/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_slug_reviews_get(client):
    """Test case for products_slug_reviews_get

    View reviews of a comparison shopping page
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/products/{slug}/reviews'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_slug_reviews_post(client):
    """Test case for products_slug_reviews_post

    Create a review for a product
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/products/{slug}/reviews'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

