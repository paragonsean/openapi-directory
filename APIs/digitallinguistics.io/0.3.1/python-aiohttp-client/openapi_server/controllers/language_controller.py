from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def add_language(request: web.Request, body) -> web.Response:
    """Add a new Language

    

    :param body: A database resource to upsert
    :type body: 

    """
    return web.Response(status=200)


async def add_lexeme_by_language(request: web.Request, language_id) -> web.Response:
    """Add a new Lexeme to a Language

    

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str

    """
    return web.Response(status=200)


async def delete_language(request: web.Request, language_id, if_match=None) -> web.Response:
    """Delete a Language by ID

    

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str
    :param if_match: The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_lexeme_by_language(request: web.Request, language_id, lexeme_id, if_match=None) -> web.Response:
    """Delete a Lexeme by ID

    

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str
    :param lexeme_id: The ID of the Lexeme to perform the operation on
    :type lexeme_id: str
    :param if_match: The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    :type if_match: str

    """
    return web.Response(status=200)


async def get_language(request: web.Request, language_id, deleted=None, if_none_match=None) -> web.Response:
    """Retrieve a Language by ID

    

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str
    :param deleted: Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    :type deleted: bool
    :param if_none_match: If &#x60;If-None-Match&#x60; header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the &#x60;If-None-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_languages(request: web.Request, continuation=None, deleted=None, if_modified_since=None, max_item_count=None, public=None) -> web.Response:
    """Get all Languages

    Retrieves all the Languages that the authenticated user or client has permission to access.

    :param continuation: The &#x60;dlx-continuation&#x60; header is used to send a continuation token with the request, when retrieving the next page of results.
    :type continuation: str
    :param deleted: Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    :type deleted: bool
    :param if_modified_since: The &#x60;If-Modified-Since&#x60; header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
    :type if_modified_since: str
    :param max_item_count: The &#x60;dlx-max-item-count&#x60; header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the &#x60;dlx-continuation&#x60; header.
    :type max_item_count: str
    :param public: Set this parameter to &#x60;true&#x60; to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
    :type public: str

    """
    return web.Response(status=200)


async def get_lexeme_by_language(request: web.Request, language_id, lexeme_id, deleted=None, if_none_match=None) -> web.Response:
    """Get a Lexeme by ID

    

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str
    :param lexeme_id: The ID of the Lexeme to perform the operation on
    :type lexeme_id: str
    :param deleted: Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    :type deleted: bool
    :param if_none_match: If &#x60;If-None-Match&#x60; header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the &#x60;If-None-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_lexemes_by_language(request: web.Request, language_id, continuation=None, deleted=None, if_modified_since=None, max_item_count=None, public=None) -> web.Response:
    """Get all Lexemes for a Language

    

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str
    :param continuation: The &#x60;dlx-continuation&#x60; header is used to send a continuation token with the request, when retrieving the next page of results.
    :type continuation: str
    :param deleted: Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    :type deleted: bool
    :param if_modified_since: The &#x60;If-Modified-Since&#x60; header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
    :type if_modified_since: str
    :param max_item_count: The &#x60;dlx-max-item-count&#x60; header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the &#x60;dlx-continuation&#x60; header.
    :type max_item_count: str
    :param public: Set this parameter to &#x60;true&#x60; to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
    :type public: str

    """
    return web.Response(status=200)


async def update_language(request: web.Request, language_id, body, if_match=None) -> web.Response:
    """Perform a partial update on a Language

    Performs a partial update the Language whose ID is specified in the URL. If the Language object has an &#x60;id&#x60; property, is ignored in favor of the ID in the URL.

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str
    :param body: A database resource to upsert
    :type body: 
    :param if_match: The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    :type if_match: str

    """
    return web.Response(status=200)


async def upsert_language(request: web.Request, body, if_match=None) -> web.Response:
    """Upsert (create or replace) a Language

    Creates a Language if it does not yet exist (i.e. if the resource does not have an &#x60;id&#x60; property yet), or replaces the existing Language resource if it does. Note that this replaces the *entire* Language. It is not a partial update.

    :param body: A database resource to upsert
    :type body: 
    :param if_match: The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    :type if_match: str

    """
    return web.Response(status=200)


async def upsert_lexeme_by_language(request: web.Request, language_id, if_match=None) -> web.Response:
    """Upsert (add or replace) a Lexeme

    

    :param language_id: The ID of the Language to perform the operation on
    :type language_id: str
    :param if_match: The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    :type if_match: str

    """
    return web.Response(status=200)
