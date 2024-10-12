# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.registration_schema_block import RegistrationSchemaBlock


pytestmark = pytest.mark.asyncio

async def test_schema_response_blocks_read(client):
    """Test case for schema_response_blocks_read

    Retrieve a list of Registration Schema Blocks for a Schema Response
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schema_responses/{schema_response_id}/schema_blocks'.format(schema_response_id='schema_response_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_get(client):
    """Test case for schema_responses_schema_response_id_schema_blocks_schema_response_block_id_get

    Retrieve a Registration Schema Block
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schema_responses/{schema_response_id}/schema_blocks/{schema_response_block_id}'.format(schema_response_id='schema_response_id_example', schema_response_block_id='schema_response_block_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

