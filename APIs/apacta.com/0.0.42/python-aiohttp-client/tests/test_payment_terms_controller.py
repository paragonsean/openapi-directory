# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.payment_terms_erp_get200_response import PaymentTermsErpGet200Response
from openapi_server.models.payment_terms_get200_response import PaymentTermsGet200Response
from openapi_server.models.payment_terms_payment_term_id_get200_response import PaymentTermsPaymentTermIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_payment_terms_erp_get(client):
    """Test case for payment_terms_erp_get

    Get integration payment terms list
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payment_terms/erp',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_terms_get(client):
    """Test case for payment_terms_get

    Get a list of payment terms
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payment_terms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_terms_payment_term_id_get(client):
    """Test case for payment_terms_payment_term_id_get

    Details of 1 payment term
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payment_terms/{payment_term_id}'.format(payment_term_id='payment_term_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

