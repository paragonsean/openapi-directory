# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_status_checks_status_check import CredasApiModelsStatusChecksStatusCheck
from openapi_server.models.credas_api_models_status_checks_status_check_request import CredasApiModelsStatusChecksStatusCheckRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_check_credit_status(client):
    """Test case for check_credit_status

    Check includes identifying bankruptcy, insolvency, CCJ's or Company Directorship.
    """
    body = openapi_server.CredasApiModelsStatusChecksStatusCheckRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/credit-status/perform',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

