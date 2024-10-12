# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_checkout_post201_response import ClockingRecordsCheckoutPost201Response
from openapi_server.models.error_not_found import ErrorNotFound


pytestmark = pytest.mark.asyncio

async def test_expenses_expense_id_original_files_file_id_get(client):
    """Test case for expenses_expense_id_original_files_file_id_get

    Show OIOUBL file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expenses/{expense_id}/original_files/{file_id}'.format(expense_id='expense_id_example', file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_expense_id_original_files_get(client):
    """Test case for expenses_expense_id_original_files_get

    Show list of all OIOUBL files for the expense
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expenses/{expense_id}/original_files'.format(expense_id='expense_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

