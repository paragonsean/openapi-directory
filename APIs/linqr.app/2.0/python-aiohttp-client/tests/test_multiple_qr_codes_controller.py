# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_qr_code_batch import AutoQRCodeBatch
from openapi_server.models.generic_error import GenericError
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_qr_code_batch_batch_qrcode_post(client):
    """Test case for qr_code_batch_batch_qrcode_post

    QR Code Batch
    """
    body = {"output":"","items":[{"output":"","image":"","data":"https://linqr.app","size":"","style":""},{"output":"","image":"","data":"https://linqr.app","size":"","style":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Byvalue': 'special-key',
        'RapidAPI': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/batch/qrcode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

