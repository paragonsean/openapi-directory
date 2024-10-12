# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_role_assignment import BillingRoleAssignment
from openapi_server.models.billing_role_assignment_list_result import BillingRoleAssignmentListResult
from openapi_server.models.billing_role_assignment_payload import BillingRoleAssignmentPayload
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_add_by_billing_account_name(client):
    """Test case for billing_role_assignments_add_by_billing_account_name

    
    """
    parameters = {"billingRoleDefinitionId":"billingRoleDefinitionId","principalId":"principalId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/providers/Microsoft.Billing/createBillingRoleAssignment'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_add_by_billing_profile_name(client):
    """Test case for billing_role_assignments_add_by_billing_profile_name

    
    """
    parameters = {"billingRoleDefinitionId":"billingRoleDefinitionId","principalId":"principalId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/providers/Microsoft.Billing/createBillingRoleAssignment'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_add_by_invoice_section_name(client):
    """Test case for billing_role_assignments_add_by_invoice_section_name

    
    """
    parameters = {"billingRoleDefinitionId":"billingRoleDefinitionId","principalId":"principalId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/providers/Microsoft.Billing/createBillingRoleAssignment'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_delete_by_billing_account_name(client):
    """Test case for billing_role_assignments_delete_by_billing_account_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/providers/Microsoft.Billing/billingRoleAssignments/{billing_role_assignment_name}'.format(billing_account_name='billing_account_name_example', billing_role_assignment_name='billing_role_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_delete_by_billing_profile_name(client):
    """Test case for billing_role_assignments_delete_by_billing_profile_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/providers/Microsoft.Billing/billingRoleAssignments/{billing_role_assignment_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', billing_role_assignment_name='billing_role_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_delete_by_invoice_section_name(client):
    """Test case for billing_role_assignments_delete_by_invoice_section_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/providers/Microsoft.Billing/billingRoleAssignments/{billing_role_assignment_name}'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example', billing_role_assignment_name='billing_role_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_get_by_billing_account(client):
    """Test case for billing_role_assignments_get_by_billing_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/providers/Microsoft.Billing/billingRoleAssignments/{billing_role_assignment_name}'.format(billing_account_name='billing_account_name_example', billing_role_assignment_name='billing_role_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_get_by_billing_profile_name(client):
    """Test case for billing_role_assignments_get_by_billing_profile_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/providers/Microsoft.Billing/billingRoleAssignments/{billing_role_assignment_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', billing_role_assignment_name='billing_role_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_get_by_invoice_section_name(client):
    """Test case for billing_role_assignments_get_by_invoice_section_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/providers/Microsoft.Billing/billingRoleAssignments/{billing_role_assignment_name}'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example', billing_role_assignment_name='billing_role_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_list_by_billing_account_name(client):
    """Test case for billing_role_assignments_list_by_billing_account_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/providers/Microsoft.Billing/billingRoleAssignments'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_list_by_billing_profile_name(client):
    """Test case for billing_role_assignments_list_by_billing_profile_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/providers/Microsoft.Billing/billingRoleAssignments'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_role_assignments_list_by_invoice_section_name(client):
    """Test case for billing_role_assignments_list_by_invoice_section_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/providers/Microsoft.Billing/billingRoleAssignments'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

