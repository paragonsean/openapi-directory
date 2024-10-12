# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_response import RestResponse


pytestmark = pytest.mark.asyncio

async def test_add_profile_using_post(client):
    """Test case for add_profile_using_post

    Creates a new profile with no faces associated to it (empty profile)
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example'),
                    ('externalId', 'external_id_example'),
                    ('screenName', 'screen_name_example'),
                    ('labels', ['labels_example']),
                    ('classificationAttributes', 'classification_attributes_example'),
                    ('details', 'details_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/profile/profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_profile2_using_delete(client):
    """Test case for delete_profile2_using_delete

    Deletes a profile and unmaps all its faces
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example'),
                    ('profileId', 'profile_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/profile/profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_profile_using_delete(client):
    """Test case for delete_profile_using_delete

    Deletes a profile and unmaps all its faces
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/profile/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_classification_attributes_from_profile_using_get(client):
    """Test case for get_classification_attributes_from_profile_using_get

    Gets classification attributes from a profile
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('profileId', 'profile_id_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/profile/classificationAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_faces_from_profile_using_get(client):
    """Test case for get_faces_from_profile_using_get

    Gets all the faceHashes associated to a profile
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('profileId', 'profile_id_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/profile/map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_enrollment_status_using_get(client):
    """Test case for get_profile_enrollment_status_using_get

    Gets the enrollment status of a profile: information on whether it is suitable for authentication.
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('profileId', 'profile_id_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/profile/enrollmentStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_using_get(client):
    """Test case for get_profile_using_get

    Retrieves a profile
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example'),
                    ('withFaces', 'false')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/profile/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_classification_attributes_to_profile_using_put(client):
    """Test case for map_classification_attributes_to_profile_using_put

    Maps classification attributes to a profile
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('profileId', 'profile_id_example'),
                    ('collectionId', 'collection_id_example'),
                    ('classificationAttributes', 'classification_attributes_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v1.1/profile/classificationAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_faces_to_profile_using_post(client):
    """Test case for map_faces_to_profile_using_post

    Adds (maps) a list of faces, identified by faceHashes, to a profile, identified by profileId
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('faceHashes', 'face_hashes_example'),
                    ('profileId', 'profile_id_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/profile/map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_classification_attributes_from_profile_using_delete(client):
    """Test case for remove_classification_attributes_from_profile_using_delete

    Removes classification attributes from a profile
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('profileId', 'profile_id_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/profile/classificationAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_faces_from_profile_using_delete(client):
    """Test case for remove_faces_from_profile_using_delete

    Removes (unmaps) a list of faces, identified by faceHashes, from a profile, identified by profileId
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('faceHashes', 'face_hashes_example'),
                    ('profileId', 'profile_id_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/profile/map',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_profile_using_patch(client):
    """Test case for update_profile_using_patch

    Update an existing profile with a given id
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example'),
                    ('externalId', 'external_id_example'),
                    ('screenName', 'screen_name_example'),
                    ('labels', ['labels_example']),
                    ('classificationAttributes', 'classification_attributes_example'),
                    ('details', 'details_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/rest/v1.1/profile/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

