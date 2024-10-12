# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.result import Result
from openapi_server.models.styles import Styles
from openapi_server.models.upload_request import UploadRequest
from openapi_server.models.upload_response import UploadResponse


pytestmark = pytest.mark.asyncio

async def test_noauth_result_get(client):
    """Test case for noauth_result_get

    
    """
    params = [('submissionId', 'submission_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/noauth/result',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_noauth_styles_get(client):
    """Test case for noauth_styles_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/noauth/styles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_noauth_upload_post(client):
    """Test case for noauth_upload_post

    
    """
    upload_request = {"styleId":"styleId","optimizeForPrint":True,"useOriginalColors":True,"imageSize":0,"partnerId":"partnerId","imageBase64Encoded":"imageBase64Encoded"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/noauth/upload',
        headers=headers,
        json=upload_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

