# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schema_responses import SchemaResponses


pytestmark = pytest.mark.asyncio

async def test_schema_response_delete(client):
    """Test case for schema_response_delete

    Delete a Incomplete Schema Response
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/schema_responses/{schema_response_id}'.format(schema_response_id='schema_response_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schema_response_patch(client):
    """Test case for schema_response_patch

    Update a Registration's Schema Response
    """
    body = openapi_server.SchemaResponses()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/schema_responses/{schema_response_id}'.format(schema_response_id='schema_response_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schema_response_ppost(client):
    """Test case for schema_response_ppost

    Create a new Schema Response
    """
    body = openapi_server.SchemaResponses()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/schema_responses/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schema_responses_list(client):
    """Test case for schema_responses_list

    List all Schema Responses
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schema_responses/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schema_responses_read(client):
    """Test case for schema_responses_read

    Retrieve a Schema Response
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schema_responses/{schema_response_id}'.format(schema_response_id='schema_response_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

