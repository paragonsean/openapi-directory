# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_question_definition_response import FetchHealthQuestionDefinitionResponse
from openapi_server.models.fetch_health_question_definitions_response import FetchHealthQuestionDefinitionsResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_health_question_definition(client):
    """Test case for fetch_health_question_definition

    Get a health question definition
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_question_definition/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_health_question_definitions(client):
    """Test case for fetch_health_question_definitions

    List health question definitions
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_question_definition',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

