# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.public_subscription_status import PublicSubscriptionStatus
from openapi_server.models.public_subscription_statuses_response import PublicSubscriptionStatusesResponse
from openapi_server.models.public_update_subscription_status_request import PublicUpdateSubscriptionStatusRequest


pytestmark = pytest.mark.asyncio

async def test_get_communication_preferences_v3_status_email_email_address_get_email_status(client):
    """Test case for get_communication_preferences_v3_status_email_email_address_get_email_status

    Get subscription statuses for a contact
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/communication-preferences/v3/status/email/{email_address}'.format(email_address='email_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_communication_preferences_v3_subscribe_subscribe(client):
    """Test case for post_communication_preferences_v3_subscribe_subscribe

    Subscribe a contact
    """
    body = {"emailAddress":"emailAddress","legalBasis":"LEGITIMATE_INTEREST_PQL","subscriptionId":"subscriptionId","legalBasisExplanation":"legalBasisExplanation"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/communication-preferences/v3/subscribe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_communication_preferences_v3_unsubscribe_unsubscribe(client):
    """Test case for post_communication_preferences_v3_unsubscribe_unsubscribe

    Unsubscribe a contact
    """
    body = {"emailAddress":"emailAddress","legalBasis":"LEGITIMATE_INTEREST_PQL","subscriptionId":"subscriptionId","legalBasisExplanation":"legalBasisExplanation"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/communication-preferences/v3/unsubscribe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

