# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement


pytestmark = pytest.mark.asyncio

async def test_v05_subscriptions_hiu_on_notify_post_0(client):
    """Test case for v05_subscriptions_hiu_on_notify_post_0

    Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
    """
    body = {"acknowledgement":{"eventId":"subscription event Id","status":"OK"},"resp":{"requestId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","error":{"code":0,"message":"message"},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/cm/v0.5/subscriptions/hiu/on-notify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_users_auth_on_notify_post_1(client):
    """Test case for v05_users_auth_on_notify_post_1

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

