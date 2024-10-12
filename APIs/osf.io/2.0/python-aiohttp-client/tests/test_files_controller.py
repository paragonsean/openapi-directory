# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.file import File
from openapi_server.models.file_version import FileVersion


pytestmark = pytest.mark.asyncio

async def test_files_detail(client):
    """Test case for files_detail

    Retrieve a file
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_patch(client):
    """Test case for files_patch

    Update a file
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_version_detail(client):
    """Test case for files_version_detail

    Retrieve a file version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/files/{file_id}/versions/{version_id}'.format(file_id='file_id_example', version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_versions(client):
    """Test case for files_versions

    List all file versions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/files/{file_id}/versions'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

