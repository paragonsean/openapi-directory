# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_nft_meta_v2200_response import GetNFTMetaV2200Response


pytestmark = pytest.mark.asyncio

async def test_get_nft_meta_v2(client):
    """Test case for get_nft_meta_v2

    Get NFT metadata V2
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/nft/{nft_contract}/{nft_token_id}'.format(blockchain='ethereum', nft_contract='0x05756b07725dA0101813475333f372a844789Dc2', nft_token_id='22'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

