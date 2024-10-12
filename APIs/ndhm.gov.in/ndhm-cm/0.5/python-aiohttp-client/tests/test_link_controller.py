# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_care_context_link_request import PatientCareContextLinkRequest
from openapi_server.models.patient_link_reference_result import PatientLinkReferenceResult
from openapi_server.models.patient_link_result import PatientLinkResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_add_contexts_post(client):
    """Test case for v05_links_link_add_contexts_post

    API for HIP initiated care-context linking for patient
    """
    body = {"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","link":{"patient":{"referenceNumber":"TMH-PUID-001","display":"display","careContexts":[{"referenceNumber":"referenceNumber","display":"display"},{"referenceNumber":"referenceNumber","display":"display"}]},"accessToken":"accessToken"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/links/link/add-contexts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_on_confirm_post(client):
    """Test case for v05_links_link_on_confirm_post

    Token authenticated by HIP, indicating completion of linkage of care-contexts
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"patient":{"referenceNumber":"referenceNumber","display":"display","careContexts":[{"referenceNumber":"referenceNumber","display":"display"},{"referenceNumber":"referenceNumber","display":"display"}]},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/links/link/on-confirm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_on_init_post(client):
    """Test case for v05_links_link_on_init_post

    Response to patient's care context link request
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","link":{"referenceNumber":"referenceNumber","meta":{"communicationMedium":"MOBILE","communicationHint":"communicationHint","communicationExpiry":"2019-12-30T12:01:55Z"},"authenticationType":"DIRECT"},"error":{"code":0,"message":"message"},"transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/links/link/on-init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

