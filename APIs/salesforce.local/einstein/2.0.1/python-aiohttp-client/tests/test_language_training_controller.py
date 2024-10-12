# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.train_response import TrainResponse
from openapi_server.models.v2_language_train_params import V2LanguageTrainParams


pytestmark = pytest.mark.asyncio

async def test_get_train_status_and_progress(client):
    """Test case for get_train_status_and_progress

    Get Training Status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/language/train/{model_id}'.format(model_id='SomeModelId'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_retrain(client):
    """Test case for retrain

    Retrain a Dataset
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('algorithm', 'algorithm_example')
    data.add_field('epochs', 56)
    data.add_field('learning_rate', 3.4)
    data.add_field('model_id', 'model_id_example')
    data.add_field('train_params', openapi_server.V2LanguageTrainParams())
    response = await client.request(
        method='POST',
        path='/v2/language/retrain',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_train(client):
    """Test case for train

    Train a Dataset
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('algorithm', 'algorithm_example')
    data.add_field('dataset_id', 56)
    data.add_field('epochs', 56)
    data.add_field('learning_rate', 3.4)
    data.add_field('name', 'name_example')
    data.add_field('train_params', openapi_server.V2LanguageTrainParams())
    response = await client.request(
        method='POST',
        path='/v2/language/train',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

