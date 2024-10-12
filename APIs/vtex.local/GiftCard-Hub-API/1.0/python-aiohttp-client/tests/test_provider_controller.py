# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_gift_card_providerby_id(client):
    """Test case for get_gift_card_providerby_id

    Get GiftCard Provider by ID
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders/{gift_card_provider_id}'.format(gift_card_provider_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_gift_card_providers(client):
    """Test case for list_all_gift_card_providers

    List All GiftCard Providers
    """
    headers = { 
        'Accept': 'text/plain',
        'accept': 'application/json',
        'content_type': 'application/json',
        'rest_range': 'resources=0-49',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
    }
    response = await client.request(
        method='GET',
        path='/giftcardproviders',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

