from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_response import RestResponse
from openapi_server import util


async def add_profile_using_post(request: web.Request, access_key, secret_key, collection_id, external_id=None, screen_name=None, labels=None, classification_attributes=None, details=None) -> web.Response:
    """Creates a new profile with no faces associated to it (empty profile)

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: Uniquely identified collection that can store multiple profiles
    :type collection_id: str
    :param external_id: External reference to additional information you don’t want to share with VisageCloud
    :type external_id: str
    :param screen_name: Human-readable label for the profile
    :type screen_name: str
    :param labels: Allows you to do finer filtering in face recognition
    :type labels: List[str]
    :param classification_attributes: Comma separated key:value classification attributes
    :type classification_attributes: str
    :param details: Comma separated key:value details of profile
    :type details: str

    """
    return web.Response(status=200)


async def delete_profile2_using_delete(request: web.Request, access_key, secret_key, collection_id, profile_id) -> web.Response:
    """Deletes a profile and unmaps all its faces

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: Uniquely identified collection that can store multiple profiles
    :type collection_id: str
    :param profile_id: The profile id (provide this if you don&#39;t have the externalId
    :type profile_id: str

    """
    return web.Response(status=200)


async def delete_profile_using_delete(request: web.Request, access_key, secret_key, collection_id, id) -> web.Response:
    """Deletes a profile and unmaps all its faces

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: Uniquely identified collection that can store multiple profiles
    :type collection_id: str
    :param id: The profile id (provide this if you don&#39;t have the externalId
    :type id: str

    """
    return web.Response(status=200)


async def get_classification_attributes_from_profile_using_get(request: web.Request, access_key, secret_key, profile_id, collection_id) -> web.Response:
    """Gets classification attributes from a profile

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param profile_id: The profile associated with the classification attributes
    :type profile_id: str
    :param collection_id: The collection that contains the profile
    :type collection_id: str

    """
    return web.Response(status=200)


async def get_faces_from_profile_using_get(request: web.Request, access_key, secret_key, profile_id, collection_id) -> web.Response:
    """Gets all the faceHashes associated to a profile

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param profile_id: The profile that contains the faces
    :type profile_id: str
    :param collection_id: The collection that contains the profile
    :type collection_id: str

    """
    return web.Response(status=200)


async def get_profile_enrollment_status_using_get(request: web.Request, access_key, secret_key, profile_id, collection_id) -> web.Response:
    """Gets the enrollment status of a profile: information on whether it is suitable for authentication.

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param profile_id: The profile that contains the faces
    :type profile_id: str
    :param collection_id: The collection that contains the profile
    :type collection_id: str

    """
    return web.Response(status=200)


async def get_profile_using_get(request: web.Request, access_key, secret_key, collection_id, id, with_faces=None) -> web.Response:
    """Retrieves a profile

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: Uniquely identified collection that can store multiple profiles
    :type collection_id: str
    :param id: The profile id (provide this if you don&#39;t have the externalId
    :type id: str
    :param with_faces: Retrieves the profile with all its associated faces
    :type with_faces: str

    """
    return web.Response(status=200)


async def map_classification_attributes_to_profile_using_put(request: web.Request, access_key, secret_key, profile_id, collection_id, classification_attributes) -> web.Response:
    """Maps classification attributes to a profile

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param profile_id: The profile associated with the classification attributes
    :type profile_id: str
    :param collection_id: The collection that contains the profile
    :type collection_id: str
    :param classification_attributes: Comma separated key:value classification attributes
    :type classification_attributes: str

    """
    return web.Response(status=200)


async def map_faces_to_profile_using_post(request: web.Request, access_key, secret_key, face_hashes, profile_id, collection_id) -> web.Response:
    """Adds (maps) a list of faces, identified by faceHashes, to a profile, identified by profileId

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param face_hashes: Comma separated face hashes, that will be associated to a profile
    :type face_hashes: str
    :param profile_id: The profile that will store the face
    :type profile_id: str
    :param collection_id: The collection that contains the profile
    :type collection_id: str

    """
    return web.Response(status=200)


async def remove_classification_attributes_from_profile_using_delete(request: web.Request, access_key, secret_key, profile_id, collection_id) -> web.Response:
    """Removes classification attributes from a profile

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param profile_id: The profile associated with the classification attributes
    :type profile_id: str
    :param collection_id: The collection that contains the profile
    :type collection_id: str

    """
    return web.Response(status=200)


async def remove_faces_from_profile_using_delete(request: web.Request, access_key, secret_key, face_hashes, profile_id, collection_id) -> web.Response:
    """Removes (unmaps) a list of faces, identified by faceHashes, from a profile, identified by profileId

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param face_hashes: Comma separated face hashes, that will be removed from a profile
    :type face_hashes: str
    :param profile_id: The profile that contains the face
    :type profile_id: str
    :param collection_id: The collection that contains the profile
    :type collection_id: str

    """
    return web.Response(status=200)


async def update_profile_using_patch(request: web.Request, access_key, secret_key, id, collection_id, external_id=None, screen_name=None, labels=None, classification_attributes=None, details=None) -> web.Response:
    """Update an existing profile with a given id

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the profile that will be updated
    :type id: str
    :param collection_id: Uniquely identified collection that can store multiple profiles
    :type collection_id: str
    :param external_id: External reference to additional information you don’t want to share with VisageCloud
    :type external_id: str
    :param screen_name: Human-readable label for the profile
    :type screen_name: str
    :param labels: Allows you to do finer filtering in face recognition
    :type labels: List[str]
    :param classification_attributes: Comma separated key:value classification attributes
    :type classification_attributes: str
    :param details: Comma separated key:value details of profile
    :type details: str

    """
    return web.Response(status=200)
