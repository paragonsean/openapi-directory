# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_types_list_result import EventTypesListResult
from openapi_server.models.topic_type_info import TopicTypeInfo
from openapi_server.models.topic_types_list_result import TopicTypesListResult


pytestmark = pytest.mark.asyncio

async def test_topic_types_get(client):
    """Test case for topic_types_get

    Get a topic type
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.EventGrid/topicTypes/{topic_type_name}'.format(topic_type_name='topic_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topic_types_list(client):
    """Test case for topic_types_list

    List topic types
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.EventGrid/topicTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topic_types_list_event_types(client):
    """Test case for topic_types_list_event_types

    List event types
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.EventGrid/topicTypes/{topic_type_name}/eventTypes'.format(topic_type_name='topic_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

