# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.share_profile_request import ShareProfileRequest
from openapi_server.models.share_profile_result import ShareProfileResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_profile_on_share_post(client):
    """Test case for v05_patients_profile_on_share_post

    Response to patient's share profile request
    """
    body = {"acknowledgement":{"healthId":"<username>@<suffix>","status":"SUCCESS"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'x_cm_id': 'x_cm_id_example',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/patients/profile/on-share',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_patients_profile_share_post(client):
    """Test case for v05_patients_profile_share_post

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

