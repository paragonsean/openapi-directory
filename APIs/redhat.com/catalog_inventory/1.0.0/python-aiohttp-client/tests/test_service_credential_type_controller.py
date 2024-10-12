# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.service_credential_type import ServiceCredentialType
from openapi_server.models.service_credential_types_collection import ServiceCredentialTypesCollection


pytestmark = pytest.mark.asyncio

async def test_list_service_credential_types(client):
    """Test case for list_service_credential_types

    List ServiceCredentialTypes
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_credential_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_service_credential_type(client):
    """Test case for show_service_credential_type

    Show an existing ServiceCredentialType
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_credential_types/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

