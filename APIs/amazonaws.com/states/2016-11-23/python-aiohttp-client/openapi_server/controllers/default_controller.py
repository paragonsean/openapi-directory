from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_activity_input import CreateActivityInput
from openapi_server.models.create_activity_output import CreateActivityOutput
from openapi_server.models.create_state_machine_alias_input import CreateStateMachineAliasInput
from openapi_server.models.create_state_machine_alias_output import CreateStateMachineAliasOutput
from openapi_server.models.create_state_machine_input import CreateStateMachineInput
from openapi_server.models.create_state_machine_output import CreateStateMachineOutput
from openapi_server.models.delete_activity_input import DeleteActivityInput
from openapi_server.models.delete_state_machine_alias_input import DeleteStateMachineAliasInput
from openapi_server.models.delete_state_machine_input import DeleteStateMachineInput
from openapi_server.models.delete_state_machine_version_input import DeleteStateMachineVersionInput
from openapi_server.models.describe_activity_input import DescribeActivityInput
from openapi_server.models.describe_activity_output import DescribeActivityOutput
from openapi_server.models.describe_execution_input import DescribeExecutionInput
from openapi_server.models.describe_execution_output import DescribeExecutionOutput
from openapi_server.models.describe_map_run_input import DescribeMapRunInput
from openapi_server.models.describe_map_run_output import DescribeMapRunOutput
from openapi_server.models.describe_state_machine_alias_input import DescribeStateMachineAliasInput
from openapi_server.models.describe_state_machine_alias_output import DescribeStateMachineAliasOutput
from openapi_server.models.describe_state_machine_for_execution_input import DescribeStateMachineForExecutionInput
from openapi_server.models.describe_state_machine_for_execution_output import DescribeStateMachineForExecutionOutput
from openapi_server.models.describe_state_machine_input import DescribeStateMachineInput
from openapi_server.models.describe_state_machine_output import DescribeStateMachineOutput
from openapi_server.models.get_activity_task_input import GetActivityTaskInput
from openapi_server.models.get_activity_task_output import GetActivityTaskOutput
from openapi_server.models.get_execution_history_input import GetExecutionHistoryInput
from openapi_server.models.get_execution_history_output import GetExecutionHistoryOutput
from openapi_server.models.list_activities_input import ListActivitiesInput
from openapi_server.models.list_activities_output import ListActivitiesOutput
from openapi_server.models.list_executions_input import ListExecutionsInput
from openapi_server.models.list_executions_output import ListExecutionsOutput
from openapi_server.models.list_map_runs_input import ListMapRunsInput
from openapi_server.models.list_map_runs_output import ListMapRunsOutput
from openapi_server.models.list_state_machine_aliases_input import ListStateMachineAliasesInput
from openapi_server.models.list_state_machine_aliases_output import ListStateMachineAliasesOutput
from openapi_server.models.list_state_machine_versions_input import ListStateMachineVersionsInput
from openapi_server.models.list_state_machine_versions_output import ListStateMachineVersionsOutput
from openapi_server.models.list_state_machines_input import ListStateMachinesInput
from openapi_server.models.list_state_machines_output import ListStateMachinesOutput
from openapi_server.models.list_tags_for_resource_input import ListTagsForResourceInput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.publish_state_machine_version_input import PublishStateMachineVersionInput
from openapi_server.models.publish_state_machine_version_output import PublishStateMachineVersionOutput
from openapi_server.models.send_task_failure_input import SendTaskFailureInput
from openapi_server.models.send_task_heartbeat_input import SendTaskHeartbeatInput
from openapi_server.models.send_task_success_input import SendTaskSuccessInput
from openapi_server.models.start_execution_input import StartExecutionInput
from openapi_server.models.start_execution_output import StartExecutionOutput
from openapi_server.models.start_sync_execution_input import StartSyncExecutionInput
from openapi_server.models.start_sync_execution_output import StartSyncExecutionOutput
from openapi_server.models.stop_execution_input import StopExecutionInput
from openapi_server.models.stop_execution_output import StopExecutionOutput
from openapi_server.models.tag_resource_input import TagResourceInput
from openapi_server.models.untag_resource_input import UntagResourceInput
from openapi_server.models.update_map_run_input import UpdateMapRunInput
from openapi_server.models.update_state_machine_alias_input import UpdateStateMachineAliasInput
from openapi_server.models.update_state_machine_alias_output import UpdateStateMachineAliasOutput
from openapi_server.models.update_state_machine_input import UpdateStateMachineInput
from openapi_server.models.update_state_machine_output import UpdateStateMachineOutput
from openapi_server import util


async def create_activity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_activity

    &lt;p&gt;Creates an activity. An activity is a task that you write in any programming language and host on any machine that has access to Step Functions. Activities must poll Step Functions using the &lt;code&gt;GetActivityTask&lt;/code&gt; API action and respond using &lt;code&gt;SendTask*&lt;/code&gt; API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;CreateActivity&lt;/code&gt; is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. &lt;code&gt;CreateActivity&lt;/code&gt;&#39;s idempotency check is based on the activity &lt;code&gt;name&lt;/code&gt;. If a following request has different &lt;code&gt;tags&lt;/code&gt; values, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, &lt;code&gt;tags&lt;/code&gt; will not be updated, even if they are different.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateActivityInput.from_dict(body)
    return web.Response(status=200)


async def create_state_machine(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_state_machine

    &lt;p&gt;Creates a state machine. A state machine consists of a collection of states that can do work (&lt;code&gt;Task&lt;/code&gt; states), determine to which states to transition next (&lt;code&gt;Choice&lt;/code&gt; states), stop an execution with an error (&lt;code&gt;Fail&lt;/code&gt; states), and so on. State machines are specified using a JSON-based, structured language. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html\&quot;&gt;Amazon States Language&lt;/a&gt; in the Step Functions User Guide.&lt;/p&gt; &lt;p&gt;If you set the &lt;code&gt;publish&lt;/code&gt; parameter of this API action to &lt;code&gt;true&lt;/code&gt;, it publishes version &lt;code&gt;1&lt;/code&gt; as the first revision of the state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;CreateStateMachine&lt;/code&gt; is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. &lt;code&gt;CreateStateMachine&lt;/code&gt;&#39;s idempotency check is based on the state machine &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;definition&lt;/code&gt;, &lt;code&gt;type&lt;/code&gt;, &lt;code&gt;LoggingConfiguration&lt;/code&gt;, and &lt;code&gt;TracingConfiguration&lt;/code&gt;. The check is also based on the &lt;code&gt;publish&lt;/code&gt; and &lt;code&gt;versionDescription&lt;/code&gt; parameters. If a following request has a different &lt;code&gt;roleArn&lt;/code&gt; or &lt;code&gt;tags&lt;/code&gt;, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, &lt;code&gt;roleArn&lt;/code&gt; and &lt;code&gt;tags&lt;/code&gt; will not be updated, even if they are different.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateStateMachineInput.from_dict(body)
    return web.Response(status=200)


async def create_state_machine_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_state_machine_alias

    &lt;p&gt;Creates an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; for a state machine that points to one or two &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; of the same state machine. You can set your application to call &lt;a&gt;StartExecution&lt;/a&gt; with an alias and update the version the alias uses without changing the client&#39;s code.&lt;/p&gt; &lt;p&gt;You can also map an alias to split &lt;a&gt;StartExecution&lt;/a&gt; requests between two versions of a state machine. To do this, add a second &lt;code&gt;RoutingConfig&lt;/code&gt; object in the &lt;code&gt;routingConfiguration&lt;/code&gt; parameter. You must also specify the percentage of execution run requests each version should receive in both &lt;code&gt;RoutingConfig&lt;/code&gt; objects. Step Functions randomly chooses which version runs a given execution based on the percentage you specify.&lt;/p&gt; &lt;p&gt;To create an alias that points to a single version, specify a single &lt;code&gt;RoutingConfig&lt;/code&gt; object with a &lt;code&gt;weight&lt;/code&gt; set to 100.&lt;/p&gt; &lt;p&gt;You can create up to 100 aliases for each state machine. You must delete unused aliases using the &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; API action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateStateMachineAlias&lt;/code&gt; is an idempotent API. Step Functions bases the idempotency check on the &lt;code&gt;stateMachineArn&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, and &lt;code&gt;routingConfiguration&lt;/code&gt; parameters. Requests that contain the same values for these parameters return a successful idempotent response without creating a duplicate resource.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateStateMachineAliasInput.from_dict(body)
    return web.Response(status=200)


async def delete_activity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_activity

    Deletes an activity.

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
    body = DeleteActivityInput.from_dict(body)
    return web.Response(status=200)


async def delete_state_machine(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_state_machine

    &lt;p&gt;Deletes a state machine. This is an asynchronous operation: It sets the state machine&#39;s status to &lt;code&gt;DELETING&lt;/code&gt; and begins the deletion process. &lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This API action also deletes all &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;aliases&lt;/a&gt; associated with a state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For &lt;code&gt;EXPRESS&lt;/code&gt; state machines, the deletion happens eventually (usually in less than a minute). Running executions may emit logs after &lt;code&gt;DeleteStateMachine&lt;/code&gt; API is called.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteStateMachineInput.from_dict(body)
    return web.Response(status=200)


async def delete_state_machine_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_state_machine_alias

    &lt;p&gt;Deletes a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you delete a state machine alias, you can&#39;t use it to start executions. When you delete a state machine alias, Step Functions doesn&#39;t delete the state machine versions that alias references.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DeleteStateMachineAliasInput.from_dict(body)
    return web.Response(status=200)


async def delete_state_machine_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_state_machine_version

    &lt;p&gt;Deletes a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;. After you delete a version, you can&#39;t call &lt;a&gt;StartExecution&lt;/a&gt; using that version&#39;s ARN or use the version with a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Deleting a state machine version won&#39;t terminate its in-progress executions.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete a state machine version currently referenced by one or more aliases. Before you delete a version, you must either delete the aliases or update them to point to another state machine version.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PublishStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineVersions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DeleteStateMachineVersionInput.from_dict(body)
    return web.Response(status=200)


async def describe_activity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_activity

    &lt;p&gt;Describes an activity.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeActivityInput.from_dict(body)
    return web.Response(status=200)


async def describe_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_execution

    &lt;p&gt;Provides information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata. Use this API action to return the Map Run Amazon Resource Name (ARN) if the execution was dispatched by a Map Run.&lt;/p&gt; &lt;p&gt;If you specify a version or alias ARN when you call the &lt;a&gt;StartExecution&lt;/a&gt; API action, &lt;code&gt;DescribeExecution&lt;/code&gt; returns that ARN.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Executions of an &lt;code&gt;EXPRESS&lt;/code&gt; state machinearen&#39;t supported by &lt;code&gt;DescribeExecution&lt;/code&gt; unless a Map Run dispatched them.&lt;/p&gt;

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
    body = DescribeExecutionInput.from_dict(body)
    return web.Response(status=200)


async def describe_map_run(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_map_run

    Provides information about a Map Run&#39;s configuration, progress, and results. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html\&quot;&gt;Examining Map Run&lt;/a&gt; in the &lt;i&gt;Step Functions Developer Guide&lt;/i&gt;.

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
    body = DescribeMapRunInput.from_dict(body)
    return web.Response(status=200)


async def describe_state_machine(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_state_machine

    &lt;p&gt;Provides information about a state machine&#39;s definition, its IAM role Amazon Resource Name (ARN), and configuration.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This API action returns the details for a state machine version if the &lt;code&gt;stateMachineArn&lt;/code&gt; you specify is a state machine version ARN.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeStateMachineInput.from_dict(body)
    return web.Response(status=200)


async def describe_state_machine_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_state_machine_alias

    &lt;p&gt;Returns details about a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeStateMachineAliasInput.from_dict(body)
    return web.Response(status=200)


async def describe_state_machine_for_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_state_machine_for_execution

    &lt;p&gt;Provides information about a state machine&#39;s definition, its execution role ARN, and configuration. If a Map Run dispatched the execution, this action returns the Map Run Amazon Resource Name (ARN) in the response. The state machine returned is the state machine associated with the Map Run.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

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
    body = DescribeStateMachineForExecutionInput.from_dict(body)
    return web.Response(status=200)


async def get_activity_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_activity_task

    &lt;p&gt;Used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available (i.e. an execution of a task of this type is needed.) The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns a &lt;code&gt;taskToken&lt;/code&gt; with a null string.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API action isn&#39;t logged in CloudTrail.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;Workers should set their client side socket timeout to at least 65 seconds (5 seconds higher than the maximum time the service may hold the poll request).&lt;/p&gt; &lt;p&gt;Polling with &lt;code&gt;GetActivityTask&lt;/code&gt; can cause latency in some implementations. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/bp-activity-pollers.html\&quot;&gt;Avoid Latency When Polling for Activity Tasks&lt;/a&gt; in the Step Functions Developer Guide.&lt;/p&gt; &lt;/important&gt;

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
    body = GetActivityTaskInput.from_dict(body)
    return web.Response(status=200)


async def get_execution_history(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_execution_history

    &lt;p&gt;Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the &lt;code&gt;timeStamp&lt;/code&gt; of the events. Use the &lt;code&gt;reverseOrder&lt;/code&gt; parameter to get the latest events first.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetExecutionHistoryInput.from_dict(body)
    return web.Response(status=200)


async def list_activities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_activities

    &lt;p&gt;Lists the existing activities.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListActivitiesInput.from_dict(body)
    return web.Response(status=200)


async def list_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_executions

    &lt;p&gt;Lists all executions of a state machine or a Map Run. You can list all executions related to a state machine by specifying a state machine Amazon Resource Name (ARN), or those related to a Map Run by specifying a Map Run ARN.&lt;/p&gt; &lt;p&gt;You can also provide a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; ARN or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt; ARN to list the executions associated with a specific alias or version.&lt;/p&gt; &lt;p&gt;Results are sorted by time, with the most recent execution first.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListExecutionsInput.from_dict(body)
    return web.Response(status=200)


async def list_map_runs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_map_runs

    Lists all Map Runs that were started by a given state machine execution. Use this API action to obtain Map Run ARNs, and then call &lt;code&gt;DescribeMapRun&lt;/code&gt; to obtain more information, if needed.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListMapRunsInput.from_dict(body)
    return web.Response(status=200)


async def list_state_machine_aliases(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_state_machine_aliases

    &lt;p&gt;Lists &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;aliases&lt;/a&gt; for a specified state machine ARN. Results are sorted by time, with the most recently created aliases listed first. &lt;/p&gt; &lt;p&gt;To list aliases that reference a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;, you can specify the version ARN in the &lt;code&gt;stateMachineArn&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = ListStateMachineAliasesInput.from_dict(body)
    return web.Response(status=200)


async def list_state_machine_versions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_state_machine_versions

    &lt;p&gt;Lists &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;versions&lt;/a&gt; for the specified state machine Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;The results are sorted in descending order of the version creation time.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PublishStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = ListStateMachineVersionsInput.from_dict(body)
    return web.Response(status=200)


async def list_state_machines(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_state_machines

    &lt;p&gt;Lists the existing state machines.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;nextToken&lt;/code&gt; is returned, there are more results available. The value of &lt;code&gt;nextToken&lt;/code&gt; is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an &lt;i&gt;HTTP 400 InvalidToken&lt;/i&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.&lt;/p&gt; &lt;/note&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListStateMachinesInput.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;List tags for a given resource.&lt;/p&gt; &lt;p&gt;Tags may only contain Unicode letters, digits, white space, or these symbols: &lt;code&gt;_ . : / &#x3D; + - @&lt;/code&gt;.&lt;/p&gt;

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
    body = ListTagsForResourceInput.from_dict(body)
    return web.Response(status=200)


async def publish_state_machine_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """publish_state_machine_version

    &lt;p&gt;Creates a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt; from the current revision of a state machine. Use versions to create immutable snapshots of your state machine. You can start executions from versions either directly or with an alias. To create an alias, use &lt;a&gt;CreateStateMachineAlias&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can publish up to 1000 versions for each state machine. You must manually delete unused versions using the &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; API action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PublishStateMachineVersion&lt;/code&gt; is an idempotent API. It doesn&#39;t create a duplicate state machine version if it already exists for the current revision. Step Functions bases &lt;code&gt;PublishStateMachineVersion&lt;/code&gt;&#39;s idempotency check on the &lt;code&gt;stateMachineArn&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, and &lt;code&gt;revisionId&lt;/code&gt; parameters. Requests with the same parameters return a successful idempotent response. If you don&#39;t specify a &lt;code&gt;revisionId&lt;/code&gt;, Step Functions checks for a previously published version of the state machine&#39;s current revision.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineVersion&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineVersions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = PublishStateMachineVersionInput.from_dict(body)
    return web.Response(status=200)


async def send_task_failure(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_task_failure

    Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report that the task identified by the &lt;code&gt;taskToken&lt;/code&gt; failed.

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
    body = SendTaskFailureInput.from_dict(body)
    return web.Response(status=200)


async def send_task_heartbeat(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_task_heartbeat

    &lt;p&gt;Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report to Step Functions that the task represented by the specified &lt;code&gt;taskToken&lt;/code&gt; is still making progress. This action resets the &lt;code&gt;Heartbeat&lt;/code&gt; clock. The &lt;code&gt;Heartbeat&lt;/code&gt; threshold is specified in the state machine&#39;s Amazon States Language definition (&lt;code&gt;HeartbeatSeconds&lt;/code&gt;). This action does not in itself create an event in the execution history. However, if the task times out, the execution history contains an &lt;code&gt;ActivityTimedOut&lt;/code&gt; entry for activities, or a &lt;code&gt;TaskTimedOut&lt;/code&gt; entry for for tasks using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync\&quot;&gt;job run&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Timeout&lt;/code&gt; of a task, defined in the state machine&#39;s Amazon States Language definition, is its maximum allowed duration, regardless of the number of &lt;a&gt;SendTaskHeartbeat&lt;/a&gt; requests received. Use &lt;code&gt;HeartbeatSeconds&lt;/code&gt; to configure the timeout interval for heartbeats.&lt;/p&gt; &lt;/note&gt;

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
    body = SendTaskHeartbeatInput.from_dict(body)
    return web.Response(status=200)


async def send_task_success(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_task_success

    Used by activity workers and task states using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token\&quot;&gt;callback&lt;/a&gt; pattern to report that the task identified by the &lt;code&gt;taskToken&lt;/code&gt; completed successfully.

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
    body = SendTaskSuccessInput.from_dict(body)
    return web.Response(status=200)


async def start_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_execution

    &lt;p&gt;Starts a state machine execution.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you start an execution with an unqualified state machine ARN, Step Functions uses the latest revision of the state machine for the execution.&lt;/p&gt; &lt;p&gt;To start executions of a state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;, call &lt;code&gt;StartExecution&lt;/code&gt; and provide the version ARN or the ARN of an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; that points to the version.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;StartExecution&lt;/code&gt; is idempotent for &lt;code&gt;STANDARD&lt;/code&gt; workflows. For a &lt;code&gt;STANDARD&lt;/code&gt; workflow, if you call &lt;code&gt;StartExecution&lt;/code&gt; with the same name and input as a running execution, the call succeeds and return the same response as the original request. If the execution is closed or if the input is different, it returns a &lt;code&gt;400 ExecutionAlreadyExists&lt;/code&gt; error. You can reuse names after 90 days. &lt;/p&gt; &lt;p&gt; &lt;code&gt;StartExecution&lt;/code&gt; isn&#39;t idempotent for &lt;code&gt;EXPRESS&lt;/code&gt; workflows. &lt;/p&gt; &lt;/note&gt;

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
    body = StartExecutionInput.from_dict(body)
    return web.Response(status=200)


async def start_sync_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_sync_execution

    &lt;p&gt;Starts a Synchronous Express state machine execution. &lt;code&gt;StartSyncExecution&lt;/code&gt; is not available for &lt;code&gt;STANDARD&lt;/code&gt; workflows.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;StartSyncExecution&lt;/code&gt; will return a &lt;code&gt;200 OK&lt;/code&gt; response, even if your execution fails, because the status code in the API response doesn&#39;t reflect function errors. Error codes are reserved for errors that prevent your execution from running, such as permissions errors, limit errors, or issues with your state machine code and configuration. &lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This API action isn&#39;t logged in CloudTrail.&lt;/p&gt; &lt;/note&gt;

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
    body = StartSyncExecutionInput.from_dict(body)
    return web.Response(status=200)


async def stop_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_execution

    &lt;p&gt;Stops an execution.&lt;/p&gt; &lt;p&gt;This API action is not supported by &lt;code&gt;EXPRESS&lt;/code&gt; state machines.&lt;/p&gt;

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
    body = StopExecutionInput.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Add a tag to a Step Functions resource.&lt;/p&gt; &lt;p&gt;An array of key-value pairs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Billing and Cost Management User Guide&lt;/i&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html\&quot;&gt;Controlling Access Using IAM Tags&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Tags may only contain Unicode letters, digits, white space, or these symbols: &lt;code&gt;_ . : / &#x3D; + - @&lt;/code&gt;.&lt;/p&gt;

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
    body = TagResourceInput.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Remove a tag from a Step Functions resource

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
    body = UntagResourceInput.from_dict(body)
    return web.Response(status=200)


async def update_map_run(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_map_run

    Updates an in-progress Map Run&#39;s configuration to include changes to the settings that control maximum concurrency and Map Run failure.

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
    body = UpdateMapRunInput.from_dict(body)
    return web.Response(status=200)


async def update_state_machine(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_state_machine

    &lt;p&gt;Updates an existing state machine by modifying its &lt;code&gt;definition&lt;/code&gt;, &lt;code&gt;roleArn&lt;/code&gt;, or &lt;code&gt;loggingConfiguration&lt;/code&gt;. Running executions will continue to use the previous &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. You must include at least one of &lt;code&gt;definition&lt;/code&gt; or &lt;code&gt;roleArn&lt;/code&gt; or you will receive a &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine. For example, the qualified state machine ARN &lt;code&gt;arn:partition:states:region:account-id:stateMachine:stateMachineName/mapStateLabel&lt;/code&gt; refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in the state machine named &lt;code&gt;stateMachineName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;A qualified state machine ARN can either refer to a &lt;i&gt;Distributed Map state&lt;/i&gt; defined within a state machine, a version ARN, or an alias ARN.&lt;/p&gt; &lt;p&gt;The following are some examples of qualified and unqualified state machine ARNs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to a &lt;i&gt;Distributed Map state&lt;/i&gt; with a label &lt;code&gt;mapStateLabel&lt;/code&gt; in a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a &lt;i&gt;Distributed Map state&lt;/i&gt;, the request fails with &lt;code&gt;ValidationException&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following qualified state machine ARN refers to an alias named &lt;code&gt;PROD&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine:PROD&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following unqualified state machine ARN refers to a state machine named &lt;code&gt;myStateMachine&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:&amp;lt;partition&amp;gt;:states:&amp;lt;region&amp;gt;:&amp;lt;account-id&amp;gt;:stateMachine:&amp;lt;myStateMachine&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;After you update your state machine, you can set the &lt;code&gt;publish&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; in the same action to publish a new &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html\&quot;&gt;version&lt;/a&gt;. This way, you can opt-in to strict versioning of your state machine.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Step Functions assigns monotonically increasing integers for state machine versions, starting at version number 1.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;All &lt;code&gt;StartExecution&lt;/code&gt; calls within a few seconds use the updated &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. Executions started immediately after you call &lt;code&gt;UpdateStateMachine&lt;/code&gt; may use the previous state machine &lt;code&gt;definition&lt;/code&gt; and &lt;code&gt;roleArn&lt;/code&gt;. &lt;/p&gt; &lt;/note&gt;

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
    body = UpdateStateMachineInput.from_dict(body)
    return web.Response(status=200)


async def update_state_machine_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_state_machine_alias

    &lt;p&gt;Updates the configuration of an existing state machine &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html\&quot;&gt;alias&lt;/a&gt; by modifying its &lt;code&gt;description&lt;/code&gt; or &lt;code&gt;routingConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You must specify at least one of the &lt;code&gt;description&lt;/code&gt; or &lt;code&gt;routingConfiguration&lt;/code&gt; parameters to update a state machine alias.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;UpdateStateMachineAlias&lt;/code&gt; is an idempotent API. Step Functions bases the idempotency check on the &lt;code&gt;stateMachineAliasArn&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, and &lt;code&gt;routingConfiguration&lt;/code&gt; parameters. Requests with the same parameters return an idempotent response.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. All &lt;a&gt;StartExecution&lt;/a&gt; requests made within a few seconds use the latest alias configuration. Executions started immediately after calling &lt;code&gt;UpdateStateMachineAlias&lt;/code&gt; may use the previous routing configuration.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Related operations:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStateMachineAliases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStateMachineAlias&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UpdateStateMachineAliasInput.from_dict(body)
    return web.Response(status=200)
