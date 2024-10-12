# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.error_object import ErrorObject
from openapi_server.models.stream_information_object import StreamInformationObject
from openapi_server.models.upload_parameter_object import UploadParameterObject
from openapi_server.models.uploader_information_object import UploaderInformationObject
from openapi_server.models.video_object import VideoObject


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create(client):
    """Test case for create

    Create a new video, optionally setting some metadata fields.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('userdata', 'userdata_example')
    response = await client.request(
        method='POST',
        path='/v1/video/create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_details(client):
    """Test case for details

    Return details about a video.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('video_id', 'video_id_example')
    response = await client.request(
        method='POST',
        path='/v1/video/details',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_query(client):
    """Test case for query

    Perform a JavaScript query to return video objects matching any desired criteria.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('filter', 'filter_example')
    response = await client.request(
        method='POST',
        path='/v1/video/query',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_stream(client):
    """Test case for stream

    Returns urls for streaming.
    """
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('video_id', 'video_id_example')
    response = await client.request(
        method='POST',
        path='/v1/video/stream',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update(client):
    """Test case for update

    Update a video's metadata.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('video_id', 'video_id_example')
    data.add_field('source', 'source_example')
    response = await client.request(
        method='POST',
        path='/v1/video/update',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload(client):
    """Test case for upload

    Return parameters needed for uploading a video file.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('video_id', 'video_id_example')
    response = await client.request(
        method='POST',
        path='/v1/video/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_uploader(client):
    """Test case for uploader

    Return embeddable url to an uploader widget
    """
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('video_id', 'video_id_example')
    data.add_field('timeout', '2 hours')
    response = await client.request(
        method='POST',
        path='/v1/video/uploader',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

