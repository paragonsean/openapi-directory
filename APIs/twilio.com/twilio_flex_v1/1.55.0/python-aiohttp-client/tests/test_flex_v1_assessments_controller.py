# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_insights_assessments import FlexV1InsightsAssessments
from openapi_server.models.list_insights_assessments_response import ListInsightsAssessmentsResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_insights_assessments(client):
    """Test case for create_insights_assessments

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'agent_id': 'agent_id_example',
        'answer_id': 'answer_id_example',
        'answer_text': 'answer_text_example',
        'category_name': 'category_name_example',
        'category_sid': 'category_sid_example',
        'metric_id': 'metric_id_example',
        'metric_name': 'metric_name_example',
        'offset': 3.4,
        'questionnaire_sid': 'questionnaire_sid_example',
        'segment_id': 'segment_id_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Insights/QualityManagement/Assessments',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_insights_assessments(client):
    """Test case for list_insights_assessments

    
    """
    params = [('SegmentId', 'segment_id_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Insights/QualityManagement/Assessments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_insights_assessments(client):
    """Test case for update_insights_assessments

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'answer_id': 'answer_id_example',
        'answer_text': 'answer_text_example',
        'offset': 3.4
        }
    response = await client.request(
        method='POST',
        path='/v1/Insights/QualityManagement/Assessments/{assessment_sid}'.format(assessment_sid='assessment_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

