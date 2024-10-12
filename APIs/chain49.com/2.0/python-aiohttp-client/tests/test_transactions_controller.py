# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_mempool_v2200_response import GetMempoolV2200Response
from openapi_server.models.get_transaction_v2200_response import GetTransactionV2200Response
from openapi_server.models.post_send_tx_v2200_response import PostSendTxV2200Response


pytestmark = pytest.mark.asyncio

async def test_get_mempool_v2(client):
    """Test case for get_mempool_v2

    Get Mempool V2
    """
    params = [('page', 1),
                    ('pageSize', 1000)]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/mempool'.format(blockchain='bitcoin'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_send_tx_v2(client):
    """Test case for get_send_tx_v2

    Send transaction (in URL) V2
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/sendtx/{hex}'.format(blockchain='bitcoin', hex='01000000017f9a22c9cbf54bd902400df746f138f37bcf5b4d93eb755820e974ba43ed5f42040000006a4730440220037f4ed5427cde81d55b9b6a2fd08c8a25090c2c2fff3a75c1a57625ca8a7118022076c702fe55969fa08137f71afd4851c48e31082dd3c40c919c92cdbc826758d30121029f6da5623c9f9b68a9baf9c1bc7511df88fa34c6c2f71f7c62f2f03ff48dca80feffffff019c9700000000000017a9146144d57c8aff48492c9dfb914e120b20bad72d6f8773d00700'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_v2(client):
    """Test case for get_transaction_v2

    Get transaction V2
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/tx/{tx_id}'.format(blockchain='bitcoin', tx_id='cd8ec77174e426070d0a50779232bba7312b712e2c6843d82d963d7076c61366'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tx_specific_v2(client):
    """Test case for get_tx_specific_v2

    Get transaction (as is from Backend) V2
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/tx-specific/{tx_id}'.format(blockchain='bitcoin', tx_id='cd8ec77174e426070d0a50779232bba7312b712e2c6843d82d963d7076c61366'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_post_send_tx_v2(client):
    """Test case for post_send_tx_v2

    Send transaction (POST) V2
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{blockchain}/v2/sendtx'.format(blockchain='bitcoin'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

