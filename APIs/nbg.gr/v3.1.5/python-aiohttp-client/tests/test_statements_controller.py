# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ob_error_response1 import OBErrorResponse1
from openapi_server.models.ob_read_statement2 import OBReadStatement2


pytestmark = pytest.mark.asyncio

async def test_accounts_account_id_statements_get(client):
    """Test case for accounts_account_id_statements_get

    Get Statements
    """
    params = [('fromStatementDateTime', '2013-10-20T19:20:30+01:00'),
                    ('toStatementDateTime', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'x_fapi_auth_date': 'x_fapi_auth_date_example',
        'x_fapi_customer_ip_address': 'x_fapi_customer_ip_address_example',
        'x_fapi_interaction_id': 'x_fapi_interaction_id_example',
        'x_customer_user_agent': 'x_customer_user_agent_example',
        'sandbox_id': 'sandbox_id_example',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/accounts/{account_id}/statements'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_id_statements_statement_id_file_get(client):
    """Test case for accounts_account_id_statements_statement_id_file_get

    Get Statements
    """
    headers = { 
        'Accept': 'application/pdf',
        'x_fapi_auth_date': 'x_fapi_auth_date_example',
        'x_fapi_customer_ip_address': 'x_fapi_customer_ip_address_example',
        'x_fapi_interaction_id': 'x_fapi_interaction_id_example',
        'x_customer_user_agent': 'x_customer_user_agent_example',
        'sandbox_id': 'sandbox_id_example',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/accounts/{account_id}/statements/{statement_id}/file'.format(account_id='account_id_example', statement_id='statement_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_id_statements_statement_id_get(client):
    """Test case for accounts_account_id_statements_statement_id_get

    Get Statements
    """
    headers = { 
        'Accept': 'application/json',
        'x_fapi_auth_date': 'x_fapi_auth_date_example',
        'x_fapi_customer_ip_address': 'x_fapi_customer_ip_address_example',
        'x_fapi_interaction_id': 'x_fapi_interaction_id_example',
        'x_customer_user_agent': 'x_customer_user_agent_example',
        'sandbox_id': 'sandbox_id_example',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/accounts/{account_id}/statements/{statement_id}'.format(account_id='account_id_example', statement_id='statement_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

