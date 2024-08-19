# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beanstream_exception import BeanstreamException
from openapi_server.models.model_return import ModelReturn
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_response import PaymentResponse
from openapi_server.models.transaction import Transaction


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_payments_post(client):
    """Test case for payments_post

    Make Payment
    """
    payment_request = openapi_server.PaymentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/payments',
        headers=headers,
        json=payment_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_payments_trans_id_completions_post(client):
    """Test case for payments_trans_id_completions_post

    Complete pre-auth
    """
    payment_request = openapi_server.PaymentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/payments/{trans_id}/completions'.format(trans_id=3.4),
        headers=headers,
        json=payment_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_trans_id_get(client):
    """Test case for payments_trans_id_get

    Get payment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payments/{trans_id}'.format(trans_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_payments_trans_id_returns_post(client):
    """Test case for payments_trans_id_returns_post

    Return payment
    """
    _return = openapi_server.ModelReturn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/payments/{trans_id}/returns'.format(trans_id=3.4),
        headers=headers,
        json=_return,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_payments_trans_id_void_post(client):
    """Test case for payments_trans_id_void_post

    Void Transaction
    """
    void = openapi_server.Void()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/payments/{trans_id}/void'.format(trans_id=3.4),
        headers=headers,
        json=void,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

