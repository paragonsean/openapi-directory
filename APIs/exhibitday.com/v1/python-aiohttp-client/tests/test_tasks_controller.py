# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_tasks0_get(client):
    """Test case for tasks0_get

    
    """
    params = [('filter_by_integration_metadata_field_1', 'filter_by_integration_metadata_field_1_example'),
                    ('filter_by_integration_metadata_field_2', 'filter_by_integration_metadata_field_2_example'),
                    ('filter_by_integration_metadata_field_3', 'filter_by_integration_metadata_field_3_example'),
                    ('filter_by_integration_metadata_field_4', 'filter_by_integration_metadata_field_4_example'),
                    ('filter_by_integration_metadata_field_5', 'filter_by_integration_metadata_field_5_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'filter_by_event_id': 3.4,
        'filter_by_general_tasks_only': 3.4,
        'filter_by_incomplete_only': 'false',
        'filter_by_completed_only': 'false',
        'filter_by_no_due_date': 'false',
        'filter_by_due_date_greater_than_or_equal_to': '2013-10-20',
        'filter_by_due_date_smaller_than_or_equal_to': '2013-10-20',
        'filter_by_has_assignee': 'false',
        'filter_by_assignee_user_id': 'filter_by_assignee_user_id_example',
        'filter_by_task_name_contains_text': 'filter_by_task_name_contains_text_example',
        'hydrate_task_comments': 'false',
    }
    response = await client.request(
        method='GET',
        path='/v1/tasks/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks1_post(client):
    """Test case for tasks1_post

    
    """
    params = [('details', 'details_example'),
                    ('integration_metadata_field_1', 'integration_metadata_field_1_example'),
                    ('integration_metadata_field_2', 'integration_metadata_field_2_example'),
                    ('integration_metadata_field_3', 'integration_metadata_field_3_example'),
                    ('integration_metadata_field_4', 'integration_metadata_field_4_example'),
                    ('integration_metadata_field_5', 'integration_metadata_field_5_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'name': 'name_example',
        'event_id': 3.4,
        'task_section_id': 3.4,
        'is_completed': 'false',
        'due_date': '2013-10-20',
        'assignee_user_id': 'assignee_user_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/tasks/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks2_patch(client):
    """Test case for tasks2_patch

    
    """
    params = [('details', 'details_example'),
                    ('integration_metadata_field_1', 'integration_metadata_field_1_example'),
                    ('integration_metadata_field_2', 'integration_metadata_field_2_example'),
                    ('integration_metadata_field_3', 'integration_metadata_field_3_example'),
                    ('integration_metadata_field_4', 'integration_metadata_field_4_example'),
                    ('integration_metadata_field_5', 'integration_metadata_field_5_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
        'name': 'name_example',
        'task_section_id': 3.4,
        'is_completed': 'false',
        'due_date': '2013-10-20',
        'assignee_user_id': 'assignee_user_id_example',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/tasks/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks3_delete(client):
    """Test case for tasks3_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
    }
    response = await client.request(
        method='DELETE',
        path='/v1/tasks/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_comment0_get(client):
    """Test case for tasks_comment0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
    }
    response = await client.request(
        method='GET',
        path='/v1/tasks/comment',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_comment1_post(client):
    """Test case for tasks_comment1_post

    
    """
    params = [('comment', 'comment_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'task_id': 3.4,
    }
    response = await client.request(
        method='POST',
        path='/v1/tasks/comment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_comment2_patch(client):
    """Test case for tasks_comment2_patch

    
    """
    params = [('comment', 'comment_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
    }
    response = await client.request(
        method='PATCH',
        path='/v1/tasks/comment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_comment3_delete(client):
    """Test case for tasks_comment3_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
    }
    response = await client.request(
        method='DELETE',
        path='/v1/tasks/comment',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_comments0_get(client):
    """Test case for tasks_comments0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'filter_by_event_id': 3.4,
        'filter_by_task_id': 3.4,
        'hydrate_task': 'false',
    }
    response = await client.request(
        method='GET',
        path='/v1/tasks/comments',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_info0_get(client):
    """Test case for tasks_info0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
    }
    response = await client.request(
        method='GET',
        path='/v1/tasks/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

