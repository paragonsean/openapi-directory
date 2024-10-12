# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pre_sign_info import PreSignInfo
from openapi_server.models.pre_sign_request import PreSignRequest


pytestmark = pytest.mark.asyncio

async def test_rmm_pre_sign_attachment_post(client):
    """Test case for rmm_pre_sign_attachment_post

    Upload an attachment via a signed URL
    """
    body = {"fileExtension":"pdf","mediaType":"application/pdf"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/rmm/pre-sign-attachment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

