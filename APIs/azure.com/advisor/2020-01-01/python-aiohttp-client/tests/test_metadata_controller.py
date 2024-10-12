# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.arm_error_response_body import ARMErrorResponseBody
from openapi_server.models.metadata_entity import MetadataEntity
from openapi_server.models.metadata_entity_list_result import MetadataEntityListResult


pytestmark = pytest.mark.asyncio

async def test_recommendation_metadata_get(client):
    """Test case for recommendation_metadata_get

    Gets the metadata entity.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Advisor/metadata/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommendation_metadata_list(client):
    """Test case for recommendation_metadata_list

    Gets the list of metadata entities.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Advisor/metadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

