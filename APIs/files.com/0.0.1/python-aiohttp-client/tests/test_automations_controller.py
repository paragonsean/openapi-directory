# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.automation_entity import AutomationEntity


pytestmark = pytest.mark.asyncio

async def test_delete_automations_id(client):
    """Test case for delete_automations_id

    Delete Automation
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/automations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automations(client):
    """Test case for get_automations

    List Automations
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('automation', 'automation_example'),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None),
                    ('with_deleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/automations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automations_id(client):
    """Test case for get_automations_id

    Show Automation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/automations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_automations_id(client):
    """Test case for patch_automations_id

    Update Automation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('automation', 'automation_example')
    data.add_field('description', 'description_example')
    data.add_field('destination', 'destination_example')
    data.add_field('destination_replace_from', 'destination_replace_from_example')
    data.add_field('destination_replace_to', 'destination_replace_to_example')
    data.add_field('destinations', ['destinations_example'])
    data.add_field('disabled', True)
    data.add_field('group_ids', 'group_ids_example')
    data.add_field('interval', 'interval_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('recurring_day', 56)
    data.add_field('schedule', None)
    data.add_field('source', 'source_example')
    data.add_field('sync_ids', 'sync_ids_example')
    data.add_field('trigger', 'trigger_example')
    data.add_field('trigger_actions', ['trigger_actions_example'])
    data.add_field('user_ids', 'user_ids_example')
    data.add_field('value', None)
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/automations/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_automations(client):
    """Test case for post_automations

    Create Automation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('automation', 'automation_example')
    data.add_field('description', 'description_example')
    data.add_field('destination', 'destination_example')
    data.add_field('destination_replace_from', 'destination_replace_from_example')
    data.add_field('destination_replace_to', 'destination_replace_to_example')
    data.add_field('destinations', ['destinations_example'])
    data.add_field('disabled', True)
    data.add_field('group_ids', 'group_ids_example')
    data.add_field('interval', 'interval_example')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('recurring_day', 56)
    data.add_field('schedule', None)
    data.add_field('source', 'source_example')
    data.add_field('sync_ids', 'sync_ids_example')
    data.add_field('trigger', 'trigger_example')
    data.add_field('trigger_actions', ['trigger_actions_example'])
    data.add_field('user_ids', 'user_ids_example')
    data.add_field('value', None)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/automations',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

