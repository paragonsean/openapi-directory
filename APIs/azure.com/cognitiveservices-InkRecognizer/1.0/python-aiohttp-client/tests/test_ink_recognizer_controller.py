# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_request import AnalysisRequest
from openapi_server.models.analysis_response import AnalysisResponse
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_ink_recognizer_recognize(client):
    """Test case for ink_recognizer_recognize

    
    """
    body = openapi_server.AnalysisRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/recognize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

