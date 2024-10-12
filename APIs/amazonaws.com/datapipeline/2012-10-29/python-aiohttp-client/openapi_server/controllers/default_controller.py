from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_pipeline_input import ActivatePipelineInput
from openapi_server.models.add_tags_input import AddTagsInput
from openapi_server.models.create_pipeline_input import CreatePipelineInput
from openapi_server.models.create_pipeline_output import CreatePipelineOutput
from openapi_server.models.deactivate_pipeline_input import DeactivatePipelineInput
from openapi_server.models.delete_pipeline_input import DeletePipelineInput
from openapi_server.models.describe_objects_input import DescribeObjectsInput
from openapi_server.models.describe_objects_output import DescribeObjectsOutput
from openapi_server.models.describe_pipelines_input import DescribePipelinesInput
from openapi_server.models.describe_pipelines_output import DescribePipelinesOutput
from openapi_server.models.evaluate_expression_input import EvaluateExpressionInput
from openapi_server.models.evaluate_expression_output import EvaluateExpressionOutput
from openapi_server.models.get_pipeline_definition_input import GetPipelineDefinitionInput
from openapi_server.models.get_pipeline_definition_output import GetPipelineDefinitionOutput
from openapi_server.models.list_pipelines_input import ListPipelinesInput
from openapi_server.models.list_pipelines_output import ListPipelinesOutput
from openapi_server.models.poll_for_task_input import PollForTaskInput
from openapi_server.models.poll_for_task_output import PollForTaskOutput
from openapi_server.models.put_pipeline_definition_input import PutPipelineDefinitionInput
from openapi_server.models.put_pipeline_definition_output import PutPipelineDefinitionOutput
from openapi_server.models.query_objects_input import QueryObjectsInput
from openapi_server.models.query_objects_output import QueryObjectsOutput
from openapi_server.models.remove_tags_input import RemoveTagsInput
from openapi_server.models.report_task_progress_input import ReportTaskProgressInput
from openapi_server.models.report_task_progress_output import ReportTaskProgressOutput
from openapi_server.models.report_task_runner_heartbeat_input import ReportTaskRunnerHeartbeatInput
from openapi_server.models.report_task_runner_heartbeat_output import ReportTaskRunnerHeartbeatOutput
from openapi_server.models.set_status_input import SetStatusInput
from openapi_server.models.set_task_status_input import SetTaskStatusInput
from openapi_server.models.validate_pipeline_definition_input import ValidatePipelineDefinitionInput
from openapi_server.models.validate_pipeline_definition_output import ValidatePipelineDefinitionOutput
from openapi_server import util


async def activate_pipeline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """activate_pipeline

    &lt;p&gt;Validates the specified pipeline and starts processing pipeline tasks. If the pipeline does not pass validation, activation fails.&lt;/p&gt; &lt;p&gt;If you need to pause the pipeline to investigate an issue with a component, such as a data source or script, call &lt;a&gt;DeactivatePipeline&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To activate a finished pipeline, modify the end date for the pipeline and then activate it.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ActivatePipelineInput.from_dict(body)
    return web.Response(status=200)


async def add_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags

    Adds or modifies tags for the specified pipeline.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = AddTagsInput.from_dict(body)
    return web.Response(status=200)


async def create_pipeline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_pipeline

    Creates a new, empty pipeline. Use &lt;a&gt;PutPipelineDefinition&lt;/a&gt; to populate the pipeline.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreatePipelineInput.from_dict(body)
    return web.Response(status=200)


async def deactivate_pipeline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deactivate_pipeline

    &lt;p&gt;Deactivates the specified running pipeline. The pipeline is set to the &lt;code&gt;DEACTIVATING&lt;/code&gt; state until the deactivation process completes.&lt;/p&gt; &lt;p&gt;To resume a deactivated pipeline, use &lt;a&gt;ActivatePipeline&lt;/a&gt;. By default, the pipeline resumes from the last completed execution. Optionally, you can specify the date and time to resume the pipeline.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeactivatePipelineInput.from_dict(body)
    return web.Response(status=200)


async def delete_pipeline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_pipeline

    &lt;p&gt;Deletes a pipeline, its pipeline definition, and its run history. AWS Data Pipeline attempts to cancel instances associated with the pipeline that are currently being processed by task runners.&lt;/p&gt; &lt;p&gt;Deleting a pipeline cannot be undone. You cannot query or restore a deleted pipeline. To temporarily pause a pipeline instead of deleting it, call &lt;a&gt;SetStatus&lt;/a&gt; with the status set to &lt;code&gt;PAUSE&lt;/code&gt; on individual components. Components that are paused by &lt;a&gt;SetStatus&lt;/a&gt; can be resumed.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeletePipelineInput.from_dict(body)
    return web.Response(status=200)


async def describe_objects(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None) -> web.Response:
    """describe_objects

    Gets the object definitions for a set of objects associated with the pipeline. Object definitions are composed of a set of fields that define the properties of the object.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param marker: Pagination token
    :type marker: str

    """
    body = DescribeObjectsInput.from_dict(body)
    return web.Response(status=200)


async def describe_pipelines(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_pipelines

    &lt;p&gt;Retrieves metadata about one or more pipelines. The information retrieved includes the name of the pipeline, the pipeline identifier, its current state, and the user account that owns the pipeline. Using account credentials, you can retrieve metadata about pipelines that you or your IAM users have created. If you are using an IAM user account, you can retrieve metadata about only those pipelines for which you have read permissions.&lt;/p&gt; &lt;p&gt;To retrieve the full pipeline definition instead of metadata about the pipeline, call &lt;a&gt;GetPipelineDefinition&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribePipelinesInput.from_dict(body)
    return web.Response(status=200)


async def evaluate_expression(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """evaluate_expression

    Task runners call &lt;code&gt;EvaluateExpression&lt;/code&gt; to evaluate a string in the context of the specified object. For example, a task runner can evaluate SQL queries stored in Amazon S3.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = EvaluateExpressionInput.from_dict(body)
    return web.Response(status=200)


async def get_pipeline_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_pipeline_definition

    Gets the definition of the specified pipeline. You can call &lt;code&gt;GetPipelineDefinition&lt;/code&gt; to retrieve the pipeline definition that you provided using &lt;a&gt;PutPipelineDefinition&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetPipelineDefinitionInput.from_dict(body)
    return web.Response(status=200)


async def list_pipelines(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None) -> web.Response:
    """list_pipelines

    Lists the pipeline identifiers for all active pipelines that you have permission to access.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param marker: Pagination token
    :type marker: str

    """
    body = ListPipelinesInput.from_dict(body)
    return web.Response(status=200)


async def poll_for_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """poll_for_task

    &lt;p&gt;Task runners call &lt;code&gt;PollForTask&lt;/code&gt; to receive a task to perform from AWS Data Pipeline. The task runner specifies which tasks it can perform by setting a value for the &lt;code&gt;workerGroup&lt;/code&gt; parameter. The task returned can come from any of the pipelines that match the &lt;code&gt;workerGroup&lt;/code&gt; value passed in by the task runner and that was launched using the IAM user credentials specified by the task runner.&lt;/p&gt; &lt;p&gt;If tasks are ready in the work queue, &lt;code&gt;PollForTask&lt;/code&gt; returns a response immediately. If no tasks are available in the queue, &lt;code&gt;PollForTask&lt;/code&gt; uses long-polling and holds on to a poll connection for up to a 90 seconds, during which time the first newly scheduled task is handed to the task runner. To accomodate this, set the socket timeout in your task runner to 90 seconds. The task runner should not call &lt;code&gt;PollForTask&lt;/code&gt; again on the same &lt;code&gt;workerGroup&lt;/code&gt; until it receives a response, and this can take up to 90 seconds. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PollForTaskInput.from_dict(body)
    return web.Response(status=200)


async def put_pipeline_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_pipeline_definition

    &lt;p&gt;Adds tasks, schedules, and preconditions to the specified pipeline. You can use &lt;code&gt;PutPipelineDefinition&lt;/code&gt; to populate a new pipeline.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPipelineDefinition&lt;/code&gt; also validates the configuration as it adds it to the pipeline. Changes to the pipeline are saved unless one of the following three validation errors exists in the pipeline. &lt;/p&gt; &lt;ol&gt; &lt;li&gt;An object is missing a name or identifier field.&lt;/li&gt; &lt;li&gt;A string or reference field is empty.&lt;/li&gt; &lt;li&gt;The number of objects in the pipeline exceeds the maximum allowed objects.&lt;/li&gt; &lt;li&gt;The pipeline is in a FINISHED state.&lt;/li&gt; &lt;/ol&gt; &lt;p&gt; Pipeline object definitions are passed to the &lt;code&gt;PutPipelineDefinition&lt;/code&gt; action and returned by the &lt;a&gt;GetPipelineDefinition&lt;/a&gt; action. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = PutPipelineDefinitionInput.from_dict(body)
    return web.Response(status=200)


async def query_objects(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """query_objects

    Queries the specified pipeline for the names of objects that match the specified set of conditions.

    :param x_amz_target: 
    :type x_amz_target: str
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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = QueryObjectsInput.from_dict(body)
    return web.Response(status=200)


async def remove_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_tags

    Removes existing tags from the specified pipeline.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RemoveTagsInput.from_dict(body)
    return web.Response(status=200)


async def report_task_progress(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """report_task_progress

    &lt;p&gt;Task runners call &lt;code&gt;ReportTaskProgress&lt;/code&gt; when assigned a task to acknowledge that it has the task. If the web service does not receive this acknowledgement within 2 minutes, it assigns the task in a subsequent &lt;a&gt;PollForTask&lt;/a&gt; call. After this initial acknowledgement, the task runner only needs to report progress every 15 minutes to maintain its ownership of the task. You can change this reporting time from 15 minutes by specifying a &lt;code&gt;reportProgressTimeout&lt;/code&gt; field in your pipeline.&lt;/p&gt; &lt;p&gt;If a task runner does not report its status after 5 minutes, AWS Data Pipeline assumes that the task runner is unable to process the task and reassigns the task in a subsequent response to &lt;a&gt;PollForTask&lt;/a&gt;. Task runners should call &lt;code&gt;ReportTaskProgress&lt;/code&gt; every 60 seconds.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ReportTaskProgressInput.from_dict(body)
    return web.Response(status=200)


async def report_task_runner_heartbeat(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """report_task_runner_heartbeat

    Task runners call &lt;code&gt;ReportTaskRunnerHeartbeat&lt;/code&gt; every 15 minutes to indicate that they are operational. If the AWS Data Pipeline Task Runner is launched on a resource managed by AWS Data Pipeline, the web service can use this call to detect when the task runner application has failed and restart a new instance.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ReportTaskRunnerHeartbeatInput.from_dict(body)
    return web.Response(status=200)


async def set_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_status

    Requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline. This update might not occur immediately, but is eventually consistent. The status that can be set depends on the type of object (for example, DataNode or Activity). You cannot perform this operation on &lt;code&gt;FINISHED&lt;/code&gt; pipelines and attempting to do so returns &lt;code&gt;InvalidRequestException&lt;/code&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SetStatusInput.from_dict(body)
    return web.Response(status=200)


async def set_task_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_task_status

    Task runners call &lt;code&gt;SetTaskStatus&lt;/code&gt; to notify AWS Data Pipeline that a task is completed and provide information about the final status. A task runner makes this call regardless of whether the task was sucessful. A task runner does not need to call &lt;code&gt;SetTaskStatus&lt;/code&gt; for tasks that are canceled by the web service during a call to &lt;a&gt;ReportTaskProgress&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SetTaskStatusInput.from_dict(body)
    return web.Response(status=200)


async def validate_pipeline_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """validate_pipeline_definition

    Validates the specified pipeline definition to ensure that it is well formed and can be run without error.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ValidatePipelineDefinitionInput.from_dict(body)
    return web.Response(status=200)
