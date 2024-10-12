# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attested_data import AttestedData
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.instance import Instance


pytestmark = pytest.mark.asyncio

async def test_attested_get_document(client):
    """Test case for attested_get_document

    
    """
    params = [('api-version', 'api_version_example'),
                    ('nonce', 'nonce_example')]
    headers = { 
        'Accept': 'application/json',
        'metadata': 'metadata_example',
    }
    response = await client.request(
        method='GET',
        path='/metadata/attested/document',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instances_get_metadata(client):
    """Test case for instances_get_metadata

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'metadata': 'metadata_example',
    }
    response = await client.request(
        method='GET',
        path='/metadata/instance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

