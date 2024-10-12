# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_files_expense_file_id_put200_response import ExpenseFilesExpenseFileIdPut200Response
from openapi_server.models.projects_get200_response import ProjectsGet200Response
from openapi_server.models.projects_has_projects_with_custom_statuses_get200_response import ProjectsHasProjectsWithCustomStatusesGet200Response
from openapi_server.models.projects_post_request import ProjectsPostRequest
from openapi_server.models.projects_project_id_all_files_get200_response import ProjectsProjectIdAllFilesGet200Response
from openapi_server.models.projects_project_id_get200_response import ProjectsProjectIdGet200Response
from openapi_server.models.projects_project_id_put_request import ProjectsProjectIdPutRequest
from openapi_server.models.projects_project_id_send_bulk_pdf_post_request import ProjectsProjectIdSendBulkPdfPostRequest
from openapi_server.models.projects_project_id_users_get200_response import ProjectsProjectIdUsersGet200Response
from openapi_server.models.projects_project_id_users_post_request import ProjectsProjectIdUsersPostRequest
from openapi_server.models.projects_project_id_users_user_id_get200_response import ProjectsProjectIdUsersUserIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_projects_get(client):
    """Test case for projects_get

    View list of projects
    """
    params = [('show_all', False),
                    ('sort', 'sort_example'),
                    ('direction', 'direction_example'),
                    ('contact_id', 'contact_id_example'),
                    ('company_id', 'company_id_example'),
                    ('project_status_id', 'project_status_id_example'),
                    ('project_status_ids', ['project_status_ids_example']),
                    ('name', 'name_example'),
                    ('erp_project_id', 'erp_project_id_example'),
                    ('erp_task_id', 'erp_task_id_example'),
                    ('start_time_gte', 'start_time_gte_example'),
                    ('start_time_lte', 'start_time_lte_example'),
                    ('start_time_eq', 'start_time_eq_example'),
                    ('event_start[][gt]', 'event_start_gt_example'),
                    ('event_start[][lt]', 'event_start_lt_example'),
                    ('event_start[][eq]', 'event_start_eq_example'),
                    ('event_end[][gt]', 'event_end_gt_example'),
                    ('event_end[][lt]', 'event_end_lt_example'),
                    ('event_end[][eq]', 'event_end_eq_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_has_projects_with_custom_statuses_get_0(client):
    """Test case for projects_has_projects_with_custom_statuses_get_0

    Check if the company has projects with custom statuses
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/has_projects_with_custom_statuses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_post(client):
    """Test case for projects_post

    Add a project
    """
    body = openapi_server.ProjectsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_all_files_get(client):
    """Test case for projects_project_id_all_files_get

    Show list of all files uploaded to project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}/all_files'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_delete(client):
    """Test case for projects_project_id_delete

    Delete a project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/projects/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_files_file_id_delete(client):
    """Test case for projects_project_id_files_file_id_delete

    Delete file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/projects/{project_id}/files/{file_id}'.format(project_id='project_id_example', file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_files_file_id_get(client):
    """Test case for projects_project_id_files_file_id_get

    Show file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}/files/{file_id}'.format(project_id='project_id_example', file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_files_file_id_put(client):
    """Test case for projects_project_id_files_file_id_put

    Edit file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/projects/{project_id}/files/{file_id}'.format(project_id='project_id_example', file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_files_get(client):
    """Test case for projects_project_id_files_get

    Show list of files uploaded to project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}/files'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_get(client):
    """Test case for projects_project_id_get

    View specific project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_project_files_get(client):
    """Test case for projects_project_id_project_files_get

    Show list of project files uploaded to project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}/project_files'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_projects_project_id_project_files_post(client):
    """Test case for projects_project_id_project_files_post

    Add project file to projects
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/projects/{project_id}/project_files'.format(project_id='project_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_project_files_project_file_id_delete(client):
    """Test case for projects_project_id_project_files_project_file_id_delete

    Delete project file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/projects/{project_id}/project_files/{project_file_id}'.format(project_file_id='project_file_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_project_files_project_file_id_get(client):
    """Test case for projects_project_id_project_files_project_file_id_get

    Show project file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}/project_files/{project_file_id}'.format(project_id='project_id_example', project_file_id='project_file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_project_files_project_file_id_put(client):
    """Test case for projects_project_id_project_files_project_file_id_put

    Edit project file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/projects/{project_id}/project_files/{project_file_id}'.format(project_id='project_id_example', project_file_id='project_file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_put(client):
    """Test case for projects_project_id_put

    Edit a project
    """
    body = openapi_server.ProjectsProjectIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/projects/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_send_bulk_pdf_post(client):
    """Test case for projects_project_id_send_bulk_pdf_post

    Send bulk forms pdf by email
    """
    body = openapi_server.ProjectsProjectIdSendBulkPdfPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/projects/{project_id}/send_bulk_pdf'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_users_get(client):
    """Test case for projects_project_id_users_get

    Show list of users added to project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}/users'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_users_post(client):
    """Test case for projects_project_id_users_post

    Add user to project
    """
    body = openapi_server.ProjectsProjectIdUsersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/projects/{project_id}/users'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_users_user_id_delete(client):
    """Test case for projects_project_id_users_user_id_delete

    Delete user from project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/projects/{project_id}/users/{user_id}'.format(user_id='user_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_project_id_users_user_id_get(client):
    """Test case for projects_project_id_users_user_id_get

    View specific user assigned to project
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects/{project_id}/users/{user_id}'.format(user_id='user_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

