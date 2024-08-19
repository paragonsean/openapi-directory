# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.object import Object


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_by_object_name(client):
    """Test case for create_by_object_name

    Create an {objectName}
    """
    body = openapi_server.Object()
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/elements/api-v2/{object_name}'.format(object_name='object_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_object_name_by_child_object_name(client):
    """Test case for create_object_name_by_child_object_name

    Create an {objectName}
    """
    body = openapi_server.Object()
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/elements/api-v2/{object_name}/{object_id}/{child_object_name}'.format(object_name='object_name_example', object_id='object_id_example', child_object_name='child_object_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_object_name_by_child_object_id(client):
    """Test case for delete_object_name_by_child_object_id

    Delete an {childObjectName}
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/elements/api-v2/{object_name}/{object_id}/{child_object_name}/{child_object_id}'.format(object_name='object_name_example', child_object_name='child_object_name_example', object_id='object_id_example', child_object_id='child_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_object_name_by_object_id(client):
    """Test case for delete_object_name_by_object_id

    Delete an {objectName}
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/elements/api-v2/{object_name}/{object_id}'.format(object_name='object_name_example', object_id='object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_object_name(client):
    """Test case for get_by_object_name

    Search for {objectName}
    """
    params = [('where', 'where_example'),
                    ('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/{object_name}'.format(object_name='object_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_name_by_child_object_id(client):
    """Test case for get_object_name_by_child_object_id

    Retrieve an {childObjectName}
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/{object_name}/{object_id}/{child_object_name}/{child_object_id}'.format(object_name='object_name_example', child_object_name='child_object_name_example', object_id='object_id_example', child_object_id='child_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_name_by_child_object_name(client):
    """Test case for get_object_name_by_child_object_name

    Search for {childObjectName}
    """
    params = [('where', 'where_example'),
                    ('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/{object_name}/{object_id}/{child_object_name}'.format(object_name='object_name_example', object_id='object_id_example', child_object_name='child_object_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_name_by_object_id(client):
    """Test case for get_object_name_by_object_id

    Retrieve an {objectName}
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/{object_name}/{object_id}'.format(object_name='object_name_example', object_id='object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_replace_object_name_by_child_object_id(client):
    """Test case for replace_object_name_by_child_object_id

    Update an {childObjectName}
    """
    body = openapi_server.Object()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/elements/api-v2/{object_name}/{object_id}/{child_object_name}/{child_object_id}'.format(object_name='object_name_example', child_object_name='child_object_name_example', object_id='object_id_example', child_object_id='child_object_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_replace_object_name_by_object_id(client):
    """Test case for replace_object_name_by_object_id

    Update an {objectName}
    """
    body = openapi_server.Object()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/elements/api-v2/{object_name}/{object_id}'.format(object_name='object_name_example', object_id='object_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_object_name_by_child_object_id(client):
    """Test case for update_object_name_by_child_object_id

    Update an {childObjectName}
    """
    body = openapi_server.Object()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/elements/api-v2/{object_name}/{object_id}/{child_object_name}/{child_object_id}'.format(object_name='object_name_example', child_object_name='child_object_name_example', object_id='object_id_example', child_object_id='child_object_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_object_name_by_object_id(client):
    """Test case for update_object_name_by_object_id

    Update an {objectName}
    """
    body = openapi_server.Object()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/elements/api-v2/{object_name}/{object_id}'.format(object_name='object_name_example', object_id='object_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

