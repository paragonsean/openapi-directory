# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.entity_with_name_dto import EntityWithNameDTO
from openapi_server.models.time_zone_dto import TimeZoneDTO
from openapi_server.models.user_dto import UserDTO


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_change_password(client):
    """Test case for change_password

    Sets user's password to a new value.
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    data = {
        'new_password': 'new_password_example',
        'old_password': 'old_password_example'
        }
    response = await client.request(
        method='PUT',
        path='/home-api/users/{user_id}/password'.format(user_id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_names_with_ids1(client):
    """Test case for get_all_names_with_ids1

    Returns list of simple users representations
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id6(client):
    """Test case for get_by_id6

    Returns user details.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/users/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_field1(client):
    """Test case for get_custom_field1

    Returns custom field of a given user.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/users/{user_id}/customFields/{custom_field_key}'.format(user_id=56, custom_field_key='custom_field_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields4(client):
    """Test case for get_custom_fields4

    Returns custom fields of a given user.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/users/{user_id}/customFields'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_me(client):
    """Test case for get_me

    Returns currently signed in user details.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/users/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_time_zone(client):
    """Test case for get_time_zone

    Returns time zone preferred by user currently signed in.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/users/me/timeZone',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update3(client):
    """Test case for update3

    Updates an existing user.
    """
    body = {"positionName":"positionName","firstName":"firstName","lastName":"lastName","gender":"gender","mobilePhone":"mobilePhone","phone":"phone","customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"timeZoneId":"timeZoneId","userGroupName":"userGroupName","id":0,"login":"login","email":"email"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/users/{user_id}'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field1(client):
    """Test case for update_custom_field1

    Updates given custom field of a given user.
    """
    body = {"name":"name","type":"TEXT","value":"{}","key":"key"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/users/{user_id}/customFields/{custom_field_key}'.format(user_id=56, custom_field_key='custom_field_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_fields2(client):
    """Test case for update_custom_fields2

    Updates custom fields of a given user.
    """
    body = {"name":"name","type":"TEXT","value":"{}","key":"key"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/users/{user_id}/customFields'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

