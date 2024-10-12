# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.payment_term_types_get200_response import PaymentTermTypesGet200Response
from openapi_server.models.payment_term_types_payment_term_type_id_get200_response import PaymentTermTypesPaymentTermTypeIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_payment_term_types_get(client):
    """Test case for payment_term_types_get

    Get a list of payment term types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payment_term_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_term_types_payment_term_type_id_get(client):
    """Test case for payment_term_types_payment_term_type_id_get

    Details of 1 payment term type
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payment_term_types/{payment_term_type_id}'.format(payment_term_type_id='payment_term_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

