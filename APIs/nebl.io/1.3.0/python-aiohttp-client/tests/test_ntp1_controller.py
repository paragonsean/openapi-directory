# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.broadcast_tx_request import BroadcastTxRequest
from openapi_server.models.broadcast_tx_response import BroadcastTxResponse
from openapi_server.models.burn_token_request import BurnTokenRequest
from openapi_server.models.burn_token_response import BurnTokenResponse
from openapi_server.models.error import Error
from openapi_server.models.get_address_info_response import GetAddressInfoResponse
from openapi_server.models.get_token_holders_response import GetTokenHoldersResponse
from openapi_server.models.get_token_id_response import GetTokenIdResponse
from openapi_server.models.get_token_metadata_response import GetTokenMetadataResponse
from openapi_server.models.get_transaction_info_response import GetTransactionInfoResponse
from openapi_server.models.issue_token_request import IssueTokenRequest
from openapi_server.models.issue_token_response import IssueTokenResponse
from openapi_server.models.send_token_request import SendTokenRequest
from openapi_server.models.send_token_response import SendTokenResponse


pytestmark = pytest.mark.asyncio

async def test_broadcast_tx(client):
    """Test case for broadcast_tx

    Broadcasts a signed raw transaction to the network
    """
    body = openapi_server.BroadcastTxRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ntp1/broadcast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_burn_token(client):
    """Test case for burn_token

    Builds a transaction that burns an NTP1 Token
    """
    body = openapi_server.BurnTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ntp1/burntoken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address_info(client):
    """Test case for get_address_info

    Information On a Neblio Address
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ntp1/addressinfo/{address}'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token_holders(client):
    """Test case for get_token_holders

    Get Addresses Holding a Token
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ntp1/stakeholders/{tokenid}'.format(tokenid='tokenid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token_id(client):
    """Test case for get_token_id

    Returns the tokenId representing a token
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ntp1/tokenid/{tokensymbol}'.format(tokensymbol='tokensymbol_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token_metadata(client):
    """Test case for get_token_metadata

    Get Metadata of Token
    """
    params = [('verbosity', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ntp1/tokenmetadata/{tokenid}'.format(tokenid='tokenid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token_metadata_of_utxo(client):
    """Test case for get_token_metadata_of_utxo

    Get UTXO Metadata of Token
    """
    params = [('verbosity', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ntp1/tokenmetadata/{tokenid}/{utxo}'.format(tokenid='tokenid_example', utxo='utxo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_info(client):
    """Test case for get_transaction_info

    Information On an NTP1 Transaction
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ntp1/transactioninfo/{txid}'.format(txid='txid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_token(client):
    """Test case for issue_token

    Builds a transaction that issues a new NTP1 Token
    """
    body = openapi_server.IssueTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ntp1/issue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_token(client):
    """Test case for send_token

    Builds a transaction that sends an NTP1 Token
    """
    body = openapi_server.SendTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ntp1/sendtoken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

