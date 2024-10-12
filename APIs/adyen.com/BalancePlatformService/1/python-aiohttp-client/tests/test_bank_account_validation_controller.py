# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bank_account_identification_validation_request import BankAccountIdentificationValidationRequest
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_post_validate_bank_account_identification(client):
    """Test case for post_validate_bank_account_identification

    Validate a bank account
    """
    body = {"accountIdentification":{"bsbCode":"bsbCode","accountNumber":"accountNumber","type":"auLocal"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/validateBankAccountIdentification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

