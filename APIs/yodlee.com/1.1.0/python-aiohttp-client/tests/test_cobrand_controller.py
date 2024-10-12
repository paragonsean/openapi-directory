# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cobrand_login_request import CobrandLoginRequest
from openapi_server.models.cobrand_login_response import CobrandLoginResponse
from openapi_server.models.cobrand_notification_response import CobrandNotificationResponse
from openapi_server.models.cobrand_public_key_response import CobrandPublicKeyResponse
from openapi_server.models.create_cobrand_notification_event_request import CreateCobrandNotificationEventRequest
from openapi_server.models.update_cobrand_notification_event_request import UpdateCobrandNotificationEventRequest
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_cobrand_login(client):
    """Test case for cobrand_login

    Cobrand Login
    """
    body = {"cobrand":{"cobrandLogin":"cobrandLogin","cobrandPassword":"cobrandPassword","locale":"locale"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cobrand/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cobrand_logout(client):
    """Test case for cobrand_logout

    Cobrand Logout
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/cobrand/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_subscription_event(client):
    """Test case for create_subscription_event

    Subscribe Event
    """
    body = {"event":{"callbackUrl":"callbackUrl"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cobrand/config/notifications/events/{event_name}'.format(event_name='event_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscribed_event(client):
    """Test case for delete_subscribed_event

    Delete Subscription
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/cobrand/config/notifications/events/{event_name}'.format(event_name='event_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_key(client):
    """Test case for get_public_key

    Get Public Key
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/cobrand/publicKey',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscribed_events(client):
    """Test case for get_subscribed_events

    Get Subscribed Events
    """
    params = [('eventName', 'event_name_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/cobrand/config/notifications/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscribed_event(client):
    """Test case for update_subscribed_event

    Update Subscription
    """
    body = {"event":{"callbackUrl":"callbackUrl"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/cobrand/config/notifications/events/{event_name}'.format(event_name='event_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

