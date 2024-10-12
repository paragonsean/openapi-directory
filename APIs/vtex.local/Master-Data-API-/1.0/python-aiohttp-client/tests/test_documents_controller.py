# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_response import DocumentResponse
from openapi_server.models.using_fields_all import UsingFieldsAll


pytestmark = pytest.mark.asyncio

async def test_createnewdocument(client):
    """Test case for createnewdocument

    Create new document
    """
    body = {'key': 'body_example'}
    params = [('_schema', 'schema')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dataentities/{data_entity_name}/documents'.format(data_entity_name='Client'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_createorupdatepartialdocument(client):
    """Test case for createorupdatepartialdocument

    Create partial document
    """
    body = {'key': 'body_example'}
    params = [('_schema', 'schema')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dataentities/{data_entity_name}/documents'.format(data_entity_name='Client'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deletedocument(client):
    """Test case for deletedocument

    Delete document
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dataentities/{data_entity_name}/documents/{id}'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getdocument(client):
    """Test case for getdocument

    Get document
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{data_entity_name}/documents/{id}'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updateentiredocument(client):
    """Test case for updateentiredocument

    Update entire document
    """
    body = {'key': 'body_example'}
    params = [('_where', 'firstName is not null.'),
                    ('_schema', 'schema')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{data_entity_name}/documents/{id}'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updatepartialdocument(client):
    """Test case for updatepartialdocument

    Update partial document
    """
    body = {'key': 'body_example'}
    params = [('_where', 'firstName is not null.'),
                    ('_schema', 'schema')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dataentities/{data_entity_name}/documents/{id}'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

