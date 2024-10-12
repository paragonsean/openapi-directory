from typing import List, Dict
from aiohttp import web

from openapi_server.models.transformation import Transformation
from openapi_server import util


async def transformations_create_or_replace(request: web.Request, api_version, subscription_id, resource_group_name, job_name, transformation_name, transformation, if_match=None, if_none_match=None) -> web.Response:
    """transformations_create_or_replace

    Creates a transformation or replaces an already existing transformation under an existing streaming job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param transformation_name: The name of the transformation.
    :type transformation_name: str
    :param transformation: The definition of the transformation that will be used to create a new transformation or replace the existing one under the streaming job.
    :type transformation: dict | bytes
    :param if_match: The ETag of the transformation. Omit this value to always overwrite the current transformation. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    :type if_match: str
    :param if_none_match: Set to &#39;*&#39; to allow a new transformation to be created, but to prevent updating an existing transformation. Other values will result in a 412 Pre-condition Failed response.
    :type if_none_match: str

    """
    transformation = Transformation.from_dict(transformation)
    return web.Response(status=200)


async def transformations_get(request: web.Request, api_version, subscription_id, resource_group_name, job_name, transformation_name) -> web.Response:
    """transformations_get

    Gets details about the specified transformation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param transformation_name: The name of the transformation.
    :type transformation_name: str

    """
    return web.Response(status=200)


async def transformations_update(request: web.Request, api_version, subscription_id, resource_group_name, job_name, transformation_name, transformation, if_match=None) -> web.Response:
    """transformations_update

    Updates an existing transformation under an existing streaming job. This can be used to partially update (ie. update one or two properties) a transformation without affecting the rest the job or transformation definition.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param transformation_name: The name of the transformation.
    :type transformation_name: str
    :param transformation: A Transformation object. The properties specified here will overwrite the corresponding properties in the existing transformation (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing transformation will remain the same and not change as a result of this PATCH operation.
    :type transformation: dict | bytes
    :param if_match: The ETag of the transformation. Omit this value to always overwrite the current transformation. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    :type if_match: str

    """
    transformation = Transformation.from_dict(transformation)
    return web.Response(status=200)
