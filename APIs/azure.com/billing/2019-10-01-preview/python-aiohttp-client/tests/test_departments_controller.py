# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.department import Department
from openapi_server.models.department_list_result import DepartmentListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_departments_get(client):
    """Test case for departments_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/departments/{department_name}'.format(billing_account_name='billing_account_name_example', department_name='department_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_departments_list_by_billing_account_name(client):
    """Test case for departments_list_by_billing_account_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/departments'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

