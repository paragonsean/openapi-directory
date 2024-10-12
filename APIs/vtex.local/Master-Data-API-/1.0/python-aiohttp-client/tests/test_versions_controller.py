# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_response import DocumentResponse
from openapi_server.models.getversion import Getversion
from openapi_server.models.listversion import Listversion


pytestmark = pytest.mark.asyncio

async def test_getversion(client):
    """Test case for getversion

    Get version
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
        path='/api/dataentities/{data_entity_name}/documents/{id}/versions/{version_id}'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e', version_id='123456789abc'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listversions(client):
    """Test case for listversions

    List versions
    """
    params = [('load', True),
                    ('fields', 'id,dataEntityId,isNewsletterOptIn,createdBy')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{data_entity_name}/documents/{id}/versions'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_putversion(client):
    """Test case for putversion

    Put version
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{data_entity_name}/documents/{id}/versions/{version_id}'.format(data_entity_name='Client', id='Client-b818cbda-e489-11e6-94f4-0ac138d2d42e', version_id='{{versionId}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

