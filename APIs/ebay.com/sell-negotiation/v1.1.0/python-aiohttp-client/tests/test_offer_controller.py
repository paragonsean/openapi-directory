# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_offers_request import CreateOffersRequest
from openapi_server.models.paged_eligible_item_collection import PagedEligibleItemCollection
from openapi_server.models.send_offer_to_interested_buyers_collection_response import SendOfferToInterestedBuyersCollectionResponse


pytestmark = pytest.mark.asyncio

async def test_find_eligible_items(client):
    """Test case for find_eligible_items

    
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/negotiation/v1/find_eligible_items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_offer_to_interested_buyers(client):
    """Test case for send_offer_to_interested_buyers

    
    """
    body = {"allowCounterOffer":True,"offeredItems":[{"discountPercentage":"discountPercentage","quantity":6,"price":{"currency":"currency","value":"value"},"listingId":"listingId"},{"discountPercentage":"discountPercentage","quantity":6,"price":{"currency":"currency","value":"value"},"listingId":"listingId"}],"offerDuration":{"unit":"unit","value":0},"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/negotiation/v1/send_offer_to_interested_buyers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

