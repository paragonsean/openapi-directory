# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chart_row_col import ChartRowCol
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_chart_rowcol_get(client):
    """Test case for chart_rowcol_get

    RowCol: List All Possible Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/RowCol',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_rowcol_get_id(client):
    """Test case for chart_rowcol_get_id

    RowCol: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/RowCol/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_rowcol_typeid_get_type_id(client):
    """Test case for chart_rowcol_typeid_get_type_id

    RowCol: Get By Type Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/RowCol/TypeId/{type_id}'.format(type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

