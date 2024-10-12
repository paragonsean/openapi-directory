# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.prediction_query_result import PredictionQueryResult
from openapi_server.models.prediction_query_token import PredictionQueryToken


pytestmark = pytest.mark.asyncio

async def test_delete_prediction(client):
    """Test case for delete_prediction

    Delete a set of predicted images and their associated prediction results
    """
    params = [('ids', ['[\"e31a14ab-5d78-4f7b-a267-3a1e4fd8a758\",\"cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12\"]'])]
    headers = { 
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='DELETE',
        path='/customvision/v2.1/Training/projects/{project_id}/predictions'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_query_predictions(client):
    """Test case for query_predictions

    Get images that were sent to your prediction endpoint
    """
    body = {"application":"application","session":"session","orderBy":"Newest","startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","iterationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","continuation":"continuation","maxCount":0,"tags":[{"minThreshold":1.4658129,"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","maxThreshold":6.0274563},{"minThreshold":1.4658129,"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","maxThreshold":6.0274563}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v2.1/Training/projects/{project_id}/predictions/query'.format(project_id='bc3f7dad-5544-468c-8573-3ef04d55463e'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_quick_test_image(client):
    """Test case for quick_test_image

    Quick test an image
    """
    params = [('iterationId', 'fe1e83c4-6f50-4899-9544-6bb08cf0e15a')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'training_key': '{API Key}',
    }
    data = FormData()
    data.add_field('image_data', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/customvision/v2.1/Training/projects/{project_id}/quicktest/image'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_quick_test_image_url(client):
    """Test case for quick_test_image_url

    Quick test an image url
    """
    body = {"url":"url"}
    params = [('iterationId', 'fe1e83c4-6f50-4899-9544-6bb08cf0e15a')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='POST',
        path='/customvision/v2.1/Training/projects/{project_id}/quicktest/url'.format(project_id='64b822c5-8082-4b36-a426-27225f4aa18c'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

