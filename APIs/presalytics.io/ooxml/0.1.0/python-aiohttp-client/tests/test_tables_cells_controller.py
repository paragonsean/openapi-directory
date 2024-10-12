# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.table_cells import TableCells


pytestmark = pytest.mark.asyncio

async def test_tables_cells_get_id(client):
    """Test case for tables_cells_get_id

    Cells: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Tables/Cells/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

