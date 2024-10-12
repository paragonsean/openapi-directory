# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_published_products_code200_response import GetPublishedProductsCode200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.published_products import PublishedProducts


pytestmark = pytest.mark.asyncio

async def test_get_published_products(client):
    """Test case for get_published_products

    Get list of published products
    """
    params = [('search', 'search_example'),
                    ('scope', 'scope_example'),
                    ('locales', 'locales_example'),
                    ('attributes', 'attributes_example'),
                    ('pagination_type', page),
                    ('page', 1),
                    ('search_after', 'cursor to the first page'),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/published-products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_published_products_code(client):
    """Test case for get_published_products_code

    Get a published product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/published-products/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

