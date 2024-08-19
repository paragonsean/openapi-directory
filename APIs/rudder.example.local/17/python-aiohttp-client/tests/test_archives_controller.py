# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.import200_response import Import200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_call_import(client):
    """Test case for call_import

    Import a ZIP archive of policies into Rudder
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'API-Tokens': 'special-key',
    }
    data = FormData()
    data.add_field('archive', '/path/to/file')
    data.add_field('merge', 'merge_example')
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/archives/import',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export(client):
    """Test case for export

    Get a ZIP archive of the requested items and their dependencies
    """
    params = [('rules', ['[\"a0573b59-e5bd-441b-9031-f307aa21a61e\",\"4cba6eee-3a43-4e17-a608-a4941b6d984f%2B35177d0823791a374de9e16a6ab27e6466fbc8c2\"]']),
                    ('directives', ['[\"a0573b59-e5bd-441b-9031-f307aa21a61e\",\"4cba6eee-3a43-4e17-a608-a4941b6d984f%2B35177d0823791a374de9e16a6ab27e6466fbc8c2\"]']),
                    ('techniques', ['[\"userManagement/6.3\",\"fileContent/3.0%2B35177d0823791a374de9e16a6ab27e6466fbc8c2\"]']),
                    ('groups', ['[\"a0573b59-e5bd-441b-9031-f307aa21a61e\",\"4cba6eee-3a43-4e17-a608-a4941b6d984f%2B35177d0823791a374de9e16a6ab27e6466fbc8c2\"]']),
                    ('include', ['[\"directives\",\"groups\"]'])]
    headers = { 
        'Accept': 'application/octet-stream',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/archives/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

