# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server.models.upload_session import UploadSession


pytestmark = pytest.mark.asyncio

async def test_abort_upload(client):
    """Test case for abort_upload

    Abort database upload process
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1.0/snapshots/uploads/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_upload(client):
    """Test case for complete_upload

    Complete snapshot upload session
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0/snapshots/uploads/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snapshot(client):
    """Test case for get_snapshot

    Download a snapshot
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/snapshots/{project_id}/{language}'.format(project_id=56, language='language_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_init_snapshot_upload(client):
    """Test case for init_snapshot_upload

    Start snapshot upload session
    """
    params = [('commit', 'commit_example'),
                    ('date', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0/snapshots/{project_id}/{language}'.format(project_id=56, language='language_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload_part(client):
    """Test case for upload_part

    Upload snapshot
    """
    body = '/path/to/file'
    headers = { 
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1.0/snapshots/uploads/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

