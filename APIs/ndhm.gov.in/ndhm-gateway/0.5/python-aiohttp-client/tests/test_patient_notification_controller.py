# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_sms_notifcation_request import PatientSMSNotifcationRequest
from openapi_server.models.patient_sms_notifcation_response import PatientSMSNotifcationResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_sms_notify_post_0(client):
    """Test case for v05_patients_sms_notify_post_0

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
async def test_v05_patients_sms_on_notify_post_0(client):
    """Test case for v05_patients_sms_on_notify_post_0

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

