# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.organization_details_output_model import OrganizationDetailsOutputModel
from openapi_server.models.patch_operation import PatchOperation


pytestmark = pytest.mark.asyncio

async def test_organization_details_patch_organization_details(client):
    """Test case for organization_details_patch_organization_details

    Update (Patch) a organization details or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/organizationdetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

