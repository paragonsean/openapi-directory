# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_subscription_notification import HIUSubscriptionNotification
from openapi_server.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
from openapi_server.models.subscription_approval_notification import SubscriptionApprovalNotification


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_subscription_requests_hiu_notify_post(client):
    """Test case for v05_subscription_requests_hiu_notify_post

    Notification for subscription grant/deny/revoke
    """
    body = {"notification":{"subscriptionRequestId":"request id of the subscription","subscription":{"sources":[{"period":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"categories":["LINK","LINK"],"hip":{"id":"id"}},{"period":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"categories":["LINK","LINK"],"hip":{"id":"id"}}],"hiu":{"id":"id"},"patient":{"id":"hinapatel@ndhm"},"id":"subscription Id"},"status":"GRANTED"},"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","timestamp":"2000-01-23T04:56:07.000+00:00"}
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

async def test_v05_subscription_requests_hiu_on_init_post(client):
    """Test case for v05_subscription_requests_hiu_on_init_post

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
        path='/gateway/v0.5/subscription-requests/hiu/on-init',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_subscriptions_hiu_notify_post(client):
    """Test case for v05_subscriptions_hiu_notify_post

    Notification to HIU on basis of a granted subscription
    """
    body = {"requestId":"5f7a535d-a3fd-416b-b069-c97d021fbacd","event":{"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","published":"2000-01-23T04:56:07.000+00:00","category":"LINK","subscriptionId":"subscription Id","content":{"patient":{"id":"hinapatel@ndhm"},"context":[{"hiTypes":["OPConsultation","OPConsultation"],"careContext":{"careContextReference":"Episode1","patientReference":"batman@tmh"}},{"hiTypes":["OPConsultation","OPConsultation"],"careContext":{"careContextReference":"Episode1","patientReference":"batman@tmh"}}],"hip":{"id":"id"}}},"timestamp":"2000-01-23T04:56:07.000+00:00"}
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

