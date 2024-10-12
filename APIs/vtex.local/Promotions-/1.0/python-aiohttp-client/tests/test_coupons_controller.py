# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_rnb_pvt_coupon_post_request import ApiRnbPvtCouponPostRequest
from openapi_server.models.api_rnb_pvt_multiple_coupons_post_request_inner import ApiRnbPvtMultipleCouponsPostRequestInner
from openapi_server.models.getall200_response_inner import Getall200ResponseInner
from openapi_server.models.getarchivedbycouponcode200_response import Getarchivedbycouponcode200Response
from openapi_server.models.getusage200_response import Getusage200Response
from openapi_server.models.massive_generation_request import MassiveGenerationRequest
from openapi_server.models.update_request import UpdateRequest


pytestmark = pytest.mark.asyncio

async def test_api_rnb_pvt_coupon_post(client):
    """Test case for api_rnb_pvt_coupon_post

    Create coupon
    """
    body = openapi_server.ApiRnbPvtCouponPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/coupon/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rnb_pvt_multiple_coupons_post(client):
    """Test case for api_rnb_pvt_multiple_coupons_post

    Create multiple coupons
    """
    body = [{"couponConfiguration":{"couponCode":"promobf4","expirationIntervalPerUse":"00:00:00","isArchived":false,"maxItemsPerClient":10,"utmCampaign":"bf","utmSource":"fb"},"quantity":1}]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/multiple-coupons',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archivebycouponcode(client):
    """Test case for archivebycouponcode

    Archive coupon by coupon code
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/archive/coupon/{coupon_code}'.format(coupon_code='test'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getall(client):
    """Test case for getall

    Get all coupons
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
        path='/api/rnb/pvt/coupon',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getarchivedbycouponcode(client):
    """Test case for getarchivedbycouponcode

    Get archived coupon by coupon code
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
        path='/api/rnb/pvt/archive/coupon/{coupon_code}'.format(coupon_code='promo10'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getbycouponcode(client):
    """Test case for getbycouponcode

    Get coupon by coupon code
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
        path='/api/rnb/pvt/coupon/{coupon_code}'.format(coupon_code='promo10'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getusage(client):
    """Test case for getusage

    Get coupon usage
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
        path='/api/rnb/pvt/coupon/usage/{coupon_code}'.format(coupon_code='test'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_massive_generation(client):
    """Test case for massive_generation

    Coupon Massive Generation
    """
    body = openapi_server.MassiveGenerationRequest()
    params = [('quantity', 10)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/coupons',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unarchivebycouponcode(client):
    """Test case for unarchivebycouponcode

    Unarchive coupon by coupon code
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/unarchive/coupon/{coupon_code}'.format(coupon_code='test'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update(client):
    """Test case for update

    Update coupon
    """
    body = openapi_server.UpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/coupon',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

