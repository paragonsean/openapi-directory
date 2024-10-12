# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_report_view_get_report_view_by_reference_id_request import CredasApiModelsReportViewGetReportViewByReferenceIdRequest
from openapi_server.models.credas_api_models_report_view_get_report_view_by_registration_id_request import CredasApiModelsReportViewGetReportViewByRegistrationIdRequest
from openapi_server.models.credas_api_models_report_view_get_report_view_response import CredasApiModelsReportViewGetReportViewResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_report_view_by_reference_id(client):
    """Test case for get_report_view_by_reference_id

    Retrieves secure links to registration details pages searching by the Reference Id.
    """
    body = openapi_server.CredasApiModelsReportViewGetReportViewByReferenceIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/report-view/by-referenceid',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_report_view_by_registration_id(client):
    """Test case for get_report_view_by_registration_id

    Retrieves secure link to registration details page searching by the Registration Id.
    """
    body = openapi_server.CredasApiModelsReportViewGetReportViewByRegistrationIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/report-view/by-registrationid',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

