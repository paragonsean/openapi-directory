# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.receipt_result import ReceiptResult
from openapi_server.models.receipt_verbose_result import ReceiptVerboseResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_api_receipt_v1_simple_file(client):
    """Test case for post_api_receipt_v1_simple_file

    transcribe a receipt by uploading an image file
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
    data.add_field('near', 'near_example')
    data.add_field('ignore_merchant_name', 'ignore_merchant_name_example')
    data.add_field('language', 'language_example')
    data.add_field('extract_time', False)
    data.add_field('sub_account_id', 'sub_account_id_example')
    data.add_field('reference_id', 'reference_id_example')
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/simple/file',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_api_receipt_v1_verbose_file(client):
    """Test case for post_api_receipt_v1_verbose_file

    transcribe a receipt by uploading an image file and return detailed result
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
    data.add_field('near', 'near_example')
    data.add_field('ignore_merchant_name', 'ignore_merchant_name_example')
    data.add_field('language', 'language_example')
    data.add_field('extract_time', False)
    data.add_field('sub_account_id', 'sub_account_id_example')
    data.add_field('reference_id', 'reference_id_example')
    response = await client.request(
        method='POST',
        path='/api/receipt/v1/verbose/file',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

