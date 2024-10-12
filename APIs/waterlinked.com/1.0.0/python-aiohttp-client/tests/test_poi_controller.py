# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_poi_payload import CreatePoiPayload
from openapi_server.models.error import Error
from openapi_server.models.update_poi_payload import UpdatePoiPayload
from openapi_server.models.waterlinked_poi import WaterlinkedPoi


pytestmark = pytest.mark.asyncio

async def test_poi_create(client):
    """Test case for poi_create

    Create poi
    """
    payload = {"depth":0.9848439086783396,"icon":"Ut molestias laboriosam.","id":3408207428662661600,"lat":0.8147274904139097,"lng":0.06472337355304676,"name":"Reprehenderit non architecto quia.","visible":False}
    headers = { 
        'Accept': 'application/vnd.goa.error',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/poi/',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_poi_delete(client):
    """Test case for poi_delete

    Delete poi
    """
    headers = { 
        'Accept': 'application/vnd.goa.error',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/poi/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_poi_list(client):
    """Test case for poi_list

    List poi
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.poi+json; type=collection',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/poi/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_poi_show(client):
    """Test case for poi_show

    Show poi
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.poi+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/poi/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_poi_update(client):
    """Test case for poi_update

    Update poi
    """
    payload = {"depth":0.9848439086783396,"icon":"Ut molestias laboriosam.","id":3408207428662661600,"lat":0.8147274904139097,"lng":0.06472337355304676,"name":"Reprehenderit non architecto quia.","visible":False}
    headers = { 
        'Accept': 'application/vnd.goa.error',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/poi/{id}'.format(id=56),
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

