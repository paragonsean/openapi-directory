# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_bank_accounts_account_verification_request import CredasApiModelsBankAccountsAccountVerificationRequest
from openapi_server.models.credas_api_models_bank_accounts_account_verification_response import CredasApiModelsBankAccountsAccountVerificationResponse
from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_verify(client):
    """Test case for verify

    Verifies bank account details.
    """
    body = openapi_server.CredasApiModelsBankAccountsAccountVerificationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/bank-accounts/verify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

