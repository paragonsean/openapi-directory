# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_iatu_products_reports_all_csv_get(client):
    """Test case for iatu_products_reports_all_csv_get

    Get a list of products in CSV format
    """
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/products/reports/all.csv',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_products_reports_all_get(client):
    """Test case for iatu_products_reports_all_get

    Get a list of products in JSON format
    """
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/products/reports/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_products_reports_local_value_get(client):
    """Test case for iatu_products_reports_local_value_get

    Get the estimated Local Value of a product
    """
    params = [('country_code', 'GT'),
                    ('carrier_code', 'Claro'),
                    ('amount', 500),
                    ('currency_code', 'USD')]
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/products/reports/local-value',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

