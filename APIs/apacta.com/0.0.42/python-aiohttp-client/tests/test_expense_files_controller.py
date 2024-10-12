# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_files_expense_file_id_get200_response import ExpenseFilesExpenseFileIdGet200Response
from openapi_server.models.expense_files_expense_file_id_put200_response import ExpenseFilesExpenseFileIdPut200Response
from openapi_server.models.expense_files_get200_response import ExpenseFilesGet200Response


pytestmark = pytest.mark.asyncio

async def test_expense_files_expense_file_id_delete(client):
    """Test case for expense_files_expense_file_id_delete

    Delete file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/expense_files/{expense_file_id}'.format(expense_file_id='expense_file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_files_expense_file_id_get(client):
    """Test case for expense_files_expense_file_id_get

    Show file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expense_files/{expense_file_id}'.format(expense_file_id='expense_file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_files_expense_file_id_put(client):
    """Test case for expense_files_expense_file_id_put

    Edit file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/expense_files/{expense_file_id}'.format(expense_file_id='expense_file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_files_get(client):
    """Test case for expense_files_get

    Show list of expense files
    """
    params = [('created_by_id', 'created_by_id_example'),
                    ('expense_id', 'expense_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expense_files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_expense_files_post(client):
    """Test case for expense_files_post

    Add file to expense
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/expense_files',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

