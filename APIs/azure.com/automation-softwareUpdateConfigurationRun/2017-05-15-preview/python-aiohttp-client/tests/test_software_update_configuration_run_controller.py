# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.software_update_configuration_run import SoftwareUpdateConfigurationRun
from openapi_server.models.software_update_configuration_run_list_result import SoftwareUpdateConfigurationRunListResult
from openapi_server.models.software_update_configuration_runs_list_default_response import SoftwareUpdateConfigurationRunsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_software_update_configuration_runs_get_by_id(client):
    """Test case for software_update_configuration_runs_get_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/softwareUpdateConfigurationRuns/{software_update_configuration_run_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', software_update_configuration_run_id='software_update_configuration_run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_software_update_configuration_runs_list(client):
    """Test case for software_update_configuration_runs_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skip', 'skip_example'),
                    ('$top', 'top_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/softwareUpdateConfigurationRuns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

