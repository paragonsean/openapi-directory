# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.computer_vision_error import ComputerVisionError
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.read_operation_result import ReadOperationResult
from openapi_server.models.text_operation_result import TextOperationResult


pytestmark = pytest.mark.asyncio

async def test_batch_read_file(client):
    """Test case for batch_read_file

    
    """
    body = {"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.1/read/core/asyncBatchAnalyze',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_read_operation_result(client):
    """Test case for get_read_operation_result

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vision/v2.1/read/operations/{operation_id}'.format(operation_id='e56ffa6e-1ee4-4042-bc07-993db706c95f'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_operation_result(client):
    """Test case for get_text_operation_result

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vision/v2.1/textOperations/{operation_id}'.format(operation_id='49a36324-fc4b-4387-aa06-090cfbf0064f'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recognize_text(client):
    """Test case for recognize_text

    
    """
    body = {"url":"url"}
    params = [('mode', 'Handwritten')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.1/recognizeText',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

