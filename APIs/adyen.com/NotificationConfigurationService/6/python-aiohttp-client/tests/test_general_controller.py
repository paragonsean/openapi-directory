# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_post_create_notification_configuration(client):
    """Test case for post_create_notification_configuration

    Subscribe to notifications
    """
    body = {"configurationDetails":{"hmacSignatureKey":"hmacSignatureKey","apiVersion":0,"eventConfigs":[{"includeMode":"EXCLUDE","eventType":"ACCOUNT_CLOSED"},{"includeMode":"EXCLUDE","eventType":"ACCOUNT_CLOSED"}],"notifyUsername":"notifyUsername","active":True,"description":"description","notifyURL":"notifyURL","sslProtocol":"TLSv12","notificationId":6,"notifyPassword":"notifyPassword"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Notification/v6/createNotificationConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_delete_notification_configurations(client):
    """Test case for post_delete_notification_configurations

    Delete a notification subscription configuration
    """
    body = {"notificationIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Notification/v6/deleteNotificationConfigurations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_notification_configuration(client):
    """Test case for post_get_notification_configuration

    Get a notification subscription configuration
    """
    body = {"notificationId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Notification/v6/getNotificationConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_notification_configuration_list(client):
    """Test case for post_get_notification_configuration_list

    Get a list of notification subscription configurations
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Notification/v6/getNotificationConfigurationList',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_test_notification_configuration(client):
    """Test case for post_test_notification_configuration

    Test a notification configuration
    """
    body = {"notificationId":0,"eventTypes":["ACCOUNT_CLOSED","ACCOUNT_CLOSED"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Notification/v6/testNotificationConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_update_notification_configuration(client):
    """Test case for post_update_notification_configuration

    Update a notification subscription configuration
    """
    body = {"configurationDetails":{"hmacSignatureKey":"hmacSignatureKey","apiVersion":0,"eventConfigs":[{"includeMode":"EXCLUDE","eventType":"ACCOUNT_CLOSED"},{"includeMode":"EXCLUDE","eventType":"ACCOUNT_CLOSED"}],"notifyUsername":"notifyUsername","active":True,"description":"description","notifyURL":"notifyURL","sslProtocol":"TLSv12","notificationId":6,"notifyPassword":"notifyPassword"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Notification/v6/updateNotificationConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

