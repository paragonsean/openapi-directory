# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.payment_error import PaymentError
from openapi_server.models.payment_refund_request import PaymentRefundRequest
from openapi_server.models.refund import Refund
from openapi_server.models.refund_error import RefundError
from openapi_server.models.refund_for_search_result import RefundForSearchResult
from openapi_server.models.refund_search_results import RefundSearchResults


pytestmark = pytest.mark.asyncio

async def test_get_a_payment_refund(client):
    """Test case for get_a_payment_refund

    Find payment refund by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payments/{payment_id}/refunds/{refund_id}'.format(payment_id='payment_id_example', refund_id='refund_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_refunds_for_a_payment(client):
    """Test case for get_all_refunds_for_a_payment

    Get all refunds for a payment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payments/{payment_id}/refunds'.format(payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_refunds(client):
    """Test case for search_refunds

    Search refunds
    """
    params = [('from_date', 'from_date_example'),
                    ('to_date', 'to_date_example'),
                    ('from_settled_date', 'from_settled_date_example'),
                    ('to_settled_date', 'to_settled_date_example'),
                    ('page', 'page_example'),
                    ('display_size', 'display_size_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/refunds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_a_refund_for_a_payment(client):
    """Test case for submit_a_refund_for_a_payment

    Submit a refund for a payment
    """
    body = {"amount":150000,"refund_amount_available":200000}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payments/{payment_id}/refunds'.format(payment_id='payment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

