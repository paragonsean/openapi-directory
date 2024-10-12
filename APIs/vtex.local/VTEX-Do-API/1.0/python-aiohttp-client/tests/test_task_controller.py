# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_comment_request import AddCommentRequest
from openapi_server.models.edit_task_request import EditTaskRequest
from openapi_server.models.new_task_request import NewTaskRequest


pytestmark = pytest.mark.asyncio

async def test_add_comment(client):
    """Test case for add_comment

    Add Comment on a Task
    """
    body = {"text":"escreva seu comentário"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tasks/{task_id}/comments'.format(task_id='123456abc'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_task(client):
    """Test case for edit_task

    Update Task
    """
    body = {"status":"InProgress"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tasks/{task_id}'.format(task_id='123456abc'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task(client):
    """Test case for get_task

    Retrieve Task
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tasks/{task_id}'.format(task_id='123456abc'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listtasksbyassignee(client):
    """Test case for listtasksbyassignee

    List tasks
    """
    params = [('assignee.email', '{{assigneeEmail}}'),
                    ('target.id', '{{targetId}}'),
                    ('context', '{{context}}'),
                    ('page', '{{page}}'),
                    ('perPage', '{{desired number per page}}'),
                    ('status', 'open')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_new_task(client):
    """Test case for new_task

    Create Task
    """
    body = {"assignee":{"email":"frederico.santos@vtex.com.br","id":null,"name":null},"context":"Marketplace","description":"Ajudar na doc API para lancar no postman","domain":"oms","dueDate":"2016-03-01","followers":[{"email":"alan.dantas@vtex.com.br","id":null,"name":null}],"name":"pricing","parentTaskId":null,"priority":"Critical","surrogateKey":"505224-0","target":[{"id":"633730670642-01","type":"order","url":"https://recorrenciaqa.vtexcommercebeta.com.br/admin/checkout/orders/633730670642-01"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tasks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

