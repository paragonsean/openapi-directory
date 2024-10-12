from typing import List, Dict
from aiohttp import web

from openapi_server.models.arm_template_info import ArmTemplateInfo
from openapi_server.models.artifact import Artifact
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.generate_arm_template_request import GenerateArmTemplateRequest
from openapi_server.models.response_with_continuation_artifact import ResponseWithContinuationArtifact
from openapi_server import util


async def artifact_generate_arm_template(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, name, api_version, generate_arm_template_request) -> web.Response:
    """artifact_generate_arm_template

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
    :param generate_arm_template_request: 
    :type generate_arm_template_request: dict | bytes

    """
    generate_arm_template_request = GenerateArmTemplateRequest.from_dict(generate_arm_template_request)
    return web.Response(status=200)


async def artifact_get_resource(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, name, api_version) -> web.Response:
    """artifact_get_resource

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

    """
    return web.Response(status=200)


async def artifact_list(request: web.Request, subscription_id, resource_group_name, lab_name, artifact_source_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """artifact_list

    List artifacts.

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
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)
