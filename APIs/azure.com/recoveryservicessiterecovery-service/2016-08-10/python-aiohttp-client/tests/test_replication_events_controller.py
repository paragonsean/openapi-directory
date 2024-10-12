# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.event_collection import EventCollection


pytestmark = pytest.mark.asyncio

async def test_replication_events_get(client):
    """Test case for replication_events_get

    Get the details of an Azure Site recovery event.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationEvents/{event_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', event_name='event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_events_list(client):
    """Test case for replication_events_list

    Gets the list of Azure Site Recovery events.
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationEvents'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

