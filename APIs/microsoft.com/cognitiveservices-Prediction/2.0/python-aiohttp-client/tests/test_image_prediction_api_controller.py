# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_url import ImageUrl


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_predict_image(client):
    """Test case for predict_image

    Predict an image and saves the result
    """
    params = [('iterationId', 'fe1e83c4-6f50-4899-9544-6bb08cf0e15a'),
                    ('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'prediction_key': '{API Key}',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v2.0/Prediction/{project_id}/image'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_predict_image_url(client):
    """Test case for predict_image_url

    Predict an image url and saves the result
    """
    body = {"url":"url"}
    params = [('iterationId', 'fe1e83c4-6f50-4899-9544-6bb08cf0e15a'),
                    ('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'prediction_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v2.0/Prediction/{project_id}/url'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_predict_image_url_with_no_store(client):
    """Test case for predict_image_url_with_no_store

    Predict an image url without saving the result
    """
    body = {"url":"url"}
    params = [('iterationId', 'fe1e83c4-6f50-4899-9544-6bb08cf0e15a'),
                    ('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'prediction_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v2.0/Prediction/{project_id}/url/nostore'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_predict_image_with_no_store(client):
    """Test case for predict_image_with_no_store

    Predict an image without saving the result
    """
    params = [('iterationId', 'fe1e83c4-6f50-4899-9544-6bb08cf0e15a'),
                    ('application', 'application_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'prediction_key': '{API Key}',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v2.0/Prediction/{project_id}/image/nostore'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

