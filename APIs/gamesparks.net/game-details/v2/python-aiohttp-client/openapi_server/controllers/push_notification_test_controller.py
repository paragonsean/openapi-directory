from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.push_notification_test_model import PushNotificationTestModel
from openapi_server.models.push_notification_test_summary_list_model import PushNotificationTestSummaryListModel
from openapi_server import util


async def test_push_amazon_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testPushAmazonNotifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)


async def test_push_apple_dev_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testPushAppleDevNotifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)


async def test_push_apple_prod_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testPushAppleProdNotifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)


async def test_push_google_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testPushGoogleNotifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)


async def test_viber_integration_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testViberIntegrationNotifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)


async def test_viber_production_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testViberProductionNotifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)


async def test_windows8_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testWindows8Notifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)


async def test_windows_phone8_notifications_using_post(request: web.Request, api_key, body) -> web.Response:
    """testWindowsPhone8Notifications

    

    :param api_key: apiKey
    :type api_key: str
    :param body: messageDetails
    :type body: dict | bytes

    """
    body = PushNotificationTestModel.from_dict(body)
    return web.Response(status=200)
