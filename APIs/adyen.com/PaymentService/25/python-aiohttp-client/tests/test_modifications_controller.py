# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_or_refund_request import CancelOrRefundRequest
from openapi_server.models.cancel_request import CancelRequest
from openapi_server.models.capture_request import CaptureRequest
from openapi_server.models.modification_result import ModificationResult
from openapi_server.models.refund_request import RefundRequest
from openapi_server.models.service_error import ServiceError
from openapi_server.models.void_pending_refund_request import VoidPendingRefundRequest


pytestmark = pytest.mark.asyncio

async def test_post_cancel(client):
    """Test case for post_cancel

    Cancel an authorisation
    """
    body = {"originalReference":"originalReference","reference":"reference","uniqueTerminalId":"uniqueTerminalId","merchantAccount":"merchantAccount","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"tenderReference":"tenderReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v25/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_cancel_or_refund(client):
    """Test case for post_cancel_or_refund

    Cancel or refund a payment
    """
    body = {"originalReference":"originalReference","reference":"reference","uniqueTerminalId":"uniqueTerminalId","merchantAccount":"merchantAccount","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"tenderReference":"tenderReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v25/cancelOrRefund',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_capture(client):
    """Test case for post_capture

    Capture an authorisation
    """
    body = {"originalReference":"originalReference","reference":"reference","uniqueTerminalId":"uniqueTerminalId","merchantAccount":"merchantAccount","modificationAmount":{"currency":"currency","value":0},"additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"tenderReference":"tenderReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v25/capture',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_refund(client):
    """Test case for post_refund

    Refund a captured payment
    """
    body = {"originalReference":"originalReference","reference":"reference","uniqueTerminalId":"uniqueTerminalId","merchantAccount":"merchantAccount","modificationAmount":{"currency":"currency","value":0},"additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"tenderReference":"tenderReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v25/refund',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_void_pending_refund(client):
    """Test case for post_void_pending_refund

    Cancel an in-person refund
    """
    body = {"originalReference":"originalReference","reference":"reference","uniqueTerminalId":"uniqueTerminalId","merchantAccount":"merchantAccount","modificationAmount":{"currency":"currency","value":0},"additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"tenderReference":"tenderReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v25/voidPendingRefund',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

