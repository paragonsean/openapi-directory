# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.broadcast_tx_response import BroadcastTxResponse
from openapi_server.models.error import Error
from openapi_server.models.get_address_response import GetAddressResponse
from openapi_server.models.get_address_utxos_response_inner import GetAddressUtxosResponseInner
from openapi_server.models.get_block_index_response import GetBlockIndexResponse
from openapi_server.models.get_block_response import GetBlockResponse
from openapi_server.models.get_raw_tx_response import GetRawTxResponse
from openapi_server.models.get_sync_response import GetSyncResponse
from openapi_server.models.get_tx_response import GetTxResponse
from openapi_server.models.get_txs_response import GetTxsResponse
from openapi_server.models.send_tx_request import SendTxRequest


pytestmark = pytest.mark.asyncio

async def test_get_address(client):
    """Test case for get_address

    Returns address object
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/addr/{address}'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address_balance(client):
    """Test case for get_address_balance

    Returns address balance in sats
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/addr/{address}/balance'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address_total_received(client):
    """Test case for get_address_total_received

    Returns total received by address in sats
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/addr/{address}/totalReceived'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address_total_sent(client):
    """Test case for get_address_total_sent

    Returns total sent by address in sats
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/addr/{address}/totalSent'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address_unconfirmed_balance(client):
    """Test case for get_address_unconfirmed_balance

    Returns address unconfirmed balance in sats
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/addr/{address}/unconfirmedBalance'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address_utxos(client):
    """Test case for get_address_utxos

    Returns all UTXOs at a given address
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/addr/{address}/utxo'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_block(client):
    """Test case for get_block

    Returns information regarding a Neblio block
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/block/{blockhash}'.format(blockhash='blockhash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_block_index(client):
    """Test case for get_block_index

    Returns block hash of block
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/block-index/{blockindex}'.format(blockindex=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_raw_tx(client):
    """Test case for get_raw_tx

    Returns raw transaction hex
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/rawtx/{txid}'.format(txid='txid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    Utility API for calling several blockchain node functions
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sync(client):
    """Test case for get_sync

    Get node sync status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/sync',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tx(client):
    """Test case for get_tx

    Returns transaction object
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/tx/{txid}'.format(txid='txid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_txs(client):
    """Test case for get_txs

    Get transactions by block or address
    """
    params = [('address', 'address_example'),
                    ('block', 'block_example'),
                    ('pageNum', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ins/txs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_tx(client):
    """Test case for send_tx

    Broadcasts a signed raw transaction to the network (not NTP1 specific)
    """
    body = openapi_server.SendTxRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ins/tx/send',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

