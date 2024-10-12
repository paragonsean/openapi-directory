# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.interview import Interview
from openapi_server.models.survey_detail import SurveyDetail
from openapi_server.models.survey_metadata import SurveyMetadata


pytestmark = pytest.mark.asyncio

async def test_surveys_get(client):
    """Test case for surveys_get

    Returns a list of available Surveys
    """
    headers = { 
        'Accept': 'application/json',
        'basic': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Surveys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_surveys_survey_id_interviews_get(client):
    """Test case for surveys_survey_id_interviews_get

    Fetches some interview records for a specific survey
    """
    params = [('start', 56),
                    ('maxLength', 56)]
    headers = { 
        'Accept': 'application/json',
        'basic': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Surveys/{survey_id}/Interviews'.format(survey_id='survey_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_surveys_survey_id_metadata_get(client):
    """Test case for surveys_survey_id_metadata_get

    Fetches the metadata for a specific survey
    """
    headers = { 
        'Accept': 'application/json',
        'basic': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Surveys/{survey_id}/Metadata'.format(survey_id='survey_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

