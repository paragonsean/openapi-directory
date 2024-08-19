from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_matching_workflow_output import CreateMatchingWorkflowOutput
from openapi_server.models.create_matching_workflow_request import CreateMatchingWorkflowRequest
from openapi_server.models.create_schema_mapping_output import CreateSchemaMappingOutput
from openapi_server.models.create_schema_mapping_request import CreateSchemaMappingRequest
from openapi_server.models.delete_matching_workflow_output import DeleteMatchingWorkflowOutput
from openapi_server.models.delete_schema_mapping_output import DeleteSchemaMappingOutput
from openapi_server.models.get_match_id_output import GetMatchIdOutput
from openapi_server.models.get_match_id_request import GetMatchIdRequest
from openapi_server.models.get_matching_job_output import GetMatchingJobOutput
from openapi_server.models.get_matching_workflow_output import GetMatchingWorkflowOutput
from openapi_server.models.get_schema_mapping_output import GetSchemaMappingOutput
from openapi_server.models.list_matching_jobs_output import ListMatchingJobsOutput
from openapi_server.models.list_matching_workflows_output import ListMatchingWorkflowsOutput
from openapi_server.models.list_schema_mappings_output import ListSchemaMappingsOutput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.start_matching_job_output import StartMatchingJobOutput
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_matching_workflow_output import UpdateMatchingWorkflowOutput
from openapi_server.models.update_matching_workflow_request import UpdateMatchingWorkflowRequest
from openapi_server import util


async def create_matching_workflow(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_matching_workflow

    Creates a &lt;code&gt;MatchingWorkflow&lt;/code&gt; object which stores the configuration of the data processing job to be run. It is important to note that there should not be a pre-existing &lt;code&gt;MatchingWorkflow&lt;/code&gt; with the same name. To modify an existing workflow, utilize the &lt;code&gt;UpdateMatchingWorkflow&lt;/code&gt; API.

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
    body = CreateMatchingWorkflowRequest.from_dict(body)
    return web.Response(status=200)


async def create_schema_mapping(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_schema_mapping

    Creates a schema mapping, which defines the schema of the input customer records table. The &lt;code&gt;SchemaMapping&lt;/code&gt; also provides Entity Resolution with some metadata about the table, such as the attribute types of the columns and which columns to match on.

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
    body = CreateSchemaMappingRequest.from_dict(body)
    return web.Response(status=200)


async def delete_matching_workflow(request: web.Request, workflow_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_matching_workflow

    Deletes the &lt;code&gt;MatchingWorkflow&lt;/code&gt; with a given name. This operation will succeed even if a workflow with the given name does not exist.

    :param workflow_name: The name of the workflow to be retrieved.
    :type workflow_name: str
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


async def delete_schema_mapping(request: web.Request, schema_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_schema_mapping

    Deletes the &lt;code&gt;SchemaMapping&lt;/code&gt; with a given name. This operation will succeed even if a schema with the given name does not exist. This operation will fail if there is a &lt;code&gt;DataIntegrationWorkflow&lt;/code&gt; object that references the &lt;code&gt;SchemaMapping&lt;/code&gt; in the workflow&#39;s &lt;code&gt;InputSourceConfig&lt;/code&gt;.

    :param schema_name: The name of the schema to delete.
    :type schema_name: str
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


async def get_match_id(request: web.Request, workflow_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_match_id

    Returns the corresponding Match ID of a customer record if the record has been processed.

    :param workflow_name: The name of the workflow.
    :type workflow_name: str
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
    body = GetMatchIdRequest.from_dict(body)
    return web.Response(status=200)


async def get_matching_job(request: web.Request, job_id, workflow_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_matching_job

    Gets the status, metrics, and errors (if there are any) that are associated with a job.

    :param job_id: The ID of the job.
    :type job_id: str
    :param workflow_name: The name of the workflow.
    :type workflow_name: str
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


async def get_matching_workflow(request: web.Request, workflow_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_matching_workflow

    Returns the &lt;code&gt;MatchingWorkflow&lt;/code&gt; with a given name, if it exists.

    :param workflow_name: The name of the workflow.
    :type workflow_name: str
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


async def get_schema_mapping(request: web.Request, schema_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_schema_mapping

    Returns the SchemaMapping of a given name.

    :param schema_name: The name of the schema to be retrieved.
    :type schema_name: str
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


async def list_matching_jobs(request: web.Request, workflow_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_matching_jobs

    Lists all jobs for a given workflow.

    :param workflow_name: The name of the workflow to be retrieved.
    :type workflow_name: str
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
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int
    :param next_token: The pagination token from the previous &lt;code&gt;ListSchemaMappings&lt;/code&gt; API call.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_matching_workflows(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_matching_workflows

    Returns a list of all the &lt;code&gt;MatchingWorkflows&lt;/code&gt; that have been created for an AWS account.

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
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int
    :param next_token: The pagination token from the previous &lt;code&gt;ListSchemaMappings&lt;/code&gt; API call.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_schema_mappings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_schema_mappings

    Returns a list of all the &lt;code&gt;SchemaMappings&lt;/code&gt; that have been created for an AWS account.

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
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int
    :param next_token: The pagination token from the previous &lt;code&gt;ListSchemaMappings&lt;/code&gt; API call.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with an AWS Entity Resolution resource. In Entity Resolution, &lt;code&gt;SchemaMapping&lt;/code&gt;, and &lt;code&gt;MatchingWorkflow&lt;/code&gt; can be tagged.

    :param resource_arn: The ARN of the resource for which you want to view tags.
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


async def start_matching_job(request: web.Request, workflow_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_matching_job

    Starts the &lt;code&gt;MatchingJob&lt;/code&gt; of a workflow. The workflow must have previously been created using the &lt;code&gt;CreateMatchingWorkflow&lt;/code&gt; endpoint.

    :param workflow_name: The name of the matching job to be retrieved.
    :type workflow_name: str
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

    Assigns one or more tags (key-value pairs) to the specified AWS Entity Resolution resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Entity Resolution, &lt;code&gt;SchemaMapping&lt;/code&gt;, and &lt;code&gt;MatchingWorkflow&lt;/code&gt; can be tagged. Tags don&#39;t have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.

    :param resource_arn: The ARN of the resource for which you want to view tags.
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

    Removes one or more tags from the specified AWS Entity Resolution resource. In Entity Resolution, &lt;code&gt;SchemaMapping&lt;/code&gt;, and &lt;code&gt;MatchingWorkflow&lt;/code&gt; can be tagged.

    :param resource_arn: The ARN of the resource for which you want to untag.
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the resource.
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


async def update_matching_workflow(request: web.Request, workflow_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_matching_workflow

    Updates an existing &lt;code&gt;MatchingWorkflow&lt;/code&gt;. This method is identical to &lt;code&gt;CreateMatchingWorkflow&lt;/code&gt;, except it uses an HTTP &lt;code&gt;PUT&lt;/code&gt; request instead of a &lt;code&gt;POST&lt;/code&gt; request, and the &lt;code&gt;MatchingWorkflow&lt;/code&gt; must already exist for the method to succeed.

    :param workflow_name: The name of the workflow to be retrieved.
    :type workflow_name: str
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
    body = UpdateMatchingWorkflowRequest.from_dict(body)
    return web.Response(status=200)
