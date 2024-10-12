from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_notification_configuration_request import CreateNotificationConfigurationRequest
from openapi_server.models.delete_notification_configuration_request import DeleteNotificationConfigurationRequest
from openapi_server.models.generic_response import GenericResponse
from openapi_server.models.get_notification_configuration_list_response import GetNotificationConfigurationListResponse
from openapi_server.models.get_notification_configuration_request import GetNotificationConfigurationRequest
from openapi_server.models.get_notification_configuration_response import GetNotificationConfigurationResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.test_notification_configuration_request import TestNotificationConfigurationRequest
from openapi_server.models.test_notification_configuration_response import TestNotificationConfigurationResponse
from openapi_server.models.update_notification_configuration_request import UpdateNotificationConfigurationRequest
from openapi_server import util


async def post_create_notification_configuration(request: web.Request, body=None) -> web.Response:
    """Subscribe to notifications

    Creates a subscription to notifications informing you of events on your platform. After the subscription is created, the events specified in the configuration will be sent to the URL specified in the configuration. Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis), so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few different endpoints as configured.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateNotificationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def post_delete_notification_configurations(request: web.Request, body=None) -> web.Response:
    """Delete a notification subscription configuration

    Deletes an existing notification subscription configuration. After the subscription is deleted, no further event notifications will be sent to the URL defined in the subscription.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteNotificationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_notification_configuration(request: web.Request, body=None) -> web.Response:
    """Get a notification subscription configuration

    Returns the details of the configuration of a notification subscription.

    :param body: 
    :type body: dict | bytes

    """
    body = GetNotificationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_notification_configuration_list(request: web.Request, body=None) -> web.Response:
    """Get a list of notification subscription configurations

    Returns the details of the configurations of all of the notification subscriptions in the platform of the executing user.

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def post_test_notification_configuration(request: web.Request, body=None) -> web.Response:
    """Test a notification configuration

    Tests an existing notification subscription configuration. For each event type specified, a test notification will be generated and sent to the URL configured in the subscription specified.

    :param body: 
    :type body: dict | bytes

    """
    body = TestNotificationConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def post_update_notification_configuration(request: web.Request, body=None) -> web.Response:
    """Update a notification subscription configuration

    Updates an existing notification subscription configuration. If you are updating the event types, you must provide all event types, otherwise the previous event type configuration will be overwritten.

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNotificationConfigurationRequest.from_dict(body)
    return web.Response(status=200)
