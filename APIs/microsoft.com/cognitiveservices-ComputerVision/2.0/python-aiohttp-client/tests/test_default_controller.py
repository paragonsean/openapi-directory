# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.area_of_interest_result import AreaOfInterestResult
from openapi_server.models.computer_vision_error import ComputerVisionError
from openapi_server.models.detect_result import DetectResult
from openapi_server.models.domain_model_results import DomainModelResults
from openapi_server.models.image_analysis import ImageAnalysis
from openapi_server.models.image_description import ImageDescription
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.list_models_result import ListModelsResult
from openapi_server.models.ocr_result import OcrResult
from openapi_server.models.tag_result import TagResult


pytestmark = pytest.mark.asyncio

async def test_analyze_image(client):
    """Test case for analyze_image

    
    """
    body = {"url":"url"}
    params = [('visualFeatures', ['[\"Categories\",\"Adult\",\"Tags\",\"Description\",\"Faces\",\"Color\",\"ImageType\",\"Objects\",\"Brands\"]']),
                    ('details', ['[\"Celebrities\",\"Landmarks\"]']),
                    ('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/analyze',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyze_image_by_domain(client):
    """Test case for analyze_image_by_domain

    
    """
    body = {"url":"url"}
    params = [('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/models/{model}/analyze'.format(model='Celebrities'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_image(client):
    """Test case for describe_image

    
    """
    body = {"url":"url"}
    params = [('maxCandidates', 1),
                    ('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/describe',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detect_objects(client):
    """Test case for detect_objects

    
    """
    body = {"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/detect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_thumbnail(client):
    """Test case for generate_thumbnail

    
    """
    body = {"url":"url"}
    params = [('width', 500),
                    ('height', 500),
                    ('smartCropping', False)]
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/generateThumbnail',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_area_of_interest(client):
    """Test case for get_area_of_interest

    
    """
    body = {"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/areaOfInterest',
        headers=headers,
        json=body,
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
        path='/vision/v2.0/models',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recognize_printed_text(client):
    """Test case for recognize_printed_text

    
    """
    body = {"url":"url"}
    params = [('detectOrientation', True),
                    ('language', unk)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/ocr',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_image(client):
    """Test case for tag_image

    
    """
    body = {"url":"url"}
    params = [('language', en)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vision/v2.0/tag',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

