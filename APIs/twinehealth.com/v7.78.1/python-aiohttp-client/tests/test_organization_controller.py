# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_organization_response import FetchOrganizationResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_organization(client):
    """Test case for fetch_organization

    Get an organization
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/organization/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

