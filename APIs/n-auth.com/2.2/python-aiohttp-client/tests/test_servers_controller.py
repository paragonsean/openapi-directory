# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server import Server
from openapi_server.models.servers import Servers


pytestmark = pytest.mark.asyncio

async def test_create_server(client):
    """Test case for create_server

    Create a new server
    """
    create_server_body = {"owner":1,"serverFlags":["serverFlags","serverFlags"],"lastLogin":6,"pinTransTimeout":5,"accountCount":0,"siteurl":"siteurl","pingTime":2,"appios":"appios","serverName":"serverName","appurl":"appurl","serverid":"serverid","serverpk":"serverpk","pinTimeout":5,"wsurl":"wsurl","appname":"appname","logo":"logo","appandroid":"appandroid"}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/',
        headers=headers,
        json=create_server_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_server_attribute(client):
    """Test case for delete_server_attribute

    Delete specific attribute of a specific server
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/attributes/{attributekey}'.format(serverid='serverid_example', attributekey='attributekey_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_server_attributes(client):
    """Test case for delete_server_attributes

    Delete all attributes of a specific server
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/attributes'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server(client):
    """Test case for get_server

    Configuration of a specific server
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_attributes(client):
    """Test case for get_server_attributes

    Get all attributes of a specific server
    """
    headers = { 
        'Accept': 'text/plain',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/attributes'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_servers(client):
    """Test case for get_servers

    List all your servers
    """
    params = [('limit', 56),
                    ('marker', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_set_server_attributes(client):
    """Test case for set_server_attributes

    Set all attributes of a specific server
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/attributes'.format(serverid='serverid_example'),
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_server(client):
    """Test case for update_server

    Update configuration of a specific server
    """
    server = {"owner":1,"serverFlags":["serverFlags","serverFlags"],"lastLogin":6,"pinTransTimeout":5,"accountCount":0,"siteurl":"siteurl","pingTime":2,"appios":"appios","serverName":"serverName","appurl":"appurl","serverid":"serverid","serverpk":"serverpk","pinTimeout":5,"wsurl":"wsurl","appname":"appname","logo":"logo","appandroid":"appandroid"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}'.format(serverid='serverid_example'),
        headers=headers,
        json=server,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_server_attributes(client):
    """Test case for update_server_attributes

    Update specified attributes of a specific server
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}/attributes'.format(serverid='serverid_example'),
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

