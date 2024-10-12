# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.box import Box
from openapi_server.models.bulk_anonymization_data import BulkAnonymizationData
from openapi_server.models.image import Image
from openapi_server.models.incoming_transaction import IncomingTransaction
from openapi_server.models.outgoing_transaction import OutgoingTransaction
from openapi_server.models.remote_box import RemoteBox
from openapi_server.models.remote_box_connection_data import RemoteBoxConnectionData


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_boxes_connect_post(client):
    """Test case for boxes_connect_post

    
    """
    remote_box = openapi_server.RemoteBox()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/boxes/connect',
        headers=headers,
        json=remote_box,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_boxes_createconnection_post(client):
    """Test case for boxes_createconnection_post

    
    """
    remote_box_connection_data = openapi_server.RemoteBoxConnectionData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/boxes/createconnection',
        headers=headers,
        json=remote_box_connection_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_get(client):
    """Test case for boxes_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/boxes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_id_delete(client):
    """Test case for boxes_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/boxes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_boxes_id_send_post(client):
    """Test case for boxes_id_send_post

    
    """
    sequence_of_image_tag_values = openapi_server.BulkAnonymizationData()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/boxes/{id}/send'.format(id=56),
        headers=headers,
        json=sequence_of_image_tag_values,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_incoming_get(client):
    """Test case for boxes_incoming_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/boxes/incoming',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_incoming_id_delete(client):
    """Test case for boxes_incoming_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/boxes/incoming/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_incoming_id_images_get(client):
    """Test case for boxes_incoming_id_images_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/boxes/incoming/{id}/images'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_outgoing_get(client):
    """Test case for boxes_outgoing_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/boxes/outgoing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_outgoing_id_delete(client):
    """Test case for boxes_outgoing_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/boxes/outgoing/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_boxes_outgoing_id_images_get(client):
    """Test case for boxes_outgoing_id_images_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/boxes/outgoing/{id}/images'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

