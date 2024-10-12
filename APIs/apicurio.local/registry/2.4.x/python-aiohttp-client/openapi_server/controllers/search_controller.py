from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_search_results import ArtifactSearchResults
from openapi_server.models.error import Error
from openapi_server.models.sort_by import SortBy
from openapi_server.models.sort_order import SortOrder
from openapi_server import util


async def search_artifacts(request: web.Request, name=None, offset=None, limit=None, order=None, orderby=None, labels=None, properties=None, description=None, group=None, global_id=None, content_id=None) -> web.Response:
    """Search for artifacts

    Returns a paginated list of all artifacts that match the provided filter criteria. 

    :param name: Filter by artifact name.
    :type name: str
    :param offset: The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    :type offset: int
    :param limit: The number of artifacts to return.  Defaults to 20.
    :type limit: int
    :param order: Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;).
    :type order: dict | bytes
    :param orderby: The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60; 
    :type orderby: dict | bytes
    :param labels: Filter by label.  Include one or more label to only return artifacts containing all of the specified labels.
    :type labels: List[str]
    :param properties: Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example &#x60;properties&#x3D;foo:bar&#x60; will return only artifacts with a custom property named &#x60;foo&#x60; and value &#x60;bar&#x60;.
    :type properties: List[str]
    :param description: Filter by description.
    :type description: str
    :param group: Filter by artifact group.
    :type group: str
    :param global_id: Filter by globalId.
    :type global_id: int
    :param content_id: Filter by contentId.
    :type content_id: int

    """
    order = .from_dict(order)
    orderby = .from_dict(orderby)
    return web.Response(status=200)


async def search_artifacts_by_content(request: web.Request, body, canonical=None, artifact_type=None, offset=None, limit=None, order=None, orderby=None) -> web.Response:
    """Search for artifacts by content

    Returns a paginated list of all artifacts with at least one version that matches the posted content. 

    :param body: The content to search for.
    :type body: str
    :param canonical: Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the &#x60;artifactType&#x60; query parameter.
    :type canonical: bool
    :param artifact_type: Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the &#x60;canonical&#x60; query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.
    :type artifact_type: str
    :param offset: The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    :type offset: int
    :param limit: The number of artifacts to return.  Defaults to 20.
    :type limit: int
    :param order: Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;).
    :type order: str
    :param orderby: The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60; 
    :type orderby: str

    """
    return web.Response(status=200)
