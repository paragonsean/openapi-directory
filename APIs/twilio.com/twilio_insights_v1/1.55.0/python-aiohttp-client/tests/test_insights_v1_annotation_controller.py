# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation_enum_answered_by import AnnotationEnumAnsweredBy
from openapi_server.models.annotation_enum_connectivity_issue import AnnotationEnumConnectivityIssue
from openapi_server.models.insights_v1_call_annotation import InsightsV1CallAnnotation


pytestmark = pytest.mark.asyncio

async def test_fetch_annotation(client):
    """Test case for fetch_annotation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/{call_sid}/Annotation'.format(call_sid='call_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_annotation(client):
    """Test case for update_annotation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'answered_by': openapi_server.AnnotationEnumAnsweredBy(),
        'call_score': 56,
        'comment': 'comment_example',
        'connectivity_issue': openapi_server.AnnotationEnumConnectivityIssue(),
        'incident': 'incident_example',
        'quality_issues': 'quality_issues_example',
        'spam': True
        }
    response = await client.request(
        method='POST',
        path='/v1/Voice/{call_sid}/Annotation'.format(call_sid='call_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

