# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.json_payload import JsonPayload
from openapi_server.models.receipt_result import ReceiptResult
from openapi_server.models.receipt_verbose_result import ReceiptVerboseResult
from openapi_server.models.url_payload import UrlPayload


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_receipt_v1_simple_encoded(client):
    """Test case for post_api_receipt_v1_simple_encoded

    transcribe a receipt using base64 encoded image in json payload
    """
    body = openapi_server.JsonPayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/simple/encoded',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_receipt_v1_simple_url(client):
    """Test case for post_api_receipt_v1_simple_url

    transcribe a receipt from URL
    """
    body = openapi_server.UrlPayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/simple/url',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_receipt_v1_verbose_encoded(client):
    """Test case for post_api_receipt_v1_verbose_encoded

    transcribe a receipt using base64 encoded image in json payload and return detailed result
    """
    body = openapi_server.JsonPayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/verbose/encoded',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_receipt_v1_verbose_url(client):
    """Test case for post_api_receipt_v1_verbose_url

    transcribe a receipt from URL and return detailed result
    """
    body = openapi_server.UrlPayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/verbose/url',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

