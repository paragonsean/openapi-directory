# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_card_payment_request import CreateCardPaymentRequest
from openapi_server.models.create_payment_result import CreatePaymentResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_payment_result import GetPaymentResult
from openapi_server.models.payment_error import PaymentError
from openapi_server.models.payment_events import PaymentEvents
from openapi_server.models.payment_search_results import PaymentSearchResults


pytestmark = pytest.mark.asyncio

async def test_cancel_a_payment(client):
    """Test case for cancel_a_payment

    Cancel payment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payments/{payment_id}/cancel'.format(payment_id='hu20sqlact5260q2nanm0q8u93'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capture_a_payment(client):
    """Test case for capture_a_payment

    Capture payment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payments/{payment_id}/capture'.format(payment_id='hu20sqlact5260q2nanm0q8u93'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_payment(client):
    """Test case for create_a_payment

    Create new payment
    """
    body = {"delayed_capture":False,"reference":"12345","amount":12000,"metadata":"{\"ledger_code\":\"123\", \"reconciled\": true}","prefilled_cardholder_details":{"billing_address":{"country":"GB","city":"address city","postcode":"AB1 2CD","line2":"address line 2","line1":"address line 1"},"cardholder_name":"J. Bogs"},"description":"New passport application","return_url":"https://service-name.gov.uk/transactions/12345","language":"en","email":"Joe.Bogs@example.org","moto":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_payment(client):
    """Test case for get_a_payment

    Find payment by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payments/{payment_id}'.format(payment_id='hu20sqlact5260q2nanm0q8u93'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_for_a_payment(client):
    """Test case for get_events_for_a_payment

    Return payment events by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payments/{payment_id}/events'.format(payment_id='hu20sqlact5260q2nanm0q8u93'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_payments(client):
    """Test case for search_payments

    Search payments
    """
    params = [('reference', 'reference_example'),
                    ('email', 'email_example'),
                    ('state', 'state_example'),
                    ('card_brand', 'card_brand_example'),
                    ('from_date', 'from_date_example'),
                    ('to_date', 'to_date_example'),
                    ('page', 'page_example'),
                    ('display_size', 'display_size_example'),
                    ('cardholder_name', 'cardholder_name_example'),
                    ('first_digits_card_number', 'first_digits_card_number_example'),
                    ('last_digits_card_number', 'last_digits_card_number_example'),
                    ('from_settled_date', 'from_settled_date_example'),
                    ('to_settled_date', 'to_settled_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

