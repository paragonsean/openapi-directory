from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_suite_definition_request import CreateSuiteDefinitionRequest
from openapi_server.models.create_suite_definition_response import CreateSuiteDefinitionResponse
from openapi_server.models.get_endpoint_response import GetEndpointResponse
from openapi_server.models.get_suite_definition_response import GetSuiteDefinitionResponse
from openapi_server.models.get_suite_run_report_response import GetSuiteRunReportResponse
from openapi_server.models.get_suite_run_response import GetSuiteRunResponse
from openapi_server.models.list_suite_definitions_response import ListSuiteDefinitionsResponse
from openapi_server.models.list_suite_runs_response import ListSuiteRunsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.start_suite_run_request import StartSuiteRunRequest
from openapi_server.models.start_suite_run_response import StartSuiteRunResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_suite_definition_request import UpdateSuiteDefinitionRequest
from openapi_server.models.update_suite_definition_response import UpdateSuiteDefinitionResponse
from openapi_server import util


async def create_suite_definition(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_suite_definition

    &lt;p&gt;Creates a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;CreateSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSuiteDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_suite_definition(request: web.Request, suite_definition_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_suite_definition

    &lt;p&gt;Deletes a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;DeleteSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

    :param suite_definition_id: Suite definition ID of the test suite to be deleted.
    :type suite_definition_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_endpoint(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, thing_arn=None, certificate_arn=None, device_role_arn=None, authentication_method=None) -> web.Response:
    """get_endpoint

    Gets information about an Device Advisor endpoint.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param thing_arn: The thing ARN of the device. This is an optional parameter.
    :type thing_arn: str
    :param certificate_arn: The certificate ARN of the device. This is an optional parameter.
    :type certificate_arn: str
    :param device_role_arn: The device role ARN of the device. This is an optional parameter.
    :type device_role_arn: str
    :param authentication_method: The authentication method used during the device connection.
    :type authentication_method: str

    """
    return web.Response(status=200)


async def get_suite_definition(request: web.Request, suite_definition_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, suite_definition_version=None) -> web.Response:
    """get_suite_definition

    &lt;p&gt;Gets information about a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

    :param suite_definition_id: Suite definition ID of the test suite to get.
    :type suite_definition_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param suite_definition_version: Suite definition version of the test suite to get.
    :type suite_definition_version: str

    """
    return web.Response(status=200)


async def get_suite_run(request: web.Request, suite_definition_id, suite_run_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_suite_run

    &lt;p&gt;Gets information about a Device Advisor test suite run.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetSuiteRun&lt;/a&gt; action.&lt;/p&gt;

    :param suite_definition_id: Suite definition ID for the test suite run.
    :type suite_definition_id: str
    :param suite_run_id: Suite run ID for the test suite run.
    :type suite_run_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_suite_run_report(request: web.Request, suite_definition_id, suite_run_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_suite_run_report

    &lt;p&gt;Gets a report download link for a successful Device Advisor qualifying test suite run.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetSuiteRunReport&lt;/a&gt; action.&lt;/p&gt;

    :param suite_definition_id: Suite definition ID of the test suite.
    :type suite_definition_id: str
    :param suite_run_id: Suite run ID of the test suite run.
    :type suite_run_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_suite_definitions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_suite_definitions

    &lt;p&gt;Lists the Device Advisor test suites you have created.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListSuiteDefinitions&lt;/a&gt; action.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return at once.
    :type max_results: int
    :param next_token: A token used to get the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_suite_runs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, suite_definition_id=None, suite_definition_version=None, max_results=None, next_token=None) -> web.Response:
    """list_suite_runs

    &lt;p&gt;Lists runs of the specified Device Advisor test suite. You can list all runs of the test suite, or the runs of a specific version of the test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListSuiteRuns&lt;/a&gt; action.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param suite_definition_id: Lists the test suite runs of the specified test suite based on suite definition ID.
    :type suite_definition_id: str
    :param suite_definition_version: Must be passed along with &lt;code&gt;suiteDefinitionId&lt;/code&gt;. Lists the test suite runs of the specified test suite based on suite definition version.
    :type suite_definition_version: str
    :param max_results: The maximum number of results to return at once.
    :type max_results: int
    :param next_token: A token to retrieve the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists the tags attached to an IoT Device Advisor resource.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListTagsForResource&lt;/a&gt; action.&lt;/p&gt;

    :param resource_arn: The resource ARN of the IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def start_suite_run(request: web.Request, suite_definition_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_suite_run

    &lt;p&gt;Starts a Device Advisor test suite run.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;StartSuiteRun&lt;/a&gt; action.&lt;/p&gt;

    :param suite_definition_id: Suite definition ID of the test suite.
    :type suite_definition_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartSuiteRunRequest.from_dict(body)
    return web.Response(status=200)


async def stop_suite_run(request: web.Request, suite_definition_id, suite_run_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_suite_run

    &lt;p&gt;Stops a Device Advisor test suite run that is currently running.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;StopSuiteRun&lt;/a&gt; action.&lt;/p&gt;

    :param suite_definition_id: Suite definition ID of the test suite run to be stopped.
    :type suite_definition_id: str
    :param suite_run_id: Suite run ID of the test suite run to be stopped.
    :type suite_run_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds to and modifies existing tags of an IoT Device Advisor resource.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;TagResource&lt;/a&gt; action.&lt;/p&gt;

    :param resource_arn: The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Removes tags from an IoT Device Advisor resource.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;UntagResource&lt;/a&gt; action.&lt;/p&gt;

    :param resource_arn: The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.
    :type resource_arn: str
    :param tag_keys: List of tag keys to remove from the IoT Device Advisor resource.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_suite_definition(request: web.Request, suite_definition_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_suite_definition

    &lt;p&gt;Updates a Device Advisor test suite.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;UpdateSuiteDefinition&lt;/a&gt; action.&lt;/p&gt;

    :param suite_definition_id: Suite definition ID of the test suite to be updated.
    :type suite_definition_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSuiteDefinitionRequest.from_dict(body)
    return web.Response(status=200)
