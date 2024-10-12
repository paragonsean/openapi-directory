# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.regulatory_compliance_assessment import RegulatoryComplianceAssessment
from openapi_server.models.regulatory_compliance_assessment_list import RegulatoryComplianceAssessmentList
from openapi_server.models.regulatory_compliance_control import RegulatoryComplianceControl
from openapi_server.models.regulatory_compliance_control_list import RegulatoryComplianceControlList
from openapi_server.models.regulatory_compliance_standard import RegulatoryComplianceStandard
from openapi_server.models.regulatory_compliance_standard_list import RegulatoryComplianceStandardList
from openapi_server.models.regulatory_compliance_standards_list_default_response import RegulatoryComplianceStandardsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_regulatory_compliance_assessments_get(client):
    """Test case for regulatory_compliance_assessments_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatory_compliance_standard_name}/regulatoryComplianceControls/{regulatory_compliance_control_name}/regulatoryComplianceAssessments/{regulatory_compliance_assessment_name}'.format(subscription_id='subscription_id_example', regulatory_compliance_standard_name='regulatory_compliance_standard_name_example', regulatory_compliance_control_name='regulatory_compliance_control_name_example', regulatory_compliance_assessment_name='regulatory_compliance_assessment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regulatory_compliance_assessments_list(client):
    """Test case for regulatory_compliance_assessments_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatory_compliance_standard_name}/regulatoryComplianceControls/{regulatory_compliance_control_name}/regulatoryComplianceAssessments'.format(subscription_id='subscription_id_example', regulatory_compliance_standard_name='regulatory_compliance_standard_name_example', regulatory_compliance_control_name='regulatory_compliance_control_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regulatory_compliance_controls_get(client):
    """Test case for regulatory_compliance_controls_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatory_compliance_standard_name}/regulatoryComplianceControls/{regulatory_compliance_control_name}'.format(subscription_id='subscription_id_example', regulatory_compliance_standard_name='regulatory_compliance_standard_name_example', regulatory_compliance_control_name='regulatory_compliance_control_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regulatory_compliance_controls_list(client):
    """Test case for regulatory_compliance_controls_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatory_compliance_standard_name}/regulatoryComplianceControls'.format(subscription_id='subscription_id_example', regulatory_compliance_standard_name='regulatory_compliance_standard_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regulatory_compliance_standards_get(client):
    """Test case for regulatory_compliance_standards_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatory_compliance_standard_name}'.format(subscription_id='subscription_id_example', regulatory_compliance_standard_name='regulatory_compliance_standard_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regulatory_compliance_standards_list(client):
    """Test case for regulatory_compliance_standards_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/regulatoryComplianceStandards'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

