# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.image_classification_request import ImageClassificationRequest
from openapi_server.models.image_classification_response import ImageClassificationResponse
from openapi_server.models.ocr_predict_response import OCRPredictResponse
from openapi_server.models.object_detection_request import ObjectDetectionRequest
from openapi_server.models.object_detection_response import ObjectDetectionResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_detect_multipart(client):
    """Test case for detect_multipart

    Detection with Image File
    """
    body = {"sampleBase64Content":"SomeBase64EncodedImage","sampleLocation":"sampleLocation","modelId":"YCQ4ZACEPJFGXZNRA6ERF3GL5E","sampleId":"sampleId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/vision/detect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_ocr_multipart(client):
    """Test case for ocr_multipart

    Detect Text
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('model_id', 'model_id_example')
    data.add_field('sample_content', '/path/to/file')
    data.add_field('sample_id', 'sample_id_example')
    data.add_field('sample_location', 'sample_location_example')
    data.add_field('task', 'text')
    response = await client.request(
        method='POST',
        path='/v2/vision/ocr',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_predict_multipart(client):
    """Test case for predict_multipart

    Make Prediction
    """
    body = {"sampleBase64Content":"SomeBase64EncodedImage","sampleLocation":"sampleLocation","modelId":"WJH4YCA7YX4PCWVNCYNWYHBMY4","sampleId":"sampleId","numResults":3}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/vision/predict',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

