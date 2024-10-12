# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.validation_result import ValidationResult


pytestmark = pytest.mark.asyncio

async def test_get_badge(client):
    """Test case for get_badge

    Return a redirect to a badge svg file depending on a source definition's validity
    """
    params = [('url', 'https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/badge',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_validate(client):
    """Test case for validate

    Validate an OpenAPI 3.0.x definition supplied in the body of the request
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('filename', 'filename_example')
    data.add_field('source', 'source_example')
    response = await client.request(
        method='POST',
        path='/api/v1/validate',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_url(client):
    """Test case for validate_url

    Validate an OpenAPI 3.0.x definition
    """
    params = [('url', 'https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/openapi.json')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

