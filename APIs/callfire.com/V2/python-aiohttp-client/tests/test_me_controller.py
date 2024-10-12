# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.api_credential import ApiCredential
from openapi_server.models.api_credential_page import ApiCredentialPage
from openapi_server.models.billing_plan_usage import BillingPlanUsage
from openapi_server.models.caller_id_list import CallerIdList
from openapi_server.models.caller_id_verification_request import CallerIdVerificationRequest
from openapi_server.models.credit_usage import CreditUsage
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_create_api_credential(client):
    """Test case for create_api_credential

    Create api credentials
    """
    body = {"password":"password","name":"name","id":5,"enabled":True,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/me/api/credentials',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_credential(client):
    """Test case for delete_api_credential

    Delete api credentials
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/me/api/credentials/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_api_credentials(client):
    """Test case for disable_api_credentials

    Disable specified API credentials
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/me/api/credentials/{id}/disable'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_api_credentials(client):
    """Test case for enable_api_credentials

    Enable specified API credentials
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/me/api/credentials/{id}/enable'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_api_credentials(client):
    """Test case for find_api_credentials

    Find api credentials
    """
    params = [('name', 'name_example'),
                    ('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/me/api/credentials',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Find account details
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/me/account',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_credential(client):
    """Test case for get_api_credential

    Find a specific api credential
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/me/api/credentials/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_billing_plan_usage(client):
    """Test case for get_billing_plan_usage

    Find plan usage
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/me/billing/plan-usage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_caller_ids(client):
    """Test case for get_caller_ids

    Find caller ids
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/me/callerids',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_credit_usage(client):
    """Test case for get_credit_usage

    Find credit usage
    """
    params = [('intervalBegin', 56),
                    ('intervalEnd', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/me/billing/credit-usage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_verification_code_to_caller_id(client):
    """Test case for send_verification_code_to_caller_id

    Create a caller id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/me/callerids/{callerid}'.format(callerid='callerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_caller_id(client):
    """Test case for verify_caller_id

    Verify a caller id
    """
    body = {"verificationCode":"verificationCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/me/callerids/{callerid}/verification-code'.format(callerid='callerid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

