# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_sk_useller200_response import GetSKUseller200Response


pytestmark = pytest.mark.asyncio

async def test_api_catalog_system_pvt_skuseller_changenotification_seller_id_seller_sku_id_post(client):
    """Test case for api_catalog_system_pvt_skuseller_changenotification_seller_id_seller_sku_id_post

    Change Notification with Seller ID and Seller SKU ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog_system/pvt/skuseller/changenotification/{seller_id}/{seller_sku_id}'.format(seller_id='101', seller_sku_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_notification(client):
    """Test case for change_notification

    Change Notification with SKU ID
    """
    headers = { 
        'Accept': 'text/plain',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog_system/pvt/skuseller/changenotification/{sku_id}'.format(sku_id='10'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sk_usellerassociation(client):
    """Test case for delete_sk_usellerassociation

    Remove a seller's SKU binding
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog_system/pvt/skuseller/remove/{seller_id}/{seller_sku_id}'.format(seller_id='101', seller_sku_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sk_useller(client):
    """Test case for get_sk_useller

    Get details of a seller's SKU
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
        path='/api/catalog_system/pvt/skuseller/{seller_id}/{seller_sku_id}'.format(seller_id='101', seller_sku_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

