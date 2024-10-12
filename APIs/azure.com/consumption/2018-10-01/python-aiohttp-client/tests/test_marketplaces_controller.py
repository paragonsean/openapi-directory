# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.marketplaces_list_result import MarketplacesListResult


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list(client):
    """Test case for marketplaces_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Consumption/marketplaces'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_by_billing_account(client):
    """Test case for marketplaces_list_by_billing_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.Consumption/marketplaces'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_by_billing_period(client):
    """Test case for marketplaces_list_by_billing_period

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/marketplaces'.format(subscription_id='subscription_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_by_department(client):
    """Test case for marketplaces_list_by_department

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/departments/{department_id}/providers/Microsoft.Consumption/marketplaces'.format(department_id='department_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_by_enrollment_account(client):
    """Test case for marketplaces_list_by_enrollment_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.Consumption/marketplaces'.format(enrollment_account_id='enrollment_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_by_management_group(client):
    """Test case for marketplaces_list_by_management_group

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.Consumption/marketplaces'.format(management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_for_billing_period_by_billing_account(client):
    """Test case for marketplaces_list_for_billing_period_by_billing_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/marketplaces'.format(billing_account_id='billing_account_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_for_billing_period_by_department(client):
    """Test case for marketplaces_list_for_billing_period_by_department

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/departments/{department_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/marketplaces'.format(department_id='department_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_for_billing_period_by_enrollment_account(client):
    """Test case for marketplaces_list_for_billing_period_by_enrollment_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/marketplaces'.format(enrollment_account_id='enrollment_account_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_for_billing_period_by_management_group(client):
    """Test case for marketplaces_list_for_billing_period_by_management_group

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/marketplaces'.format(management_group_id='management_group_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

