# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response_list_published_written_question import ApiResponseListPublishedWrittenQuestion
from openapi_server.models.api_response_object import ApiResponseObject


pytestmark = pytest.mark.asyncio

async def test_published_oral_question_get(client):
    """Test case for published_oral_question_get

    Returns a list of oral questions
    """
    params = [('parameters.answeringDateStart', '2013-10-20T19:20:30+01:00'),
                    ('parameters.answeringDateEnd', '2013-10-20T19:20:30+01:00'),
                    ('parameters.questionType', 'parameters_question_type_example'),
                    ('parameters.oralQuestionTimeId', 56),
                    ('parameters.askingMemberIds', [56]),
                    ('parameters.uINs', [56]),
                    ('parameters.answeringBodyIds', [56]),
                    ('parameters.skip', 56),
                    ('parameters.take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/oralquestions/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

