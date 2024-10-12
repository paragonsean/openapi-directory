# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.file_response_vo import FileResponseVO
from openapi_server.models.file_tag_response_vo import FileTagResponseVO
from openapi_server.models.http_status_vo import HTTPStatusVO


pytestmark = pytest.mark.asyncio

async def test_get_file(client):
    """Test case for get_file

    Get File from Project.  Works for Regular and Remote Files
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/1.1/workgroups/{workgroup_id}/projects/{project_id}/files/{file_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_tags(client):
    """Test case for get_file_tags

    List Tags from Workgroup and Project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/1.1/workgroups/{workgroup_id}/projects/{project_id}/fileTags'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files(client):
    """Test case for get_files

    List Files from Project.  Works for Regular and Remote Files
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/1.1/workgroups/{workgroup_id}/projects/{project_id}/files'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file(client):
    """Test case for upload_file

    Upload File to Project.  A multipart/form-data request with a name \"file\"
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    response = await client.request(
        method='POST',
        path='/v1/1.1/workgroups/{workgroup_id}/projects/{project_id}/files'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

