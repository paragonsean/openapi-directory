# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_insights_questionnaires_question import FlexV1InsightsQuestionnairesQuestion
from openapi_server.models.list_insights_questionnaires_question_response import ListInsightsQuestionnairesQuestionResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_insights_questionnaires_question(client):
    """Test case for create_insights_questionnaires_question

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'allow_na': True,
        'answer_set_id': 'answer_set_id_example',
        'category_sid': 'category_sid_example',
        'description': 'description_example',
        'question': 'question_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Insights/QualityManagement/Questions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_insights_questionnaires_question(client):
    """Test case for delete_insights_questionnaires_question

    
    """
    headers = { 
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Insights/QualityManagement/Questions/{question_sid}'.format(question_sid='question_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_insights_questionnaires_question(client):
    """Test case for list_insights_questionnaires_question

    
    """
    params = [('CategorySid', ['category_sid_example']),
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
        path='/v1/Insights/QualityManagement/Questions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_insights_questionnaires_question(client):
    """Test case for update_insights_questionnaires_question

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'allow_na': True,
        'answer_set_id': 'answer_set_id_example',
        'category_sid': 'category_sid_example',
        'description': 'description_example',
        'question': 'question_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Insights/QualityManagement/Questions/{question_sid}'.format(question_sid='question_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

