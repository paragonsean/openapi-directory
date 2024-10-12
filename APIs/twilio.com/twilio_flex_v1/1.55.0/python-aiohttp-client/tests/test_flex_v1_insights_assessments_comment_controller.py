# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_insights_assessments_comment import FlexV1InsightsAssessmentsComment
from openapi_server.models.list_insights_assessments_comment_response import ListInsightsAssessmentsCommentResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_insights_assessments_comment(client):
    """Test case for create_insights_assessments_comment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'agent_id': 'agent_id_example',
        'category_id': 'category_id_example',
        'category_name': 'category_name_example',
        'comment': 'comment_example',
        'offset': 3.4,
        'segment_id': 'segment_id_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Insights/QualityManagement/Assessments/Comments',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_insights_assessments_comment(client):
    """Test case for list_insights_assessments_comment

    
    """
    params = [('SegmentId', 'segment_id_example'),
                    ('AgentId', 'agent_id_example'),
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
        path='/v1/Insights/QualityManagement/Assessments/Comments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

