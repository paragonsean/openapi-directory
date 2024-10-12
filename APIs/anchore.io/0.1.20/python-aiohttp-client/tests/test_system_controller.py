# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.anchore_error_code import AnchoreErrorCode
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.feed_metadata import FeedMetadata
from openapi_server.models.feed_sync_result import FeedSyncResult
from openapi_server.models.gate_spec import GateSpec
from openapi_server.models.service import Service
from openapi_server.models.status_response import StatusResponse
from openapi_server.models.system_status_response import SystemStatusResponse


pytestmark = pytest.mark.asyncio

async def test_delete_feed(client):
    """Test case for delete_feed

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/system/feeds/{feed}'.format(feed='feed_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_feed_group(client):
    """Test case for delete_feed_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/system/feeds/{feed}/{group}'.format(feed='feed_example', group='group_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    Delete the service config
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/system/services/{servicename}/{hostid}'.format(servicename='servicename_example', hostid='hostid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_error_codes(client):
    """Test case for describe_error_codes

    Describe anchore engine error codes.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/system/error_codes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_policy(client):
    """Test case for describe_policy

    Describe the policy language spec implemented by this service.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/system/policy_spec',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_detail(client):
    """Test case for get_service_detail

    System status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/system',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services_by_name(client):
    """Test case for get_services_by_name

    Get a service configuration and state
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/system/services/{servicename}'.format(servicename='servicename_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services_by_name_and_host(client):
    """Test case for get_services_by_name_and_host

    Get service config for a specific host
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/system/services/{servicename}/{hostid}'.format(servicename='servicename_example', hostid='hostid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    Service status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_system_feeds(client):
    """Test case for get_system_feeds

    list feeds operations and information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/system/feeds',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_services(client):
    """Test case for list_services

    List system services
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/system/services',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_system_feeds(client):
    """Test case for post_system_feeds

    trigger feeds operations
    """
    params = [('flush', True),
                    ('sync', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/system/feeds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_webhook(client):
    """Test case for test_webhook

    Adds the capabilities to test a webhook delivery for the given notification type
    """
    params = [('notification_type', tag_update)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/system/webhooks/{webhook_type}/test'.format(webhook_type='webhook_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_feed_enabled(client):
    """Test case for toggle_feed_enabled

    
    """
    params = [('enabled', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/system/feeds/{feed}'.format(feed='feed_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_group_enabled(client):
    """Test case for toggle_group_enabled

    
    """
    params = [('enabled', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/system/feeds/{feed}/{group}'.format(feed='feed_example', group='group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

