# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assessments_metadata_list_default_response import AssessmentsMetadataListDefaultResponse
from openapi_server.models.security_assessment_metadata import SecurityAssessmentMetadata
from openapi_server.models.security_assessment_metadata_list import SecurityAssessmentMetadataList


pytestmark = pytest.mark.asyncio

async def test_assessments_metadata_get(client):
    """Test case for assessments_metadata_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Security/assessmentMetadata/{assessment_metadata_name}'.format(assessment_metadata_name='assessment_metadata_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_metadata_list(client):
    """Test case for assessments_metadata_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Security/assessmentMetadata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_metadata_subscription_create(client):
    """Test case for assessments_metadata_subscription_create

    
    """
    assessment_metadata = {"properties":{"preview":True,"severity":"Low","userImpact":"Low","policyDefinitionId":"policyDefinitionId","assessmentType":"BuiltIn","partnerData":{"partnerName":"partnerName","secret":"secret","productName":"productName"},"implementationEffort":"Low","displayName":"displayName","description":"description","threats":["accountBreach","accountBreach"],"remediationDescription":"remediationDescription","category":["Compute","Compute"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/assessmentMetadata/{assessment_metadata_name}'.format(assessment_metadata_name='assessment_metadata_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=assessment_metadata,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_metadata_subscription_delete(client):
    """Test case for assessments_metadata_subscription_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/assessmentMetadata/{assessment_metadata_name}'.format(assessment_metadata_name='assessment_metadata_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_metadata_subscription_get(client):
    """Test case for assessments_metadata_subscription_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/assessmentMetadata/{assessment_metadata_name}'.format(assessment_metadata_name='assessment_metadata_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assessments_metadata_subscription_list(client):
    """Test case for assessments_metadata_subscription_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/assessmentMetadata'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

