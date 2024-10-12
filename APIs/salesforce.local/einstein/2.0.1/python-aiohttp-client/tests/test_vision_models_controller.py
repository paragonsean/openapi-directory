# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deletion_response import DeletionResponse
from openapi_server.models.learning_curve_list import LearningCurveList
from openapi_server.models.metrics import Metrics
from openapi_server.models.model_list import ModelList


pytestmark = pytest.mark.asyncio

async def test_delete_model1(client):
    """Test case for delete_model1

    Delete a Model
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/vision/models/{model_id}'.format(model_id='SomeModelId'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trained_model_learning_curve1(client):
    """Test case for get_trained_model_learning_curve1

    Get Model Learning Curve
    """
    params = [('offset', '0'),
                    ('count', '25')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/vision/models/{model_id}/lc'.format(model_id='SomeModelId'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trained_model_metrics1(client):
    """Test case for get_trained_model_metrics1

    Get Model Metrics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/vision/models/{model_id}'.format(model_id='SomeModelId'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trained_models1(client):
    """Test case for get_trained_models1

    Get All Models
    """
    params = [('offset', '0'),
                    ('count', '100')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/vision/datasets/{dataset_id}/models'.format(dataset_id='SomeDatasetId'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

