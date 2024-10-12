# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_export201_response import CreateOrganizationExport201Response
from openapi_server.models.create_organization_export_request import CreateOrganizationExportRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_create_organization_export(client):
    """Test case for create_organization_export

    Create an organization export request
    """
    body = openapi_server.CreateOrganizationExportRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/organization_exports',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_export(client):
    """Test case for get_organization_export

    Get details on an org export request
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/organization_exports/{organization_export_gid}'.format(organization_export_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

