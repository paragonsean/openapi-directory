# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.object_permission import ObjectPermission
from openapi_server.models.token import Token
from openapi_server.models.user import User
from openapi_server.models.users_groups_list200_response import UsersGroupsList200Response
from openapi_server.models.users_permissions_list200_response import UsersPermissionsList200Response
from openapi_server.models.users_tokens_list200_response import UsersTokensList200Response
from openapi_server.models.users_users_list200_response import UsersUsersList200Response
from openapi_server.models.writable_object_permission import WritableObjectPermission
from openapi_server.models.writable_token import WritableToken
from openapi_server.models.writable_user import WritableUser


pytestmark = pytest.mark.asyncio

async def test_users_config_list(client):
    """Test case for users_config_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/config/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_bulk_delete(client):
    """Test case for users_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_bulk_partial_update(client):
    """Test case for users_groups_bulk_partial_update

    
    """
    body = {"user_count":1,"display":"display","name":"name","id":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_bulk_update(client):
    """Test case for users_groups_bulk_update

    
    """
    body = {"user_count":1,"display":"display","name":"name","id":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_create(client):
    """Test case for users_groups_create

    
    """
    body = {"user_count":1,"display":"display","name":"name","id":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_delete(client):
    """Test case for users_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_list(client):
    """Test case for users_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('q', 'q_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_partial_update(client):
    """Test case for users_groups_partial_update

    
    """
    body = {"user_count":1,"display":"display","name":"name","id":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_read(client):
    """Test case for users_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_groups_update(client):
    """Test case for users_groups_update

    
    """
    body = {"user_count":1,"display":"display","name":"name","id":6,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_bulk_delete(client):
    """Test case for users_permissions_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/permissions/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_bulk_partial_update(client):
    """Test case for users_permissions_bulk_partial_update

    
    """
    body = {"object_types":["object_types","object_types"],"display":"display","name":"name","description":"description","groups":[0,0],"id":6,"actions":["actions","actions"],"constraints":"{}","enabled":True,"url":"https://openapi-generator.tech","users":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/permissions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_bulk_update(client):
    """Test case for users_permissions_bulk_update

    
    """
    body = {"object_types":["object_types","object_types"],"display":"display","name":"name","description":"description","groups":[0,0],"id":6,"actions":["actions","actions"],"constraints":"{}","enabled":True,"url":"https://openapi-generator.tech","users":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/permissions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_create(client):
    """Test case for users_permissions_create

    
    """
    body = {"object_types":["object_types","object_types"],"display":"display","name":"name","description":"description","groups":[0,0],"id":6,"actions":["actions","actions"],"constraints":"{}","enabled":True,"url":"https://openapi-generator.tech","users":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/permissions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_delete(client):
    """Test case for users_permissions_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/permissions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_list(client):
    """Test case for users_permissions_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('enabled', 'enabled_example'),
                    ('object_types', 'object_types_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('user_id', 'user_id_example'),
                    ('user', 'user_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('object_types__n', 'object_types__n_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('user_id__n', 'user_id__n_example'),
                    ('user__n', 'user__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/permissions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_partial_update(client):
    """Test case for users_permissions_partial_update

    
    """
    body = {"object_types":["object_types","object_types"],"display":"display","name":"name","description":"description","groups":[0,0],"id":6,"actions":["actions","actions"],"constraints":"{}","enabled":True,"url":"https://openapi-generator.tech","users":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/permissions/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_read(client):
    """Test case for users_permissions_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/permissions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_permissions_update(client):
    """Test case for users_permissions_update

    
    """
    body = {"object_types":["object_types","object_types"],"display":"display","name":"name","description":"description","groups":[0,0],"id":6,"actions":["actions","actions"],"constraints":"{}","enabled":True,"url":"https://openapi-generator.tech","users":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/permissions/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_bulk_delete(client):
    """Test case for users_tokens_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/tokens/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_bulk_partial_update(client):
    """Test case for users_tokens_bulk_partial_update

    
    """
    body = {"expires":"2000-01-23T04:56:07.000+00:00","allowed_ips":[{},{}],"created":"2000-01-23T04:56:07.000+00:00","write_enabled":True,"display":"display","last_used":"2000-01-23T04:56:07.000+00:00","description":"description","id":0,"user":6,"key":"key","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/tokens/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_bulk_update(client):
    """Test case for users_tokens_bulk_update

    
    """
    body = {"expires":"2000-01-23T04:56:07.000+00:00","allowed_ips":[{},{}],"created":"2000-01-23T04:56:07.000+00:00","write_enabled":True,"display":"display","last_used":"2000-01-23T04:56:07.000+00:00","description":"description","id":0,"user":6,"key":"key","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/tokens/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_create(client):
    """Test case for users_tokens_create

    
    """
    body = {"expires":"2000-01-23T04:56:07.000+00:00","allowed_ips":[{},{}],"created":"2000-01-23T04:56:07.000+00:00","write_enabled":True,"display":"display","last_used":"2000-01-23T04:56:07.000+00:00","description":"description","id":0,"user":6,"key":"key","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/tokens/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_delete(client):
    """Test case for users_tokens_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/tokens/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_list(client):
    """Test case for users_tokens_list

    
    """
    params = [('id', 'id_example'),
                    ('key', 'key_example'),
                    ('write_enabled', 'write_enabled_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('user_id', 'user_id_example'),
                    ('user', 'user_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('expires', 'expires_example'),
                    ('expires__gte', 'expires__gte_example'),
                    ('expires__lte', 'expires__lte_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('key__n', 'key__n_example'),
                    ('key__ic', 'key__ic_example'),
                    ('key__nic', 'key__nic_example'),
                    ('key__iew', 'key__iew_example'),
                    ('key__niew', 'key__niew_example'),
                    ('key__isw', 'key__isw_example'),
                    ('key__nisw', 'key__nisw_example'),
                    ('key__ie', 'key__ie_example'),
                    ('key__nie', 'key__nie_example'),
                    ('key__empty', 'key__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('user_id__n', 'user_id__n_example'),
                    ('user__n', 'user__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/tokens/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_partial_update(client):
    """Test case for users_tokens_partial_update

    
    """
    body = {"expires":"2000-01-23T04:56:07.000+00:00","allowed_ips":[{},{}],"created":"2000-01-23T04:56:07.000+00:00","write_enabled":True,"display":"display","last_used":"2000-01-23T04:56:07.000+00:00","description":"description","id":0,"user":6,"key":"key","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/tokens/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_provision_create(client):
    """Test case for users_tokens_provision_create

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/tokens/provision/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_read(client):
    """Test case for users_tokens_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/tokens/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_tokens_update(client):
    """Test case for users_tokens_update

    
    """
    body = {"expires":"2000-01-23T04:56:07.000+00:00","allowed_ips":[{},{}],"created":"2000-01-23T04:56:07.000+00:00","write_enabled":True,"display":"display","last_used":"2000-01-23T04:56:07.000+00:00","description":"description","id":0,"user":6,"key":"key","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/tokens/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_bulk_delete(client):
    """Test case for users_users_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/users/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_bulk_partial_update(client):
    """Test case for users_users_bulk_partial_update

    
    """
    body = {"password":"password","is_active":True,"is_staff":True,"display":"display","groups":[0,0],"last_name":"last_name","date_joined":"2000-01-23T04:56:07.000+00:00","id":6,"first_name":"first_name","email":"email","url":"https://openapi-generator.tech","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_bulk_update(client):
    """Test case for users_users_bulk_update

    
    """
    body = {"password":"password","is_active":True,"is_staff":True,"display":"display","groups":[0,0],"last_name":"last_name","date_joined":"2000-01-23T04:56:07.000+00:00","id":6,"first_name":"first_name","email":"email","url":"https://openapi-generator.tech","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_create(client):
    """Test case for users_users_create

    
    """
    body = {"password":"password","is_active":True,"is_staff":True,"display":"display","groups":[0,0],"last_name":"last_name","date_joined":"2000-01-23T04:56:07.000+00:00","id":6,"first_name":"first_name","email":"email","url":"https://openapi-generator.tech","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users/users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_delete(client):
    """Test case for users_users_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_list(client):
    """Test case for users_users_list

    
    """
    params = [('id', 'id_example'),
                    ('username', 'username_example'),
                    ('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('email', 'email_example'),
                    ('is_staff', 'is_staff_example'),
                    ('is_active', 'is_active_example'),
                    ('q', 'q_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('username__n', 'username__n_example'),
                    ('username__ic', 'username__ic_example'),
                    ('username__nic', 'username__nic_example'),
                    ('username__iew', 'username__iew_example'),
                    ('username__niew', 'username__niew_example'),
                    ('username__isw', 'username__isw_example'),
                    ('username__nisw', 'username__nisw_example'),
                    ('username__ie', 'username__ie_example'),
                    ('username__nie', 'username__nie_example'),
                    ('username__empty', 'username__empty_example'),
                    ('first_name__n', 'first_name__n_example'),
                    ('first_name__ic', 'first_name__ic_example'),
                    ('first_name__nic', 'first_name__nic_example'),
                    ('first_name__iew', 'first_name__iew_example'),
                    ('first_name__niew', 'first_name__niew_example'),
                    ('first_name__isw', 'first_name__isw_example'),
                    ('first_name__nisw', 'first_name__nisw_example'),
                    ('first_name__ie', 'first_name__ie_example'),
                    ('first_name__nie', 'first_name__nie_example'),
                    ('first_name__empty', 'first_name__empty_example'),
                    ('last_name__n', 'last_name__n_example'),
                    ('last_name__ic', 'last_name__ic_example'),
                    ('last_name__nic', 'last_name__nic_example'),
                    ('last_name__iew', 'last_name__iew_example'),
                    ('last_name__niew', 'last_name__niew_example'),
                    ('last_name__isw', 'last_name__isw_example'),
                    ('last_name__nisw', 'last_name__nisw_example'),
                    ('last_name__ie', 'last_name__ie_example'),
                    ('last_name__nie', 'last_name__nie_example'),
                    ('last_name__empty', 'last_name__empty_example'),
                    ('email__n', 'email__n_example'),
                    ('email__ic', 'email__ic_example'),
                    ('email__nic', 'email__nic_example'),
                    ('email__iew', 'email__iew_example'),
                    ('email__niew', 'email__niew_example'),
                    ('email__isw', 'email__isw_example'),
                    ('email__nisw', 'email__nisw_example'),
                    ('email__ie', 'email__ie_example'),
                    ('email__nie', 'email__nie_example'),
                    ('email__empty', 'email__empty_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_partial_update(client):
    """Test case for users_users_partial_update

    
    """
    body = {"password":"password","is_active":True,"is_staff":True,"display":"display","groups":[0,0],"last_name":"last_name","date_joined":"2000-01-23T04:56:07.000+00:00","id":6,"first_name":"first_name","email":"email","url":"https://openapi-generator.tech","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/users/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_read(client):
    """Test case for users_users_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_users_update(client):
    """Test case for users_users_update

    
    """
    body = {"password":"password","is_active":True,"is_staff":True,"display":"display","groups":[0,0],"last_name":"last_name","date_joined":"2000-01-23T04:56:07.000+00:00","id":6,"first_name":"first_name","email":"email","url":"https://openapi-generator.tech","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

