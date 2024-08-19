from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_task import ActivityTask
from openapi_server.models.activity_task_status import ActivityTaskStatus
from openapi_server.models.activity_type_detail import ActivityTypeDetail
from openapi_server.models.activity_type_infos import ActivityTypeInfos
from openapi_server.models.count_closed_workflow_executions_input import CountClosedWorkflowExecutionsInput
from openapi_server.models.count_open_workflow_executions_input import CountOpenWorkflowExecutionsInput
from openapi_server.models.count_pending_activity_tasks_input import CountPendingActivityTasksInput
from openapi_server.models.count_pending_decision_tasks_input import CountPendingDecisionTasksInput
from openapi_server.models.decision_task import DecisionTask
from openapi_server.models.deprecate_activity_type_input import DeprecateActivityTypeInput
from openapi_server.models.deprecate_domain_input import DeprecateDomainInput
from openapi_server.models.deprecate_workflow_type_input import DeprecateWorkflowTypeInput
from openapi_server.models.describe_activity_type_input import DescribeActivityTypeInput
from openapi_server.models.describe_domain_input import DescribeDomainInput
from openapi_server.models.describe_workflow_execution_input import DescribeWorkflowExecutionInput
from openapi_server.models.describe_workflow_type_input import DescribeWorkflowTypeInput
from openapi_server.models.domain_detail import DomainDetail
from openapi_server.models.domain_infos import DomainInfos
from openapi_server.models.get_workflow_execution_history_input import GetWorkflowExecutionHistoryInput
from openapi_server.models.history import History
from openapi_server.models.list_activity_types_input import ListActivityTypesInput
from openapi_server.models.list_closed_workflow_executions_input import ListClosedWorkflowExecutionsInput
from openapi_server.models.list_domains_input import ListDomainsInput
from openapi_server.models.list_open_workflow_executions_input import ListOpenWorkflowExecutionsInput
from openapi_server.models.list_tags_for_resource_input import ListTagsForResourceInput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.list_workflow_types_input import ListWorkflowTypesInput
from openapi_server.models.pending_task_count import PendingTaskCount
from openapi_server.models.poll_for_activity_task_input import PollForActivityTaskInput
from openapi_server.models.poll_for_decision_task_input import PollForDecisionTaskInput
from openapi_server.models.record_activity_task_heartbeat_input import RecordActivityTaskHeartbeatInput
from openapi_server.models.register_activity_type_input import RegisterActivityTypeInput
from openapi_server.models.register_domain_input import RegisterDomainInput
from openapi_server.models.register_workflow_type_input import RegisterWorkflowTypeInput
from openapi_server.models.request_cancel_workflow_execution_input import RequestCancelWorkflowExecutionInput
from openapi_server.models.respond_activity_task_canceled_input import RespondActivityTaskCanceledInput
from openapi_server.models.respond_activity_task_completed_input import RespondActivityTaskCompletedInput
from openapi_server.models.respond_activity_task_failed_input import RespondActivityTaskFailedInput
from openapi_server.models.respond_decision_task_completed_input import RespondDecisionTaskCompletedInput
from openapi_server.models.run import Run
from openapi_server.models.signal_workflow_execution_input import SignalWorkflowExecutionInput
from openapi_server.models.start_workflow_execution_input import StartWorkflowExecutionInput
from openapi_server.models.tag_resource_input import TagResourceInput
from openapi_server.models.terminate_workflow_execution_input import TerminateWorkflowExecutionInput
from openapi_server.models.undeprecate_activity_type_input import UndeprecateActivityTypeInput
from openapi_server.models.undeprecate_domain_input import UndeprecateDomainInput
from openapi_server.models.undeprecate_workflow_type_input import UndeprecateWorkflowTypeInput
from openapi_server.models.untag_resource_input import UntagResourceInput
from openapi_server.models.workflow_execution_count import WorkflowExecutionCount
from openapi_server.models.workflow_execution_detail import WorkflowExecutionDetail
from openapi_server.models.workflow_execution_infos import WorkflowExecutionInfos
from openapi_server.models.workflow_type_detail import WorkflowTypeDetail
from openapi_server.models.workflow_type_infos import WorkflowTypeInfos
from openapi_server import util


async def count_closed_workflow_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """count_closed_workflow_executions

    &lt;p&gt;Returns the number of closed workflow executions within the given domain that meet the specified filtering criteria.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagFilter.tag&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:tagFilter.tag&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CountClosedWorkflowExecutionsInput.from_dict(body)
    return web.Response(status=200)


async def count_open_workflow_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """count_open_workflow_executions

    &lt;p&gt;Returns the number of open workflow executions within the given domain that meet the specified filtering criteria.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagFilter.tag&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:tagFilter.tag&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CountOpenWorkflowExecutionsInput.from_dict(body)
    return web.Response(status=200)


async def count_pending_activity_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """count_pending_activity_tasks

    &lt;p&gt;Returns the estimated number of activity tasks in the specified task list. The count returned is an approximation and isn&#39;t guaranteed to be exact. If you specify a task list that no activity task was ever scheduled in then &lt;code&gt;0&lt;/code&gt; is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the &lt;code&gt;taskList.name&lt;/code&gt; parameter by using a &lt;code&gt;Condition&lt;/code&gt; element with the &lt;code&gt;swf:taskList.name&lt;/code&gt; key to allow the action to access only certain task lists.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CountPendingActivityTasksInput.from_dict(body)
    return web.Response(status=200)


async def count_pending_decision_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """count_pending_decision_tasks

    &lt;p&gt;Returns the estimated number of decision tasks in the specified task list. The count returned is an approximation and isn&#39;t guaranteed to be exact. If you specify a task list that no decision task was ever scheduled in then &lt;code&gt;0&lt;/code&gt; is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the &lt;code&gt;taskList.name&lt;/code&gt; parameter by using a &lt;code&gt;Condition&lt;/code&gt; element with the &lt;code&gt;swf:taskList.name&lt;/code&gt; key to allow the action to access only certain task lists.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CountPendingDecisionTasksInput.from_dict(body)
    return web.Response(status=200)


async def deprecate_activity_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deprecate_activity_type

    &lt;p&gt;Deprecates the specified &lt;i&gt;activity type&lt;/i&gt;. After an activity type has been deprecated, you cannot create new tasks of that activity type. Tasks of this type that were scheduled before the type was deprecated continue to run.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;activityType.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:activityType.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;activityType.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:activityType.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DeprecateActivityTypeInput.from_dict(body)
    return web.Response(status=200)


async def deprecate_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deprecate_domain

    &lt;p&gt;Deprecates the specified domain. After a domain has been deprecated it cannot be used to create new workflow executions or register new types. However, you can still use visibility actions on this domain. Deprecating a domain also deprecates all activity and workflow types registered in the domain. Executions that were started before the domain was deprecated continues to run.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DeprecateDomainInput.from_dict(body)
    return web.Response(status=200)


async def deprecate_workflow_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deprecate_workflow_type

    &lt;p&gt;Deprecates the specified &lt;i&gt;workflow type&lt;/i&gt;. After a workflow type has been deprecated, you cannot create new executions of that type. Executions that were started before the type was deprecated continues to run. A deprecated workflow type may still be used when calling visibility actions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DeprecateWorkflowTypeInput.from_dict(body)
    return web.Response(status=200)


async def describe_activity_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_activity_type

    &lt;p&gt;Returns information about the specified activity type. This includes configuration settings provided when the type was registered and other general information about the type.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;activityType.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:activityType.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;activityType.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:activityType.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeActivityTypeInput.from_dict(body)
    return web.Response(status=200)


async def describe_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_domain

    &lt;p&gt;Returns information about the specified domain, including description and status.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeDomainInput.from_dict(body)
    return web.Response(status=200)


async def describe_workflow_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workflow_execution

    &lt;p&gt;Returns information about the specified workflow execution including its type and some statistics.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeWorkflowExecutionInput.from_dict(body)
    return web.Response(status=200)


async def describe_workflow_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_workflow_type

    &lt;p&gt;Returns information about the specified &lt;i&gt;workflow type&lt;/i&gt;. This includes configuration settings specified when the type was registered and other information such as creation date, current status, etc.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeWorkflowTypeInput.from_dict(body)
    return web.Response(status=200)


async def get_workflow_execution_history(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maximum_page_size=None, next_page_token=None) -> web.Response:
    """get_workflow_execution_history

    &lt;p&gt;Returns the history of the specified workflow execution. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the &lt;code&gt;nextPageToken&lt;/code&gt; returned by the initial call.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param maximum_page_size: Pagination limit
    :type maximum_page_size: str
    :param next_page_token: Pagination token
    :type next_page_token: str

    """
    body = GetWorkflowExecutionHistoryInput.from_dict(body)
    return web.Response(status=200)


async def list_activity_types(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maximum_page_size=None, next_page_token=None) -> web.Response:
    """list_activity_types

    &lt;p&gt;Returns information about all activities registered in the specified domain that match the specified name and registration status. The result includes information like creation date, current status of the activity, etc. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the &lt;code&gt;nextPageToken&lt;/code&gt; returned by the initial call.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param maximum_page_size: Pagination limit
    :type maximum_page_size: str
    :param next_page_token: Pagination token
    :type next_page_token: str

    """
    body = ListActivityTypesInput.from_dict(body)
    return web.Response(status=200)


async def list_closed_workflow_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maximum_page_size=None, next_page_token=None) -> web.Response:
    """list_closed_workflow_executions

    &lt;p&gt;Returns a list of closed workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagFilter.tag&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:tagFilter.tag&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param maximum_page_size: Pagination limit
    :type maximum_page_size: str
    :param next_page_token: Pagination token
    :type next_page_token: str

    """
    body = ListClosedWorkflowExecutionsInput.from_dict(body)
    return web.Response(status=200)


async def list_domains(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maximum_page_size=None, next_page_token=None) -> web.Response:
    """list_domains

    &lt;p&gt;Returns the list of domains registered in the account. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains. The element must be set to &lt;code&gt;arn:aws:swf::AccountID:domain/*&lt;/code&gt;, where &lt;i&gt;AccountID&lt;/i&gt; is the account ID, with no dashes.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param maximum_page_size: Pagination limit
    :type maximum_page_size: str
    :param next_page_token: Pagination token
    :type next_page_token: str

    """
    body = ListDomainsInput.from_dict(body)
    return web.Response(status=200)


async def list_open_workflow_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maximum_page_size=None, next_page_token=None) -> web.Response:
    """list_open_workflow_executions

    &lt;p&gt;Returns a list of open workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagFilter.tag&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:tagFilter.tag&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;typeFilter.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:typeFilter.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param maximum_page_size: Pagination limit
    :type maximum_page_size: str
    :param next_page_token: Pagination token
    :type next_page_token: str

    """
    body = ListOpenWorkflowExecutionsInput.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    List tags for a given domain.

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


async def list_workflow_types(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maximum_page_size=None, next_page_token=None) -> web.Response:
    """list_workflow_types

    &lt;p&gt;Returns information about workflow types in the specified domain. The results may be split into multiple pages that can be retrieved by making the call repeatedly.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param maximum_page_size: Pagination limit
    :type maximum_page_size: str
    :param next_page_token: Pagination token
    :type next_page_token: str

    """
    body = ListWorkflowTypesInput.from_dict(body)
    return web.Response(status=200)


async def poll_for_activity_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """poll_for_activity_task

    &lt;p&gt;Used by workers to get an &lt;a&gt;ActivityTask&lt;/a&gt; from the specified activity &lt;code&gt;taskList&lt;/code&gt;. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available. The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns an empty result. An empty result, in this context, means that an ActivityTask is returned, but that the value of taskToken is an empty string. If a task is returned, the worker should use its type to identify and process it correctly.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Workers should set their client side socket timeout to at least 70 seconds (10 seconds higher than the maximum time service may hold the poll request).&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the &lt;code&gt;taskList.name&lt;/code&gt; parameter by using a &lt;code&gt;Condition&lt;/code&gt; element with the &lt;code&gt;swf:taskList.name&lt;/code&gt; key to allow the action to access only certain task lists.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = PollForActivityTaskInput.from_dict(body)
    return web.Response(status=200)


async def poll_for_decision_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maximum_page_size=None, next_page_token=None) -> web.Response:
    """poll_for_decision_task

    &lt;p&gt;Used by deciders to get a &lt;a&gt;DecisionTask&lt;/a&gt; from the specified decision &lt;code&gt;taskList&lt;/code&gt;. A decision task may be returned for any open workflow execution that is using the specified task list. The task includes a paginated view of the history of the workflow execution. The decider should use the workflow type and the history to determine how to properly handle the task.&lt;/p&gt; &lt;p&gt;This action initiates a long poll, where the service holds the HTTP connection open and responds as soon a task becomes available. If no decision task is available in the specified task list before the timeout of 60 seconds expires, an empty result is returned. An empty result, in this context, means that a DecisionTask is returned, but that the value of taskToken is an empty string.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Deciders should set their client side socket timeout to at least 70 seconds (10 seconds higher than the timeout).&lt;/p&gt; &lt;/important&gt; &lt;important&gt; &lt;p&gt;Because the number of workflow history events for a single workflow execution might be very large, the result returned might be split up across a number of pages. To retrieve subsequent pages, make additional calls to &lt;code&gt;PollForDecisionTask&lt;/code&gt; using the &lt;code&gt;nextPageToken&lt;/code&gt; returned by the initial call. Note that you do &lt;i&gt;not&lt;/i&gt; call &lt;code&gt;GetWorkflowExecutionHistory&lt;/code&gt; with this &lt;code&gt;nextPageToken&lt;/code&gt;. Instead, call &lt;code&gt;PollForDecisionTask&lt;/code&gt; again.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the &lt;code&gt;taskList.name&lt;/code&gt; parameter by using a &lt;code&gt;Condition&lt;/code&gt; element with the &lt;code&gt;swf:taskList.name&lt;/code&gt; key to allow the action to access only certain task lists.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    :param maximum_page_size: Pagination limit
    :type maximum_page_size: str
    :param next_page_token: Pagination token
    :type next_page_token: str

    """
    body = PollForDecisionTaskInput.from_dict(body)
    return web.Response(status=200)


async def record_activity_task_heartbeat(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """record_activity_task_heartbeat

    &lt;p&gt;Used by activity workers to report to the service that the &lt;a&gt;ActivityTask&lt;/a&gt; represented by the specified &lt;code&gt;taskToken&lt;/code&gt; is still making progress. The worker can also specify details of the progress, for example percent complete, using the &lt;code&gt;details&lt;/code&gt; parameter. This action can also be used by the worker as a mechanism to check if cancellation is being requested for the activity task. If a cancellation is being attempted for the specified task, then the boolean &lt;code&gt;cancelRequested&lt;/code&gt; flag returned by the service is set to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This action resets the &lt;code&gt;taskHeartbeatTimeout&lt;/code&gt; clock. The &lt;code&gt;taskHeartbeatTimeout&lt;/code&gt; is specified in &lt;a&gt;RegisterActivityType&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This action doesn&#39;t in itself create an event in the workflow execution history. However, if the task times out, the workflow execution history contains a &lt;code&gt;ActivityTaskTimedOut&lt;/code&gt; event that contains the information from the last heartbeat generated by the activity worker.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;taskStartToCloseTimeout&lt;/code&gt; of an activity type is the maximum duration of an activity task, regardless of the number of &lt;a&gt;RecordActivityTaskHeartbeat&lt;/a&gt; requests received. The &lt;code&gt;taskStartToCloseTimeout&lt;/code&gt; is also specified in &lt;a&gt;RegisterActivityType&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This operation is only useful for long-lived activities to report liveliness of the task and to determine if a cancellation is being attempted.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;If the &lt;code&gt;cancelRequested&lt;/code&gt; flag returns &lt;code&gt;true&lt;/code&gt;, a cancellation is being attempted. If the worker can cancel the activity, it should respond with &lt;a&gt;RespondActivityTaskCanceled&lt;/a&gt;. Otherwise, it should ignore the cancellation request.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RecordActivityTaskHeartbeatInput.from_dict(body)
    return web.Response(status=200)


async def register_activity_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_activity_type

    &lt;p&gt;Registers a new &lt;i&gt;activity type&lt;/i&gt; along with its configuration settings in the specified domain.&lt;/p&gt; &lt;important&gt; &lt;p&gt;A &lt;code&gt;TypeAlreadyExists&lt;/code&gt; fault is returned if the type already exists in the domain. You cannot change any configuration settings of the type after its registration, and it must be registered as a new version.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;defaultTaskList.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:defaultTaskList.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RegisterActivityTypeInput.from_dict(body)
    return web.Response(status=200)


async def register_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_domain

    &lt;p&gt;Registers a new domain.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to control domain access for this action. The name of the domain being registered is available as the resource of this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RegisterDomainInput.from_dict(body)
    return web.Response(status=200)


async def register_workflow_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_workflow_type

    &lt;p&gt;Registers a new &lt;i&gt;workflow type&lt;/i&gt; and its configuration settings in the specified domain.&lt;/p&gt; &lt;p&gt;The retention period for the workflow history is set by the &lt;a&gt;RegisterDomain&lt;/a&gt; action.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the type already exists, then a &lt;code&gt;TypeAlreadyExists&lt;/code&gt; fault is returned. You cannot change the configuration settings of a workflow type once it is registered and it must be registered as a new version.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;defaultTaskList.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:defaultTaskList.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RegisterWorkflowTypeInput.from_dict(body)
    return web.Response(status=200)


async def request_cancel_workflow_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """request_cancel_workflow_execution

    &lt;p&gt;Records a &lt;code&gt;WorkflowExecutionCancelRequested&lt;/code&gt; event in the currently running workflow execution identified by the given domain, workflowId, and runId. This logically requests the cancellation of the workflow execution as a whole. It is up to the decider to take appropriate actions when it receives an execution history with this event.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the runId isn&#39;t specified, the &lt;code&gt;WorkflowExecutionCancelRequested&lt;/code&gt; event is recorded in the history of the current open workflow execution with the specified workflowId in the domain.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Because this action allows the workflow to properly clean up and gracefully close, it should be used instead of &lt;a&gt;TerminateWorkflowExecution&lt;/a&gt; when possible.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RequestCancelWorkflowExecutionInput.from_dict(body)
    return web.Response(status=200)


async def respond_activity_task_canceled(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """respond_activity_task_canceled

    &lt;p&gt;Used by workers to tell the service that the &lt;a&gt;ActivityTask&lt;/a&gt; identified by the &lt;code&gt;taskToken&lt;/code&gt; was successfully canceled. Additional &lt;code&gt;details&lt;/code&gt; can be provided using the &lt;code&gt;details&lt;/code&gt; argument.&lt;/p&gt; &lt;p&gt;These &lt;code&gt;details&lt;/code&gt; (if provided) appear in the &lt;code&gt;ActivityTaskCanceled&lt;/code&gt; event added to the workflow history.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Only use this operation if the &lt;code&gt;canceled&lt;/code&gt; flag of a &lt;a&gt;RecordActivityTaskHeartbeat&lt;/a&gt; request returns &lt;code&gt;true&lt;/code&gt; and if the activity can be safely undone or abandoned.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to &lt;a&gt;RespondActivityTaskCompleted&lt;/a&gt;, RespondActivityTaskCanceled, &lt;a&gt;RespondActivityTaskFailed&lt;/a&gt;, or the task has &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html#swf-dev-timeout-types\&quot;&gt;timed out&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RespondActivityTaskCanceledInput.from_dict(body)
    return web.Response(status=200)


async def respond_activity_task_completed(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """respond_activity_task_completed

    &lt;p&gt;Used by workers to tell the service that the &lt;a&gt;ActivityTask&lt;/a&gt; identified by the &lt;code&gt;taskToken&lt;/code&gt; completed successfully with a &lt;code&gt;result&lt;/code&gt; (if provided). The &lt;code&gt;result&lt;/code&gt; appears in the &lt;code&gt;ActivityTaskCompleted&lt;/code&gt; event in the workflow history.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the requested task doesn&#39;t complete successfully, use &lt;a&gt;RespondActivityTaskFailed&lt;/a&gt; instead. If the worker finds that the task is canceled through the &lt;code&gt;canceled&lt;/code&gt; flag returned by &lt;a&gt;RecordActivityTaskHeartbeat&lt;/a&gt;, it should cancel the task, clean up and then call &lt;a&gt;RespondActivityTaskCanceled&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to RespondActivityTaskCompleted, &lt;a&gt;RespondActivityTaskCanceled&lt;/a&gt;, &lt;a&gt;RespondActivityTaskFailed&lt;/a&gt;, or the task has &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html#swf-dev-timeout-types\&quot;&gt;timed out&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RespondActivityTaskCompletedInput.from_dict(body)
    return web.Response(status=200)


async def respond_activity_task_failed(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """respond_activity_task_failed

    &lt;p&gt;Used by workers to tell the service that the &lt;a&gt;ActivityTask&lt;/a&gt; identified by the &lt;code&gt;taskToken&lt;/code&gt; has failed with &lt;code&gt;reason&lt;/code&gt; (if specified). The &lt;code&gt;reason&lt;/code&gt; and &lt;code&gt;details&lt;/code&gt; appear in the &lt;code&gt;ActivityTaskFailed&lt;/code&gt; event added to the workflow history.&lt;/p&gt; &lt;p&gt;A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to &lt;a&gt;RespondActivityTaskCompleted&lt;/a&gt;, &lt;a&gt;RespondActivityTaskCanceled&lt;/a&gt;, RespondActivityTaskFailed, or the task has &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html#swf-dev-timeout-types\&quot;&gt;timed out&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RespondActivityTaskFailedInput.from_dict(body)
    return web.Response(status=200)


async def respond_decision_task_completed(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """respond_decision_task_completed

    &lt;p&gt;Used by deciders to tell the service that the &lt;a&gt;DecisionTask&lt;/a&gt; identified by the &lt;code&gt;taskToken&lt;/code&gt; has successfully completed. The &lt;code&gt;decisions&lt;/code&gt; argument specifies the list of decisions made while processing the task.&lt;/p&gt; &lt;p&gt;A &lt;code&gt;DecisionTaskCompleted&lt;/code&gt; event is added to the workflow history. The &lt;code&gt;executionContext&lt;/code&gt; specified is attached to the event in the workflow execution history.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If an IAM policy grants permission to use &lt;code&gt;RespondDecisionTaskCompleted&lt;/code&gt;, it can express permissions for the list of decisions in the &lt;code&gt;decisions&lt;/code&gt; parameter. Each of the decisions has one or more parameters, much like a regular API call. To allow for policies to be as readable as possible, you can express permissions on decisions as if they were actual API calls, including applying conditions to some parameters. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RespondDecisionTaskCompletedInput.from_dict(body)
    return web.Response(status=200)


async def signal_workflow_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """signal_workflow_execution

    &lt;p&gt;Records a &lt;code&gt;WorkflowExecutionSignaled&lt;/code&gt; event in the workflow execution history and creates a decision task for the workflow execution identified by the given domain, workflowId and runId. The event is recorded with the specified user defined signalName and input (if provided).&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a runId isn&#39;t specified, then the &lt;code&gt;WorkflowExecutionSignaled&lt;/code&gt; event is recorded in the history of the current open workflow with the matching workflowId in the domain.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;If the specified workflow execution isn&#39;t open, this method fails with &lt;code&gt;UnknownResource&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = SignalWorkflowExecutionInput.from_dict(body)
    return web.Response(status=200)


async def start_workflow_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_workflow_execution

    &lt;p&gt;Starts an execution of the workflow type in the specified domain using the provided &lt;code&gt;workflowId&lt;/code&gt; and input data.&lt;/p&gt; &lt;p&gt;This action returns the newly started workflow execution.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagList.member.0&lt;/code&gt;: The key is &lt;code&gt;swf:tagList.member.0&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagList.member.1&lt;/code&gt;: The key is &lt;code&gt;swf:tagList.member.1&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagList.member.2&lt;/code&gt;: The key is &lt;code&gt;swf:tagList.member.2&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagList.member.3&lt;/code&gt;: The key is &lt;code&gt;swf:tagList.member.3&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tagList.member.4&lt;/code&gt;: The key is &lt;code&gt;swf:tagList.member.4&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;taskList&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:taskList.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = StartWorkflowExecutionInput.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Add a tag to a Amazon SWF domain.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon SWF supports a maximum of 50 tags per resource.&lt;/p&gt; &lt;/note&gt;

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


async def terminate_workflow_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """terminate_workflow_execution

    &lt;p&gt;Records a &lt;code&gt;WorkflowExecutionTerminated&lt;/code&gt; event and forces closure of the workflow execution identified by the given domain, runId, and workflowId. The child policy, registered with the workflow type or specified when starting this execution, is applied to any open child workflow executions of this workflow execution.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the identified workflow execution was in progress, it is terminated immediately.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;If a runId isn&#39;t specified, then the &lt;code&gt;WorkflowExecutionTerminated&lt;/code&gt; event is recorded in the history of the current open workflow with the matching workflowId in the domain.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;You should consider using &lt;a&gt;RequestCancelWorkflowExecution&lt;/a&gt; action instead because it allows the workflow to gracefully close while &lt;a&gt;TerminateWorkflowExecution&lt;/a&gt; doesn&#39;t.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = TerminateWorkflowExecutionInput.from_dict(body)
    return web.Response(status=200)


async def undeprecate_activity_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """undeprecate_activity_type

    &lt;p&gt;Undeprecates a previously deprecated &lt;i&gt;activity type&lt;/i&gt;. After an activity type has been undeprecated, you can create new tasks of that activity type.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;activityType.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:activityType.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;activityType.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:activityType.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = UndeprecateActivityTypeInput.from_dict(body)
    return web.Response(status=200)


async def undeprecate_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """undeprecate_domain

    &lt;p&gt;Undeprecates a previously deprecated domain. After a domain has been undeprecated it can be used to create new workflow executions or register new types.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use an IAM policy to constrain this action&#39;s parameters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = UndeprecateDomainInput.from_dict(body)
    return web.Response(status=200)


async def undeprecate_workflow_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """undeprecate_workflow_type

    &lt;p&gt;Undeprecates a previously deprecated &lt;i&gt;workflow type&lt;/i&gt;. After a workflow type has been undeprecated, you can create new executions of that type. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Access Control&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use IAM policies to control this action&#39;s access to Amazon SWF resources as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use a &lt;code&gt;Resource&lt;/code&gt; element with the domain name to limit the action to only specified domains.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use an &lt;code&gt;Action&lt;/code&gt; element to allow or deny permission to call this action.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Constrain the following parameters by using a &lt;code&gt;Condition&lt;/code&gt; element with the appropriate keys.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.name&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.name&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;workflowType.version&lt;/code&gt;: String constraint. The key is &lt;code&gt;swf:workflowType.version&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the caller doesn&#39;t have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute&#39;s &lt;code&gt;cause&lt;/code&gt; parameter is set to &lt;code&gt;OPERATION_NOT_PERMITTED&lt;/code&gt;. For details and example IAM policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\&quot;&gt;Using IAM to Manage Access to Amazon SWF Workflows&lt;/a&gt; in the &lt;i&gt;Amazon SWF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = UndeprecateWorkflowTypeInput.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Remove a tag from a Amazon SWF domain.

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
