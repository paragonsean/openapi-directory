# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_url import ImageUrl


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_classify_image(client):
    """Test case for classify_image

    Classify an image and saves the result.
    """
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apim_key': 'special-key',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/classify/iterations/{published_name}/image'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_classify_image_url(client):
    """Test case for classify_image_url

    Classify an image url and saves the result.
    """
    body = {"url":"url"}
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/classify/iterations/{published_name}/url'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_classify_image_url_with_no_store(client):
    """Test case for classify_image_url_with_no_store

    Classify an image url without saving the result.
    """
    body = {"url":"url"}
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/classify/iterations/{published_name}/url/nostore'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_classify_image_with_no_store(client):
    """Test case for classify_image_with_no_store

    Classify an image without saving the result.
    """
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apim_key': 'special-key',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/classify/iterations/{published_name}/image/nostore'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_detect_image(client):
    """Test case for detect_image

    Detect objects in an image and saves the result.
    """
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apim_key': 'special-key',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/detect/iterations/{published_name}/image'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_detect_image_url(client):
    """Test case for detect_image_url

    Detect objects in an image url and saves the result.
    """
    body = {"url":"url"}
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/detect/iterations/{published_name}/url'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_detect_image_url_with_no_store(client):
    """Test case for detect_image_url_with_no_store

    Detect objects in an image url without saving the result.
    """
    body = {"url":"url"}
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/detect/iterations/{published_name}/url/nostore'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_detect_image_with_no_store(client):
    """Test case for detect_image_with_no_store

    Detect objects in an image without saving the result.
    """
    params = [('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apim_key': 'special-key',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v3.0/prediction/{project_id}/detect/iterations/{published_name}/image/nostore'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c', published_name='MyModel1'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

