# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.chunk_upload_response import ChunkUploadResponse
from openapi_server.models.complete_upload_request import CompleteUploadRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.node import Node


pytestmark = pytest.mark.asyncio

async def test_cancel_file_upload_by_token(client):
    """Test case for cancel_file_upload_by_token

    Cancel file upload
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/uploads/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_file_upload_by_token(client):
    """Test case for complete_file_upload_by_token

    Complete file upload
    """
    body = {"resolutionStrategy":"autorename","fileName":"fileName","keepShareLinks":False,"userFileKeyList":{"items":[{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0},{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0}]},"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/uploads/{token}'.format(token='token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file_by_token_as_multipart1(client):
    """Test case for upload_file_by_token_as_multipart1

    Upload file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'content_range': 'content_range_example',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v4/uploads/{token}'.format(token='token_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

