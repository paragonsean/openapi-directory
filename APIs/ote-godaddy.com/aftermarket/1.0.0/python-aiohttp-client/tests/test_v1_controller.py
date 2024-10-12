# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aftermarket_listing_action import AftermarketListingAction
from openapi_server.models.aftermarket_listing_expiry_create import AftermarketListingExpiryCreate
from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_expiry_listings(client):
    """Test case for add_expiry_listings

    Add expiry listings into GoDaddy Auction
    """
    body = {"pageViewsMonthly":6,"domain":"domain","revenueMonthly":1,"expiresAt":"expiresAt","losingRegistrarId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/aftermarket/listings/expiry',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_listings(client):
    """Test case for delete_listings

    Remove listings from GoDaddy Auction
    """
    params = [('domains', ['domains_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/aftermarket/listings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

