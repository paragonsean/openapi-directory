# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_discovery_result import PatientDiscoveryResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_care_contexts_on_discover_post(client):
    """Test case for v05_care_contexts_on_discover_post

    Response to patient's account discovery request
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"patient":{"referenceNumber":"referenceNumber","display":"display","matchedBy":["MOBILE","MOBILE"],"careContexts":[{"referenceNumber":"referenceNumber","display":"display"},{"referenceNumber":"referenceNumber","display":"display"}]},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/care-contexts/on-discover',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

