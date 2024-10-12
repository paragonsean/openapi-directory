# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analyze_image_request import AnalyzeImageRequest
from openapi_server.models.computer_vision_error import ComputerVisionError
from openapi_server.models.domain_model_results import DomainModelResults
from openapi_server.models.image_analysis import ImageAnalysis
from openapi_server.models.image_description import ImageDescription
from openapi_server.models.list_models_result import ListModelsResult
from openapi_server.models.ocr_result import OcrResult
from openapi_server.models.tag_result import TagResult
from openapi_server.models.text_operation_result import TextOperationResult


pytestmark = pytest.mark.asyncio

async def test_analyze_image(client):
    """Test case for analyze_image

    
    """
    image_url = openapi_server.AnalyzeImageRequest()
    params = [('visualFeatures', ['visual_features_example']),
                    ('details', ['details_example']),
                    ('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v1.0/analyze',
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyze_image_by_domain(client):
    """Test case for analyze_image_by_domain

    
    """
    image_url = openapi_server.AnalyzeImageRequest()
    params = [('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v1.0/models/{model}/analyze'.format(model='model_example'),
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_image(client):
    """Test case for describe_image

    
    """
    image_url = openapi_server.AnalyzeImageRequest()
    params = [('maxCandidates', '1'),
                    ('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v1.0/describe',
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_thumbnail(client):
    """Test case for generate_thumbnail

    
    """
    image_url = openapi_server.AnalyzeImageRequest()
    params = [('width', 56),
                    ('height', 56),
                    ('smartCropping', False)]
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v1.0/generateThumbnail',
        headers=headers,
        json=image_url,
        params=params,
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
        path='/vision/v1.0/textOperations/{operation_id}'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_models(client):
    """Test case for list_models

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vision/v1.0/models',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recognize_printed_text(client):
    """Test case for recognize_printed_text

    
    """
    image_url = openapi_server.AnalyzeImageRequest()
    params = [('detectOrientation', True),
                    ('language', unk)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v1.0/ocr',
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recognize_text(client):
    """Test case for recognize_text

    
    """
    image_url = openapi_server.AnalyzeImageRequest()
    params = [('detectHandwriting', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v1.0/recognizeText',
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_image(client):
    """Test case for tag_image

    
    """
    image_url = openapi_server.AnalyzeImageRequest()
    params = [('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v1.0/tag',
        headers=headers,
        json=image_url,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

