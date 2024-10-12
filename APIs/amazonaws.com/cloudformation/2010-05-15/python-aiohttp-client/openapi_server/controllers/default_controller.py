from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_type_input import ActivateTypeInput
from openapi_server.models.activate_type_output import ActivateTypeOutput
from openapi_server.models.batch_describe_type_configurations_input import BatchDescribeTypeConfigurationsInput
from openapi_server.models.batch_describe_type_configurations_output import BatchDescribeTypeConfigurationsOutput
from openapi_server.models.cancel_update_stack_input import CancelUpdateStackInput
from openapi_server.models.capability import Capability
from openapi_server.models.continue_update_rollback_input import ContinueUpdateRollbackInput
from openapi_server.models.create_change_set_input import CreateChangeSetInput
from openapi_server.models.create_change_set_output import CreateChangeSetOutput
from openapi_server.models.create_stack_input import CreateStackInput
from openapi_server.models.create_stack_instances_input import CreateStackInstancesInput
from openapi_server.models.create_stack_instances_output import CreateStackInstancesOutput
from openapi_server.models.create_stack_output import CreateStackOutput
from openapi_server.models.create_stack_set_input import CreateStackSetInput
from openapi_server.models.create_stack_set_output import CreateStackSetOutput
from openapi_server.models.deactivate_type_input import DeactivateTypeInput
from openapi_server.models.delete_change_set_input import DeleteChangeSetInput
from openapi_server.models.delete_stack_input import DeleteStackInput
from openapi_server.models.delete_stack_instances_input import DeleteStackInstancesInput
from openapi_server.models.delete_stack_instances_output import DeleteStackInstancesOutput
from openapi_server.models.delete_stack_set_input import DeleteStackSetInput
from openapi_server.models.deregister_type_input import DeregisterTypeInput
from openapi_server.models.describe_account_limits_input import DescribeAccountLimitsInput
from openapi_server.models.describe_account_limits_output import DescribeAccountLimitsOutput
from openapi_server.models.describe_change_set_hooks_input import DescribeChangeSetHooksInput
from openapi_server.models.describe_change_set_hooks_output import DescribeChangeSetHooksOutput
from openapi_server.models.describe_change_set_input import DescribeChangeSetInput
from openapi_server.models.describe_change_set_output import DescribeChangeSetOutput
from openapi_server.models.describe_organizations_access_input import DescribeOrganizationsAccessInput
from openapi_server.models.describe_organizations_access_output import DescribeOrganizationsAccessOutput
from openapi_server.models.describe_publisher_input import DescribePublisherInput
from openapi_server.models.describe_publisher_output import DescribePublisherOutput
from openapi_server.models.describe_stack_drift_detection_status_input import DescribeStackDriftDetectionStatusInput
from openapi_server.models.describe_stack_drift_detection_status_output import DescribeStackDriftDetectionStatusOutput
from openapi_server.models.describe_stack_events_input import DescribeStackEventsInput
from openapi_server.models.describe_stack_events_output import DescribeStackEventsOutput
from openapi_server.models.describe_stack_instance_input import DescribeStackInstanceInput
from openapi_server.models.describe_stack_instance_output import DescribeStackInstanceOutput
from openapi_server.models.describe_stack_resource_drifts_input import DescribeStackResourceDriftsInput
from openapi_server.models.describe_stack_resource_drifts_output import DescribeStackResourceDriftsOutput
from openapi_server.models.describe_stack_resource_input import DescribeStackResourceInput
from openapi_server.models.describe_stack_resource_output import DescribeStackResourceOutput
from openapi_server.models.describe_stack_resources_input import DescribeStackResourcesInput
from openapi_server.models.describe_stack_resources_output import DescribeStackResourcesOutput
from openapi_server.models.describe_stack_set_input import DescribeStackSetInput
from openapi_server.models.describe_stack_set_operation_input import DescribeStackSetOperationInput
from openapi_server.models.describe_stack_set_operation_output import DescribeStackSetOperationOutput
from openapi_server.models.describe_stack_set_output import DescribeStackSetOutput
from openapi_server.models.describe_stacks_input import DescribeStacksInput
from openapi_server.models.describe_stacks_output import DescribeStacksOutput
from openapi_server.models.describe_type_input import DescribeTypeInput
from openapi_server.models.describe_type_output import DescribeTypeOutput
from openapi_server.models.describe_type_registration_input import DescribeTypeRegistrationInput
from openapi_server.models.describe_type_registration_output import DescribeTypeRegistrationOutput
from openapi_server.models.detect_stack_drift_input import DetectStackDriftInput
from openapi_server.models.detect_stack_drift_output import DetectStackDriftOutput
from openapi_server.models.detect_stack_resource_drift_input import DetectStackResourceDriftInput
from openapi_server.models.detect_stack_resource_drift_output import DetectStackResourceDriftOutput
from openapi_server.models.detect_stack_set_drift_input import DetectStackSetDriftInput
from openapi_server.models.detect_stack_set_drift_output import DetectStackSetDriftOutput
from openapi_server.models.estimate_template_cost_input import EstimateTemplateCostInput
from openapi_server.models.estimate_template_cost_output import EstimateTemplateCostOutput
from openapi_server.models.execute_change_set_input import ExecuteChangeSetInput
from openapi_server.models.get_activate_type_logging_config_parameter import GETActivateTypeLoggingConfigParameter
from openapi_server.models.get_create_change_set_rollback_configuration_parameter import GETCreateChangeSetRollbackConfigurationParameter
from openapi_server.models.get_create_stack_instances_deployment_targets_parameter import GETCreateStackInstancesDeploymentTargetsParameter
from openapi_server.models.get_create_stack_instances_operation_preferences_parameter import GETCreateStackInstancesOperationPreferencesParameter
from openapi_server.models.get_create_stack_set_auto_deployment_parameter import GETCreateStackSetAutoDeploymentParameter
from openapi_server.models.get_create_stack_set_managed_execution_parameter import GETCreateStackSetManagedExecutionParameter
from openapi_server.models.get_get_template_summary_template_summary_config_parameter import GETGetTemplateSummaryTemplateSummaryConfigParameter
from openapi_server.models.get_list_types_filters_parameter import GETListTypesFiltersParameter
from openapi_server.models.get_stack_policy_input import GetStackPolicyInput
from openapi_server.models.get_stack_policy_output import GetStackPolicyOutput
from openapi_server.models.get_template_input import GetTemplateInput
from openapi_server.models.get_template_output import GetTemplateOutput
from openapi_server.models.get_template_summary_input import GetTemplateSummaryInput
from openapi_server.models.get_template_summary_output import GetTemplateSummaryOutput
from openapi_server.models.import_stacks_to_stack_set_input import ImportStacksToStackSetInput
from openapi_server.models.import_stacks_to_stack_set_output import ImportStacksToStackSetOutput
from openapi_server.models.list_change_sets_input import ListChangeSetsInput
from openapi_server.models.list_change_sets_output import ListChangeSetsOutput
from openapi_server.models.list_exports_input import ListExportsInput
from openapi_server.models.list_exports_output import ListExportsOutput
from openapi_server.models.list_imports_input import ListImportsInput
from openapi_server.models.list_imports_output import ListImportsOutput
from openapi_server.models.list_stack_instance_resource_drifts_input import ListStackInstanceResourceDriftsInput
from openapi_server.models.list_stack_instance_resource_drifts_output import ListStackInstanceResourceDriftsOutput
from openapi_server.models.list_stack_instances_input import ListStackInstancesInput
from openapi_server.models.list_stack_instances_output import ListStackInstancesOutput
from openapi_server.models.list_stack_resources_input import ListStackResourcesInput
from openapi_server.models.list_stack_resources_output import ListStackResourcesOutput
from openapi_server.models.list_stack_set_operation_results_input import ListStackSetOperationResultsInput
from openapi_server.models.list_stack_set_operation_results_output import ListStackSetOperationResultsOutput
from openapi_server.models.list_stack_set_operations_input import ListStackSetOperationsInput
from openapi_server.models.list_stack_set_operations_output import ListStackSetOperationsOutput
from openapi_server.models.list_stack_sets_input import ListStackSetsInput
from openapi_server.models.list_stack_sets_output import ListStackSetsOutput
from openapi_server.models.list_stacks_input import ListStacksInput
from openapi_server.models.list_stacks_output import ListStacksOutput
from openapi_server.models.list_type_registrations_input import ListTypeRegistrationsInput
from openapi_server.models.list_type_registrations_output import ListTypeRegistrationsOutput
from openapi_server.models.list_type_versions_input import ListTypeVersionsInput
from openapi_server.models.list_type_versions_output import ListTypeVersionsOutput
from openapi_server.models.list_types_input import ListTypesInput
from openapi_server.models.list_types_output import ListTypesOutput
from openapi_server.models.operation_result_filter import OperationResultFilter
from openapi_server.models.parameter import Parameter
from openapi_server.models.publish_type_input import PublishTypeInput
from openapi_server.models.publish_type_output import PublishTypeOutput
from openapi_server.models.record_handler_progress_input import RecordHandlerProgressInput
from openapi_server.models.register_publisher_input import RegisterPublisherInput
from openapi_server.models.register_publisher_output import RegisterPublisherOutput
from openapi_server.models.register_type_input import RegisterTypeInput
from openapi_server.models.register_type_output import RegisterTypeOutput
from openapi_server.models.resource_to_import import ResourceToImport
from openapi_server.models.rollback_stack_input import RollbackStackInput
from openapi_server.models.rollback_stack_output import RollbackStackOutput
from openapi_server.models.set_stack_policy_input import SetStackPolicyInput
from openapi_server.models.set_type_configuration_input import SetTypeConfigurationInput
from openapi_server.models.set_type_configuration_output import SetTypeConfigurationOutput
from openapi_server.models.set_type_default_version_input import SetTypeDefaultVersionInput
from openapi_server.models.signal_resource_input import SignalResourceInput
from openapi_server.models.stack_instance_filter import StackInstanceFilter
from openapi_server.models.stack_resource_drift_status import StackResourceDriftStatus
from openapi_server.models.stack_status import StackStatus
from openapi_server.models.stop_stack_set_operation_input import StopStackSetOperationInput
from openapi_server.models.tag import Tag
from openapi_server.models.test_type_input import TestTypeInput
from openapi_server.models.test_type_output import TestTypeOutput
from openapi_server.models.type_configuration_identifier import TypeConfigurationIdentifier
from openapi_server.models.update_stack_input import UpdateStackInput
from openapi_server.models.update_stack_instances_input import UpdateStackInstancesInput
from openapi_server.models.update_stack_instances_output import UpdateStackInstancesOutput
from openapi_server.models.update_stack_output import UpdateStackOutput
from openapi_server.models.update_stack_set_input import UpdateStackSetInput
from openapi_server.models.update_stack_set_output import UpdateStackSetOutput
from openapi_server.models.update_termination_protection_input import UpdateTerminationProtectionInput
from openapi_server.models.update_termination_protection_output import UpdateTerminationProtectionOutput
from openapi_server.models.validate_template_input import ValidateTemplateInput
from openapi_server.models.validate_template_output import ValidateTemplateOutput
from openapi_server import util


async def g_et_activate_organizations_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_activate_organizations_access

    Activate trusted access with Organizations. With trusted access between StackSets and Organizations activated, the management account has permissions to create and manage StackSets for your organization.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_activate_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, public_type_arn=None, publisher_id=None, type_name=None, type_name_alias=None, auto_update=None, logging_config=None, execution_role_arn=None, version_bump=None, major_version=None) -> web.Response:
    """g_et_activate_type

    &lt;p&gt;Activates a public third-party extension, making it available for use in stack templates. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html\&quot;&gt;Using public extensions&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Once you have activated a public third-party extension in your account and Region, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html\&quot;&gt;SetTypeConfiguration&lt;/a&gt; to specify configuration properties for the extension. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type: &lt;p&gt;The extension type.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;PublicTypeArn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt;, &lt;code&gt;Type&lt;/code&gt;, and &lt;code&gt;PublisherId&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param public_type_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the public extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;PublicTypeArn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt;, &lt;code&gt;Type&lt;/code&gt;, and &lt;code&gt;PublisherId&lt;/code&gt;.&lt;/p&gt;
    :type public_type_arn: str
    :param publisher_id: &lt;p&gt;The ID of the extension publisher.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;PublicTypeArn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt;, &lt;code&gt;Type&lt;/code&gt;, and &lt;code&gt;PublisherId&lt;/code&gt;.&lt;/p&gt;
    :type publisher_id: str
    :param type_name: &lt;p&gt;The name of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;PublicTypeArn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt;, &lt;code&gt;Type&lt;/code&gt;, and &lt;code&gt;PublisherId&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param type_name_alias: &lt;p&gt;An alias to assign to the public extension, in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.&lt;/p&gt; &lt;p&gt;An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.&lt;/p&gt;
    :type type_name_alias: str
    :param auto_update: &lt;p&gt;Whether to automatically update the extension in this account and Region when a new &lt;i&gt;minor&lt;/i&gt; version is published by the extension publisher. Major versions released by the publisher must be manually updated.&lt;/p&gt; &lt;p&gt;The default is &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;
    :type auto_update: bool
    :param logging_config: Contains logging configuration information for an extension.
    :type logging_config: dict | bytes
    :param execution_role_arn: The name of the IAM execution role to use to activate the extension.
    :type execution_role_arn: str
    :param version_bump: &lt;p&gt;Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of &lt;code&gt;AutoUpdate&lt;/code&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MAJOR&lt;/code&gt;: CloudFormation updates the extension to the newest major version, if one is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MINOR&lt;/code&gt;: CloudFormation updates the extension to the newest minor version, if one is available.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type version_bump: str
    :param major_version: &lt;p&gt;The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available &lt;i&gt;minor&lt;/i&gt; version of the major version selected.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;MajorVersion&lt;/code&gt; or &lt;code&gt;VersionBump&lt;/code&gt;, but not both.&lt;/p&gt;
    :type major_version: int

    """
    logging_config = .from_dict(logging_config)
    return web.Response(status=200)


async def g_et_batch_describe_type_configurations(request: web.Request, type_configuration_identifiers, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_batch_describe_type_configurations

    &lt;p&gt;Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and Region.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt;

    :param type_configuration_identifiers: The list of identifiers for the desired extension configurations.
    :type type_configuration_identifiers: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    type_configuration_identifiers = [TypeConfigurationIdentifier.from_dict(d) for d in type_configuration_identifiers]
    return web.Response(status=200)


async def g_et_cancel_update_stack(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_request_token=None) -> web.Response:
    """g_et_cancel_update_stack

    &lt;p&gt;Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can cancel only stacks that are in the &lt;code&gt;UPDATE_IN_PROGRESS&lt;/code&gt; state.&lt;/p&gt; &lt;/note&gt;

    :param stack_name: &lt;note&gt; &lt;p&gt;If you don&#39;t pass a parameter to &lt;code&gt;StackName&lt;/code&gt;, the API returns a response that describes all resources in the account.&lt;/p&gt; &lt;p&gt;The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:&lt;/p&gt; &lt;p&gt; &lt;code&gt;{ \&quot;Version\&quot;: \&quot;2012-10-17\&quot;, \&quot;Statement\&quot;: [{ \&quot;Effect\&quot;: \&quot;Deny\&quot;, \&quot;Action\&quot;: \&quot;cloudformation:DescribeStacks\&quot;, \&quot;NotResource\&quot;: \&quot;arn:aws:cloudformation:*:*:stack/*/*\&quot; }] }&lt;/code&gt; &lt;/p&gt; &lt;/note&gt; &lt;p&gt;The name or the unique stack ID that&#39;s associated with the stack.&lt;/p&gt;
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param client_request_token: A unique identifier for this &lt;code&gt;CancelUpdateStack&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to cancel an update on a stack with the same name. You might retry &lt;code&gt;CancelUpdateStack&lt;/code&gt; requests to ensure that CloudFormation successfully received them.
    :type client_request_token: str

    """
    return web.Response(status=200)


async def g_et_continue_update_rollback(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, role_arn=None, resources_to_skip=None, client_request_token=None) -> web.Response:
    """g_et_continue_update_rollback

    &lt;p&gt;For a specified stack that&#39;s in the &lt;code&gt;UPDATE_ROLLBACK_FAILED&lt;/code&gt; state, continues rolling it back to the &lt;code&gt;UPDATE_ROLLBACK_COMPLETE&lt;/code&gt; state. Depending on the cause of the failure, you can manually &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed\&quot;&gt; fix the error&lt;/a&gt; and continue the rollback. By continuing the rollback, you can return your stack to a working state (the &lt;code&gt;UPDATE_ROLLBACK_COMPLETE&lt;/code&gt; state), and then try to update the stack again.&lt;/p&gt; &lt;p&gt;A stack goes into the &lt;code&gt;UPDATE_ROLLBACK_FAILED&lt;/code&gt; state when CloudFormation can&#39;t roll back all changes after a failed stack update. For example, you might have a stack that&#39;s rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn&#39;t know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.&lt;/p&gt;

    :param stack_name: &lt;p&gt;The name or the unique ID of the stack that you want to continue rolling back.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Don&#39;t specify the name of a nested stack (a stack that was created by using the &lt;code&gt;AWS::CloudFormation::Stack&lt;/code&gt; resource). Instead, use this operation on the parent stack (the stack that contains the &lt;code&gt;AWS::CloudFormation::Stack&lt;/code&gt; resource).&lt;/p&gt; &lt;/note&gt;
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to roll back the stack. CloudFormation uses the role&#39;s credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don&#39;t have permission to pass it. Ensure that the role grants least permission.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that&#39;s generated from your user credentials.&lt;/p&gt;
    :type role_arn: str
    :param resources_to_skip: &lt;p&gt;A list of the logical IDs of the resources that CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the &lt;code&gt;UPDATE_FAILED&lt;/code&gt; state because a rollback failed. You can&#39;t specify resources that are in the &lt;code&gt;UPDATE_FAILED&lt;/code&gt; state for other reasons, for example, because an update was canceled. To check why a resource update failed, use the &lt;a&gt;DescribeStackResources&lt;/a&gt; action, and view the resource status reason.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Specify this property to skip rolling back resources that CloudFormation can&#39;t successfully roll back. We recommend that you &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed\&quot;&gt; troubleshoot&lt;/a&gt; resources before skipping them. CloudFormation sets the status of the specified resources to &lt;code&gt;UPDATE_COMPLETE&lt;/code&gt; and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don&#39;t, subsequent stack updates might fail, and the stack will become unrecoverable.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.&lt;/p&gt; &lt;p&gt;To skip resources that are part of nested stacks, use the following format: &lt;code&gt;NestedStackName.ResourceLogicalID&lt;/code&gt;. If you want to specify the logical ID of a stack resource (&lt;code&gt;Type: AWS::CloudFormation::Stack&lt;/code&gt;) in the &lt;code&gt;ResourcesToSkip&lt;/code&gt; list, then its corresponding embedded stack must be in one of the following states: &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt;, &lt;code&gt;DELETE_COMPLETE&lt;/code&gt;, or &lt;code&gt;DELETE_FAILED&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Don&#39;t confuse a child stack&#39;s name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html#nested-stacks\&quot;&gt;Using ResourcesToSkip to recover a nested stacks hierarchy&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;
    :type resources_to_skip: List[str]
    :param client_request_token: A unique identifier for this &lt;code&gt;ContinueUpdateRollback&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to continue the rollback to a stack with the same name. You might retry &lt;code&gt;ContinueUpdateRollback&lt;/code&gt; requests to ensure that CloudFormation successfully received them.
    :type client_request_token: str

    """
    return web.Response(status=200)


async def g_et_create_change_set(request: web.Request, stack_name, change_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_body=None, template_url=None, use_previous_template=None, parameters=None, capabilities=None, resource_types=None, role_arn=None, rollback_configuration=None, notification_arns=None, tags=None, client_token=None, description=None, change_set_type=None, resources_to_import=None, include_nested_stacks=None, on_stack_failure=None) -> web.Response:
    """g_et_create_change_set

    &lt;p&gt;Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn&#39;t exist or an existing stack. If you create a change set for a stack that doesn&#39;t exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack&#39;s information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.&lt;/p&gt; &lt;p&gt;To create a change set for a stack that doesn&#39;t exist, for the &lt;code&gt;ChangeSetType&lt;/code&gt; parameter, specify &lt;code&gt;CREATE&lt;/code&gt;. To create a change set for an existing stack, specify &lt;code&gt;UPDATE&lt;/code&gt; for the &lt;code&gt;ChangeSetType&lt;/code&gt; parameter. To create a change set for an import operation, specify &lt;code&gt;IMPORT&lt;/code&gt; for the &lt;code&gt;ChangeSetType&lt;/code&gt; parameter. After the &lt;code&gt;CreateChangeSet&lt;/code&gt; call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the &lt;a&gt;DescribeChangeSet&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;When you are satisfied with the changes the change set will make, execute the change set by using the &lt;a&gt;ExecuteChangeSet&lt;/a&gt; action. CloudFormation doesn&#39;t make changes until you execute the change set.&lt;/p&gt; &lt;p&gt;To create a change set for the entire stack hierarchy, set &lt;code&gt;IncludeNestedStacks&lt;/code&gt; to &lt;code&gt;True&lt;/code&gt;.&lt;/p&gt;

    :param stack_name: The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stack&#39;s information with the information that you submit, such as a modified template or different parameter input values.
    :type stack_name: str
    :param change_set_name: &lt;p&gt;The name of the change set. The name must be unique among all change sets that are associated with the specified stack.&lt;/p&gt; &lt;p&gt;A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and can&#39;t exceed 128 characters.&lt;/p&gt;
    :type change_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_body: &lt;p&gt;A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt;.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that&#39;s located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt;.&lt;/p&gt;
    :type template_url: str
    :param use_previous_template: Whether to reuse the template that&#39;s associated with the stack to create the change set.
    :type use_previous_template: bool
    :param parameters: A list of &lt;code&gt;Parameter&lt;/code&gt; structures that specify input parameters for the change set. For more information, see the &lt;a&gt;Parameter&lt;/a&gt; data type.
    :type parameters: list | bytes
    :param capabilities: &lt;p&gt;In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; and &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.&lt;/p&gt; &lt;p&gt;The following IAM resources require you to specify either the &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; or &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; capability.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources, you can specify either capability.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources with custom names, you &lt;i&gt;must&lt;/i&gt; specify &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify either of these capabilities, CloudFormation returns an &lt;code&gt;InsufficientCapabilities&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html\&quot;&gt; AWS::IAM::AccessKey&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html\&quot;&gt; AWS::IAM::Group&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html\&quot;&gt;AWS::IAM::InstanceProfile&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html\&quot;&gt; AWS::IAM::Policy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html\&quot;&gt; AWS::IAM::Role&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html\&quot;&gt; AWS::IAM::User&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html\&quot;&gt;AWS::IAM::UserToGroupAddition&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities\&quot;&gt;Acknowledging IAM resources in CloudFormation templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_AUTO_EXPAND&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html\&quot;&gt;AWS::Include&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html\&quot;&gt;AWS::Serverless&lt;/a&gt; transforms, which are macros hosted by CloudFormation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This capacity doesn&#39;t apply to creating change sets, and specifying it when creating change sets has no effect.&lt;/p&gt; &lt;p&gt;If you want to create a stack from a stack template that contains macros &lt;i&gt;and&lt;/i&gt; nested stacks, you must create or update the stack directly from the template using the &lt;a&gt;CreateStack&lt;/a&gt; or &lt;a&gt;UpdateStack&lt;/a&gt; action, and specifying this capability.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information about macros, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html\&quot;&gt;Using CloudFormation macros to perform custom processing on templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type capabilities: list | bytes
    :param resource_types: &lt;p&gt;The template resource types that you have permissions to work with if you execute this change set, such as &lt;code&gt;AWS::EC2::Instance&lt;/code&gt;, &lt;code&gt;AWS::EC2::*&lt;/code&gt;, or &lt;code&gt;Custom::MyCustomInstance&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If the list of resource types doesn&#39;t include a resource type that you&#39;re updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for CloudFormation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html\&quot;&gt;Controlling access with Identity and Access Management&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt;
    :type resource_types: List[str]
    :param role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes when executing the change set. CloudFormation uses the role&#39;s credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don&#39;t have permission to pass it. Ensure that the role grants least permission.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.&lt;/p&gt;
    :type role_arn: str
    :param rollback_configuration: The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    :type rollback_configuration: dict | bytes
    :param notification_arns: The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.
    :type notification_arns: List[str]
    :param tags: Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.
    :type tags: list | bytes
    :param client_token: A unique identifier for this &lt;code&gt;CreateChangeSet&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to create another change set with the same name. You might retry &lt;code&gt;CreateChangeSet&lt;/code&gt; requests to ensure that CloudFormation successfully received them.
    :type client_token: str
    :param description: A description to help you identify this change set.
    :type description: str
    :param change_set_type: &lt;p&gt;The type of change set operation. To create a change set for a new stack, specify &lt;code&gt;CREATE&lt;/code&gt;. To create a change set for an existing stack, specify &lt;code&gt;UPDATE&lt;/code&gt;. To create a change set for an import operation, specify &lt;code&gt;IMPORT&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995\&quot;&gt;REVIEW_IN_PROGRESS&lt;/a&gt; state until you execute the change set.&lt;/p&gt; &lt;p&gt;By default, CloudFormation specifies &lt;code&gt;UPDATE&lt;/code&gt;. You can&#39;t use the &lt;code&gt;UPDATE&lt;/code&gt; type to create a change set for a new stack or the &lt;code&gt;CREATE&lt;/code&gt; type to create a change set for an existing stack.&lt;/p&gt;
    :type change_set_type: str
    :param resources_to_import: The resources to import into your stack.
    :type resources_to_import: list | bytes
    :param include_nested_stacks: Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to &lt;code&gt;False&lt;/code&gt;. To include nested sets in a change set, specify &lt;code&gt;True&lt;/code&gt;.
    :type include_nested_stacks: bool
    :param on_stack_failure: &lt;p&gt;Determines what action will be taken if stack creation fails. If this parameter is specified, the &lt;code&gt;DisableRollback&lt;/code&gt; parameter to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html\&quot;&gt;ExecuteChangeSet&lt;/a&gt; API operation must not be specified. This must be one of these values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DELETE&lt;/code&gt; - Deletes the change set if the stack creation fails. This is only valid when the &lt;code&gt;ChangeSetType&lt;/code&gt; parameter is set to &lt;code&gt;CREATE&lt;/code&gt;. If the deletion of the stack fails, the status of the stack is &lt;code&gt;DELETE_FAILED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DO_NOTHING&lt;/code&gt; - if the stack creation fails, do nothing. This is equivalent to specifying &lt;code&gt;true&lt;/code&gt; for the &lt;code&gt;DisableRollback&lt;/code&gt; parameter to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html\&quot;&gt;ExecuteChangeSet&lt;/a&gt; API operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ROLLBACK&lt;/code&gt; - if the stack creation fails, roll back the stack. This is equivalent to specifying &lt;code&gt;false&lt;/code&gt; for the &lt;code&gt;DisableRollback&lt;/code&gt; parameter to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html\&quot;&gt;ExecuteChangeSet&lt;/a&gt; API operation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For nested stacks, when the &lt;code&gt;OnStackFailure&lt;/code&gt; parameter is set to &lt;code&gt;DELETE&lt;/code&gt; for the change set for the parent stack, any failure in a child stack will cause the parent stack creation to fail and all stacks to be deleted.&lt;/p&gt;
    :type on_stack_failure: str

    """
    parameters = [Parameter.from_dict(d) for d in parameters]
    capabilities = [Capability.from_dict(d) for d in capabilities]
    rollback_configuration = .from_dict(rollback_configuration)
    tags = [Tag.from_dict(d) for d in tags]
    resources_to_import = [ResourceToImport.from_dict(d) for d in resources_to_import]
    return web.Response(status=200)


async def g_et_create_stack(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_body=None, template_url=None, parameters=None, disable_rollback=None, rollback_configuration=None, timeout_in_minutes=None, notification_arns=None, capabilities=None, resource_types=None, role_arn=None, on_failure=None, stack_policy_body=None, stack_policy_url=None, tags=None, client_request_token=None, enable_termination_protection=None, retain_except_on_create=None) -> web.Response:
    """g_et_create_stack

    Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the &lt;a&gt;DescribeStacks&lt;/a&gt; operation.

    :param stack_name: &lt;p&gt;The name that&#39;s associated with the stack. The name must be unique in the Region in which you are creating the stack.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetical character and can&#39;t be longer than 128 characters.&lt;/p&gt; &lt;/note&gt;
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_body: &lt;p&gt;Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either the &lt;code&gt;TemplateBody&lt;/code&gt; or the &lt;code&gt;TemplateURL&lt;/code&gt; parameter, but not both.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that&#39;s located in an Amazon S3 bucket or a Systems Manager document. For more information, go to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either the &lt;code&gt;TemplateBody&lt;/code&gt; or the &lt;code&gt;TemplateURL&lt;/code&gt; parameter, but not both.&lt;/p&gt;
    :type template_url: str
    :param parameters: A list of &lt;code&gt;Parameter&lt;/code&gt; structures that specify input parameters for the stack. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html\&quot;&gt;Parameter&lt;/a&gt; data type.
    :type parameters: list | bytes
    :param disable_rollback: &lt;p&gt;Set to &lt;code&gt;true&lt;/code&gt; to disable rollback of the stack if stack creation failed. You can specify either &lt;code&gt;DisableRollback&lt;/code&gt; or &lt;code&gt;OnFailure&lt;/code&gt;, but not both.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type disable_rollback: bool
    :param rollback_configuration: The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    :type rollback_configuration: dict | bytes
    :param timeout_in_minutes: The amount of time that can pass before the stack status becomes CREATE_FAILED; if &lt;code&gt;DisableRollback&lt;/code&gt; is not set or is set to &lt;code&gt;false&lt;/code&gt;, the stack will be rolled back.
    :type timeout_in_minutes: int
    :param notification_arns: The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).
    :type notification_arns: List[str]
    :param capabilities: &lt;p&gt;In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; and &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.&lt;/p&gt; &lt;p&gt;The following IAM resources require you to specify either the &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; or &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; capability.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources, you can specify either capability.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources with custom names, you &lt;i&gt;must&lt;/i&gt; specify &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify either of these capabilities, CloudFormation returns an &lt;code&gt;InsufficientCapabilities&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html\&quot;&gt; AWS::IAM::AccessKey&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html\&quot;&gt; AWS::IAM::Group&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html\&quot;&gt;AWS::IAM::InstanceProfile&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html\&quot;&gt; AWS::IAM::Policy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html\&quot;&gt; AWS::IAM::Role&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html\&quot;&gt; AWS::IAM::User&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html\&quot;&gt;AWS::IAM::UserToGroupAddition&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities\&quot;&gt;Acknowledging IAM Resources in CloudFormation Templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_AUTO_EXPAND&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html\&quot;&gt;AWS::Include&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html\&quot;&gt;AWS::Serverless&lt;/a&gt; transforms, which are macros hosted by CloudFormation.&lt;/p&gt; &lt;p&gt;If you want to create a stack from a stack template that contains macros &lt;i&gt;and&lt;/i&gt; nested stacks, you must create the stack directly from the template using this capability.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You should only create stacks directly from a stack template that contains macros if you know what processing the macro performs.&lt;/p&gt; &lt;p&gt;Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html\&quot;&gt;Using CloudFormation macros to perform custom processing on templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type capabilities: list | bytes
    :param resource_types: &lt;p&gt;The template resource types that you have permissions to work with for this create stack action, such as &lt;code&gt;AWS::EC2::Instance&lt;/code&gt;, &lt;code&gt;AWS::EC2::*&lt;/code&gt;, or &lt;code&gt;Custom::MyCustomInstance&lt;/code&gt;. Use the following syntax to describe template resource types: &lt;code&gt;AWS::*&lt;/code&gt; (for all Amazon Web Services resources), &lt;code&gt;Custom::*&lt;/code&gt; (for all custom resources), &lt;code&gt;Custom::&lt;i&gt;logical_ID&lt;/i&gt; &lt;/code&gt; (for a specific custom resource), &lt;code&gt;AWS::&lt;i&gt;service_name&lt;/i&gt;::*&lt;/code&gt; (for all resources of a particular Amazon Web Services service), and &lt;code&gt;AWS::&lt;i&gt;service_name&lt;/i&gt;::&lt;i&gt;resource_logical_ID&lt;/i&gt; &lt;/code&gt; (for a specific Amazon Web Services resource).&lt;/p&gt; &lt;p&gt;If the list of resource types doesn&#39;t include a resource that you&#39;re creating, the stack creation fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html\&quot;&gt;Controlling Access with Identity and Access Management&lt;/a&gt;.&lt;/p&gt;
    :type resource_types: List[str]
    :param role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to create the stack. CloudFormation uses the role&#39;s credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don&#39;t have permission to pass it. Ensure that the role grants least privilege.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that&#39;s generated from your user credentials.&lt;/p&gt;
    :type role_arn: str
    :param on_failure: &lt;p&gt;Determines what action will be taken if stack creation fails. This must be one of: &lt;code&gt;DO_NOTHING&lt;/code&gt;, &lt;code&gt;ROLLBACK&lt;/code&gt;, or &lt;code&gt;DELETE&lt;/code&gt;. You can specify either &lt;code&gt;OnFailure&lt;/code&gt; or &lt;code&gt;DisableRollback&lt;/code&gt;, but not both.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;ROLLBACK&lt;/code&gt; &lt;/p&gt;
    :type on_failure: str
    :param stack_policy_body: Structure containing the stack policy body. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html\&quot;&gt; Prevent Updates to Stack Resources&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;. You can specify either the &lt;code&gt;StackPolicyBody&lt;/code&gt; or the &lt;code&gt;StackPolicyURL&lt;/code&gt; parameter, but not both.
    :type stack_policy_body: str
    :param stack_policy_url: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. You can specify either the &lt;code&gt;StackPolicyBody&lt;/code&gt; or the &lt;code&gt;StackPolicyURL&lt;/code&gt; parameter, but not both.
    :type stack_policy_url: str
    :param tags: Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.
    :type tags: list | bytes
    :param client_request_token: &lt;p&gt;A unique identifier for this &lt;code&gt;CreateStack&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to create a stack with the same name. You might retry &lt;code&gt;CreateStack&lt;/code&gt; requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a &lt;code&gt;CreateStack&lt;/code&gt; operation with the token &lt;code&gt;token1&lt;/code&gt;, then all the &lt;code&gt;StackEvents&lt;/code&gt; generated by that operation will have &lt;code&gt;ClientRequestToken&lt;/code&gt; set as &lt;code&gt;token1&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format &lt;i&gt;Console-StackOperation-ID&lt;/i&gt;, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: &lt;code&gt;Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002&lt;/code&gt;.&lt;/p&gt;
    :type client_request_token: str
    :param enable_termination_protection: &lt;p&gt;Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html\&quot;&gt;Protecting a Stack From Being Deleted&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;. Termination protection is deactivated on stacks by default.&lt;/p&gt; &lt;p&gt;For &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html\&quot;&gt;nested stacks&lt;/a&gt;, termination protection is set on the root stack and can&#39;t be changed directly on the nested stack.&lt;/p&gt;
    :type enable_termination_protection: bool
    :param retain_except_on_create: This deletion policy deletes newly created resources, but retains existing resources, when a stack operation is rolled back. This ensures new, empty, and unused resources are deleted, while critical resources and their data are retained. &lt;code&gt;RetainExceptOnCreate&lt;/code&gt; can be specified for any resource that supports the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html\&quot;&gt; DeletionPolicy&lt;/a&gt; attribute.
    :type retain_except_on_create: bool

    """
    parameters = [Parameter.from_dict(d) for d in parameters]
    rollback_configuration = .from_dict(rollback_configuration)
    capabilities = [Capability.from_dict(d) for d in capabilities]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_stack_instances(request: web.Request, stack_set_name, regions, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, accounts=None, deployment_targets=None, parameter_overrides=None, operation_preferences=None, operation_id=None, call_as=None) -> web.Response:
    """g_et_create_stack_instances

    Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, and you must specify at least one value for &lt;code&gt;Regions&lt;/code&gt;.

    :param stack_set_name: The name or unique ID of the stack set that you want to create stack instances from.
    :type stack_set_name: str
    :param regions: The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.
    :type regions: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param accounts: &lt;p&gt;[Self-managed permissions] The names of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, but not both.&lt;/p&gt;
    :type accounts: List[str]
    :param deployment_targets: &lt;p&gt;[Service-managed permissions] The Organizations accounts for which to create stack instances in the specified Amazon Web Services Regions.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, but not both.&lt;/p&gt;
    :type deployment_targets: dict | bytes
    :param parameter_overrides: &lt;p&gt;A list of stack set parameters whose values you want to override in the selected stack instances.&lt;/p&gt; &lt;p&gt;Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To override the current value for a parameter, include the parameter and specify its value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To leave an overridden parameter set to its present value, include the parameter and specify &lt;code&gt;UsePreviousValue&lt;/code&gt; as &lt;code&gt;true&lt;/code&gt;. (You can&#39;t specify both a value and set &lt;code&gt;UsePreviousValue&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don&#39;t include the parameter in the list.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To leave all parameters set to their present values, don&#39;t specify this property at all.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;During stack set updates, any parameter values overridden for a stack instance aren&#39;t updated, but retain their overridden value.&lt;/p&gt; &lt;p&gt;You can only override the parameter &lt;i&gt;values&lt;/i&gt; that are specified in the stack set; to add or delete a parameter itself, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html\&quot;&gt;UpdateStackSet&lt;/a&gt; to update the stack set template.&lt;/p&gt;
    :type parameter_overrides: list | bytes
    :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
    :type operation_preferences: dict | bytes
    :param operation_id: &lt;p&gt;The unique identifier for this stack set operation.&lt;/p&gt; &lt;p&gt;The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify an operation ID, the SDK generates one automatically.&lt;/p&gt; &lt;p&gt;Repeating this stack set operation with a new operation ID retries all stack instances whose status is &lt;code&gt;OUTDATED&lt;/code&gt;.&lt;/p&gt;
    :type operation_id: str
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    deployment_targets = .from_dict(deployment_targets)
    parameter_overrides = [Parameter.from_dict(d) for d in parameter_overrides]
    operation_preferences = .from_dict(operation_preferences)
    return web.Response(status=200)


async def g_et_create_stack_set(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None, template_body=None, template_url=None, stack_id=None, parameters=None, capabilities=None, tags=None, administration_role_arn=None, execution_role_name=None, permission_model=None, auto_deployment=None, call_as=None, client_request_token=None, managed_execution=None) -> web.Response:
    """g_et_create_stack_set

    Creates a stack set.

    :param stack_set_name: &lt;p&gt;The name to associate with the stack set. The name must be unique in the Region where you create your stack set.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can&#39;t be longer than 128 characters.&lt;/p&gt; &lt;/note&gt;
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param description: A description of the stack set. You can use the description to identify the stack set&#39;s purpose or other important information.
    :type description: str
    :param template_body: &lt;p&gt;The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that&#39;s located in an Amazon S3 bucket or a Systems Manager document. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.&lt;/p&gt;
    :type template_url: str
    :param stack_id: The stack ID you are importing into a new stack set. Specify the Amazon Resource Name (ARN) of the stack.
    :type stack_id: str
    :param parameters: The input parameters for the stack set template.
    :type parameters: list | bytes
    :param capabilities: &lt;p&gt;In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for CloudFormation to create the stack set and related stack instances.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; and &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities.&lt;/p&gt; &lt;p&gt;The following IAM resources require you to specify either the &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; or &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; capability.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources, you can specify either capability.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources with custom names, you &lt;i&gt;must&lt;/i&gt; specify &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify either of these capabilities, CloudFormation returns an &lt;code&gt;InsufficientCapabilities&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html\&quot;&gt; AWS::IAM::AccessKey&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html\&quot;&gt; AWS::IAM::Group&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html\&quot;&gt;AWS::IAM::InstanceProfile&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html\&quot;&gt; AWS::IAM::Policy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html\&quot;&gt; AWS::IAM::Role&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html\&quot;&gt; AWS::IAM::User&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html\&quot;&gt;AWS::IAM::UserToGroupAddition&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/using-iam-template.html#capabilities\&quot;&gt;Acknowledging IAM Resources in CloudFormation Templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_AUTO_EXPAND&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some templates reference macros. If your stack set template references one or more macros, you must create the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To create the stack set directly, you must acknowledge this capability. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/template-macros.html\&quot;&gt;Using CloudFormation Macros to Perform Custom Processing on Templates&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Stack sets with service-managed permissions don&#39;t currently support the use of macros in templates. (This includes the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html\&quot;&gt;AWS::Include&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/transform-aws-serverless.html\&quot;&gt;AWS::Serverless&lt;/a&gt; transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ul&gt;
    :type capabilities: list | bytes
    :param tags: &lt;p&gt;The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.&lt;/p&gt; &lt;p&gt;If you specify tags as part of a &lt;code&gt;CreateStackSet&lt;/code&gt; action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don&#39;t, the entire &lt;code&gt;CreateStackSet&lt;/code&gt; action fails with an &lt;code&gt;access denied&lt;/code&gt; error, and the stack set is not created.&lt;/p&gt;
    :type tags: list | bytes
    :param administration_role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the IAM role to use to create this stack set.&lt;/p&gt; &lt;p&gt;Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/stacksets-prereqs.html\&quot;&gt;Prerequisites: Granting Permissions for Stack Set Operations&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt;
    :type administration_role_arn: str
    :param execution_role_name: &lt;p&gt;The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, CloudFormation uses the &lt;code&gt;AWSCloudFormationStackSetExecutionRole&lt;/code&gt; role for the stack set operation.&lt;/p&gt; &lt;p&gt;Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.&lt;/p&gt;
    :type execution_role_name: str
    :param permission_model: &lt;p&gt;Describes how the IAM roles required for stack set operations are created. By default, &lt;code&gt;SELF-MANAGED&lt;/code&gt; is specified.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;With &lt;code&gt;self-managed&lt;/code&gt; permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html\&quot;&gt;Grant Self-Managed Stack Set Permissions&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;With &lt;code&gt;service-managed&lt;/code&gt; permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html\&quot;&gt;Grant Service-Managed Stack Set Permissions&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type permission_model: str
    :param auto_deployment: Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if &lt;code&gt;PermissionModel&lt;/code&gt; is &lt;code&gt;SERVICE_MANAGED&lt;/code&gt;.
    :type auto_deployment: dict | bytes
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To create a stack set with service-managed permissions while signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.&lt;/p&gt;
    :type call_as: str
    :param client_request_token: &lt;p&gt;A unique identifier for this &lt;code&gt;CreateStackSet&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to create another stack set with the same name. You might retry &lt;code&gt;CreateStackSet&lt;/code&gt; requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify an operation ID, the SDK generates one automatically.&lt;/p&gt;
    :type client_request_token: str
    :param managed_execution: Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
    :type managed_execution: dict | bytes

    """
    parameters = [Parameter.from_dict(d) for d in parameters]
    capabilities = [Capability.from_dict(d) for d in capabilities]
    tags = [Tag.from_dict(d) for d in tags]
    auto_deployment = .from_dict(auto_deployment)
    managed_execution = .from_dict(managed_execution)
    return web.Response(status=200)


async def g_et_deactivate_organizations_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_deactivate_organizations_access

    Deactivates trusted access with Organizations. If trusted access is deactivated, the management account does not have permissions to create and manage service-managed StackSets for your organization.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_deactivate_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type_name=None, type=None, arn=None) -> web.Response:
    """g_et_deactivate_type

    &lt;p&gt;Deactivates a public extension that was previously activated in this account and Region.&lt;/p&gt; &lt;p&gt;Once deactivated, an extension can&#39;t be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren&#39;t automatically updated if a new version of the extension is released.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type_name: &lt;p&gt;The type name of the extension, in this account and Region. If you specified a type name alias when enabling the extension, use the type name alias.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param type: &lt;p&gt;The extension type.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param arn: &lt;p&gt;The Amazon Resource Name (ARN) for the extension, in this account and Region.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type arn: str

    """
    return web.Response(status=200)


async def g_et_delete_change_set(request: web.Request, change_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None) -> web.Response:
    """g_et_delete_change_set

    &lt;p&gt;Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.&lt;/p&gt; &lt;p&gt;If the call successfully completes, CloudFormation successfully deleted the change set.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;IncludeNestedStacks&lt;/code&gt; specifies &lt;code&gt;True&lt;/code&gt; during the creation of the nested change set, then &lt;code&gt;DeleteChangeSet&lt;/code&gt; will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of &lt;code&gt;REVIEW_IN_PROGRESS&lt;/code&gt;.&lt;/p&gt;

    :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want to delete.
    :type change_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that&#39;s associated with it.
    :type stack_name: str

    """
    return web.Response(status=200)


async def g_et_delete_stack(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, retain_resources=None, role_arn=None, client_request_token=None) -> web.Response:
    """g_et_delete_stack

    Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don&#39;t show up in the &lt;a&gt;DescribeStacks&lt;/a&gt; operation if the deletion has been completed successfully.

    :param stack_name: The name or the unique stack ID that&#39;s associated with the stack.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param retain_resources: &lt;p&gt;For stacks in the &lt;code&gt;DELETE_FAILED&lt;/code&gt; state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, CloudFormation deletes the stack but doesn&#39;t delete the retained resources.&lt;/p&gt; &lt;p&gt;Retaining resources is useful when you can&#39;t delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.&lt;/p&gt;
    :type retain_resources: List[str]
    :param role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to delete the stack. CloudFormation uses the role&#39;s credentials to make calls on your behalf.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that&#39;s generated from your user credentials.&lt;/p&gt;
    :type role_arn: str
    :param client_request_token: &lt;p&gt;A unique identifier for this &lt;code&gt;DeleteStack&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to delete a stack with the same name. You might retry &lt;code&gt;DeleteStack&lt;/code&gt; requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a &lt;code&gt;CreateStack&lt;/code&gt; operation with the token &lt;code&gt;token1&lt;/code&gt;, then all the &lt;code&gt;StackEvents&lt;/code&gt; generated by that operation will have &lt;code&gt;ClientRequestToken&lt;/code&gt; set as &lt;code&gt;token1&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format &lt;i&gt;Console-StackOperation-ID&lt;/i&gt;, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: &lt;code&gt;Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002&lt;/code&gt;.&lt;/p&gt;
    :type client_request_token: str

    """
    return web.Response(status=200)


async def g_et_delete_stack_instances(request: web.Request, stack_set_name, regions, retain_stacks, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, accounts=None, deployment_targets=None, operation_preferences=None, operation_id=None, call_as=None) -> web.Response:
    """g_et_delete_stack_instances

    Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.

    :param stack_set_name: The name or unique ID of the stack set that you want to delete stack instances for.
    :type stack_set_name: str
    :param regions: The Amazon Web Services Regions where you want to delete stack set instances.
    :type regions: List[str]
    :param retain_stacks: &lt;p&gt;Removes the stack instances from the specified stack set, but doesn&#39;t delete the stacks. You can&#39;t reassociate a retained stack or add an existing, saved stack to a new stack set.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options\&quot;&gt;Stack set operation options&lt;/a&gt;.&lt;/p&gt;
    :type retain_stacks: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param accounts: &lt;p&gt;[Self-managed permissions] The names of the Amazon Web Services accounts that you want to delete stack instances for.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, but not both.&lt;/p&gt;
    :type accounts: List[str]
    :param deployment_targets: &lt;p&gt;[Service-managed permissions] The Organizations accounts from which to delete stack instances.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, but not both.&lt;/p&gt;
    :type deployment_targets: dict | bytes
    :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
    :type operation_preferences: dict | bytes
    :param operation_id: &lt;p&gt;The unique identifier for this stack set operation.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify an operation ID, the SDK generates one automatically.&lt;/p&gt; &lt;p&gt;The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;Repeating this stack set operation with a new operation ID retries all stack instances whose status is &lt;code&gt;OUTDATED&lt;/code&gt;.&lt;/p&gt;
    :type operation_id: str
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    deployment_targets = .from_dict(deployment_targets)
    operation_preferences = .from_dict(operation_preferences)
    return web.Response(status=200)


async def g_et_delete_stack_set(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, call_as=None) -> web.Response:
    """g_et_delete_stack_set

    Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see &lt;a&gt;DeleteStackInstances&lt;/a&gt;.

    :param stack_set_name: The name or unique ID of the stack set that you&#39;re deleting. You can obtain this value by running &lt;a&gt;ListStackSets&lt;/a&gt;.
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_deregister_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, arn=None, type=None, type_name=None, version_id=None) -> web.Response:
    """g_et_deregister_type

    &lt;p&gt;Marks an extension or extension version as &lt;code&gt;DEPRECATED&lt;/code&gt; in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.&lt;/p&gt; &lt;p&gt;To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.&lt;/p&gt; &lt;p&gt;You can&#39;t deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.&lt;/p&gt; &lt;p&gt;To view the deprecation status of an extension or extension version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html\&quot;&gt;DescribeType&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param arn: &lt;p&gt;The Amazon Resource Name (ARN) of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type arn: str
    :param type: &lt;p&gt;The kind of extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param type_name: &lt;p&gt;The name of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param version_id: The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.
    :type version_id: str

    """
    return web.Response(status=200)


async def g_et_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_describe_account_limits

    Retrieves your account&#39;s CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html\&quot;&gt;CloudFormation Quotas&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: A string that identifies the next page of limits that you want to retrieve.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_describe_change_set(request: web.Request, change_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None, next_token=None) -> web.Response:
    """g_et_describe_change_set

    Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html\&quot;&gt;Updating Stacks Using Change Sets&lt;/a&gt; in the CloudFormation User Guide.

    :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want to describe.
    :type change_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.
    :type stack_name: str
    :param next_token: A string (provided by the &lt;a&gt;DescribeChangeSet&lt;/a&gt; response output) that identifies the next page of information that you want to retrieve.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_describe_change_set_hooks(request: web.Request, change_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None, next_token=None, logical_resource_id=None) -> web.Response:
    """g_et_describe_change_set_hooks

    Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

    :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want to describe.
    :type change_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.
    :type stack_name: str
    :param next_token: A string, provided by the &lt;code&gt;DescribeChangeSetHooks&lt;/code&gt; response output, that identifies the next page of information that you want to retrieve.
    :type next_token: str
    :param logical_resource_id: If specified, lists only the hooks related to the specified &lt;code&gt;LogicalResourceId&lt;/code&gt;.
    :type logical_resource_id: str

    """
    return web.Response(status=200)


async def g_et_describe_organizations_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, call_as=None) -> web.Response:
    """g_et_describe_organizations_access

    Retrieves information about the account&#39;s &lt;code&gt;OrganizationAccess&lt;/code&gt; status. This API can be called either by the management account or the delegated administrator by using the &lt;code&gt;CallAs&lt;/code&gt; parameter. This API can also be called without the &lt;code&gt;CallAs&lt;/code&gt; parameter by the management account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_describe_publisher(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, publisher_id=None) -> web.Response:
    """g_et_describe_publisher

    &lt;p&gt;Returns information about a CloudFormation extension publisher.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a &lt;code&gt;PublisherId&lt;/code&gt;, and you have registered as an extension publisher, &lt;code&gt;DescribePublisher&lt;/code&gt; returns information about your own publisher account.&lt;/p&gt; &lt;p&gt;For more information about registering as a publisher, see:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html\&quot;&gt;RegisterPublisher&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html\&quot;&gt;Publishing extensions to make them available for public use&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param publisher_id: &lt;p&gt;The ID of the extension publisher.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a &lt;code&gt;PublisherId&lt;/code&gt;, and you have registered as an extension publisher, &lt;code&gt;DescribePublisher&lt;/code&gt; returns information about your own publisher account.&lt;/p&gt;
    :type publisher_id: str

    """
    return web.Response(status=200)


async def g_et_describe_stack_drift_detection_status(request: web.Request, stack_drift_detection_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_stack_drift_detection_status

    &lt;p&gt;Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack&#39;s actual configuration differs, or has &lt;i&gt;drifted&lt;/i&gt;, from its expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\&quot;&gt;Detecting Unregulated Configuration Changes to Stacks and Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DetectStackDrift&lt;/a&gt; to initiate a stack drift detection operation. &lt;code&gt;DetectStackDrift&lt;/code&gt; returns a &lt;code&gt;StackDriftDetectionId&lt;/code&gt; you can use to monitor the progress of the operation using &lt;code&gt;DescribeStackDriftDetectionStatus&lt;/code&gt;. Once the drift detection operation has completed, use &lt;a&gt;DescribeStackResourceDrifts&lt;/a&gt; to return drift information about the stack and its resources.&lt;/p&gt;

    :param stack_drift_detection_id: &lt;p&gt;The ID of the drift detection results of this operation.&lt;/p&gt; &lt;p&gt;CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results CloudFormation retains for any given stack, and for how long, may vary.&lt;/p&gt;
    :type stack_drift_detection_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_describe_stack_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None, next_token=None) -> web.Response:
    """g_et_describe_stack_events

    &lt;p&gt;Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack&#39;s event history, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html\&quot;&gt;Stacks&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: &lt;p&gt;The name or the unique stack ID that&#39;s associated with the stack, which aren&#39;t always interchangeable:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Running stacks: You can specify either the stack&#39;s name or its unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deleted stacks: You must specify the unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type stack_name: str
    :param next_token: A string that identifies the next page of events that you want to retrieve.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_describe_stack_instance(request: web.Request, stack_set_name, stack_instance_account, stack_instance_region, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, call_as=None) -> web.Response:
    """g_et_describe_stack_instance

    &lt;p&gt;Returns the stack instance that&#39;s associated with the specified StackSet, Amazon Web Services account, and Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;For a list of stack instances that are associated with a specific StackSet, use &lt;a&gt;ListStackInstances&lt;/a&gt;.&lt;/p&gt;

    :param stack_set_name: The name or the unique stack ID of the stack set that you want to get stack instance information for.
    :type stack_set_name: str
    :param stack_instance_account: The ID of an Amazon Web Services account that&#39;s associated with this stack instance.
    :type stack_instance_account: str
    :param stack_instance_region: The name of a Region that&#39;s associated with this stack instance.
    :type stack_instance_region: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_describe_stack_resource(request: web.Request, stack_name, logical_resource_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_stack_resource

    &lt;p&gt;Returns a description of the specified resource in the specified stack.&lt;/p&gt; &lt;p&gt;For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.&lt;/p&gt;

    :param stack_name: &lt;p&gt;The name or the unique stack ID that&#39;s associated with the stack, which aren&#39;t always interchangeable:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Running stacks: You can specify either the stack&#39;s name or its unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deleted stacks: You must specify the unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type stack_name: str
    :param logical_resource_id: &lt;p&gt;The logical name of the resource as specified in the template.&lt;/p&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type logical_resource_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_describe_stack_resource_drifts(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_resource_drift_status_filters=None, next_token=None, max_results=None) -> web.Response:
    """g_et_describe_stack_resource_drifts

    &lt;p&gt;Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.&lt;/p&gt; &lt;p&gt;For a given stack, there will be one &lt;code&gt;StackResourceDrift&lt;/code&gt; for each stack resource that has been checked for drift. Resources that haven&#39;t yet been checked for drift aren&#39;t included. Resources that don&#39;t currently support drift detection aren&#39;t checked, and so not included. For a list of resources that support drift detection, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html\&quot;&gt;Resources that Support Drift Detection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DetectStackResourceDrift&lt;/a&gt; to detect drift on individual resources, or &lt;a&gt;DetectStackDrift&lt;/a&gt; to detect drift on all supported resources for a given stack.&lt;/p&gt;

    :param stack_name: The name of the stack for which you want drift information.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_resource_drift_status_filters: &lt;p&gt;The resource drift status values to use as filters for the resource drift results returned.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DELETED&lt;/code&gt;: The resource differs from its expected template configuration in that the resource has been deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MODIFIED&lt;/code&gt;: One or more resource properties differ from their expected template values.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IN_SYNC&lt;/code&gt;: The resource&#39;s actual configuration matches its expected template configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NOT_CHECKED&lt;/code&gt;: CloudFormation doesn&#39;t currently return this value.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type stack_resource_drift_status_filters: list | bytes
    :param next_token: A string that identifies the next page of stack resource drift results.
    :type next_token: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int

    """
    stack_resource_drift_status_filters = [StackResourceDriftStatus.from_dict(d) for d in stack_resource_drift_status_filters]
    return web.Response(status=200)


async def g_et_describe_stack_resources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None, logical_resource_id=None, physical_resource_id=None) -> web.Response:
    """g_et_describe_stack_resources

    &lt;p&gt;Returns Amazon Web Services resource descriptions for running and deleted stacks. If &lt;code&gt;StackName&lt;/code&gt; is specified, all the associated resources that are part of the stack are returned. If &lt;code&gt;PhysicalResourceId&lt;/code&gt; is specified, the associated resources of the stack that the resource belongs to are returned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the first 100 resources will be returned. If your stack has more resources than this, you should use &lt;code&gt;ListStackResources&lt;/code&gt; instead.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For deleted stacks, &lt;code&gt;DescribeStackResources&lt;/code&gt; returns resource information for up to 90 days after the stack has been deleted.&lt;/p&gt; &lt;p&gt;You must specify either &lt;code&gt;StackName&lt;/code&gt; or &lt;code&gt;PhysicalResourceId&lt;/code&gt;, but not both. In addition, you can specify &lt;code&gt;LogicalResourceId&lt;/code&gt; to filter the returned result. For more information about resources, the &lt;code&gt;LogicalResourceId&lt;/code&gt; and &lt;code&gt;PhysicalResourceId&lt;/code&gt;, go to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/\&quot;&gt;CloudFormation User Guide&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A &lt;code&gt;ValidationError&lt;/code&gt; is returned if you specify both &lt;code&gt;StackName&lt;/code&gt; and &lt;code&gt;PhysicalResourceId&lt;/code&gt; in the same request.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: &lt;p&gt;The name or the unique stack ID that is associated with the stack, which aren&#39;t always interchangeable:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Running stacks: You can specify either the stack&#39;s name or its unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deleted stacks: You must specify the unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt; &lt;p&gt;Required: Conditional. If you don&#39;t specify &lt;code&gt;StackName&lt;/code&gt;, you must specify &lt;code&gt;PhysicalResourceId&lt;/code&gt;.&lt;/p&gt;
    :type stack_name: str
    :param logical_resource_id: &lt;p&gt;The logical name of the resource as specified in the template.&lt;/p&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type logical_resource_id: str
    :param physical_resource_id: &lt;p&gt;The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.&lt;/p&gt; &lt;p&gt;For example, for an Amazon Elastic Compute Cloud (EC2) instance, &lt;code&gt;PhysicalResourceId&lt;/code&gt; corresponds to the &lt;code&gt;InstanceId&lt;/code&gt;. You can pass the EC2 &lt;code&gt;InstanceId&lt;/code&gt; to &lt;code&gt;DescribeStackResources&lt;/code&gt; to find which stack the instance belongs to and what other resources are part of the stack.&lt;/p&gt; &lt;p&gt;Required: Conditional. If you don&#39;t specify &lt;code&gt;PhysicalResourceId&lt;/code&gt;, you must specify &lt;code&gt;StackName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type physical_resource_id: str

    """
    return web.Response(status=200)


async def g_et_describe_stack_set(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, call_as=None) -> web.Response:
    """g_et_describe_stack_set

    Returns the description of the specified StackSet.

    :param stack_set_name: The name or unique ID of the stack set whose description you want.
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_describe_stack_set_operation(request: web.Request, stack_set_name, operation_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, call_as=None) -> web.Response:
    """g_et_describe_stack_set_operation

    Returns the description of the specified StackSet operation.

    :param stack_set_name: The name or the unique stack ID of the stack set for the stack operation.
    :type stack_set_name: str
    :param operation_id: The unique ID of the stack set operation.
    :type operation_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_describe_stacks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None, next_token=None) -> web.Response:
    """g_et_describe_stacks

    &lt;p&gt;Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the stack doesn&#39;t exist, an &lt;code&gt;ValidationError&lt;/code&gt; is returned.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: &lt;note&gt; &lt;p&gt;If you don&#39;t pass a parameter to &lt;code&gt;StackName&lt;/code&gt;, the API returns a response that describes all resources in the account. This requires &lt;code&gt;ListStacks&lt;/code&gt; and &lt;code&gt;DescribeStacks&lt;/code&gt; permissions.&lt;/p&gt; &lt;p&gt;The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:&lt;/p&gt; &lt;p&gt;{ \&quot;Version\&quot;: \&quot;2012-10-17\&quot;, \&quot;Statement\&quot;: [{ \&quot;Effect\&quot;: \&quot;Deny\&quot;, \&quot;Action\&quot;: \&quot;cloudformation:DescribeStacks\&quot;, \&quot;NotResource\&quot;: \&quot;arn:aws:cloudformation:*:*:stack/*/*\&quot; }] }&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The name or the unique stack ID that&#39;s associated with the stack, which aren&#39;t always interchangeable:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Running stacks: You can specify either the stack&#39;s name or its unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deleted stacks: You must specify the unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type stack_name: str
    :param next_token: A string that identifies the next page of stacks that you want to retrieve.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_describe_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, type_name=None, arn=None, version_id=None, publisher_id=None, public_version_number=None) -> web.Response:
    """g_et_describe_type

    &lt;p&gt;Returns detailed information about an extension that has been registered.&lt;/p&gt; &lt;p&gt;If you specify a &lt;code&gt;VersionId&lt;/code&gt;, &lt;code&gt;DescribeType&lt;/code&gt; returns information about that specific extension version. Otherwise, it returns information about the default extension version.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type: &lt;p&gt;The kind of extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param type_name: &lt;p&gt;The name of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param arn: &lt;p&gt;The Amazon Resource Name (ARN) of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type arn: str
    :param version_id: &lt;p&gt;The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.&lt;/p&gt; &lt;p&gt;If you specify a &lt;code&gt;VersionId&lt;/code&gt;, &lt;code&gt;DescribeType&lt;/code&gt; returns information about that specific extension version. Otherwise, it returns information about the default extension version.&lt;/p&gt;
    :type version_id: str
    :param publisher_id: &lt;p&gt;The publisher ID of the extension publisher.&lt;/p&gt; &lt;p&gt;Extensions provided by Amazon Web Services are not assigned a publisher ID.&lt;/p&gt;
    :type publisher_id: str
    :param public_version_number: The version number of a public third-party extension.
    :type public_version_number: str

    """
    return web.Response(status=200)


async def g_et_describe_type_registration(request: web.Request, registration_token, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_type_registration

    &lt;p&gt;Returns information about an extension&#39;s registration, including its current status and type and version identifiers.&lt;/p&gt; &lt;p&gt;When you initiate a registration request using &lt;a&gt;RegisterType&lt;/a&gt;, you can then use &lt;a&gt;DescribeTypeRegistration&lt;/a&gt; to monitor the progress of that registration request.&lt;/p&gt; &lt;p&gt;Once the registration request has completed, use &lt;a&gt;DescribeType&lt;/a&gt; to return detailed information about an extension.&lt;/p&gt;

    :param registration_token: &lt;p&gt;The identifier for this registration request.&lt;/p&gt; &lt;p&gt;This registration token is generated by CloudFormation when you initiate a registration request using &lt;a&gt;RegisterType&lt;/a&gt;.&lt;/p&gt;
    :type registration_token: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_detect_stack_drift(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, logical_resource_ids=None) -> web.Response:
    """g_et_detect_stack_drift

    &lt;p&gt;Detects whether a stack&#39;s actual configuration differs, or has &lt;i&gt;drifted&lt;/i&gt;, from its expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\&quot;&gt;Detecting Unregulated Configuration Changes to Stacks and Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;code&gt;DetectStackDrift&lt;/code&gt; to detect drift on all supported resources for a given stack, or &lt;a&gt;DetectStackResourceDrift&lt;/a&gt; to detect drift on individual resources.&lt;/p&gt; &lt;p&gt;For a list of stack resources that currently support drift detection, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html\&quot;&gt;Resources that Support Drift Detection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectStackDrift&lt;/code&gt; can take up to several minutes, depending on the number of resources contained within the stack. Use &lt;a&gt;DescribeStackDriftDetectionStatus&lt;/a&gt; to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use &lt;a&gt;DescribeStackResourceDrifts&lt;/a&gt; to return drift information about the stack and its resources.&lt;/p&gt; &lt;p&gt;When detecting drift on a stack, CloudFormation doesn&#39;t detect drift on any nested stacks belonging to that stack. Perform &lt;code&gt;DetectStackDrift&lt;/code&gt; directly on the nested stack itself.&lt;/p&gt;

    :param stack_name: The name of the stack for which you want to detect drift.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param logical_resource_ids: The logical names of any resources you want to use as filters.
    :type logical_resource_ids: List[str]

    """
    return web.Response(status=200)


async def g_et_detect_stack_resource_drift(request: web.Request, stack_name, logical_resource_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_detect_stack_resource_drift

    &lt;p&gt;Returns information about whether a resource&#39;s actual configuration differs, or has &lt;i&gt;drifted&lt;/i&gt;, from its expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\&quot;&gt;Detecting Unregulated Configuration Changes to Stacks and Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;code&gt;DetectStackResourceDrift&lt;/code&gt; to detect drift on individual resources, or &lt;a&gt;DetectStackDrift&lt;/a&gt; to detect drift on all resources in a given stack that support drift detection.&lt;/p&gt; &lt;p&gt;Resources that don&#39;t currently support drift detection can&#39;t be checked. For a list of resources that support drift detection, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html\&quot;&gt;Resources that Support Drift Detection&lt;/a&gt;.&lt;/p&gt;

    :param stack_name: The name of the stack to which the resource belongs.
    :type stack_name: str
    :param logical_resource_id: The logical name of the resource for which to return drift information.
    :type logical_resource_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_detect_stack_set_drift(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, operation_preferences=None, operation_id=None, call_as=None) -> web.Response:
    """g_et_detect_stack_set_drift

    &lt;p&gt;Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html\&quot;&gt;How CloudFormation performs drift detection on a stack set&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectStackSetDrift&lt;/code&gt; returns the &lt;code&gt;OperationId&lt;/code&gt; of the stack set drift detection operation. Use this operation id with &lt;a&gt;DescribeStackSetOperation&lt;/a&gt; to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.&lt;/p&gt; &lt;p&gt;Once the operation has completed, use the following actions to return drift information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;DescribeStackSet&lt;/a&gt; to return detailed information about the stack set, including detailed information about the last &lt;i&gt;completed&lt;/i&gt; drift operation performed on the stack set. (Information about drift operations that are in progress isn&#39;t included.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;ListStackInstances&lt;/a&gt; to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;DescribeStackInstance&lt;/a&gt; to return detailed information about a specific stack instance, including its drift status and last drift time checked.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about performing a drift detection operation on a stack set, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html\&quot;&gt;Detecting unmanaged changes in stack sets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can only run a single drift detection operation on a given stack set at one time.&lt;/p&gt; &lt;p&gt;To stop a drift detection stack set operation, use &lt;a&gt;StopStackSetOperation&lt;/a&gt;.&lt;/p&gt;

    :param stack_set_name: The name of the stack set on which to perform the drift detection operation.
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param operation_preferences: &lt;p&gt;The user-specified preferences for how CloudFormation performs a stack set operation.&lt;/p&gt; &lt;p&gt;For more information about maximum concurrent accounts and failure tolerance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options\&quot;&gt;Stack set operation options&lt;/a&gt;.&lt;/p&gt;
    :type operation_preferences: dict | bytes
    :param operation_id:  &lt;i&gt;The ID of the stack set operation.&lt;/i&gt; 
    :type operation_id: str
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    operation_preferences = .from_dict(operation_preferences)
    return web.Response(status=200)


async def g_et_estimate_template_cost(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_body=None, template_url=None, parameters=None) -> web.Response:
    """g_et_estimate_template_cost

    Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_body: &lt;p&gt;Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.)&lt;/p&gt; &lt;p&gt;Conditional: You must pass &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt;. If both are passed, only &lt;code&gt;TemplateBody&lt;/code&gt; is used.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;Location of file containing the template body. The URL must point to a template that&#39;s located in an Amazon S3 bucket or a Systems Manager document. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must pass &lt;code&gt;TemplateURL&lt;/code&gt; or &lt;code&gt;TemplateBody&lt;/code&gt;. If both are passed, only &lt;code&gt;TemplateBody&lt;/code&gt; is used.&lt;/p&gt;
    :type template_url: str
    :param parameters: A list of &lt;code&gt;Parameter&lt;/code&gt; structures that specify input parameters.
    :type parameters: list | bytes

    """
    parameters = [Parameter.from_dict(d) for d in parameters]
    return web.Response(status=200)


async def g_et_execute_change_set(request: web.Request, change_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None, client_request_token=None, disable_rollback=None, retain_except_on_create=None) -> web.Response:
    """g_et_execute_change_set

    &lt;p&gt;Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the &lt;a&gt;DescribeStacks&lt;/a&gt; action to view the status of the update.&lt;/p&gt; &lt;p&gt;When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren&#39;t valid for the updated stack.&lt;/p&gt; &lt;p&gt;If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can&#39;t specify a temporary stack policy that overrides the current policy.&lt;/p&gt; &lt;p&gt;To create a change set for the entire stack hierarchy, &lt;code&gt;IncludeNestedStacks&lt;/code&gt; must have been set to &lt;code&gt;True&lt;/code&gt;.&lt;/p&gt;

    :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.
    :type change_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that&#39;s associated with the change set you want to execute.
    :type stack_name: str
    :param client_request_token: A unique identifier for this &lt;code&gt;ExecuteChangeSet&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to execute a change set to update a stack with the same name. You might retry &lt;code&gt;ExecuteChangeSet&lt;/code&gt; requests to ensure that CloudFormation successfully received them.
    :type client_request_token: str
    :param disable_rollback: &lt;p&gt;Preserves the state of previously provisioned resources when an operation fails. This parameter can&#39;t be specified when the &lt;code&gt;OnStackFailure&lt;/code&gt; parameter to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html\&quot;&gt;CreateChangeSet&lt;/a&gt; API operation was specified.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;True&lt;/code&gt; - if the stack creation fails, do nothing. This is equivalent to specifying &lt;code&gt;DO_NOTHING&lt;/code&gt; for the &lt;code&gt;OnStackFailure&lt;/code&gt; parameter to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html\&quot;&gt;CreateChangeSet&lt;/a&gt; API operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;False&lt;/code&gt; - if the stack creation fails, roll back the stack. This is equivalent to specifying &lt;code&gt;ROLLBACK&lt;/code&gt; for the &lt;code&gt;OnStackFailure&lt;/code&gt; parameter to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html\&quot;&gt;CreateChangeSet&lt;/a&gt; API operation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;True&lt;/code&gt; &lt;/p&gt;
    :type disable_rollback: bool
    :param retain_except_on_create: This deletion policy deletes newly created resources, but retains existing resources, when a stack operation is rolled back. This ensures new, empty, and unused resources are deleted, while critical resources and their data are retained. &lt;code&gt;RetainExceptOnCreate&lt;/code&gt; can be specified for any resource that supports the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html\&quot;&gt; DeletionPolicy&lt;/a&gt; attribute.
    :type retain_except_on_create: bool

    """
    return web.Response(status=200)


async def g_et_get_stack_policy(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_stack_policy

    Returns the stack policy for a specified stack. If a stack doesn&#39;t have a policy, a null value is returned.

    :param stack_name: The name or unique stack ID that&#39;s associated with the stack whose policy you want to get.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_get_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_name=None, change_set_name=None, template_stage=None) -> web.Response:
    """g_et_get_template

    &lt;p&gt;Returns the template body for a specified stack. You can get the template for running or deleted stacks.&lt;/p&gt; &lt;p&gt;For deleted stacks, &lt;code&gt;GetTemplate&lt;/code&gt; returns the template for up to 90 days after the stack has been deleted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the template doesn&#39;t exist, a &lt;code&gt;ValidationError&lt;/code&gt; is returned.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_name: &lt;p&gt;The name or the unique stack ID that&#39;s associated with the stack, which aren&#39;t always interchangeable:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Running stacks: You can specify either the stack&#39;s name or its unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deleted stacks: You must specify the unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type stack_name: str
    :param change_set_name: The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the &lt;code&gt;StackName&lt;/code&gt;.
    :type change_set_name: str
    :param template_stage: &lt;p&gt;For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify &lt;code&gt;Original&lt;/code&gt;. To get the template after CloudFormation has processed all transforms, specify &lt;code&gt;Processed&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If the template doesn&#39;t include transforms, &lt;code&gt;Original&lt;/code&gt; and &lt;code&gt;Processed&lt;/code&gt; return the same template. By default, CloudFormation specifies &lt;code&gt;Processed&lt;/code&gt;.&lt;/p&gt;
    :type template_stage: str

    """
    return web.Response(status=200)


async def g_et_get_template_summary(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_body=None, template_url=None, stack_name=None, stack_set_name=None, call_as=None, template_summary_config=None) -> web.Response:
    """g_et_get_template_summary

    &lt;p&gt;Returns information about a new or existing template. The &lt;code&gt;GetTemplateSummary&lt;/code&gt; action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetTemplateSummary&lt;/code&gt; action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.&lt;/p&gt; &lt;p&gt;For deleted stacks, &lt;code&gt;GetTemplateSummary&lt;/code&gt; returns the template information for up to 90 days after the stack has been deleted. If the template doesn&#39;t exist, a &lt;code&gt;ValidationError&lt;/code&gt; is returned.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_body: &lt;p&gt;Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;StackName&lt;/code&gt;, &lt;code&gt;StackSetName&lt;/code&gt;, &lt;code&gt;TemplateBody&lt;/code&gt;, or &lt;code&gt;TemplateURL&lt;/code&gt;.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that&#39;s located in an Amazon S3 bucket or a Systems Manager document. For more information about templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;StackName&lt;/code&gt;, &lt;code&gt;StackSetName&lt;/code&gt;, &lt;code&gt;TemplateBody&lt;/code&gt;, or &lt;code&gt;TemplateURL&lt;/code&gt;.&lt;/p&gt;
    :type template_url: str
    :param stack_name: &lt;p&gt;The name or the stack ID that&#39;s associated with the stack, which aren&#39;t always interchangeable. For running stacks, you can specify either the stack&#39;s name or its unique stack ID. For deleted stack, you must specify the unique stack ID.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;StackName&lt;/code&gt;, &lt;code&gt;StackSetName&lt;/code&gt;, &lt;code&gt;TemplateBody&lt;/code&gt;, or &lt;code&gt;TemplateURL&lt;/code&gt;.&lt;/p&gt;
    :type stack_name: str
    :param stack_set_name: &lt;p&gt;The name or unique ID of the stack set from which the stack was created.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;StackName&lt;/code&gt;, &lt;code&gt;StackSetName&lt;/code&gt;, &lt;code&gt;TemplateBody&lt;/code&gt;, or &lt;code&gt;TemplateURL&lt;/code&gt;.&lt;/p&gt;
    :type stack_set_name: str
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str
    :param template_summary_config: Specifies options for the &lt;code&gt;GetTemplateSummary&lt;/code&gt; API action.
    :type template_summary_config: dict | bytes

    """
    template_summary_config = .from_dict(template_summary_config)
    return web.Response(status=200)


async def g_et_import_stacks_to_stack_set(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_ids=None, stack_ids_url=None, organizational_unit_ids=None, operation_preferences=None, operation_id=None, call_as=None) -> web.Response:
    """g_et_import_stacks_to_stack_set

    Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.

    :param stack_set_name: The name of the stack set. The name must be unique in the Region where you create your stack set.
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_ids: &lt;p&gt;The IDs of the stacks you are importing into a stack set. You import up to 10 stacks per stack set at a time.&lt;/p&gt; &lt;p&gt;Specify either &lt;code&gt;StackIds&lt;/code&gt; or &lt;code&gt;StackIdsUrl&lt;/code&gt;.&lt;/p&gt;
    :type stack_ids: List[str]
    :param stack_ids_url: &lt;p&gt;The Amazon S3 URL which contains list of stack ids to be inputted.&lt;/p&gt; &lt;p&gt;Specify either &lt;code&gt;StackIds&lt;/code&gt; or &lt;code&gt;StackIdsUrl&lt;/code&gt;.&lt;/p&gt;
    :type stack_ids_url: str
    :param organizational_unit_ids: The list of OU ID&#39;s to which the stacks being imported has to be mapped as deployment target.
    :type organizational_unit_ids: List[str]
    :param operation_preferences: &lt;p&gt;The user-specified preferences for how CloudFormation performs a stack set operation.&lt;/p&gt; &lt;p&gt;For more information about maximum concurrent accounts and failure tolerance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options\&quot;&gt;Stack set operation options&lt;/a&gt;.&lt;/p&gt;
    :type operation_preferences: dict | bytes
    :param operation_id: A unique, user defined, identifier for the stack set operation.
    :type operation_id: str
    :param call_as: &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For service managed stack sets, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    operation_preferences = .from_dict(operation_preferences)
    return web.Response(status=200)


async def g_et_list_change_sets(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_change_sets

    Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the &lt;code&gt;CREATE_IN_PROGRESS&lt;/code&gt; or &lt;code&gt;CREATE_PENDING&lt;/code&gt; state.

    :param stack_name: The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: A string (provided by the &lt;a&gt;ListChangeSets&lt;/a&gt; response output) that identifies the next page of change sets that you want to retrieve.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_exports(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_exports

    &lt;p&gt;Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html\&quot;&gt; Fn::ImportValue&lt;/a&gt; function.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html\&quot;&gt; CloudFormation export stack output values&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: A string (provided by the &lt;a&gt;ListExports&lt;/a&gt; response output) that identifies the next page of exported output values that you asked to retrieve.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_imports(request: web.Request, export_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_imports

    &lt;p&gt;Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see &lt;a&gt;ListExports&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about importing an exported output value, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html\&quot;&gt;Fn::ImportValue&lt;/a&gt; function.&lt;/p&gt;

    :param export_name: The name of the exported output value. CloudFormation returns the stack names that are importing this value.
    :type export_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: A string (provided by the &lt;a&gt;ListImports&lt;/a&gt; response output) that identifies the next page of stacks that are importing the specified exported output value.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_stack_instance_resource_drifts(request: web.Request, stack_set_name, stack_instance_account, stack_instance_region, operation_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, stack_instance_resource_drift_statuses=None, call_as=None) -> web.Response:
    """g_et_list_stack_instance_resource_drifts

    &lt;p&gt;Returns drift information for resources in a stack instance.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ListStackInstanceResourceDrifts&lt;/code&gt; returns drift information for the most recent drift detection operation. If an operation is in progress, it may only return partial results.&lt;/p&gt; &lt;/note&gt;

    :param stack_set_name: The name or unique ID of the stack set that you want to list drifted resources for.
    :type stack_set_name: str
    :param stack_instance_account: The name of the Amazon Web Services account that you want to list resource drifts for.
    :type stack_instance_account: str
    :param stack_instance_region: The name of the Region where you want to list resource drifts.
    :type stack_instance_region: str
    :param operation_id: The unique ID of the drift operation.
    :type operation_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: If the previous paginated request didn&#39;t return all of the remaining results, the response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param stack_instance_resource_drift_statuses: &lt;p&gt;The resource drift status of the stack instance. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DELETED&lt;/code&gt;: The resource differs from its expected template configuration in that the resource has been deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MODIFIED&lt;/code&gt;: One or more resource properties differ from their expected template values.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IN_SYNC&lt;/code&gt;: The resource&#39;s actual configuration matches its expected template configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NOT_CHECKED&lt;/code&gt;: CloudFormation doesn&#39;t currently return this value.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type stack_instance_resource_drift_statuses: list | bytes
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    stack_instance_resource_drift_statuses = [StackResourceDriftStatus.from_dict(d) for d in stack_instance_resource_drift_statuses]
    return web.Response(status=200)


async def g_et_list_stack_instances(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, filters=None, stack_instance_account=None, stack_instance_region=None, call_as=None) -> web.Response:
    """g_et_list_stack_instances

    Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.

    :param stack_set_name: The name or unique ID of the stack set that you want to list stack instances for.
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: If the previous request didn&#39;t return all the remaining results, the response&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call &lt;code&gt;ListStackInstances&lt;/code&gt; again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param filters: The filter to apply to stack instances
    :type filters: list | bytes
    :param stack_instance_account: The name of the Amazon Web Services account that you want to list stack instances for.
    :type stack_instance_account: str
    :param stack_instance_region: The name of the Region where you want to list stack instances.
    :type stack_instance_region: str
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    filters = [StackInstanceFilter.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_list_stack_resources(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_stack_resources

    &lt;p&gt;Returns descriptions of all resources of the specified stack.&lt;/p&gt; &lt;p&gt;For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.&lt;/p&gt;

    :param stack_name: &lt;p&gt;The name or the unique stack ID that is associated with the stack, which aren&#39;t always interchangeable:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Running stacks: You can specify either the stack&#39;s name or its unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deleted stacks: You must specify the unique stack ID.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: There is no default value.&lt;/p&gt;
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: A string that identifies the next page of stack resources that you want to retrieve.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_stack_set_operation_results(request: web.Request, stack_set_name, operation_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, call_as=None, filters=None) -> web.Response:
    """g_et_list_stack_set_operation_results

    Returns summary information about the results of a stack set operation.

    :param stack_set_name: The name or unique ID of the stack set that you want to get operation results for.
    :type stack_set_name: str
    :param operation_id: The ID of the stack set operation.
    :type operation_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: If the previous request didn&#39;t return all the remaining results, the response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call &lt;code&gt;ListStackSetOperationResults&lt;/code&gt; again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str
    :param filters: The filter to apply to operation results.
    :type filters: list | bytes

    """
    filters = [OperationResultFilter.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_list_stack_set_operations(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, call_as=None) -> web.Response:
    """g_et_list_stack_set_operations

    Returns summary information about operations performed on a stack set.

    :param stack_set_name: The name or unique ID of the stack set that you want to get operation summaries for.
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: If the previous paginated request didn&#39;t return all of the remaining results, the response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call &lt;code&gt;ListStackSetOperations&lt;/code&gt; again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_list_stack_sets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, status=None, call_as=None) -> web.Response:
    """g_et_list_stack_sets

    &lt;p&gt;Returns summary information about stack sets that are associated with the user.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;[Self-managed permissions] If you set the &lt;code&gt;CallAs&lt;/code&gt; parameter to &lt;code&gt;SELF&lt;/code&gt; while signed in to your Amazon Web Services account, &lt;code&gt;ListStackSets&lt;/code&gt; returns all self-managed stack sets in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;[Service-managed permissions] If you set the &lt;code&gt;CallAs&lt;/code&gt; parameter to &lt;code&gt;SELF&lt;/code&gt; while signed in to the organization&#39;s management account, &lt;code&gt;ListStackSets&lt;/code&gt; returns all stack sets in the management account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;[Service-managed permissions] If you set the &lt;code&gt;CallAs&lt;/code&gt; parameter to &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt; while signed in to your member account, &lt;code&gt;ListStackSets&lt;/code&gt; returns all stack sets with service-managed permissions in the management account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: If the previous paginated request didn&#39;t return all the remaining results, the response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call &lt;code&gt;ListStackSets&lt;/code&gt; again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param status: The status of the stack sets that you want to get summary information about.
    :type status: str
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_list_stacks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, stack_status_filter=None) -> web.Response:
    """g_et_list_stacks

    Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: A string that identifies the next page of stacks that you want to retrieve.
    :type next_token: str
    :param stack_status_filter: Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the &lt;code&gt;StackStatus&lt;/code&gt; parameter of the &lt;a&gt;Stack&lt;/a&gt; data type.
    :type stack_status_filter: list | bytes

    """
    stack_status_filter = [StackStatus.from_dict(d) for d in stack_status_filter]
    return web.Response(status=200)


async def g_et_list_type_registrations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, type_name=None, type_arn=None, registration_status_filter=None, max_results=None, next_token=None) -> web.Response:
    """g_et_list_type_registrations

    Returns a list of registration tokens for the specified extension(s).

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type: &lt;p&gt;The kind of extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param type_name: &lt;p&gt;The name of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param type_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type_arn: str
    :param registration_status_filter: &lt;p&gt;The current status of the extension registration request.&lt;/p&gt; &lt;p&gt;The default is &lt;code&gt;IN_PROGRESS&lt;/code&gt;.&lt;/p&gt;
    :type registration_status_filter: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param next_token: If the previous paginated request didn&#39;t return all the remaining results, the response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_type_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, type_name=None, arn=None, max_results=None, next_token=None, deprecated_status=None, publisher_id=None) -> web.Response:
    """g_et_list_type_versions

    Returns summary information about the versions of an extension.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type: &lt;p&gt;The kind of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param type_name: &lt;p&gt;The name of the extension for which you want version summary information.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param arn: &lt;p&gt;The Amazon Resource Name (ARN) of the extension for which you want version summary information.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type arn: str
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param next_token: If the previous paginated request didn&#39;t return all of the remaining results, the response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str
    :param deprecated_status: &lt;p&gt;The deprecation status of the extension versions that you want to get summary information about.&lt;/p&gt; &lt;p&gt;Valid values include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LIVE&lt;/code&gt;: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DEPRECATED&lt;/code&gt;: The extension version has been deregistered and can no longer be used in CloudFormation operations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The default is &lt;code&gt;LIVE&lt;/code&gt;.&lt;/p&gt;
    :type deprecated_status: str
    :param publisher_id: &lt;p&gt;The publisher ID of the extension publisher.&lt;/p&gt; &lt;p&gt;Extensions published by Amazon aren&#39;t assigned a publisher ID.&lt;/p&gt;
    :type publisher_id: str

    """
    return web.Response(status=200)


async def g_et_list_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, visibility=None, provisioning_type=None, deprecated_status=None, type=None, filters=None, max_results=None, next_token=None) -> web.Response:
    """g_et_list_types

    Returns summary information about extension that have been registered with CloudFormation.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param visibility: &lt;p&gt;The scope at which the extensions are visible and usable in CloudFormation operations.&lt;/p&gt; &lt;p&gt;Valid values include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PRIVATE&lt;/code&gt;: Extensions that are visible and usable within this account and Region. This includes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Private extensions you have registered in this account and Region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Public extensions that you have activated in this account and Region.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PUBLIC&lt;/code&gt;: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services, in addition to third-party publishers.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The default is &lt;code&gt;PRIVATE&lt;/code&gt;.&lt;/p&gt;
    :type visibility: str
    :param provisioning_type: &lt;p&gt;For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.&lt;/p&gt; &lt;p&gt;Valid values include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FULLY_MUTABLE&lt;/code&gt;: The resource type includes an update handler to process updates to the type during stack update operations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IMMUTABLE&lt;/code&gt;: The resource type doesn&#39;t include an update handler, so the type can&#39;t be updated and must instead be replaced during stack update operations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NON_PROVISIONABLE&lt;/code&gt;: The resource type doesn&#39;t include create, read, and delete handlers, and therefore can&#39;t actually be provisioned.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The default is &lt;code&gt;FULLY_MUTABLE&lt;/code&gt;.&lt;/p&gt;
    :type provisioning_type: str
    :param deprecated_status: &lt;p&gt;The deprecation status of the extension that you want to get summary information about.&lt;/p&gt; &lt;p&gt;Valid values include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LIVE&lt;/code&gt;: The extension is registered for use in CloudFormation operations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DEPRECATED&lt;/code&gt;: The extension has been deregistered and can no longer be used in CloudFormation operations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type deprecated_status: str
    :param type: The type of extension.
    :type type: str
    :param filters: &lt;p&gt;Filter criteria to use in determining which extensions to return.&lt;/p&gt; &lt;p&gt;Filters must be compatible with &lt;code&gt;Visibility&lt;/code&gt; to return valid results. For example, specifying &lt;code&gt;AWS_TYPES&lt;/code&gt; for &lt;code&gt;Category&lt;/code&gt; and &lt;code&gt;PRIVATE&lt;/code&gt; for &lt;code&gt;Visibility&lt;/code&gt; returns an empty list of types, but specifying &lt;code&gt;PUBLIC&lt;/code&gt; for &lt;code&gt;Visibility&lt;/code&gt; returns the desired list.&lt;/p&gt;
    :type filters: dict | bytes
    :param max_results: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a &lt;code&gt;NextToken&lt;/code&gt; value that you can assign to the &lt;code&gt;NextToken&lt;/code&gt; request parameter to get the next set of results.
    :type max_results: int
    :param next_token: If the previous paginated request didn&#39;t return all the remaining results, the response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s &lt;code&gt;NextToken&lt;/code&gt; parameter is set to &lt;code&gt;null&lt;/code&gt;.
    :type next_token: str

    """
    filters = .from_dict(filters)
    return web.Response(status=200)


async def g_et_publish_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, arn=None, type_name=None, public_version_number=None) -> web.Response:
    """g_et_publish_type

    &lt;p&gt;Publishes the specified extension to the CloudFormation registry as a public extension in this Region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html\&quot;&gt;Publishing extensions to make them available for public use&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html\&quot;&gt;RegisterPublisher&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type: &lt;p&gt;The type of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param arn: &lt;p&gt;The Amazon Resource Name (ARN) of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type arn: str
    :param type_name: &lt;p&gt;The name of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param public_version_number: &lt;p&gt;The version number to assign to this version of the extension.&lt;/p&gt; &lt;p&gt;Use the following format, and adhere to semantic versioning when assigning a version number to your extension:&lt;/p&gt; &lt;p&gt; &lt;code&gt;MAJOR.MINOR.PATCH&lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://semver.org/\&quot;&gt;Semantic Versioning 2.0.0&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a version number, CloudFormation increments the version number by one minor version release.&lt;/p&gt; &lt;p&gt;You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be &lt;code&gt;1.0.0&lt;/code&gt;.&lt;/p&gt;
    :type public_version_number: str

    """
    return web.Response(status=200)


async def g_et_record_handler_progress(request: web.Request, bearer_token, operation_status, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, current_operation_status=None, status_message=None, error_code=None, resource_model=None, client_request_token=None) -> web.Response:
    """g_et_record_handler_progress

    &lt;p&gt;Reports progress of a resource handler to CloudFormation.&lt;/p&gt; &lt;p&gt;Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;. Don&#39;t use this API in your code.&lt;/p&gt;

    :param bearer_token: Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;.
    :type bearer_token: str
    :param operation_status: Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;.
    :type operation_status: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param current_operation_status: Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;.
    :type current_operation_status: str
    :param status_message: Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;.
    :type status_message: str
    :param error_code: Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;.
    :type error_code: str
    :param resource_model: Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;.
    :type resource_model: str
    :param client_request_token: Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;.
    :type client_request_token: str

    """
    return web.Response(status=200)


async def g_et_register_publisher(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, accept_terms_and_conditions=None, connection_arn=None) -> web.Response:
    """g_et_register_publisher

    &lt;p&gt;Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.&lt;/p&gt; &lt;p&gt;For information about requirements for registering as a public extension publisher, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs\&quot;&gt;Registering your account to publish CloudFormation extensions&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param accept_terms_and_conditions: &lt;p&gt;Whether you accept the &lt;a href&#x3D;\&quot;https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf\&quot;&gt;Terms and Conditions&lt;/a&gt; for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.&lt;/p&gt; &lt;p&gt;The default is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt;
    :type accept_terms_and_conditions: bool
    :param connection_arn: &lt;p&gt;If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs\&quot;&gt;Registering your account to publish CloudFormation extensions&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt;
    :type connection_arn: str

    """
    return web.Response(status=200)


async def g_et_register_type(request: web.Request, type_name, schema_handler_package, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, logging_config=None, execution_role_arn=None, client_request_token=None) -> web.Response:
    """g_et_register_type

    &lt;p&gt;Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Validating the extension schema.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Determining which handlers, if any, have been specified for the extension.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Making the extension available for use in your account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about how to develop extensions and ready them for registration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html\&quot;&gt;Creating Resource Providers&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per Region. Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html\&quot;&gt;DeregisterType&lt;/a&gt; to deregister specific extension versions if necessary.&lt;/p&gt; &lt;p&gt;Once you have initiated a registration request using &lt;a&gt;RegisterType&lt;/a&gt;, you can use &lt;a&gt;DescribeTypeRegistration&lt;/a&gt; to monitor the progress of the registration request.&lt;/p&gt; &lt;p&gt;Once you have registered a private extension in your account and Region, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html\&quot;&gt;SetTypeConfiguration&lt;/a&gt; to specify configuration properties for the extension. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt;

    :param type_name: &lt;p&gt;The name of the extension being registered.&lt;/p&gt; &lt;p&gt;We suggest that extension names adhere to the following patterns:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For resource types, &lt;i&gt;company_or_organization&lt;/i&gt;::&lt;i&gt;service&lt;/i&gt;::&lt;i&gt;type&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For modules, &lt;i&gt;company_or_organization&lt;/i&gt;::&lt;i&gt;service&lt;/i&gt;::&lt;i&gt;type&lt;/i&gt;::MODULE.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For hooks, &lt;i&gt;MyCompany&lt;/i&gt;::&lt;i&gt;Testing&lt;/i&gt;::&lt;i&gt;MyTestHook&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The following organization namespaces are reserved and can&#39;t be used in your extension names:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Alexa&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AMZN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Amazon&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Custom&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Dev&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;
    :type type_name: str
    :param schema_handler_package: &lt;p&gt;A URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register.&lt;/p&gt; &lt;p&gt;For information about generating a schema handler package for the extension you want to register, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html\&quot;&gt;submit&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The user registering the extension must be able to access the package in the S3 bucket. That&#39;s, the user needs to have &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html\&quot;&gt;GetObject&lt;/a&gt; permissions for the schema handler package. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html\&quot;&gt;Actions, Resources, and Condition Keys for Amazon S3&lt;/a&gt; in the &lt;i&gt;Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
    :type schema_handler_package: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type: The kind of extension.
    :type type: str
    :param logging_config: Specifies logging configuration information for an extension.
    :type logging_config: dict | bytes
    :param execution_role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.&lt;/p&gt; &lt;p&gt;For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principle (&lt;code&gt;resources.cloudformation.amazonaws.com&lt;/code&gt;). For more information about adding trust relationships, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy\&quot;&gt;Modifying a role trust policy&lt;/a&gt; in the &lt;i&gt;Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If your extension calls Amazon Web Services APIs in any of its handlers, you must create an &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html\&quot;&gt;IAM execution role&lt;/a&gt; &lt;/i&gt; that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.&lt;/p&gt;
    :type execution_role_arn: str
    :param client_request_token: A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.
    :type client_request_token: str

    """
    logging_config = .from_dict(logging_config)
    return web.Response(status=200)


async def g_et_rollback_stack(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, role_arn=None, client_request_token=None, retain_except_on_create=None) -> web.Response:
    """g_et_rollback_stack

    &lt;p&gt;When specifying &lt;code&gt;RollbackStack&lt;/code&gt;, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the &lt;a&gt;DescribeStacks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;Rolls back the specified stack to the last known stable state from &lt;code&gt;CREATE_FAILED&lt;/code&gt; or &lt;code&gt;UPDATE_FAILED&lt;/code&gt; stack statuses.&lt;/p&gt; &lt;p&gt;This operation will delete a stack if it doesn&#39;t contain a last known stable state. A last known stable state includes any status in a &lt;code&gt;*_COMPLETE&lt;/code&gt;. This includes the following stack statuses.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CREATE_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UPDATE_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UPDATE_ROLLBACK_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IMPORT_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IMPORT_ROLLBACK_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param stack_name: The name that&#39;s associated with the stack.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param role_arn: The Amazon Resource Name (ARN) of an Identity and Access Management role that CloudFormation assumes to rollback the stack.
    :type role_arn: str
    :param client_request_token: A unique identifier for this &lt;code&gt;RollbackStack&lt;/code&gt; request.
    :type client_request_token: str
    :param retain_except_on_create: This deletion policy deletes newly created resources, but retains existing resources, when a stack operation is rolled back. This ensures new, empty, and unused resources are deleted, while critical resources and their data are retained. &lt;code&gt;RetainExceptOnCreate&lt;/code&gt; can be specified for any resource that supports the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html\&quot;&gt; DeletionPolicy&lt;/a&gt; attribute.
    :type retain_except_on_create: bool

    """
    return web.Response(status=200)


async def g_et_set_stack_policy(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stack_policy_body=None, stack_policy_url=None) -> web.Response:
    """g_et_set_stack_policy

    Sets a stack policy for a specified stack.

    :param stack_name: The name or unique stack ID that you want to associate a policy with.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param stack_policy_body: Structure containing the stack policy body. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html\&quot;&gt; Prevent updates to stack resources&lt;/a&gt; in the CloudFormation User Guide. You can specify either the &lt;code&gt;StackPolicyBody&lt;/code&gt; or the &lt;code&gt;StackPolicyURL&lt;/code&gt; parameter, but not both.
    :type stack_policy_body: str
    :param stack_policy_url: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. You can specify either the &lt;code&gt;StackPolicyBody&lt;/code&gt; or the &lt;code&gt;StackPolicyURL&lt;/code&gt; parameter, but not both.
    :type stack_policy_url: str

    """
    return web.Response(status=200)


async def g_et_set_type_configuration(request: web.Request, configuration, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type_arn=None, configuration_alias=None, type_name=None, type=None) -> web.Response:
    """g_et_set_type_configuration

    &lt;p&gt;Specifies the configuration data for a registered CloudFormation extension, in the given account and Region.&lt;/p&gt; &lt;p&gt;To view the current configuration data for an extension, refer to the &lt;code&gt;ConfigurationSchema&lt;/code&gt; element of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html\&quot;&gt;DescribeType&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It&#39;s strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/\&quot;&gt;Using dynamic references to specify template values&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param configuration: &lt;p&gt;The configuration data for the extension, in this account and Region.&lt;/p&gt; &lt;p&gt;The configuration data must be formatted as JSON, and validate against the schema returned in the &lt;code&gt;ConfigurationSchema&lt;/code&gt; response element of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html\&quot;&gt;DescribeType&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration\&quot;&gt;Defining account-level configuration data for an extension&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt;
    :type configuration: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param type_arn: &lt;p&gt;The Amazon Resource Name (ARN) for the extension, in this account and Region.&lt;/p&gt; &lt;p&gt;For public extensions, this will be the ARN assigned when you &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html\&quot;&gt;activate the type&lt;/a&gt; in this account and Region. For private extensions, this will be the ARN assigned when you &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html\&quot;&gt;register the type&lt;/a&gt; in this account and Region.&lt;/p&gt; &lt;p&gt;Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.&lt;/p&gt;
    :type type_arn: str
    :param configuration_alias: &lt;p&gt;An alias by which to refer to this extension configuration data.&lt;/p&gt; &lt;p&gt;Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.&lt;/p&gt;
    :type configuration_alias: str
    :param type_name: &lt;p&gt;The name of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;ConfigurationArn&lt;/code&gt;, or &lt;code&gt;Type&lt;/code&gt; and &lt;code&gt;TypeName&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param type: &lt;p&gt;The type of extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;ConfigurationArn&lt;/code&gt;, or &lt;code&gt;Type&lt;/code&gt; and &lt;code&gt;TypeName&lt;/code&gt;.&lt;/p&gt;
    :type type: str

    """
    return web.Response(status=200)


async def g_et_set_type_default_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, arn=None, type=None, type_name=None, version_id=None) -> web.Response:
    """g_et_set_type_default_version

    Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param arn: &lt;p&gt;The Amazon Resource Name (ARN) of the extension for which you want version summary information.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type arn: str
    :param type: &lt;p&gt;The kind of extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param type_name: &lt;p&gt;The name of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify either &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;, or &lt;code&gt;Arn&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param version_id: The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.
    :type version_id: str

    """
    return web.Response(status=200)


async def g_et_signal_resource(request: web.Request, stack_name, logical_resource_id, unique_id, status, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_signal_resource

    Sends a signal to the specified resource with a success or failure status. You can use the &lt;code&gt;SignalResource&lt;/code&gt; operation in conjunction with a creation policy or update policy. CloudFormation doesn&#39;t proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The &lt;code&gt;SignalResource&lt;/code&gt; operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.

    :param stack_name: The stack name or unique stack ID that includes the resource that you want to signal.
    :type stack_name: str
    :param logical_resource_id: The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.
    :type logical_resource_id: str
    :param unique_id: A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.
    :type unique_id: str
    :param status: The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.
    :type status: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_stop_stack_set_operation(request: web.Request, stack_set_name, operation_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, call_as=None) -> web.Response:
    """g_et_stop_stack_set_operation

    Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

    :param stack_set_name: The name or unique ID of the stack set that you want to stop the operation for.
    :type stack_set_name: str
    :param operation_id: The ID of the stack operation.
    :type operation_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    return web.Response(status=200)


async def g_et_test_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, arn=None, type=None, type_name=None, version_id=None, log_delivery_bucket=None) -> web.Response:
    """g_et_test_type

    &lt;p&gt;Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For resource types, this includes passing all contracts tests defined for the type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For modules, this includes determining if the module&#39;s model meets all necessary requirements.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing\&quot;&gt;Testing your public extension prior to publishing&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a version, CloudFormation uses the default version of the extension in your account and Region for testing.&lt;/p&gt; &lt;p&gt;To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html\&quot;&gt;RegisterType&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Once you&#39;ve initiated testing on an extension using &lt;code&gt;TestType&lt;/code&gt;, you can pass the returned &lt;code&gt;TypeVersionArn&lt;/code&gt; into &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html\&quot;&gt;DescribeType&lt;/a&gt; to monitor the current test status and test status description for the extension.&lt;/p&gt; &lt;p&gt;An extension must have a test status of &lt;code&gt;PASSED&lt;/code&gt; before it can be published. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html\&quot;&gt;Publishing extensions to make them available for public use&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param arn: &lt;p&gt;The Amazon Resource Name (ARN) of the extension.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type arn: str
    :param type: &lt;p&gt;The type of the extension to test.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type type: str
    :param type_name: &lt;p&gt;The name of the extension to test.&lt;/p&gt; &lt;p&gt;Conditional: You must specify &lt;code&gt;Arn&lt;/code&gt;, or &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt;
    :type type_name: str
    :param version_id: &lt;p&gt;The version of the extension to test.&lt;/p&gt; &lt;p&gt;You can specify the version id with either &lt;code&gt;Arn&lt;/code&gt;, or with &lt;code&gt;TypeName&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a version, CloudFormation uses the default version of the extension in this account and Region for testing.&lt;/p&gt;
    :type version_id: str
    :param log_delivery_bucket: &lt;p&gt;The S3 bucket to which CloudFormation delivers the contract test execution logs.&lt;/p&gt; &lt;p&gt;CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of &lt;code&gt;PASSED&lt;/code&gt; or &lt;code&gt;FAILED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The user calling &lt;code&gt;TestType&lt;/code&gt; must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetObject&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PutObject&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html\&quot;&gt;Actions, Resources, and Condition Keys for Amazon S3&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt;
    :type log_delivery_bucket: str

    """
    return web.Response(status=200)


async def g_et_update_stack(request: web.Request, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_body=None, template_url=None, use_previous_template=None, stack_policy_during_update_body=None, stack_policy_during_update_url=None, parameters=None, capabilities=None, resource_types=None, role_arn=None, rollback_configuration=None, stack_policy_body=None, stack_policy_url=None, notification_arns=None, tags=None, disable_rollback=None, client_request_token=None, retain_except_on_create=None) -> web.Response:
    """g_et_update_stack

    &lt;p&gt;Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the &lt;a&gt;DescribeStacks&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;To get a copy of the template for an existing stack, you can use the &lt;a&gt;GetTemplate&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about creating an update template, updating a stack, and monitoring the progress of the update, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html\&quot;&gt;Updating a Stack&lt;/a&gt;.&lt;/p&gt;

    :param stack_name: The name or unique stack ID of the stack to update.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_body: &lt;p&gt;Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.)&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;TemplateBody&lt;/code&gt;, &lt;code&gt;TemplateURL&lt;/code&gt;, or set the &lt;code&gt;UsePreviousTemplate&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;Location of file containing the template body. The URL must point to a template that&#39;s located in an Amazon S3 bucket or a Systems Manager document. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;TemplateBody&lt;/code&gt;, &lt;code&gt;TemplateURL&lt;/code&gt;, or set the &lt;code&gt;UsePreviousTemplate&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;
    :type template_url: str
    :param use_previous_template: &lt;p&gt;Reuse the existing template that is associated with the stack that you are updating.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;TemplateBody&lt;/code&gt;, &lt;code&gt;TemplateURL&lt;/code&gt;, or set the &lt;code&gt;UsePreviousTemplate&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;
    :type use_previous_template: bool
    :param stack_policy_during_update_body: &lt;p&gt;Structure containing the temporary overriding stack policy body. You can specify either the &lt;code&gt;StackPolicyDuringUpdateBody&lt;/code&gt; or the &lt;code&gt;StackPolicyDuringUpdateURL&lt;/code&gt; parameter, but not both.&lt;/p&gt; &lt;p&gt;If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don&#39;t specify a stack policy, the current policy that is associated with the stack will be used.&lt;/p&gt;
    :type stack_policy_during_update_body: str
    :param stack_policy_during_update_url: &lt;p&gt;Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the &lt;code&gt;StackPolicyDuringUpdateBody&lt;/code&gt; or the &lt;code&gt;StackPolicyDuringUpdateURL&lt;/code&gt; parameter, but not both.&lt;/p&gt; &lt;p&gt;If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don&#39;t specify a stack policy, the current policy that is associated with the stack will be used.&lt;/p&gt;
    :type stack_policy_during_update_url: str
    :param parameters: A list of &lt;code&gt;Parameter&lt;/code&gt; structures that specify input parameters for the stack. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html\&quot;&gt;Parameter&lt;/a&gt; data type.
    :type parameters: list | bytes
    :param capabilities: &lt;p&gt;In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; and &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.&lt;/p&gt; &lt;p&gt;The following IAM resources require you to specify either the &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; or &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; capability.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources, you can specify either capability.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources with custom names, you &lt;i&gt;must&lt;/i&gt; specify &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify either of these capabilities, CloudFormation returns an &lt;code&gt;InsufficientCapabilities&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html\&quot;&gt; AWS::IAM::AccessKey&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html\&quot;&gt; AWS::IAM::Group&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html\&quot;&gt;AWS::IAM::InstanceProfile&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html\&quot;&gt; AWS::IAM::Policy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html\&quot;&gt; AWS::IAM::Role&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html\&quot;&gt; AWS::IAM::User&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html\&quot;&gt;AWS::IAM::UserToGroupAddition&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities\&quot;&gt;Acknowledging IAM Resources in CloudFormation Templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_AUTO_EXPAND&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually updating the stack. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html\&quot;&gt;AWS::Include&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html\&quot;&gt;AWS::Serverless&lt;/a&gt; transforms, which are macros hosted by CloudFormation.&lt;/p&gt; &lt;p&gt;If you want to update a stack from a stack template that contains macros &lt;i&gt;and&lt;/i&gt; nested stacks, you must update the stack directly from the template using this capability.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You should only update stacks directly from a stack template that contains macros if you know what processing the macro performs.&lt;/p&gt; &lt;p&gt;Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html\&quot;&gt;Using CloudFormation Macros to Perform Custom Processing on Templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type capabilities: list | bytes
    :param resource_types: &lt;p&gt;The template resource types that you have permissions to work with for this update stack action, such as &lt;code&gt;AWS::EC2::Instance&lt;/code&gt;, &lt;code&gt;AWS::EC2::*&lt;/code&gt;, or &lt;code&gt;Custom::MyCustomInstance&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If the list of resource types doesn&#39;t include a resource that you&#39;re updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html\&quot;&gt;Controlling Access with Identity and Access Management&lt;/a&gt;.&lt;/p&gt;
    :type resource_types: List[str]
    :param role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to update the stack. CloudFormation uses the role&#39;s credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don&#39;t have permission to pass it. Ensure that the role grants least privilege.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.&lt;/p&gt;
    :type role_arn: str
    :param rollback_configuration: The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    :type rollback_configuration: dict | bytes
    :param stack_policy_body: &lt;p&gt;Structure containing a new stack policy body. You can specify either the &lt;code&gt;StackPolicyBody&lt;/code&gt; or the &lt;code&gt;StackPolicyURL&lt;/code&gt; parameter, but not both.&lt;/p&gt; &lt;p&gt;You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don&#39;t specify a stack policy, the current policy that is associated with the stack is unchanged.&lt;/p&gt;
    :type stack_policy_body: str
    :param stack_policy_url: &lt;p&gt;Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the &lt;code&gt;StackPolicyBody&lt;/code&gt; or the &lt;code&gt;StackPolicyURL&lt;/code&gt; parameter, but not both.&lt;/p&gt; &lt;p&gt;You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don&#39;t specify a stack policy, the current policy that is associated with the stack is unchanged.&lt;/p&gt;
    :type stack_policy_url: str
    :param notification_arns: Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation associates with the stack. Specify an empty list to remove all notification topics.
    :type notification_arns: List[str]
    :param tags: &lt;p&gt;Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify this parameter, CloudFormation doesn&#39;t modify the stack&#39;s tags. If you specify an empty value, CloudFormation removes all associated tags.&lt;/p&gt;
    :type tags: list | bytes
    :param disable_rollback: &lt;p&gt;Preserve the state of previously provisioned resources when an operation fails.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;False&lt;/code&gt; &lt;/p&gt;
    :type disable_rollback: bool
    :param client_request_token: &lt;p&gt;A unique identifier for this &lt;code&gt;UpdateStack&lt;/code&gt; request. Specify this token if you plan to retry requests so that CloudFormation knows that you&#39;re not attempting to update a stack with the same name. You might retry &lt;code&gt;UpdateStack&lt;/code&gt; requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a &lt;code&gt;CreateStack&lt;/code&gt; operation with the token &lt;code&gt;token1&lt;/code&gt;, then all the &lt;code&gt;StackEvents&lt;/code&gt; generated by that operation will have &lt;code&gt;ClientRequestToken&lt;/code&gt; set as &lt;code&gt;token1&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format &lt;i&gt;Console-StackOperation-ID&lt;/i&gt;, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: &lt;code&gt;Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002&lt;/code&gt;.&lt;/p&gt;
    :type client_request_token: str
    :param retain_except_on_create: This deletion policy deletes newly created resources, but retains existing resources, when a stack operation is rolled back. This ensures new, empty, and unused resources are deleted, while critical resources and their data are retained. &lt;code&gt;RetainExceptOnCreate&lt;/code&gt; can be specified for any resource that supports the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html\&quot;&gt; DeletionPolicy&lt;/a&gt; attribute.
    :type retain_except_on_create: bool

    """
    parameters = [Parameter.from_dict(d) for d in parameters]
    capabilities = [Capability.from_dict(d) for d in capabilities]
    rollback_configuration = .from_dict(rollback_configuration)
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_update_stack_instances(request: web.Request, stack_set_name, regions, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, accounts=None, deployment_targets=None, parameter_overrides=None, operation_preferences=None, operation_id=None, call_as=None) -> web.Response:
    """g_et_update_stack_instances

    &lt;p&gt;Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.&lt;/p&gt; &lt;p&gt;You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html\&quot;&gt;CreateStackInstances&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;During stack set updates, any parameters overridden for a stack instance aren&#39;t updated, but retain their overridden value.&lt;/p&gt; &lt;p&gt;You can only update the parameter &lt;i&gt;values&lt;/i&gt; that are specified in the stack set; to add or delete a parameter itself, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html\&quot;&gt;UpdateStackSet&lt;/a&gt; to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html\&quot;&gt;UpdateStackSet&lt;/a&gt; to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using &lt;code&gt;UpdateStackInstances&lt;/code&gt;.&lt;/p&gt;

    :param stack_set_name: The name or unique ID of the stack set associated with the stack instances.
    :type stack_set_name: str
    :param regions: The names of one or more Amazon Web Services Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.
    :type regions: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param accounts: &lt;p&gt;[Self-managed permissions] The names of one or more Amazon Web Services accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, but not both.&lt;/p&gt;
    :type accounts: List[str]
    :param deployment_targets: &lt;p&gt;[Service-managed permissions] The Organizations accounts for which you want to update parameter values for stack instances. If your update targets OUs, the overridden parameter values only apply to the accounts that are currently in the target OUs and their child OUs. Accounts added to the target OUs and their child OUs in the future won&#39;t use the overridden values.&lt;/p&gt; &lt;p&gt;You can specify &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, but not both.&lt;/p&gt;
    :type deployment_targets: dict | bytes
    :param parameter_overrides: &lt;p&gt;A list of input parameters whose values you want to update for the specified stack instances.&lt;/p&gt; &lt;p&gt;Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance update operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To override the current value for a parameter, include the parameter and specify its value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To leave an overridden parameter set to its present value, include the parameter and specify &lt;code&gt;UsePreviousValue&lt;/code&gt; as &lt;code&gt;true&lt;/code&gt;. (You can&#39;t specify both a value and set &lt;code&gt;UsePreviousValue&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don&#39;t include the parameter in the list.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To leave all parameters set to their present values, don&#39;t specify this property at all.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;During stack set updates, any parameter values overridden for a stack instance aren&#39;t updated, but retain their overridden value.&lt;/p&gt; &lt;p&gt;You can only override the parameter &lt;i&gt;values&lt;/i&gt; that are specified in the stack set; to add or delete a parameter itself, use &lt;code&gt;UpdateStackSet&lt;/code&gt; to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html\&quot;&gt;UpdateStackSet&lt;/a&gt; to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using &lt;code&gt;UpdateStackInstances&lt;/code&gt;.&lt;/p&gt;
    :type parameter_overrides: list | bytes
    :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
    :type operation_preferences: dict | bytes
    :param operation_id: &lt;p&gt;The unique identifier for this stack set operation.&lt;/p&gt; &lt;p&gt;The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify an operation ID, the SDK generates one automatically.&lt;/p&gt;
    :type operation_id: str
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str

    """
    deployment_targets = .from_dict(deployment_targets)
    parameter_overrides = [Parameter.from_dict(d) for d in parameter_overrides]
    operation_preferences = .from_dict(operation_preferences)
    return web.Response(status=200)


async def g_et_update_stack_set(request: web.Request, stack_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None, template_body=None, template_url=None, use_previous_template=None, parameters=None, capabilities=None, tags=None, operation_preferences=None, administration_role_arn=None, execution_role_name=None, deployment_targets=None, permission_model=None, auto_deployment=None, operation_id=None, accounts=None, regions=None, call_as=None, managed_execution=None) -> web.Response:
    """g_et_update_stack_set

    &lt;p&gt;Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.&lt;/p&gt; &lt;p&gt;Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent &lt;a&gt;CreateStackInstances&lt;/a&gt; calls on the specified stack set use the updated stack set.&lt;/p&gt;

    :param stack_set_name: The name or unique ID of the stack set that you want to update.
    :type stack_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param description: A brief description of updates that you are making.
    :type description: str
    :param template_body: &lt;p&gt;The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt;—or set &lt;code&gt;UsePreviousTemplate&lt;/code&gt; to true.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt;—or set &lt;code&gt;UsePreviousTemplate&lt;/code&gt; to true.&lt;/p&gt;
    :type template_url: str
    :param use_previous_template: &lt;p&gt;Use the existing template that&#39;s associated with the stack set that you&#39;re updating.&lt;/p&gt; &lt;p&gt;Conditional: You must specify only one of the following parameters: &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt;—or set &lt;code&gt;UsePreviousTemplate&lt;/code&gt; to true.&lt;/p&gt;
    :type use_previous_template: bool
    :param parameters: A list of input parameters for the stack set template.
    :type parameters: list | bytes
    :param capabilities: &lt;p&gt;In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack set and its associated stack instances.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; and &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities.&lt;/p&gt; &lt;p&gt;The following IAM resources require you to specify either the &lt;code&gt;CAPABILITY_IAM&lt;/code&gt; or &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt; capability.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources, you can specify either capability.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you have IAM resources with custom names, you &lt;i&gt;must&lt;/i&gt; specify &lt;code&gt;CAPABILITY_NAMED_IAM&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify either of these capabilities, CloudFormation returns an &lt;code&gt;InsufficientCapabilities&lt;/code&gt; error.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html\&quot;&gt; AWS::IAM::AccessKey&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html\&quot;&gt; AWS::IAM::Group&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html\&quot;&gt; AWS::IAM::InstanceProfile&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html\&quot;&gt; AWS::IAM::Policy&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html\&quot;&gt; AWS::IAM::Role&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html\&quot;&gt; AWS::IAM::User&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html\&quot;&gt; AWS::IAM::UserToGroupAddition&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/using-iam-template.html#capabilities\&quot;&gt;Acknowledging IAM Resources in CloudFormation Templates&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CAPABILITY_AUTO_EXPAND&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Some templates reference macros. If your stack set template references one or more macros, you must update the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To update the stack set directly, you must acknowledge this capability. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/template-macros.html\&quot;&gt;Using CloudFormation Macros to Perform Custom Processing on Templates&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Stack sets with service-managed permissions do not currently support the use of macros in templates. (This includes the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html\&quot;&gt;AWS::Include&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/transform-aws-serverless.html\&quot;&gt;AWS::Serverless&lt;/a&gt; transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ul&gt;
    :type capabilities: list | bytes
    :param tags: &lt;p&gt;The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.&lt;/p&gt; &lt;p&gt;If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you don&#39;t specify this parameter, CloudFormation doesn&#39;t modify the stack&#39;s tags.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you specify &lt;i&gt;any&lt;/i&gt; tags using this parameter, you must specify &lt;i&gt;all&lt;/i&gt; the tags that you want associated with this stack set, even tags you&#39;ve specified before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don&#39;t include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you specify an empty value, CloudFormation removes all currently associated tags.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify new tags as part of an &lt;code&gt;UpdateStackSet&lt;/code&gt; action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you don&#39;t have the necessary permission(s), the entire &lt;code&gt;UpdateStackSet&lt;/code&gt; action fails with an &lt;code&gt;access denied&lt;/code&gt; error, and the stack set is not updated.&lt;/p&gt;
    :type tags: list | bytes
    :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
    :type operation_preferences: dict | bytes
    :param administration_role_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the IAM role to use to update this stack set.&lt;/p&gt; &lt;p&gt;Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/stacksets-prereqs.html\&quot;&gt;Granting Permissions for Stack Set Operations&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specified a customized administrator role when you created the stack set, you must specify a customized administrator role, even if it is the same customized administrator role used with this stack set previously.&lt;/p&gt;
    :type administration_role_arn: str
    :param execution_role_name: &lt;p&gt;The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, CloudFormation uses the &lt;code&gt;AWSCloudFormationStackSetExecutionRole&lt;/code&gt; role for the stack set operation.&lt;/p&gt; &lt;p&gt;Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.&lt;/p&gt; &lt;p&gt;If you specify a customized execution role, CloudFormation uses that role to update the stack. If you do not specify a customized execution role, CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.&lt;/p&gt;
    :type execution_role_name: str
    :param deployment_targets: &lt;p&gt;[Service-managed permissions] The Organizations accounts in which to update associated stack instances.&lt;/p&gt; &lt;p&gt;To update all the stack instances associated with this stack set, do not specify &lt;code&gt;DeploymentTargets&lt;/code&gt; or &lt;code&gt;Regions&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If the stack set update includes changes to the template (that is, if &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt; is specified), or the &lt;code&gt;Parameters&lt;/code&gt;, CloudFormation marks all stack instances with a status of &lt;code&gt;OUTDATED&lt;/code&gt; prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update doesn&#39;t include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.&lt;/p&gt;
    :type deployment_targets: dict | bytes
    :param permission_model: &lt;p&gt;Describes how the IAM roles required for stack set operations are created. You cannot modify &lt;code&gt;PermissionModel&lt;/code&gt; if there are stack instances associated with your stack set.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;With &lt;code&gt;self-managed&lt;/code&gt; permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html\&quot;&gt;Grant Self-Managed Stack Set Permissions&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;With &lt;code&gt;service-managed&lt;/code&gt; permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html\&quot;&gt;Grant Service-Managed Stack Set Permissions&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type permission_model: str
    :param auto_deployment: &lt;p&gt;[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU).&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;AutoDeployment&lt;/code&gt;, don&#39;t specify &lt;code&gt;DeploymentTargets&lt;/code&gt; or &lt;code&gt;Regions&lt;/code&gt;.&lt;/p&gt;
    :type auto_deployment: dict | bytes
    :param operation_id: &lt;p&gt;The unique ID for this stack set operation.&lt;/p&gt; &lt;p&gt;The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify an operation ID, CloudFormation generates one automatically.&lt;/p&gt; &lt;p&gt;Repeating this stack set operation with a new operation ID retries all stack instances whose status is &lt;code&gt;OUTDATED&lt;/code&gt;.&lt;/p&gt;
    :type operation_id: str
    :param accounts: &lt;p&gt;[Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Amazon Web Services Regions in which to update stack set instances.&lt;/p&gt; &lt;p&gt;To update &lt;i&gt;all&lt;/i&gt; the stack instances associated with this stack set, don&#39;t specify the &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;Regions&lt;/code&gt; properties.&lt;/p&gt; &lt;p&gt;If the stack set update includes changes to the template (that is, if the &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt; properties are specified), or the &lt;code&gt;Parameters&lt;/code&gt; property, CloudFormation marks all stack instances with a status of &lt;code&gt;OUTDATED&lt;/code&gt; prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Amazon Web Services Regions, while leaving all other stack instances with their existing stack instance status.&lt;/p&gt;
    :type accounts: List[str]
    :param regions: &lt;p&gt;The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update stack set instances.&lt;/p&gt; &lt;p&gt;To update &lt;i&gt;all&lt;/i&gt; the stack instances associated with this stack set, do not specify the &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;Regions&lt;/code&gt; properties.&lt;/p&gt; &lt;p&gt;If the stack set update includes changes to the template (that is, if the &lt;code&gt;TemplateBody&lt;/code&gt; or &lt;code&gt;TemplateURL&lt;/code&gt; properties are specified), or the &lt;code&gt;Parameters&lt;/code&gt; property, CloudFormation marks all stack instances with a status of &lt;code&gt;OUTDATED&lt;/code&gt; prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.&lt;/p&gt;
    :type regions: List[str]
    :param call_as: &lt;p&gt;[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization&#39;s management account or as a delegated administrator in a member account.&lt;/p&gt; &lt;p&gt;By default, &lt;code&gt;SELF&lt;/code&gt; is specified. Use &lt;code&gt;SELF&lt;/code&gt; for stack sets with self-managed permissions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are signed in to the management account, specify &lt;code&gt;SELF&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are signed in to a delegated administrator account, specify &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html\&quot;&gt;Register a delegated administrator&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type call_as: str
    :param managed_execution: Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
    :type managed_execution: dict | bytes

    """
    parameters = [Parameter.from_dict(d) for d in parameters]
    capabilities = [Capability.from_dict(d) for d in capabilities]
    tags = [Tag.from_dict(d) for d in tags]
    operation_preferences = .from_dict(operation_preferences)
    deployment_targets = .from_dict(deployment_targets)
    auto_deployment = .from_dict(auto_deployment)
    managed_execution = .from_dict(managed_execution)
    return web.Response(status=200)


async def g_et_update_termination_protection(request: web.Request, enable_termination_protection, stack_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_termination_protection

    &lt;p&gt;Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html\&quot;&gt;Protecting a Stack From Being Deleted&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html\&quot;&gt;nested stacks&lt;/a&gt;, termination protection is set on the root stack and can&#39;t be changed directly on the nested stack.&lt;/p&gt;

    :param enable_termination_protection: Whether to enable termination protection on the specified stack.
    :type enable_termination_protection: bool
    :param stack_name: The name or unique ID of the stack for which you want to set termination protection.
    :type stack_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_validate_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_body=None, template_url=None) -> web.Response:
    """g_et_validate_template

    Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn&#39;t, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_body: &lt;p&gt;Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must pass &lt;code&gt;TemplateURL&lt;/code&gt; or &lt;code&gt;TemplateBody&lt;/code&gt;. If both are passed, only &lt;code&gt;TemplateBody&lt;/code&gt; is used.&lt;/p&gt;
    :type template_body: str
    :param template_url: &lt;p&gt;Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html\&quot;&gt;Template Anatomy&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;p&gt;Conditional: You must pass &lt;code&gt;TemplateURL&lt;/code&gt; or &lt;code&gt;TemplateBody&lt;/code&gt;. If both are passed, only &lt;code&gt;TemplateBody&lt;/code&gt; is used.&lt;/p&gt;
    :type template_url: str

    """
    return web.Response(status=200)


async def p_ost_activate_organizations_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_activate_organizations_access

    Activate trusted access with Organizations. With trusted access between StackSets and Organizations activated, the management account has permissions to create and manage StackSets for your organization.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def p_ost_activate_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_activate_type

    &lt;p&gt;Activates a public third-party extension, making it available for use in stack templates. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html\&quot;&gt;Using public extensions&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Once you have activated a public third-party extension in your account and Region, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html\&quot;&gt;SetTypeConfiguration&lt;/a&gt; to specify configuration properties for the extension. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ActivateTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_batch_describe_type_configurations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_batch_describe_type_configurations

    &lt;p&gt;Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and Region.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = BatchDescribeTypeConfigurationsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_cancel_update_stack(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_cancel_update_stack

    &lt;p&gt;Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can cancel only stacks that are in the &lt;code&gt;UPDATE_IN_PROGRESS&lt;/code&gt; state.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CancelUpdateStackInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_continue_update_rollback(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_continue_update_rollback

    &lt;p&gt;For a specified stack that&#39;s in the &lt;code&gt;UPDATE_ROLLBACK_FAILED&lt;/code&gt; state, continues rolling it back to the &lt;code&gt;UPDATE_ROLLBACK_COMPLETE&lt;/code&gt; state. Depending on the cause of the failure, you can manually &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed\&quot;&gt; fix the error&lt;/a&gt; and continue the rollback. By continuing the rollback, you can return your stack to a working state (the &lt;code&gt;UPDATE_ROLLBACK_COMPLETE&lt;/code&gt; state), and then try to update the stack again.&lt;/p&gt; &lt;p&gt;A stack goes into the &lt;code&gt;UPDATE_ROLLBACK_FAILED&lt;/code&gt; state when CloudFormation can&#39;t roll back all changes after a failed stack update. For example, you might have a stack that&#39;s rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn&#39;t know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ContinueUpdateRollbackInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_change_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_change_set

    &lt;p&gt;Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn&#39;t exist or an existing stack. If you create a change set for a stack that doesn&#39;t exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack&#39;s information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.&lt;/p&gt; &lt;p&gt;To create a change set for a stack that doesn&#39;t exist, for the &lt;code&gt;ChangeSetType&lt;/code&gt; parameter, specify &lt;code&gt;CREATE&lt;/code&gt;. To create a change set for an existing stack, specify &lt;code&gt;UPDATE&lt;/code&gt; for the &lt;code&gt;ChangeSetType&lt;/code&gt; parameter. To create a change set for an import operation, specify &lt;code&gt;IMPORT&lt;/code&gt; for the &lt;code&gt;ChangeSetType&lt;/code&gt; parameter. After the &lt;code&gt;CreateChangeSet&lt;/code&gt; call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the &lt;a&gt;DescribeChangeSet&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;When you are satisfied with the changes the change set will make, execute the change set by using the &lt;a&gt;ExecuteChangeSet&lt;/a&gt; action. CloudFormation doesn&#39;t make changes until you execute the change set.&lt;/p&gt; &lt;p&gt;To create a change set for the entire stack hierarchy, set &lt;code&gt;IncludeNestedStacks&lt;/code&gt; to &lt;code&gt;True&lt;/code&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateChangeSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_stack(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_stack

    Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the &lt;a&gt;DescribeStacks&lt;/a&gt; operation.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateStackInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_stack_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_stack_instances

    Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either &lt;code&gt;Accounts&lt;/code&gt; or &lt;code&gt;DeploymentTargets&lt;/code&gt;, and you must specify at least one value for &lt;code&gt;Regions&lt;/code&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateStackInstancesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_stack_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_stack_set

    Creates a stack set.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateStackSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_deactivate_organizations_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_deactivate_organizations_access

    Deactivates trusted access with Organizations. If trusted access is deactivated, the management account does not have permissions to create and manage service-managed StackSets for your organization.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def p_ost_deactivate_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_deactivate_type

    &lt;p&gt;Deactivates a public extension that was previously activated in this account and Region.&lt;/p&gt; &lt;p&gt;Once deactivated, an extension can&#39;t be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren&#39;t automatically updated if a new version of the extension is released.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeactivateTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_change_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_change_set

    &lt;p&gt;Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.&lt;/p&gt; &lt;p&gt;If the call successfully completes, CloudFormation successfully deleted the change set.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;IncludeNestedStacks&lt;/code&gt; specifies &lt;code&gt;True&lt;/code&gt; during the creation of the nested change set, then &lt;code&gt;DeleteChangeSet&lt;/code&gt; will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of &lt;code&gt;REVIEW_IN_PROGRESS&lt;/code&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteChangeSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_stack(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_stack

    Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don&#39;t show up in the &lt;a&gt;DescribeStacks&lt;/a&gt; operation if the deletion has been completed successfully.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteStackInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_stack_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_stack_instances

    Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteStackInstancesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_stack_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_stack_set

    Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see &lt;a&gt;DeleteStackInstances&lt;/a&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteStackSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_deregister_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_deregister_type

    &lt;p&gt;Marks an extension or extension version as &lt;code&gt;DEPRECATED&lt;/code&gt; in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.&lt;/p&gt; &lt;p&gt;To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.&lt;/p&gt; &lt;p&gt;You can&#39;t deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.&lt;/p&gt; &lt;p&gt;To view the deprecation status of an extension or extension version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html\&quot;&gt;DescribeType&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeregisterTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_account_limits

    Retrieves your account&#39;s CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html\&quot;&gt;CloudFormation Quotas&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAccountLimitsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_change_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_change_set

    Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html\&quot;&gt;Updating Stacks Using Change Sets&lt;/a&gt; in the CloudFormation User Guide.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeChangeSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_change_set_hooks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_change_set_hooks

    Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeChangeSetHooksInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_organizations_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_organizations_access

    Retrieves information about the account&#39;s &lt;code&gt;OrganizationAccess&lt;/code&gt; status. This API can be called either by the management account or the delegated administrator by using the &lt;code&gt;CallAs&lt;/code&gt; parameter. This API can also be called without the &lt;code&gt;CallAs&lt;/code&gt; parameter by the management account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeOrganizationsAccessInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_publisher(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_publisher

    &lt;p&gt;Returns information about a CloudFormation extension publisher.&lt;/p&gt; &lt;p&gt;If you don&#39;t supply a &lt;code&gt;PublisherId&lt;/code&gt;, and you have registered as an extension publisher, &lt;code&gt;DescribePublisher&lt;/code&gt; returns information about your own publisher account.&lt;/p&gt; &lt;p&gt;For more information about registering as a publisher, see:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html\&quot;&gt;RegisterPublisher&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html\&quot;&gt;Publishing extensions to make them available for public use&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribePublisherInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_drift_detection_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_stack_drift_detection_status

    &lt;p&gt;Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack&#39;s actual configuration differs, or has &lt;i&gt;drifted&lt;/i&gt;, from its expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\&quot;&gt;Detecting Unregulated Configuration Changes to Stacks and Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DetectStackDrift&lt;/a&gt; to initiate a stack drift detection operation. &lt;code&gt;DetectStackDrift&lt;/code&gt; returns a &lt;code&gt;StackDriftDetectionId&lt;/code&gt; you can use to monitor the progress of the operation using &lt;code&gt;DescribeStackDriftDetectionStatus&lt;/code&gt;. Once the drift detection operation has completed, use &lt;a&gt;DescribeStackResourceDrifts&lt;/a&gt; to return drift information about the stack and its resources.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackDriftDetectionStatusInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_stack_events

    &lt;p&gt;Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack&#39;s event history, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html\&quot;&gt;Stacks&lt;/a&gt; in the CloudFormation User Guide.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackEventsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_instance(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_stack_instance

    &lt;p&gt;Returns the stack instance that&#39;s associated with the specified StackSet, Amazon Web Services account, and Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;For a list of stack instances that are associated with a specific StackSet, use &lt;a&gt;ListStackInstances&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackInstanceInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_stack_resource

    &lt;p&gt;Returns a description of the specified resource in the specified stack.&lt;/p&gt; &lt;p&gt;For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackResourceInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_resource_drifts(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_stack_resource_drifts

    &lt;p&gt;Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.&lt;/p&gt; &lt;p&gt;For a given stack, there will be one &lt;code&gt;StackResourceDrift&lt;/code&gt; for each stack resource that has been checked for drift. Resources that haven&#39;t yet been checked for drift aren&#39;t included. Resources that don&#39;t currently support drift detection aren&#39;t checked, and so not included. For a list of resources that support drift detection, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html\&quot;&gt;Resources that Support Drift Detection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DetectStackResourceDrift&lt;/a&gt; to detect drift on individual resources, or &lt;a&gt;DetectStackDrift&lt;/a&gt; to detect drift on all supported resources for a given stack.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackResourceDriftsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_resources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_stack_resources

    &lt;p&gt;Returns Amazon Web Services resource descriptions for running and deleted stacks. If &lt;code&gt;StackName&lt;/code&gt; is specified, all the associated resources that are part of the stack are returned. If &lt;code&gt;PhysicalResourceId&lt;/code&gt; is specified, the associated resources of the stack that the resource belongs to are returned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the first 100 resources will be returned. If your stack has more resources than this, you should use &lt;code&gt;ListStackResources&lt;/code&gt; instead.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For deleted stacks, &lt;code&gt;DescribeStackResources&lt;/code&gt; returns resource information for up to 90 days after the stack has been deleted.&lt;/p&gt; &lt;p&gt;You must specify either &lt;code&gt;StackName&lt;/code&gt; or &lt;code&gt;PhysicalResourceId&lt;/code&gt;, but not both. In addition, you can specify &lt;code&gt;LogicalResourceId&lt;/code&gt; to filter the returned result. For more information about resources, the &lt;code&gt;LogicalResourceId&lt;/code&gt; and &lt;code&gt;PhysicalResourceId&lt;/code&gt;, go to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/\&quot;&gt;CloudFormation User Guide&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A &lt;code&gt;ValidationError&lt;/code&gt; is returned if you specify both &lt;code&gt;StackName&lt;/code&gt; and &lt;code&gt;PhysicalResourceId&lt;/code&gt; in the same request.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackResourcesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_stack_set

    Returns the description of the specified StackSet.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stack_set_operation(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_stack_set_operation

    Returns the description of the specified StackSet operation.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStackSetOperationInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_stacks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_stacks

    &lt;p&gt;Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the stack doesn&#39;t exist, an &lt;code&gt;ValidationError&lt;/code&gt; is returned.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeStacksInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_type

    &lt;p&gt;Returns detailed information about an extension that has been registered.&lt;/p&gt; &lt;p&gt;If you specify a &lt;code&gt;VersionId&lt;/code&gt;, &lt;code&gt;DescribeType&lt;/code&gt; returns information about that specific extension version. Otherwise, it returns information about the default extension version.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_type_registration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_type_registration

    &lt;p&gt;Returns information about an extension&#39;s registration, including its current status and type and version identifiers.&lt;/p&gt; &lt;p&gt;When you initiate a registration request using &lt;a&gt;RegisterType&lt;/a&gt;, you can then use &lt;a&gt;DescribeTypeRegistration&lt;/a&gt; to monitor the progress of that registration request.&lt;/p&gt; &lt;p&gt;Once the registration request has completed, use &lt;a&gt;DescribeType&lt;/a&gt; to return detailed information about an extension.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTypeRegistrationInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_detect_stack_drift(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detect_stack_drift

    &lt;p&gt;Detects whether a stack&#39;s actual configuration differs, or has &lt;i&gt;drifted&lt;/i&gt;, from its expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\&quot;&gt;Detecting Unregulated Configuration Changes to Stacks and Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;code&gt;DetectStackDrift&lt;/code&gt; to detect drift on all supported resources for a given stack, or &lt;a&gt;DetectStackResourceDrift&lt;/a&gt; to detect drift on individual resources.&lt;/p&gt; &lt;p&gt;For a list of stack resources that currently support drift detection, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html\&quot;&gt;Resources that Support Drift Detection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectStackDrift&lt;/code&gt; can take up to several minutes, depending on the number of resources contained within the stack. Use &lt;a&gt;DescribeStackDriftDetectionStatus&lt;/a&gt; to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use &lt;a&gt;DescribeStackResourceDrifts&lt;/a&gt; to return drift information about the stack and its resources.&lt;/p&gt; &lt;p&gt;When detecting drift on a stack, CloudFormation doesn&#39;t detect drift on any nested stacks belonging to that stack. Perform &lt;code&gt;DetectStackDrift&lt;/code&gt; directly on the nested stack itself.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DetectStackDriftInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_detect_stack_resource_drift(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detect_stack_resource_drift

    &lt;p&gt;Returns information about whether a resource&#39;s actual configuration differs, or has &lt;i&gt;drifted&lt;/i&gt;, from its expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\&quot;&gt;Detecting Unregulated Configuration Changes to Stacks and Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use &lt;code&gt;DetectStackResourceDrift&lt;/code&gt; to detect drift on individual resources, or &lt;a&gt;DetectStackDrift&lt;/a&gt; to detect drift on all resources in a given stack that support drift detection.&lt;/p&gt; &lt;p&gt;Resources that don&#39;t currently support drift detection can&#39;t be checked. For a list of resources that support drift detection, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html\&quot;&gt;Resources that Support Drift Detection&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DetectStackResourceDriftInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_detect_stack_set_drift(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detect_stack_set_drift

    &lt;p&gt;Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html\&quot;&gt;How CloudFormation performs drift detection on a stack set&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DetectStackSetDrift&lt;/code&gt; returns the &lt;code&gt;OperationId&lt;/code&gt; of the stack set drift detection operation. Use this operation id with &lt;a&gt;DescribeStackSetOperation&lt;/a&gt; to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.&lt;/p&gt; &lt;p&gt;Once the operation has completed, use the following actions to return drift information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;DescribeStackSet&lt;/a&gt; to return detailed information about the stack set, including detailed information about the last &lt;i&gt;completed&lt;/i&gt; drift operation performed on the stack set. (Information about drift operations that are in progress isn&#39;t included.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;ListStackInstances&lt;/a&gt; to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;DescribeStackInstance&lt;/a&gt; to return detailed information about a specific stack instance, including its drift status and last drift time checked.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about performing a drift detection operation on a stack set, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html\&quot;&gt;Detecting unmanaged changes in stack sets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can only run a single drift detection operation on a given stack set at one time.&lt;/p&gt; &lt;p&gt;To stop a drift detection stack set operation, use &lt;a&gt;StopStackSetOperation&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DetectStackSetDriftInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_estimate_template_cost(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_estimate_template_cost

    Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = EstimateTemplateCostInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_execute_change_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_execute_change_set

    &lt;p&gt;Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the &lt;a&gt;DescribeStacks&lt;/a&gt; action to view the status of the update.&lt;/p&gt; &lt;p&gt;When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren&#39;t valid for the updated stack.&lt;/p&gt; &lt;p&gt;If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can&#39;t specify a temporary stack policy that overrides the current policy.&lt;/p&gt; &lt;p&gt;To create a change set for the entire stack hierarchy, &lt;code&gt;IncludeNestedStacks&lt;/code&gt; must have been set to &lt;code&gt;True&lt;/code&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ExecuteChangeSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_stack_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_stack_policy

    Returns the stack policy for a specified stack. If a stack doesn&#39;t have a policy, a null value is returned.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GetStackPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_template

    &lt;p&gt;Returns the template body for a specified stack. You can get the template for running or deleted stacks.&lt;/p&gt; &lt;p&gt;For deleted stacks, &lt;code&gt;GetTemplate&lt;/code&gt; returns the template for up to 90 days after the stack has been deleted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the template doesn&#39;t exist, a &lt;code&gt;ValidationError&lt;/code&gt; is returned.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GetTemplateInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_template_summary(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_template_summary

    &lt;p&gt;Returns information about a new or existing template. The &lt;code&gt;GetTemplateSummary&lt;/code&gt; action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;GetTemplateSummary&lt;/code&gt; action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.&lt;/p&gt; &lt;p&gt;For deleted stacks, &lt;code&gt;GetTemplateSummary&lt;/code&gt; returns the template information for up to 90 days after the stack has been deleted. If the template doesn&#39;t exist, a &lt;code&gt;ValidationError&lt;/code&gt; is returned.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = GetTemplateSummaryInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_import_stacks_to_stack_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_import_stacks_to_stack_set

    Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ImportStacksToStackSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_change_sets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_change_sets

    Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the &lt;code&gt;CREATE_IN_PROGRESS&lt;/code&gt; or &lt;code&gt;CREATE_PENDING&lt;/code&gt; state.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListChangeSetsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_exports(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_exports

    &lt;p&gt;Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html\&quot;&gt; Fn::ImportValue&lt;/a&gt; function.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html\&quot;&gt; CloudFormation export stack output values&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListExportsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_imports(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_imports

    &lt;p&gt;Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see &lt;a&gt;ListExports&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about importing an exported output value, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html\&quot;&gt;Fn::ImportValue&lt;/a&gt; function.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListImportsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_stack_instance_resource_drifts(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_stack_instance_resource_drifts

    &lt;p&gt;Returns drift information for resources in a stack instance.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ListStackInstanceResourceDrifts&lt;/code&gt; returns drift information for the most recent drift detection operation. If an operation is in progress, it may only return partial results.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListStackInstanceResourceDriftsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_stack_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_stack_instances

    Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListStackInstancesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_stack_resources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_stack_resources

    &lt;p&gt;Returns descriptions of all resources of the specified stack.&lt;/p&gt; &lt;p&gt;For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListStackResourcesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_stack_set_operation_results(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_stack_set_operation_results

    Returns summary information about the results of a stack set operation.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListStackSetOperationResultsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_stack_set_operations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_stack_set_operations

    Returns summary information about operations performed on a stack set.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListStackSetOperationsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_stack_sets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_stack_sets

    &lt;p&gt;Returns summary information about stack sets that are associated with the user.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;[Self-managed permissions] If you set the &lt;code&gt;CallAs&lt;/code&gt; parameter to &lt;code&gt;SELF&lt;/code&gt; while signed in to your Amazon Web Services account, &lt;code&gt;ListStackSets&lt;/code&gt; returns all self-managed stack sets in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;[Service-managed permissions] If you set the &lt;code&gt;CallAs&lt;/code&gt; parameter to &lt;code&gt;SELF&lt;/code&gt; while signed in to the organization&#39;s management account, &lt;code&gt;ListStackSets&lt;/code&gt; returns all stack sets in the management account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;[Service-managed permissions] If you set the &lt;code&gt;CallAs&lt;/code&gt; parameter to &lt;code&gt;DELEGATED_ADMIN&lt;/code&gt; while signed in to your member account, &lt;code&gt;ListStackSets&lt;/code&gt; returns all stack sets with service-managed permissions in the management account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListStackSetsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_stacks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_stacks

    Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListStacksInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_type_registrations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_type_registrations

    Returns a list of registration tokens for the specified extension(s).

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListTypeRegistrationsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_type_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_type_versions

    Returns summary information about the versions of an extension.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListTypeVersionsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_types

    Returns summary information about extension that have been registered with CloudFormation.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListTypesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_publish_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_publish_type

    &lt;p&gt;Publishes the specified extension to the CloudFormation registry as a public extension in this Region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html\&quot;&gt;Publishing extensions to make them available for public use&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html\&quot;&gt;RegisterPublisher&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = PublishTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_record_handler_progress(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_record_handler_progress

    &lt;p&gt;Reports progress of a resource handler to CloudFormation.&lt;/p&gt; &lt;p&gt;Reserved for use by the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html\&quot;&gt;CloudFormation CLI&lt;/a&gt;. Don&#39;t use this API in your code.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RecordHandlerProgressInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_register_publisher(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_register_publisher

    &lt;p&gt;Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.&lt;/p&gt; &lt;p&gt;For information about requirements for registering as a public extension publisher, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs\&quot;&gt;Registering your account to publish CloudFormation extensions&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p/&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RegisterPublisherInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_register_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_register_type

    &lt;p&gt;Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Validating the extension schema.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Determining which handlers, if any, have been specified for the extension.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Making the extension available for use in your account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about how to develop extensions and ready them for registration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html\&quot;&gt;Creating Resource Providers&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per Region. Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html\&quot;&gt;DeregisterType&lt;/a&gt; to deregister specific extension versions if necessary.&lt;/p&gt; &lt;p&gt;Once you have initiated a registration request using &lt;a&gt;RegisterType&lt;/a&gt;, you can use &lt;a&gt;DescribeTypeRegistration&lt;/a&gt; to monitor the progress of the registration request.&lt;/p&gt; &lt;p&gt;Once you have registered a private extension in your account and Region, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html\&quot;&gt;SetTypeConfiguration&lt;/a&gt; to specify configuration properties for the extension. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RegisterTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_rollback_stack(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_rollback_stack

    &lt;p&gt;When specifying &lt;code&gt;RollbackStack&lt;/code&gt;, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the &lt;a&gt;DescribeStacks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;Rolls back the specified stack to the last known stable state from &lt;code&gt;CREATE_FAILED&lt;/code&gt; or &lt;code&gt;UPDATE_FAILED&lt;/code&gt; stack statuses.&lt;/p&gt; &lt;p&gt;This operation will delete a stack if it doesn&#39;t contain a last known stable state. A last known stable state includes any status in a &lt;code&gt;*_COMPLETE&lt;/code&gt;. This includes the following stack statuses.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CREATE_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UPDATE_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UPDATE_ROLLBACK_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IMPORT_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IMPORT_ROLLBACK_COMPLETE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RollbackStackInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_stack_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_stack_policy

    Sets a stack policy for a specified stack.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SetStackPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_type_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_type_configuration

    &lt;p&gt;Specifies the configuration data for a registered CloudFormation extension, in the given account and Region.&lt;/p&gt; &lt;p&gt;To view the current configuration data for an extension, refer to the &lt;code&gt;ConfigurationSchema&lt;/code&gt; element of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html\&quot;&gt;DescribeType&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration\&quot;&gt;Configuring extensions at the account level&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It&#39;s strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/\&quot;&gt;Using dynamic references to specify template values&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SetTypeConfigurationInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_type_default_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_type_default_version

    Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SetTypeDefaultVersionInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_signal_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_signal_resource

    Sends a signal to the specified resource with a success or failure status. You can use the &lt;code&gt;SignalResource&lt;/code&gt; operation in conjunction with a creation policy or update policy. CloudFormation doesn&#39;t proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The &lt;code&gt;SignalResource&lt;/code&gt; operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SignalResourceInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_stop_stack_set_operation(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_stop_stack_set_operation

    Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = StopStackSetOperationInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_test_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_test_type

    &lt;p&gt;Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For resource types, this includes passing all contracts tests defined for the type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For modules, this includes determining if the module&#39;s model meets all necessary requirements.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing\&quot;&gt;Testing your public extension prior to publishing&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a version, CloudFormation uses the default version of the extension in your account and Region for testing.&lt;/p&gt; &lt;p&gt;To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html\&quot;&gt;RegisterType&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Once you&#39;ve initiated testing on an extension using &lt;code&gt;TestType&lt;/code&gt;, you can pass the returned &lt;code&gt;TypeVersionArn&lt;/code&gt; into &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html\&quot;&gt;DescribeType&lt;/a&gt; to monitor the current test status and test status description for the extension.&lt;/p&gt; &lt;p&gt;An extension must have a test status of &lt;code&gt;PASSED&lt;/code&gt; before it can be published. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html\&quot;&gt;Publishing extensions to make them available for public use&lt;/a&gt; in the &lt;i&gt;CloudFormation CLI User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = TestTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_stack(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_stack

    &lt;p&gt;Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the &lt;a&gt;DescribeStacks&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;To get a copy of the template for an existing stack, you can use the &lt;a&gt;GetTemplate&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about creating an update template, updating a stack, and monitoring the progress of the update, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html\&quot;&gt;Updating a Stack&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateStackInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_stack_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_stack_instances

    &lt;p&gt;Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.&lt;/p&gt; &lt;p&gt;You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html\&quot;&gt;CreateStackInstances&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;During stack set updates, any parameters overridden for a stack instance aren&#39;t updated, but retain their overridden value.&lt;/p&gt; &lt;p&gt;You can only update the parameter &lt;i&gt;values&lt;/i&gt; that are specified in the stack set; to add or delete a parameter itself, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html\&quot;&gt;UpdateStackSet&lt;/a&gt; to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html\&quot;&gt;UpdateStackSet&lt;/a&gt; to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using &lt;code&gt;UpdateStackInstances&lt;/code&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateStackInstancesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_stack_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_stack_set

    &lt;p&gt;Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.&lt;/p&gt; &lt;p&gt;Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent &lt;a&gt;CreateStackInstances&lt;/a&gt; calls on the specified stack set use the updated stack set.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateStackSetInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_termination_protection(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_termination_protection

    &lt;p&gt;Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html\&quot;&gt;Protecting a Stack From Being Deleted&lt;/a&gt; in the &lt;i&gt;CloudFormation User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html\&quot;&gt;nested stacks&lt;/a&gt;, termination protection is set on the root stack and can&#39;t be changed directly on the nested stack.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTerminationProtectionInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_validate_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_validate_template

    Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn&#39;t, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ValidateTemplateInput.from_dict(body)
    return web.Response(status=200)
