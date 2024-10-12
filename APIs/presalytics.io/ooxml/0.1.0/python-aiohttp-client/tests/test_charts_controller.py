# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chart_chart_data_dto import ChartChartDataDTO
from openapi_server.models.chart_charts import ChartCharts
from openapi_server.models.chart_charts_details import ChartChartsDetails
from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.ooxml_dto import OoxmlDTO
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_charts_charts_chartupdate_get_id(client):
    """Test case for charts_charts_chartupdate_get_id

    Charts: Get Chart Data
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/ChartUpdate/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_charts_charts_chartupdate_put_id(client):
    """Test case for charts_charts_chartupdate_put_id

    Charts: Update Chart Data
    """
    body = openapi_server.ChartChartDataDTO()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='PUT',
        path='/ooxml-automation/Charts/ChartUpdate/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charts_charts_childobjects_get_id(client):
    """Test case for charts_charts_childobjects_get_id

    Charts: Get Dependent Objects Tree
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/ChildObjects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charts_charts_details_get_id(client):
    """Test case for charts_charts_details_get_id

    Charts: Get Details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/Details/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charts_charts_get_id(client):
    """Test case for charts_charts_get_id

    Charts: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charts_charts_openofficexml_get_id_updated(client):
    """Test case for charts_charts_openofficexml_get_id_updated

    Charts: Get Underlying Xml
    """
    params = [('updated', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_charts_charts_openofficexml_put_id(client):
    """Test case for charts_charts_openofficexml_put_id

    Charts: Modify Underlying Xml
    """
    body = {"openOfficeXml":"openOfficeXml","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='PUT',
        path='/ooxml-automation/Charts/OpenOfficeXml/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charts_charts_svg_get_id_use_cache(client):
    """Test case for charts_charts_svg_get_id_use_cache

    Charts: Get Svg file
    """
    params = [('use_cache', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/Svg/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

