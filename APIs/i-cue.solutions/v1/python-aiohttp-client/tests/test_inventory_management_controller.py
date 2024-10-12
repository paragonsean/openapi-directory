# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_inventory_amazon_ipi_post(client):
    """Test case for inventory_amazon_ipi_post

    Calculate Amazon Inventory Performance Index (IPI)
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/amazon-ipi',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_caryying_cost_post(client):
    """Test case for inventory_caryying_cost_post

    Carrying Cost
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/caryying-cost',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_eoq_post(client):
    """Test case for inventory_eoq_post

    Calculate economic order quantity
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/eoq',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_fill_rate_post(client):
    """Test case for inventory_fill_rate_post

    Calculate fill rate
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/fill-rate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_financial_imapct_forecast_accuracy_post(client):
    """Test case for inventory_financial_imapct_forecast_accuracy_post

    Calculate financial impact of forecast accuracy
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/financial-imapct-forecast-accuracy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_inventory_turnover_post(client):
    """Test case for inventory_inventory_turnover_post

    Inventroy Turn-over
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/inventory-turnover',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_ltd_post(client):
    """Test case for inventory_ltd_post

    Calculate lead time demand
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/ltd',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_moq_post(client):
    """Test case for inventory_moq_post

    Calculate minimum order quantity
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/moq',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_optimal_service_level_post(client):
    """Test case for inventory_optimal_service_level_post

    Calculate optimal service level
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/optimal-service-level',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_reorder_point_post(client):
    """Test case for inventory_reorder_point_post

    Re-order Point
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/reorder-point',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_safety_stock_post(client):
    """Test case for inventory_safety_stock_post

    Safety Stock
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/safety-stock',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_service_level_post(client):
    """Test case for inventory_service_level_post

    Calculate service level
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/service-level',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_turns_post(client):
    """Test case for inventory_turns_post

    Calculate inventory turns
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/inventory/turns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

