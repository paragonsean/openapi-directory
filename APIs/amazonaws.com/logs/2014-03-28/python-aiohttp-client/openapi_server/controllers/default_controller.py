from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_kms_key_request import AssociateKmsKeyRequest
from openapi_server.models.cancel_export_task_request import CancelExportTaskRequest
from openapi_server.models.create_export_task_request import CreateExportTaskRequest
from openapi_server.models.create_export_task_response import CreateExportTaskResponse
from openapi_server.models.create_log_group_request import CreateLogGroupRequest
from openapi_server.models.create_log_stream_request import CreateLogStreamRequest
from openapi_server.models.delete_account_policy_request import DeleteAccountPolicyRequest
from openapi_server.models.delete_data_protection_policy_request import DeleteDataProtectionPolicyRequest
from openapi_server.models.delete_destination_request import DeleteDestinationRequest
from openapi_server.models.delete_log_group_request import DeleteLogGroupRequest
from openapi_server.models.delete_log_stream_request import DeleteLogStreamRequest
from openapi_server.models.delete_metric_filter_request import DeleteMetricFilterRequest
from openapi_server.models.delete_query_definition_request import DeleteQueryDefinitionRequest
from openapi_server.models.delete_query_definition_response import DeleteQueryDefinitionResponse
from openapi_server.models.delete_resource_policy_request import DeleteResourcePolicyRequest
from openapi_server.models.delete_retention_policy_request import DeleteRetentionPolicyRequest
from openapi_server.models.delete_subscription_filter_request import DeleteSubscriptionFilterRequest
from openapi_server.models.describe_account_policies_request import DescribeAccountPoliciesRequest
from openapi_server.models.describe_account_policies_response import DescribeAccountPoliciesResponse
from openapi_server.models.describe_destinations_request import DescribeDestinationsRequest
from openapi_server.models.describe_destinations_response import DescribeDestinationsResponse
from openapi_server.models.describe_export_tasks_request import DescribeExportTasksRequest
from openapi_server.models.describe_export_tasks_response import DescribeExportTasksResponse
from openapi_server.models.describe_log_groups_request import DescribeLogGroupsRequest
from openapi_server.models.describe_log_groups_response import DescribeLogGroupsResponse
from openapi_server.models.describe_log_streams_request import DescribeLogStreamsRequest
from openapi_server.models.describe_log_streams_response import DescribeLogStreamsResponse
from openapi_server.models.describe_metric_filters_request import DescribeMetricFiltersRequest
from openapi_server.models.describe_metric_filters_response import DescribeMetricFiltersResponse
from openapi_server.models.describe_queries_request import DescribeQueriesRequest
from openapi_server.models.describe_queries_response import DescribeQueriesResponse
from openapi_server.models.describe_query_definitions_request import DescribeQueryDefinitionsRequest
from openapi_server.models.describe_query_definitions_response import DescribeQueryDefinitionsResponse
from openapi_server.models.describe_resource_policies_request import DescribeResourcePoliciesRequest
from openapi_server.models.describe_resource_policies_response import DescribeResourcePoliciesResponse
from openapi_server.models.describe_subscription_filters_request import DescribeSubscriptionFiltersRequest
from openapi_server.models.describe_subscription_filters_response import DescribeSubscriptionFiltersResponse
from openapi_server.models.disassociate_kms_key_request import DisassociateKmsKeyRequest
from openapi_server.models.filter_log_events_request import FilterLogEventsRequest
from openapi_server.models.filter_log_events_response import FilterLogEventsResponse
from openapi_server.models.get_data_protection_policy_request import GetDataProtectionPolicyRequest
from openapi_server.models.get_data_protection_policy_response import GetDataProtectionPolicyResponse
from openapi_server.models.get_log_events_request import GetLogEventsRequest
from openapi_server.models.get_log_events_response import GetLogEventsResponse
from openapi_server.models.get_log_group_fields_request import GetLogGroupFieldsRequest
from openapi_server.models.get_log_group_fields_response import GetLogGroupFieldsResponse
from openapi_server.models.get_log_record_request import GetLogRecordRequest
from openapi_server.models.get_log_record_response import GetLogRecordResponse
from openapi_server.models.get_query_results_request import GetQueryResultsRequest
from openapi_server.models.get_query_results_response import GetQueryResultsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_tags_log_group_request import ListTagsLogGroupRequest
from openapi_server.models.list_tags_log_group_response import ListTagsLogGroupResponse
from openapi_server.models.put_account_policy_request import PutAccountPolicyRequest
from openapi_server.models.put_account_policy_response import PutAccountPolicyResponse
from openapi_server.models.put_data_protection_policy_request import PutDataProtectionPolicyRequest
from openapi_server.models.put_data_protection_policy_response import PutDataProtectionPolicyResponse
from openapi_server.models.put_destination_policy_request import PutDestinationPolicyRequest
from openapi_server.models.put_destination_request import PutDestinationRequest
from openapi_server.models.put_destination_response import PutDestinationResponse
from openapi_server.models.put_log_events_request import PutLogEventsRequest
from openapi_server.models.put_log_events_response import PutLogEventsResponse
from openapi_server.models.put_metric_filter_request import PutMetricFilterRequest
from openapi_server.models.put_query_definition_request import PutQueryDefinitionRequest
from openapi_server.models.put_query_definition_response import PutQueryDefinitionResponse
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.put_resource_policy_response import PutResourcePolicyResponse
from openapi_server.models.put_retention_policy_request import PutRetentionPolicyRequest
from openapi_server.models.put_subscription_filter_request import PutSubscriptionFilterRequest
from openapi_server.models.start_query_request import StartQueryRequest
from openapi_server.models.start_query_response import StartQueryResponse
from openapi_server.models.stop_query_request import StopQueryRequest
from openapi_server.models.stop_query_response import StopQueryResponse
from openapi_server.models.tag_log_group_request import TagLogGroupRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.test_metric_filter_request import TestMetricFilterRequest
from openapi_server.models.test_metric_filter_response import TestMetricFilterResponse
from openapi_server.models.untag_log_group_request import UntagLogGroupRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server import util


async def associate_kms_key(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_kms_key

    &lt;p&gt;Associates the specified KMS key with either one log group in the account, or with all stored CloudWatch Logs query insights results in the account.&lt;/p&gt; &lt;p&gt;When you use &lt;code&gt;AssociateKmsKey&lt;/code&gt;, you specify either the &lt;code&gt;logGroupName&lt;/code&gt; parameter or the &lt;code&gt;resourceIdentifier&lt;/code&gt; parameter. You can&#39;t specify both of those parameters in the same operation.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Specify the &lt;code&gt;logGroupName&lt;/code&gt; parameter to cause all log events stored in the log group to be encrypted with that key. Only the log events ingested after the key is associated are encrypted with that key.&lt;/p&gt; &lt;p&gt;Associating a KMS key with a log group overrides any existing associations between the log group and a KMS key. After a KMS key is associated with a log group, all newly ingested data for the log group is encrypted using the KMS key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs. This enables CloudWatch Logs to decrypt this data whenever it is requested.&lt;/p&gt; &lt;p&gt;Associating a key with a log group does not cause the results of queries of that log group to be encrypted with that key. To have query results encrypted with a KMS key, you must use an &lt;code&gt;AssociateKmsKey&lt;/code&gt; operation with the &lt;code&gt;resourceIdentifier&lt;/code&gt; parameter that specifies a &lt;code&gt;query-result&lt;/code&gt; resource. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify the &lt;code&gt;resourceIdentifier&lt;/code&gt; parameter with a &lt;code&gt;query-result&lt;/code&gt; resource, to use that key to encrypt the stored results of all future &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html\&quot;&gt;StartQuery&lt;/a&gt; operations in the account. The response from a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html\&quot;&gt;GetQueryResults&lt;/a&gt; operation will still return the query results in plain text.&lt;/p&gt; &lt;p&gt;Even if you have not associated a key with your query results, the query results are encrypted when stored, using the default CloudWatch Logs method.&lt;/p&gt; &lt;p&gt;If you run a query from a monitoring account that queries logs in a source account, the query results key from the monitoring account, if any, is used.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;If you delete the key that is used to encrypt log events or log group query results, then all the associated stored log events or query results that were encrypted with that key will be unencryptable and unusable.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;CloudWatch Logs supports only symmetric KMS keys. Do not use an associate an asymmetric KMS key with your log group or query results. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html\&quot;&gt;Using Symmetric and Asymmetric Keys&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;It can take up to 5 minutes for this operation to take effect.&lt;/p&gt; &lt;p&gt;If you attempt to associate a KMS key with a log group but the KMS key does not exist or the KMS key is disabled, you receive an &lt;code&gt;InvalidParameterException&lt;/code&gt; error. &lt;/p&gt;

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
    body = AssociateKmsKeyRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_export_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_export_task

    &lt;p&gt;Cancels the specified export task.&lt;/p&gt; &lt;p&gt;The task must be in the &lt;code&gt;PENDING&lt;/code&gt; or &lt;code&gt;RUNNING&lt;/code&gt; state.&lt;/p&gt;

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
    body = CancelExportTaskRequest.from_dict(body)
    return web.Response(status=200)


async def create_export_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_export_task

    &lt;p&gt;Creates an export task so that you can efficiently export data from a log group to an Amazon S3 bucket. When you perform a &lt;code&gt;CreateExportTask&lt;/code&gt; operation, you must use credentials that have permission to write to the S3 bucket that you specify as the destination.&lt;/p&gt; &lt;p&gt;Exporting log data to S3 buckets that are encrypted by KMS is supported. Exporting log data to Amazon S3 buckets that have S3 Object Lock enabled with a retention period is also supported.&lt;/p&gt; &lt;p&gt;Exporting to S3 buckets that are encrypted with AES-256 is supported. &lt;/p&gt; &lt;p&gt;This is an asynchronous call. If all the required information is provided, this operation initiates an export task and responds with the ID of the task. After the task has started, you can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.html\&quot;&gt;DescribeExportTasks&lt;/a&gt; to get the status of the export task. Each account can only have one active (&lt;code&gt;RUNNING&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt;) export task at a time. To cancel an export task, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.html\&quot;&gt;CancelExportTask&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can export logs from multiple log groups or multiple time ranges to the same S3 bucket. To separate log data for each export task, specify a prefix to be used as the Amazon S3 key prefix for all exported objects.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Time-based sorting on chunks of log data inside an exported file is not guaranteed. You can sort the exported log field data by using Linux utilities.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateExportTaskRequest.from_dict(body)
    return web.Response(status=200)


async def create_log_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_log_group

    &lt;p&gt;Creates a log group with the specified name. You can create up to 20,000 log groups per account.&lt;/p&gt; &lt;p&gt;You must use the following guidelines when naming a log group:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Log group names must be unique within a Region for an Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Log group names can be between 1 and 512 characters long.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Log group names consist of the following characters: a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (hyphen), &#39;/&#39; (forward slash), &#39;.&#39; (period), and &#39;#&#39; (number sign)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you create a log group, by default the log events in the log group do not expire. To set a retention policy so that events expire and are deleted after a specified time, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.html\&quot;&gt;PutRetentionPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you associate an KMS key with the log group, ingested data is encrypted using the KMS key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs. This enables CloudWatch Logs to decrypt this data whenever it is requested.&lt;/p&gt; &lt;p&gt;If you attempt to associate a KMS key with the log group but the KMS key does not exist or the KMS key is disabled, you receive an &lt;code&gt;InvalidParameterException&lt;/code&gt; error. &lt;/p&gt; &lt;important&gt; &lt;p&gt;CloudWatch Logs supports only symmetric KMS keys. Do not associate an asymmetric KMS key with your log group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html\&quot;&gt;Using Symmetric and Asymmetric Keys&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateLogGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_log_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_log_stream

    &lt;p&gt;Creates a log stream for the specified log group. A log stream is a sequence of log events that originate from a single source, such as an application instance or a resource that is being monitored.&lt;/p&gt; &lt;p&gt;There is no limit on the number of log streams that you can create for a log group. There is a limit of 50 TPS on &lt;code&gt;CreateLogStream&lt;/code&gt; operations, after which transactions are throttled.&lt;/p&gt; &lt;p&gt;You must use the following guidelines when naming a log stream:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Log stream names must be unique within the log group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Log stream names can be between 1 and 512 characters long.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Don&#39;t use &#39;:&#39; (colon) or &#39;*&#39; (asterisk) characters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateLogStreamRequest.from_dict(body)
    return web.Response(status=200)


async def delete_account_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_account_policy

    &lt;p&gt;Deletes a CloudWatch Logs account policy.&lt;/p&gt; &lt;p&gt;To use this operation, you must be signed on with the &lt;code&gt;logs:DeleteDataProtectionPolicy&lt;/code&gt; and &lt;code&gt;logs:DeleteAccountPolicy&lt;/code&gt; permissions.&lt;/p&gt;

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
    body = DeleteAccountPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_data_protection_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_data_protection_policy

    &lt;p&gt;Deletes the data protection policy from the specified log group. &lt;/p&gt; &lt;p&gt;For more information about data protection policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html\&quot;&gt;PutDataProtectionPolicy&lt;/a&gt;.&lt;/p&gt;

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
    body = DeleteDataProtectionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_destination

    Deletes the specified destination, and eventually disables all the subscription filters that publish to it. This operation does not delete the physical resource encapsulated by the destination.

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
    body = DeleteDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_log_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_log_group

    Deletes the specified log group and permanently deletes all the archived log events associated with the log group.

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
    body = DeleteLogGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_log_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_log_stream

    Deletes the specified log stream and permanently deletes all the archived log events associated with the log stream.

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
    body = DeleteLogStreamRequest.from_dict(body)
    return web.Response(status=200)


async def delete_metric_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_metric_filter

    Deletes the specified metric filter.

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
    body = DeleteMetricFilterRequest.from_dict(body)
    return web.Response(status=200)


async def delete_query_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_query_definition

    &lt;p&gt;Deletes a saved CloudWatch Logs Insights query definition. A query definition contains details about a saved CloudWatch Logs Insights query.&lt;/p&gt; &lt;p&gt;Each &lt;code&gt;DeleteQueryDefinition&lt;/code&gt; operation can delete one query definition.&lt;/p&gt; &lt;p&gt;You must have the &lt;code&gt;logs:DeleteQueryDefinition&lt;/code&gt; permission to be able to perform this operation.&lt;/p&gt;

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
    body = DeleteQueryDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

    Deletes a resource policy from this account. This revokes the access of the identities in that policy to put log events to this account.

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
    body = DeleteResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_retention_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_retention_policy

    &lt;p&gt;Deletes the specified retention policy.&lt;/p&gt; &lt;p&gt;Log events do not expire if they belong to log groups without a retention policy.&lt;/p&gt;

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
    body = DeleteRetentionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_subscription_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_subscription_filter

    Deletes the specified subscription filter.

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
    body = DeleteSubscriptionFilterRequest.from_dict(body)
    return web.Response(status=200)


async def describe_account_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account_policies

    Returns a list of all CloudWatch Logs account policies in the account.

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
    body = DescribeAccountPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_destinations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_destinations

    Lists all your destinations. The results are ASCII-sorted by destination name.

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeDestinationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_export_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_export_tasks

    Lists the specified export tasks. You can list all your export tasks or filter the results based on task ID or task status.

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
    body = DescribeExportTasksRequest.from_dict(body)
    return web.Response(status=200)


async def describe_log_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_log_groups

    &lt;p&gt;Lists the specified log groups. You can list all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.&lt;/p&gt; &lt;p&gt;CloudWatch Logs doesn’t support IAM policies that control access to the &lt;code&gt;DescribeLogGroups&lt;/code&gt; action by using the &lt;code&gt;aws:ResourceTag/&lt;i&gt;key-name&lt;/i&gt; &lt;/code&gt; condition key. Other CloudWatch Logs actions do support the use of the &lt;code&gt;aws:ResourceTag/&lt;i&gt;key-name&lt;/i&gt; &lt;/code&gt; condition key to control access. For more information about using tags to control access, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\&quot;&gt;Controlling access to Amazon Web Services resources using tags&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt;

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeLogGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_log_streams(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_log_streams

    &lt;p&gt;Lists the log streams for the specified log group. You can list all the log streams or filter the results by prefix. You can also control how the results are ordered.&lt;/p&gt; &lt;p&gt;You can specify the log group to search by using either &lt;code&gt;logGroupIdentifier&lt;/code&gt; or &lt;code&gt;logGroupName&lt;/code&gt;. You must include one of these two parameters, but you can&#39;t include both. &lt;/p&gt; &lt;p&gt;This operation has a limit of five transactions per second, after which transactions are throttled.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt;

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeLogStreamsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_metric_filters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_metric_filters

    Lists the specified metric filters. You can list all of the metric filters or filter the results by log name, prefix, metric name, or metric namespace. The results are ASCII-sorted by filter name.

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeMetricFiltersRequest.from_dict(body)
    return web.Response(status=200)


async def describe_queries(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_queries

    Returns a list of CloudWatch Logs Insights queries that are scheduled, running, or have been run recently in this account. You can request all queries or limit it to queries of a specific log group or queries with a certain status.

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
    body = DescribeQueriesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_query_definitions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_query_definitions

    &lt;p&gt;This operation returns a paginated list of your saved CloudWatch Logs Insights query definitions.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;queryDefinitionNamePrefix&lt;/code&gt; parameter to limit the results to only the query definitions that have names that start with a certain string.&lt;/p&gt;

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
    body = DescribeQueryDefinitionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_resource_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_resource_policies

    Lists the resource policies in this account.

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
    body = DescribeResourcePoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_subscription_filters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_subscription_filters

    Lists the subscription filters for the specified log group. You can list all the subscription filters or filter the results by prefix. The results are ASCII-sorted by filter name.

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeSubscriptionFiltersRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_kms_key(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_kms_key

    &lt;p&gt;Disassociates the specified KMS key from the specified log group or from all CloudWatch Logs Insights query results in the account.&lt;/p&gt; &lt;p&gt;When you use &lt;code&gt;DisassociateKmsKey&lt;/code&gt;, you specify either the &lt;code&gt;logGroupName&lt;/code&gt; parameter or the &lt;code&gt;resourceIdentifier&lt;/code&gt; parameter. You can&#39;t specify both of those parameters in the same operation.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Specify the &lt;code&gt;logGroupName&lt;/code&gt; parameter to stop using the KMS key to encrypt future log events ingested and stored in the log group. Instead, they will be encrypted with the default CloudWatch Logs method. The log events that were ingested while the key was associated with the log group are still encrypted with that key. Therefore, CloudWatch Logs will need permissions for the key whenever that data is accessed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify the &lt;code&gt;resourceIdentifier&lt;/code&gt; parameter with the &lt;code&gt;query-result&lt;/code&gt; resource to stop using the KMS key to encrypt the results of all future &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html\&quot;&gt;StartQuery&lt;/a&gt; operations in the account. They will instead be encrypted with the default CloudWatch Logs method. The results from queries that ran while the key was associated with the account are still encrypted with that key. Therefore, CloudWatch Logs will need permissions for the key whenever that data is accessed.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;It can take up to 5 minutes for this operation to take effect.&lt;/p&gt;

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
    body = DisassociateKmsKeyRequest.from_dict(body)
    return web.Response(status=200)


async def filter_log_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """filter_log_events

    &lt;p&gt;Lists log events from the specified log group. You can list all the log events or filter the results using a filter pattern, a time range, and the name of the log stream.&lt;/p&gt; &lt;p&gt;You must have the &lt;code&gt;logs:FilterLogEvents&lt;/code&gt; permission to perform this operation.&lt;/p&gt; &lt;p&gt;You can specify the log group to search by using either &lt;code&gt;logGroupIdentifier&lt;/code&gt; or &lt;code&gt;logGroupName&lt;/code&gt;. You must include one of these two parameters, but you can&#39;t include both. &lt;/p&gt; &lt;p&gt;By default, this operation returns as many log events as can fit in 1 MB (up to 10,000 log events) or all the events found within the specified time range. If the results include a token, that means there are more log events available. You can get additional results by specifying the token in a subsequent call. This operation can return empty results while there are more log events available through the token.&lt;/p&gt; &lt;p&gt;The returned log events are sorted by event timestamp, the timestamp when the event was ingested by CloudWatch Logs, and the ID of the &lt;code&gt;PutLogEvents&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt;

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = FilterLogEventsRequest.from_dict(body)
    return web.Response(status=200)


async def get_data_protection_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_data_protection_policy

    Returns information about a log group data protection policy.

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
    body = GetDataProtectionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def get_log_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """get_log_events

    &lt;p&gt;Lists log events from the specified log stream. You can list all of the log events or filter using a time range.&lt;/p&gt; &lt;p&gt;By default, this operation returns as many log events as can fit in a response size of 1MB (up to 10,000 log events). You can get additional log events by specifying one of the tokens in a subsequent call. This operation can return empty results while there are more log events available through the token.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can specify the log group to search by using either &lt;code&gt;logGroupIdentifier&lt;/code&gt; or &lt;code&gt;logGroupName&lt;/code&gt;. You must include one of these two parameters, but you can&#39;t include both. &lt;/p&gt;

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetLogEventsRequest.from_dict(body)
    return web.Response(status=200)


async def get_log_group_fields(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_log_group_fields

    &lt;p&gt;Returns a list of the fields that are included in log events in the specified log group. Includes the percentage of log events that contain each field. The search is limited to a time period that you specify.&lt;/p&gt; &lt;p&gt;You can specify the log group to search by using either &lt;code&gt;logGroupIdentifier&lt;/code&gt; or &lt;code&gt;logGroupName&lt;/code&gt;. You must specify one of these parameters, but you can&#39;t specify both. &lt;/p&gt; &lt;p&gt;In the results, fields that start with &lt;code&gt;@&lt;/code&gt; are fields generated by CloudWatch Logs. For example, &lt;code&gt;@timestamp&lt;/code&gt; is the timestamp of each log event. For more information about the fields that are generated by CloudWatch logs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html\&quot;&gt;Supported Logs and Discovered Fields&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The response results are sorted by the frequency percentage, starting with the highest percentage.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt;

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
    body = GetLogGroupFieldsRequest.from_dict(body)
    return web.Response(status=200)


async def get_log_record(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_log_record

    &lt;p&gt;Retrieves all of the fields and values of a single log event. All fields are retrieved, even if the original query that produced the &lt;code&gt;logRecordPointer&lt;/code&gt; retrieved only a subset of fields. Fields are returned as field name/field value pairs.&lt;/p&gt; &lt;p&gt;The full unparsed log event is returned within &lt;code&gt;@message&lt;/code&gt;.&lt;/p&gt;

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
    body = GetLogRecordRequest.from_dict(body)
    return web.Response(status=200)


async def get_query_results(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_query_results

    &lt;p&gt;Returns the results from the specified query.&lt;/p&gt; &lt;p&gt;Only the fields requested in the query are returned, along with a &lt;code&gt;@ptr&lt;/code&gt; field, which is the identifier for the log record. You can use the value of &lt;code&gt;@ptr&lt;/code&gt; in a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.html\&quot;&gt;GetLogRecord&lt;/a&gt; operation to get the full log record.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetQueryResults&lt;/code&gt; does not start running a query. To run a query, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html\&quot;&gt;StartQuery&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the value of the &lt;code&gt;Status&lt;/code&gt; field in the output is &lt;code&gt;Running&lt;/code&gt;, this operation returns only partial results. If you see a value of &lt;code&gt;Scheduled&lt;/code&gt; or &lt;code&gt;Running&lt;/code&gt; for the status, you can retry the operation later to see the final results. &lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account to start queries in linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt;

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
    body = GetQueryResultsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with a CloudWatch Logs resource. Currently, log groups and destinations support tagging.

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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_log_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_log_group

    &lt;important&gt; &lt;p&gt;The ListTagsLogGroup operation is on the path to deprecation. We recommend that you use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt; instead.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Lists the tags for the specified log group.&lt;/p&gt;

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
    body = ListTagsLogGroupRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_policy

    &lt;p&gt;Creates an account-level data protection policy that applies to all log groups in the account. A data protection policy can help safeguard sensitive data that&#39;s ingested by your log groups by auditing and masking the sensitive log data. Each account can have only one account-level policy.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Sensitive data is detected and masked when it is ingested into a log group. When you set a data protection policy, log events ingested into the log groups before that time are not masked.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you use &lt;code&gt;PutAccountPolicy&lt;/code&gt; to create a data protection policy for your whole account, it applies to both existing log groups and all log groups that are created later in this account. The account policy is applied to existing log groups with eventual consistency. It might take up to 5 minutes before sensitive data in existing log groups begins to be masked.&lt;/p&gt; &lt;p&gt;By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the &lt;code&gt;logs:Unmask&lt;/code&gt; permission can use a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html\&quot;&gt;GetLogEvents&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html\&quot;&gt;FilterLogEvents&lt;/a&gt; operation with the &lt;code&gt;unmask&lt;/code&gt; parameter set to &lt;code&gt;true&lt;/code&gt; to view the unmasked log events. Users with the &lt;code&gt;logs:Unmask&lt;/code&gt; can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the &lt;code&gt;unmask&lt;/code&gt; query command.&lt;/p&gt; &lt;p&gt;For more information, including a list of types of data that can be audited and masked, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html\&quot;&gt;Protect sensitive log data with masking&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To use the &lt;code&gt;PutAccountPolicy&lt;/code&gt; operation, you must be signed on with the &lt;code&gt;logs:PutDataProtectionPolicy&lt;/code&gt; and &lt;code&gt;logs:PutAccountPolicy&lt;/code&gt; permissions.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;PutAccountPolicy&lt;/code&gt; operation applies to all log groups in the account. You can also use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html\&quot;&gt;PutDataProtectionPolicy&lt;/a&gt; to create a data protection policy that applies to just one log group. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.&lt;/p&gt;

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
    body = PutAccountPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_data_protection_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_data_protection_policy

    &lt;p&gt;Creates a data protection policy for the specified log group. A data protection policy can help safeguard sensitive data that&#39;s ingested by the log group by auditing and masking the sensitive log data.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Sensitive data is detected and masked when it is ingested into the log group. When you set a data protection policy, log events ingested into the log group before that time are not masked.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the &lt;code&gt;logs:Unmask&lt;/code&gt; permission can use a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html\&quot;&gt;GetLogEvents&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html\&quot;&gt;FilterLogEvents&lt;/a&gt; operation with the &lt;code&gt;unmask&lt;/code&gt; parameter set to &lt;code&gt;true&lt;/code&gt; to view the unmasked log events. Users with the &lt;code&gt;logs:Unmask&lt;/code&gt; can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the &lt;code&gt;unmask&lt;/code&gt; query command.&lt;/p&gt; &lt;p&gt;For more information, including a list of types of data that can be audited and masked, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html\&quot;&gt;Protect sensitive log data with masking&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;PutDataProtectionPolicy&lt;/code&gt; operation applies to only the specified log group. You can also use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html\&quot;&gt;PutAccountPolicy&lt;/a&gt; to create an account-level data protection policy that applies to all log groups in the account, including both existing log groups and log groups that are created level. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.&lt;/p&gt;

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
    body = PutDataProtectionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_destination

    &lt;p&gt;Creates or updates a destination. This operation is used only to create destinations for cross-account subscriptions.&lt;/p&gt; &lt;p&gt;A destination encapsulates a physical resource (such as an Amazon Kinesis stream). With a destination, you can subscribe to a real-time stream of log events for a different account, ingested using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html\&quot;&gt;PutLogEvents&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Through an access policy, a destination controls what is written to it. By default, &lt;code&gt;PutDestination&lt;/code&gt; does not set any access policy with the destination, which means a cross-account user cannot call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.html\&quot;&gt;PutSubscriptionFilter&lt;/a&gt; against this destination. To enable this, the destination owner must call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.html\&quot;&gt;PutDestinationPolicy&lt;/a&gt; after &lt;code&gt;PutDestination&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To perform a &lt;code&gt;PutDestination&lt;/code&gt; operation, you must also have the &lt;code&gt;iam:PassRole&lt;/code&gt; permission.&lt;/p&gt;

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
    body = PutDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def put_destination_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_destination_policy

    Creates or updates an access policy associated with an existing destination. An access policy is an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/policies_overview.html\&quot;&gt;IAM policy document&lt;/a&gt; that is used to authorize claims to register a subscription filter against a given destination.

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
    body = PutDestinationPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_log_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_log_events

    &lt;p&gt;Uploads a batch of log events to the specified log stream.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The sequence token is now ignored in &lt;code&gt;PutLogEvents&lt;/code&gt; actions. &lt;code&gt;PutLogEvents&lt;/code&gt; actions are always accepted and never return &lt;code&gt;InvalidSequenceTokenException&lt;/code&gt; or &lt;code&gt;DataAlreadyAcceptedException&lt;/code&gt; even if the sequence token is not valid. You can use parallel &lt;code&gt;PutLogEvents&lt;/code&gt; actions on the same log stream. &lt;/p&gt; &lt;/important&gt; &lt;p&gt;The batch of events must satisfy the following constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The maximum batch size is 1,048,576 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;None of the log events in the batch can be more than 2 hours in the future.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;None of the log events in the batch can be more than 14 days in the past. Also, none of the log events can be from earlier than the retention period of the log group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The log events in the batch must be in chronological order by their timestamp. The timestamp is the time that the event occurred, expressed as the number of milliseconds after &lt;code&gt;Jan 1, 1970 00:00:00 UTC&lt;/code&gt;. (In Amazon Web Services Tools for PowerShell and the Amazon Web Services SDK for .NET, the timestamp is specified in .NET format: &lt;code&gt;yyyy-mm-ddThh:mm:ss&lt;/code&gt;. For example, &lt;code&gt;2017-09-15T13:45:30&lt;/code&gt;.) &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A batch of log events in a single request cannot span more than 24 hours. Otherwise, the operation fails.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each log event can be no larger than 256 KB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum number of log events in a batch is 10,000.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;important&gt; &lt;p&gt;The quota of five requests per second per log stream has been removed. Instead, &lt;code&gt;PutLogEvents&lt;/code&gt; actions are throttled based on a per-second per-account quota. You can request an increase to the per-second throttling quota by using the Service Quotas service.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If a call to &lt;code&gt;PutLogEvents&lt;/code&gt; returns \&quot;UnrecognizedClientException\&quot; the most likely cause is a non-valid Amazon Web Services access key ID or secret key. &lt;/p&gt;

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
    body = PutLogEventsRequest.from_dict(body)
    return web.Response(status=200)


async def put_metric_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_metric_filter

    &lt;p&gt;Creates or updates a metric filter and associates it with the specified log group. With metric filters, you can configure rules to extract metric data from log events ingested through &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html\&quot;&gt;PutLogEvents&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The maximum number of metric filters that can be associated with a log group is 100.&lt;/p&gt; &lt;p&gt;When you create a metric filter, you can also optionally assign a unit and dimensions to the metric that is created.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as &lt;code&gt;IPAddress&lt;/code&gt; or &lt;code&gt;requestID&lt;/code&gt; as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric. &lt;/p&gt; &lt;p&gt;CloudWatch Logs disables a metric filter if it generates 1,000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges.&lt;/p&gt; &lt;p&gt;You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html\&quot;&gt; Creating a Billing Alarm to Monitor Your Estimated Amazon Web Services Charges&lt;/a&gt;. &lt;/p&gt; &lt;/important&gt;

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
    body = PutMetricFilterRequest.from_dict(body)
    return web.Response(status=200)


async def put_query_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_query_definition

    &lt;p&gt;Creates or updates a query definition for CloudWatch Logs Insights. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html\&quot;&gt;Analyzing Log Data with CloudWatch Logs Insights&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To update a query definition, specify its &lt;code&gt;queryDefinitionId&lt;/code&gt; in your request. The values of &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;queryString&lt;/code&gt;, and &lt;code&gt;logGroupNames&lt;/code&gt; are changed to the values that you specify in your update operation. No current values are retained from the current query definition. For example, imagine updating a current query definition that includes log groups. If you don&#39;t specify the &lt;code&gt;logGroupNames&lt;/code&gt; parameter in your update operation, the query definition changes to contain no log groups.&lt;/p&gt; &lt;p&gt;You must have the &lt;code&gt;logs:PutQueryDefinition&lt;/code&gt; permission to be able to perform this operation.&lt;/p&gt;

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
    body = PutQueryDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def put_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

    Creates or updates a resource policy allowing other Amazon Web Services services to put log events to this account, such as Amazon Route 53. An account can have up to 10 resource policies per Amazon Web Services Region.

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
    body = PutResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_retention_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_retention_policy

    &lt;p&gt;Sets the retention of the specified log group. With a retention policy, you can configure the number of days for which to retain log events in the specified log group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;CloudWatch Logs doesn’t immediately delete log events when they reach their retention setting. It typically takes up to 72 hours after that before log events are deleted, but in rare situations might take longer.&lt;/p&gt; &lt;p&gt;To illustrate, imagine that you change a log group to have a longer retention setting when it contains log events that are past the expiration date, but haven’t been deleted. Those log events will take up to 72 hours to be deleted after the new retention date is reached. To make sure that log data is deleted permanently, keep a log group at its lower retention setting until 72 hours after the previous retention period ends. Alternatively, wait to change the retention setting until you confirm that the earlier log events are deleted. &lt;/p&gt; &lt;/note&gt;

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
    body = PutRetentionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_subscription_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_subscription_filter

    &lt;p&gt;Creates or updates a subscription filter and associates it with the specified log group. With subscription filters, you can subscribe to a real-time stream of log events ingested through &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html\&quot;&gt;PutLogEvents&lt;/a&gt; and have them delivered to a specific destination. When log events are sent to the receiving service, they are Base64 encoded and compressed with the GZIP format.&lt;/p&gt; &lt;p&gt;The following destinations are supported for subscription filters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A logical destination created with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html\&quot;&gt;PutDestination&lt;/a&gt; that belongs to a different account, for cross-account delivery. We currently support Kinesis Data Streams and Kinesis Data Firehose as logical destinations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An Amazon Kinesis Data Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An Lambda function that belongs to the same account as the subscription filter, for same-account delivery.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Each log group can have up to two subscription filters associated with it. If you are updating an existing filter, you must specify the correct name in &lt;code&gt;filterName&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To perform a &lt;code&gt;PutSubscriptionFilter&lt;/code&gt; operation for any destination except a Lambda function, you must also have the &lt;code&gt;iam:PassRole&lt;/code&gt; permission.&lt;/p&gt;

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
    body = PutSubscriptionFilterRequest.from_dict(body)
    return web.Response(status=200)


async def start_query(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_query

    &lt;p&gt;Schedules a query of a log group using CloudWatch Logs Insights. You specify the log group and time range to query and the query string to use.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html\&quot;&gt;CloudWatch Logs Insights Query Syntax&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you run a query using &lt;code&gt;StartQuery&lt;/code&gt;, the query results are stored by CloudWatch Logs. You can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html\&quot;&gt;GetQueryResults&lt;/a&gt; to retrieve the results of a query, using the &lt;code&gt;queryId&lt;/code&gt; that &lt;code&gt;StartQuery&lt;/code&gt; returns. &lt;/p&gt; &lt;p&gt;If you have associated a KMS key with the query results in this account, then &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html\&quot;&gt;StartQuery&lt;/a&gt; uses that key to encrypt the results when it stores them. If no key is associated with query results, the query results are encrypted with the default CloudWatch Logs encryption method.&lt;/p&gt; &lt;p&gt;Queries time out after 60 minutes of runtime. If your queries are timing out, reduce the time range being searched or partition your query into a number of queries.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account to start a query in a linked source account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;. For a cross-account &lt;code&gt;StartQuery&lt;/code&gt; operation, the query definition must be defined in the monitoring account.&lt;/p&gt; &lt;p&gt;You can have up to 30 concurrent CloudWatch Logs insights queries, including queries that have been added to dashboards. &lt;/p&gt;

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
    body = StartQueryRequest.from_dict(body)
    return web.Response(status=200)


async def stop_query(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_query

    Stops a CloudWatch Logs Insights query that is in progress. If the query has already ended, the operation returns an error indicating that the specified query is not running.

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
    body = StopQueryRequest.from_dict(body)
    return web.Response(status=200)


async def tag_log_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_log_group

    &lt;important&gt; &lt;p&gt;The TagLogGroup operation is on the path to deprecation. We recommend that you use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; instead.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Adds or updates the specified tags for the specified log group.&lt;/p&gt; &lt;p&gt;To list the tags for a log group, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;. To remove tags, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#log-group-tagging\&quot;&gt;Tag Log Groups in Amazon CloudWatch Logs&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch Logs User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;CloudWatch Logs doesn’t support IAM policies that prevent users from assigning specified tags to log groups using the &lt;code&gt;aws:Resource/&lt;i&gt;key-name&lt;/i&gt; &lt;/code&gt; or &lt;code&gt;aws:TagKeys&lt;/code&gt; condition keys. For more information about using tags to control access, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\&quot;&gt;Controlling access to Amazon Web Services resources using tags&lt;/a&gt;.&lt;/p&gt;

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
    body = TagLogGroupRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified CloudWatch Logs resource. Currently, the only CloudWatch Logs resources that can be tagged are log groups and destinations. &lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a CloudWatch Logs resource.&lt;/p&gt;

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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def test_metric_filter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """test_metric_filter

    Tests the filter pattern of a metric filter against a sample of log event messages. You can use this operation to validate the correctness of a metric filter pattern.

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
    body = TestMetricFilterRequest.from_dict(body)
    return web.Response(status=200)


async def untag_log_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_log_group

    &lt;important&gt; &lt;p&gt;The UntagLogGroup operation is on the path to deprecation. We recommend that you use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt; instead.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Removes the specified tags from the specified log group.&lt;/p&gt; &lt;p&gt;To list the tags for a log group, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;. To add tags, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;CloudWatch Logs doesn’t support IAM policies that prevent users from assigning specified tags to log groups using the &lt;code&gt;aws:Resource/&lt;i&gt;key-name&lt;/i&gt; &lt;/code&gt; or &lt;code&gt;aws:TagKeys&lt;/code&gt; condition keys. &lt;/p&gt;

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
    body = UntagLogGroupRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from the specified resource.

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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)
