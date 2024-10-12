from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.annotation_error import AnnotationError
from openapi_server.models.annotations_list_result import AnnotationsListResult
from openapi_server import util


async def annotations_create(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, annotation_properties) -> web.Response:
    """annotations_create

    Create an Annotation of an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param annotation_properties: Properties that need to be specified to create an annotation of a Application Insights component.
    :type annotation_properties: dict | bytes

    """
    annotation_properties = Annotation.from_dict(annotation_properties)
    return web.Response(status=200)


async def annotations_delete(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, annotation_id) -> web.Response:
    """annotations_delete

    Delete an Annotation of an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param annotation_id: The unique annotation ID. This is unique within a Application Insights component.
    :type annotation_id: str

    """
    return web.Response(status=200)


async def annotations_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, annotation_id) -> web.Response:
    """annotations_get

    Get the annotation for given id.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param annotation_id: The unique annotation ID. This is unique within a Application Insights component.
    :type annotation_id: str

    """
    return web.Response(status=200)


async def annotations_list(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, start, end) -> web.Response:
    """annotations_list

    Gets the list of annotations for a component for given time range

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param start: The start time to query from for annotations, cannot be older than 90 days from current date.
    :type start: str
    :param end: The end time to query for annotations.
    :type end: str

    """
    return web.Response(status=200)
