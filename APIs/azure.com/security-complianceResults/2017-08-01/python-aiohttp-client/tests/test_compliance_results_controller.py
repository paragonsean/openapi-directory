# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compliance_result import ComplianceResult
from openapi_server.models.compliance_result_list import ComplianceResultList
from openapi_server.models.compliance_results_get_default_response import ComplianceResultsGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_compliance_results_get(client):
    """Test case for compliance_results_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_id}/providers/Microsoft.Security/complianceResults/{compliance_result_name}'.format(resource_id='resource_id_example', compliance_result_name='compliance_result_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compliance_results_list(client):
    """Test case for compliance_results_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Security/complianceResults'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

