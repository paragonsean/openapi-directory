# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.commititemfeedorderstatus_request import CommititemfeedorderstatusRequest
from openapi_server.models.feed_configuration_request import FeedConfigurationRequest
from openapi_server.models.get_feed_configuration200_response import GetFeedConfiguration200Response
from openapi_server.models.getfeedorderstatus import Getfeedorderstatus
from openapi_server.models.test_jso_nata_expression import TestJSONataExpression


pytestmark = pytest.mark.asyncio

async def test_commititemfeedorderstatus(client):
    """Test case for commititemfeedorderstatus

    Commit feed items
    """
    body = {"handles":["AQEBSM/bSqonHYtx+UrHdbuJ0i7M9yMbI2jtYwMIPdEc4BenuneaCTC9VEJ3dgAy1XtfQvHBvgwZTO8LvGObIKNqiKXDZiMKY25vK+pblZEqf1pWdLMugu5XoHA5ZAd4IcBcXrBcrlr1GU8uvPEBoVLOsVBP9IAxIZkkeEedIDg3K6GPyEXVuPlTEYb/0OCunEGxWF+AZ1frFdXh7ulORTcuqO5oDlBGbpD+QYzCmF4mUZtQ0VVWh9icM1QBVh6PlJ0D/lfwnJKWpBn3jf8c+DTm7sD7wb1Lcz9uWMLhDtPwvH9vue4MvKU9sCahEQe7K5jWuwwb54szGbFKdfcACsTSQ9WlyBfMdbV83c27k68G3cnaBFExkC1MLHHE9UzpQ6l4s43BT4k95ocgMXffnj/HMUYXn+OCvlvjytY59x1OCRE="]}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/feed',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_feed_configuration(client):
    """Test case for feed_configuration

    Create or update feed configuration
    """
    body = {"filter":{"expression":"expression","disableSingleFire":False,"type":"FromWorkflow","status":["status","status"]},"queue":{"visibilityTimeoutInSeconds":250,"MessageRetentionPeriodInSeconds":3456000}}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/feed/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_feed_configuration_delete(client):
    """Test case for feed_configuration_delete

    Delete feed configuration
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/orders/feed/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feed_configuration(client):
    """Test case for get_feed_configuration

    Get feed configuration
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/orders/feed/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getfeedorderstatus1(client):
    """Test case for getfeedorderstatus1

    Retrieve feed items
    """
    params = [('maxlot', '{{maxLot}}')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/orders/feed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_jso_nata_expression(client):
    """Test case for test_jso_nata_expression

    Test JSONata expression
    """
    body = {"Expression":"Expression","Document":"Document"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/expressions/jsonata',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

