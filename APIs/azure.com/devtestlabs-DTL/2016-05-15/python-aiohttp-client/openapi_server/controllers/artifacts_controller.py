from typing import List, Dict
from aiohttp import web

from openapi_server.models.arm_template_info import ArmTemplateInfo
from openapi_server.models.artifact import Artifact
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.generate_arm_template_request import GenerateArmTemplateRequest
from openapi_server.models.response_with_continuation_artifact import ResponseWithContinuationArtifact
from openapi_server import util


async def artifacts_generate_arm_template(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, name, api_version, generate_arm_template_request) -> web.Response:
    """artifacts_generate_arm_template

    Generates an ARM template for the given artifact, uploads the required files to a storage account, and validates the generated artifact.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param artifact_source_name: The name of the artifact source.
    :type artifact_source_name: str
    :param name: The name of the artifact.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param generate_arm_template_request: Parameters for generating an ARM template for deploying artifacts.
    :type generate_arm_template_request: dict | bytes

    """
    generate_arm_template_request = GenerateArmTemplateRequest.from_dict(generate_arm_template_request)
    return web.Response(status=200)


async def artifacts_get(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, name, api_version, expand=None) -> web.Response:
    """artifacts_get

    Get artifact.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param artifact_source_name: The name of the artifact source.
    :type artifact_source_name: str
    :param name: The name of the artifact.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;title)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def artifacts_list(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """artifacts_list

    List artifacts in a given artifact source.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param artifact_source_name: The name of the artifact source.
    :type artifact_source_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;title)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)
