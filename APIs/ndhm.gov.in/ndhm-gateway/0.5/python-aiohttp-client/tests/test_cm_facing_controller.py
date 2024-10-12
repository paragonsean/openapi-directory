# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.consent_artefact_response import ConsentArtefactResponse
from openapi_server.models.consent_request_init_response import ConsentRequestInitResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification import HIPConsentNotification
from openapi_server.models.hiphi_request import HIPHIRequest
from openapi_server.models.hiu_consent_notification_event import HIUConsentNotificationEvent
from openapi_server.models.hiu_consent_request_status import HIUConsentRequestStatus
from openapi_server.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
from openapi_server.models.hiu_subscription_notification import HIUSubscriptionNotification
from openapi_server.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
from openapi_server.models.link_confirmation_request import LinkConfirmationRequest
from openapi_server.models.patient_auth_confirm_response import PatientAuthConfirmResponse
from openapi_server.models.patient_auth_init_response import PatientAuthInitResponse
from openapi_server.models.patient_auth_mode_query_response import PatientAuthModeQueryResponse
from openapi_server.models.patient_auth_notification import PatientAuthNotification
from openapi_server.models.patient_care_context_link_response import PatientCareContextLinkResponse
from openapi_server.models.patient_discovery_request import PatientDiscoveryRequest
from openapi_server.models.patient_discovery_result import PatientDiscoveryResult
from openapi_server.models.patient_identification_response import PatientIdentificationResponse
from openapi_server.models.patient_link_reference_request import PatientLinkReferenceRequest
from openapi_server.models.patient_sms_notifcation_response import PatientSMSNotifcationResponse
from openapi_server.models.share_profile_request import ShareProfileRequest
from openapi_server.models.subscription_approval_notification import SubscriptionApprovalNotification


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_care_contexts_discover_post_0(client):
    """Test case for v05_care_contexts_discover_post_0

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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_care_contexts_on_discover_post_0(client):
    """Test case for v05_care_contexts_on_discover_post_0

    Response to patient's account discovery request
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"patient":{"referenceNumber":"referenceNumber","display":"display","matchedBy":["MOBILE","MOBILE"],"careContexts":[{"referenceNumber":"referenceNumber","display":"display"},{"referenceNumber":"referenceNumber","display":"display"}]},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"transactionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/care-contexts/on-discover',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_consent_requests_on_init_post_0(client):
    """Test case for v05_consent_requests_on_init_post_0

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
async def test_v05_consent_requests_on_status_post_0(client):
    """Test case for v05_consent_requests_on_status_post_0

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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_consents_hip_notify_post_0(client):
    """Test case for v05_consents_hip_notify_post_0

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


pytestmark = pytest.mark.asyncio

async def test_v05_consents_hiu_notify_post_0(client):
    """Test case for v05_consents_hiu_notify_post_0

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
async def test_v05_consents_on_fetch_post_0(client):
    """Test case for v05_consents_on_fetch_post_0

    Result of fetch request for a consent artefact
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","consent":{"signature":"Signature of CM as defined in W3C standards; Base64 encoded","consentDetail":{"requester":{"identifier":{"system":"https://www.mciindia.org","type":"REGNO","value":"MH1001"},"name":"Dr. Manju"},"createdAt":"2000-01-23T04:56:07.000+00:00","consentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","consentManager":{"id":"id"},"schemaVersion":"schemaVersion","hiTypes":["OPConsultation","OPConsultation"],"hiu":{"id":"id"},"purpose":{"code":"code","text":"text","refUri":"https://openapi-generator.tech"},"patient":{"id":"hinapatel79@ndhm"},"permission":{"dateRange":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"accessMode":"VIEW","dataEraseAt":"2000-01-23T04:56:07.000+00:00","frequency":{"repeats":0,"unit":"HOUR","value":6}},"careContexts":[{"careContextReference":"Episode1","patientReference":"hinapatel79@hospital"},{"careContextReference":"Episode1","patientReference":"hinapatel79@hospital"}],"hip":{"id":"id"}},"status":"GRANTED"},"error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_health_information_cm_on_request_post_0(client):
    """Test case for v05_health_information_cm_on_request_post_0

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
async def test_v05_health_information_hip_request_post_0(client):
    """Test case for v05_health_information_hip_request_post_0

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
async def test_v05_links_link_confirm_post_0(client):
    """Test case for v05_links_link_confirm_post_0

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
async def test_v05_links_link_init_post_0(client):
    """Test case for v05_links_link_init_post_0

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
async def test_v05_links_link_on_add_contexts_post_0(client):
    """Test case for v05_links_link_on_add_contexts_post_0

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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_on_find_post_0(client):
    """Test case for v05_patients_on_find_post_0

    Identification result for a consent-manager user-id
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"patient":{"name":"Hina Patel","id":"hinapatel79@ndhm"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/patients/on-find',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_profile_share_post_0(client):
    """Test case for v05_patients_profile_share_post_0

    Share patient profile details
    """
    body = {"patient":{"hipCode":"12345 (CounterId)","userDemographics":{"address":{"pincode":"pincode","line":"line","district":"district","state":"state"},"gender":"M","dayOfBirth":0,"identifiers":[{"type":"MOBILE","value":"+919800083232"},{"type":"MOBILE","value":"+919800083232"}],"name":"Jane Doe","healthId":"<username>@<suffix>","healthIdNumber":"1111-1111-1111-11","monthOfBirth":6,"yearOfBirth":2000}},"requestId":"499a5a4a-7dda-4f20-9b67-e24589627061","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/patients/profile/share',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_sms_on_notify_post(client):
    """Test case for v05_patients_sms_on_notify_post

    Acknowledgment response for SMS notification sent to patient by HIP
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"status":"ACKNOWLEDGED","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hip_id': 'x_hip_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/patients/sms/on-notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v05_subscription_requests_cm_on_init_post_0(client):
    """Test case for v05_subscription_requests_cm_on_init_post_0

    callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
    """
    body = {"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"subscriptionRequest":{"id":"f29f0e59-8388-4698-9fe6-05db67aeac46"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/subscription-requests/cm/on-init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_subscription_requests_hiu_notify_post_0(client):
    """Test case for v05_subscription_requests_hiu_notify_post_0

    Notification for subscription grant/deny/revoke
    """
    body = {"notification":{"subscriptionRequestId":"request id of the subscription","subscription":{"sources":[{"period":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"categories":["LINK","LINK"],"hip":{"id":"id"}},{"period":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"categories":["LINK","LINK"],"hip":{"id":"id"}}],"hiu":{"id":"id"},"patient":{"id":"hinapatel79@ndhm"},"id":"subscription Id"},"status":"GRANTED"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/subscription-requests/hiu/notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_subscriptions_hiu_notify_post_0(client):
    """Test case for v05_subscriptions_hiu_notify_post_0

    Notification to HIU on basis of a granted subscription
    """
    body = {"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","event":{"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","published":"2000-01-23T04:56:07.000+00:00","category":"LINK","subscriptionId":"subscription Id","content":{"patient":{"id":"hinapatel79@ndhm"},"context":[{"hiTypes":["OPConsultation","OPConsultation"],"careContext":{"careContextReference":"Episode1","patientReference":"batman@tmh"}},{"hiTypes":["OPConsultation","OPConsultation"],"careContext":{"careContextReference":"Episode1","patientReference":"batman@tmh"}}],"hip":{"id":"id"}}},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_hiu_id': 'x_hiu_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/subscriptions/hiu/notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_notify_post_0(client):
    """Test case for v05_users_auth_notify_post_0

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
async def test_v05_users_auth_on_confirm_post_0(client):
    """Test case for v05_users_auth_on_confirm_post_0

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
async def test_v05_users_auth_on_fetch_modes_post_0(client):
    """Test case for v05_users_auth_on_fetch_modes_post_0

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
async def test_v05_users_auth_on_init_post_0(client):
    """Test case for v05_users_auth_on_init_post_0

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

