# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analyze_result import AnalyzeResult
from openapi_server.models.analyze_with_custom_model_request import AnalyzeWithCustomModelRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.keys_result import KeysResult
from openapi_server.models.model_result import ModelResult
from openapi_server.models.models_result import ModelsResult
from openapi_server.models.train_request import TrainRequest
from openapi_server.models.train_result import TrainResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyze_with_custom_model(client):
    """Test case for analyze_with_custom_model

    Analyze Form
    """
    body = openapi_server.AnalyzeWithCustomModelRequest()
    params = [('keys', ['keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/pdf',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/custom/models/{id}/analyze'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_model(client):
    """Test case for delete_custom_model

    Delete Model
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/custom/models/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_model(client):
    """Test case for get_custom_model

    Get Model
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom/models/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_models(client):
    """Test case for get_custom_models

    Get Models
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom/models',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_extracted_keys(client):
    """Test case for get_extracted_keys

    Get Keys
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom/models/{id}/keys'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_train_custom_model(client):
    """Test case for train_custom_model

    Train Model
    """
    train_request = {"source":"source","sourceFilter":{"includeSubFolders":True,"prefix":"prefix"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/custom/train',
        headers=headers,
        json=train_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

