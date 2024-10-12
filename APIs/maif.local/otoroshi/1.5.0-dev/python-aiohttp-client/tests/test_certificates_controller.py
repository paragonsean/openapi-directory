# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner


pytestmark = pytest.mark.asyncio

async def test_all_certs(client):
    """Test case for all_certs

    Get all certificates
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/certificates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_cert(client):
    """Test case for create_cert

    Create one certificate
    """
    body = {"valid":"a string value","privateKey":"a string value","chain":"a string value","caRef":"a string value","subject":"a string value","domain":"a string value","autoRenew":"a string value","from":"a string value","selfSigned":"a string value","id":"a string value","to":"a string value","ca":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/certificates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cert(client):
    """Test case for delete_cert

    Delete one certificate by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/certificates/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_one_cert(client):
    """Test case for one_cert

    Get one certificate by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/certificates/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_cert(client):
    """Test case for patch_cert

    Update one certificate by id
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/certificates/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_cert(client):
    """Test case for put_cert

    Update one certificate by id
    """
    body = {"valid":"a string value","privateKey":"a string value","chain":"a string value","caRef":"a string value","subject":"a string value","domain":"a string value","autoRenew":"a string value","from":"a string value","selfSigned":"a string value","id":"a string value","to":"a string value","ca":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/certificates/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

