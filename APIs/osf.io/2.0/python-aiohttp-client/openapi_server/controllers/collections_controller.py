from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server import util


async def collections_add_metadata(request: web.Request, collection_id, body) -> web.Response:
    """Add Metadata or Subjects to a Entity in a Collection

    List of user created metadata for entities within a collection. #### Permissions To edit this collection a user must have collections write permissions #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def collections_collected_metadata(request: web.Request, collection_id, cgm_id) -> web.Response:
    """Retrieve subject data for a specific piece of metadata info for a collection

     #### Permissions In order to view these subject it must be a public collection or a user must have read permissions for collection.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error, other then permissions errors.

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param cgm_id: A short id for that piece of metadata
    :type cgm_id: str

    """
    return web.Response(status=200)


async def collections_create(request: web.Request, body) -> web.Response:
    """Create a Collection

    Retrieves a list collections, either public or related to the user #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def collections_delete(request: web.Request, collection_id) -> web.Response:
    """Delete a Collection

    Deletes a collection, if the user has appropriate permissions. #### Permissions Users must have write permissions on a collection in order to delete it #### Returns Nothing is returned in the body

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_detail(request: web.Request, collection_id) -> web.Response:
    """Retrieve a Collection

    Retrieves a collection, if the user has appropriate permissions.  #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_linked_nodes_list(request: web.Request, collection_id) -> web.Response:
    """List All Linked Nodes for a Collection

    List of all nodes linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_linked_nodes_relationships(request: web.Request, collection_id, body) -> web.Response:
    """Link Nodes to Collection

    This endpoint allow users to a add a node to a collection by issuing a POST request. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def collections_linked_nodes_relationships_create(request: web.Request, collection_id) -> web.Response:
    """Give a Sparse List of Node Ids

    List of all the node ids linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_linked_nodes_relationships_delete(request: web.Request, collection_id, body) -> web.Response:
    """Remove Nodes From Collection

     This removes associated nodes from a collection #### Permissions Any user with write permissions on this collection should be to remove nodes from this collection. #### Returns Nothing in the response body.

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def collections_linked_preprints_list(request: web.Request, collection_id) -> web.Response:
    """List All Linked Preprints for a Collection

    List of all preprints linked to the given collection. #### Permissions This returns all public preprints associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_linked_registrations_list(request: web.Request, collection_id) -> web.Response:
    """List All Linked Registrations for a Collection

    List of all registrations linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_linked_registrations_relationships(request: web.Request, collection_id, body) -> web.Response:
    """Link Registrations to Collection

    This endpoint allow users to a add a registration to a collection by issuing a POST request. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def collections_linked_registrations_relationships_create(request: web.Request, collection_id) -> web.Response:
    """Give a Sparse List of Registrations Ids

    List of all the registration ids linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_linked_registrations_relationships_delete(request: web.Request, collection_id, body) -> web.Response:
    """Remove Registrations From Collection

     This removes associated registrations from a collection #### Permissions Any user with write permissions on this collection should be to remove registrations from this collection. #### Returns Nothing in the response body.

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def collections_list(request: web.Request, ) -> web.Response:
    """List all Collections

    Retrieves a list collections, either public or related to the user #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).


    """
    return web.Response(status=200)


async def collections_metadata_delete(request: web.Request, collection_id, cgm_id) -> web.Response:
    """Delete Collection Metadata from entitiy

     #### Permissions Only a user with collection admin permissions can delete collected metadata #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param cgm_id: A short id for that piece of metadata
    :type cgm_id: str

    """
    return web.Response(status=200)


async def collections_metadata_detail(request: web.Request, collection_id, cgm_id, body) -> web.Response:
    """Add Metadata or Subjects to an Entity in a Collection

    List of user created metadata for entities within a collection. #### Permissions To edit this collection a user must have collections write permissions #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param cgm_id: A short id for that piece of metadata
    :type cgm_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def collections_metadata_registrations_detail(request: web.Request, collection_id, cgm_id) -> web.Response:
    """Retrieve Specific Metadata for a Collection

     #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param cgm_id: A short id for that piece of metadata
    :type cgm_id: str

    """
    return web.Response(status=200)


async def collections_metadata_registrations_list(request: web.Request, collection_id) -> web.Response:
    """Retrieve a list of collected metadata for a collection

    List of user created metadata for entities within a collection. #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

    :param collection_id: A short id for that collection
    :type collection_id: str

    """
    return web.Response(status=200)


async def collections_metadata_subjects_relationships(request: web.Request, collection_id, cgm_id) -> web.Response:
    """Retrieve subject metadata for a specific piece of metadata in a collection

     #### Permissions This is public for a logged out user when an entity is public. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param cgm_id: A short id for that piece of metadata
    :type cgm_id: str

    """
    return web.Response(status=200)


async def collections_metadata_subjects_relationships_update(request: web.Request, collection_id, cgm_id, body) -> web.Response:
    """Update subjects for a specific piece of metadata in a collection

     #### Permissions This is editable for a user with a write permission for this collection.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

    :param collection_id: A short id for that collection
    :type collection_id: str
    :param cgm_id: A short id for that piece of metadata
    :type cgm_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
