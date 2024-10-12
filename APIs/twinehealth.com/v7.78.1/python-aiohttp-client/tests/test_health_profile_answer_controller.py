# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_profile_answer_response import FetchHealthProfileAnswerResponse
from openapi_server.models.fetch_health_profile_answers_response import FetchHealthProfileAnswersResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_health_profile_answer(client):
    """Test case for fetch_health_profile_answer

    Get a health profile answer
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_profile_answer/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_health_profile_answers(client):
    """Test case for fetch_health_profile_answers

    List health profile answers
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example'),
                    ('page[number]', 1),
                    ('page[size]', 50),
                    ('page[limit]', 50),
                    ('page[cursor]', 'page_cursor_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_profile_answer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

