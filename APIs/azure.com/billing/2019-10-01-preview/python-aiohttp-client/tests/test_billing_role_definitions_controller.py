# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_role_definition import BillingRoleDefinition
from openapi_server.models.billing_role_definition_list_result import BillingRoleDefinitionListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_billing_role_definitions_get_by_billing_account(client):
    """Test case for billing_role_definitions_get_by_billing_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingRoleDefinitions/{billing_role_definition_name}'.format(billing_account_name='billing_account_name_example', billing_role_definition_name='billing_role_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_definitions_get_by_billing_profile(client):
    """Test case for billing_role_definitions_get_by_billing_profile

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/billingRoleDefinitions/{billing_role_definition_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', billing_role_definition_name='billing_role_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_definitions_get_by_invoice_section(client):
    """Test case for billing_role_definitions_get_by_invoice_section

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/billingRoleDefinitions/{billing_role_definition_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example', billing_role_definition_name='billing_role_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_definitions_list_by_billing_account(client):
    """Test case for billing_role_definitions_list_by_billing_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingRoleDefinitions'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_definitions_list_by_billing_profile(client):
    """Test case for billing_role_definitions_list_by_billing_profile

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/billingRoleDefinitions'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_definitions_list_by_invoice_section(client):
    """Test case for billing_role_definitions_list_by_invoice_section

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/billingRoleDefinitions'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

