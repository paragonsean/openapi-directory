# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agent_registration_information_get_default_response import AgentRegistrationInformationGetDefaultResponse
from openapi_server.models.dsc_node_report import DscNodeReport
from openapi_server.models.dsc_node_report_list_result import DscNodeReportListResult


pytestmark = pytest.mark.asyncio

async def test_node_reports_get(client):
    """Test case for node_reports_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodes/{node_id}/reports/{report_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_id='node_id_example', report_id='report_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_node_reports_get_content(client):
    """Test case for node_reports_get_content

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodes/{node_id}/reports/{report_id}/content'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_id='node_id_example', report_id='report_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_node_reports_list_by_node(client):
    """Test case for node_reports_list_by_node

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodes/{node_id}/reports'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_id='node_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

