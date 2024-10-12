from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_search_results import ArtifactSearchResults
from openapi_server.models.error import Error
from openapi_server.models.version_search_results import VersionSearchResults
from openapi_server import util


async def search_artifacts(request: web.Request, offset, limit, search=None, over=None, order=None) -> web.Response:
    """Search for artifacts

    Returns a paginated list of all artifacts that match the provided search criteria. 

    :param offset: The number of artifacts to skip before starting to collect the result set.
    :type offset: int
    :param limit: The number of artifacts to return.
    :type limit: int
    :param search: The text to search.
    :type search: str
    :param over: What fields to search.
    :type over: str
    :param order: Sort order, ascending or descending.
    :type order: str

    """
    return web.Response(status=200)


async def search_versions(request: web.Request, artifact_id, offset, limit) -> web.Response:
    """Search artifact versions

    Searches for versions of a specific artifact.  This is typically used to get a listing of all versions of an artifact (for example, in a user interface).

    :param artifact_id: The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    :type artifact_id: str
    :param offset: The number of versions to skip before starting to collect the result set.
    :type offset: int
    :param limit: The number of versions to return.
    :type limit: int

    """
    return web.Response(status=200)
