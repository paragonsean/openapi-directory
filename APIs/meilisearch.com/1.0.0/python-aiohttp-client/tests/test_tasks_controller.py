# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_cancel_tasks(client):
    """Test case for cancel_tasks

    Cancel tasks
    """
    params = [('uids', 'uids_example'),
                    ('indexUids', 'books'),
                    ('types', 'documentAdditionOrUpdate'),
                    ('statuses', 'failed'),
                    ('beforeEnqueuedAt', 'before_enqueued_at_example'),
                    ('afterEnqueuedAt', 'after_enqueued_at_example'),
                    ('beforeStartedAt', 'before_started_at_example'),
                    ('afterStartedAt', 'after_started_at_example'),
                    ('beforeFinishedAt', 'before_finished_at_example'),
                    ('afterFinishedAt', 'after_finished_at_example'),
                    ('canceledBy', 'canceled_by_example'),
                    ('limit', '2'),
                    ('from', '10')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/tasks/cancel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tasks(client):
    """Test case for delete_tasks

    Delete tasks
    """
    params = [('uids', 'uids_example'),
                    ('indexUids', 'books'),
                    ('types', 'documentAdditionOrUpdate'),
                    ('statuses', 'failed'),
                    ('beforeEnqueuedAt', 'before_enqueued_at_example'),
                    ('afterEnqueuedAt', 'after_enqueued_at_example'),
                    ('beforeStartedAt', 'before_started_at_example'),
                    ('afterStartedAt', 'after_started_at_example'),
                    ('beforeFinishedAt', 'before_finished_at_example'),
                    ('afterFinishedAt', 'after_finished_at_example'),
                    ('canceledBy', 'canceled_by_example'),
                    ('limit', '2'),
                    ('from', '10')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_tasks(client):
    """Test case for get_all_tasks

    Get all tasks
    """
    params = [('uids', '3'),
                    ('indexUids', 'books'),
                    ('types', 'documentAdditionOrUpdate'),
                    ('statuses', 'failed'),
                    ('beforeEnqueuedAt', 'before_enqueued_at_example'),
                    ('afterEnqueuedAt', 'after_enqueued_at_example'),
                    ('beforeStartedAt', 'before_started_at_example'),
                    ('afterStartedAt', 'after_started_at_example'),
                    ('beforeFinishedAt', 'before_finished_at_example'),
                    ('afterFinishedAt', 'after_finished_at_example'),
                    ('canceledBy', 'canceled_by_example'),
                    ('limit', '2'),
                    ('from', '10')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_one_task(client):
    """Test case for get_one_task

    Get one task
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/tasks/0',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

