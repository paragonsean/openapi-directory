# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.createnewdocument import Createnewdocument
from openapi_server.models.usingfilters import Usingfilters


pytestmark = pytest.mark.asyncio

async def test_createnewdocument(client):
    """Test case for createnewdocument

    Create new document
    """
    body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit..."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dataentities/{acronym}/documents'.format(acronym='{{acronym}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_createorupdateentiredocument(client):
    """Test case for createorupdateentiredocument

    Create or update entire document
    """
    body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit.... ","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","id":"4e4c55ac-e491-11e6-94f4-0ac138d2d42e"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{acronym}/documents'.format(acronym='{{acronym}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_createorupdatepartialdocument(client):
    """Test case for createorupdatepartialdocument

    Create or update partial document
    """
    body = {"Boolean":true,"id":"4e4c55ac-e491-11e6-94f4-0ac138d2d42e"}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dataentities/{acronym}/documents'.format(acronym='{{acronym}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deletedocument(client):
    """Test case for deletedocument

    Delete document
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/dataentities/{acronym}/documents/{id}'.format(acronym='{{acronym}}', id='{{id}}'),
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
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{acronym}/documents/{id}'.format(acronym='{{acronym}}', id='{{id}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updateentiredocument(client):
    """Test case for updateentiredocument

    Update entire document
    """
    body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit..."}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/dataentities/{acronym}/documents/{id}'.format(acronym='{{acronym}}', id='{{id}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updatepartialdocument(client):
    """Test case for updatepartialdocument

    Update partial document
    """
    body = {"Boolean":false}
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/dataentities/{acronym}/documents/{id}'.format(acronym='{{acronym}}', id='{{id}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

