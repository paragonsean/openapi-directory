# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.file_action_entity import FileActionEntity
from openapi_server.models.file_entity import FileEntity
from openapi_server.models.file_upload_part_entity import FileUploadPartEntity


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_file_action_begin_upload(client):
    """Test case for file_action_begin_upload

    Begin file upload
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('mkdir_parents', True)
    data.add_field('part', 56)
    data.add_field('parts', 56)
    data.add_field('ref', 'ref_example')
    data.add_field('restart', 56)
    data.add_field('size', 56)
    data.add_field('with_rename', True)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/file_actions/begin_upload/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_file_action_copy(client):
    """Test case for file_action_copy

    Copy file/folder
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('destination', 'destination_example')
    data.add_field('structure', True)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/file_actions/copy/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_action_find(client):
    """Test case for file_action_find

    Find file/folder by path
    """
    params = [('preview_size', 'preview_size_example'),
                    ('with_previews', True),
                    ('with_priority_color', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/file_actions/metadata/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_file_action_move(client):
    """Test case for file_action_move

    Move file/folder
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('destination', 'destination_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/file_actions/move/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

