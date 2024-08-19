# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analyze_operation_result import AnalyzeOperationResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.model import Model
from openapi_server.models.models import Models
from openapi_server.models.train_request import TrainRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyze_layout_async(client):
    """Test case for analyze_layout_async

    Analyze Layout
    """
    file_stream = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/pdf',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/layout/analyze',
        headers=headers,
        json=file_stream,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyze_receipt_async(client):
    """Test case for analyze_receipt_async

    Analyze Receipt
    """
    file_stream = None
    params = [('includeTextDetails', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/pdf',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/prebuilt/receipt/analyze',
        headers=headers,
        json=file_stream,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyze_with_custom_model(client):
    """Test case for analyze_with_custom_model

    Analyze Form
    """
    file_stream = None
    params = [('includeTextDetails', False)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/pdf',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/custom/models/{model_id}/analyze'.format(model_id='model_id_example'),
        headers=headers,
        json=file_stream,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_model(client):
    """Test case for delete_custom_model

    Delete Custom Model
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/custom/models/{model_id}'.format(model_id='model_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analyze_form_result(client):
    """Test case for get_analyze_form_result

    Get Analyze Form Result
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom/models/{model_id}/analyzeResults/{result_id}'.format(model_id='model_id_example', result_id='result_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analyze_layout_result(client):
    """Test case for get_analyze_layout_result

    Get Analyze Layout Result
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/layout/analyzeResults/{result_id}'.format(result_id='result_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analyze_receipt_result(client):
    """Test case for get_analyze_receipt_result

    Get Analyze Receipt Result
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/prebuilt/receipt/analyzeResults/{result_id}'.format(result_id='result_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_model(client):
    """Test case for get_custom_model

    Get Custom Model
    """
    params = [('includeKeys', False)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom/models/{model_id}'.format(model_id='model_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_models(client):
    """Test case for get_custom_models

    List Custom Models
    """
    params = [('op', full)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom/models',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_train_custom_model_async(client):
    """Test case for train_custom_model_async

    Train Custom Model
    """
    train_request = {"useLabelFile":False,"source":"source","sourceFilter":{"includeSubFolders":False,"prefix":"prefix"}}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/custom/models',
        headers=headers,
        json=train_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

