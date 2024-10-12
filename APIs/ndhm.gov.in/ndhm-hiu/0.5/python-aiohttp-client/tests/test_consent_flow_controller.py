# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.consent_artefact_response import ConsentArtefactResponse
from openapi_server.models.consent_request_init_response import ConsentRequestInitResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_consent_notification_event import HIUConsentNotificationEvent
from openapi_server.models.hiu_consent_request_status import HIUConsentRequestStatus


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_consent_requests_on_init_post(client):
    """Test case for v05_consent_requests_on_init_post

    Response to consent request
    """
    body = {"consentRequest":{"id":"f29f0e59-8388-4698-9fe6-05db67aeac46"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/consent-requests/on-init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_consent_requests_on_status_post(client):
    """Test case for v05_consent_requests_on_status_post

    Result of consent request status
    """
    body = {"consentRequest":{"id":"<consent-request-id>","consentArtefacts":[{"id":"<consent-artefact-id>"},{"id":"<consent-artefact-id>"}],"status":"GRANTED"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/consent-requests/on-status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v05_consents_hiu_notify_post(client):
    """Test case for v05_consents_hiu_notify_post

    Consent notification
    """
    body = {"notification":{"consentRequestId":"<consent-request-id>","consentArtefacts":[{"id":"<consent-artefact-id>"},{"id":"<consent-artefact-id>"}],"status":"GRANTED"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/consents/hiu/notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_consents_on_fetch_post(client):
    """Test case for v05_consents_on_fetch_post

    Result of fetch request for a consent artefact
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","consent":{"signature":"Signature of CM as defined in W3C standards; Base64 encoded","consentDetail":{"requester":{"identifier":{"system":"https://www.mciindia.org","type":"REGNO","value":"MH1001"},"name":"Dr. Manju"},"createdAt":"2000-01-23T04:56:07.000+00:00","consentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","consentManager":{"id":"id"},"schemaVersion":"schemaVersion","hiTypes":["OPConsultation","OPConsultation"],"hiu":{"id":"id"},"purpose":{"code":"code","text":"text","refUri":"https://openapi-generator.tech"},"patient":{"id":"hinapatel@ndhm"},"permission":{"dateRange":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"accessMode":"VIEW","dataEraseAt":"2000-01-23T04:56:07.000+00:00","frequency":{"repeats":0,"unit":"HOUR","value":6}},"careContexts":[{"careContextReference":"Episode1","patientReference":"hinapatel79@hospital"},{"careContextReference":"Episode1","patientReference":"hinapatel79@hospital"}],"hip":{"id":"id"}},"status":"GRANTED"},"error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/consents/on-fetch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

