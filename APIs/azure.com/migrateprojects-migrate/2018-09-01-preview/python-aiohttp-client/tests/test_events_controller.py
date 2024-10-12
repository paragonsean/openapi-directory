# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_collection import EventCollection
from openapi_server.models.migrate_event import MigrateEvent


pytestmark = pytest.mark.asyncio

async def test_events_delete_event(client):
    """Test case for events_delete_event

    Delete the migrate event
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/migrateEvents/{event_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', event_name='event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_enumerate_events(client):
    """Test case for events_enumerate_events

    Gets a list of events in the migrate project.
    """
    params = [('api-version', 'api_version_example'),
                    ('continuationToken', 'continuation_token_example'),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/migrateEvents'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_get_event(client):
    """Test case for events_get_event

    Gets an event in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/migrateEvents/{event_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', event_name='event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

