# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_pkg_notification import AppPkgNotification
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_app_pkg_notification_post(client):
    """Test case for app_pkg_notification_post

    Registers a notification endpoint to notify application package operations
    """
    body = {"timeStamp":{"seconds":6,"nanoSeconds":0},"appPkgId":"appPkgId","_links":{"subscription":{"href":"https://openapi-generator.tech"}},"appDId":"appDId","id":"id","notificationType":"AppPackageOnBoarded","operationalState":"DISABLED","subscriptionId":"subscriptionId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/user_defined_notification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

