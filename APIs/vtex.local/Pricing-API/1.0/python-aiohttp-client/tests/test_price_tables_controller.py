# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getallpricetablesandrules200_response_inner import Getallpricetablesandrules200ResponseInner
from openapi_server.models.getrulesforapricetable200_response import Getrulesforapricetable200Response
from openapi_server.models.pricing_pipeline_catalog_price_table_id_put_request import PricingPipelineCatalogPriceTableIdPutRequest


pytestmark = pytest.mark.asyncio

async def test_getallpricetablesandrules(client):
    """Test case for getallpricetablesandrules

    Get all price tables and their rules
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
        path='/pricing/pipeline/catalog',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getrulesforapricetable(client):
    """Test case for getrulesforapricetable

    Get rules for a price table
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
        path='/pricing/pipeline/catalog/{price_table_id}'.format(price_table_id='b2c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listpricetables(client):
    """Test case for listpricetables

    List price tables
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
        path='/pricing/tables',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricing_pipeline_catalog_price_table_id_put(client):
    """Test case for pricing_pipeline_catalog_price_table_id_put

    Update rules for a price table
    """
    body = openapi_server.PricingPipelineCatalogPriceTableIdPutRequest()
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/pricing/pipeline/catalog/{price_table_id}'.format(price_table_id='price_table_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

