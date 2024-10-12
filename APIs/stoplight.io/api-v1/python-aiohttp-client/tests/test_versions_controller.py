# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_versions_version_id_export_format200_response import GETVersionsVersionIdExportFormat200Response
from openapi_server.models.post_versions_version_id_publish200_response import POSTVersionsVersionIdPublish200Response
from openapi_server.models.put_versions_version_id_import200_response import PUTVersionsVersionIdImport200Response
from openapi_server.models.put_versions_version_id_import_request import PUTVersionsVersionIdImportRequest
from openapi_server.models.put_versions_version_id_unpublish200_response import PUTVersionsVersionIdUnpublish200Response


pytestmark = pytest.mark.asyncio

async def test_g_et_versions_version_id_export_format(client):
    """Test case for g_et_versions_version_id_export_format

    Export
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/versions/{version_id}/export/{format}'.format(version_id='', format=oas.json),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_versions_version_id_publish(client):
    """Test case for p_ost_versions_version_id_publish

    Publish
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/versions/{version_id}/publish'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ut_versions_version_id_import(client):
    """Test case for p_ut_versions_version_id_import

    Import
    """
    body = openapi_server.PUTVersionsVersionIdImportRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/versions/{version_id}/import'.format(version_id='version_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ut_versions_version_id_unpublish(client):
    """Test case for p_ut_versions_version_id_unpublish

    Unpublish
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/versions/{version_id}/unpublish'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

