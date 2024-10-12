# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.external_billing_account_definition import ExternalBillingAccountDefinition
from openapi_server.models.external_billing_account_definition_list_result import ExternalBillingAccountDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_external_billing_account_get(client):
    """Test case for external_billing_account_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/externalBillingAccounts/{external_billing_account_name}'.format(external_billing_account_name='external_billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_billing_account_list(client):
    """Test case for external_billing_account_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/externalBillingAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

