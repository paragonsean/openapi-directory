# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chart_axis_data_types import ChartAxisDataTypes
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_chart_axisdatatypes_get(client):
    """Test case for chart_axisdatatypes_get

    AxisDataTypes: List All Possible Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/AxisDataTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_axisdatatypes_get_id(client):
    """Test case for chart_axisdatatypes_get_id

    AxisDataTypes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/AxisDataTypes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_axisdatatypes_typeid_get_type_id(client):
    """Test case for chart_axisdatatypes_typeid_get_type_id

    AxisDataTypes: Get By Type Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/AxisDataTypes/TypeId/{type_id}'.format(type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

