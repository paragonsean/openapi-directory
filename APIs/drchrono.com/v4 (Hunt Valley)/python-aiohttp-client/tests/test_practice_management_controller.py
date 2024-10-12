# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.doctor_message import DoctorMessage
from openapi_server.models.inventory_categories_list200_response import InventoryCategoriesList200Response
from openapi_server.models.inventory_category import InventoryCategory
from openapi_server.models.inventory_vaccine import InventoryVaccine
from openapi_server.models.inventory_vaccines_list200_response import InventoryVaccinesList200Response
from openapi_server.models.messages_list200_response import MessagesList200Response
from openapi_server.models.office import Office
from openapi_server.models.offices_list200_response import OfficesList200Response
from openapi_server.models.task import Task
from openapi_server.models.task_categories_list200_response import TaskCategoriesList200Response
from openapi_server.models.task_category import TaskCategory
from openapi_server.models.task_note import TaskNote
from openapi_server.models.task_notes_list200_response import TaskNotesList200Response
from openapi_server.models.task_status import TaskStatus
from openapi_server.models.task_statuses_list200_response import TaskStatusesList200Response
from openapi_server.models.task_template import TaskTemplate
from openapi_server.models.task_templates_list200_response import TaskTemplatesList200Response
from openapi_server.models.tasks_list200_response import TasksList200Response


pytestmark = pytest.mark.asyncio

async def test_inventory_categories_list(client):
    """Test case for inventory_categories_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/inventory_categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_categories_read(client):
    """Test case for inventory_categories_read

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/inventory_categories/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_vaccines_create(client):
    """Test case for inventory_vaccines_create

    
    """
    params = [('status', 'status_example'),
                    ('cvx_code', 'cvx_code_example'),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/inventory_vaccines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_vaccines_list(client):
    """Test case for inventory_vaccines_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('status', 'status_example'),
                    ('cvx_code', 'cvx_code_example'),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/inventory_vaccines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_vaccines_read(client):
    """Test case for inventory_vaccines_read

    
    """
    params = [('status', 'status_example'),
                    ('cvx_code', 'cvx_code_example'),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/inventory_vaccines/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_create(client):
    """Test case for messages_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56),
                    ('responsible_user', 56),
                    ('updated_since', 'updated_since_example'),
                    ('received_since', 'received_since_example'),
                    ('owner', 56),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_delete(client):
    """Test case for messages_delete

    
    """
    params = [('patient', 56),
                    ('doctor', 56),
                    ('responsible_user', 56),
                    ('updated_since', 'updated_since_example'),
                    ('received_since', 'received_since_example'),
                    ('owner', 56),
                    ('type', 'type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_list(client):
    """Test case for messages_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56),
                    ('responsible_user', 56),
                    ('updated_since', 'updated_since_example'),
                    ('received_since', 'received_since_example'),
                    ('owner', 56),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_partial_update(client):
    """Test case for messages_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56),
                    ('responsible_user', 56),
                    ('updated_since', 'updated_since_example'),
                    ('received_since', 'received_since_example'),
                    ('owner', 56),
                    ('type', 'type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_read(client):
    """Test case for messages_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56),
                    ('responsible_user', 56),
                    ('updated_since', 'updated_since_example'),
                    ('received_since', 'received_since_example'),
                    ('owner', 56),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_update(client):
    """Test case for messages_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56),
                    ('responsible_user', 56),
                    ('updated_since', 'updated_since_example'),
                    ('received_since', 'received_since_example'),
                    ('owner', 56),
                    ('type', 'type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offices_add_exam_room(client):
    """Test case for offices_add_exam_room

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/offices/{id}/add_exam_room'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offices_list(client):
    """Test case for offices_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/offices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offices_partial_update(client):
    """Test case for offices_partial_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/offices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offices_read(client):
    """Test case for offices_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/offices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offices_update(client):
    """Test case for offices_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/offices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_categories_create(client):
    """Test case for task_categories_create

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/task_categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_categories_list(client):
    """Test case for task_categories_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_categories_partial_update(client):
    """Test case for task_categories_partial_update

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/task_categories/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_categories_read(client):
    """Test case for task_categories_read

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_categories/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_categories_update(client):
    """Test case for task_categories_update

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/task_categories/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_notes_create(client):
    """Test case for task_notes_create

    
    """
    params = [('task', 56),
                    ('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/task_notes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_notes_list(client):
    """Test case for task_notes_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('task', 56),
                    ('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_notes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_notes_partial_update(client):
    """Test case for task_notes_partial_update

    
    """
    params = [('task', 56),
                    ('since', 'since_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/task_notes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_notes_read(client):
    """Test case for task_notes_read

    
    """
    params = [('task', 56),
                    ('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_notes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_notes_update(client):
    """Test case for task_notes_update

    
    """
    params = [('task', 56),
                    ('since', 'since_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/task_notes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_statuses_create(client):
    """Test case for task_statuses_create

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/task_statuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_statuses_list(client):
    """Test case for task_statuses_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_statuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_statuses_partial_update(client):
    """Test case for task_statuses_partial_update

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/task_statuses/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_statuses_read(client):
    """Test case for task_statuses_read

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_statuses/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_statuses_update(client):
    """Test case for task_statuses_update

    
    """
    params = [('since', 'since_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/task_statuses/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_templates_create(client):
    """Test case for task_templates_create

    
    """
    params = [('assignee_user', 56),
                    ('status', 56),
                    ('assignee_group', 56),
                    ('since', 'since_example'),
                    ('category', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/task_templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_templates_list(client):
    """Test case for task_templates_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('assignee_user', 56),
                    ('status', 56),
                    ('assignee_group', 56),
                    ('since', 'since_example'),
                    ('category', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_templates_partial_update(client):
    """Test case for task_templates_partial_update

    
    """
    params = [('assignee_user', 56),
                    ('status', 56),
                    ('assignee_group', 56),
                    ('since', 'since_example'),
                    ('category', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/task_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_templates_read(client):
    """Test case for task_templates_read

    
    """
    params = [('assignee_user', 56),
                    ('status', 56),
                    ('assignee_group', 56),
                    ('since', 'since_example'),
                    ('category', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/task_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_templates_update(client):
    """Test case for task_templates_update

    
    """
    params = [('assignee_user', 56),
                    ('status', 56),
                    ('assignee_group', 56),
                    ('since', 'since_example'),
                    ('category', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/task_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_create(client):
    """Test case for tasks_create

    
    """
    params = [('status', 56),
                    ('category', 56),
                    ('due_at_date', 'due_at_date_example'),
                    ('due_at_unknown', 'due_at_unknown_example'),
                    ('since', 'since_example'),
                    ('due_at_since', 'due_at_since_example'),
                    ('assignee_user', 56),
                    ('assignee_group', 56),
                    ('due_at_range', 'due_at_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_list(client):
    """Test case for tasks_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('status', 56),
                    ('category', 56),
                    ('due_at_date', 'due_at_date_example'),
                    ('due_at_unknown', 'due_at_unknown_example'),
                    ('since', 'since_example'),
                    ('due_at_since', 'due_at_since_example'),
                    ('assignee_user', 56),
                    ('assignee_group', 56),
                    ('due_at_range', 'due_at_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_partial_update(client):
    """Test case for tasks_partial_update

    
    """
    params = [('status', 56),
                    ('category', 56),
                    ('due_at_date', 'due_at_date_example'),
                    ('due_at_unknown', 'due_at_unknown_example'),
                    ('since', 'since_example'),
                    ('due_at_since', 'due_at_since_example'),
                    ('assignee_user', 56),
                    ('assignee_group', 56),
                    ('due_at_range', 'due_at_range_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tasks/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_read(client):
    """Test case for tasks_read

    
    """
    params = [('status', 56),
                    ('category', 56),
                    ('due_at_date', 'due_at_date_example'),
                    ('due_at_unknown', 'due_at_unknown_example'),
                    ('since', 'since_example'),
                    ('due_at_since', 'due_at_since_example'),
                    ('assignee_user', 56),
                    ('assignee_group', 56),
                    ('due_at_range', 'due_at_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tasks/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_update(client):
    """Test case for tasks_update

    
    """
    params = [('status', 56),
                    ('category', 56),
                    ('due_at_date', 'due_at_date_example'),
                    ('due_at_unknown', 'due_at_unknown_example'),
                    ('since', 'since_example'),
                    ('due_at_since', 'due_at_since_example'),
                    ('assignee_user', 56),
                    ('assignee_group', 56),
                    ('due_at_range', 'due_at_range_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tasks/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

