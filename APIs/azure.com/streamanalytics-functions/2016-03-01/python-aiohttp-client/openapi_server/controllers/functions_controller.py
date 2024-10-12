from typing import List, Dict
from aiohttp import web

from openapi_server.models.function import Function
from openapi_server.models.function_list_result import FunctionListResult
from openapi_server.models.function_retrieve_default_definition_parameters import FunctionRetrieveDefaultDefinitionParameters
from openapi_server.models.functions_test200_response import FunctionsTest200Response
from openapi_server import util


async def functions_create_or_replace(request: web.Request, api_version, subscription_id, resource_group_name, job_name, function_name, function, if_match=None, if_none_match=None) -> web.Response:
    """functions_create_or_replace

    Creates a function or replaces an already existing function under an existing streaming job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param function_name: The name of the function.
    :type function_name: str
    :param function: The definition of the function that will be used to create a new function or replace the existing one under the streaming job.
    :type function: dict | bytes
    :param if_match: The ETag of the function. Omit this value to always overwrite the current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    :type if_match: str
    :param if_none_match: Set to &#39;*&#39; to allow a new function to be created, but to prevent updating an existing function. Other values will result in a 412 Pre-condition Failed response.
    :type if_none_match: str

    """
    function = Function.from_dict(function)
    return web.Response(status=200)


async def functions_delete(request: web.Request, api_version, subscription_id, resource_group_name, job_name, function_name) -> web.Response:
    """functions_delete

    Deletes a function from the streaming job.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param function_name: The name of the function.
    :type function_name: str

    """
    return web.Response(status=200)


async def functions_get(request: web.Request, api_version, subscription_id, resource_group_name, job_name, function_name) -> web.Response:
    """functions_get

    Gets details about the specified function.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param function_name: The name of the function.
    :type function_name: str

    """
    return web.Response(status=200)


async def functions_list_by_streaming_job(request: web.Request, api_version, subscription_id, resource_group_name, job_name, select=None) -> web.Response:
    """functions_list_by_streaming_job

    Lists all of the functions under the specified streaming job.

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


async def functions_retrieve_default_definition(request: web.Request, api_version, subscription_id, resource_group_name, job_name, function_name, function_retrieve_default_definition_parameters=None) -> web.Response:
    """functions_retrieve_default_definition

    Retrieves the default definition of a function based on the parameters specified.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param function_name: The name of the function.
    :type function_name: str
    :param function_retrieve_default_definition_parameters: Parameters used to specify the type of function to retrieve the default definition for.
    :type function_retrieve_default_definition_parameters: dict | bytes

    """
    function_retrieve_default_definition_parameters = FunctionRetrieveDefaultDefinitionParameters.from_dict(function_retrieve_default_definition_parameters)
    return web.Response(status=200)


async def functions_test(request: web.Request, api_version, subscription_id, resource_group_name, job_name, function_name, function=None) -> web.Response:
    """functions_test

    Tests if the information provided for a function is valid. This can range from testing the connection to the underlying web service behind the function or making sure the function code provided is syntactically correct.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param function_name: The name of the function.
    :type function_name: str
    :param function: If the function specified does not already exist, this parameter must contain the full function definition intended to be tested. If the function specified already exists, this parameter can be left null to test the existing function as is or if specified, the properties specified will overwrite the corresponding properties in the existing function (exactly like a PATCH operation) and the resulting function will be tested.
    :type function: dict | bytes

    """
    function = Function.from_dict(function)
    return web.Response(status=200)


async def functions_update(request: web.Request, api_version, subscription_id, resource_group_name, job_name, function_name, function, if_match=None) -> web.Response:
    """functions_update

    Updates an existing function under an existing streaming job. This can be used to partially update (ie. update one or two properties) a function without affecting the rest the job or function definition.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: GUID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param job_name: The name of the streaming job.
    :type job_name: str
    :param function_name: The name of the function.
    :type function_name: str
    :param function: A function object. The properties specified here will overwrite the corresponding properties in the existing function (ie. Those properties will be updated). Any properties that are set to null here will mean that the corresponding property in the existing function will remain the same and not change as a result of this PATCH operation.
    :type function: dict | bytes
    :param if_match: The ETag of the function. Omit this value to always overwrite the current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    :type if_match: str

    """
    function = Function.from_dict(function)
    return web.Response(status=200)
