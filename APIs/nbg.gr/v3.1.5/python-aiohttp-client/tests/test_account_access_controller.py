# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ob_error_response1 import OBErrorResponse1
from openapi_server.models.ob_read_consent1 import OBReadConsent1
from openapi_server.models.ob_read_consent_response1 import OBReadConsentResponse1


pytestmark = pytest.mark.asyncio

async def test_account_access_consents_consent_id_delete(client):
    """Test case for account_access_consents_consent_id_delete

    Delete Account Access Consents
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
        method='DELETE',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/account-access-consents/{consent_id}'.format(consent_id='consent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_access_consents_consent_id_get(client):
    """Test case for account_access_consents_consent_id_get

    Get Account Access Consents
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
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/account-access-consents/{consent_id}'.format(consent_id='consent_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_access_consents_post(client):
    """Test case for account_access_consents_post

    Create Account Access Consents
    """
    body = {"Risk":"{}","Data":{"TransactionToDateTime":"2000-01-23T04:56:07.000+00:00","ExpirationDateTime":"2000-01-23T04:56:07.000+00:00","Permissions":["ReadAccountsBasic","ReadAccountsBasic"],"TransactionFromDateTime":"2000-01-23T04:56:07.000+00:00"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_fapi_auth_date': 'x_fapi_auth_date_example',
        'x_fapi_customer_ip_address': 'x_fapi_customer_ip_address_example',
        'x_fapi_interaction_id': 'x_fapi_interaction_id_example',
        'x_customer_user_agent': 'x_customer_user_agent_example',
        'sandbox_id': 'sandbox_id_example',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/account-access-consents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

