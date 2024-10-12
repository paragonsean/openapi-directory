# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.input_csv_conversion_json import InputCsvConversionJSON
from openapi_server.models.input_data_query import InputDataQuery
from openapi_server.models.input_json_conversion_csv import InputJsonConversionCSV
from openapi_server.models.input_json_conversion_html import InputJsonConversionHTML
from openapi_server.models.input_json_conversion_xml import InputJsonConversionXML
from openapi_server.models.input_xml_conversion_json import InputXmlConversionJSON
from openapi_server.models.output_string import OutputString


pytestmark = pytest.mark.asyncio

async def test_csv_to_json(client):
    """Test case for csv_to_json

    Data - CSV to JSON
    """
    csv_conversion_json = openapi_server.InputCsvConversionJSON()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CSVtoJSON',
        headers=headers,
        json=csv_conversion_json,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_json_to_csv(client):
    """Test case for json_to_csv

    Data - JSON to CSV
    """
    json_conversion_csv = openapi_server.InputJsonConversionCSV()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/JSONtoCSV',
        headers=headers,
        json=json_conversion_csv,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_json_to_html(client):
    """Test case for json_to_html

    Data - JSON to HTML Table
    """
    json_conversion_html = openapi_server.InputJsonConversionHTML()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/JSONtoHTML',
        headers=headers,
        json=json_conversion_html,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_json_to_xml(client):
    """Test case for json_to_xml

    Data - JSON to XML
    """
    json_conversion_xml = openapi_server.InputJsonConversionXML()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/JSONtoXML',
        headers=headers,
        json=json_conversion_xml,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_json(client):
    """Test case for query_json

    Data - Query JSON
    """
    input_data_query = openapi_server.InputDataQuery()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/QueryJSON',
        headers=headers,
        json=input_data_query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_xml(client):
    """Test case for query_xml

    Data - Query XML
    """
    input_data_query = openapi_server.InputDataQuery()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/QueryXML',
        headers=headers,
        json=input_data_query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_xml_to_json(client):
    """Test case for xml_to_json

    Data - XML to JSON
    """
    xml_conversion_json = openapi_server.InputXmlConversionJSON()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/XMLtoJSON',
        headers=headers,
        json=xml_conversion_json,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

