# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification_response import HIPConsentNotificationResponse
from openapi_server.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement
from openapi_server.models.health_information_notification import HealthInformationNotification
from openapi_server.models.patient_auth_confirm_request import PatientAuthConfirmRequest
from openapi_server.models.patient_auth_init_request import PatientAuthInitRequest
from openapi_server.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
from openapi_server.models.patient_care_context_link_request import PatientCareContextLinkRequest
from openapi_server.models.patient_link_reference_result import PatientLinkReferenceResult
from openapi_server.models.patient_link_result import PatientLinkResult
from openapi_server.models.patient_sms_notifcation_request import PatientSMSNotifcationRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_consents_hip_on_notify_post_0(client):
    """Test case for v05_consents_hip_on_notify_post_0

    Consent notification
    """
    body = {"acknowledgement":{"consentId":"<consent-artefact-id>","status":"OK"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/consents/hip/on-notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_hip_on_request_post_0(client):
    """Test case for v05_health_information_hip_on_request_post_0

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
async def test_v05_health_information_notify_post_0(client):
    """Test case for v05_health_information_notify_post_0

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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_add_contexts_post_0(client):
    """Test case for v05_links_link_add_contexts_post_0

    API for HIP initiated care-context linking for patient
    """
    body = {"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","link":{"patient":{"referenceNumber":"TMH-PUID-001","display":"display","careContexts":[{"referenceNumber":"referenceNumber","display":"display"},{"referenceNumber":"referenceNumber","display":"display"}]},"accessToken":"accessToken"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/links/link/add-contexts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_on_confirm_post_0(client):
    """Test case for v05_links_link_on_confirm_post_0

    Token authenticated by HIP, indicating completion of linkage of care-contexts
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"patient":{"referenceNumber":"referenceNumber","display":"display","careContexts":[{"referenceNumber":"referenceNumber","display":"display"},{"referenceNumber":"referenceNumber","display":"display"}]},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/links/link/on-confirm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_links_link_on_init_post_0(client):
    """Test case for v05_links_link_on_init_post_0

    Response to patient's care context link request
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","link":{"referenceNumber":"referenceNumber","meta":{"communicationMedium":"MOBILE","communicationHint":"communicationHint","communicationExpiry":"2019-12-30T12:01:55Z"},"authenticationType":"DIRECT"},"error":{"code":0,"message":"message"},"transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/links/link/on-init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_sms_notify_post(client):
    """Test case for v05_patients_sms_notify_post

    API for HIP to send SMS notifications to patients
    """
    body = {"notification":{"receiverName":"Ramesh Singh (Optional)","careContextInfo":"X-Ray on 22nd Dec","deeplinkUrl":"https://link.to.health.records/ (Optional)","hip":{"name":"Max Healthcare (Optional)","id":"HIP_001"},"phoneNo":"+91-9999999999"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/patients/sms/notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_confirm_post_0(client):
    """Test case for v05_users_auth_confirm_post_0

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
async def test_v05_users_auth_fetch_modes_post_0(client):
    """Test case for v05_users_auth_fetch_modes_post_0

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
async def test_v05_users_auth_init_post_0(client):
    """Test case for v05_users_auth_init_post_0

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
async def test_v05_users_auth_on_notify_post_0(client):
    """Test case for v05_users_auth_on_notify_post_0

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

