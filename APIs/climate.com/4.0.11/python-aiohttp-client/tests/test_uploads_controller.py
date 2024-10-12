# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.upload import Upload
from openapi_server.models.upload_status import UploadStatus
from openapi_server.models.upload_status_query import UploadStatusQuery
from openapi_server.models.upload_statuses import UploadStatuses


pytestmark = pytest.mark.asyncio

async def test_chunked_upload(client):
    """Test case for chunked_upload

    Chunked upload of data
    """
    headers = { 
        'Accept': 'application/json',
        'content_range': 'content_range_example',
        'content_type': 'content_type_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v4/uploads/{upload_id}'.format(upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_upload_status_by_id(client):
    """Test case for fetch_upload_status_by_id

    Retrieve Upload status
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/uploads/{upload_id}/status'.format(upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_upload_statuses(client):
    """Test case for fetch_upload_statuses

    Retrieve Upload statuses in batch
    """
    body = {"ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/uploads/status/query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_upload(client):
    """Test case for post_upload

    Initiate a new upload
    """
    body = {"metadata":{"key":""},"length":0,"contentType":"image/vnd.climate.thermal.geotiff","md5":"md5"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_recipient_email': 'x_recipient_email_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/uploads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

