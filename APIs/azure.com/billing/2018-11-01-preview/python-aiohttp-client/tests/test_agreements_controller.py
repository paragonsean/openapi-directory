# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agreement import Agreement
from openapi_server.models.agreement_list_result import AgreementListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_agreements_get(client):
    """Test case for agreements_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/agreements/{agreement_name}'.format(billing_account_name='billing_account_name_example', agreement_name='agreement_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agreements_list_by_billing_account_name(client):
    """Test case for agreements_list_by_billing_account_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/agreements'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

