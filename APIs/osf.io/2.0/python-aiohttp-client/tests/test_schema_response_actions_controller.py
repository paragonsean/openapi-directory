# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schema_response_actions import SchemaResponseActions


pytestmark = pytest.mark.asyncio

async def test_schema_response_action_read(client):
    """Test case for schema_response_action_read

    Retrieve a list of Schema Response Actions for a Schema Response
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schema_responses/{schema_response_id}/actions'.format(schema_response_id='schema_response_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schema_responses_schema_response_id_actions_post(client):
    """Test case for schema_responses_schema_response_id_actions_post

    Create a new Schema Response Action
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/schema_responses/{schema_response_id}/actions'.format(schema_response_id='schema_response_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schema_responses_schema_response_id_actions_schema_response_action_id_get(client):
    """Test case for schema_responses_schema_response_id_actions_schema_response_action_id_get

    A Schema Response Action from a Schema Response
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schema_responses/{schema_response_id}/actions/{schema_response_action_id}'.format(schema_response_id='schema_response_id_example', schema_response_action_id='schema_response_action_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

