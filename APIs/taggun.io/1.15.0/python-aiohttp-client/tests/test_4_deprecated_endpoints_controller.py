# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.receipt_match_result import ReceiptMatchResult
from openapi_server.models.receipt_result import ReceiptResult
from openapi_server.models.receipt_verbose_result import ReceiptVerboseResult
from openapi_server.models.storage_payload import StoragePayload


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_api_receipt_v1_match_file(client):
    """Test case for post_api_receipt_v1_match_file

    detect and match a receipt against keywords and metadata by uploading an image file
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
        'apikey': 'apikey_example',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('refresh', False)
    data.add_field('incognito', False)
    data.add_field('ip_address', 'ip_address_example')
    data.add_field('primary_keywords', ['primary_keywords_example'])
    data.add_field('secondary_keywords', ['secondary_keywords_example'])
    data.add_field('stop_words', ['stop_words_example'])
    data.add_field('language', 'language_example')
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/match/file',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_receipt_v1_simple_storage(client):
    """Test case for post_api_receipt_v1_simple_storage

    transcribe a receipt in storage
    """
    body = openapi_server.StoragePayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/simple/storage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_api_receipt_v1_verbose_storage(client):
    """Test case for post_api_receipt_v1_verbose_storage

    transcribe a receipt in storage and return detailed result
    """
    body = openapi_server.StoragePayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/verbose/storage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

