# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.created_export import CreatedExport
from openapi_server.models.error import Error
from openapi_server.models.export import Export
from openapi_server.models.export_contents import ExportContents
from openapi_server.models.export_status import ExportStatus


pytestmark = pytest.mark.asyncio

async def test_fetch_export_contents_by_id(client):
    """Test case for fetch_export_contents_by_id

    Retrieve the binary contents of a processed export request.
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'range': 'range_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/exports/{export_id}/contents'.format(export_id='export_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_export_status_by_id(client):
    """Test case for fetch_export_status_by_id

    Retrieve the status of an Export.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/exports/{export_id}/status'.format(export_id='export_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_export(client):
    """Test case for post_export

    Initiate a new export request.
    """
    body = {"definition":"{}","contentType":"application/vnd.climate.acrsi.geojson"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/exports',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

