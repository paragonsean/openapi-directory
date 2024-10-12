# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config import Config
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_config_config_get(client):
    """Test case for config_config_get

    Config
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topic_topic_topic_name_get(client):
    """Test case for topic_topic_topic_name_get

    Topic
    """
    params = [('message', 'message_example'),
                    ('base64_message', 'base64_message_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/topic/{topic_name}'.format(topic_name='topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

