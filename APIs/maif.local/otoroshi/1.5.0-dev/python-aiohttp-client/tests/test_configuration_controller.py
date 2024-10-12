# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.global_config import GlobalConfig
from openapi_server.models.patch_inner import PatchInner


pytestmark = pytest.mark.asyncio

async def test_global_config(client):
    """Test case for global_config

    Get the full configuration of Otoroshi
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/globalconfig',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_global_config(client):
    """Test case for patch_global_config

    Update the global configuration with a diff
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/globalconfig',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_global_config(client):
    """Test case for put_global_config

    Update the global configuration
    """
    body = {"maxLogsSize":123123,"apiReadOnly":True,"analyticsWebhooks":[{"headers":{"key":"value"},"url":"http://www.google.com"},{"headers":{"key":"value"},"url":"http://www.google.com"}],"elasticReadsConfig":{"clusterUri":"a string value","headers":{"key":"value"},"password":"a string value","index":"a string value","type":"a string value","user":"a string value"},"limitConcurrentRequests":True,"maxConcurrentRequests":123,"endlessIpAddresses":["192.192.192.192","192.192.192.192"],"maxHttp10ResponseSize":123,"streamEntityOnly":True,"backofficeAuth0Config":{"clientId":"a string value","domain":"a string value","callbackUrl":"a string value","clientSecret":"a string value"},"alertsEmails":["admin@otoroshi.io","admin@otoroshi.io"],"autoLinkToDefaultGroup":True,"alertsWebhooks":[{"headers":{"key":"value"},"url":"http://www.google.com"},{"headers":{"key":"value"},"url":"http://www.google.com"}],"middleFingers":True,"privateAppsAuth0Config":{"clientId":"a string value","domain":"a string value","callbackUrl":"a string value","clientSecret":"a string value"},"throttlingQuota":123,"cleverSettings":{"consumerSecret":"a string value","orgaId":"a string value","secret":"a string value","consumerKey":"a string value","token":"a string value"},"u2fLoginOnly":True,"ipFiltering":{"blacklist":["192.192.192.192","192.192.192.192"],"whitelist":["192.192.192.192","192.192.192.192"]},"mailerSettings":{"eu":True,"apiKey":"a string value","domain":"a string value","apiKeyPrivate":"a string value","header":{"key":"value"},"apiKeyPublic":"a string value","type":"a string value","url":"a string value"},"perIpThrottlingQuota":123,"elasticWritesConfigs":[{"clusterUri":"a string value","headers":{"key":"value"},"password":"a string value","index":"a string value","type":"a string value","user":"a string value"},{"clusterUri":"a string value","headers":{"key":"value"},"password":"a string value","index":"a string value","type":"a string value","user":"a string value"}],"lines":["a string value","a string value"],"useCircuitBreakers":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/globalconfig',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

