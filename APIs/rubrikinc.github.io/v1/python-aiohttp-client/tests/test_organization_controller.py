# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.envoy_bulk_update import EnvoyBulkUpdate
from openapi_server.models.envoy_create import EnvoyCreate
from openapi_server.models.envoy_detail_list import EnvoyDetailList
from openapi_server.models.envoy_id_list import EnvoyIdList


pytestmark = pytest.mark.asyncio

async def test_bulk_create_envoys(client):
    """Test case for bulk_create_envoys

    Create a list of Rubrik Envoy objects
    """
    body = {"port":0,"ipAddress":"ipAddress"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organization/{id}/envoy/bulk'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_envoys(client):
    """Test case for bulk_delete_envoys

    Remove a list of Rubrik Envoy objects
    """
    body = {"envoyIds":["envoyIds","envoyIds"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organization/{id}/envoy/bulk'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_envoys(client):
    """Test case for bulk_update_envoys

    Update a list of Rubrik Envoy objects
    """
    body = {"updateProperties":{"port":0,"ipAddress":"ipAddress"},"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/organization/{id}/envoy/bulk'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

