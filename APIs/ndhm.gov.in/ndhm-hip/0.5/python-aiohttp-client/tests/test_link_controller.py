# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.link_confirmation_request import LinkConfirmationRequest
from openapi_server.models.patient_care_context_link_response import PatientCareContextLinkResponse
from openapi_server.models.patient_link_reference_request import PatientLinkReferenceRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_confirm_post(client):
    """Test case for v05_links_link_confirm_post

    Token submission by Consent Manager for link confirmation
    """
    body = {"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","confirmation":{"linkRefNumber":"linkRefNumber","token":"token"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/links/link/confirm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_init_post(client):
    """Test case for v05_links_link_init_post

    Link patient's care contexts
    """
    body = {"patient":{"referenceNumber":"TMH-PUID-001","id":"hinapatel79@ndhm","careContexts":[{"referenceNumber":"referenceNumber"},{"referenceNumber":"referenceNumber"}]},"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/links/link/init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_on_add_contexts_post(client):
    """Test case for v05_links_link_on_add_contexts_post

    callback API for HIP initiated patient linking /link/add-context
    """
    body = {"acknowledgement":{"status":"SUCCESS"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/links/link/on-add-contexts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

