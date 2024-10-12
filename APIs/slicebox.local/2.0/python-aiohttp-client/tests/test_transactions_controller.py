# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.failed_outgoing_transaction_image import FailedOutgoingTransactionImage
from openapi_server.models.outgoing_transaction_image import OutgoingTransactionImage


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_transactions_token_image_post(client):
    """Test case for transactions_token_image_post

    
    """
    dataset = None
    params = [('transactionid', 56),
                    ('sequencenumber', 56),
                    ('totalimagecount', 56)]
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='POST',
        path='/api/transactions/{token}/image'.format(token='token_example'),
        headers=headers,
        json=dataset,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_transactions_token_outgoing_done_post(client):
    """Test case for transactions_token_outgoing_done_post

    
    """
    outgoing_entry_and_image_information_block = openapi_server.OutgoingTransactionImage()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/transactions/{token}/outgoing/done'.format(token='token_example'),
        headers=headers,
        json=outgoing_entry_and_image_information_block,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_transactions_token_outgoing_failed_post(client):
    """Test case for transactions_token_outgoing_failed_post

    
    """
    outgoing_transaction_and_image_and_error_message = openapi_server.FailedOutgoingTransactionImage()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/transactions/{token}/outgoing/failed'.format(token='token_example'),
        headers=headers,
        json=outgoing_transaction_and_image_and_error_message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_token_outgoing_get(client):
    """Test case for transactions_token_outgoing_get

    
    """
    params = [('transactionid', 56),
                    ('imageid', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/transactions/{token}/outgoing'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_token_outgoing_poll_get(client):
    """Test case for transactions_token_outgoing_poll_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/transactions/{token}/outgoing/poll'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_token_status_get(client):
    """Test case for transactions_token_status_get

    
    """
    params = [('transactionid', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/transactions/{token}/status'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_transactions_token_status_put(client):
    """Test case for transactions_token_status_put

    
    """
    transaction_status = 'transaction_status_example'
    params = [('transactionid', 56)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/transactions/{token}/status'.format(token='token_example'),
        headers=headers,
        json=transaction_status,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

