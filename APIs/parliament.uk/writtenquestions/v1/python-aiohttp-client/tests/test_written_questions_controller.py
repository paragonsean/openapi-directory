# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.answered import Answered
from openapi_server.models.house_enum import HouseEnum
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.question_status_enum import QuestionStatusEnum
from openapi_server.models.questions_view_model_item import QuestionsViewModelItem
from openapi_server.models.questions_view_model_search_result import QuestionsViewModelSearchResult


pytestmark = pytest.mark.asyncio

async def test_api_writtenquestions_questions_date_uin_get(client):
    """Test case for api_writtenquestions_questions_date_uin_get

    Returns a written question
    """
    params = [('expandMember', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/writtenquestions/questions/{_date}/{uin}'.format(_date='2013-10-20T19:20:30+01:00', uin='uin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_writtenquestions_questions_get(client):
    """Test case for api_writtenquestions_questions_get

    Returns a list of written questions
    """
    params = [('askingMemberId', 56),
                    ('answeringMemberId', 56),
                    ('tabledWhenFrom', '2013-10-20T19:20:30+01:00'),
                    ('tabledWhenTo', '2013-10-20T19:20:30+01:00'),
                    ('answered', openapi_server.Answered()),
                    ('answeredWhenFrom', '2013-10-20T19:20:30+01:00'),
                    ('answeredWhenTo', '2013-10-20T19:20:30+01:00'),
                    ('questionStatus', openapi_server.QuestionStatusEnum()),
                    ('includeWithdrawn', True),
                    ('expandMember', True),
                    ('correctedWhenFrom', '2013-10-20T19:20:30+01:00'),
                    ('correctedWhenTo', '2013-10-20T19:20:30+01:00'),
                    ('searchTerm', 'search_term_example'),
                    ('uIN', 'u_in_example'),
                    ('answeringBodies', [56]),
                    ('members', [56]),
                    ('house', openapi_server.HouseEnum()),
                    ('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/writtenquestions/questions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_writtenquestions_questions_id_get(client):
    """Test case for api_writtenquestions_questions_id_get

    Returns a written question
    """
    params = [('expandMember', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/writtenquestions/questions/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

