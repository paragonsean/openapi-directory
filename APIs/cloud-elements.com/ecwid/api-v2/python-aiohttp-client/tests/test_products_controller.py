# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product import Product
from openapi_server.models.product_patch import ProductPatch
from openapi_server.models.product_post import ProductPost


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_product(client):
    """Test case for create_product

    Create a new product in eCommerce system.With the exception of the 'id' field, the required fields indicated in the 'Product' model are those required to create a new product
    """
    product = openapi_server.ProductPost()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/elements/api-v2/products',
        headers=headers,
        json=product,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_product_by_id(client):
    """Test case for delete_product_by_id

    Delete a product associated with a given ID from your eCommerce system. Specifying a product associated with a given ID that does not exist will result in an error message
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/elements/api-v2/products/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_by_id(client):
    """Test case for get_product_by_id

    Retrieve a product associated with a given ID from the eCommerce system. Specifying a product with an ID that does not exist will result in an error response
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/products/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products(client):
    """Test case for get_products

    Find products in the eCommerce system, using the provided CEQL search expression. The search expression in CEQL is the WHERE clause in a typical SQL query, but without the WHERE keyword.  If no search expression is provided, all records will be retrieved
    """
    params = [('where', 'where_example'),
                    ('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_product_by_id(client):
    """Test case for update_product_by_id

    Update a product associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the product object will be updated, and those fields not provided will be left alone. Updating a product with a specified ID that does not exist will result in an error response. <p><strong>Update supports the following fields: sku, quantity, trackQuantity, quantityDelta, warningLimit, name, price, weight, tangible, enabled, fixedShippingRateOnly, fixedShippingRate, description, wholesalePrices, compareAtPrice, productClassId</strong>
    """
    product = openapi_server.ProductPatch()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/elements/api-v2/products/{id}'.format(id='id_example'),
        headers=headers,
        json=product,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

