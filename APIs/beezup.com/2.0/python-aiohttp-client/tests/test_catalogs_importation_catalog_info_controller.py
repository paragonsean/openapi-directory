# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.change_custom_column_request import ChangeCustomColumnRequest
from openapi_server.models.configure_catalog_column_catalog_request import ConfigureCatalogColumnCatalogRequest
from openapi_server.models.detected_catalog_column_list import DetectedCatalogColumnList
from openapi_server.models.importation_custom_column_list import ImportationCustomColumnList
from openapi_server.models.map_beez_up_column_request import MapBeezUPColumnRequest
from openapi_server.models.product_sample import ProductSample


pytestmark = pytest.mark.asyncio

async def test_importation_configure_catalog_column(client):
    """Test case for importation_configure_catalog_column

    Configure catalog column
    """
    body = openapi_server.ConfigureCatalogColumnCatalogRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/catalogColumns/{column_id}'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_delete_custom_column(client):
    """Test case for importation_delete_custom_column

    Delete Custom Column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/customColumns/{column_id}'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_custom_column_expression(client):
    """Test case for importation_get_custom_column_expression

    Get the encrypted custom column expression in this importation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/customColumns/{column_id}/expression'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_custom_columns(client):
    """Test case for importation_get_custom_columns

    Get custom columns currently place in this importation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/customColumns'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_detected_catalog_columns(client):
    """Test case for importation_get_detected_catalog_columns

    Get detected catalog columns during this importation.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/catalogColumns'.format(store_id='store_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_product_sample(client):
    """Test case for importation_get_product_sample

    Get the product sample related to this importation with all columns (catalog and custom)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/productSamples/{product_sample_index}'.format(store_id='store_id_example', execution_id='execution_id_example', product_sample_index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_get_product_sample_custom_column_value(client):
    """Test case for importation_get_product_sample_custom_column_value

    Get product sample custom column value related to this importation.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/productSamples/{product_sample_index}/customColumns/{column_id}'.format(store_id='store_id_example', execution_id='execution_id_example', product_sample_index=56, column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_ignore_column(client):
    """Test case for importation_ignore_column

    Ignore Column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/catalogColumns/{column_id}/ignore'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_map_catalog_column(client):
    """Test case for importation_map_catalog_column

    Map catalog column to a BeezUP column
    """
    body = openapi_server.MapBeezUPColumnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/catalogColumns/{column_id}/map'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_map_custom_column(client):
    """Test case for importation_map_custom_column

    Map custom column to a BeezUP column
    """
    body = openapi_server.MapBeezUPColumnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/customColumns/{column_id}/map'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_reattend_column(client):
    """Test case for importation_reattend_column

    Reattend Column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/catalogColumns/{column_id}/reattend'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_save_custom_column(client):
    """Test case for importation_save_custom_column

    Create or replace a custom column
    """
    body = openapi_server.ChangeCustomColumnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/customColumns/{column_id}'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_unmap_catalog_column(client):
    """Test case for importation_unmap_catalog_column

    Unmap catalog column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/catalogColumns/{column_id}/unmap'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_importation_unmap_custom_column(client):
    """Test case for importation_unmap_custom_column

    Unmap custom column
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/catalogs/{store_id}/importations/{execution_id}/customColumns/{column_id}/unmap'.format(store_id='store_id_example', execution_id='execution_id_example', column_id='column_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

