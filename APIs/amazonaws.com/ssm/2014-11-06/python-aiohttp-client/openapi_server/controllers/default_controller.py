from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tags_to_resource_request import AddTagsToResourceRequest
from openapi_server.models.associate_ops_item_related_item_request import AssociateOpsItemRelatedItemRequest
from openapi_server.models.associate_ops_item_related_item_response import AssociateOpsItemRelatedItemResponse
from openapi_server.models.cancel_command_request import CancelCommandRequest
from openapi_server.models.cancel_maintenance_window_execution_request import CancelMaintenanceWindowExecutionRequest
from openapi_server.models.cancel_maintenance_window_execution_result import CancelMaintenanceWindowExecutionResult
from openapi_server.models.create_activation_request import CreateActivationRequest
from openapi_server.models.create_activation_result import CreateActivationResult
from openapi_server.models.create_association_batch_request import CreateAssociationBatchRequest
from openapi_server.models.create_association_batch_result import CreateAssociationBatchResult
from openapi_server.models.create_association_request import CreateAssociationRequest
from openapi_server.models.create_association_result import CreateAssociationResult
from openapi_server.models.create_document_request import CreateDocumentRequest
from openapi_server.models.create_document_result import CreateDocumentResult
from openapi_server.models.create_maintenance_window_request import CreateMaintenanceWindowRequest
from openapi_server.models.create_maintenance_window_result import CreateMaintenanceWindowResult
from openapi_server.models.create_ops_item_request import CreateOpsItemRequest
from openapi_server.models.create_ops_item_response import CreateOpsItemResponse
from openapi_server.models.create_ops_metadata_request import CreateOpsMetadataRequest
from openapi_server.models.create_ops_metadata_result import CreateOpsMetadataResult
from openapi_server.models.create_patch_baseline_request import CreatePatchBaselineRequest
from openapi_server.models.create_patch_baseline_result import CreatePatchBaselineResult
from openapi_server.models.create_resource_data_sync_request import CreateResourceDataSyncRequest
from openapi_server.models.delete_activation_request import DeleteActivationRequest
from openapi_server.models.delete_association_request import DeleteAssociationRequest
from openapi_server.models.delete_document_request import DeleteDocumentRequest
from openapi_server.models.delete_inventory_request import DeleteInventoryRequest
from openapi_server.models.delete_inventory_result import DeleteInventoryResult
from openapi_server.models.delete_maintenance_window_request import DeleteMaintenanceWindowRequest
from openapi_server.models.delete_maintenance_window_result import DeleteMaintenanceWindowResult
from openapi_server.models.delete_ops_metadata_request import DeleteOpsMetadataRequest
from openapi_server.models.delete_parameter_request import DeleteParameterRequest
from openapi_server.models.delete_parameters_request import DeleteParametersRequest
from openapi_server.models.delete_parameters_result import DeleteParametersResult
from openapi_server.models.delete_patch_baseline_request import DeletePatchBaselineRequest
from openapi_server.models.delete_patch_baseline_result import DeletePatchBaselineResult
from openapi_server.models.delete_resource_data_sync_request import DeleteResourceDataSyncRequest
from openapi_server.models.delete_resource_policy_request import DeleteResourcePolicyRequest
from openapi_server.models.deregister_managed_instance_request import DeregisterManagedInstanceRequest
from openapi_server.models.deregister_patch_baseline_for_patch_group_request import DeregisterPatchBaselineForPatchGroupRequest
from openapi_server.models.deregister_patch_baseline_for_patch_group_result import DeregisterPatchBaselineForPatchGroupResult
from openapi_server.models.deregister_target_from_maintenance_window_request import DeregisterTargetFromMaintenanceWindowRequest
from openapi_server.models.deregister_target_from_maintenance_window_result import DeregisterTargetFromMaintenanceWindowResult
from openapi_server.models.deregister_task_from_maintenance_window_request import DeregisterTaskFromMaintenanceWindowRequest
from openapi_server.models.deregister_task_from_maintenance_window_result import DeregisterTaskFromMaintenanceWindowResult
from openapi_server.models.describe_activations_request import DescribeActivationsRequest
from openapi_server.models.describe_activations_result import DescribeActivationsResult
from openapi_server.models.describe_association_execution_targets_request import DescribeAssociationExecutionTargetsRequest
from openapi_server.models.describe_association_execution_targets_result import DescribeAssociationExecutionTargetsResult
from openapi_server.models.describe_association_executions_request import DescribeAssociationExecutionsRequest
from openapi_server.models.describe_association_executions_result import DescribeAssociationExecutionsResult
from openapi_server.models.describe_association_request import DescribeAssociationRequest
from openapi_server.models.describe_association_result import DescribeAssociationResult
from openapi_server.models.describe_automation_executions_request import DescribeAutomationExecutionsRequest
from openapi_server.models.describe_automation_executions_result import DescribeAutomationExecutionsResult
from openapi_server.models.describe_automation_step_executions_request import DescribeAutomationStepExecutionsRequest
from openapi_server.models.describe_automation_step_executions_result import DescribeAutomationStepExecutionsResult
from openapi_server.models.describe_available_patches_request import DescribeAvailablePatchesRequest
from openapi_server.models.describe_available_patches_result import DescribeAvailablePatchesResult
from openapi_server.models.describe_document_permission_request import DescribeDocumentPermissionRequest
from openapi_server.models.describe_document_permission_response import DescribeDocumentPermissionResponse
from openapi_server.models.describe_document_request import DescribeDocumentRequest
from openapi_server.models.describe_document_result import DescribeDocumentResult
from openapi_server.models.describe_effective_instance_associations_request import DescribeEffectiveInstanceAssociationsRequest
from openapi_server.models.describe_effective_instance_associations_result import DescribeEffectiveInstanceAssociationsResult
from openapi_server.models.describe_effective_patches_for_patch_baseline_request import DescribeEffectivePatchesForPatchBaselineRequest
from openapi_server.models.describe_effective_patches_for_patch_baseline_result import DescribeEffectivePatchesForPatchBaselineResult
from openapi_server.models.describe_instance_associations_status_request import DescribeInstanceAssociationsStatusRequest
from openapi_server.models.describe_instance_associations_status_result import DescribeInstanceAssociationsStatusResult
from openapi_server.models.describe_instance_information_request import DescribeInstanceInformationRequest
from openapi_server.models.describe_instance_information_result import DescribeInstanceInformationResult
from openapi_server.models.describe_instance_patch_states_for_patch_group_request import DescribeInstancePatchStatesForPatchGroupRequest
from openapi_server.models.describe_instance_patch_states_for_patch_group_result import DescribeInstancePatchStatesForPatchGroupResult
from openapi_server.models.describe_instance_patch_states_request import DescribeInstancePatchStatesRequest
from openapi_server.models.describe_instance_patch_states_result import DescribeInstancePatchStatesResult
from openapi_server.models.describe_instance_patches_request import DescribeInstancePatchesRequest
from openapi_server.models.describe_instance_patches_result import DescribeInstancePatchesResult
from openapi_server.models.describe_inventory_deletions_request import DescribeInventoryDeletionsRequest
from openapi_server.models.describe_inventory_deletions_result import DescribeInventoryDeletionsResult
from openapi_server.models.describe_maintenance_window_execution_task_invocations_request import DescribeMaintenanceWindowExecutionTaskInvocationsRequest
from openapi_server.models.describe_maintenance_window_execution_task_invocations_result import DescribeMaintenanceWindowExecutionTaskInvocationsResult
from openapi_server.models.describe_maintenance_window_execution_tasks_request import DescribeMaintenanceWindowExecutionTasksRequest
from openapi_server.models.describe_maintenance_window_execution_tasks_result import DescribeMaintenanceWindowExecutionTasksResult
from openapi_server.models.describe_maintenance_window_executions_request import DescribeMaintenanceWindowExecutionsRequest
from openapi_server.models.describe_maintenance_window_executions_result import DescribeMaintenanceWindowExecutionsResult
from openapi_server.models.describe_maintenance_window_schedule_request import DescribeMaintenanceWindowScheduleRequest
from openapi_server.models.describe_maintenance_window_schedule_result import DescribeMaintenanceWindowScheduleResult
from openapi_server.models.describe_maintenance_window_targets_request import DescribeMaintenanceWindowTargetsRequest
from openapi_server.models.describe_maintenance_window_targets_result import DescribeMaintenanceWindowTargetsResult
from openapi_server.models.describe_maintenance_window_tasks_request import DescribeMaintenanceWindowTasksRequest
from openapi_server.models.describe_maintenance_window_tasks_result import DescribeMaintenanceWindowTasksResult
from openapi_server.models.describe_maintenance_windows_for_target_request import DescribeMaintenanceWindowsForTargetRequest
from openapi_server.models.describe_maintenance_windows_for_target_result import DescribeMaintenanceWindowsForTargetResult
from openapi_server.models.describe_maintenance_windows_request import DescribeMaintenanceWindowsRequest
from openapi_server.models.describe_maintenance_windows_result import DescribeMaintenanceWindowsResult
from openapi_server.models.describe_ops_items_request import DescribeOpsItemsRequest
from openapi_server.models.describe_ops_items_response import DescribeOpsItemsResponse
from openapi_server.models.describe_parameters_request import DescribeParametersRequest
from openapi_server.models.describe_parameters_result import DescribeParametersResult
from openapi_server.models.describe_patch_baselines_request import DescribePatchBaselinesRequest
from openapi_server.models.describe_patch_baselines_result import DescribePatchBaselinesResult
from openapi_server.models.describe_patch_group_state_request import DescribePatchGroupStateRequest
from openapi_server.models.describe_patch_group_state_result import DescribePatchGroupStateResult
from openapi_server.models.describe_patch_groups_request import DescribePatchGroupsRequest
from openapi_server.models.describe_patch_groups_result import DescribePatchGroupsResult
from openapi_server.models.describe_patch_properties_request import DescribePatchPropertiesRequest
from openapi_server.models.describe_patch_properties_result import DescribePatchPropertiesResult
from openapi_server.models.describe_sessions_request import DescribeSessionsRequest
from openapi_server.models.describe_sessions_response import DescribeSessionsResponse
from openapi_server.models.disassociate_ops_item_related_item_request import DisassociateOpsItemRelatedItemRequest
from openapi_server.models.get_automation_execution_request import GetAutomationExecutionRequest
from openapi_server.models.get_automation_execution_result import GetAutomationExecutionResult
from openapi_server.models.get_calendar_state_request import GetCalendarStateRequest
from openapi_server.models.get_calendar_state_response import GetCalendarStateResponse
from openapi_server.models.get_command_invocation_request import GetCommandInvocationRequest
from openapi_server.models.get_command_invocation_result import GetCommandInvocationResult
from openapi_server.models.get_connection_status_request import GetConnectionStatusRequest
from openapi_server.models.get_connection_status_response import GetConnectionStatusResponse
from openapi_server.models.get_default_patch_baseline_request import GetDefaultPatchBaselineRequest
from openapi_server.models.get_default_patch_baseline_result import GetDefaultPatchBaselineResult
from openapi_server.models.get_deployable_patch_snapshot_for_instance_request import GetDeployablePatchSnapshotForInstanceRequest
from openapi_server.models.get_deployable_patch_snapshot_for_instance_result import GetDeployablePatchSnapshotForInstanceResult
from openapi_server.models.get_document_request import GetDocumentRequest
from openapi_server.models.get_document_result import GetDocumentResult
from openapi_server.models.get_inventory_request import GetInventoryRequest
from openapi_server.models.get_inventory_result import GetInventoryResult
from openapi_server.models.get_inventory_schema_request import GetInventorySchemaRequest
from openapi_server.models.get_inventory_schema_result import GetInventorySchemaResult
from openapi_server.models.get_maintenance_window_execution_request import GetMaintenanceWindowExecutionRequest
from openapi_server.models.get_maintenance_window_execution_result import GetMaintenanceWindowExecutionResult
from openapi_server.models.get_maintenance_window_execution_task_invocation_request import GetMaintenanceWindowExecutionTaskInvocationRequest
from openapi_server.models.get_maintenance_window_execution_task_invocation_result import GetMaintenanceWindowExecutionTaskInvocationResult
from openapi_server.models.get_maintenance_window_execution_task_request import GetMaintenanceWindowExecutionTaskRequest
from openapi_server.models.get_maintenance_window_execution_task_result import GetMaintenanceWindowExecutionTaskResult
from openapi_server.models.get_maintenance_window_request import GetMaintenanceWindowRequest
from openapi_server.models.get_maintenance_window_result import GetMaintenanceWindowResult
from openapi_server.models.get_maintenance_window_task_request import GetMaintenanceWindowTaskRequest
from openapi_server.models.get_maintenance_window_task_result import GetMaintenanceWindowTaskResult
from openapi_server.models.get_ops_item_request import GetOpsItemRequest
from openapi_server.models.get_ops_item_response import GetOpsItemResponse
from openapi_server.models.get_ops_metadata_request import GetOpsMetadataRequest
from openapi_server.models.get_ops_metadata_result import GetOpsMetadataResult
from openapi_server.models.get_ops_summary_request import GetOpsSummaryRequest
from openapi_server.models.get_ops_summary_result import GetOpsSummaryResult
from openapi_server.models.get_parameter_history_request import GetParameterHistoryRequest
from openapi_server.models.get_parameter_history_result import GetParameterHistoryResult
from openapi_server.models.get_parameter_request import GetParameterRequest
from openapi_server.models.get_parameter_result import GetParameterResult
from openapi_server.models.get_parameters_by_path_request import GetParametersByPathRequest
from openapi_server.models.get_parameters_by_path_result import GetParametersByPathResult
from openapi_server.models.get_parameters_request import GetParametersRequest
from openapi_server.models.get_parameters_result import GetParametersResult
from openapi_server.models.get_patch_baseline_for_patch_group_request import GetPatchBaselineForPatchGroupRequest
from openapi_server.models.get_patch_baseline_for_patch_group_result import GetPatchBaselineForPatchGroupResult
from openapi_server.models.get_patch_baseline_request import GetPatchBaselineRequest
from openapi_server.models.get_patch_baseline_result import GetPatchBaselineResult
from openapi_server.models.get_resource_policies_request import GetResourcePoliciesRequest
from openapi_server.models.get_resource_policies_response import GetResourcePoliciesResponse
from openapi_server.models.get_service_setting_request import GetServiceSettingRequest
from openapi_server.models.get_service_setting_result import GetServiceSettingResult
from openapi_server.models.label_parameter_version_request import LabelParameterVersionRequest
from openapi_server.models.label_parameter_version_result import LabelParameterVersionResult
from openapi_server.models.list_association_versions_request import ListAssociationVersionsRequest
from openapi_server.models.list_association_versions_result import ListAssociationVersionsResult
from openapi_server.models.list_associations_request import ListAssociationsRequest
from openapi_server.models.list_associations_result import ListAssociationsResult
from openapi_server.models.list_command_invocations_request import ListCommandInvocationsRequest
from openapi_server.models.list_command_invocations_result import ListCommandInvocationsResult
from openapi_server.models.list_commands_request import ListCommandsRequest
from openapi_server.models.list_commands_result import ListCommandsResult
from openapi_server.models.list_compliance_items_request import ListComplianceItemsRequest
from openapi_server.models.list_compliance_items_result import ListComplianceItemsResult
from openapi_server.models.list_compliance_summaries_request import ListComplianceSummariesRequest
from openapi_server.models.list_compliance_summaries_result import ListComplianceSummariesResult
from openapi_server.models.list_document_metadata_history_request import ListDocumentMetadataHistoryRequest
from openapi_server.models.list_document_metadata_history_response import ListDocumentMetadataHistoryResponse
from openapi_server.models.list_document_versions_request import ListDocumentVersionsRequest
from openapi_server.models.list_document_versions_result import ListDocumentVersionsResult
from openapi_server.models.list_documents_request import ListDocumentsRequest
from openapi_server.models.list_documents_result import ListDocumentsResult
from openapi_server.models.list_inventory_entries_request import ListInventoryEntriesRequest
from openapi_server.models.list_inventory_entries_result import ListInventoryEntriesResult
from openapi_server.models.list_ops_item_events_request import ListOpsItemEventsRequest
from openapi_server.models.list_ops_item_events_response import ListOpsItemEventsResponse
from openapi_server.models.list_ops_item_related_items_request import ListOpsItemRelatedItemsRequest
from openapi_server.models.list_ops_item_related_items_response import ListOpsItemRelatedItemsResponse
from openapi_server.models.list_ops_metadata_request import ListOpsMetadataRequest
from openapi_server.models.list_ops_metadata_result import ListOpsMetadataResult
from openapi_server.models.list_resource_compliance_summaries_request import ListResourceComplianceSummariesRequest
from openapi_server.models.list_resource_compliance_summaries_result import ListResourceComplianceSummariesResult
from openapi_server.models.list_resource_data_sync_request import ListResourceDataSyncRequest
from openapi_server.models.list_resource_data_sync_result import ListResourceDataSyncResult
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.modify_document_permission_request import ModifyDocumentPermissionRequest
from openapi_server.models.put_compliance_items_request import PutComplianceItemsRequest
from openapi_server.models.put_inventory_request import PutInventoryRequest
from openapi_server.models.put_inventory_result import PutInventoryResult
from openapi_server.models.put_parameter_request import PutParameterRequest
from openapi_server.models.put_parameter_result import PutParameterResult
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.put_resource_policy_response import PutResourcePolicyResponse
from openapi_server.models.register_default_patch_baseline_request import RegisterDefaultPatchBaselineRequest
from openapi_server.models.register_default_patch_baseline_result import RegisterDefaultPatchBaselineResult
from openapi_server.models.register_patch_baseline_for_patch_group_request import RegisterPatchBaselineForPatchGroupRequest
from openapi_server.models.register_patch_baseline_for_patch_group_result import RegisterPatchBaselineForPatchGroupResult
from openapi_server.models.register_target_with_maintenance_window_request import RegisterTargetWithMaintenanceWindowRequest
from openapi_server.models.register_target_with_maintenance_window_result import RegisterTargetWithMaintenanceWindowResult
from openapi_server.models.register_task_with_maintenance_window_request import RegisterTaskWithMaintenanceWindowRequest
from openapi_server.models.register_task_with_maintenance_window_result import RegisterTaskWithMaintenanceWindowResult
from openapi_server.models.remove_tags_from_resource_request import RemoveTagsFromResourceRequest
from openapi_server.models.reset_service_setting_request import ResetServiceSettingRequest
from openapi_server.models.reset_service_setting_result import ResetServiceSettingResult
from openapi_server.models.resume_session_request import ResumeSessionRequest
from openapi_server.models.resume_session_response import ResumeSessionResponse
from openapi_server.models.send_automation_signal_request import SendAutomationSignalRequest
from openapi_server.models.send_command_request import SendCommandRequest
from openapi_server.models.send_command_result import SendCommandResult
from openapi_server.models.start_associations_once_request import StartAssociationsOnceRequest
from openapi_server.models.start_automation_execution_request import StartAutomationExecutionRequest
from openapi_server.models.start_automation_execution_result import StartAutomationExecutionResult
from openapi_server.models.start_change_request_execution_request import StartChangeRequestExecutionRequest
from openapi_server.models.start_change_request_execution_result import StartChangeRequestExecutionResult
from openapi_server.models.start_session_request import StartSessionRequest
from openapi_server.models.start_session_response import StartSessionResponse
from openapi_server.models.stop_automation_execution_request import StopAutomationExecutionRequest
from openapi_server.models.terminate_session_request import TerminateSessionRequest
from openapi_server.models.terminate_session_response import TerminateSessionResponse
from openapi_server.models.unlabel_parameter_version_request import UnlabelParameterVersionRequest
from openapi_server.models.unlabel_parameter_version_result import UnlabelParameterVersionResult
from openapi_server.models.update_association_request import UpdateAssociationRequest
from openapi_server.models.update_association_result import UpdateAssociationResult
from openapi_server.models.update_association_status_request import UpdateAssociationStatusRequest
from openapi_server.models.update_association_status_result import UpdateAssociationStatusResult
from openapi_server.models.update_document_default_version_request import UpdateDocumentDefaultVersionRequest
from openapi_server.models.update_document_default_version_result import UpdateDocumentDefaultVersionResult
from openapi_server.models.update_document_metadata_request import UpdateDocumentMetadataRequest
from openapi_server.models.update_document_request import UpdateDocumentRequest
from openapi_server.models.update_document_result import UpdateDocumentResult
from openapi_server.models.update_maintenance_window_request import UpdateMaintenanceWindowRequest
from openapi_server.models.update_maintenance_window_result import UpdateMaintenanceWindowResult
from openapi_server.models.update_maintenance_window_target_request import UpdateMaintenanceWindowTargetRequest
from openapi_server.models.update_maintenance_window_target_result import UpdateMaintenanceWindowTargetResult
from openapi_server.models.update_maintenance_window_task_request import UpdateMaintenanceWindowTaskRequest
from openapi_server.models.update_maintenance_window_task_result import UpdateMaintenanceWindowTaskResult
from openapi_server.models.update_managed_instance_role_request import UpdateManagedInstanceRoleRequest
from openapi_server.models.update_ops_item_request import UpdateOpsItemRequest
from openapi_server.models.update_ops_metadata_request import UpdateOpsMetadataRequest
from openapi_server.models.update_ops_metadata_result import UpdateOpsMetadataResult
from openapi_server.models.update_patch_baseline_request import UpdatePatchBaselineRequest
from openapi_server.models.update_patch_baseline_result import UpdatePatchBaselineResult
from openapi_server.models.update_resource_data_sync_request import UpdateResourceDataSyncRequest
from openapi_server.models.update_service_setting_request import UpdateServiceSettingRequest
from openapi_server import util


async def add_tags_to_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags_to_resource

    &lt;p&gt;Adds or overwrites one or more tags for the specified resource. &lt;i&gt;Tags&lt;/i&gt; are metadata that you can assign to your automations, documents, managed nodes, maintenance windows, Parameter Store parameters, and patch baselines. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account&#39;s managed nodes that helps you track each node&#39;s owner and stack level. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Key&#x3D;Owner,Value&#x3D;DbAdmin&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Key&#x3D;Owner,Value&#x3D;SysAdmin&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Key&#x3D;Owner,Value&#x3D;Dev&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Key&#x3D;Stack,Value&#x3D;Production&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Key&#x3D;Stack,Value&#x3D;Pre-Production&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Key&#x3D;Stack,Value&#x3D;Test&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Most resources can have a maximum of 50 tags. Automations can have a maximum of 5 tags.&lt;/p&gt; &lt;p&gt;We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don&#39;t have any semantic meaning to and are interpreted strictly as a string of characters.&lt;/p&gt; &lt;p&gt;For more information about using tags with Amazon Elastic Compute Cloud (Amazon EC2) instances, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html\&quot;&gt;Tagging your Amazon EC2 resources&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = AddTagsToResourceRequest.from_dict(body)
    return web.Response(status=200)


async def associate_ops_item_related_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_ops_item_related_item

    Associates a related item to a Systems Manager OpsCenter OpsItem. For example, you can associate an Incident Manager incident or analysis with an OpsItem. Incident Manager and OpsCenter are capabilities of Amazon Web Services Systems Manager.

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
    body = AssociateOpsItemRelatedItemRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_command(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_command

    Attempts to cancel the command specified by the Command ID. There is no guarantee that the command will be terminated and the underlying process stopped.

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
    body = CancelCommandRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_maintenance_window_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_maintenance_window_execution

    Stops a maintenance window execution that is already in progress and cancels any tasks in the window that haven&#39;t already starting running. Tasks already in progress will continue to completion.

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
    body = CancelMaintenanceWindowExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def create_activation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_activation

    &lt;p&gt;Generates an activation code and activation ID you can use to register your on-premises servers, edge devices, or virtual machine (VM) with Amazon Web Services Systems Manager. Registering these machines with Systems Manager makes it possible to manage them using Systems Manager capabilities. You use the activation code and ID when installing SSM Agent on machines in your hybrid environment. For more information about requirements for managing on-premises machines using Systems Manager, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html\&quot;&gt;Setting up Amazon Web Services Systems Manager for hybrid environments&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and VMs that are configured for Systems Manager are all called &lt;i&gt;managed nodes&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateActivationRequest.from_dict(body)
    return web.Response(status=200)


async def create_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_association

    A State Manager association defines the state that you want to maintain on your managed nodes. For example, an association can specify that anti-virus software must be installed and running on your managed nodes, or that certain ports must be closed. For static targets, the association specifies a schedule for when the configuration is reapplied. For dynamic targets, such as an Amazon Web Services resource group or an Amazon Web Services autoscaling group, State Manager, a capability of Amazon Web Services Systems Manager applies the configuration when new managed nodes are added to the group. The association also specifies actions to take when applying the configuration. For example, an association for anti-virus software might run once a day. If the software isn&#39;t installed, then State Manager installs it. If the software is installed, but the service isn&#39;t running, then the association might instruct State Manager to start the service. 

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
    body = CreateAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def create_association_batch(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_association_batch

    &lt;p&gt;Associates the specified Amazon Web Services Systems Manager document (SSM document) with the specified managed nodes or targets.&lt;/p&gt; &lt;p&gt;When you associate a document with one or more managed nodes using IDs or tags, Amazon Web Services Systems Manager Agent (SSM Agent) running on the managed node processes the document and configures the node as specified.&lt;/p&gt; &lt;p&gt;If you associate a document with a managed node that already has an associated document, the system returns the AssociationAlreadyExists exception.&lt;/p&gt;

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
    body = CreateAssociationBatchRequest.from_dict(body)
    return web.Response(status=200)


async def create_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_document

    Creates a Amazon Web Services Systems Manager (SSM document). An SSM document defines the actions that Systems Manager performs on your managed nodes. For more information about SSM documents, including information about supported schemas, features, and syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html\&quot;&gt;Amazon Web Services Systems Manager Documents&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.

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
    body = CreateDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def create_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_maintenance_window

    &lt;p&gt;Creates a new maintenance window.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The value you specify for &lt;code&gt;Duration&lt;/code&gt; determines the specific end time for the maintenance window based on the time it begins. No maintenance window tasks are permitted to start after the resulting endtime minus the number of hours you specify for &lt;code&gt;Cutoff&lt;/code&gt;. For example, if the maintenance window starts at 3 PM, the duration is three hours, and the value you specify for &lt;code&gt;Cutoff&lt;/code&gt; is one hour, no maintenance window tasks can start after 5 PM.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def create_ops_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_ops_item

    &lt;p&gt;Creates a new OpsItem. You must have permission in Identity and Access Management (IAM) to create a new OpsItem. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html\&quot;&gt;Set up OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html\&quot;&gt;Amazon Web Services Systems Manager OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;. &lt;/p&gt;

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
    body = CreateOpsItemRequest.from_dict(body)
    return web.Response(status=200)


async def create_ops_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_ops_metadata

    If you create a new application in Application Manager, Amazon Web Services Systems Manager calls this API operation to specify information about the new application, including the application type.

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
    body = CreateOpsMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def create_patch_baseline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_patch_baseline

    &lt;p&gt;Creates a patch baseline.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For information about valid key-value pairs in &lt;code&gt;PatchFilters&lt;/code&gt; for each supported operating system type, see &lt;a&gt;PatchFilter&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreatePatchBaselineRequest.from_dict(body)
    return web.Response(status=200)


async def create_resource_data_sync(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_resource_data_sync

    &lt;p&gt;A resource data sync helps you view data from multiple sources in a single location. Amazon Web Services Systems Manager offers two types of resource data sync: &lt;code&gt;SyncToDestination&lt;/code&gt; and &lt;code&gt;SyncFromSource&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can configure Systems Manager Inventory to use the &lt;code&gt;SyncToDestination&lt;/code&gt; type to synchronize Inventory data from multiple Amazon Web Services Regions to a single Amazon Simple Storage Service (Amazon S3) bucket. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-datasync.html\&quot;&gt;Configuring resource data sync for Inventory&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can configure Systems Manager Explorer to use the &lt;code&gt;SyncFromSource&lt;/code&gt; type to synchronize operational work items (OpsItems) and operational data (OpsData) from multiple Amazon Web Services Regions to a single Amazon S3 bucket. This type can synchronize OpsItems and OpsData from multiple Amazon Web Services accounts and Amazon Web Services Regions or &lt;code&gt;EntireOrganization&lt;/code&gt; by using Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html\&quot;&gt;Setting up Systems Manager Explorer to display data from multiple accounts and Regions&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;A resource data sync is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data. To check the status of a sync, use the &lt;a&gt;ListResourceDataSync&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;By default, data isn&#39;t encrypted in Amazon S3. We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy. &lt;/p&gt; &lt;/note&gt;

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
    body = CreateResourceDataSyncRequest.from_dict(body)
    return web.Response(status=200)


async def delete_activation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_activation

    Deletes an activation. You aren&#39;t required to delete an activation. If you delete an activation, you can no longer use it to register additional managed nodes. Deleting an activation doesn&#39;t de-register managed nodes. You must manually de-register managed nodes.

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
    body = DeleteActivationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_association

    &lt;p&gt;Disassociates the specified Amazon Web Services Systems Manager document (SSM document) from the specified managed node. If you created the association by using the &lt;code&gt;Targets&lt;/code&gt; parameter, then you must delete the association by using the association ID.&lt;/p&gt; &lt;p&gt;When you disassociate a document from a managed node, it doesn&#39;t change the configuration of the node. To change the configuration state of a managed node after you disassociate a document, you must create a new document with the desired configuration and associate it with the node.&lt;/p&gt;

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
    body = DeleteAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_document

    &lt;p&gt;Deletes the Amazon Web Services Systems Manager document (SSM document) and all managed node associations to the document.&lt;/p&gt; &lt;p&gt;Before you delete the document, we recommend that you use &lt;a&gt;DeleteAssociation&lt;/a&gt; to disassociate all managed nodes that are associated with the document.&lt;/p&gt;

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
    body = DeleteDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_inventory(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_inventory

    Delete a custom inventory type or the data associated with a custom Inventory type. Deleting a custom inventory type is also referred to as deleting a custom inventory schema.

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
    body = DeleteInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def delete_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_maintenance_window

    Deletes a maintenance window.

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
    body = DeleteMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def delete_ops_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_ops_metadata

    Delete OpsMetadata related to an application.

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
    body = DeleteOpsMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def delete_parameter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_parameter

    Delete a parameter from the system. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.

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
    body = DeleteParameterRequest.from_dict(body)
    return web.Response(status=200)


async def delete_parameters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_parameters

    Delete a list of parameters. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.

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
    body = DeleteParametersRequest.from_dict(body)
    return web.Response(status=200)


async def delete_patch_baseline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_patch_baseline

    Deletes a patch baseline.

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
    body = DeletePatchBaselineRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_data_sync(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_data_sync

    Deletes a resource data sync configuration. After the configuration is deleted, changes to data on managed nodes are no longer synced to or from the target. Deleting a sync configuration doesn&#39;t delete data.

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
    body = DeleteResourceDataSyncRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

    Deletes a Systems Manager resource policy. A resource policy helps you to define the IAM entity (for example, an Amazon Web Services account) that can manage your Systems Manager resources. Currently, &lt;code&gt;OpsItemGroup&lt;/code&gt; is the only resource that supports Systems Manager resource policies. The resource policy for &lt;code&gt;OpsItemGroup&lt;/code&gt; enables Amazon Web Services accounts to view and interact with OpsCenter operational work items (OpsItems).

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


async def deregister_managed_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_managed_instance

    Removes the server or virtual machine from the list of registered servers. You can reregister the node again at any time. If you don&#39;t plan to use Run Command on the server, we suggest uninstalling SSM Agent first.

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
    body = DeregisterManagedInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_patch_baseline_for_patch_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_patch_baseline_for_patch_group

    Removes a patch group from a patch baseline.

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
    body = DeregisterPatchBaselineForPatchGroupRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_target_from_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_target_from_maintenance_window

    Removes a target from a maintenance window.

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
    body = DeregisterTargetFromMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_task_from_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_task_from_maintenance_window

    Removes a task from a maintenance window.

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
    body = DeregisterTaskFromMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def describe_activations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_activations

    Describes details about the activation, such as the date and time the activation was created, its expiration date, the Identity and Access Management (IAM) role assigned to the managed nodes in the activation, and the number of nodes registered by using this activation.

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
    body = DescribeActivationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_association

    Describes the association for the specified target or managed node. If you created the association by using the &lt;code&gt;Targets&lt;/code&gt; parameter, then you must retrieve the association by using the association ID.

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
    body = DescribeAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_association_execution_targets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_association_execution_targets

    Views information about a specific execution of a specific association.

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
    body = DescribeAssociationExecutionTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_association_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_association_executions

    Views all executions for a specific association ID. 

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
    body = DescribeAssociationExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_automation_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_automation_executions

    Provides details about all active and terminated Automation executions.

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
    body = DescribeAutomationExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_automation_step_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_automation_step_executions

    Information about all active and terminated step executions in an Automation workflow.

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
    body = DescribeAutomationStepExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_available_patches(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_available_patches

    Lists all patches eligible to be included in a patch baseline.

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
    body = DescribeAvailablePatchesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_document

    Describes the specified Amazon Web Services Systems Manager document (SSM document).

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
    body = DescribeDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def describe_document_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_document_permission

    Describes the permissions for a Amazon Web Services Systems Manager document (SSM document). If you created the document, you are the owner. If a document is shared, it can either be shared privately (by specifying a user&#39;s Amazon Web Services account ID) or publicly (&lt;i&gt;All&lt;/i&gt;). 

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
    body = DescribeDocumentPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def describe_effective_instance_associations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_effective_instance_associations

    All associations for the managed node(s).

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
    body = DescribeEffectiveInstanceAssociationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_effective_patches_for_patch_baseline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_effective_patches_for_patch_baseline

    Retrieves the current effective patches (the patch and the approval state) for the specified patch baseline. Applies to patch baselines for Windows only.

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
    body = DescribeEffectivePatchesForPatchBaselineRequest.from_dict(body)
    return web.Response(status=200)


async def describe_instance_associations_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_instance_associations_status

    The status of the associations for the managed node(s).

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
    body = DescribeInstanceAssociationsStatusRequest.from_dict(body)
    return web.Response(status=200)


async def describe_instance_information(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_instance_information

    &lt;p&gt;Provides information about one or more of your managed nodes, including the operating system platform, SSM Agent version, association status, and IP address. This operation does not return information for nodes that are either Stopped or Terminated.&lt;/p&gt; &lt;p&gt;If you specify one or more node IDs, the operation returns information for those managed nodes. If you don&#39;t specify node IDs, it returns information for all your managed nodes. If you specify a node ID that isn&#39;t valid or a node that you don&#39;t own, you receive an error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;IamRole&lt;/code&gt; field returned for this API operation is the Identity and Access Management (IAM) role assigned to on-premises managed nodes. This operation does not return the IAM role for EC2 instances.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeInstanceInformationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_instance_patch_states(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_instance_patch_states

    Retrieves the high-level patch state of one or more managed nodes.

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
    body = DescribeInstancePatchStatesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_instance_patch_states_for_patch_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_instance_patch_states_for_patch_group

    Retrieves the high-level patch state for the managed nodes in the specified patch group.

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
    body = DescribeInstancePatchStatesForPatchGroupRequest.from_dict(body)
    return web.Response(status=200)


async def describe_instance_patches(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_instance_patches

    Retrieves information about the patches on the specified managed node and their state relative to the patch baseline being used for the node.

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
    body = DescribeInstancePatchesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_inventory_deletions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_inventory_deletions

    Describes a specific delete inventory operation.

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
    body = DescribeInventoryDeletionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_window_execution_task_invocations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_window_execution_task_invocations

    Retrieves the individual task executions (one per target) for a particular task run as part of a maintenance window execution.

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
    body = DescribeMaintenanceWindowExecutionTaskInvocationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_window_execution_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_window_execution_tasks

    For a given maintenance window execution, lists the tasks that were run.

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
    body = DescribeMaintenanceWindowExecutionTasksRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_window_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_window_executions

    Lists the executions of a maintenance window. This includes information about when the maintenance window was scheduled to be active, and information about tasks registered and run with the maintenance window.

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
    body = DescribeMaintenanceWindowExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_window_schedule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_window_schedule

    Retrieves information about upcoming executions of a maintenance window.

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
    body = DescribeMaintenanceWindowScheduleRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_window_targets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_window_targets

    Lists the targets registered with the maintenance window.

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
    body = DescribeMaintenanceWindowTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_window_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_window_tasks

    &lt;p&gt;Lists the tasks in a maintenance window.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For maintenance window tasks without a specified target, you can&#39;t supply values for &lt;code&gt;--max-errors&lt;/code&gt; and &lt;code&gt;--max-concurrency&lt;/code&gt;. Instead, the system inserts a placeholder value of &lt;code&gt;1&lt;/code&gt;, which may be reported in the response to this command. These values don&#39;t affect the running of your task and can be ignored.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeMaintenanceWindowTasksRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_windows(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_windows

    Retrieves the maintenance windows in an Amazon Web Services account.

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
    body = DescribeMaintenanceWindowsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_windows_for_target(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_maintenance_windows_for_target

    Retrieves information about the maintenance window targets or tasks that a managed node is associated with.

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
    body = DescribeMaintenanceWindowsForTargetRequest.from_dict(body)
    return web.Response(status=200)


async def describe_ops_items(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_ops_items

    &lt;p&gt;Query a set of OpsItems. You must have permission in Identity and Access Management (IAM) to query a list of OpsItems. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html\&quot;&gt;Set up OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html\&quot;&gt;OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;. &lt;/p&gt;

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
    body = DescribeOpsItemsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_parameters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_parameters

    &lt;p&gt;Get information about a parameter.&lt;/p&gt; &lt;p&gt;Request results are returned on a best-effort basis. If you specify &lt;code&gt;MaxResults&lt;/code&gt; in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of &lt;code&gt;MaxResults&lt;/code&gt;. If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a &lt;code&gt;NextToken&lt;/code&gt;. You can specify the &lt;code&gt;NextToken&lt;/code&gt; in a subsequent call to get the next set of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you change the KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, &lt;code&gt;DescribeParameters&lt;/code&gt; retrieves whatever the original key alias was referencing.&lt;/p&gt; &lt;/important&gt;

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
    body = DescribeParametersRequest.from_dict(body)
    return web.Response(status=200)


async def describe_patch_baselines(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_patch_baselines

    Lists the patch baselines in your Amazon Web Services account.

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
    body = DescribePatchBaselinesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_patch_group_state(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_patch_group_state

    Returns high-level aggregated patch compliance state information for a patch group.

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
    body = DescribePatchGroupStateRequest.from_dict(body)
    return web.Response(status=200)


async def describe_patch_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_patch_groups

    Lists all patch groups that have been registered with patch baselines.

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
    body = DescribePatchGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_patch_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_patch_properties

    &lt;p&gt;Lists the properties of available patches organized by product, product family, classification, severity, and other properties of available patches. You can use the reported properties in the filters you specify in requests for operations such as &lt;a&gt;CreatePatchBaseline&lt;/a&gt;, &lt;a&gt;UpdatePatchBaseline&lt;/a&gt;, &lt;a&gt;DescribeAvailablePatches&lt;/a&gt;, and &lt;a&gt;DescribePatchBaselines&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following section lists the properties that can be used in filters for each major operating system type:&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;AMAZON_LINUX&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; | &lt;code&gt;SEVERITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;AMAZON_LINUX_2&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; | &lt;code&gt;SEVERITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;CENTOS&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; | &lt;code&gt;SEVERITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;DEBIAN&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;PRIORITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;MACOS&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;ORACLE_LINUX&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; | &lt;code&gt;SEVERITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;REDHAT_ENTERPRISE_LINUX&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; | &lt;code&gt;SEVERITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;SUSE&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; | &lt;code&gt;SEVERITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;UBUNTU&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;PRIORITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;WINDOWS&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Valid properties: &lt;code&gt;PRODUCT&lt;/code&gt; | &lt;code&gt;PRODUCT_FAMILY&lt;/code&gt; | &lt;code&gt;CLASSIFICATION&lt;/code&gt; | &lt;code&gt;MSRC_SEVERITY&lt;/code&gt; &lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt;

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
    body = DescribePatchPropertiesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_sessions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_sessions

    Retrieves a list of all active sessions (both connected and disconnected) or terminated sessions from the past 30 days.

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
    body = DescribeSessionsRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_ops_item_related_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_ops_item_related_item

    Deletes the association between an OpsItem and a related item. For example, this API operation can delete an Incident Manager incident from an OpsItem. Incident Manager is a capability of Amazon Web Services Systems Manager.

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
    body = DisassociateOpsItemRelatedItemRequest.from_dict(body)
    return web.Response(status=200)


async def get_automation_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_automation_execution

    Get detailed information about a particular Automation execution.

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
    body = GetAutomationExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def get_calendar_state(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_calendar_state

    &lt;p&gt;Gets the state of a Amazon Web Services Systems Manager change calendar at the current time or a specified time. If you specify a time, &lt;code&gt;GetCalendarState&lt;/code&gt; returns the state of the calendar at that specific time, and returns the next time that the change calendar state will transition. If you don&#39;t specify a time, &lt;code&gt;GetCalendarState&lt;/code&gt; uses the current time. Change Calendar entries have two possible states: &lt;code&gt;OPEN&lt;/code&gt; or &lt;code&gt;CLOSED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you specify more than one calendar in a request, the command returns the status of &lt;code&gt;OPEN&lt;/code&gt; only if all calendars in the request are open. If one or more calendars in the request are closed, the status returned is &lt;code&gt;CLOSED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about Change Calendar, a capability of Amazon Web Services Systems Manager, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html\&quot;&gt;Amazon Web Services Systems Manager Change Calendar&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = GetCalendarStateRequest.from_dict(body)
    return web.Response(status=200)


async def get_command_invocation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_command_invocation

    &lt;p&gt;Returns detailed information about command execution for an invocation or plugin.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetCommandInvocation&lt;/code&gt; only gives the execution status of a plugin in a document. To get the command execution status on a specific managed node, use &lt;a&gt;ListCommandInvocations&lt;/a&gt;. To get the command execution status across managed nodes, use &lt;a&gt;ListCommands&lt;/a&gt;.&lt;/p&gt;

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
    body = GetCommandInvocationRequest.from_dict(body)
    return web.Response(status=200)


async def get_connection_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_connection_status

    Retrieves the Session Manager connection status for a managed node to determine whether it is running and ready to receive Session Manager connections.

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
    body = GetConnectionStatusRequest.from_dict(body)
    return web.Response(status=200)


async def get_default_patch_baseline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_default_patch_baseline

    &lt;p&gt;Retrieves the default patch baseline. Amazon Web Services Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify an operating system value, the default patch baseline for Windows is returned.&lt;/p&gt;

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
    body = GetDefaultPatchBaselineRequest.from_dict(body)
    return web.Response(status=200)


async def get_deployable_patch_snapshot_for_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_deployable_patch_snapshot_for_instance

    &lt;p&gt;Retrieves the current snapshot for the patch baseline the managed node uses. This API is primarily used by the &lt;code&gt;AWS-RunPatchBaseline&lt;/code&gt; Systems Manager document (SSM document).&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you run the command locally, such as with the Command Line Interface (CLI), the system attempts to use your local Amazon Web Services credentials and the operation fails. To avoid this, you can run the command in the Amazon Web Services Systems Manager console. Use Run Command, a capability of Amazon Web Services Systems Manager, with an SSM document that enables you to target a managed node with a script or command. For example, run the command using the &lt;code&gt;AWS-RunShellScript&lt;/code&gt; document or the &lt;code&gt;AWS-RunPowerShellScript&lt;/code&gt; document.&lt;/p&gt; &lt;/note&gt;

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
    body = GetDeployablePatchSnapshotForInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def get_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_document

    Gets the contents of the specified Amazon Web Services Systems Manager document (SSM document).

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
    body = GetDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def get_inventory(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_inventory

    Query inventory information. This includes managed node status, such as &lt;code&gt;Stopped&lt;/code&gt; or &lt;code&gt;Terminated&lt;/code&gt;.

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
    body = GetInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def get_inventory_schema(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_inventory_schema

    Return a list of inventory type names for the account, or return a list of attribute names for a specific Inventory item type.

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
    body = GetInventorySchemaRequest.from_dict(body)
    return web.Response(status=200)


async def get_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_maintenance_window

    Retrieves a maintenance window.

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
    body = GetMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def get_maintenance_window_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_maintenance_window_execution

    Retrieves details about a specific a maintenance window execution.

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
    body = GetMaintenanceWindowExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def get_maintenance_window_execution_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_maintenance_window_execution_task

    Retrieves the details about a specific task run as part of a maintenance window execution.

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
    body = GetMaintenanceWindowExecutionTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_maintenance_window_execution_task_invocation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_maintenance_window_execution_task_invocation

    Retrieves information about a specific task running on a specific target.

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
    body = GetMaintenanceWindowExecutionTaskInvocationRequest.from_dict(body)
    return web.Response(status=200)


async def get_maintenance_window_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_maintenance_window_task

    &lt;p&gt;Retrieves the details of a maintenance window task.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For maintenance window tasks without a specified target, you can&#39;t supply values for &lt;code&gt;--max-errors&lt;/code&gt; and &lt;code&gt;--max-concurrency&lt;/code&gt;. Instead, the system inserts a placeholder value of &lt;code&gt;1&lt;/code&gt;, which may be reported in the response to this command. These values don&#39;t affect the running of your task and can be ignored.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To retrieve a list of tasks in a maintenance window, instead use the &lt;a&gt;DescribeMaintenanceWindowTasks&lt;/a&gt; command.&lt;/p&gt;

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
    body = GetMaintenanceWindowTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_ops_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_ops_item

    &lt;p&gt;Get information about an OpsItem by using the ID. You must have permission in Identity and Access Management (IAM) to view information about an OpsItem. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html\&quot;&gt;Set up OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html\&quot;&gt;OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;. &lt;/p&gt;

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
    body = GetOpsItemRequest.from_dict(body)
    return web.Response(status=200)


async def get_ops_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_ops_metadata

    View operational metadata related to an application in Application Manager.

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
    body = GetOpsMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def get_ops_summary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_ops_summary

    View a summary of operations metadata (OpsData) based on specified filters and aggregators. OpsData can include information about Amazon Web Services Systems Manager OpsCenter operational workitems (OpsItems) as well as information about any Amazon Web Services resource or service configured to report OpsData to Amazon Web Services Systems Manager Explorer. 

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
    body = GetOpsSummaryRequest.from_dict(body)
    return web.Response(status=200)


async def get_parameter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_parameter

    &lt;p&gt;Get information about a single parameter by specifying the parameter name.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To get information about more than one parameter at a time, use the &lt;a&gt;GetParameters&lt;/a&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = GetParameterRequest.from_dict(body)
    return web.Response(status=200)


async def get_parameter_history(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_parameter_history

    &lt;p&gt;Retrieves the history of all changes to a parameter.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you change the KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, &lt;code&gt;GetParameterHistory&lt;/code&gt; retrieves whatever the original key alias was referencing.&lt;/p&gt; &lt;/important&gt;

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
    body = GetParameterHistoryRequest.from_dict(body)
    return web.Response(status=200)


async def get_parameters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_parameters

    &lt;p&gt;Get information about one or more parameters by specifying multiple parameter names.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To get information about a single parameter, you can use the &lt;a&gt;GetParameter&lt;/a&gt; operation instead.&lt;/p&gt; &lt;/note&gt;

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
    body = GetParametersRequest.from_dict(body)
    return web.Response(status=200)


async def get_parameters_by_path(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_parameters_by_path

    &lt;p&gt;Retrieve information about one or more parameters in a specific hierarchy. &lt;/p&gt; &lt;p&gt;Request results are returned on a best-effort basis. If you specify &lt;code&gt;MaxResults&lt;/code&gt; in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of &lt;code&gt;MaxResults&lt;/code&gt;. If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a &lt;code&gt;NextToken&lt;/code&gt;. You can specify the &lt;code&gt;NextToken&lt;/code&gt; in a subsequent call to get the next set of results.&lt;/p&gt;

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
    body = GetParametersByPathRequest.from_dict(body)
    return web.Response(status=200)


async def get_patch_baseline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_patch_baseline

    Retrieves information about a patch baseline.

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
    body = GetPatchBaselineRequest.from_dict(body)
    return web.Response(status=200)


async def get_patch_baseline_for_patch_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_patch_baseline_for_patch_group

    Retrieves the patch baseline that should be used for the specified patch group.

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
    body = GetPatchBaselineForPatchGroupRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_resource_policies

    Returns an array of the &lt;code&gt;Policy&lt;/code&gt; object.

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
    body = GetResourcePoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def get_service_setting(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_setting

    &lt;p&gt; &lt;code&gt;ServiceSetting&lt;/code&gt; is an account-level setting for an Amazon Web Services service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an Amazon Web Services service charges money to the account based on feature or service usage, then the Amazon Web Services service team might create a default setting of &lt;code&gt;false&lt;/code&gt;. This means the user can&#39;t use this feature unless they change the setting to &lt;code&gt;true&lt;/code&gt; and intentionally opt in for a paid feature.&lt;/p&gt; &lt;p&gt;Services map a &lt;code&gt;SettingId&lt;/code&gt; object to a setting value. Amazon Web Services services teams define the default value for a &lt;code&gt;SettingId&lt;/code&gt;. You can&#39;t create a new &lt;code&gt;SettingId&lt;/code&gt;, but you can overwrite the default value if you have the &lt;code&gt;ssm:UpdateServiceSetting&lt;/code&gt; permission for the setting. Use the &lt;a&gt;UpdateServiceSetting&lt;/a&gt; API operation to change the default setting. Or use the &lt;a&gt;ResetServiceSetting&lt;/a&gt; to change the value back to the original value defined by the Amazon Web Services service team.&lt;/p&gt; &lt;p&gt;Query the current service setting for the Amazon Web Services account. &lt;/p&gt;

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
    body = GetServiceSettingRequest.from_dict(body)
    return web.Response(status=200)


async def label_parameter_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """label_parameter_version

    &lt;p&gt;A parameter label is a user-defined alias to help you manage different versions of a parameter. When you modify a parameter, Amazon Web Services Systems Manager automatically saves a new version and increments the version number by one. A label can help you remember the purpose of a parameter when there are multiple versions. &lt;/p&gt; &lt;p&gt;Parameter labels have the following requirements and restrictions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A version of a parameter can have a maximum of 10 labels.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t attach the same label to different versions of the same parameter. For example, if version 1 has the label Production, then you can&#39;t attach Production to version 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can move a label from one version of a parameter to another.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t create a label when you create a new parameter. You must attach a label to a specific version of a parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you no longer want to use a parameter label, then you can either delete it or move it to a different version of a parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A label can have a maximum of 100 characters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Labels can contain letters (case sensitive), numbers, periods (.), hyphens (-), or underscores (_).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Labels can&#39;t begin with a number, \&quot;&lt;code&gt;aws&lt;/code&gt;\&quot; or \&quot;&lt;code&gt;ssm&lt;/code&gt;\&quot; (not case sensitive). If a label fails to meet these requirements, then the label isn&#39;t associated with a parameter and the system displays it in the list of InvalidLabels.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = LabelParameterVersionRequest.from_dict(body)
    return web.Response(status=200)


async def list_association_versions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_association_versions

    Retrieves all versions of an association for a specific association ID.

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
    body = ListAssociationVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_associations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_associations

    Returns all State Manager associations in the current Amazon Web Services account and Amazon Web Services Region. You can limit the results to a specific State Manager association document or managed node by specifying a filter. State Manager is a capability of Amazon Web Services Systems Manager.

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
    body = ListAssociationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_command_invocations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_command_invocations

    An invocation is copy of a command sent to a specific managed node. A command can apply to one or more managed nodes. A command invocation applies to one managed node. For example, if a user runs &lt;code&gt;SendCommand&lt;/code&gt; against three managed nodes, then a command invocation is created for each requested managed node ID. &lt;code&gt;ListCommandInvocations&lt;/code&gt; provide status about command execution.

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
    body = ListCommandInvocationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_commands(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_commands

    Lists the commands requested by users of the Amazon Web Services account.

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
    body = ListCommandsRequest.from_dict(body)
    return web.Response(status=200)


async def list_compliance_items(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_compliance_items

    For a specified resource ID, this API operation returns a list of compliance statuses for different resource types. Currently, you can only specify one resource ID per call. List results depend on the criteria specified in the filter.

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
    body = ListComplianceItemsRequest.from_dict(body)
    return web.Response(status=200)


async def list_compliance_summaries(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_compliance_summaries

    Returns a summary count of compliant and non-compliant resources for a compliance type. For example, this call can return State Manager associations, patches, or custom compliance types according to the filter criteria that you specify.

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
    body = ListComplianceSummariesRequest.from_dict(body)
    return web.Response(status=200)


async def list_document_metadata_history(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_document_metadata_history

    Information about approval reviews for a version of a change template in Change Manager.

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
    body = ListDocumentMetadataHistoryRequest.from_dict(body)
    return web.Response(status=200)


async def list_document_versions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_document_versions

    List all versions for a document.

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
    body = ListDocumentVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_documents(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_documents

    Returns all Systems Manager (SSM) documents in the current Amazon Web Services account and Amazon Web Services Region. You can limit the results of this request by using a filter.

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
    body = ListDocumentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_inventory_entries(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_inventory_entries

    A list of inventory items returned by the request.

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
    body = ListInventoryEntriesRequest.from_dict(body)
    return web.Response(status=200)


async def list_ops_item_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_ops_item_events

    Returns a list of all OpsItem events in the current Amazon Web Services Region and Amazon Web Services account. You can limit the results to events associated with specific OpsItems by specifying a filter.

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
    body = ListOpsItemEventsRequest.from_dict(body)
    return web.Response(status=200)


async def list_ops_item_related_items(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_ops_item_related_items

    Lists all related-item resources associated with a Systems Manager OpsCenter OpsItem. OpsCenter is a capability of Amazon Web Services Systems Manager.

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
    body = ListOpsItemRelatedItemsRequest.from_dict(body)
    return web.Response(status=200)


async def list_ops_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_ops_metadata

    Amazon Web Services Systems Manager calls this API operation when displaying all Application Manager OpsMetadata objects or blobs.

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
    body = ListOpsMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def list_resource_compliance_summaries(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_resource_compliance_summaries

    Returns a resource-level summary count. The summary includes information about compliant and non-compliant statuses and detailed compliance-item severity counts, according to the filter criteria you specify.

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
    body = ListResourceComplianceSummariesRequest.from_dict(body)
    return web.Response(status=200)


async def list_resource_data_sync(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_resource_data_sync

    &lt;p&gt;Lists your resource data sync configurations. Includes information about the last time a sync attempted to start, the last sync status, and the last time a sync successfully completed.&lt;/p&gt; &lt;p&gt;The number of sync configurations might be too large to return using a single call to &lt;code&gt;ListResourceDataSync&lt;/code&gt;. You can limit the number of sync configurations returned by using the &lt;code&gt;MaxResults&lt;/code&gt; parameter. To determine whether there are more sync configurations to list, check the value of &lt;code&gt;NextToken&lt;/code&gt; in the output. If there are more sync configurations to list, you can request them by specifying the &lt;code&gt;NextToken&lt;/code&gt; returned in the call to the parameter of a subsequent call. &lt;/p&gt;

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
    body = ListResourceDataSyncRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Returns a list of the tags assigned to the specified resource.&lt;/p&gt; &lt;p&gt;For information about the ID format for each supported resource type, see &lt;a&gt;AddTagsToResource&lt;/a&gt;.&lt;/p&gt;

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


async def modify_document_permission(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """modify_document_permission

    Shares a Amazon Web Services Systems Manager document (SSM document)publicly or privately. If you share a document privately, you must specify the Amazon Web Services user IDs for those people who can use the document. If you share a document publicly, you must specify &lt;i&gt;All&lt;/i&gt; as the account ID.

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
    body = ModifyDocumentPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def put_compliance_items(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_compliance_items

    &lt;p&gt;Registers a compliance type and other compliance details on a designated resource. This operation lets you register custom compliance details with a resource. This call overwrites existing compliance information on the resource, so you must provide a full list of compliance items each time that you send the request.&lt;/p&gt; &lt;p&gt;ComplianceType can be one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;ExecutionId: The execution ID when the patch, association, or custom compliance item was applied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ExecutionType: Specify patch, association, or Custom:&lt;code&gt;string&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ExecutionTime. The time the patch, association, or custom compliance item was applied to the managed node.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Id: The patch, association, or custom compliance ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Title: A title.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Status: The status of the compliance item. For example, &lt;code&gt;approved&lt;/code&gt; for patches, or &lt;code&gt;Failed&lt;/code&gt; for associations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Severity: A patch severity. For example, &lt;code&gt;Critical&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DocumentName: An SSM document name. For example, &lt;code&gt;AWS-RunPatchBaseline&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DocumentVersion: An SSM document version number. For example, 4.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Classification: A patch classification. For example, &lt;code&gt;security updates&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;PatchBaselineId: A patch baseline ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;PatchSeverity: A patch severity. For example, &lt;code&gt;Critical&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;PatchState: A patch state. For example, &lt;code&gt;InstancesWithFailedPatches&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;PatchGroup: The name of a patch group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;InstalledTime: The time the association, patch, or custom compliance item was applied to the resource. Specify the time by using the following format: yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = PutComplianceItemsRequest.from_dict(body)
    return web.Response(status=200)


async def put_inventory(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_inventory

    Bulk update custom inventory items on one or more managed nodes. The request adds an inventory item, if it doesn&#39;t already exist, or updates an inventory item, if it does exist.

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
    body = PutInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def put_parameter(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_parameter

    Add a parameter to the system.

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
    body = PutParameterRequest.from_dict(body)
    return web.Response(status=200)


async def put_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

    Creates or updates a Systems Manager resource policy. A resource policy helps you to define the IAM entity (for example, an Amazon Web Services account) that can manage your Systems Manager resources. Currently, &lt;code&gt;OpsItemGroup&lt;/code&gt; is the only resource that supports Systems Manager resource policies. The resource policy for &lt;code&gt;OpsItemGroup&lt;/code&gt; enables Amazon Web Services accounts to view and interact with OpsCenter operational work items (OpsItems).

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


async def register_default_patch_baseline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_default_patch_baseline

    &lt;p&gt;Defines the default patch baseline for the relevant operating system.&lt;/p&gt; &lt;p&gt;To reset the Amazon Web Services-predefined patch baseline as the default, specify the full patch baseline Amazon Resource Name (ARN) as the baseline ID value. For example, for CentOS, specify &lt;code&gt;arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646ed&lt;/code&gt; instead of &lt;code&gt;pb-0574b43a65ea646ed&lt;/code&gt;.&lt;/p&gt;

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
    body = RegisterDefaultPatchBaselineRequest.from_dict(body)
    return web.Response(status=200)


async def register_patch_baseline_for_patch_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_patch_baseline_for_patch_group

    Registers a patch baseline for a patch group.

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
    body = RegisterPatchBaselineForPatchGroupRequest.from_dict(body)
    return web.Response(status=200)


async def register_target_with_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_target_with_maintenance_window

    Registers a target with a maintenance window.

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
    body = RegisterTargetWithMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def register_task_with_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_task_with_maintenance_window

    Adds a new task to a maintenance window.

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
    body = RegisterTaskWithMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def remove_tags_from_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_tags_from_resource

    Removes tag keys from the specified resource.

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
    body = RemoveTagsFromResourceRequest.from_dict(body)
    return web.Response(status=200)


async def reset_service_setting(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reset_service_setting

    &lt;p&gt; &lt;code&gt;ServiceSetting&lt;/code&gt; is an account-level setting for an Amazon Web Services service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an Amazon Web Services service charges money to the account based on feature or service usage, then the Amazon Web Services service team might create a default setting of \&quot;false\&quot;. This means the user can&#39;t use this feature unless they change the setting to \&quot;true\&quot; and intentionally opt in for a paid feature.&lt;/p&gt; &lt;p&gt;Services map a &lt;code&gt;SettingId&lt;/code&gt; object to a setting value. Amazon Web Services services teams define the default value for a &lt;code&gt;SettingId&lt;/code&gt;. You can&#39;t create a new &lt;code&gt;SettingId&lt;/code&gt;, but you can overwrite the default value if you have the &lt;code&gt;ssm:UpdateServiceSetting&lt;/code&gt; permission for the setting. Use the &lt;a&gt;GetServiceSetting&lt;/a&gt; API operation to view the current value. Use the &lt;a&gt;UpdateServiceSetting&lt;/a&gt; API operation to change the default setting. &lt;/p&gt; &lt;p&gt;Reset the service setting for the account to the default value as provisioned by the Amazon Web Services service team. &lt;/p&gt;

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
    body = ResetServiceSettingRequest.from_dict(body)
    return web.Response(status=200)


async def resume_session(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resume_session

    &lt;p&gt;Reconnects a session to a managed node after it has been disconnected. Connections can be resumed for disconnected sessions, but not terminated sessions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This command is primarily for use by client machines to automatically reconnect during intermittent network issues. It isn&#39;t intended for any other use.&lt;/p&gt; &lt;/note&gt;

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
    body = ResumeSessionRequest.from_dict(body)
    return web.Response(status=200)


async def send_automation_signal(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_automation_signal

    Sends a signal to an Automation execution to change the current behavior or status of the execution. 

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
    body = SendAutomationSignalRequest.from_dict(body)
    return web.Response(status=200)


async def send_command(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_command

    Runs commands on one or more managed nodes.

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
    body = SendCommandRequest.from_dict(body)
    return web.Response(status=200)


async def start_associations_once(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_associations_once

    Runs an association immediately and only one time. This operation can be helpful when troubleshooting associations.

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
    body = StartAssociationsOnceRequest.from_dict(body)
    return web.Response(status=200)


async def start_automation_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_automation_execution

    Initiates execution of an Automation runbook.

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
    body = StartAutomationExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def start_change_request_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_change_request_execution

    Creates a change request for Change Manager. The Automation runbooks specified in the change request run only after all required approvals for the change request have been received.

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
    body = StartChangeRequestExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def start_session(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_session

    &lt;p&gt;Initiates a connection to a target (for example, a managed node) for a Session Manager session. Returns a URL and token that can be used to open a WebSocket connection for sending input and receiving outputs.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Web Services CLI usage: &lt;code&gt;start-session&lt;/code&gt; is an interactive command that requires the Session Manager plugin to be installed on the client machine making the call. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html\&quot;&gt;Install the Session Manager plugin for the Amazon Web Services CLI&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Amazon Web Services Tools for PowerShell usage: Start-SSMSession isn&#39;t currently supported by Amazon Web Services Tools for PowerShell on Windows local machines.&lt;/p&gt; &lt;/note&gt;

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
    body = StartSessionRequest.from_dict(body)
    return web.Response(status=200)


async def stop_automation_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_automation_execution

    Stop an Automation that is currently running.

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
    body = StopAutomationExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def terminate_session(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """terminate_session

    Permanently ends a session and closes the data connection between the Session Manager client and SSM Agent on the managed node. A terminated session can&#39;t be resumed.

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
    body = TerminateSessionRequest.from_dict(body)
    return web.Response(status=200)


async def unlabel_parameter_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """unlabel_parameter_version

    Remove a label or labels from a parameter.

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
    body = UnlabelParameterVersionRequest.from_dict(body)
    return web.Response(status=200)


async def update_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_association

    &lt;p&gt;Updates an association. You can update the association name and version, the document version, schedule, parameters, and Amazon Simple Storage Service (Amazon S3) output. When you call &lt;code&gt;UpdateAssociation&lt;/code&gt;, the system removes all optional parameters from the request and overwrites the association with null values for those parameters. This is by design. You must specify all optional parameters in the call, even if you are not changing the parameters. This includes the &lt;code&gt;Name&lt;/code&gt; parameter. Before calling this API action, we recommend that you call the &lt;a&gt;DescribeAssociation&lt;/a&gt; API operation and make a note of all optional parameters required for your &lt;code&gt;UpdateAssociation&lt;/code&gt; call.&lt;/p&gt; &lt;p&gt;In order to call this API operation, a user, group, or role must be granted permission to call the &lt;a&gt;DescribeAssociation&lt;/a&gt; API operation. If you don&#39;t have permission to call &lt;code&gt;DescribeAssociation&lt;/code&gt;, then you receive the following error: &lt;code&gt;An error occurred (AccessDeniedException) when calling the UpdateAssociation operation: User: &amp;lt;user_arn&amp;gt; isn&#39;t authorized to perform: ssm:DescribeAssociation on resource: &amp;lt;resource_arn&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;important&gt; &lt;p&gt;When you update an association, the association immediately runs against the specified targets. You can add the &lt;code&gt;ApplyOnlyAtCronInterval&lt;/code&gt; parameter to run the association during the next schedule run.&lt;/p&gt; &lt;/important&gt;

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
    body = UpdateAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def update_association_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_association_status

    &lt;p&gt;Updates the status of the Amazon Web Services Systems Manager document (SSM document) associated with the specified managed node.&lt;/p&gt; &lt;p&gt; &lt;code&gt;UpdateAssociationStatus&lt;/code&gt; is primarily used by the Amazon Web Services Systems Manager Agent (SSM Agent) to report status updates about your associations and is only used for associations created with the &lt;code&gt;InstanceId&lt;/code&gt; legacy parameter.&lt;/p&gt;

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
    body = UpdateAssociationStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_document(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_document

    Updates one or more values for an SSM document.

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
    body = UpdateDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def update_document_default_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_document_default_version

    &lt;p&gt;Set the default version of a document. &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the &lt;code&gt;apply-only-at-cron-interval&lt;/code&gt; parameter.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateDocumentDefaultVersionRequest.from_dict(body)
    return web.Response(status=200)


async def update_document_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_document_metadata

    Updates information related to approval reviews for a specific version of a change template in Change Manager.

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
    body = UpdateDocumentMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def update_maintenance_window(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_maintenance_window

    &lt;p&gt;Updates an existing maintenance window. Only specified parameters are modified.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The value you specify for &lt;code&gt;Duration&lt;/code&gt; determines the specific end time for the maintenance window based on the time it begins. No maintenance window tasks are permitted to start after the resulting endtime minus the number of hours you specify for &lt;code&gt;Cutoff&lt;/code&gt;. For example, if the maintenance window starts at 3 PM, the duration is three hours, and the value you specify for &lt;code&gt;Cutoff&lt;/code&gt; is one hour, no maintenance window tasks can start after 5 PM.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateMaintenanceWindowRequest.from_dict(body)
    return web.Response(status=200)


async def update_maintenance_window_target(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_maintenance_window_target

    &lt;p&gt;Modifies the target of an existing maintenance window. You can change the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Name&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Owner&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IDs for an ID target&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tags for a Tag target&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;From any supported tag type to another. The three supported tag types are ID target, Tag target, and resource group. For more information, see &lt;a&gt;Target&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;If a parameter is null, then the corresponding field isn&#39;t modified.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateMaintenanceWindowTargetRequest.from_dict(body)
    return web.Response(status=200)


async def update_maintenance_window_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_maintenance_window_task

    &lt;p&gt;Modifies a task assigned to a maintenance window. You can&#39;t change the task type, but you can change the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TaskARN&lt;/code&gt;. For example, you can change a &lt;code&gt;RUN_COMMAND&lt;/code&gt; task from &lt;code&gt;AWS-RunPowerShellScript&lt;/code&gt; to &lt;code&gt;AWS-RunShellScript&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ServiceRoleArn&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TaskInvocationParameters&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Priority&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MaxConcurrency&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MaxErrors&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that don&#39;t specify targets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html\&quot;&gt;Registering maintenance window tasks without targets&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If the value for a parameter in &lt;code&gt;UpdateMaintenanceWindowTask&lt;/code&gt; is null, then the corresponding field isn&#39;t modified. If you set &lt;code&gt;Replace&lt;/code&gt; to true, then all fields required by the &lt;a&gt;RegisterTaskWithMaintenanceWindow&lt;/a&gt; operation are required for this request. Optional fields that aren&#39;t specified are set to null.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you update a maintenance window task that has options specified in &lt;code&gt;TaskInvocationParameters&lt;/code&gt;, you must provide again all the &lt;code&gt;TaskInvocationParameters&lt;/code&gt; values that you want to retain. The values you don&#39;t specify again are removed. For example, suppose that when you registered a Run Command task, you specified &lt;code&gt;TaskInvocationParameters&lt;/code&gt; values for &lt;code&gt;Comment&lt;/code&gt;, &lt;code&gt;NotificationConfig&lt;/code&gt;, and &lt;code&gt;OutputS3BucketName&lt;/code&gt;. If you update the maintenance window task and specify only a different &lt;code&gt;OutputS3BucketName&lt;/code&gt; value, the values for &lt;code&gt;Comment&lt;/code&gt; and &lt;code&gt;NotificationConfig&lt;/code&gt; are removed.&lt;/p&gt; &lt;/important&gt;

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
    body = UpdateMaintenanceWindowTaskRequest.from_dict(body)
    return web.Response(status=200)


async def update_managed_instance_role(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_managed_instance_role

    Changes the Identity and Access Management (IAM) role that is assigned to the on-premises server, edge device, or virtual machines (VM). IAM roles are first assigned to these hybrid nodes during the activation process. For more information, see &lt;a&gt;CreateActivation&lt;/a&gt;.

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
    body = UpdateManagedInstanceRoleRequest.from_dict(body)
    return web.Response(status=200)


async def update_ops_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_ops_item

    &lt;p&gt;Edit or change an OpsItem. You must have permission in Identity and Access Management (IAM) to update an OpsItem. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html\&quot;&gt;Set up OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html\&quot;&gt;OpsCenter&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;. &lt;/p&gt;

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
    body = UpdateOpsItemRequest.from_dict(body)
    return web.Response(status=200)


async def update_ops_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_ops_metadata

    Amazon Web Services Systems Manager calls this API operation when you edit OpsMetadata in Application Manager.

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
    body = UpdateOpsMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def update_patch_baseline(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_patch_baseline

    &lt;p&gt;Modifies an existing patch baseline. Fields not specified in the request are left unchanged.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For information about valid key-value pairs in &lt;code&gt;PatchFilters&lt;/code&gt; for each supported operating system type, see &lt;a&gt;PatchFilter&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdatePatchBaselineRequest.from_dict(body)
    return web.Response(status=200)


async def update_resource_data_sync(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_resource_data_sync

    &lt;p&gt;Update a resource data sync. After you create a resource data sync for a Region, you can&#39;t change the account options for that sync. For example, if you create a sync in the us-east-2 (Ohio) Region and you choose the &lt;code&gt;Include only the current account&lt;/code&gt; option, you can&#39;t edit that sync later and choose the &lt;code&gt;Include all accounts from my Organizations configuration&lt;/code&gt; option. Instead, you must delete the first resource data sync, and create a new one.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API operation only supports a resource data sync that was created with a SyncFromSource &lt;code&gt;SyncType&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateResourceDataSyncRequest.from_dict(body)
    return web.Response(status=200)


async def update_service_setting(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_setting

    &lt;p&gt; &lt;code&gt;ServiceSetting&lt;/code&gt; is an account-level setting for an Amazon Web Services service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an Amazon Web Services service charges money to the account based on feature or service usage, then the Amazon Web Services service team might create a default setting of \&quot;false\&quot;. This means the user can&#39;t use this feature unless they change the setting to \&quot;true\&quot; and intentionally opt in for a paid feature.&lt;/p&gt; &lt;p&gt;Services map a &lt;code&gt;SettingId&lt;/code&gt; object to a setting value. Amazon Web Services services teams define the default value for a &lt;code&gt;SettingId&lt;/code&gt;. You can&#39;t create a new &lt;code&gt;SettingId&lt;/code&gt;, but you can overwrite the default value if you have the &lt;code&gt;ssm:UpdateServiceSetting&lt;/code&gt; permission for the setting. Use the &lt;a&gt;GetServiceSetting&lt;/a&gt; API operation to view the current value. Or, use the &lt;a&gt;ResetServiceSetting&lt;/a&gt; to change the value back to the original value defined by the Amazon Web Services service team.&lt;/p&gt; &lt;p&gt;Update the service setting for the account. &lt;/p&gt;

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
    body = UpdateServiceSettingRequest.from_dict(body)
    return web.Response(status=200)
