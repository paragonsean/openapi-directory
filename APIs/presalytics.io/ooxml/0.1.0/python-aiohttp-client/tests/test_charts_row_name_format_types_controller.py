# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chart_row_name_format_types import ChartRowNameFormatTypes
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_chart_rownameformattypes_get(client):
    """Test case for chart_rownameformattypes_get

    RowNameFormatTypes: List All Possible Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/RowNameFormatTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_rownameformattypes_get_id(client):
    """Test case for chart_rownameformattypes_get_id

    RowNameFormatTypes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/RowNameFormatTypes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_rownameformattypes_typeid_get_type_id(client):
    """Test case for chart_rownameformattypes_typeid_get_type_id

    RowNameFormatTypes: Get By Type Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/RowNameFormatTypes/TypeId/{type_id}'.format(type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

