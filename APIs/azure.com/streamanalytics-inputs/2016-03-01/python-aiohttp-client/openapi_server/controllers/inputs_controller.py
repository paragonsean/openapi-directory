from typing import List, Dict
from aiohttp import web

from openapi_server.models.input import Input
from openapi_server.models.input_list_result import InputListResult
from openapi_server.models.resource_test_status import ResourceTestStatus
from openapi_server import util


async def inputs_create_or_replace(request: web.Request, api_version, subscription_id, resource_group_name, job_name, input_name, input, if_match=None, if_none_match=None) -> web.Response:
    """inputs_create_or_replace

    Creates an input or replaces an already existing input under an existing streaming job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param input_name: The name of the input.
    :type input_name: str
    :param input: The definition of the input that will be used to create a new input or replace the existing one under the streaming job.
    :type input: dict | bytes
    :param if_match: The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    :type if_match: str
    :param if_none_match: Set to &#39;*&#39; to allow a new input to be created, but to prevent updating an existing input. Other values will result in a 412 Pre-condition Failed response.
    :type if_none_match: str

    """
    input = Input.from_dict(input)
    return web.Response(status=200)


async def inputs_delete(request: web.Request, api_version, subscription_id, resource_group_name, job_name, input_name) -> web.Response:
    """inputs_delete

    Deletes an input from the streaming job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param input_name: The name of the input.
    :type input_name: str

    """
    return web.Response(status=200)


async def inputs_get(request: web.Request, api_version, subscription_id, resource_group_name, job_name, input_name) -> web.Response:
    """inputs_get

    Gets details about the specified input.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param input_name: The name of the input.
    :type input_name: str

    """
    return web.Response(status=200)


async def inputs_list_by_streaming_job(request: web.Request, api_version, subscription_id, resource_group_name, job_name, select=None) -> web.Response:
    """inputs_list_by_streaming_job

    Lists all of the inputs under the specified streaming job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param select: The $select OData query parameter. This is a comma-separated list of structural properties to include in the response, or \&quot;*\&quot; to include all properties. By default, all properties are returned except diagnostics. Currently only accepts &#39;*&#39; as a valid value.
    :type select: str

    """
    return web.Response(status=200)


async def inputs_test(request: web.Request, api_version, subscription_id, resource_group_name, job_name, input_name, input=None) -> web.Response:
    """inputs_test

    Tests whether an input’s datasource is reachable and usable by the Azure Stream Analytics service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param input_name: The name of the input.
    :type input_name: str
    :param input: If the input specified does not already exist, this parameter must contain the full input definition intended to be tested. If the input specified already exists, this parameter can be left null to test the existing input as is or if specified, the properties specified will overwrite the corresponding properties in the existing input (exactly like a PATCH operation) and the resulting input will be tested.
    :type input: dict | bytes

    """
    input = Input.from_dict(input)
    return web.Response(status=200)


async def inputs_update(request: web.Request, api_version, subscription_id, resource_group_name, job_name, input_name, input, if_match=None) -> web.Response:
    """inputs_update

    Updates an existing input under an existing streaming job. This can be used to partially update (ie. update one or two properties) an input without affecting the rest the job or input definition.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param input_name: The name of the input.
    :type input_name: str
    :param input: An Input object. The properties specified here will overwrite the corresponding properties in the existing input (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing input will remain the same and not change as a result of this PATCH operation.
    :type input: dict | bytes
    :param if_match: The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    :type if_match: str

    """
    input = Input.from_dict(input)
    return web.Response(status=200)
