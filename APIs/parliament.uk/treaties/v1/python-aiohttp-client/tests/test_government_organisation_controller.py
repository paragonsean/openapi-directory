# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.government_organisation_resource_collection import GovernmentOrganisationResourceCollection


pytestmark = pytest.mark.asyncio

async def test_get_organisations(client):
    """Test case for get_organisations

    Returns all government organisations.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/GovernmentOrganisation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

