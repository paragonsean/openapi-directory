# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_profile_question_response import FetchHealthProfileQuestionResponse
from openapi_server.models.fetch_health_profile_questions_response import FetchHealthProfileQuestionsResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_health_profile_question(client):
    """Test case for fetch_health_profile_question

    Get a health profile question
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_profile_question/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_health_profile_questions(client):
    """Test case for fetch_health_profile_questions

    List health profile questions
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_profile_question',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

