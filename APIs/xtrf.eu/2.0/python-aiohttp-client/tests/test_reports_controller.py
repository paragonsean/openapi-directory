# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.export_request_dto import ExportRequestDTO
from openapi_server.models.import_request_dto import ImportRequestDTO
from openapi_server.models.import_result_dto import ImportResultDTO
from openapi_server.models.preferred_request_dto import PreferredRequestDTO
from openapi_server.models.report_result_dto import ReportResultDTO


pytestmark = pytest.mark.asyncio

async def test_delete11(client):
    """Test case for delete11

    Removes a report.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/reports/{report_id}'.format(report_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_duplicate1(client):
    """Test case for duplicate1

    Duplicates a report.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/reports/{report_id}/duplicate'.format(report_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_export_to_xml(client):
    """Test case for export_to_xml

    Exports reports definition to XML.
    """
    body = /home-api/assets/examples/reports/exportToXML.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/reports/export/xml',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_csv(client):
    """Test case for generate_csv

    Generates CSV content for a report.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/reports/{report_id}/result/csv'.format(report_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_printer_friendly(client):
    """Test case for generate_printer_friendly

    Generates printer friendly content for a report.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/reports/{report_id}/result/printerFriendly'.format(report_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_import_from_xml(client):
    """Test case for import_from_xml

    Imports reports definition from XML.
    """
    body = /home-api/assets/examples/reports/importFromXML.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/reports/import/xml',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_set_preferred(client):
    """Test case for set_preferred

    Marks report as preferred or not.
    """
    body = openapi_server.PreferredRequestDTO()
    headers = { 
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/reports/{report_id}/preferred'.format(report_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

