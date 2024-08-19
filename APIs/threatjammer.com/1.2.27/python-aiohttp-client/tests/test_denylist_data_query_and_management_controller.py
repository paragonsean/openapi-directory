# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.acl_list_collection_output import AclListCollectionOutput
from openapi_server.models.address import Address
from openapi_server.models.body_change_status_of_the_denylist_v1_denylist_public_denylist_id_put import BodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut
from openapi_server.models.body_change_status_of_the_origin_denylist_v1_denylist_private_denylist_id_origin_put import BodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut
from openapi_server.models.body_change_status_of_the_origin_denylist_v1_denylist_public_denylist_id_origin_put import BodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut
from openapi_server.models.body_create_private_denylist_of_the_user_v1_denylist_private_post import BodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost
from openapi_server.models.body_update_private_content_of_the_denylist_of_the_user_v1_denylist_private_denylist_id_content_put import BodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut
from openapi_server.models.body_update_private_denylist_of_the_user_v1_denylist_private_denylist_id_put import BodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.ip_list_collection_output import IPListCollectionOutput
from openapi_server.models.ip_list_output import IPListOutput
from openapi_server.models.private_acl_group_list_collection_output import PrivateAclGroupListCollectionOutput
from openapi_server.models.private_acl_group_list_output import PrivateAclGroupListOutput
from openapi_server.models.private_acl_list_collection_output import PrivateAclListCollectionOutput
from openapi_server.models.public_acl_group_list_collection_output import PublicAclGroupListCollectionOutput
from openapi_server.models.public_acl_group_list_output import PublicAclGroupListOutput


pytestmark = pytest.mark.asyncio

async def test_change_status_of_the_denylist_v1_denylist_public_denylist_id_put(client):
    """Test case for change_status_of_the_denylist_v1_denylist_public_denylist_id_put

    Toogle the status of an deny list.
    """
    body = openapi_server.BodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/denylist/public/{denylist_id}'.format(denylist_id='denylist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status_of_the_origin_denylist_v1_denylist_private_denylist_id_origin_put(client):
    """Test case for change_status_of_the_origin_denylist_v1_denylist_private_denylist_id_origin_put

    Toogle the status of the origin in a deny list.
    """
    body = openapi_server.BodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/denylist/private/{denylist_id}/origin'.format(denylist_id='denylist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status_of_the_origin_denylist_v1_denylist_public_denylist_id_origin_put(client):
    """Test case for change_status_of_the_origin_denylist_v1_denylist_public_denylist_id_origin_put

    Toogle the status of the origin in a deny list.
    """
    body = openapi_server.BodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/denylist/public/{denylist_id}/origin'.format(denylist_id='denylist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_private_denylist_of_the_user_v1_denylist_private_post(client):
    """Test case for create_private_denylist_of_the_user_v1_denylist_private_post

    Creates a new private denylist binded to the user.
    """
    body = openapi_server.BodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/denylist/private',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_all_ip_addresses_reported_by_the_user_v1_denylist_reported_ip_all_delete(client):
    """Test case for delete_all_ip_addresses_reported_by_the_user_v1_denylist_reported_ip_all_delete

    Delete all the automatically reported IP addresses by the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/denylist/reported/ip/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_an_ip_address_reported_by_the_user_v1_denylist_reported_ip_ip_address_delete(client):
    """Test case for delete_an_ip_address_reported_by_the_user_v1_denylist_reported_ip_ip_address_delete

    Delete the automatically reported IP address by the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/denylist/reported/ip/{ip_address}'.format(ip_address='ip_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_the_denylist_content_v1_denylist_private_denylist_id_content_delete(client):
    """Test case for delete_the_denylist_content_v1_denylist_private_denylist_id_content_delete

    Delete all the content of a private denylist of the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/denylist/private/{denylist_id}/content'.format(denylist_id='denylist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_the_denylist_v1_denylist_private_denylist_id_delete(client):
    """Test case for delete_the_denylist_v1_denylist_private_denylist_id_delete

    Delete all the bindings between a user and a private denylist.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/denylist/private/{denylist_id}'.format(denylist_id='denylist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_the_denylist_v1_denylist_public_denylist_id_delete(client):
    """Test case for delete_the_denylist_v1_denylist_public_denylist_id_delete

    Delete all the bindings between a user and an denylist.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/denylist/public/{denylist_id}'.format(denylist_id='denylist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_owned_denylists_by_resource_type_v1_denylist_public_owned_resource_type_get(client):
    """Test case for get_all_owned_denylists_by_resource_type_v1_denylist_public_owned_resource_type_get

    Get the set of public denylists of a user by resource type.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/public/owned/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_private_denylists_by_resource_type_v1_denylist_private_all_resource_type_get(client):
    """Test case for get_all_private_denylists_by_resource_type_v1_denylist_private_all_resource_type_get

    Get the set of private denylists of the user by resource type.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/private/all/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_private_denylists_v1_denylist_private_all_get(client):
    """Test case for get_all_private_denylists_v1_denylist_private_all_get

    Get the set of private denylists of the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/private/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_public_denylists_by_resource_type_v1_denylist_public_all_resource_type_get(client):
    """Test case for get_all_public_denylists_by_resource_type_v1_denylist_public_all_resource_type_get

    Get the set of public denylists by resource type.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/public/all/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_public_denylists_v1_denylist_public_all_get(client):
    """Test case for get_all_public_denylists_v1_denylist_public_all_get

    Get the set of public denylists.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/public/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_denylist_content_v1_denylist_private_denylist_id_content_get(client):
    """Test case for get_denylist_content_v1_denylist_private_denylist_id_content_get

    Get the content of a private denylist of the user.
    """
    params = [('page', 1),
                    ('page_size', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/private/{denylist_id}/content'.format(denylist_id='denylist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_denylists_owned_by_the_user_v1_denylist_public_owned_get(client):
    """Test case for get_public_denylists_owned_by_the_user_v1_denylist_public_owned_get

    Get the set of owned denylists.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/public/owned',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_denylist_v1_denylist_private_denylist_id_get(client):
    """Test case for get_single_denylist_v1_denylist_private_denylist_id_get

    Get the details of a specific private denylist of the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/private/{denylist_id}'.format(denylist_id='denylist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_denylist_v1_denylist_public_denylist_id_get(client):
    """Test case for get_single_denylist_v1_denylist_public_denylist_id_get

    Get the details of the denylist.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/public/{denylist_id}'.format(denylist_id='denylist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_all_the_ip_addresses_reported_by_the_user_v1_denylist_reported_ip_get(client):
    """Test case for query_all_the_ip_addresses_reported_by_the_user_v1_denylist_reported_ip_get

    Get the list of automatically reported IP addresses by the user.
    """
    params = [('dataset', 'dataset_example'),
                    ('reported_before', 56),
                    ('reported_after', 56),
                    ('expires_before', 56),
                    ('expires_after', 56),
                    ('greater_than', 56),
                    ('less_than', 56),
                    ('ip_protocol_version', ALL),
                    ('output_format', JSON)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/reported/ip',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_an_ip_addresses_reported_by_the_user_v1_denylist_reported_ip_ip_address_get(client):
    """Test case for query_an_ip_addresses_reported_by_the_user_v1_denylist_reported_ip_ip_address_get

    Get the details of an automatically reported IP addresses by the user.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/reported/ip/{ip_address}'.format(ip_address='ip_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_resource_denylists_v1_denylist_private_ip_address_get(client):
    """Test case for query_resource_denylists_v1_denylist_private_ip_address_get

    Get the different denylists where the IP address was found.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/private/ip/{address}'.format(address=openapi_server.Address()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_resource_denylists_v1_denylist_public_ip_address_get(client):
    """Test case for query_resource_denylists_v1_denylist_public_ip_address_get

    Get the different public denylists where the IP address was found.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/denylist/public/ip/{address}'.format(address=openapi_server.Address()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_private_content_of_the_denylist_of_the_user_v1_denylist_private_denylist_id_content_put(client):
    """Test case for update_private_content_of_the_denylist_of_the_user_v1_denylist_private_denylist_id_content_put

    Add or remove content of a private denylist of the user.
    """
    body = openapi_server.BodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/denylist/private/{denylist_id}/content'.format(denylist_id='denylist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_private_denylist_of_the_user_v1_denylist_private_denylist_id_put(client):
    """Test case for update_private_denylist_of_the_user_v1_denylist_private_denylist_id_put

    Update the information of an existing private denylist of the user.
    """
    body = openapi_server.BodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/denylist/private/{denylist_id}'.format(denylist_id='denylist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

