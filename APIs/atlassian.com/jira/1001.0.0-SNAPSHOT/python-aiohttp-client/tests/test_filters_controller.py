# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.change_filter_owner import ChangeFilterOwner
from openapi_server.models.column_item import ColumnItem
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.filter import Filter
from openapi_server.models.page_bean_filter_details import PageBeanFilterDetails


pytestmark = pytest.mark.asyncio

async def test_change_filter_owner(client):
    """Test case for change_filter_owner

    Change filter owner
    """
    body = {"accountId":"accountId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/filter/{id}/owner'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_filter(client):
    """Test case for create_filter

    Create filter
    """
    body = {"owner":"","sharedUsers":"","subscriptions":"","jql":"jql","favouritedCount":0,"description":"description","favourite":True,"editPermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}],"name":"name","viewUrl":"https://openapi-generator.tech","self":"https://openapi-generator.tech","searchUrl":"https://openapi-generator.tech","id":"id","sharePermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}]}
    params = [('expand', 'expand_example'),
                    ('overrideSharePermissions', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/filter',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_favourite_for_filter(client):
    """Test case for delete_favourite_for_filter

    Remove filter as favorite
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/filter/{id}/favourite'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_filter(client):
    """Test case for delete_filter

    Delete filter
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/filter/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_columns(client):
    """Test case for get_columns

    Get columns
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/{id}/columns'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_favourite_filters(client):
    """Test case for get_favourite_filters

    Get favorite filters
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/favourite',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filter(client):
    """Test case for get_filter

    Get filter
    """
    params = [('expand', 'expand_example'),
                    ('overrideSharePermissions', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filters_paginated(client):
    """Test case for get_filters_paginated

    Search for filters
    """
    params = [('filterName', 'filter_name_example'),
                    ('accountId', 'account_id_example'),
                    ('owner', 'owner_example'),
                    ('groupname', 'groupname_example'),
                    ('groupId', 'group_id_example'),
                    ('projectId', 56),
                    ('id', [56]),
                    ('orderBy', name),
                    ('startAt', 0),
                    ('maxResults', 50),
                    ('expand', 'expand_example'),
                    ('overrideSharePermissions', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_my_filters(client):
    """Test case for get_my_filters

    Get my filters
    """
    params = [('expand', 'expand_example'),
                    ('includeFavourites', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/my',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_columns(client):
    """Test case for reset_columns

    Reset columns
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/filter/{id}/columns'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_set_columns(client):
    """Test case for set_columns

    Set columns
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/filter/{id}/columns'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_favourite_for_filter(client):
    """Test case for set_favourite_for_filter

    Add filter as favorite
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/filter/{id}/favourite'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_filter(client):
    """Test case for update_filter

    Update filter
    """
    body = {"owner":"","sharedUsers":"","subscriptions":"","jql":"jql","favouritedCount":0,"description":"description","favourite":True,"editPermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}],"name":"name","viewUrl":"https://openapi-generator.tech","self":"https://openapi-generator.tech","searchUrl":"https://openapi-generator.tech","id":"id","sharePermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}]}
    params = [('expand', 'expand_example'),
                    ('overrideSharePermissions', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/filter/{id}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

