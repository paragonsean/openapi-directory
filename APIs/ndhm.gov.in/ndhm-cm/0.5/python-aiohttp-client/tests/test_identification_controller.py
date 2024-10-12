# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_identification_request import PatientIdentificationRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_find_post(client):
    """Test case for v05_patients_find_post

    Identify a patient by her consent-manager user-id
    """
    body = {"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","query":{"requester":{"id":"100005","type":"HIU"},"patient":{"id":"hinapatel79@ndhm"}},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/patients/find',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

