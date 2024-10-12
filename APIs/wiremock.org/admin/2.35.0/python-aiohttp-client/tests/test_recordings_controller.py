# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_mappings_get200_response import AdminMappingsGet200Response
from openapi_server.models.admin_recordings_snapshot_post_request import AdminRecordingsSnapshotPostRequest
from openapi_server.models.admin_recordings_start_post_request import AdminRecordingsStartPostRequest
from openapi_server.models.admin_recordings_status_get200_response import AdminRecordingsStatusGet200Response


pytestmark = pytest.mark.asyncio

async def test_admin_recordings_snapshot_post(client):
    """Test case for admin_recordings_snapshot_post

    Take a snapshot recording
    """
    body = {"captureHeaders":{"Accept":{},"Content-Type":{"caseInsensitive":true}},"extractBodyCriteria":{"binarySizeThreshold":"1 Mb","textSizeThreshold":"2 kb"},"filters":{"ids":["40a93c4a-d378-4e07-8321-6158d5dbcb29"],"method":"GET","urlPathPattern":"/api/.*"},"outputFormat":"FULL","persist":false,"repeatsAsScenarios":false,"requestBodyPattern":{"ignoreArrayOrder":false,"ignoreExtraElements":true,"matcher":"equalToJson"},"transformerParameters":{"headerValue":"123"},"transformers":["modify-response-header"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/recordings/snapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_recordings_start_post(client):
    """Test case for admin_recordings_start_post

    Start recording
    """
    body = {"captureHeaders":{"Accept":{},"Content-Type":{"caseInsensitive":true}},"extractBodyCriteria":{"binarySizeThreshold":"10240","textSizeThreshold":"2048"},"filters":{"method":"GET","urlPathPattern":"/api/.*"},"persist":false,"repeatsAsScenarios":false,"requestBodyPattern":{"ignoreArrayOrder":false,"ignoreExtraElements":true,"matcher":"equalToJson"},"targetBaseUrl":"http://example.mocklab.io","transformerParameters":{"headerValue":"123"},"transformers":["modify-response-header"]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/recordings/start',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_recordings_status_get(client):
    """Test case for admin_recordings_status_get

    Get recording status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/recordings/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_recordings_stop_post(client):
    """Test case for admin_recordings_stop_post

    Stop recording
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/recordings/stop',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

