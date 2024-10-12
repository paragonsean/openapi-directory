# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.enrollment_account import EnrollmentAccount
from openapi_server.models.enrollment_account_list_result import EnrollmentAccountListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_enrollment_accounts_get_by_enrollment_account_id(client):
    """Test case for enrollment_accounts_get_by_enrollment_account_id

    
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
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/enrollmentAccounts/{enrollment_account_name}'.format(billing_account_name='billing_account_name_example', enrollment_account_name='enrollment_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enrollment_accounts_list_by_billing_account_name(client):
    """Test case for enrollment_accounts_list_by_billing_account_name

    
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
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/enrollmentAccounts'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

