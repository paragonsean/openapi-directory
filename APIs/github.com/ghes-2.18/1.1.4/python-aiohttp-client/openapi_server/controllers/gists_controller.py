from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_gist import BaseGist
from openapi_server.models.basic_error import BasicError
from openapi_server.models.gist_comment import GistComment
from openapi_server.models.gist_commit import GistCommit
from openapi_server.models.gist_simple import GistSimple
from openapi_server.models.gists_create_comment_request import GistsCreateCommentRequest
from openapi_server.models.gists_create_request import GistsCreateRequest
from openapi_server.models.gists_get403_response import GistsGet403Response
from openapi_server.models.gists_update_request import GistsUpdateRequest
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def gists_check_is_starred(request: web.Request, gist_id) -> web.Response:
    """Check if a gist is starred

    

    :param gist_id: gist_id parameter
    :type gist_id: str

    """
    return web.Response(status=200)


async def gists_create(request: web.Request, body) -> web.Response:
    """Create a gist

    Allows you to add a new gist with one or more files.  **Note:** Don&#39;t name your files \&quot;gistfile\&quot; with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally.

    :param body: 
    :type body: dict | bytes

    """
    body = GistsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def gists_create_comment(request: web.Request, gist_id, body) -> web.Response:
    """Create a gist comment

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GistsCreateCommentRequest.from_dict(body)
    return web.Response(status=200)


async def gists_delete(request: web.Request, gist_id) -> web.Response:
    """Delete a gist

    

    :param gist_id: gist_id parameter
    :type gist_id: str

    """
    return web.Response(status=200)


async def gists_delete_comment(request: web.Request, gist_id, comment_id) -> web.Response:
    """Delete a gist comment

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def gists_fork(request: web.Request, gist_id) -> web.Response:
    """Fork a gist

    **Note**: This was previously &#x60;/gists/:gist_id/fork&#x60;.

    :param gist_id: gist_id parameter
    :type gist_id: str

    """
    return web.Response(status=200)


async def gists_get(request: web.Request, gist_id) -> web.Response:
    """Get a gist

    

    :param gist_id: gist_id parameter
    :type gist_id: str

    """
    return web.Response(status=200)


async def gists_get_comment(request: web.Request, gist_id, comment_id) -> web.Response:
    """Get a gist comment

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param comment_id: comment_id parameter
    :type comment_id: int

    """
    return web.Response(status=200)


async def gists_get_revision(request: web.Request, gist_id, sha) -> web.Response:
    """Get a gist revision

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param sha: 
    :type sha: str

    """
    return web.Response(status=200)


async def gists_list(request: web.Request, since=None, per_page=None, page=None) -> web.Response:
    """List gists for the authenticated user

    Lists the authenticated user&#39;s gists or if called anonymously, this endpoint returns all public gists:

    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def gists_list_comments(request: web.Request, gist_id, per_page=None, page=None) -> web.Response:
    """List gist comments

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def gists_list_commits(request: web.Request, gist_id, per_page=None, page=None) -> web.Response:
    """List gist commits

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def gists_list_for_user(request: web.Request, username, since=None, per_page=None, page=None) -> web.Response:
    """List gists for a user

    Lists public gists for the specified user:

    :param username: 
    :type username: str
    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def gists_list_forks(request: web.Request, gist_id, per_page=None, page=None) -> web.Response:
    """List gist forks

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def gists_list_public(request: web.Request, since=None, per_page=None, page=None) -> web.Response:
    """List public gists

    List public gists sorted by most recently updated to least recently updated.  Note: With [pagination](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#pagination), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.

    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def gists_list_starred(request: web.Request, since=None, per_page=None, page=None) -> web.Response:
    """List starred gists

    List the authenticated user&#39;s starred gists:

    :param since: Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;.
    :type since: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def gists_star(request: web.Request, gist_id) -> web.Response:
    """Star a gist

    Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.18/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

    :param gist_id: gist_id parameter
    :type gist_id: str

    """
    return web.Response(status=200)


async def gists_unstar(request: web.Request, gist_id) -> web.Response:
    """Unstar a gist

    

    :param gist_id: gist_id parameter
    :type gist_id: str

    """
    return web.Response(status=200)


async def gists_update(request: web.Request, gist_id, body) -> web.Response:
    """Update a gist

    Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren&#39;t explicitly changed during an edit are unchanged.

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GistsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def gists_update_comment(request: web.Request, gist_id, comment_id, body) -> web.Response:
    """Update a gist comment

    

    :param gist_id: gist_id parameter
    :type gist_id: str
    :param comment_id: comment_id parameter
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GistsCreateCommentRequest.from_dict(body)
    return web.Response(status=200)
