# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_insights_questionnaires import FlexV1InsightsQuestionnaires
from openapi_server.models.list_insights_questionnaires_response import ListInsightsQuestionnairesResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_insights_questionnaires(client):
    """Test case for create_insights_questionnaires

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'description': 'description_example',
        'name': 'name_example',
        'question_sids': ['question_sids_example']
        }
    response = await client.request(
        method='POST',
        path='/v1/Insights/QualityManagement/Questionnaires',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_insights_questionnaires(client):
    """Test case for delete_insights_questionnaires

    
    """
    headers = { 
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Insights/QualityManagement/Questionnaires/{questionnaire_sid}'.format(questionnaire_sid='questionnaire_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_insights_questionnaires(client):
    """Test case for fetch_insights_questionnaires

    
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Insights/QualityManagement/Questionnaires/{questionnaire_sid}'.format(questionnaire_sid='questionnaire_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_insights_questionnaires(client):
    """Test case for list_insights_questionnaires

    
    """
    params = [('IncludeInactive', True),
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
        path='/v1/Insights/QualityManagement/Questionnaires',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_insights_questionnaires(client):
    """Test case for update_insights_questionnaires

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'description': 'description_example',
        'name': 'name_example',
        'question_sids': ['question_sids_example']
        }
    response = await client.request(
        method='POST',
        path='/v1/Insights/QualityManagement/Questionnaires/{questionnaire_sid}'.format(questionnaire_sid='questionnaire_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

