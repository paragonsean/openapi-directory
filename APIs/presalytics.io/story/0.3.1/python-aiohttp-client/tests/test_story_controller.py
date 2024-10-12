# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.file_upload import FileUpload
from openapi_server.models.outline import Outline
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.status import Status
from openapi_server.models.story import Story


pytestmark = pytest.mark.asyncio

async def test_story_get(client):
    """Test case for story_get

    Story: Get List of User Stories
    """
    params = [('include_relationships', True),
                    ('include_outline', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_analytics(client):
    """Test case for story_id_analytics

    Story: View Analytics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/analytics'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_delete(client):
    """Test case for story_id_delete

    Story: Delete by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/story/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_file_ooxmlautomationid_delete(client):
    """Test case for story_id_file_ooxmlautomationid_delete

    Story: Delete Subdocument
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/story/{id}/file/{ooxml_automation_id}'.format(id='id_example', ooxml_automation_id='ooxml_automation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_file_ooxmlautomationid_get(client):
    """Test case for story_id_file_ooxmlautomationid_get

    Story: Download Updated File
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/file/{ooxml_automation_id}'.format(id='id_example', ooxml_automation_id='ooxml_automation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_story_id_file_post(client):
    """Test case for story_id_file_post

    Story: Upload a File To Existing Story
    """
    params = [('replace_existing', True),
                    ('obsolete_id', 'obsolete_id_example'),
                    ('include_outline', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', ['/path/to/file'])
    response = await client.request(
        method='POST',
        path='/story/{id}/file'.format(id='id_example'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_get(client):
    """Test case for story_id_get

    Story: Get by Id
    """
    params = [('include_relationships', True),
                    ('include_outline', True),
                    ('full', True),
                    ('refresh_cache', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_outline_get(client):
    """Test case for story_id_outline_get

    Story: Get Story Outline
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/outline'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_outline_post(client):
    """Test case for story_id_outline_post

    Story: Post Story Outline
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/{id}/outline'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_public(client):
    """Test case for story_id_public

    Story: Public Link to Story Reveal.js Document
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/public'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_put(client):
    """Test case for story_id_put

    Story: Modify
    """
    body = openapi_server.Story()
    params = [('include_outline', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/story/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_reveal(client):
    """Test case for story_id_reveal

    Story: Get Story at Reveal.js Document
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/reveal'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_status_get(client):
    """Test case for story_id_status_get

    Story: Get Story Status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/status'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_post(client):
    """Test case for story_post

    Story: Upload
    """
    body = openapi_server.Outline()
    params = [('include_outline', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_story_post_file(client):
    """Test case for story_post_file

    Story: Upload a File
    """
    params = [('include_outline', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', ['/path/to/file'])
    response = await client.request(
        method='POST',
        path='/story/file',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_post_file_json(client):
    """Test case for story_post_file_json

    Story: Upload a File (base64)
    """
    body = openapi_server.FileUpload()
    params = [('include_outline', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/file/json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

