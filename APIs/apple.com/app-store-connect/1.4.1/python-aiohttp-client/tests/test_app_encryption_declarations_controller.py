# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_encryption_declaration_builds_linkages_request import AppEncryptionDeclarationBuildsLinkagesRequest
from openapi_server.models.app_encryption_declaration_response import AppEncryptionDeclarationResponse
from openapi_server.models.app_encryption_declarations_response import AppEncryptionDeclarationsResponse
from openapi_server.models.app_response import AppResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_encryption_declarations_app_get_to_one_related(client):
    """Test case for app_encryption_declarations_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appEncryptionDeclarations/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_encryption_declarations_builds_create_to_many_relationship(client):
    """Test case for app_encryption_declarations_builds_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"builds"},{"id":"id","type":"builds"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appEncryptionDeclarations/{id}/relationships/builds'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_encryption_declarations_get_collection(client):
    """Test case for app_encryption_declarations_get_collection

    
    """
    params = [('filter[platform]', ['filter_platform_example']),
                    ('filter[app]', ['filter_app_example']),
                    ('filter[builds]', ['filter_builds_example']),
                    ('fields[appEncryptionDeclarations]', ['fields_app_encryption_declarations_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appEncryptionDeclarations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_encryption_declarations_get_instance(client):
    """Test case for app_encryption_declarations_get_instance

    
    """
    params = [('fields[appEncryptionDeclarations]', ['fields_app_encryption_declarations_example']),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appEncryptionDeclarations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

