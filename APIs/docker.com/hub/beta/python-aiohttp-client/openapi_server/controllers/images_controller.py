from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_namespace_repository_images_response import GetNamespaceRepositoryImagesResponse
from openapi_server.models.get_namespace_repository_images_summary_response import GetNamespaceRepositoryImagesSummaryResponse
from openapi_server.models.get_namespace_repository_images_tags_response import GetNamespaceRepositoryImagesTagsResponse
from openapi_server.models.post_namespaces_delete_images_request import PostNamespacesDeleteImagesRequest
from openapi_server.models.post_namespaces_delete_images_response_error import PostNamespacesDeleteImagesResponseError
from openapi_server.models.post_namespaces_delete_images_response_success import PostNamespacesDeleteImagesResponseSuccess
from openapi_server import util


async def get_namespaces_repositories_images(request: web.Request, namespace, repository, status=None, currently_tagged=None, ordering=None, active_from=None, page=None, page_size=None) -> web.Response:
    """Get details of repository&#39;s images

    Gets details on the images in a repository.

    :param namespace: Namespace of the repository.
    :type namespace: str
    :param repository: Name of the repository.
    :type repository: str
    :param status: Filters to only show images of this status.
    :type status: str
    :param currently_tagged: Filters to only show images with: - &#x60;true&#x60;: at least 1 current tag. - &#x60;false&#x60;: no current tags. 
    :type currently_tagged: bool
    :param ordering: Orders the results by this property.  Prefixing with &#x60;-&#x60; sorts by descending order. 
    :type ordering: str
    :param active_from: Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time. 
    :type active_from: str
    :param page: Page number to get. Defaults to 1.
    :type page: int
    :param page_size: Number of images to get per page. Defaults to 10. Max of 100.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_namespaces_repositories_images_summary(request: web.Request, namespace, repository, active_from=None) -> web.Response:
    """Get summary of repository&#39;s images

    Gets the number of images in a repository and the number of images counted as active and inactive. 

    :param namespace: Namespace of the repository.
    :type namespace: str
    :param repository: Name of the repository.
    :type repository: str
    :param active_from: Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time. 
    :type active_from: str

    """
    return web.Response(status=200)


async def get_namespaces_repositories_images_tags(request: web.Request, namespace, repository, digest, page=None, page_size=None) -> web.Response:
    """Get image&#39;s tags

    Gets current and historical tags for an image.

    :param namespace: Namespace of the repository.
    :type namespace: str
    :param repository: Name of the repository.
    :type repository: str
    :param digest: Digest of the image.
    :type digest: str
    :param page: Page number to get. Defaults to 1.
    :type page: int
    :param page_size: Number of images to get per page. Defaults to 10. Max of 100.
    :type page_size: int

    """
    return web.Response(status=200)


async def post_namespaces_delete_images(request: web.Request, namespace, body) -> web.Response:
    """Delete images

    Deletes one or more images within a namespace. This is currently limited to a single  repository.  If you attempt to delete images that are marked as active or are currently tagged, the deletion does not happen and it displays the warnings. To continue with the deletion, you must ignore these warnings by putting them in the &#x60;ignore_warnings&#x60; property.  Deleting a currently tagged image deletes the tag from the repository.  You cannot ignore errors. It is not possible to directly delete children of multi-arch images. 

    :param namespace: Namespace of the repository.
    :type namespace: str
    :param body: Delete request.
    :type body: dict | bytes

    """
    body = PostNamespacesDeleteImagesRequest.from_dict(body)
    return web.Response(status=200)
