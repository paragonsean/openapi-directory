# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_connection_manager(client):
    """Test case for get_connection_manager

    Gets Dlna media receiver registrar xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/ConnectionManager'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connection_manager2(client):
    """Test case for get_connection_manager2

    Gets Dlna media receiver registrar xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/ConnectionManager/ConnectionManager'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connection_manager3(client):
    """Test case for get_connection_manager3

    Gets Dlna media receiver registrar xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/ConnectionManager/ConnectionManager.xml'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_content_directory(client):
    """Test case for get_content_directory

    Gets Dlna content directory xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/ContentDirectory'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_content_directory2(client):
    """Test case for get_content_directory2

    Gets Dlna content directory xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/ContentDirectory/ContentDirectory'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_content_directory3(client):
    """Test case for get_content_directory3

    Gets Dlna content directory xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/ContentDirectory/ContentDirectory.xml'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_description_xml(client):
    """Test case for get_description_xml

    Get Description Xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/description'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_description_xml2(client):
    """Test case for get_description_xml2

    Get Description Xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/description.xml'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_icon(client):
    """Test case for get_icon

    Gets a server icon.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/icons/{file_name}'.format(file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_icon_id(client):
    """Test case for get_icon_id

    Gets a server icon.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/icons/{file_name}'.format(server_id='server_id_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_receiver_registrar(client):
    """Test case for get_media_receiver_registrar

    Gets Dlna media receiver registrar xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/MediaReceiverRegistrar'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_receiver_registrar2(client):
    """Test case for get_media_receiver_registrar2

    Gets Dlna media receiver registrar xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/MediaReceiverRegistrar/MediaReceiverRegistrar'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_receiver_registrar3(client):
    """Test case for get_media_receiver_registrar3

    Gets Dlna media receiver registrar xml.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='GET',
        path='/Dlna/{server_id}/MediaReceiverRegistrar/MediaReceiverRegistrar.xml'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_process_connection_manager_control_request(client):
    """Test case for process_connection_manager_control_request

    Process a connection manager control request.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='POST',
        path='/Dlna/{server_id}/ConnectionManager/Control'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_process_content_directory_control_request(client):
    """Test case for process_content_directory_control_request

    Process a content directory control request.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='POST',
        path='/Dlna/{server_id}/ContentDirectory/Control'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_process_media_receiver_registrar_control_request(client):
    """Test case for process_media_receiver_registrar_control_request

    Process a media receiver registrar control request.
    """
    headers = { 
        'Accept': 'text/xml',
    }
    response = await client.request(
        method='POST',
        path='/Dlna/{server_id}/MediaReceiverRegistrar/Control'.format(server_id='server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

