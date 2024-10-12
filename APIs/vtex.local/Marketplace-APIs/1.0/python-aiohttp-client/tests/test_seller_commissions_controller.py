# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_upsert_seller_commissions_request import BulkUpsertSellerCommissionsRequest
from openapi_server.models.upsert_seller_commissions_request import UpsertSellerCommissionsRequest


pytestmark = pytest.mark.asyncio

async def test_bulk_upsert_seller_commissions(client):
    """Test case for bulk_upsert_seller_commissions

    Upsert Seller Commissions in Bulk
    """
    body = {"categoryFullPath":null,"categoryId":"6","freightCommissionPercentage":2.43,"productCommissionPercentage":9.85}
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/seller-register/pvt/sellers/{seller_id}/commissions/categories'.format(seller_id='seller123'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_seller_commissions(client):
    """Test case for list_seller_commissions

    List Seller Commissions by seller ID
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/seller-register/pvt/sellers/{seller_id}/commissions'.format(seller_id='seller123'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_seller_commissions(client):
    """Test case for remove_seller_commissions

    Remove Seller Commissions by Category ID
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/seller-register/pvt/sellers/{seller_id}/commissions/{category_id}'.format(seller_id='seller123', category_id='6'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_seller_commissions(client):
    """Test case for retrieve_seller_commissions

    Get Seller Commissions by Category ID
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/seller-register/pvt/sellers/{seller_id}/commissions/{category_id}'.format(seller_id='seller123', category_id='6'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_seller_commissions(client):
    """Test case for upsert_seller_commissions

    Upsert Seller Commissions by Category ID
    """
    body = {"categoryFullPath":null,"categoryId":"6","freightCommissionPercentage":2.43,"productCommissionPercentage":9.85}
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/seller-register/pvt/sellers/{seller_id}/commissions/{category_id}'.format(seller_id='seller123', category_id='6'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

