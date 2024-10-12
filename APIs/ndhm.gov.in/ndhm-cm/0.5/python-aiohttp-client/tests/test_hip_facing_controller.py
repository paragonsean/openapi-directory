# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement


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
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/users/auth/fetch-modes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_on_notify_post_0(client):
    """Test case for v05_users_auth_on_notify_post_0

    callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)
    """
    body = {"acknowledgement":{"status":"OK"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/users/auth/on-notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

