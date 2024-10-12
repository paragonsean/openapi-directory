# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_amount_update_request import PaymentAmountUpdateRequest
from openapi_server.models.payment_amount_update_response import PaymentAmountUpdateResponse
from openapi_server.models.payment_cancel_request import PaymentCancelRequest
from openapi_server.models.payment_cancel_response import PaymentCancelResponse
from openapi_server.models.payment_capture_request import PaymentCaptureRequest
from openapi_server.models.payment_capture_response import PaymentCaptureResponse
from openapi_server.models.payment_refund_request import PaymentRefundRequest
from openapi_server.models.payment_refund_response import PaymentRefundResponse
from openapi_server.models.payment_reversal_request import PaymentReversalRequest
from openapi_server.models.payment_reversal_response import PaymentReversalResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.standalone_payment_cancel_request import StandalonePaymentCancelRequest
from openapi_server.models.standalone_payment_cancel_response import StandalonePaymentCancelResponse


pytestmark = pytest.mark.asyncio

async def test_post_cancels(client):
    """Test case for post_cancels

    Cancel an authorised payment
    """
    body = {"reference":"reference","merchantAccount":"merchantAccount","paymentReference":"paymentReference","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v41/cancels',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_payment_psp_reference_amount_updates(client):
    """Test case for post_payments_payment_psp_reference_amount_updates

    Update an authorised amount
    """
    body = {"reference":"reference","reason":"delayedCharge","amount":{"currency":"currency","value":0},"splits":[{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"}],"merchantAccount":"merchantAccount","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v41/payments/{payment_psp_reference}/amountUpdates'.format(payment_psp_reference='payment_psp_reference_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_payment_psp_reference_cancels(client):
    """Test case for post_payments_payment_psp_reference_cancels

    Cancel an authorised payment
    """
    body = {"reference":"reference","merchantAccount":"merchantAccount","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v41/payments/{payment_psp_reference}/cancels'.format(payment_psp_reference='payment_psp_reference_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_payment_psp_reference_captures(client):
    """Test case for post_payments_payment_psp_reference_captures

    Capture an authorised payment
    """
    body = {"lineItems":[{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6},{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6}],"reference":"reference","amount":{"currency":"currency","value":0},"splits":[{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"}],"merchantAccount":"merchantAccount","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v41/payments/{payment_psp_reference}/captures'.format(payment_psp_reference='payment_psp_reference_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_payment_psp_reference_refunds(client):
    """Test case for post_payments_payment_psp_reference_refunds

    Refund a captured payment
    """
    body = {"lineItems":[{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6},{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6}],"reference":"reference","amount":{"currency":"currency","value":0},"splits":[{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"}],"merchantAccount":"merchantAccount","merchantRefundReason":"FRAUD","store":"store","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v41/payments/{payment_psp_reference}/refunds'.format(payment_psp_reference='payment_psp_reference_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_payment_psp_reference_reversals(client):
    """Test case for post_payments_payment_psp_reference_reversals

    Refund or cancel a payment
    """
    body = {"reference":"reference","merchantAccount":"merchantAccount","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v41/payments/{payment_psp_reference}/reversals'.format(payment_psp_reference='payment_psp_reference_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

