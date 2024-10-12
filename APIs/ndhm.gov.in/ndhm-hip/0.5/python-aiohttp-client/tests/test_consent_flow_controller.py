# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification import HIPConsentNotification


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_consents_hip_notify_post(client):
    """Test case for v05_consents_hip_notify_post

    Consent notification
    """
    body = {"notification":{"consentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","signature":"Signature of CM as defined in W3C standards; Base64 encoded","consentDetail":{"createdAt":"2000-01-23T04:56:07.000+00:00","consentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","consentManager":{"id":"id"},"schemaVersion":"schemaVersion","hiTypes":["OPConsultation","OPConsultation"],"purpose":{"code":"code","text":"text","refUri":"https://openapi-generator.tech"},"patient":{"id":"hinapatel79@ndhm"},"permission":{"dateRange":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"accessMode":"VIEW","dataEraseAt":"2000-01-23T04:56:07.000+00:00","frequency":{"repeats":0,"unit":"HOUR","value":6}},"careContexts":[{"careContextReference":"Episode1","patientReference":"hinapatel79@hospital"},{"careContextReference":"Episode1","patientReference":"hinapatel79@hospital"}],"hip":{"id":"id"}},"status":"GRANTED"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/consents/hip/notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

