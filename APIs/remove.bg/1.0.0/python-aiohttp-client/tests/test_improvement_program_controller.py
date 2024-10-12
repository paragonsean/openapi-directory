# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_failed import AuthFailed
from openapi_server.models.improve_post400_response import ImprovePost400Response
from openapi_server.models.improvement_program_json import ImprovementProgramJson
from openapi_server.models.improvement_program_json_response import ImprovementProgramJsonResponse
from openapi_server.models.improvement_program_multipart import ImprovementProgramMultipart
from openapi_server.models.rate_limit import RateLimit


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_improve_post(client):
    """Test case for improve_post

    
    """
    body = {"image_file_b64":"","image_filename":"car.jpg","image_url":"https://www.remove.bg/example-hd.jpg","tag":"batch_1_2020"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/improve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

