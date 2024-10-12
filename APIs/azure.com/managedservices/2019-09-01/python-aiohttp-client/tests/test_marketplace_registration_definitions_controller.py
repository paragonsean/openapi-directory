# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.marketplace_registration_definition_list import MarketplaceRegistrationDefinitionList
from openapi_server.models.registration_definition import RegistrationDefinition


pytestmark = pytest.mark.asyncio

async def test_marketplace_registration_definitions_get(client):
    """Test case for marketplace_registration_definitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedServices/marketplaceRegistrationDefinitions/{marketplace_identifier}'.format(scope='scope_example', marketplace_identifier='marketplace_identifier_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplace_registration_definitions_list(client):
    """Test case for marketplace_registration_definitions_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedServices/marketplaceRegistrationDefinitions'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

