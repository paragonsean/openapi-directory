# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_a_new_question_request import CreateANewQuestionRequest


pytestmark = pytest.mark.asyncio

async def test_create_a_new_question(client):
    """Test case for create_a_new_question

    Create a New Question
    """
    body = openapi_server.CreateANewQuestionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/questions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_questions(client):
    """Test case for list_all_questions

    List All Questions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/questions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

