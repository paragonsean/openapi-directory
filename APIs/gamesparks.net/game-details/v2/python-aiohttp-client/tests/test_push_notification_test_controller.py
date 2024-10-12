# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.push_notification_test_model import PushNotificationTestModel
from openapi_server.models.push_notification_test_summary_list_model import PushNotificationTestSummaryListModel


pytestmark = pytest.mark.asyncio

async def test_test_push_amazon_notifications_using_post(client):
    """Test case for test_push_amazon_notifications_using_post

    testPushAmazonNotifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/amazon'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_push_apple_dev_notifications_using_post(client):
    """Test case for test_push_apple_dev_notifications_using_post

    testPushAppleDevNotifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/apple/development'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_push_apple_prod_notifications_using_post(client):
    """Test case for test_push_apple_prod_notifications_using_post

    testPushAppleProdNotifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/apple/production'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_push_google_notifications_using_post(client):
    """Test case for test_push_google_notifications_using_post

    testPushGoogleNotifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/google'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_viber_integration_notifications_using_post(client):
    """Test case for test_viber_integration_notifications_using_post

    testViberIntegrationNotifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/viber/integration'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_viber_production_notifications_using_post(client):
    """Test case for test_viber_production_notifications_using_post

    testViberProductionNotifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/viber/production'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_windows8_notifications_using_post(client):
    """Test case for test_windows8_notifications_using_post

    testWindows8Notifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/microsoft/windows8'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_windows_phone8_notifications_using_post(client):
    """Test case for test_windows_phone8_notifications_using_post

    testWindowsPhone8Notifications
    """
    body = {"pushId":"pushId","summary":"summary","subtitle":"subtitle","messageId":"messageId","title":"title","customJson":"customJson"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/pushNotifications/test/microsoft/windowsPhone8'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

