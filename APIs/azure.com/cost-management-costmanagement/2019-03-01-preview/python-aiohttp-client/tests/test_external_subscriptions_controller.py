# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.external_subscription_definition import ExternalSubscriptionDefinition
from openapi_server.models.external_subscription_definition_list_result import ExternalSubscriptionDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_external_subscription_get(client):
    """Test case for external_subscription_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/externalSubscriptions/{external_subscription_name}'.format(external_subscription_name='external_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_subscription_list(client):
    """Test case for external_subscription_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/externalSubscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_subscription_list_by_external_billing_account(client):
    """Test case for external_subscription_list_by_external_billing_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/externalBillingAccounts/{external_billing_account_name}/externalSubscriptions'.format(external_billing_account_name='external_billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_subscription_list_by_management_group(client):
    """Test case for external_subscription_list_by_management_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$recurse', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.CostManagement/externalSubscriptions'.format(management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_subscription_update_management_group(client):
    """Test case for external_subscription_update_management_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.CostManagement/externalSubscriptions/{external_subscription_name}'.format(management_group_id='management_group_id_example', external_subscription_name='external_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

