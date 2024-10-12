# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.composite_token import CompositeToken
from openapi_server.models.digital_wallet_validation import DigitalWalletValidation
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError


pytestmark = pytest.mark.asyncio

async def test_get_token(client):
    """Test case for get_token

    Retrieve a token
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tokens/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token_collection(client):
    """Test case for get_token_collection

    Retrieve a list of tokens
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_digital_wallet_validation(client):
    """Test case for post_digital_wallet_validation

    Validate a digital wallet session
    """
    body = {"type":"Apple Pay"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/digital-wallets/validation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_token(client):
    """Test case for post_token

    Create a payment token
    """
    body = {"method":"payment-card","billingAddress":"","paymentInstrument":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tokens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

