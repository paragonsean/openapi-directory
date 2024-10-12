# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.catalog_column_list import CatalogColumnList
from openapi_server.models.catalog_store_index import CatalogStoreIndex
from openapi_server.models.category_list import CategoryList
from openapi_server.models.change_custom_column_expression_request import ChangeCustomColumnExpressionRequest
from openapi_server.models.change_user_column_name_request import ChangeUserColumnNameRequest
from openapi_server.models.compute_expression_request import ComputeExpressionRequest
from openapi_server.models.create_custom_column_request import CreateCustomColumnRequest
from openapi_server.models.custom_column_list import CustomColumnList
from openapi_server.models.get_products_request import GetProductsRequest
from openapi_server.models.import_already_in_progress_response import ImportAlreadyInProgressResponse
from openapi_server.models.last_manual_import_input_configuration import LastManualImportInputConfiguration
from openapi_server.models.product import Product
from openapi_server.models.product_list import ProductList
from openapi_server.models.random_product_list import RandomProductList


pytestmark = pytest.mark.asyncio

async def test_catalog_change_catalog_column_user_name(client):
    """Test case for catalog_change_catalog_column_user_name

    Change Catalog Column User Name
    """
    body = openapi_server.ChangeUserColumnNameRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/catalogColumns/{column_id}/rename'.format(store_id='store_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_change_custom_column_expression(client):
    """Test case for catalog_change_custom_column_expression

    Change custom column expression
    """
    body = openapi_server.ChangeCustomColumnExpressionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/catalogs/{store_id}/customColumns/{column_id}/expression'.format(store_id='store_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_change_custom_column_user_name(client):
    """Test case for catalog_change_custom_column_user_name

    Change Custom Column User Name
    """
    body = openapi_server.ChangeUserColumnNameRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/customColumns/{column_id}/rename'.format(store_id='store_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_compute_expression(client):
    """Test case for catalog_compute_expression

    Compute the expression for this catalog.
    """
    body = openapi_server.ComputeExpressionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/customColumns/computeExpression'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_delete_custom_column(client):
    """Test case for catalog_delete_custom_column

    Delete custom column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/catalogs/{store_id}/customColumns/{column_id}'.format(store_id='store_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_catalog_columns(client):
    """Test case for catalog_get_catalog_columns

    Get catalog column list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/catalogColumns'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_categories(client):
    """Test case for catalog_get_categories

    Get category list
    """
    headers = { 
        'Accept': 'application/json',
        'accept_encoding': ['accept_encoding_example'],
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/categories'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_custom_column_expression(client):
    """Test case for catalog_get_custom_column_expression

    Get the encrypted custom column expression
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/customColumns/{column_id}/expression'.format(store_id='store_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_custom_columns(client):
    """Test case for catalog_get_custom_columns

    Get custom column list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/customColumns'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_product_by_product_id(client):
    """Test case for catalog_get_product_by_product_id

    Get product by ProductId
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/products/{product_id}'.format(store_id='store_id_example', product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_product_by_sku(client):
    """Test case for catalog_get_product_by_sku

    Get product by Sku
    """
    params = [('sku', 'sku_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/products'.format(store_id='store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_products(client):
    """Test case for catalog_get_products

    Get product list
    """
    body = openapi_server.GetProductsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/products/list'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_get_random_products(client):
    """Test case for catalog_get_random_products

    Get random product list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/products/random'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_save_custom_column(client):
    """Test case for catalog_save_custom_column

    Create or replace a custom column
    """
    body = openapi_server.CreateCustomColumnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/catalogs/{store_id}/customColumns/{column_id}'.format(store_id='store_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_store_index(client):
    """Test case for catalog_store_index

    Get the index of the catalog API for this store
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_manual_update_last_input_config(client):
    """Test case for importation_get_manual_update_last_input_config

    Get the last input configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/inputConfiguration'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

