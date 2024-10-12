# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_data_check_add_data_check_request import CredasApiModelsDataCheckAddDataCheckRequest
from openapi_server.models.credas_api_models_data_check_add_data_check_response import CredasApiModelsDataCheckAddDataCheckResponse
from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_data_check(client):
    """Test case for add_data_check

    Creates new data check against a specified registration.
    """
    body = openapi_server.CredasApiModelsDataCheckAddDataCheckRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/datachecks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

