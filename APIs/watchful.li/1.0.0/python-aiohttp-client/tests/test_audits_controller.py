# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit import Audit


pytestmark = pytest.mark.asyncio

async def test_delete_audit_by_id(client):
    """Test case for delete_audit_by_id

    Delete a specific audit
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/audits/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audit_by_id(client):
    """Test case for get_audit_by_id

    Find audit by ID
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/audits/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audits(client):
    """Test case for get_audits

    Get a list of audits
    """
    params = [('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/audits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fields_audits(client):
    """Test case for get_fields_audits

    Get the list of fields
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/audits/metadata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

