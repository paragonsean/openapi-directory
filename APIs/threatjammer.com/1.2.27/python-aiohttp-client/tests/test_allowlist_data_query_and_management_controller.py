# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.acl_list_collection_output import AclListCollectionOutput
from openapi_server.models.address import Address
from openapi_server.models.body_change_status_of_the_allowlist_v1_allowlist_public_allowlist_id_put import BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut
from openapi_server.models.body_change_status_of_the_origin_allowlist_v1_allowlist_private_allowlist_id_origin_put import BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut
from openapi_server.models.body_change_status_of_the_origin_allowlist_v1_allowlist_public_allowlist_id_origin_put import BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut
from openapi_server.models.body_create_private_allowlist_of_the_user_v1_allowlist_private_post import BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost
from openapi_server.models.body_update_private_allowlist_of_the_user_v1_allowlist_private_allowlist_id_put import BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut
from openapi_server.models.body_update_private_content_of_the_allowlist_of_the_user_v1_allowlist_private_allowlist_id_content_put import BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.private_acl_group_list_collection_output import PrivateAclGroupListCollectionOutput
from openapi_server.models.private_acl_group_list_output import PrivateAclGroupListOutput
from openapi_server.models.private_acl_list_collection_output import PrivateAclListCollectionOutput
from openapi_server.models.public_acl_group_list_collection_output import PublicAclGroupListCollectionOutput
from openapi_server.models.public_acl_group_list_output import PublicAclGroupListOutput


pytestmark = pytest.mark.asyncio

async def test_change_status_of_the_allowlist_v1_allowlist_public_allowlist_id_put(client):
    """Test case for change_status_of_the_allowlist_v1_allowlist_public_allowlist_id_put

    Toogle the status of an allow list.
    """
    body = openapi_server.BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/allowlist/public/{allowlist_id}'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status_of_the_origin_allowlist_v1_allowlist_private_allowlist_id_origin_put(client):
    """Test case for change_status_of_the_origin_allowlist_v1_allowlist_private_allowlist_id_origin_put

    Toogle the status of the origin in an allow list.
    """
    body = openapi_server.BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/allowlist/private/{allowlist_id}/origin'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status_of_the_origin_allowlist_v1_allowlist_public_allowlist_id_origin_put(client):
    """Test case for change_status_of_the_origin_allowlist_v1_allowlist_public_allowlist_id_origin_put

    Toogle the status of the origin in an allow list.
    """
    body = openapi_server.BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/allowlist/public/{allowlist_id}/origin'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_private_allowlist_of_the_user_v1_allowlist_private_post(client):
    """Test case for create_private_allowlist_of_the_user_v1_allowlist_private_post

    Creates a new private allowlist binded to the user.
    """
    body = openapi_server.BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/allowlist/private',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_the_allowlist_content_v1_allowlist_private_allowlist_id_content_delete(client):
    """Test case for delete_the_allowlist_content_v1_allowlist_private_allowlist_id_content_delete

    Delete all the content of a private allowlist of the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/allowlist/private/{allowlist_id}/content'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_the_allowlist_v1_allowlist_private_allowlist_id_delete(client):
    """Test case for delete_the_allowlist_v1_allowlist_private_allowlist_id_delete

    Delete all the bindings between a user and a private allowlist.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/allowlist/private/{allowlist_id}'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_the_allowlist_v1_allowlist_public_allowlist_id_delete(client):
    """Test case for delete_the_allowlist_v1_allowlist_public_allowlist_id_delete

    Delete all the bindings between a user and an allowlist.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/allowlist/public/{allowlist_id}'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_owned_allowlists_by_resource_type_v1_allowlist_public_owned_resource_type_get(client):
    """Test case for get_all_owned_allowlists_by_resource_type_v1_allowlist_public_owned_resource_type_get

    Get the set of public allowlists of a user by resource type.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/public/owned/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_private_allowlists_by_resource_type_v1_allowlist_private_all_resource_type_get(client):
    """Test case for get_all_private_allowlists_by_resource_type_v1_allowlist_private_all_resource_type_get

    Get the set of private allowlists of the user by resource type.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/private/all/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_private_allowlists_v1_allowlist_private_all_get(client):
    """Test case for get_all_private_allowlists_v1_allowlist_private_all_get

    Get the set of private allowlists of the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/private/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_public_allowlists_by_resource_type_v1_allowlist_public_all_resource_type_get(client):
    """Test case for get_all_public_allowlists_by_resource_type_v1_allowlist_public_all_resource_type_get

    Get the set of public allowlists by resource type.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/public/all/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_public_allowlists_v1_allowlist_public_all_get(client):
    """Test case for get_all_public_allowlists_v1_allowlist_public_all_get

    Get the set of public allowlists.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/public/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_allowlist_content_v1_allowlist_private_allowlist_id_content_get(client):
    """Test case for get_allowlist_content_v1_allowlist_private_allowlist_id_content_get

    Get the content of a private allowlist of the user.
    """
    params = [('page', 1),
                    ('page_size', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/private/{allowlist_id}/content'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_allowlists_owned_by_the_user_v1_allowlist_public_owned_get(client):
    """Test case for get_public_allowlists_owned_by_the_user_v1_allowlist_public_owned_get

    Get the set of owned allowlists.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/public/owned',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_allowlist_v1_allowlist_private_allowlist_id_get(client):
    """Test case for get_single_allowlist_v1_allowlist_private_allowlist_id_get

    Get the details of a specific private allowlist of the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/private/{allowlist_id}'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_allowlist_v1_allowlist_public_allowlist_id_get(client):
    """Test case for get_single_allowlist_v1_allowlist_public_allowlist_id_get

    Get the details of the allowlist.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/public/{allowlist_id}'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_resource_allowlists_v1_allowlist_public_ip_address_get(client):
    """Test case for query_resource_allowlists_v1_allowlist_public_ip_address_get

    Get the different public allowlists where the IP address was found.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/public/ip/{address}'.format(address=openapi_server.Address()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_resource_denylists_v1_allowlist_private_ip_address_get(client):
    """Test case for query_resource_denylists_v1_allowlist_private_ip_address_get

    Get the different private allowlists where the IP address was found.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/allowlist/private/ip/{address}'.format(address=openapi_server.Address()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_private_allowlist_of_the_user_v1_allowlist_private_allowlist_id_put(client):
    """Test case for update_private_allowlist_of_the_user_v1_allowlist_private_allowlist_id_put

    Update the information of an existing private allowlist of the user.
    """
    body = openapi_server.BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/allowlist/private/{allowlist_id}'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_private_content_of_the_allowlist_of_the_user_v1_allowlist_private_allowlist_id_content_put(client):
    """Test case for update_private_content_of_the_allowlist_of_the_user_v1_allowlist_private_allowlist_id_content_put

    Add or remove content of a private allowlist of the user.
    """
    body = openapi_server.BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/allowlist/private/{allowlist_id}/content'.format(allowlist_id='allowlist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

