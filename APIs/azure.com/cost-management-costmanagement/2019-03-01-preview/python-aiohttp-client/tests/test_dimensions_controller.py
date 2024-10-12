# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dimensions_list_result import DimensionsListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_by_billing_account(client):
    """Test case for dimensions_list_by_billing_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/dimensions'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_by_department(client):
    """Test case for dimensions_list_by_department

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/departments/{department_id}/providers/Microsoft.CostManagement/dimensions'.format(billing_account_id='billing_account_id_example', department_id='department_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_by_enrollment_account(client):
    """Test case for dimensions_list_by_enrollment_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.CostManagement/dimensions'.format(billing_account_id='billing_account_id_example', enrollment_account_id='enrollment_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_by_management_group(client):
    """Test case for dimensions_list_by_management_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.CostManagement/dimensions'.format(management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_by_resource_group(client):
    """Test case for dimensions_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/dimensions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_by_subscription(client):
    """Test case for dimensions_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/dimensions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

