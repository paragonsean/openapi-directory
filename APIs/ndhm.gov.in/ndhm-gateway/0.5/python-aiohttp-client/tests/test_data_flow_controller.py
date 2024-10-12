# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiphi_request import HIPHIRequest
from openapi_server.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement
from openapi_server.models.hi_request import HIRequest
from openapi_server.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
from openapi_server.models.health_information_notification import HealthInformationNotification


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_cm_on_request_post(client):
    """Test case for v05_health_information_cm_on_request_post

    Health information data request
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","error":{"code":0,"message":"message"},"hiRequest":{"sessionStatus":"REQUESTED","transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/health-information/cm/on-request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_cm_request_post(client):
    """Test case for v05_health_information_cm_request_post

    Health information data request
    """
    body = {"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","hiRequest":{"keyMaterial":{"curve":"Curve25519","cryptoAlg":"ECDH","dhPublicKey":{"keyValue":"keyValue","expiry":"2000-01-23T04:56:07.000+00:00","parameters":"Curve25519/32byte random key"},"nonce":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"dateRange":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"dataPushUrl":"dataPushUrl","consent":{"id":"id"}},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/health-information/cm/request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_hip_on_request_post(client):
    """Test case for v05_health_information_hip_on_request_post

    Health information data request
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"hiRequest":{"sessionStatus":"ACKNOWLEDGED","transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/health-information/hip/on-request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_hip_request_post(client):
    """Test case for v05_health_information_hip_request_post

    Health information data request
    """
    body = {"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","hiRequest":{"keyMaterial":{"curve":"Curve25519","cryptoAlg":"ECDH","dhPublicKey":{"keyValue":"keyValue","expiry":"2000-01-23T04:56:07.000+00:00","parameters":"Curve25519/32byte random key"},"nonce":"3fa85f64-5717-4562-b3fc-2c963f66afa6"},"dateRange":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"dataPushUrl":"dataPushUrl","consent":{"id":"id"}},"transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/health-information/hip/request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_notify_post(client):
    """Test case for v05_health_information_notify_post

    Notifications corresponding to events during data flow
    """
    body = {"notification":{"doneAt":"2000-01-23T04:56:07.000+00:00","consentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","notifier":{"id":"tmh","type":"HIU"},"statusNotification":{"hipId":"max","statusResponses":[{"careContextReference":"careContextReference","hiStatus":"OK","description":"description"},{"careContextReference":"careContextReference","hiStatus":"OK","description":"description"}],"sessionStatus":"TRANSFERRED"},"transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"499a5a4a-7dda-4f20-9b67-e24589627061","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/health-information/notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

