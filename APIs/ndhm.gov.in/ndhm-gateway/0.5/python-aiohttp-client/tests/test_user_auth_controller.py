# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_auth_confirm_request import PatientAuthConfirmRequest
from openapi_server.models.patient_auth_confirm_response import PatientAuthConfirmResponse
from openapi_server.models.patient_auth_init_request import PatientAuthInitRequest
from openapi_server.models.patient_auth_init_response import PatientAuthInitResponse
from openapi_server.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from openapi_server.models.patient_auth_mode_query_response import PatientAuthModeQueryResponse
from openapi_server.models.patient_auth_notification import PatientAuthNotification
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_confirm_post(client):
    """Test case for v05_users_auth_confirm_post

    Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
    """
    body = {"credential":{"authCode":"authCode","demographic":{"identifier":{"type":"MOBILE","value":"+919800083232"},"gender":"M","name":"janki das","dateOfBirth":"1972-02-29"}},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","transactionId":"transactionId","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/confirm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_fetch_modes_post(client):
    """Test case for v05_users_auth_fetch_modes_post

    Get a patient's authentication modes relevant to specified purpose
    """
    body = {"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","query":{"requester":{"id":"100005","type":"HIP"},"purpose":"LINK","id":"hinapatel79@ndhm"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/fetch-modes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_init_post(client):
    """Test case for v05_users_auth_init_post

    Initialize authentication from HIP
    """
    body = {"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","query":{"authMode":"MOBILE_OTP","requester":{"id":"100005","type":"HIP"},"purpose":"LINK","id":"hinapatel@ndhm"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_notify_post(client):
    """Test case for v05_users_auth_notify_post

    notification API in case of DIRECT mode of authentication by the CM
    """
    body = {"auth":{"patient":{"address":{"pincode":"pincode","line":"line","district":"district","state":"state"},"gender":"M","identifiers":[{"type":"MOBILE","value":"+919800083232"},{"type":"MOBILE","value":"+919800083232"}],"name":"Hina Patel","id":"<patient-id>@<consent-manager-id>","yearOfBirth":2000},"validity":{"requester":{"id":"100005","type":"HIP"},"purpose":"LINK","limit":1,"expiry":"2000-01-23T04:56:07.000+00:00"},"accessToken":"accessToken","transactionId":"transactionId","status":"GRANTED"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_on_confirm_post(client):
    """Test case for v05_users_auth_on_confirm_post

    callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
    """
    body = {"auth":{"patient":{"address":{"pincode":"pincode","line":"line","district":"district","state":"state"},"gender":"M","identifiers":[{"type":"MOBILE","value":"+919800083232"},{"type":"MOBILE","value":"+919800083232"}],"name":"Hina Patel","id":"<patient-id>@<consent-manager-id>","yearOfBirth":2000},"validity":{"requester":{"id":"100005","type":"HIP"},"purpose":"LINK","limit":1,"expiry":"2000-01-23T04:56:07.000+00:00"},"accessToken":"accessToken"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/on-confirm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_on_fetch_modes_post(client):
    """Test case for v05_users_auth_on_fetch_modes_post

    Identification result for a consent-manager user-id
    """
    body = {"auth":{"modes":["MOBILE_OTP","MOBILE_OTP"],"purpose":"LINK"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/on-fetch-modes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_on_init_post(client):
    """Test case for v05_users_auth_on_init_post

    Response to user authentication initialization from HIP
    """
    body = {"auth":{"mode":"MOBILE_OTP","meta":{"hint":"hint","expiry":"2019-12-30T12:01:55Z"},"transactionId":"transactionId"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/on-init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_on_notify_post(client):
    """Test case for v05_users_auth_on_notify_post

    callback API by HIU/HIPs as acknowledgement of auth notification
    """
    body = {"acknowledgement":{"status":"OK"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/users/auth/on-notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

