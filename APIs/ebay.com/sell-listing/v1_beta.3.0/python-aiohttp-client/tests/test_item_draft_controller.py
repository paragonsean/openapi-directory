# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.item_draft import ItemDraft
from openapi_server.models.item_draft_response import ItemDraftResponse


pytestmark = pytest.mark.asyncio

async def test_create_item_draft(client):
    """Test case for create_item_draft

    
    """
    body = {"condition":"condition","product":{"imageUrls":["imageUrls","imageUrls"],"aspects":[{"values":["values","values"],"name":"name"},{"values":["values","values"],"name":"name"}],"description":"description","epid":"epid","title":"title","brand":"brand"},"charity":{"donationPercentage":"donationPercentage","charityId":"charityId"},"format":"format","categoryId":"categoryId","pricingSummary":{"auctionReservePrice":{"currency":"currency","value":"value"},"price":{"currency":"currency","value":"value"},"auctionStartPrice":{"currency":"currency","value":"value"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_language': 'content_language_example',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/listing/v1_beta/item_draft/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

