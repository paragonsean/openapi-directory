# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.table_columns import TableColumns


pytestmark = pytest.mark.asyncio

async def test_tables_columns_get_id(client):
    """Test case for tables_columns_get_id

    Columns: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Tables/Columns/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

