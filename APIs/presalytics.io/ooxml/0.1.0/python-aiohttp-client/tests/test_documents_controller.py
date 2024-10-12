# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.document import Document
from openapi_server.models.document_clone_dto import DocumentCloneDTO


pytestmark = pytest.mark.asyncio

async def test_documents_childobjects_get_id(client):
    """Test case for documents_childobjects_get_id

    DocumentsController: Get Dependent Objects Tree
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Documents/ChildObjects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_clone_post_id(client):
    """Test case for documents_clone_post_id

    Documents: Clone an existing Ooxml Document to new Parent Story
    """
    body = {"storyId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ooxml-automation/Documents/Clone/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_delete_id(client):
    """Test case for documents_delete_id

    Documents: Delete by Id
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/ooxml-automation/Documents/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_download_get_id_orginal(client):
    """Test case for documents_download_get_id_orginal

    Documents: Download
    """
    params = [('orginal', False)]
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Documents/Download/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_get_id(client):
    """Test case for documents_get_id

    Documents: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Documents/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_documents_post(client):
    """Test case for documents_post

    Documents: Upload
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('story_id', 'story_id_example')
    response = await client.request(
        method='POST',
        path='/ooxml-automation/Documents',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

