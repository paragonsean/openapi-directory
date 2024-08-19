# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_iatu_number_validator_get(client):
    """Test case for iatu_number_validator_get

    Mobile number validation
    """
    params = [('country_code', 'BR'),
                    ('mobile_number', '5521983115555')]
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/number-validator',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iatu_products_promotions_get(client):
    """Test case for iatu_products_promotions_get

    Current promotions
    """
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/iatu/products/promotions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_get(client):
    """Test case for status_get

    Status check
    """
    headers = { 
        'x_idt_beyond_app_id': 'APP_ID',
        'x_idt_beyond_app_key': 'APP_KEY',
    }
    response = await client.request(
        method='GET',
        path='/v1/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

