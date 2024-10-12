# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_formats import ArtifactFormats
from openapi_server.models.change_log_item import ChangeLogItem
from openapi_server.models.event_type import EventType


pytestmark = pytest.mark.asyncio

async def test_artifact_formats_get(client):
    """Test case for artifact_formats_get

    Artifact formats
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/artifact-formats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_log_get(client):
    """Test case for change_log_get

    Recent changes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/change-log',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_types_get(client):
    """Test case for event_types_get

    Event types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/event-types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

