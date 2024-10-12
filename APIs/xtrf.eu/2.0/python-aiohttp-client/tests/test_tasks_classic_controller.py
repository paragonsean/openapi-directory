# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contacts_dto import ContactsDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.file_dto import FileDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.project_dates_dto import ProjectDatesDTO
from openapi_server.models.string_dto import StringDTO
from openapi_server.models.task_files_dto import TaskFilesDTO
from openapi_server.models.task_progress_dto import TaskProgressDTO


pytestmark = pytest.mark.asyncio

async def test_add_file(client):
    """Test case for add_file

    Adds files to a given task.
    """
    body = {"name":"name","content":"content","url":"url","token":"token"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/tasks/{task_id}/files/input'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete14(client):
    """Test case for delete14

    Removes a task.
    """
    params = [('removeFilesFromDisc', True),
                    ('removeExternalProjects', True),
                    ('forceJobsRemoval', True)]
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/tasks/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contacts1(client):
    """Test case for get_contacts1

    Returns contacts of a given task.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/tasks/{task_id}/contacts'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields7(client):
    """Test case for get_custom_fields7

    Returns custom fields of a given task.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/tasks/{task_id}/customFields'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dates3(client):
    """Test case for get_dates3

    Returns dates of a given task.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/tasks/{task_id}/dates'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instructions2(client):
    """Test case for get_instructions2

    Returns instructions of a given task.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/tasks/{task_id}/instructions'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_progress(client):
    """Test case for get_progress

    Returns progress of a given task.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/tasks/{task_id}/progress'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_files(client):
    """Test case for get_task_files

    Returns lists of files of a given task.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/tasks/{task_id}/files'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start1(client):
    """Test case for start1

    Starts a task.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/tasks/{task_id}/start'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_task_po_number(client):
    """Test case for update_client_task_po_number

    Updates Client Task PO Number of a given task.
    """
    body = {"value":"value"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/tasks/{task_id}/clientTaskPONumber'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_contacts1(client):
    """Test case for update_contacts1

    Updates contacts of a given task.
    """
    body = {"sendBackToId":5,"primaryId":5,"additionalIds":[1,1]}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/tasks/{task_id}/contacts'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_fields5(client):
    """Test case for update_custom_fields5

    Updates custom fields of a given task.
    """
    body = {"name":"name","type":"TEXT","value":"{}","key":"key"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/tasks/{task_id}/customFields'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_dates2(client):
    """Test case for update_dates2

    Updates dates of a given task.
    """
    body = {"actualDeliveryDate":{"value":6},"actualStartDate":{"value":6},"deadline":{"value":6},"startDate":{"value":6}}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/tasks/{task_id}/dates'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_instructions3(client):
    """Test case for update_instructions3

    Updates instructions of a given task.
    """
    body = {"internal":"internal","notes":"notes","forProvider":"forProvider","paymentNoteForCustomer":"paymentNoteForCustomer","fromCustomer":"fromCustomer","paymentNoteForVendor":"paymentNoteForVendor"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/tasks/{task_id}/instructions'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_name(client):
    """Test case for update_name

    Updates name of a given task.
    """
    body = {"value":"value"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/tasks/{task_id}/name'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

