# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_orders import GetOrders
from openapi_server.models.get_orders_shipments import GetOrdersShipments
from openapi_server.models.orders_shipments import OrdersShipments


pytestmark = pytest.mark.asyncio

async def test_orders_get(client):
    """Test case for orders_get

    Returns orders details
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_shipments_delivered_get(client):
    """Test case for orders_shipments_delivered_get

    Returns list of shipments
    """
    params = [('status', 'status_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/shipments/delivered',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_shipments_delivered_post(client):
    """Test case for orders_shipments_delivered_post

    Bulk update of order shipments
    """
    ordersshipments = {"shipments":[{"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","trackingUrl":"trackingUrl","sellerShipmentId":"sellerShipmentId","invoice":{"linkXml":"linkXml","number":"number","accessKey":"accessKey","serie":"serie","cnpj":"cnpj","issuedAt":"2000-01-23T04:56:07.000+00:00","linkDanfe":"linkDanfe"},"items":[{"quantity":9,"skuSellerId":"skuSellerId"},{"quantity":9,"skuSellerId":"skuSellerId"}],"order":"order","status":"status"},{"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","trackingUrl":"trackingUrl","sellerShipmentId":"sellerShipmentId","invoice":{"linkXml":"linkXml","number":"number","accessKey":"accessKey","serie":"serie","cnpj":"cnpj","issuedAt":"2000-01-23T04:56:07.000+00:00","linkDanfe":"linkDanfe"},"items":[{"quantity":9,"skuSellerId":"skuSellerId"},{"quantity":9,"skuSellerId":"skuSellerId"}],"order":"order","status":"status"}]}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/orders/shipments/delivered',
        headers=headers,
        json=ordersshipments,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_shipments_shipped_get(client):
    """Test case for orders_shipments_shipped_get

    Returns a list of shipments shipped
    """
    params = [('status', 'status_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/shipments/shipped',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_shipments_shipped_post(client):
    """Test case for orders_shipments_shipped_post

    Bulk update of order shipments
    """
    ordersshipments = {"shipments":[{"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","trackingUrl":"trackingUrl","sellerShipmentId":"sellerShipmentId","invoice":{"linkXml":"linkXml","number":"number","accessKey":"accessKey","serie":"serie","cnpj":"cnpj","issuedAt":"2000-01-23T04:56:07.000+00:00","linkDanfe":"linkDanfe"},"items":[{"quantity":9,"skuSellerId":"skuSellerId"},{"quantity":9,"skuSellerId":"skuSellerId"}],"order":"order","status":"status"},{"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","trackingUrl":"trackingUrl","sellerShipmentId":"sellerShipmentId","invoice":{"linkXml":"linkXml","number":"number","accessKey":"accessKey","serie":"serie","cnpj":"cnpj","issuedAt":"2000-01-23T04:56:07.000+00:00","linkDanfe":"linkDanfe"},"items":[{"quantity":9,"skuSellerId":"skuSellerId"},{"quantity":9,"skuSellerId":"skuSellerId"}],"order":"order","status":"status"}]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/orders/shipments/shipped',
        headers=headers,
        json=ordersshipments,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_approved_get(client):
    """Test case for orders_status_approved_get

    Return list of approved orders
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/status/approved',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_canceled_get(client):
    """Test case for orders_status_canceled_get

    Returns lists of canceled orders
    """
    params = [('offset', 56),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/status/canceled',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_delivered_get(client):
    """Test case for orders_status_delivered_get

    Returns a list of orders successfully delivered associated with this seller.
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/status/delivered',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_new_get(client):
    """Test case for orders_status_new_get

    Returns a list of orders flagged as new.
    """
    params = [('offset', 56),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/status/new',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_partially_delivered_get(client):
    """Test case for orders_status_partially_delivered_get

    Returns a list of partially deliverd orders
    """
    params = [('offset', 56),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/status/partiallyDelivered',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_partially_sent_get(client):
    """Test case for orders_status_partially_sent_get

    Returns a list of orders partially fullfiled
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/status/partiallySent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_sent_get(client):
    """Test case for orders_status_sent_get

    Returns a list with orders fully sent
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/orders/status/sent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

