# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_discovery_request import PatientDiscoveryRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_care_contexts_discover_post(client):
    """Test case for v05_care_contexts_discover_post

    Discover patient's accounts
    """
    body = {"patient":{"verifiedIdentifiers":[{"type":"MOBILE","value":"+919800083232"},{"type":"MOBILE","value":"+919800083232"}],"gender":"M","name":"chandler bing","unverifiedIdentifiers":[{"type":"MOBILE","value":"+919800083232"},{"type":"MOBILE","value":"+919800083232"}],"id":"<patient-id>@<consent-manager-id>","yearOfBirth":2000},"requestId":"499a5a4a-7dda-4f20-9b67-e24589627061","transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/care-contexts/discover',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

