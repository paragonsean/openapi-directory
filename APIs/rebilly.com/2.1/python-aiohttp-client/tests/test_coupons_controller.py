# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.coupon import Coupon
from openapi_server.models.coupon_expiration import CouponExpiration
from openapi_server.models.coupon_redemption import CouponRedemption
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError


pytestmark = pytest.mark.asyncio

async def test_get_coupon(client):
    """Test case for get_coupon

    Retrieve a coupon
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/coupons/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_coupon_collection(client):
    """Test case for get_coupon_collection

    Retrieve a list of coupons
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/coupons',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_coupon_redemption(client):
    """Test case for get_coupon_redemption

    Retrieve a coupon redemption with specified identifier string
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/coupons-redemptions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_coupon_redemption_collection(client):
    """Test case for get_coupon_redemption_collection

    Retrieve a list of coupon redemptions
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/coupons-redemptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_coupon(client):
    """Test case for post_coupon

    Create a coupon
    """
    body = {"redemptionsCount":0,"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"issuedTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","description":"description","discount":{"type":"fixed"},"restrictions":[{"type":"discounts-per-redemption"},{"type":"discounts-per-redemption"}],"id":"","expiredTime":"2000-01-23T04:56:07.000+00:00","status":"draft"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/coupons',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_coupon_expiration(client):
    """Test case for post_coupon_expiration

    Set a coupon's expiration time
    """
    body = {"expiredTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/coupons/{id}/expiration'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_coupon_redemption(client):
    """Test case for post_coupon_redemption

    Redeem a coupon
    """
    body = {"additionalRestrictions":[{"type":"discounts-per-redemption"},{"type":"discounts-per-redemption"}],"_links":[{"rel":"self"},{"rel":"self"}],"customerId":"","createdTime":"","id":"","canceledTime":"","couponId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/coupons-redemptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_coupon_redemption_cancellation(client):
    """Test case for post_coupon_redemption_cancellation

    Cancel a coupon redemption
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/coupons-redemptions/{id}/cancel'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_coupon(client):
    """Test case for put_coupon

    Create or update a coupon with predefined coupon ID
    """
    body = {"redemptionsCount":0,"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"issuedTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","description":"description","discount":{"type":"fixed"},"restrictions":[{"type":"discounts-per-redemption"},{"type":"discounts-per-redemption"}],"id":"","expiredTime":"2000-01-23T04:56:07.000+00:00","status":"draft"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/coupons/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

