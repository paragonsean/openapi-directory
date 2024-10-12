# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.survey_answers import SurveyAnswers
from openapi_server.models.survey_question import SurveyQuestion


pytestmark = pytest.mark.asyncio

async def test_get_questions(client):
    """Test case for get_questions

    Get survey questions in given scope and type
    """
    params = [('attach_answers_for_project', 74)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/surveys/{scope}/{type}'.format(scope='vendor', type='profile'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_answers(client):
    """Test case for submit_answers

    Post survey answers for scope and type
    """
    body = {"answers":[{"answer":"answer","project_id":0,"user_id":5,"question_answer_id":6,"question_id":1},{"answer":"answer","project_id":0,"user_id":5,"question_answer_id":6,"question_id":1}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/surveys/{scope}/{type}'.format(scope='vendor', type='profile'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

