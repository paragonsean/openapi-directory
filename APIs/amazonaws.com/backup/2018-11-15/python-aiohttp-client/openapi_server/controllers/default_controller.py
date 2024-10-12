from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_backup_plan_output import CreateBackupPlanOutput
from openapi_server.models.create_backup_plan_request import CreateBackupPlanRequest
from openapi_server.models.create_backup_selection_output import CreateBackupSelectionOutput
from openapi_server.models.create_backup_selection_request import CreateBackupSelectionRequest
from openapi_server.models.create_backup_vault_output import CreateBackupVaultOutput
from openapi_server.models.create_backup_vault_request import CreateBackupVaultRequest
from openapi_server.models.create_framework_output import CreateFrameworkOutput
from openapi_server.models.create_framework_request import CreateFrameworkRequest
from openapi_server.models.create_legal_hold_output import CreateLegalHoldOutput
from openapi_server.models.create_legal_hold_request import CreateLegalHoldRequest
from openapi_server.models.create_report_plan_output import CreateReportPlanOutput
from openapi_server.models.create_report_plan_request import CreateReportPlanRequest
from openapi_server.models.describe_backup_job_output import DescribeBackupJobOutput
from openapi_server.models.describe_backup_vault_output import DescribeBackupVaultOutput
from openapi_server.models.describe_copy_job_output import DescribeCopyJobOutput
from openapi_server.models.describe_framework_output import DescribeFrameworkOutput
from openapi_server.models.describe_global_settings_output import DescribeGlobalSettingsOutput
from openapi_server.models.describe_protected_resource_output import DescribeProtectedResourceOutput
from openapi_server.models.describe_recovery_point_output import DescribeRecoveryPointOutput
from openapi_server.models.describe_region_settings_output import DescribeRegionSettingsOutput
from openapi_server.models.describe_report_job_output import DescribeReportJobOutput
from openapi_server.models.describe_report_plan_output import DescribeReportPlanOutput
from openapi_server.models.describe_restore_job_output import DescribeRestoreJobOutput
from openapi_server.models.export_backup_plan_template_output import ExportBackupPlanTemplateOutput
from openapi_server.models.get_backup_plan_from_json_output import GetBackupPlanFromJSONOutput
from openapi_server.models.get_backup_plan_from_json_request import GetBackupPlanFromJSONRequest
from openapi_server.models.get_backup_plan_from_template_output import GetBackupPlanFromTemplateOutput
from openapi_server.models.get_backup_plan_output import GetBackupPlanOutput
from openapi_server.models.get_backup_selection_output import GetBackupSelectionOutput
from openapi_server.models.get_backup_vault_access_policy_output import GetBackupVaultAccessPolicyOutput
from openapi_server.models.get_backup_vault_notifications_output import GetBackupVaultNotificationsOutput
from openapi_server.models.get_legal_hold_output import GetLegalHoldOutput
from openapi_server.models.get_recovery_point_restore_metadata_output import GetRecoveryPointRestoreMetadataOutput
from openapi_server.models.get_supported_resource_types_output import GetSupportedResourceTypesOutput
from openapi_server.models.list_backup_jobs_output import ListBackupJobsOutput
from openapi_server.models.list_backup_plan_templates_output import ListBackupPlanTemplatesOutput
from openapi_server.models.list_backup_plan_versions_output import ListBackupPlanVersionsOutput
from openapi_server.models.list_backup_plans_output import ListBackupPlansOutput
from openapi_server.models.list_backup_selections_output import ListBackupSelectionsOutput
from openapi_server.models.list_backup_vaults_output import ListBackupVaultsOutput
from openapi_server.models.list_copy_jobs_output import ListCopyJobsOutput
from openapi_server.models.list_frameworks_output import ListFrameworksOutput
from openapi_server.models.list_legal_holds_output import ListLegalHoldsOutput
from openapi_server.models.list_protected_resources_output import ListProtectedResourcesOutput
from openapi_server.models.list_recovery_points_by_backup_vault_output import ListRecoveryPointsByBackupVaultOutput
from openapi_server.models.list_recovery_points_by_legal_hold_output import ListRecoveryPointsByLegalHoldOutput
from openapi_server.models.list_recovery_points_by_resource_output import ListRecoveryPointsByResourceOutput
from openapi_server.models.list_report_jobs_output import ListReportJobsOutput
from openapi_server.models.list_report_plans_output import ListReportPlansOutput
from openapi_server.models.list_restore_jobs_output import ListRestoreJobsOutput
from openapi_server.models.put_backup_vault_access_policy_request import PutBackupVaultAccessPolicyRequest
from openapi_server.models.put_backup_vault_lock_configuration_request import PutBackupVaultLockConfigurationRequest
from openapi_server.models.put_backup_vault_notifications_request import PutBackupVaultNotificationsRequest
from openapi_server.models.start_backup_job_output import StartBackupJobOutput
from openapi_server.models.start_backup_job_request import StartBackupJobRequest
from openapi_server.models.start_copy_job_output import StartCopyJobOutput
from openapi_server.models.start_copy_job_request import StartCopyJobRequest
from openapi_server.models.start_report_job_output import StartReportJobOutput
from openapi_server.models.start_report_job_request import StartReportJobRequest
from openapi_server.models.start_restore_job_output import StartRestoreJobOutput
from openapi_server.models.start_restore_job_request import StartRestoreJobRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_framework_output import UpdateFrameworkOutput
from openapi_server.models.update_framework_request import UpdateFrameworkRequest
from openapi_server.models.update_global_settings_request import UpdateGlobalSettingsRequest
from openapi_server.models.update_recovery_point_lifecycle_output import UpdateRecoveryPointLifecycleOutput
from openapi_server.models.update_recovery_point_lifecycle_request import UpdateRecoveryPointLifecycleRequest
from openapi_server.models.update_region_settings_request import UpdateRegionSettingsRequest
from openapi_server.models.update_report_plan_output import UpdateReportPlanOutput
from openapi_server.models.update_report_plan_request import UpdateReportPlanRequest
from openapi_server import util


async def cancel_legal_hold(request: web.Request, legal_hold_id, cancel_description, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, retain_record_in_days=None) -> web.Response:
    """cancel_legal_hold

    This action removes the specified legal hold on a recovery point. This action can only be performed by a user with sufficient permissions.

    :param legal_hold_id: Legal hold ID required to remove the specified legal hold on a recovery point.
    :type legal_hold_id: str
    :param cancel_description: String describing the reason for removing the legal hold.
    :type cancel_description: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param retain_record_in_days: The integer amount in days specifying amount of days after this API operation to remove legal hold.
    :type retain_record_in_days: int

    """
    return web.Response(status=200)


async def create_backup_plan(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_backup_plan

    &lt;p&gt;Creates a backup plan using a backup plan name and backup rules. A backup plan is a document that contains information that Backup uses to schedule tasks that create recovery points for resources.&lt;/p&gt; &lt;p&gt;If you call &lt;code&gt;CreateBackupPlan&lt;/code&gt; with a plan that already exists, you receive an &lt;code&gt;AlreadyExistsException&lt;/code&gt; exception.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateBackupPlanRequest.from_dict(body)
    return web.Response(status=200)


async def create_backup_selection(request: web.Request, backup_plan_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_backup_selection

    Creates a JSON document that specifies a set of resources to assign to a backup plan. For examples, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-json\&quot;&gt;Assigning resources programmatically&lt;/a&gt;. 

    :param backup_plan_id: Uniquely identifies the backup plan to be associated with the selection of resources.
    :type backup_plan_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateBackupSelectionRequest.from_dict(body)
    return web.Response(status=200)


async def create_backup_vault(request: web.Request, backup_vault_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_backup_vault

    &lt;p&gt;Creates a logical container where backups are stored. A &lt;code&gt;CreateBackupVault&lt;/code&gt; request includes a name, optionally one or more resource tags, an encryption key, and a request ID.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Do not include sensitive data, such as passport numbers, in the name of a backup vault.&lt;/p&gt; &lt;/note&gt;

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateBackupVaultRequest.from_dict(body)
    return web.Response(status=200)


async def create_framework(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_framework

    Creates a framework with one or more controls. A framework is a collection of controls that you can use to evaluate your backup practices. By using pre-built customizable controls to define your policies, you can evaluate whether your backup practices comply with your policies and which resources are not yet in compliance.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateFrameworkRequest.from_dict(body)
    return web.Response(status=200)


async def create_legal_hold(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_legal_hold

    This action creates a legal hold on a recovery point (backup). A legal hold is a restraint on altering or deleting a backup until an authorized user cancels the legal hold. Any actions to delete or disassociate a recovery point will fail with an error if one or more active legal holds are on the recovery point.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateLegalHoldRequest.from_dict(body)
    return web.Response(status=200)


async def create_report_plan(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_report_plan

    &lt;p&gt;Creates a report plan. A report plan is a document that contains information about the contents of the report and where Backup will deliver it.&lt;/p&gt; &lt;p&gt;If you call &lt;code&gt;CreateReportPlan&lt;/code&gt; with a plan that already exists, you receive an &lt;code&gt;AlreadyExistsException&lt;/code&gt; exception.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateReportPlanRequest.from_dict(body)
    return web.Response(status=200)


async def delete_backup_selection(request: web.Request, backup_plan_id, selection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_backup_selection

    Deletes the resource selection associated with a backup plan that is specified by the &lt;code&gt;SelectionId&lt;/code&gt;.

    :param backup_plan_id: Uniquely identifies a backup plan.
    :type backup_plan_id: str
    :param selection_id: Uniquely identifies the body of a request to assign a set of resources to a backup plan.
    :type selection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_backup_vault(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_backup_vault

    Deletes the backup vault identified by its name. A vault can be deleted only if it is empty.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_backup_vault_access_policy(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_backup_vault_access_policy

    Deletes the policy document that manages permissions on a backup vault.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_backup_vault_lock_configuration(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_backup_vault_lock_configuration

    &lt;p&gt;Deletes Backup Vault Lock from a backup vault specified by a backup vault name.&lt;/p&gt; &lt;p&gt;If the Vault Lock configuration is immutable, then you cannot delete Vault Lock using API operations, and you will receive an &lt;code&gt;InvalidRequestException&lt;/code&gt; if you attempt to do so. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html\&quot;&gt;Vault Lock&lt;/a&gt; in the &lt;i&gt;Backup Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param backup_vault_name: The name of the backup vault from which to delete Backup Vault Lock.
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_backup_vault_notifications(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_backup_vault_notifications

    Deletes event notifications for the specified backup vault.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_framework(request: web.Request, framework_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_framework

    Deletes the framework specified by a framework name.

    :param framework_name: The unique name of a framework.
    :type framework_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_recovery_point(request: web.Request, backup_vault_name, recovery_point_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_recovery_point

    &lt;p&gt;Deletes the recovery point specified by a recovery point ID.&lt;/p&gt; &lt;p&gt;If the recovery point ID belongs to a continuous backup, calling this endpoint deletes the existing continuous backup and stops future continuous backup.&lt;/p&gt; &lt;p&gt;When an IAM role&#39;s permissions are insufficient to call this API, the service sends back an HTTP 200 response with an empty HTTP body, but the recovery point is not deleted. Instead, it enters an &lt;code&gt;EXPIRED&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt; &lt;code&gt;EXPIRED&lt;/code&gt; recovery points can be deleted with this API once the IAM role has the &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; action. To learn more about adding this role, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html#deleting-backups-troubleshooting\&quot;&gt; Troubleshooting manual deletions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the user or role is deleted or the permission within the role is removed, the deletion will not be successful and will enter an &lt;code&gt;EXPIRED&lt;/code&gt; state.&lt;/p&gt;

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;.
    :type recovery_point_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_report_plan(request: web.Request, report_plan_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_report_plan

    Deletes the report plan specified by a report plan name.

    :param report_plan_name: The unique name of a report plan.
    :type report_plan_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_backup_job(request: web.Request, backup_job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_backup_job

    Returns backup job details for the specified &lt;code&gt;BackupJobId&lt;/code&gt;.

    :param backup_job_id: Uniquely identifies a request to Backup to back up a resource.
    :type backup_job_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_backup_vault(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_backup_vault

    Returns metadata about a backup vault specified by its name.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_copy_job(request: web.Request, copy_job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_copy_job

    Returns metadata associated with creating a copy of a resource.

    :param copy_job_id: Uniquely identifies a copy job.
    :type copy_job_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_framework(request: web.Request, framework_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_framework

    Returns the framework details for the specified &lt;code&gt;FrameworkName&lt;/code&gt;.

    :param framework_name: The unique name of a framework.
    :type framework_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_global_settings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_global_settings

    Describes whether the Amazon Web Services account is opted in to cross-account backup. Returns an error if the account is not a member of an Organizations organization. Example: &lt;code&gt;describe-global-settings --region us-west-2&lt;/code&gt; 

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_protected_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_protected_resource

    Returns information about a saved resource, including the last time it was backed up, its Amazon Resource Name (ARN), and the Amazon Web Services service type of the saved resource.

    :param resource_arn: An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
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


async def describe_recovery_point(request: web.Request, backup_vault_name, recovery_point_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_recovery_point

    Returns metadata associated with a recovery point, including ID, status, encryption, and lifecycle.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;.
    :type recovery_point_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_region_settings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_region_settings

    Returns the current service opt-in settings for the Region. If service opt-in is enabled for a service, Backup tries to protect that service&#39;s resources in this Region, when the resource is included in an on-demand backup or scheduled backup plan. Otherwise, Backup does not try to protect that service&#39;s resources in this Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_report_job(request: web.Request, report_job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_report_job

    Returns the details associated with creating a report as specified by its &lt;code&gt;ReportJobId&lt;/code&gt;.

    :param report_job_id: The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. The report job ID cannot be edited.
    :type report_job_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_report_plan(request: web.Request, report_plan_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_report_plan

    Returns a list of all report plans for an Amazon Web Services account and Amazon Web Services Region.

    :param report_plan_name: The unique name of a report plan.
    :type report_plan_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def describe_restore_job(request: web.Request, restore_job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_restore_job

    Returns metadata associated with a restore job that is specified by a job ID.

    :param restore_job_id: Uniquely identifies the job that restores a recovery point.
    :type restore_job_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def disassociate_recovery_point(request: web.Request, backup_vault_name, recovery_point_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_recovery_point

    &lt;p&gt;Deletes the specified continuous backup recovery point from Backup and releases control of that continuous backup to the source service, such as Amazon RDS. The source service will continue to create and retain continuous backups using the lifecycle that you specified in your original backup plan.&lt;/p&gt; &lt;p&gt;Does not support snapshot backup recovery points.&lt;/p&gt;

    :param backup_vault_name: The unique name of an Backup vault.
    :type backup_vault_name: str
    :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies an Backup recovery point.
    :type recovery_point_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def disassociate_recovery_point_from_parent(request: web.Request, backup_vault_name, recovery_point_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_recovery_point_from_parent

    This action to a specific child (nested) recovery point removes the relationship between the specified recovery point and its parent (composite) recovery point.

    :param backup_vault_name: This is the name of a logical container where the child (nested) recovery point is stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param recovery_point_arn: This is the Amazon Resource Name (ARN) that uniquely identifies the child (nested) recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.&lt;/code&gt; 
    :type recovery_point_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def export_backup_plan_template(request: web.Request, backup_plan_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """export_backup_plan_template

    Returns the backup plan that is specified by the plan ID as a backup template.

    :param backup_plan_id: Uniquely identifies a backup plan.
    :type backup_plan_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_backup_plan(request: web.Request, backup_plan_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version_id=None) -> web.Response:
    """get_backup_plan

    Returns &lt;code&gt;BackupPlan&lt;/code&gt; details for the specified &lt;code&gt;BackupPlanId&lt;/code&gt;. The details are the body of a backup plan in JSON format, in addition to plan metadata.

    :param backup_plan_id: Uniquely identifies a backup plan.
    :type backup_plan_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version_id: Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
    :type version_id: str

    """
    return web.Response(status=200)


async def get_backup_plan_from_json(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_backup_plan_from_json

    Returns a valid JSON document specifying a backup plan or an error.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetBackupPlanFromJSONRequest.from_dict(body)
    return web.Response(status=200)


async def get_backup_plan_from_template(request: web.Request, template_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_backup_plan_from_template

    Returns the template specified by its &lt;code&gt;templateId&lt;/code&gt; as a backup plan.

    :param template_id: Uniquely identifies a stored backup plan template.
    :type template_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_backup_selection(request: web.Request, backup_plan_id, selection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_backup_selection

    Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.

    :param backup_plan_id: Uniquely identifies a backup plan.
    :type backup_plan_id: str
    :param selection_id: Uniquely identifies the body of a request to assign a set of resources to a backup plan.
    :type selection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_backup_vault_access_policy(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_backup_vault_access_policy

    Returns the access policy document that is associated with the named backup vault.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_backup_vault_notifications(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_backup_vault_notifications

    Returns event notifications for the specified backup vault.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_legal_hold(request: web.Request, legal_hold_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_legal_hold

    This action returns details for a specified legal hold. The details are the body of a legal hold in JSON format, in addition to metadata.

    :param legal_hold_id: This is the ID required to use &lt;code&gt;GetLegalHold&lt;/code&gt;. This unique ID is associated with a specific legal hold.
    :type legal_hold_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_recovery_point_restore_metadata(request: web.Request, backup_vault_name, recovery_point_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_recovery_point_restore_metadata

    Returns a set of metadata key-value pairs that were used to create the backup.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;.
    :type recovery_point_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_supported_resource_types(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_supported_resource_types

    Returns the Amazon Web Services resource types supported by Backup.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def list_backup_jobs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, resource_arn=None, state=None, backup_vault_name=None, created_before=None, created_after=None, resource_type=None, account_id=None, complete_after=None, complete_before=None, parent_job_id=None, max_results2=None, next_token2=None) -> web.Response:
    """list_backup_jobs

    Returns a list of existing backup jobs for an authenticated account for the last 30 days. For a longer period of time, consider using these &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html\&quot;&gt;monitoring tools&lt;/a&gt;.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param resource_arn: Returns only backup jobs that match the specified resource Amazon Resource Name (ARN).
    :type resource_arn: str
    :param state: Returns only backup jobs that are in the specified state.
    :type state: str
    :param backup_vault_name: Returns only backup jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param created_before: Returns only backup jobs that were created before the specified date.
    :type created_before: str
    :param created_after: Returns only backup jobs that were created after the specified date.
    :type created_after: str
    :param resource_type: &lt;p&gt;Returns only backup jobs for the specified resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Aurora&lt;/code&gt; for Amazon Aurora&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DocumentDB&lt;/code&gt; for Amazon DocumentDB (with MongoDB compatibility)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DynamoDB&lt;/code&gt; for Amazon DynamoDB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EBS&lt;/code&gt; for Amazon Elastic Block Store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EC2&lt;/code&gt; for Amazon Elastic Compute Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EFS&lt;/code&gt; for Amazon Elastic File System&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FSx&lt;/code&gt; for Amazon FSx&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Neptune&lt;/code&gt; for Amazon Neptune&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RDS&lt;/code&gt; for Amazon Relational Database Service&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Storage Gateway&lt;/code&gt; for Storage Gateway&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;S3&lt;/code&gt; for Amazon S3&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;VirtualMachine&lt;/code&gt; for virtual machines&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_type: str
    :param account_id: &lt;p&gt;The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.&lt;/p&gt; &lt;p&gt;If used from an Organizations management account, passing &lt;code&gt;*&lt;/code&gt; returns all jobs across the organization.&lt;/p&gt;
    :type account_id: str
    :param complete_after: Returns only backup jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).
    :type complete_after: str
    :param complete_before: Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).
    :type complete_before: str
    :param parent_job_id: This is a filter to list child (nested) jobs based on parent job ID.
    :type parent_job_id: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    complete_after = util.deserialize_datetime(complete_after)
    complete_before = util.deserialize_datetime(complete_before)
    return web.Response(status=200)


async def list_backup_plan_templates(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_backup_plan_templates

    Returns metadata of your saved backup plan templates, including the template ID, name, and the creation and deletion dates.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_backup_plan_versions(request: web.Request, backup_plan_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_backup_plan_versions

    Returns version metadata of your backup plans, including Amazon Resource Names (ARNs), backup plan IDs, creation and deletion dates, plan names, and version IDs.

    :param backup_plan_id: Uniquely identifies a backup plan.
    :type backup_plan_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_backup_plans(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, include_deleted=None, max_results2=None, next_token2=None) -> web.Response:
    """list_backup_plans

    Returns a list of all active backup plans for an authenticated account. The list contains information such as Amazon Resource Names (ARNs), plan IDs, creation and deletion dates, version IDs, plan names, and creator request IDs.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param include_deleted: A Boolean value with a default value of &lt;code&gt;FALSE&lt;/code&gt; that returns deleted backup plans when set to &lt;code&gt;TRUE&lt;/code&gt;.
    :type include_deleted: bool
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_backup_selections(request: web.Request, backup_plan_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_backup_selections

    Returns an array containing metadata of the resources associated with the target backup plan.

    :param backup_plan_id: Uniquely identifies a backup plan.
    :type backup_plan_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_backup_vaults(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_backup_vaults

    Returns a list of recovery point storage containers along with information about them.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_copy_jobs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, resource_arn=None, state=None, created_before=None, created_after=None, resource_type=None, destination_vault_arn=None, account_id=None, complete_before=None, complete_after=None, parent_job_id=None, max_results2=None, next_token2=None) -> web.Response:
    """list_copy_jobs

    Returns metadata about your copy jobs.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return maxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token. 
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param resource_arn: Returns only copy jobs that match the specified resource Amazon Resource Name (ARN). 
    :type resource_arn: str
    :param state: Returns only copy jobs that are in the specified state.
    :type state: str
    :param created_before: Returns only copy jobs that were created before the specified date.
    :type created_before: str
    :param created_after: Returns only copy jobs that were created after the specified date.
    :type created_after: str
    :param resource_type: &lt;p&gt;Returns only backup jobs for the specified resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Aurora&lt;/code&gt; for Amazon Aurora&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DocumentDB&lt;/code&gt; for Amazon DocumentDB (with MongoDB compatibility)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DynamoDB&lt;/code&gt; for Amazon DynamoDB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EBS&lt;/code&gt; for Amazon Elastic Block Store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EC2&lt;/code&gt; for Amazon Elastic Compute Cloud&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EFS&lt;/code&gt; for Amazon Elastic File System&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FSx&lt;/code&gt; for Amazon FSx&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Neptune&lt;/code&gt; for Amazon Neptune&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RDS&lt;/code&gt; for Amazon Relational Database Service&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Storage Gateway&lt;/code&gt; for Storage Gateway&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;S3&lt;/code&gt; for Amazon S3&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;VirtualMachine&lt;/code&gt; for virtual machines&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_type: str
    :param destination_vault_arn: An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:vault:aBackupVault&lt;/code&gt;. 
    :type destination_vault_arn: str
    :param account_id: The account ID to list the jobs from. Returns only copy jobs associated with the specified account ID.
    :type account_id: str
    :param complete_before: Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).
    :type complete_before: str
    :param complete_after: Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).
    :type complete_after: str
    :param parent_job_id: This is a filter to list child (nested) jobs based on parent job ID.
    :type parent_job_id: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    complete_before = util.deserialize_datetime(complete_before)
    complete_after = util.deserialize_datetime(complete_after)
    return web.Response(status=200)


async def list_frameworks(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_frameworks

    Returns a list of all frameworks for an Amazon Web Services account and Amazon Web Services Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
    :type max_results: int
    :param next_token: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_legal_holds(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_legal_holds

    This action returns metadata about active and previous legal holds.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned resources. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of resources, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of resource list items to be returned.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_protected_resources(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_protected_resources

    Returns an array of resources successfully backed up by Backup, including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_recovery_points_by_backup_vault(request: web.Request, backup_vault_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, resource_arn=None, resource_type=None, backup_plan_id=None, created_before=None, created_after=None, parent_recovery_point_arn=None, max_results2=None, next_token2=None) -> web.Response:
    """list_recovery_points_by_backup_vault

    Returns detailed information about the recovery points stored in a backup vault.

    :param backup_vault_name: &lt;p&gt;The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Backup vault name might not be available when a supported service creates the backup.&lt;/p&gt; &lt;/note&gt;
    :type backup_vault_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param resource_arn: Returns only recovery points that match the specified resource Amazon Resource Name (ARN).
    :type resource_arn: str
    :param resource_type: Returns only recovery points that match the specified resource type.
    :type resource_type: str
    :param backup_plan_id: Returns only recovery points that match the specified backup plan ID.
    :type backup_plan_id: str
    :param created_before: Returns only recovery points that were created before the specified timestamp.
    :type created_before: str
    :param created_after: Returns only recovery points that were created after the specified timestamp.
    :type created_after: str
    :param parent_recovery_point_arn: This returns only recovery points that match the specified parent (composite) recovery point Amazon Resource Name (ARN).
    :type parent_recovery_point_arn: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    return web.Response(status=200)


async def list_recovery_points_by_legal_hold(request: web.Request, legal_hold_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_recovery_points_by_legal_hold

    This action returns recovery point ARNs (Amazon Resource Names) of the specified legal hold.

    :param legal_hold_id: This is the ID of the legal hold.
    :type legal_hold_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: This is the next item following a partial list of returned resources. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of resources, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: This is the maximum number of resource list items to be returned.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_recovery_points_by_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_recovery_points_by_resource

    &lt;p&gt;Returns detailed information about all the recovery points of the type specified by a resource Amazon Resource Name (ARN).&lt;/p&gt; &lt;note&gt; &lt;p&gt;For Amazon EFS and Amazon EC2, this action only lists recovery points created by Backup.&lt;/p&gt; &lt;/note&gt;

    :param resource_arn: An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
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
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of items to be returned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon RDS requires a value of at least 20.&lt;/p&gt; &lt;/note&gt;
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_report_jobs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, report_plan_name=None, creation_before=None, creation_after=None, status=None, max_results=None, next_token=None) -> web.Response:
    """list_report_jobs

    Returns details about your report jobs.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param report_plan_name: Returns only report jobs with the specified report plan name.
    :type report_plan_name: str
    :param creation_before: Returns only report jobs that were created before the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.
    :type creation_before: str
    :param creation_after: Returns only report jobs that were created after the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.
    :type creation_after: str
    :param status: &lt;p&gt;Returns only report jobs that are in the specified status. The statuses are:&lt;/p&gt; &lt;p&gt; &lt;code&gt;CREATED | RUNNING | COMPLETED | FAILED&lt;/code&gt; &lt;/p&gt;
    :type status: str
    :param max_results: The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
    :type max_results: int
    :param next_token: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
    :type next_token: str

    """
    creation_before = util.deserialize_datetime(creation_before)
    creation_after = util.deserialize_datetime(creation_after)
    return web.Response(status=200)


async def list_report_plans(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_report_plans

    Returns a list of your report plans. For detailed information about a single report plan, use &lt;code&gt;DescribeReportPlan&lt;/code&gt;.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
    :type max_results: int
    :param next_token: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_restore_jobs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, account_id=None, created_before=None, created_after=None, status=None, complete_before=None, complete_after=None, max_results2=None, next_token2=None) -> web.Response:
    """list_restore_jobs

    Returns a list of jobs that Backup initiated to restore a saved resource, including details about the recovery process.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The next item following a partial list of returned items. For example, if a request is made to return &lt;code&gt;maxResults&lt;/code&gt; number of items, &lt;code&gt;NextToken&lt;/code&gt; allows you to return more items in your list starting at the location pointed to by the next token.
    :type next_token: str
    :param max_results: The maximum number of items to be returned.
    :type max_results: int
    :param account_id: The account ID to list the jobs from. Returns only restore jobs associated with the specified account ID.
    :type account_id: str
    :param created_before: Returns only restore jobs that were created before the specified date.
    :type created_before: str
    :param created_after: Returns only restore jobs that were created after the specified date.
    :type created_after: str
    :param status: Returns only restore jobs associated with the specified job status.
    :type status: str
    :param complete_before: Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).
    :type complete_before: str
    :param complete_after: Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).
    :type complete_after: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    complete_before = util.deserialize_datetime(complete_before)
    complete_after = util.deserialize_datetime(complete_after)
    return web.Response(status=200)


async def put_backup_vault_access_policy(request: web.Request, backup_vault_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_backup_vault_access_policy

    Sets a resource-based policy that is used to manage access permissions on the target backup vault. Requires a backup vault name and an access policy document in JSON format.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutBackupVaultAccessPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_backup_vault_lock_configuration(request: web.Request, backup_vault_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_backup_vault_lock_configuration

    &lt;p&gt;Applies Backup Vault Lock to a backup vault, preventing attempts to delete any recovery point stored in or created in a backup vault. Vault Lock also prevents attempts to update the lifecycle policy that controls the retention period of any recovery point currently stored in a backup vault. If specified, Vault Lock enforces a minimum and maximum retention period for future backup and copy jobs that target a backup vault.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Backup Vault Lock has been assessed by Cohasset Associates for use in environments that are subject to SEC 17a-4, CFTC, and FINRA regulations. For more information about how Backup Vault Lock relates to these regulations, see the &lt;a href&#x3D;\&quot;samples/cohassetreport.zip\&quot;&gt;Cohasset Associates Compliance Assessment.&lt;/a&gt; &lt;/p&gt; &lt;/note&gt;

    :param backup_vault_name: The Backup Vault Lock configuration that specifies the name of the backup vault it protects.
    :type backup_vault_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutBackupVaultLockConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_backup_vault_notifications(request: web.Request, backup_vault_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_backup_vault_notifications

    Turns on notifications on a backup vault for the specified topic and events.

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutBackupVaultNotificationsRequest.from_dict(body)
    return web.Response(status=200)


async def start_backup_job(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_backup_job

    Starts an on-demand backup job for the specified resource.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = StartBackupJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_copy_job(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_copy_job

    &lt;p&gt;Starts a job to create a one-time copy of the specified resource.&lt;/p&gt; &lt;p&gt;Does not support continuous backups.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = StartCopyJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_report_job(request: web.Request, report_plan_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_report_job

    Starts an on-demand report job for the specified report plan.

    :param report_plan_name: The unique name of a report plan.
    :type report_plan_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = StartReportJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_restore_job(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_restore_job

    Recovers the saved resource identified by an Amazon Resource Name (ARN).

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = StartRestoreJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_backup_job(request: web.Request, backup_job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_backup_job

    &lt;p&gt;Attempts to cancel a job to create a one-time backup of a resource.&lt;/p&gt; &lt;p&gt;This action is not supported for the following services: Amazon FSx for Windows File Server, Amazon FSx for Lustre, FSx for ONTAP , Amazon FSx for OpenZFS, Amazon DocumentDB (with MongoDB compatibility), Amazon RDS, Amazon Aurora, and Amazon Neptune.&lt;/p&gt;

    :param backup_job_id: Uniquely identifies a request to Backup to back up a resource.
    :type backup_job_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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

    Assigns a set of key-value pairs to a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN).

    :param resource_arn: An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.
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


async def untag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes a set of key-value pairs from a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN)

    :param resource_arn: An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_framework(request: web.Request, framework_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_framework

    Updates an existing framework identified by its &lt;code&gt;FrameworkName&lt;/code&gt; with the input document in JSON format.

    :param framework_name: The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
    :type framework_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateFrameworkRequest.from_dict(body)
    return web.Response(status=200)


async def update_global_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_global_settings

    Updates whether the Amazon Web Services account is opted in to cross-account backup. Returns an error if the account is not an Organizations management account. Use the &lt;code&gt;DescribeGlobalSettings&lt;/code&gt; API to determine the current settings.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateGlobalSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_recovery_point_lifecycle(request: web.Request, backup_vault_name, recovery_point_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_recovery_point_lifecycle

    &lt;p&gt;Sets the transition lifecycle of a recovery point.&lt;/p&gt; &lt;p&gt;The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.&lt;/p&gt; &lt;p&gt;Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.&lt;/p&gt; &lt;p&gt;Resource types that are able to be transitioned to cold storage are listed in the \&quot;Lifecycle to cold storage\&quot; section of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource\&quot;&gt; Feature availability by resource&lt;/a&gt; table. Backup ignores this expression for other resource types.&lt;/p&gt; &lt;p&gt;This operation does not support continuous backups.&lt;/p&gt;

    :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.
    :type backup_vault_name: str
    :param recovery_point_arn: An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45&lt;/code&gt;.
    :type recovery_point_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateRecoveryPointLifecycleRequest.from_dict(body)
    return web.Response(status=200)


async def update_region_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_region_settings

    Updates the current service opt-in settings for the Region. If service-opt-in is enabled for a service, Backup tries to protect that service&#39;s resources in this Region, when the resource is included in an on-demand backup or scheduled backup plan. Otherwise, Backup does not try to protect that service&#39;s resources in this Region. Use the &lt;code&gt;DescribeRegionSettings&lt;/code&gt; API to determine the resource types that are supported.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateRegionSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_report_plan(request: web.Request, report_plan_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_report_plan

    Updates an existing report plan identified by its &lt;code&gt;ReportPlanName&lt;/code&gt; with the input document in JSON format.

    :param report_plan_name: The unique name of the report plan. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
    :type report_plan_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateReportPlanRequest.from_dict(body)
    return web.Response(status=200)
