from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_source_identifier_to_subscription_message import AddSourceIdentifierToSubscriptionMessage
from openapi_server.models.add_source_identifier_to_subscription_result import AddSourceIdentifierToSubscriptionResult
from openapi_server.models.add_tags_to_resource_message import AddTagsToResourceMessage
from openapi_server.models.apply_pending_maintenance_action_message import ApplyPendingMaintenanceActionMessage
from openapi_server.models.apply_pending_maintenance_action_result import ApplyPendingMaintenanceActionResult
from openapi_server.models.certificate_message import CertificateMessage
from openapi_server.models.copy_db_cluster_parameter_group_message import CopyDBClusterParameterGroupMessage
from openapi_server.models.copy_db_cluster_parameter_group_result import CopyDBClusterParameterGroupResult
from openapi_server.models.copy_db_cluster_snapshot_message import CopyDBClusterSnapshotMessage
from openapi_server.models.copy_db_cluster_snapshot_result import CopyDBClusterSnapshotResult
from openapi_server.models.create_db_cluster_message import CreateDBClusterMessage
from openapi_server.models.create_db_cluster_parameter_group_message import CreateDBClusterParameterGroupMessage
from openapi_server.models.create_db_cluster_parameter_group_result import CreateDBClusterParameterGroupResult
from openapi_server.models.create_db_cluster_result import CreateDBClusterResult
from openapi_server.models.create_db_cluster_snapshot_message import CreateDBClusterSnapshotMessage
from openapi_server.models.create_db_cluster_snapshot_result import CreateDBClusterSnapshotResult
from openapi_server.models.create_db_instance_message import CreateDBInstanceMessage
from openapi_server.models.create_db_instance_result import CreateDBInstanceResult
from openapi_server.models.create_db_subnet_group_message import CreateDBSubnetGroupMessage
from openapi_server.models.create_db_subnet_group_result import CreateDBSubnetGroupResult
from openapi_server.models.create_event_subscription_message import CreateEventSubscriptionMessage
from openapi_server.models.create_event_subscription_result import CreateEventSubscriptionResult
from openapi_server.models.create_global_cluster_message import CreateGlobalClusterMessage
from openapi_server.models.create_global_cluster_result import CreateGlobalClusterResult
from openapi_server.models.db_cluster_message import DBClusterMessage
from openapi_server.models.db_cluster_parameter_group_details import DBClusterParameterGroupDetails
from openapi_server.models.db_cluster_parameter_group_name_message import DBClusterParameterGroupNameMessage
from openapi_server.models.db_cluster_parameter_groups_message import DBClusterParameterGroupsMessage
from openapi_server.models.db_cluster_snapshot_message import DBClusterSnapshotMessage
from openapi_server.models.db_engine_version_message import DBEngineVersionMessage
from openapi_server.models.db_instance_message import DBInstanceMessage
from openapi_server.models.db_subnet_group_message import DBSubnetGroupMessage
from openapi_server.models.delete_db_cluster_message import DeleteDBClusterMessage
from openapi_server.models.delete_db_cluster_parameter_group_message import DeleteDBClusterParameterGroupMessage
from openapi_server.models.delete_db_cluster_result import DeleteDBClusterResult
from openapi_server.models.delete_db_cluster_snapshot_message import DeleteDBClusterSnapshotMessage
from openapi_server.models.delete_db_cluster_snapshot_result import DeleteDBClusterSnapshotResult
from openapi_server.models.delete_db_instance_message import DeleteDBInstanceMessage
from openapi_server.models.delete_db_instance_result import DeleteDBInstanceResult
from openapi_server.models.delete_db_subnet_group_message import DeleteDBSubnetGroupMessage
from openapi_server.models.delete_event_subscription_message import DeleteEventSubscriptionMessage
from openapi_server.models.delete_event_subscription_result import DeleteEventSubscriptionResult
from openapi_server.models.delete_global_cluster_message import DeleteGlobalClusterMessage
from openapi_server.models.delete_global_cluster_result import DeleteGlobalClusterResult
from openapi_server.models.describe_certificates_message import DescribeCertificatesMessage
from openapi_server.models.describe_db_cluster_parameter_groups_message import DescribeDBClusterParameterGroupsMessage
from openapi_server.models.describe_db_cluster_parameters_message import DescribeDBClusterParametersMessage
from openapi_server.models.describe_db_cluster_snapshot_attributes_message import DescribeDBClusterSnapshotAttributesMessage
from openapi_server.models.describe_db_cluster_snapshot_attributes_result import DescribeDBClusterSnapshotAttributesResult
from openapi_server.models.describe_db_cluster_snapshots_message import DescribeDBClusterSnapshotsMessage
from openapi_server.models.describe_db_clusters_message import DescribeDBClustersMessage
from openapi_server.models.describe_db_engine_versions_message import DescribeDBEngineVersionsMessage
from openapi_server.models.describe_db_instances_message import DescribeDBInstancesMessage
from openapi_server.models.describe_db_subnet_groups_message import DescribeDBSubnetGroupsMessage
from openapi_server.models.describe_engine_default_cluster_parameters_message import DescribeEngineDefaultClusterParametersMessage
from openapi_server.models.describe_engine_default_cluster_parameters_result import DescribeEngineDefaultClusterParametersResult
from openapi_server.models.describe_event_categories_message import DescribeEventCategoriesMessage
from openapi_server.models.describe_event_subscriptions_message import DescribeEventSubscriptionsMessage
from openapi_server.models.describe_events_message import DescribeEventsMessage
from openapi_server.models.describe_global_clusters_message import DescribeGlobalClustersMessage
from openapi_server.models.describe_orderable_db_instance_options_message import DescribeOrderableDBInstanceOptionsMessage
from openapi_server.models.describe_pending_maintenance_actions_message import DescribePendingMaintenanceActionsMessage
from openapi_server.models.event_categories_message import EventCategoriesMessage
from openapi_server.models.event_subscriptions_message import EventSubscriptionsMessage
from openapi_server.models.events_message import EventsMessage
from openapi_server.models.failover_db_cluster_message import FailoverDBClusterMessage
from openapi_server.models.failover_db_cluster_result import FailoverDBClusterResult
from openapi_server.models.get_add_tags_to_resource_tags_parameter_inner import GETAddTagsToResourceTagsParameterInner
from openapi_server.models.get_describe_certificates_filters_parameter_inner import GETDescribeCertificatesFiltersParameterInner
from openapi_server.models.get_modify_db_cluster_cloudwatch_logs_export_configuration_parameter import GETModifyDBClusterCloudwatchLogsExportConfigurationParameter
from openapi_server.models.get_modify_db_cluster_parameter_group_parameters_parameter_inner import GETModifyDBClusterParameterGroupParametersParameterInner
from openapi_server.models.global_clusters_message import GlobalClustersMessage
from openapi_server.models.list_tags_for_resource_message import ListTagsForResourceMessage
from openapi_server.models.modify_db_cluster_message import ModifyDBClusterMessage
from openapi_server.models.modify_db_cluster_parameter_group_message import ModifyDBClusterParameterGroupMessage
from openapi_server.models.modify_db_cluster_result import ModifyDBClusterResult
from openapi_server.models.modify_db_cluster_snapshot_attribute_message import ModifyDBClusterSnapshotAttributeMessage
from openapi_server.models.modify_db_cluster_snapshot_attribute_result import ModifyDBClusterSnapshotAttributeResult
from openapi_server.models.modify_db_instance_message import ModifyDBInstanceMessage
from openapi_server.models.modify_db_instance_result import ModifyDBInstanceResult
from openapi_server.models.modify_db_subnet_group_message import ModifyDBSubnetGroupMessage
from openapi_server.models.modify_db_subnet_group_result import ModifyDBSubnetGroupResult
from openapi_server.models.modify_event_subscription_message import ModifyEventSubscriptionMessage
from openapi_server.models.modify_event_subscription_result import ModifyEventSubscriptionResult
from openapi_server.models.modify_global_cluster_message import ModifyGlobalClusterMessage
from openapi_server.models.modify_global_cluster_result import ModifyGlobalClusterResult
from openapi_server.models.orderable_db_instance_options_message import OrderableDBInstanceOptionsMessage
from openapi_server.models.pending_maintenance_actions_message import PendingMaintenanceActionsMessage
from openapi_server.models.reboot_db_instance_message import RebootDBInstanceMessage
from openapi_server.models.reboot_db_instance_result import RebootDBInstanceResult
from openapi_server.models.remove_from_global_cluster_message import RemoveFromGlobalClusterMessage
from openapi_server.models.remove_from_global_cluster_result import RemoveFromGlobalClusterResult
from openapi_server.models.remove_source_identifier_from_subscription_message import RemoveSourceIdentifierFromSubscriptionMessage
from openapi_server.models.remove_source_identifier_from_subscription_result import RemoveSourceIdentifierFromSubscriptionResult
from openapi_server.models.remove_tags_from_resource_message import RemoveTagsFromResourceMessage
from openapi_server.models.reset_db_cluster_parameter_group_message import ResetDBClusterParameterGroupMessage
from openapi_server.models.restore_db_cluster_from_snapshot_message import RestoreDBClusterFromSnapshotMessage
from openapi_server.models.restore_db_cluster_from_snapshot_result import RestoreDBClusterFromSnapshotResult
from openapi_server.models.restore_db_cluster_to_point_in_time_message import RestoreDBClusterToPointInTimeMessage
from openapi_server.models.restore_db_cluster_to_point_in_time_result import RestoreDBClusterToPointInTimeResult
from openapi_server.models.start_db_cluster_message import StartDBClusterMessage
from openapi_server.models.start_db_cluster_result import StartDBClusterResult
from openapi_server.models.stop_db_cluster_message import StopDBClusterMessage
from openapi_server.models.stop_db_cluster_result import StopDBClusterResult
from openapi_server.models.tag_list_message import TagListMessage
from openapi_server import util


async def g_et_add_source_identifier_to_subscription(request: web.Request, subscription_name, source_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_source_identifier_to_subscription

    Adds a source identifier to an existing event notification subscription.

    :param subscription_name: The name of the Amazon DocumentDB event notification subscription that you want to add a source identifier to.
    :type subscription_name: str
    :param source_identifier: &lt;p&gt;The identifier of the event source to be added:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the source type is an instance, a &lt;code&gt;DBInstanceIdentifier&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a security group, a &lt;code&gt;DBSecurityGroupName&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a parameter group, a &lt;code&gt;DBParameterGroupName&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a snapshot, a &lt;code&gt;DBSnapshotIdentifier&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_identifier: str
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


async def g_et_add_tags_to_resource(request: web.Request, resource_name, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_tags_to_resource

    Adds metadata tags to an Amazon DocumentDB resource. You can use these tags with cost allocation reporting to track costs that are associated with Amazon DocumentDB resources or in a &lt;code&gt;Condition&lt;/code&gt; statement in an Identity and Access Management (IAM) policy for Amazon DocumentDB.

    :param resource_name: The Amazon DocumentDB resource that the tags are added to. This value is an Amazon Resource Name .
    :type resource_name: str
    :param tags: The tags to be assigned to the Amazon DocumentDB resource.
    :type tags: list | bytes
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
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_apply_pending_maintenance_action(request: web.Request, resource_identifier, apply_action, opt_in_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_apply_pending_maintenance_action

    Applies a pending maintenance action to a resource (for example, to an Amazon DocumentDB instance).

    :param resource_identifier: The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to.
    :type resource_identifier: str
    :param apply_action: &lt;p&gt;The pending maintenance action to apply to this resource.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;system-update&lt;/code&gt;, &lt;code&gt;db-upgrade&lt;/code&gt; &lt;/p&gt;
    :type apply_action: str
    :param opt_in_type: &lt;p&gt;A value that specifies the type of opt-in request or undoes an opt-in request. An opt-in request of type &lt;code&gt;immediate&lt;/code&gt; can&#39;t be undone.&lt;/p&gt; &lt;p&gt;Valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;immediate&lt;/code&gt; - Apply the maintenance action immediately.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;next-maintenance&lt;/code&gt; - Apply the maintenance action during the next maintenance window for the resource. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;undo-opt-in&lt;/code&gt; - Cancel any existing &lt;code&gt;next-maintenance&lt;/code&gt; opt-in requests.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type opt_in_type: str
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


async def g_et_copy_db_cluster_parameter_group(request: web.Request, source_db_cluster_parameter_group_identifier, target_db_cluster_parameter_group_identifier, target_db_cluster_parameter_group_description, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_copy_db_cluster_parameter_group

    Copies the specified cluster parameter group.

    :param source_db_cluster_parameter_group_identifier: &lt;p&gt;The identifier or Amazon Resource Name (ARN) for the source cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must specify a valid cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source cluster parameter group is in the same Amazon Web Services Region as the copy, specify a valid parameter group identifier; for example, &lt;code&gt;my-db-cluster-param-group&lt;/code&gt;, or a valid ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source parameter group is in a different Amazon Web Services Region than the copy, specify a valid cluster parameter group ARN; for example, &lt;code&gt;arn:aws:rds:us-east-1:123456789012:sample-cluster:sample-parameter-group&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_db_cluster_parameter_group_identifier: str
    :param target_db_cluster_parameter_group_identifier: &lt;p&gt;The identifier for the copied cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cannot be null, empty, or blank.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 255 letters, numbers, or hyphens. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster-param-group1&lt;/code&gt; &lt;/p&gt;
    :type target_db_cluster_parameter_group_identifier: str
    :param target_db_cluster_parameter_group_description: A description for the copied cluster parameter group.
    :type target_db_cluster_parameter_group_description: str
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
    :param tags: The tags that are to be assigned to the parameter group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_copy_db_cluster_snapshot(request: web.Request, source_db_cluster_snapshot_identifier, target_db_cluster_snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, kms_key_id=None, pre_signed_url=None, copy_tags=None, tags=None) -> web.Response:
    """g_et_copy_db_cluster_snapshot

    &lt;p&gt;Copies a snapshot of a cluster.&lt;/p&gt; &lt;p&gt;To copy a cluster snapshot from a shared manual cluster snapshot, &lt;code&gt;SourceDBClusterSnapshotIdentifier&lt;/code&gt; must be the Amazon Resource Name (ARN) of the shared cluster snapshot. You can only copy a shared DB cluster snapshot, whether encrypted or not, in the same Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;To cancel the copy operation after it is in progress, delete the target cluster snapshot identified by &lt;code&gt;TargetDBClusterSnapshotIdentifier&lt;/code&gt; while that cluster snapshot is in the &lt;i&gt;copying&lt;/i&gt; status.&lt;/p&gt;

    :param source_db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the cluster snapshot to copy. This parameter is not case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must specify a valid system snapshot in the &lt;i&gt;available&lt;/i&gt; state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source snapshot is in the same Amazon Web Services Region as the copy, specify a valid snapshot identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source snapshot is in a different Amazon Web Services Region than the copy, specify a valid cluster snapshot ARN.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster-snapshot1&lt;/code&gt; &lt;/p&gt;
    :type source_db_cluster_snapshot_identifier: str
    :param target_db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the new cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster-snapshot2&lt;/code&gt; &lt;/p&gt;
    :type target_db_cluster_snapshot_identifier: str
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
    :param kms_key_id: &lt;p&gt;The KMS key ID for an encrypted cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key. &lt;/p&gt; &lt;p&gt;If you copy an encrypted cluster snapshot from your Amazon Web Services account, you can specify a value for &lt;code&gt;KmsKeyId&lt;/code&gt; to encrypt the copy with a new KMS encryption key. If you don&#39;t specify a value for &lt;code&gt;KmsKeyId&lt;/code&gt;, then the copy of the cluster snapshot is encrypted with the same KMS key as the source cluster snapshot.&lt;/p&gt; &lt;p&gt;If you copy an encrypted cluster snapshot that is shared from another Amazon Web Services account, then you must specify a value for &lt;code&gt;KmsKeyId&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To copy an encrypted cluster snapshot to another Amazon Web Services Region, set &lt;code&gt;KmsKeyId&lt;/code&gt; to the KMS key ID that you want to use to encrypt the copy of the cluster snapshot in the destination Region. KMS encryption keys are specific to the Amazon Web Services Region that they are created in, and you can&#39;t use encryption keys from one Amazon Web Services Region in another Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;If you copy an unencrypted cluster snapshot and specify a value for the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter, an error is returned.&lt;/p&gt;
    :type kms_key_id: str
    :param pre_signed_url: &lt;p&gt;The URL that contains a Signature Version 4 signed request for the&lt;code&gt;CopyDBClusterSnapshot&lt;/code&gt; API action in the Amazon Web Services Region that contains the source cluster snapshot to copy. You must use the &lt;code&gt;PreSignedUrl&lt;/code&gt; parameter when copying a cluster snapshot from another Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;If you are using an Amazon Web Services SDK tool or the CLI, you can specify &lt;code&gt;SourceRegion&lt;/code&gt; (or &lt;code&gt;--source-region&lt;/code&gt; for the CLI) instead of specifying &lt;code&gt;PreSignedUrl&lt;/code&gt; manually. Specifying &lt;code&gt;SourceRegion&lt;/code&gt; autogenerates a pre-signed URL that is a valid request for the operation that can be executed in the source Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;The presigned URL must be a valid request for the &lt;code&gt;CopyDBClusterSnapshot&lt;/code&gt; API action that can be executed in the source Amazon Web Services Region that contains the cluster snapshot to be copied. The presigned URL request must contain the following parameter values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SourceRegion&lt;/code&gt; - The ID of the region that contains the snapshot to be copied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SourceDBClusterSnapshotIdentifier&lt;/code&gt; - The identifier for the the encrypted cluster snapshot to be copied. This identifier must be in the Amazon Resource Name (ARN) format for the source Amazon Web Services Region. For example, if you are copying an encrypted cluster snapshot from the us-east-1 Amazon Web Services Region, then your &lt;code&gt;SourceDBClusterSnapshotIdentifier&lt;/code&gt; looks something like the following: &lt;code&gt;arn:aws:rds:us-east-1:12345678012:sample-cluster:sample-cluster-snapshot&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TargetDBClusterSnapshotIdentifier&lt;/code&gt; - The identifier for the new cluster snapshot to be created. This parameter isn&#39;t case sensitive.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type pre_signed_url: str
    :param copy_tags: Set to &lt;code&gt;true&lt;/code&gt; to copy all tags from the source cluster snapshot to the target cluster snapshot, and otherwise &lt;code&gt;false&lt;/code&gt;. The default is &lt;code&gt;false&lt;/code&gt;.
    :type copy_tags: bool
    :param tags: The tags to be assigned to the cluster snapshot.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_cluster(request: web.Request, db_cluster_identifier, engine, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, availability_zones=None, backup_retention_period=None, db_cluster_parameter_group_name=None, vpc_security_group_ids=None, db_subnet_group_name=None, engine_version=None, port=None, master_username=None, master_user_password=None, preferred_backup_window=None, preferred_maintenance_window=None, tags=None, storage_encrypted=None, kms_key_id=None, pre_signed_url=None, enable_cloudwatch_logs_exports=None, deletion_protection=None, global_cluster_identifier=None) -> web.Response:
    """g_et_create_db_cluster

    Creates a new Amazon DocumentDB cluster.

    :param db_cluster_identifier: &lt;p&gt;The cluster identifier. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster&lt;/code&gt; &lt;/p&gt;
    :type db_cluster_identifier: str
    :param engine: &lt;p&gt;The name of the database engine to be used for this cluster.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;docdb&lt;/code&gt; &lt;/p&gt;
    :type engine: str
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
    :param availability_zones: A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.
    :type availability_zones: List[]
    :param backup_retention_period: &lt;p&gt;The number of days for which automated backups are retained. You must specify a minimum value of 1.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be a value from 1 to 35.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type backup_retention_period: int
    :param db_cluster_parameter_group_name: The name of the cluster parameter group to associate with this cluster.
    :type db_cluster_parameter_group_name: str
    :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this cluster. 
    :type vpc_security_group_ids: List[]
    :param db_subnet_group_name: &lt;p&gt;A subnet group to associate with this cluster.&lt;/p&gt; &lt;p&gt;Constraints: Must match the name of an existing &lt;code&gt;DBSubnetGroup&lt;/code&gt;. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param engine_version: The version number of the database engine to use. The &lt;code&gt;--engine-version&lt;/code&gt; will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.
    :type engine_version: str
    :param port: The port number on which the instances in the cluster accept connections.
    :type port: int
    :param master_username: &lt;p&gt;The name of the master user for the cluster.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be from 1 to 63 letters or numbers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be a reserved word for the chosen database engine. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type master_username: str
    :param master_user_password: &lt;p&gt;The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote (\&quot;), or the \&quot;at\&quot; symbol (@).&lt;/p&gt; &lt;p&gt;Constraints: Must contain from 8 to 100 characters.&lt;/p&gt;
    :type master_user_password: str
    :param preferred_backup_window: &lt;p&gt;The daily time range during which automated backups are created if automated backups are enabled using the &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; parameter. &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be in the format &lt;code&gt;hh24:mi-hh24:mi&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not conflict with the preferred maintenance window. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be at least 30 minutes.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type preferred_backup_window: str
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.&lt;/p&gt; &lt;p&gt;Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param tags: The tags to be assigned to the cluster.
    :type tags: list | bytes
    :param storage_encrypted: Specifies whether the cluster is encrypted.
    :type storage_encrypted: bool
    :param kms_key_id: &lt;p&gt;The KMS key identifier for an encrypted cluster.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon Web Services account that owns the KMS encryption key that is used to encrypt the new cluster, you can use the KMS key alias instead of the ARN for the KMS encryption key.&lt;/p&gt; &lt;p&gt;If an encryption key is not specified in &lt;code&gt;KmsKeyId&lt;/code&gt;: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the &lt;code&gt;StorageEncrypted&lt;/code&gt; parameter is &lt;code&gt;true&lt;/code&gt;, Amazon DocumentDB uses your default encryption key. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Regions.&lt;/p&gt;
    :type kms_key_id: str
    :param pre_signed_url: Not currently supported. 
    :type pre_signed_url: str
    :param enable_cloudwatch_logs_exports: A list of log types that need to be enabled for exporting to Amazon CloudWatch Logs. You can enable audit logs or profiler logs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html\&quot;&gt; Auditing Amazon DocumentDB Events&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html\&quot;&gt; Profiling Amazon DocumentDB Operations&lt;/a&gt;. 
    :type enable_cloudwatch_logs_exports: List[str]
    :param deletion_protection: Specifies whether this cluster can be deleted. If &lt;code&gt;DeletionProtection&lt;/code&gt; is enabled, the cluster cannot be deleted unless it is modified and &lt;code&gt;DeletionProtection&lt;/code&gt; is disabled. &lt;code&gt;DeletionProtection&lt;/code&gt; protects clusters from being accidentally deleted.
    :type deletion_protection: bool
    :param global_cluster_identifier: The cluster identifier of the new global cluster.
    :type global_cluster_identifier: str

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_cluster_parameter_group(request: web.Request, db_cluster_parameter_group_name, db_parameter_group_family, description, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_db_cluster_parameter_group

    &lt;p&gt;Creates a new cluster parameter group.&lt;/p&gt; &lt;p&gt;Parameters in a cluster parameter group apply to all of the instances in a cluster.&lt;/p&gt; &lt;p&gt;A cluster parameter group is initially created with the default parameters for the database engine used by instances in the cluster. In Amazon DocumentDB, you cannot make modifications directly to the &lt;code&gt;default.docdb3.6&lt;/code&gt; cluster parameter group. If your Amazon DocumentDB cluster is using the default cluster parameter group and you want to modify a value in it, you must first &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_group-create.html\&quot;&gt; create a new parameter group&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_group-copy.html\&quot;&gt; copy an existing parameter group&lt;/a&gt;, modify it, and then apply the modified parameter group to your cluster. For the new cluster parameter group and associated settings to take effect, you must then reboot the instances in the cluster without failover. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_group-modify.html\&quot;&gt; Modifying Amazon DocumentDB Cluster Parameter Groups&lt;/a&gt;. &lt;/p&gt;

    :param db_cluster_parameter_group_name: &lt;p&gt;The name of the cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must not match the name of an existing &lt;code&gt;DBClusterParameterGroup&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;This value is stored as a lowercase string.&lt;/p&gt; &lt;/note&gt;
    :type db_cluster_parameter_group_name: str
    :param db_parameter_group_family: The cluster parameter group family name.
    :type db_parameter_group_family: str
    :param description: The description for the cluster parameter group.
    :type description: str
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
    :param tags: The tags to be assigned to the cluster parameter group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_cluster_snapshot(request: web.Request, db_cluster_snapshot_identifier, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_db_cluster_snapshot

    Creates a snapshot of a cluster. 

    :param db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the cluster snapshot. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster-snapshot1&lt;/code&gt; &lt;/p&gt;
    :type db_cluster_snapshot_identifier: str
    :param db_cluster_identifier: &lt;p&gt;The identifier of the cluster to create a snapshot for. This parameter is not case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing &lt;code&gt;DBCluster&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster&lt;/code&gt; &lt;/p&gt;
    :type db_cluster_identifier: str
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
    :param tags: The tags to be assigned to the cluster snapshot.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_instance(request: web.Request, db_instance_identifier, db_instance_class, engine, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, availability_zone=None, preferred_maintenance_window=None, auto_minor_version_upgrade=None, tags=None, copy_tags_to_snapshot=None, promotion_tier=None, enable_performance_insights=None, performance_insights_kms_key_id=None) -> web.Response:
    """g_et_create_db_instance

    Creates a new instance.

    :param db_instance_identifier: &lt;p&gt;The instance identifier. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;mydbinstance&lt;/code&gt; &lt;/p&gt;
    :type db_instance_identifier: str
    :param db_instance_class: The compute and memory capacity of the instance; for example, &lt;code&gt;db.r5.large&lt;/code&gt;. 
    :type db_instance_class: str
    :param engine: &lt;p&gt;The name of the database engine to be used for this instance.&lt;/p&gt; &lt;p&gt;Valid value: &lt;code&gt;docdb&lt;/code&gt; &lt;/p&gt;
    :type engine: str
    :param db_cluster_identifier: The identifier of the cluster that the instance will belong to.
    :type db_cluster_identifier: str
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
    :param availability_zone: &lt;p&gt;The Amazon EC2 Availability Zone that the instance is created in. &lt;/p&gt; &lt;p&gt;Default: A random, system-chosen Availability Zone in the endpoint&#39;s Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;us-east-1d&lt;/code&gt; &lt;/p&gt;
    :type availability_zone: str
    :param preferred_maintenance_window: &lt;p&gt;The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt; Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. &lt;/p&gt; &lt;p&gt;Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param auto_minor_version_upgrade: &lt;p&gt;This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type auto_minor_version_upgrade: bool
    :param tags: The tags to be assigned to the instance. You can assign up to 10 tags to an instance.
    :type tags: list | bytes
    :param copy_tags_to_snapshot: A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
    :type copy_tags_to_snapshot: bool
    :param promotion_tier: &lt;p&gt;A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Valid values: 0-15&lt;/p&gt;
    :type promotion_tier: int
    :param enable_performance_insights: A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights.html\&quot;&gt;Using Amazon Performance Insights&lt;/a&gt;.
    :type enable_performance_insights: bool
    :param performance_insights_kms_key_id: &lt;p&gt;The KMS key identifier for encryption of Performance Insights data.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.&lt;/p&gt; &lt;p&gt;If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.&lt;/p&gt;
    :type performance_insights_kms_key_id: str

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_subnet_group(request: web.Request, db_subnet_group_name, db_subnet_group_description, subnet_ids, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_db_subnet_group

    Creates a new subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the Amazon Web Services Region.

    :param db_subnet_group_name: &lt;p&gt;The name for the subnet group. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param db_subnet_group_description: The description for the subnet group.
    :type db_subnet_group_description: str
    :param subnet_ids: The Amazon EC2 subnet IDs for the subnet group.
    :type subnet_ids: List[]
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
    :param tags: The tags to be assigned to the subnet group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_event_subscription(request: web.Request, subscription_name, sns_topic_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_type=None, event_categories=None, source_ids=None, enabled=None, tags=None) -> web.Response:
    """g_et_create_event_subscription

    &lt;p&gt;Creates an Amazon DocumentDB event notification subscription. This action requires a topic Amazon Resource Name (ARN) created by using the Amazon DocumentDB console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the Amazon SNS console.&lt;/p&gt; &lt;p&gt;You can specify the type of source (&lt;code&gt;SourceType&lt;/code&gt;) that you want to be notified of. You can also provide a list of Amazon DocumentDB sources (&lt;code&gt;SourceIds&lt;/code&gt;) that trigger the events, and you can provide a list of event categories (&lt;code&gt;EventCategories&lt;/code&gt;) for events that you want to be notified of. For example, you can specify &lt;code&gt;SourceType &#x3D; db-instance&lt;/code&gt;, &lt;code&gt;SourceIds &#x3D; mydbinstance1, mydbinstance2&lt;/code&gt; and &lt;code&gt;EventCategories &#x3D; Availability, Backup&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you specify both the &lt;code&gt;SourceType&lt;/code&gt; and &lt;code&gt;SourceIds&lt;/code&gt; (such as &lt;code&gt;SourceType &#x3D; db-instance&lt;/code&gt; and &lt;code&gt;SourceIdentifier &#x3D; myDBInstance1&lt;/code&gt;), you are notified of all the &lt;code&gt;db-instance&lt;/code&gt; events for the specified source. If you specify a &lt;code&gt;SourceType&lt;/code&gt; but do not specify a &lt;code&gt;SourceIdentifier&lt;/code&gt;, you receive notice of the events for that source type for all your Amazon DocumentDB sources. If you do not specify either the &lt;code&gt;SourceType&lt;/code&gt; or the &lt;code&gt;SourceIdentifier&lt;/code&gt;, you are notified of events generated from all Amazon DocumentDB sources belonging to your customer account.&lt;/p&gt;

    :param subscription_name: &lt;p&gt;The name of the subscription.&lt;/p&gt; &lt;p&gt;Constraints: The name must be fewer than 255 characters.&lt;/p&gt;
    :type subscription_name: str
    :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic created for event notification. Amazon SNS creates the ARN when you create a topic and subscribe to it.
    :type sns_topic_arn: str
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
    :param source_type: &lt;p&gt;The type of source that is generating the events. For example, if you want to be notified of events generated by an instance, you would set this parameter to &lt;code&gt;db-instance&lt;/code&gt;. If this value is not specified, all events are returned.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;db-instance&lt;/code&gt;, &lt;code&gt;db-cluster&lt;/code&gt;, &lt;code&gt;db-parameter-group&lt;/code&gt;, &lt;code&gt;db-security-group&lt;/code&gt;, &lt;code&gt;db-cluster-snapshot&lt;/code&gt; &lt;/p&gt;
    :type source_type: str
    :param event_categories:  A list of event categories for a &lt;code&gt;SourceType&lt;/code&gt; that you want to subscribe to. 
    :type event_categories: List[]
    :param source_ids: &lt;p&gt;The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can&#39;t end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;SourceIds&lt;/code&gt; are provided, &lt;code&gt;SourceType&lt;/code&gt; must also be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is an instance, a &lt;code&gt;DBInstanceIdentifier&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a security group, a &lt;code&gt;DBSecurityGroupName&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a parameter group, a &lt;code&gt;DBParameterGroupName&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a snapshot, a &lt;code&gt;DBSnapshotIdentifier&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_ids: List[]
    :param enabled:  A Boolean value; set to &lt;code&gt;true&lt;/code&gt; to activate the subscription, set to &lt;code&gt;false&lt;/code&gt; to create the subscription but not active it. 
    :type enabled: bool
    :param tags: The tags to be assigned to the event subscription.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_global_cluster(request: web.Request, global_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_db_cluster_identifier=None, engine=None, engine_version=None, deletion_protection=None, database_name=None, storage_encrypted=None) -> web.Response:
    """g_et_create_global_cluster

    &lt;p&gt;Creates an Amazon DocumentDB global cluster that can span multiple multiple Amazon Web Services Regions. The global cluster contains one primary cluster with read-write capability, and up-to give read-only secondary clusters. Global clusters uses storage-based fast replication across regions with latencies less than one second, using dedicated infrastructure with no impact to your workload’s performance.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;You can create a global cluster that is initially empty, and then add a primary and a secondary to it. Or you can specify an existing cluster during the create operation, and this cluster becomes the primary of the global cluster. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

    :param global_cluster_identifier: The cluster identifier of the new global cluster.
    :type global_cluster_identifier: str
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
    :param source_db_cluster_identifier: The Amazon Resource Name (ARN) to use as the primary cluster of the global cluster. This parameter is optional.
    :type source_db_cluster_identifier: str
    :param engine: The name of the database engine to be used for this cluster.
    :type engine: str
    :param engine_version: The engine version of the global cluster.
    :type engine_version: str
    :param deletion_protection: The deletion protection setting for the new global cluster. The global cluster can&#39;t be deleted when deletion protection is enabled. 
    :type deletion_protection: bool
    :param database_name: The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon DocumentDB will not create a database in the global cluster you are creating.
    :type database_name: str
    :param storage_encrypted: The storage encryption setting for the new global cluster. 
    :type storage_encrypted: bool

    """
    return web.Response(status=200)


async def g_et_delete_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_final_snapshot=None, final_db_snapshot_identifier=None) -> web.Response:
    """g_et_delete_db_cluster

    &lt;p&gt;Deletes a previously provisioned cluster. When you delete a cluster, all automated backups for that cluster are deleted and can&#39;t be recovered. Manual DB cluster snapshots of the specified cluster are not deleted.&lt;/p&gt; &lt;p/&gt;

    :param db_cluster_identifier: &lt;p&gt;The cluster identifier for the cluster to be deleted. This parameter isn&#39;t case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match an existing &lt;code&gt;DBClusterIdentifier&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
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
    :param skip_final_snapshot: &lt;p&gt; Determines whether a final cluster snapshot is created before the cluster is deleted. If &lt;code&gt;true&lt;/code&gt; is specified, no cluster snapshot is created. If &lt;code&gt;false&lt;/code&gt; is specified, a cluster snapshot is created before the DB cluster is deleted. &lt;/p&gt; &lt;note&gt; &lt;p&gt;If &lt;code&gt;SkipFinalSnapshot&lt;/code&gt; is &lt;code&gt;false&lt;/code&gt;, you must specify a &lt;code&gt;FinalDBSnapshotIdentifier&lt;/code&gt; parameter.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type skip_final_snapshot: bool
    :param final_db_snapshot_identifier: &lt;p&gt; The cluster snapshot identifier of the new cluster snapshot created when &lt;code&gt;SkipFinalSnapshot&lt;/code&gt; is set to &lt;code&gt;false&lt;/code&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; Specifying this parameter and also setting the &lt;code&gt;SkipFinalShapshot&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; results in an error. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be from 1 to 255 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type final_db_snapshot_identifier: str

    """
    return web.Response(status=200)


async def g_et_delete_db_cluster_parameter_group(request: web.Request, db_cluster_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_db_cluster_parameter_group

    Deletes a specified cluster parameter group. The cluster parameter group to be deleted can&#39;t be associated with any clusters.

    :param db_cluster_parameter_group_name: &lt;p&gt;The name of the cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be the name of an existing cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t delete a default cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be associated with any clusters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_parameter_group_name: str
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


async def g_et_delete_db_cluster_snapshot(request: web.Request, db_cluster_snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_db_cluster_snapshot

    &lt;p&gt;Deletes a cluster snapshot. If the snapshot is being copied, the copy operation is terminated.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The cluster snapshot must be in the &lt;code&gt;available&lt;/code&gt; state to be deleted.&lt;/p&gt; &lt;/note&gt;

    :param db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the cluster snapshot to delete.&lt;/p&gt; &lt;p&gt;Constraints: Must be the name of an existing cluster snapshot in the &lt;code&gt;available&lt;/code&gt; state.&lt;/p&gt;
    :type db_cluster_snapshot_identifier: str
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


async def g_et_delete_db_instance(request: web.Request, db_instance_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_db_instance

    Deletes a previously provisioned instance.

    :param db_instance_identifier: &lt;p&gt;The instance identifier for the instance to be deleted. This parameter isn&#39;t case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the name of an existing instance.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_instance_identifier: str
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


async def g_et_delete_db_subnet_group(request: web.Request, db_subnet_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_db_subnet_group

    &lt;p&gt;Deletes a subnet group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The specified database subnet group must not be associated with any DB instances.&lt;/p&gt; &lt;/note&gt;

    :param db_subnet_group_name: &lt;p&gt;The name of the database subnet group to delete.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete the default subnet group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;p&gt;Must match the name of an existing &lt;code&gt;DBSubnetGroup&lt;/code&gt;. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
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


async def g_et_delete_event_subscription(request: web.Request, subscription_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_event_subscription

    Deletes an Amazon DocumentDB event notification subscription.

    :param subscription_name: The name of the Amazon DocumentDB event notification subscription that you want to delete.
    :type subscription_name: str
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


async def g_et_delete_global_cluster(request: web.Request, global_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_global_cluster

    &lt;p&gt;Deletes a global cluster. The primary and secondary clusters must already be detached or deleted before attempting to delete a global cluster.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

    :param global_cluster_identifier: The cluster identifier of the global cluster being deleted.
    :type global_cluster_identifier: str
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


async def g_et_describe_certificates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, certificate_identifier=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_certificates

    Returns a list of certificate authority (CA) certificates provided by Amazon DocumentDB for this Amazon Web Services account.

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
    :param certificate_identifier: &lt;p&gt;The user-supplied certificate identifier. If this parameter is specified, information for only the specified certificate is returned. If this parameter is omitted, a list of up to &lt;code&gt;MaxRecords&lt;/code&gt; certificates is returned. This parameter is not case sensitive.&lt;/p&gt; &lt;p&gt;Constraints&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match an existing &lt;code&gt;CertificateIdentifier&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type certificate_identifier: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt;The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Minimum: 20&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum: 100&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeCertificates&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_cluster_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_parameter_group_name=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_cluster_parameter_groups

    Returns a list of &lt;code&gt;DBClusterParameterGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; parameter is specified, the list contains only the description of the specified cluster parameter group. 

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
    :param db_cluster_parameter_group_name: &lt;p&gt;The name of a specific cluster parameter group to return details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If provided, must match the name of an existing &lt;code&gt;DBClusterParameterGroup&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_parameter_group_name: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_cluster_parameters(request: web.Request, db_cluster_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_cluster_parameters

    Returns the detailed parameter list for a particular cluster parameter group.

    :param db_cluster_parameter_group_name: &lt;p&gt;The name of a specific cluster parameter group to return parameter details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If provided, must match the name of an existing &lt;code&gt;DBClusterParameterGroup&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_parameter_group_name: str
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
    :param source:  A value that indicates to return only parameters for a specific source. Parameter sources can be &lt;code&gt;engine&lt;/code&gt;, &lt;code&gt;service&lt;/code&gt;, or &lt;code&gt;customer&lt;/code&gt;. 
    :type source: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_cluster_snapshot_attributes(request: web.Request, db_cluster_snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_db_cluster_snapshot_attributes

    &lt;p&gt;Returns a list of cluster snapshot attribute names and values for a manual DB cluster snapshot.&lt;/p&gt; &lt;p&gt;When you share snapshots with other Amazon Web Services accounts, &lt;code&gt;DescribeDBClusterSnapshotAttributes&lt;/code&gt; returns the &lt;code&gt;restore&lt;/code&gt; attribute and a list of IDs for the Amazon Web Services accounts that are authorized to copy or restore the manual cluster snapshot. If &lt;code&gt;all&lt;/code&gt; is included in the list of values for the &lt;code&gt;restore&lt;/code&gt; attribute, then the manual cluster snapshot is public and can be copied or restored by all Amazon Web Services accounts.&lt;/p&gt;

    :param db_cluster_snapshot_identifier: The identifier for the cluster snapshot to describe the attributes for.
    :type db_cluster_snapshot_identifier: str
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


async def g_et_describe_db_cluster_snapshots(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_identifier=None, db_cluster_snapshot_identifier=None, snapshot_type=None, filters=None, max_records=None, marker=None, include_shared=None, include_public=None) -> web.Response:
    """g_et_describe_db_cluster_snapshots

    Returns information about cluster snapshots. This API operation supports pagination.

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
    :param db_cluster_identifier: &lt;p&gt;The ID of the cluster to retrieve the list of cluster snapshots for. This parameter can&#39;t be used with the &lt;code&gt;DBClusterSnapshotIdentifier&lt;/code&gt; parameter. This parameter is not case sensitive. &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If provided, must match the identifier of an existing &lt;code&gt;DBCluster&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param db_cluster_snapshot_identifier: &lt;p&gt;A specific cluster snapshot identifier to describe. This parameter can&#39;t be used with the &lt;code&gt;DBClusterIdentifier&lt;/code&gt; parameter. This value is stored as a lowercase string. &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If provided, must match the identifier of an existing &lt;code&gt;DBClusterSnapshot&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If this identifier is for an automated snapshot, the &lt;code&gt;SnapshotType&lt;/code&gt; parameter must also be specified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_snapshot_identifier: str
    :param snapshot_type: &lt;p&gt;The type of cluster snapshots to be returned. You can specify one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;automated&lt;/code&gt; - Return all cluster snapshots that Amazon DocumentDB has automatically created for your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;manual&lt;/code&gt; - Return all cluster snapshots that you have manually created for your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;shared&lt;/code&gt; - Return all manual cluster snapshots that have been shared to your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public&lt;/code&gt; - Return all cluster snapshots that have been marked as public.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you don&#39;t specify a &lt;code&gt;SnapshotType&lt;/code&gt; value, then both automated and manual cluster snapshots are returned. You can include shared cluster snapshots with these results by setting the &lt;code&gt;IncludeShared&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;. You can include public cluster snapshots with these results by setting the&lt;code&gt;IncludePublic&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;IncludeShared&lt;/code&gt; and &lt;code&gt;IncludePublic&lt;/code&gt; parameters don&#39;t apply for &lt;code&gt;SnapshotType&lt;/code&gt; values of &lt;code&gt;manual&lt;/code&gt; or &lt;code&gt;automated&lt;/code&gt;. The &lt;code&gt;IncludePublic&lt;/code&gt; parameter doesn&#39;t apply when &lt;code&gt;SnapshotType&lt;/code&gt; is set to &lt;code&gt;shared&lt;/code&gt;. The &lt;code&gt;IncludeShared&lt;/code&gt; parameter doesn&#39;t apply when &lt;code&gt;SnapshotType&lt;/code&gt; is set to &lt;code&gt;public&lt;/code&gt;.&lt;/p&gt;
    :type snapshot_type: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str
    :param include_shared: Set to &lt;code&gt;true&lt;/code&gt; to include shared manual cluster snapshots from other Amazon Web Services accounts that this Amazon Web Services account has been given permission to copy or restore, and otherwise &lt;code&gt;false&lt;/code&gt;. The default is &lt;code&gt;false&lt;/code&gt;.
    :type include_shared: bool
    :param include_public: Set to &lt;code&gt;true&lt;/code&gt; to include manual cluster snapshots that are public and can be copied or restored by any Amazon Web Services account, and otherwise &lt;code&gt;false&lt;/code&gt;. The default is &lt;code&gt;false&lt;/code&gt;.
    :type include_public: bool

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_identifier=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_clusters

    Returns information about provisioned Amazon DocumentDB clusters. This API operation supports pagination. For certain management features such as cluster and instance lifecycle management, Amazon DocumentDB leverages operational technology that is shared with Amazon RDS and Amazon Neptune. Use the &lt;code&gt;filterName&#x3D;engine,Values&#x3D;docdb&lt;/code&gt; filter parameter to return only Amazon DocumentDB clusters.

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
    :param db_cluster_identifier: &lt;p&gt;The user-provided cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn&#39;t case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If provided, must match an existing &lt;code&gt;DBClusterIdentifier&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param filters: &lt;p&gt;A filter that specifies one or more clusters to describe.&lt;/p&gt; &lt;p&gt;Supported filters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-cluster-id&lt;/code&gt; - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list only includes information about the clusters identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_engine_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine=None, engine_version=None, db_parameter_group_family=None, filters=None, max_records=None, marker=None, default_only=None, list_supported_character_sets=None, list_supported_timezones=None) -> web.Response:
    """g_et_describe_db_engine_versions

    Returns a list of the available engines.

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
    :param engine: The database engine to return.
    :type engine: str
    :param engine_version: &lt;p&gt;The database engine version to return.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;3.6.0&lt;/code&gt; &lt;/p&gt;
    :type engine_version: str
    :param db_parameter_group_family: &lt;p&gt;The name of a specific parameter group family to return details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If provided, must match an existing &lt;code&gt;DBParameterGroupFamily&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_family: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str
    :param default_only: Indicates that only the default version of the specified engine or engine and major version combination is returned.
    :type default_only: bool
    :param list_supported_character_sets: If this parameter is specified and the requested engine supports the &lt;code&gt;CharacterSetName&lt;/code&gt; parameter for &lt;code&gt;CreateDBInstance&lt;/code&gt;, the response includes a list of supported character sets for each engine version. 
    :type list_supported_character_sets: bool
    :param list_supported_timezones: If this parameter is specified and the requested engine supports the &lt;code&gt;TimeZone&lt;/code&gt; parameter for &lt;code&gt;CreateDBInstance&lt;/code&gt;, the response includes a list of supported time zones for each engine version. 
    :type list_supported_timezones: bool

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_instance_identifier=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_instances

    Returns information about provisioned Amazon DocumentDB instances. This API supports pagination.

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
    :param db_instance_identifier: &lt;p&gt;The user-provided instance identifier. If this parameter is specified, information from only the specific instance is returned. This parameter isn&#39;t case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If provided, must match the identifier of an existing &lt;code&gt;DBInstance&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_instance_identifier: str
    :param filters: &lt;p&gt;A filter that specifies one or more instances to describe.&lt;/p&gt; &lt;p&gt;Supported filters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-cluster-id&lt;/code&gt; - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only the information about the instances that are associated with the clusters that are identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-instance-id&lt;/code&gt; - Accepts instance identifiers and instance ARNs. The results list includes only the information about the instances that are identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_subnet_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_subnet_group_name=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_subnet_groups

    Returns a list of &lt;code&gt;DBSubnetGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBSubnetGroupName&lt;/code&gt; is specified, the list will contain only the descriptions of the specified &lt;code&gt;DBSubnetGroup&lt;/code&gt;.

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
    :param db_subnet_group_name: The name of the subnet group to return details for.
    :type db_subnet_group_name: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_engine_default_cluster_parameters(request: web.Request, db_parameter_group_family, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_engine_default_cluster_parameters

    Returns the default engine and system parameter information for the cluster database engine.

    :param db_parameter_group_family: The name of the cluster parameter group family to return the engine parameter information for.
    :type db_parameter_group_family: str
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
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_event_categories(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_type=None, filters=None) -> web.Response:
    """g_et_describe_event_categories

    Displays a list of categories for all event source types, or, if specified, for a specified source type. 

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
    :param source_type: &lt;p&gt;The type of source that is generating the events.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;db-instance&lt;/code&gt;, &lt;code&gt;db-parameter-group&lt;/code&gt;, &lt;code&gt;db-security-group&lt;/code&gt; &lt;/p&gt;
    :type source_type: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_event_subscriptions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, subscription_name=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_event_subscriptions

    &lt;p&gt;Lists all the subscription descriptions for a customer account. The description for a subscription includes &lt;code&gt;SubscriptionName&lt;/code&gt;, &lt;code&gt;SNSTopicARN&lt;/code&gt;, &lt;code&gt;CustomerID&lt;/code&gt;, &lt;code&gt;SourceType&lt;/code&gt;, &lt;code&gt;SourceID&lt;/code&gt;, &lt;code&gt;CreationTime&lt;/code&gt;, and &lt;code&gt;Status&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you specify a &lt;code&gt;SubscriptionName&lt;/code&gt;, lists the description for that subscription.&lt;/p&gt;

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
    :param subscription_name: The name of the Amazon DocumentDB event notification subscription that you want to describe.
    :type subscription_name: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_identifier=None, source_type=None, start_time=None, end_time=None, duration=None, event_categories=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_events

    Returns events related to instances, security groups, snapshots, and DB parameter groups for the past 14 days. You can obtain events specific to a particular DB instance, security group, snapshot, or parameter group by providing the name as a parameter. By default, the events of the past hour are returned.

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
    :param source_identifier: &lt;p&gt;The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;SourceIdentifier&lt;/code&gt; is provided, &lt;code&gt;SourceType&lt;/code&gt; must also be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBInstance&lt;/code&gt;, a &lt;code&gt;DBInstanceIdentifier&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBSecurityGroup&lt;/code&gt;, a &lt;code&gt;DBSecurityGroupName&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBParameterGroup&lt;/code&gt;, a &lt;code&gt;DBParameterGroupName&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBSnapshot&lt;/code&gt;, a &lt;code&gt;DBSnapshotIdentifier&lt;/code&gt; must be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_identifier: str
    :param source_type: The event source to retrieve events for. If no value is specified, all events are returned.
    :type source_type: str
    :param start_time: &lt;p&gt; The beginning of the time interval to retrieve events for, specified in ISO 8601 format. &lt;/p&gt; &lt;p&gt;Example: 2009-07-08T18:00Z&lt;/p&gt;
    :type start_time: str
    :param end_time: &lt;p&gt; The end of the time interval for which to retrieve events, specified in ISO 8601 format. &lt;/p&gt; &lt;p&gt;Example: 2009-07-08T18:00Z&lt;/p&gt;
    :type end_time: str
    :param duration: &lt;p&gt;The number of minutes to retrieve events for.&lt;/p&gt; &lt;p&gt;Default: 60&lt;/p&gt;
    :type duration: int
    :param event_categories: A list of event categories that trigger notifications for an event notification subscription.
    :type event_categories: List[]
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_global_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, global_cluster_identifier=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_global_clusters

    &lt;p&gt;Returns information about Amazon DocumentDB global clusters. This API supports pagination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    :param global_cluster_identifier: The user-supplied cluster identifier. If this parameter is specified, information from only the specific cluster is returned. This parameter isn&#39;t case-sensitive.
    :type global_cluster_identifier: str
    :param filters: &lt;p&gt;A filter that specifies one or more global DB clusters to describe.&lt;/p&gt; &lt;p&gt;Supported filters: &lt;code&gt;db-cluster-id&lt;/code&gt; accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list will only include information about the clusters identified by these ARNs.&lt;/p&gt;
    :type filters: list | bytes
    :param max_records: The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that you can retrieve the remaining results. 
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeGlobalClusters&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_orderable_db_instance_options(request: web.Request, engine, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine_version=None, db_instance_class=None, license_model=None, vpc=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_orderable_db_instance_options

    Returns a list of orderable instance options for the specified engine.

    :param engine: The name of the engine to retrieve instance options for.
    :type engine: str
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
    :param engine_version: The engine version filter value. Specify this parameter to show only the available offerings that match the specified engine version.
    :type engine_version: str
    :param db_instance_class: The instance class filter value. Specify this parameter to show only the available offerings that match the specified instance class.
    :type db_instance_class: str
    :param license_model: The license model filter value. Specify this parameter to show only the available offerings that match the specified license model.
    :type license_model: str
    :param vpc: The virtual private cloud (VPC) filter value. Specify this parameter to show only the available VPC or non-VPC offerings.
    :type vpc: bool
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_pending_maintenance_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, resource_identifier=None, filters=None, marker=None, max_records=None) -> web.Response:
    """g_et_describe_pending_maintenance_actions

    Returns a list of resources (for example, instances) that have at least one pending maintenance action.

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
    :param resource_identifier: The ARN of a resource to return pending maintenance actions for.
    :type resource_identifier: str
    :param filters: &lt;p&gt;A filter that specifies one or more resources to return pending maintenance actions for.&lt;/p&gt; &lt;p&gt;Supported filters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-cluster-id&lt;/code&gt; - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only pending maintenance actions for the clusters identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-instance-id&lt;/code&gt; - Accepts instance identifiers and instance ARNs. The results list includes only pending maintenance actions for the DB instances identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type filters: list | bytes
    :param marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_failover_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_identifier=None, target_db_instance_identifier=None) -> web.Response:
    """g_et_failover_db_cluster

    &lt;p&gt;Forces a failover for a cluster.&lt;/p&gt; &lt;p&gt;A failover for a cluster promotes one of the Amazon DocumentDB replicas (read-only instances) in the cluster to be the primary instance (the cluster writer).&lt;/p&gt; &lt;p&gt;If the primary instance fails, Amazon DocumentDB automatically fails over to an Amazon DocumentDB replica, if one exists. You can force a failover when you want to simulate a failure of a primary instance for testing.&lt;/p&gt;

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
    :param db_cluster_identifier: &lt;p&gt;A cluster identifier to force a failover for. This parameter is not case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing &lt;code&gt;DBCluster&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param target_db_instance_identifier: &lt;p&gt;The name of the instance to promote to the primary instance.&lt;/p&gt; &lt;p&gt;You must specify the instance identifier for an Amazon DocumentDB replica in the cluster. For example, &lt;code&gt;mydbcluster-replica1&lt;/code&gt;.&lt;/p&gt;
    :type target_db_instance_identifier: str

    """
    return web.Response(status=200)


async def g_et_list_tags_for_resource(request: web.Request, resource_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None) -> web.Response:
    """g_et_list_tags_for_resource

    Lists all tags on an Amazon DocumentDB resource.

    :param resource_name: The Amazon DocumentDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).
    :type resource_name: str
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
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes

    """
    filters = [GETDescribeCertificatesFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_modify_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, new_db_cluster_identifier=None, apply_immediately=None, backup_retention_period=None, db_cluster_parameter_group_name=None, vpc_security_group_ids=None, port=None, master_user_password=None, preferred_backup_window=None, preferred_maintenance_window=None, cloudwatch_logs_export_configuration=None, engine_version=None, allow_major_version_upgrade=None, deletion_protection=None) -> web.Response:
    """g_et_modify_db_cluster

    Modifies a setting for an Amazon DocumentDB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. 

    :param db_cluster_identifier: &lt;p&gt;The cluster identifier for the cluster that is being modified. This parameter is not case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing &lt;code&gt;DBCluster&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
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
    :param new_db_cluster_identifier: &lt;p&gt;The new cluster identifier for the cluster when renaming a cluster. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster2&lt;/code&gt; &lt;/p&gt;
    :type new_db_cluster_identifier: str
    :param apply_immediately: &lt;p&gt;A value that specifies whether the changes in this request and any pending changes are asynchronously applied as soon as possible, regardless of the &lt;code&gt;PreferredMaintenanceWindow&lt;/code&gt; setting for the cluster. If this parameter is set to &lt;code&gt;false&lt;/code&gt;, changes to the cluster are applied during the next maintenance window.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter affects only the &lt;code&gt;NewDBClusterIdentifier&lt;/code&gt; and &lt;code&gt;MasterUserPassword&lt;/code&gt; values. If you set this parameter value to &lt;code&gt;false&lt;/code&gt;, the changes to the &lt;code&gt;NewDBClusterIdentifier&lt;/code&gt; and &lt;code&gt;MasterUserPassword&lt;/code&gt; values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type apply_immediately: bool
    :param backup_retention_period: &lt;p&gt;The number of days for which automated backups are retained. You must specify a minimum value of 1.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be a value from 1 to 35.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type backup_retention_period: int
    :param db_cluster_parameter_group_name: The name of the cluster parameter group to use for the cluster.
    :type db_cluster_parameter_group_name: str
    :param vpc_security_group_ids: A list of virtual private cloud (VPC) security groups that the cluster will belong to.
    :type vpc_security_group_ids: List[]
    :param port: &lt;p&gt;The port number on which the cluster accepts connections.&lt;/p&gt; &lt;p&gt;Constraints: Must be a value from &lt;code&gt;1150&lt;/code&gt; to &lt;code&gt;65535&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Default: The same port as the original cluster.&lt;/p&gt;
    :type port: int
    :param master_user_password: &lt;p&gt;The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote (\&quot;), or the \&quot;at\&quot; symbol (@).&lt;/p&gt; &lt;p&gt;Constraints: Must contain from 8 to 100 characters.&lt;/p&gt;
    :type master_user_password: str
    :param preferred_backup_window: &lt;p&gt;The daily time range during which automated backups are created if automated backups are enabled, using the &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; parameter. &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be in the format &lt;code&gt;hh24:mi-hh24:mi&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not conflict with the preferred maintenance window.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be at least 30 minutes.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type preferred_backup_window: str
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week. &lt;/p&gt; &lt;p&gt;Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param cloudwatch_logs_export_configuration: The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs for a specific instance or cluster. The &lt;code&gt;EnableLogTypes&lt;/code&gt; and &lt;code&gt;DisableLogTypes&lt;/code&gt; arrays determine which logs are exported (or not exported) to CloudWatch Logs.
    :type cloudwatch_logs_export_configuration: dict | bytes
    :param engine_version: &lt;p&gt;The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless &lt;code&gt;ApplyImmediately&lt;/code&gt; is enabled.&lt;/p&gt; &lt;p&gt;To list all of the available engine versions for Amazon DocumentDB use the following command:&lt;/p&gt; &lt;p&gt; &lt;code&gt;aws docdb describe-db-engine-versions --engine docdb --query \&quot;DBEngineVersions[].EngineVersion\&quot;&lt;/code&gt; &lt;/p&gt;
    :type engine_version: str
    :param allow_major_version_upgrade: &lt;p&gt;A value that indicates whether major version upgrades are allowed.&lt;/p&gt; &lt;p&gt;Constraints: You must allow major version upgrades when specifying a value for the &lt;code&gt;EngineVersion&lt;/code&gt; parameter that is a different major version than the DB cluster&#39;s current version.&lt;/p&gt;
    :type allow_major_version_upgrade: bool
    :param deletion_protection: Specifies whether this cluster can be deleted. If &lt;code&gt;DeletionProtection&lt;/code&gt; is enabled, the cluster cannot be deleted unless it is modified and &lt;code&gt;DeletionProtection&lt;/code&gt; is disabled. &lt;code&gt;DeletionProtection&lt;/code&gt; protects clusters from being accidentally deleted.
    :type deletion_protection: bool

    """
    cloudwatch_logs_export_configuration = .from_dict(cloudwatch_logs_export_configuration)
    return web.Response(status=200)


async def g_et_modify_db_cluster_parameter_group(request: web.Request, db_cluster_parameter_group_name, parameters, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_db_cluster_parameter_group

    &lt;p&gt; Modifies the parameters of a cluster parameter group. To modify more than one parameter, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt;, &lt;code&gt;ParameterValue&lt;/code&gt;, and &lt;code&gt;ApplyMethod&lt;/code&gt;. A maximum of 20 parameters can be modified in a single request. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot or maintenance window before the change can take effect.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;After you create a cluster parameter group, you should wait at least 5 minutes before creating your first cluster that uses that cluster parameter group as the default parameter group. This allows Amazon DocumentDB to fully complete the create action before the parameter group is used as the default for a new cluster. This step is especially important for parameters that are critical when creating the default database for a cluster, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter.&lt;/p&gt; &lt;/important&gt;

    :param db_cluster_parameter_group_name: The name of the cluster parameter group to modify.
    :type db_cluster_parameter_group_name: str
    :param parameters: A list of parameters in the cluster parameter group to modify.
    :type parameters: list | bytes
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
    parameters = [GETModifyDBClusterParameterGroupParametersParameterInner.from_dict(d) for d in parameters]
    return web.Response(status=200)


async def g_et_modify_db_cluster_snapshot_attribute(request: web.Request, db_cluster_snapshot_identifier, attribute_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, values_to_add=None, values_to_remove=None) -> web.Response:
    """g_et_modify_db_cluster_snapshot_attribute

    &lt;p&gt;Adds an attribute and values to, or removes an attribute and values from, a manual cluster snapshot.&lt;/p&gt; &lt;p&gt;To share a manual cluster snapshot with other Amazon Web Services accounts, specify &lt;code&gt;restore&lt;/code&gt; as the &lt;code&gt;AttributeName&lt;/code&gt;, and use the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter to add a list of IDs of the Amazon Web Services accounts that are authorized to restore the manual cluster snapshot. Use the value &lt;code&gt;all&lt;/code&gt; to make the manual cluster snapshot public, which means that it can be copied or restored by all Amazon Web Services accounts. Do not add the &lt;code&gt;all&lt;/code&gt; value for any manual cluster snapshots that contain private information that you don&#39;t want available to all Amazon Web Services accounts. If a manual cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized Amazon Web Services account IDs for the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter. You can&#39;t use &lt;code&gt;all&lt;/code&gt; as a value for that parameter in this case.&lt;/p&gt;

    :param db_cluster_snapshot_identifier: The identifier for the cluster snapshot to modify the attributes for.
    :type db_cluster_snapshot_identifier: str
    :param attribute_name: &lt;p&gt;The name of the cluster snapshot attribute to modify.&lt;/p&gt; &lt;p&gt;To manage authorization for other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this value to &lt;code&gt;restore&lt;/code&gt;.&lt;/p&gt;
    :type attribute_name: str
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
    :param values_to_add: &lt;p&gt;A list of cluster snapshot attributes to add to the attribute specified by &lt;code&gt;AttributeName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To authorize other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this list to include one or more Amazon Web Services account IDs. To make the manual cluster snapshot restorable by any Amazon Web Services account, set it to &lt;code&gt;all&lt;/code&gt;. Do not add the &lt;code&gt;all&lt;/code&gt; value for any manual cluster snapshots that contain private information that you don&#39;t want to be available to all Amazon Web Services accounts.&lt;/p&gt;
    :type values_to_add: List[]
    :param values_to_remove: &lt;p&gt;A list of cluster snapshot attributes to remove from the attribute specified by &lt;code&gt;AttributeName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To remove authorization for other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this list to include one or more Amazon Web Services account identifiers. To remove authorization for any Amazon Web Services account to copy or restore the cluster snapshot, set it to &lt;code&gt;all&lt;/code&gt; . If you specify &lt;code&gt;all&lt;/code&gt;, an Amazon Web Services account whose account ID is explicitly added to the &lt;code&gt;restore&lt;/code&gt; attribute can still copy or restore a manual cluster snapshot.&lt;/p&gt;
    :type values_to_remove: List[]

    """
    return web.Response(status=200)


async def g_et_modify_db_instance(request: web.Request, db_instance_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_instance_class=None, apply_immediately=None, preferred_maintenance_window=None, auto_minor_version_upgrade=None, new_db_instance_identifier=None, ca_certificate_identifier=None, copy_tags_to_snapshot=None, promotion_tier=None, enable_performance_insights=None, performance_insights_kms_key_id=None) -> web.Response:
    """g_et_modify_db_instance

    Modifies settings for an instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.

    :param db_instance_identifier: &lt;p&gt;The instance identifier. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing &lt;code&gt;DBInstance&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_instance_identifier: str
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
    :param db_instance_class: &lt;p&gt;The new compute and memory capacity of the instance; for example, &lt;code&gt;db.r5.large&lt;/code&gt;. Not all instance classes are available in all Amazon Web Services Regions. &lt;/p&gt; &lt;p&gt;If you modify the instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless &lt;code&gt;ApplyImmediately&lt;/code&gt; is specified as &lt;code&gt;true&lt;/code&gt; for this request. &lt;/p&gt; &lt;p&gt;Default: Uses existing setting.&lt;/p&gt;
    :type db_instance_class: str
    :param apply_immediately: &lt;p&gt;Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the &lt;code&gt;PreferredMaintenanceWindow&lt;/code&gt; setting for the instance. &lt;/p&gt; &lt;p&gt; If this parameter is set to &lt;code&gt;false&lt;/code&gt;, changes to the instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next reboot.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type apply_immediately: bool
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn&#39;t result in an outage except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, changing this parameter causes a reboot of the instance. If you are moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure that pending changes are applied.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting.&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun&lt;/p&gt; &lt;p&gt;Constraints: Must be at least 30 minutes.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param auto_minor_version_upgrade: This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.
    :type auto_minor_version_upgrade: bool
    :param new_db_instance_identifier: &lt;p&gt; The new instance identifier for the instance when renaming an instance. When you change the instance identifier, an instance reboot occurs immediately if you set &lt;code&gt;Apply Immediately&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;. It occurs during the next maintenance window if you set &lt;code&gt;Apply Immediately&lt;/code&gt; to &lt;code&gt;false&lt;/code&gt;. This value is stored as a lowercase string. &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;mydbinstance&lt;/code&gt; &lt;/p&gt;
    :type new_db_instance_identifier: str
    :param ca_certificate_identifier: Indicates the certificate that needs to be associated with the instance.
    :type ca_certificate_identifier: str
    :param copy_tags_to_snapshot: A value that indicates whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
    :type copy_tags_to_snapshot: bool
    :param promotion_tier: &lt;p&gt;A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Valid values: 0-15&lt;/p&gt;
    :type promotion_tier: int
    :param enable_performance_insights: A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights.html\&quot;&gt;Using Amazon Performance Insights&lt;/a&gt;.
    :type enable_performance_insights: bool
    :param performance_insights_kms_key_id: &lt;p&gt;The KMS key identifier for encryption of Performance Insights data.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.&lt;/p&gt; &lt;p&gt;If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.&lt;/p&gt;
    :type performance_insights_kms_key_id: str

    """
    return web.Response(status=200)


async def g_et_modify_db_subnet_group(request: web.Request, db_subnet_group_name, subnet_ids, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_subnet_group_description=None) -> web.Response:
    """g_et_modify_db_subnet_group

    Modifies an existing subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the Amazon Web Services Region.

    :param db_subnet_group_name: &lt;p&gt;The name for the subnet group. This value is stored as a lowercase string. You can&#39;t modify the default subnet group. &lt;/p&gt; &lt;p&gt;Constraints: Must match the name of an existing &lt;code&gt;DBSubnetGroup&lt;/code&gt;. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param subnet_ids: The Amazon EC2 subnet IDs for the subnet group.
    :type subnet_ids: List[]
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
    :param db_subnet_group_description: The description for the subnet group.
    :type db_subnet_group_description: str

    """
    return web.Response(status=200)


async def g_et_modify_event_subscription(request: web.Request, subscription_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sns_topic_arn=None, source_type=None, event_categories=None, enabled=None) -> web.Response:
    """g_et_modify_event_subscription

    Modifies an existing Amazon DocumentDB event notification subscription.

    :param subscription_name: The name of the Amazon DocumentDB event notification subscription.
    :type subscription_name: str
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
    :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
    :type sns_topic_arn: str
    :param source_type: &lt;p&gt;The type of source that is generating the events. For example, if you want to be notified of events generated by an instance, set this parameter to &lt;code&gt;db-instance&lt;/code&gt;. If this value is not specified, all events are returned.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;db-instance&lt;/code&gt;, &lt;code&gt;db-parameter-group&lt;/code&gt;, &lt;code&gt;db-security-group&lt;/code&gt; &lt;/p&gt;
    :type source_type: str
    :param event_categories:  A list of event categories for a &lt;code&gt;SourceType&lt;/code&gt; that you want to subscribe to.
    :type event_categories: List[]
    :param enabled:  A Boolean value; set to &lt;code&gt;true&lt;/code&gt; to activate the subscription. 
    :type enabled: bool

    """
    return web.Response(status=200)


async def g_et_modify_global_cluster(request: web.Request, global_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, new_global_cluster_identifier=None, deletion_protection=None) -> web.Response:
    """g_et_modify_global_cluster

    &lt;p&gt;Modify a setting for an Amazon DocumentDB global cluster. You can change one or more configuration parameters (for example: deletion protection), or the global cluster identifier by specifying these parameters and the new values in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

    :param global_cluster_identifier: &lt;p&gt;The identifier for the global cluster being modified. This parameter isn&#39;t case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing global cluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type global_cluster_identifier: str
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
    :param new_global_cluster_identifier: &lt;p&gt;The new identifier for a global cluster when you modify a global cluster. This value is stored as a lowercase string.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens&lt;/p&gt; &lt;p&gt;The first character must be a letter&lt;/p&gt; &lt;p&gt;Can&#39;t end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster2&lt;/code&gt; &lt;/p&gt;
    :type new_global_cluster_identifier: str
    :param deletion_protection: Indicates if the global cluster has deletion protection enabled. The global cluster can&#39;t be deleted when deletion protection is enabled. 
    :type deletion_protection: bool

    """
    return web.Response(status=200)


async def g_et_reboot_db_instance(request: web.Request, db_instance_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, force_failover=None) -> web.Response:
    """g_et_reboot_db_instance

    &lt;p&gt;You might need to reboot your instance, usually for maintenance reasons. For example, if you make certain changes, or if you change the cluster parameter group that is associated with the instance, you must reboot the instance for the changes to take effect. &lt;/p&gt; &lt;p&gt;Rebooting an instance restarts the database engine service. Rebooting an instance results in a momentary outage, during which the instance status is set to &lt;i&gt;rebooting&lt;/i&gt;. &lt;/p&gt;

    :param db_instance_identifier: &lt;p&gt;The instance identifier. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing &lt;code&gt;DBInstance&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_instance_identifier: str
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
    :param force_failover: &lt;p&gt; When &lt;code&gt;true&lt;/code&gt;, the reboot is conducted through a Multi-AZ failover. &lt;/p&gt; &lt;p&gt;Constraint: You can&#39;t specify &lt;code&gt;true&lt;/code&gt; if the instance is not configured for Multi-AZ.&lt;/p&gt;
    :type force_failover: bool

    """
    return web.Response(status=200)


async def g_et_remove_from_global_cluster(request: web.Request, global_cluster_identifier, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_from_global_cluster

    &lt;p&gt;Detaches an Amazon DocumentDB secondary cluster from a global cluster. The cluster becomes a standalone cluster with read-write capability instead of being read-only and receiving data from a primary in a different region. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

    :param global_cluster_identifier: The cluster identifier to detach from the Amazon DocumentDB global cluster. 
    :type global_cluster_identifier: str
    :param db_cluster_identifier: The Amazon Resource Name (ARN) identifying the cluster that was detached from the Amazon DocumentDB global cluster. 
    :type db_cluster_identifier: str
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


async def g_et_remove_source_identifier_from_subscription(request: web.Request, subscription_name, source_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_source_identifier_from_subscription

    Removes a source identifier from an existing Amazon DocumentDB event notification subscription.

    :param subscription_name: The name of the Amazon DocumentDB event notification subscription that you want to remove a source identifier from.
    :type subscription_name: str
    :param source_identifier:  The source identifier to be removed from the subscription, such as the instance identifier for an instance, or the name of a security group. 
    :type source_identifier: str
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


async def g_et_remove_tags_from_resource(request: web.Request, resource_name, tag_keys, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_tags_from_resource

    Removes metadata tags from an Amazon DocumentDB resource.

    :param resource_name: The Amazon DocumentDB resource that the tags are removed from. This value is an Amazon Resource Name (ARN).
    :type resource_name: str
    :param tag_keys: The tag key (name) of the tag to be removed.
    :type tag_keys: List[str]
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


async def g_et_reset_db_cluster_parameter_group(request: web.Request, db_cluster_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reset_all_parameters=None, parameters=None) -> web.Response:
    """g_et_reset_db_cluster_parameter_group

    &lt;p&gt; Modifies the parameters of a cluster parameter group to the default value. To reset specific parameters, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt; and &lt;code&gt;ApplyMethod&lt;/code&gt;. To reset the entire cluster parameter group, specify the &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; and &lt;code&gt;ResetAllParameters&lt;/code&gt; parameters. &lt;/p&gt; &lt;p&gt; When you reset the entire group, dynamic parameters are updated immediately and static parameters are set to &lt;code&gt;pending-reboot&lt;/code&gt; to take effect on the next DB instance reboot.&lt;/p&gt;

    :param db_cluster_parameter_group_name: The name of the cluster parameter group to reset.
    :type db_cluster_parameter_group_name: str
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
    :param reset_all_parameters: A value that is set to &lt;code&gt;true&lt;/code&gt; to reset all parameters in the cluster parameter group to their default values, and &lt;code&gt;false&lt;/code&gt; otherwise. You can&#39;t use this parameter if there is a list of parameter names specified for the &lt;code&gt;Parameters&lt;/code&gt; parameter.
    :type reset_all_parameters: bool
    :param parameters: A list of parameter names in the cluster parameter group to reset to the default values. You can&#39;t use this parameter if the &lt;code&gt;ResetAllParameters&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt;.
    :type parameters: list | bytes

    """
    parameters = [GETModifyDBClusterParameterGroupParametersParameterInner.from_dict(d) for d in parameters]
    return web.Response(status=200)


async def g_et_restore_db_cluster_from_snapshot(request: web.Request, db_cluster_identifier, snapshot_identifier, engine, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, availability_zones=None, engine_version=None, port=None, db_subnet_group_name=None, vpc_security_group_ids=None, tags=None, kms_key_id=None, enable_cloudwatch_logs_exports=None, deletion_protection=None, db_cluster_parameter_group_name=None) -> web.Response:
    """g_et_restore_db_cluster_from_snapshot

    &lt;p&gt;Creates a new cluster from a snapshot or cluster snapshot.&lt;/p&gt; &lt;p&gt;If a snapshot is specified, the target cluster is created from the source DB snapshot with a default configuration and default security group.&lt;/p&gt; &lt;p&gt;If a cluster snapshot is specified, the target cluster is created from the source cluster restore point with the same configuration as the original source DB cluster, except that the new cluster is created with the default security group.&lt;/p&gt;

    :param db_cluster_identifier: &lt;p&gt;The name of the cluster to create from the snapshot or cluster snapshot. This parameter isn&#39;t case sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-snapshot-id&lt;/code&gt; &lt;/p&gt;
    :type db_cluster_identifier: str
    :param snapshot_identifier: &lt;p&gt;The identifier for the snapshot or cluster snapshot to restore from.&lt;/p&gt; &lt;p&gt;You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing snapshot.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type snapshot_identifier: str
    :param engine: &lt;p&gt;The database engine to use for the new cluster.&lt;/p&gt; &lt;p&gt;Default: The same as source.&lt;/p&gt; &lt;p&gt;Constraint: Must be compatible with the engine of the source.&lt;/p&gt;
    :type engine: str
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
    :param availability_zones: Provides the list of Amazon EC2 Availability Zones that instances in the restored DB cluster can be created in.
    :type availability_zones: List[]
    :param engine_version: The version of the database engine to use for the new cluster.
    :type engine_version: str
    :param port: &lt;p&gt;The port number on which the new cluster accepts connections.&lt;/p&gt; &lt;p&gt;Constraints: Must be a value from &lt;code&gt;1150&lt;/code&gt; to &lt;code&gt;65535&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Default: The same port as the original cluster.&lt;/p&gt;
    :type port: int
    :param db_subnet_group_name: &lt;p&gt;The name of the subnet group to use for the new cluster.&lt;/p&gt; &lt;p&gt;Constraints: If provided, must match the name of an existing &lt;code&gt;DBSubnetGroup&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param vpc_security_group_ids: A list of virtual private cloud (VPC) security groups that the new cluster will belong to.
    :type vpc_security_group_ids: List[]
    :param tags: The tags to be assigned to the restored cluster.
    :type tags: list | bytes
    :param kms_key_id: &lt;p&gt;The KMS key identifier to use when restoring an encrypted cluster from a DB snapshot or cluster snapshot.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a cluster with the same Amazon Web Services account that owns the KMS encryption key used to encrypt the new cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.&lt;/p&gt; &lt;p&gt;If you do not specify a value for the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter, then the following occurs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the snapshot or cluster snapshot in &lt;code&gt;SnapshotIdentifier&lt;/code&gt; is encrypted, then the restored cluster is encrypted using the KMS key that was used to encrypt the snapshot or the cluster snapshot.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the snapshot or the cluster snapshot in &lt;code&gt;SnapshotIdentifier&lt;/code&gt; is not encrypted, then the restored DB cluster is not encrypted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type kms_key_id: str
    :param enable_cloudwatch_logs_exports: A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.
    :type enable_cloudwatch_logs_exports: List[str]
    :param deletion_protection: Specifies whether this cluster can be deleted. If &lt;code&gt;DeletionProtection&lt;/code&gt; is enabled, the cluster cannot be deleted unless it is modified and &lt;code&gt;DeletionProtection&lt;/code&gt; is disabled. &lt;code&gt;DeletionProtection&lt;/code&gt; protects clusters from being accidentally deleted.
    :type deletion_protection: bool
    :param db_cluster_parameter_group_name: &lt;p&gt;The name of the DB cluster parameter group to associate with this DB cluster.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Type:&lt;/i&gt; String.       &lt;i&gt;Required:&lt;/i&gt; No.&lt;/p&gt; &lt;p&gt;If this argument is omitted, the default DB cluster parameter group is used. If supplied, must match the name of an existing default DB cluster parameter group. The string must consist of from 1 to 255 letters, numbers or hyphens. Its first character must be a letter, and it cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt;
    :type db_cluster_parameter_group_name: str

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_restore_db_cluster_to_point_in_time(request: web.Request, db_cluster_identifier, source_db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, restore_type=None, restore_to_time=None, use_latest_restorable_time=None, port=None, db_subnet_group_name=None, vpc_security_group_ids=None, tags=None, kms_key_id=None, enable_cloudwatch_logs_exports=None, deletion_protection=None) -> web.Response:
    """g_et_restore_db_cluster_to_point_in_time

    Restores a cluster to an arbitrary point in time. Users can restore to any point in time before &lt;code&gt;LatestRestorableTime&lt;/code&gt; for up to &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; days. The target cluster is created from the source cluster with the same configuration as the original cluster, except that the new cluster is created with the default security group. 

    :param db_cluster_identifier: &lt;p&gt;The name of the new cluster to be created.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param source_db_cluster_identifier: &lt;p&gt;The identifier of the source cluster from which to restore.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing &lt;code&gt;DBCluster&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_db_cluster_identifier: str
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
    :param restore_type: &lt;p&gt;The type of restore to be performed. You can specify one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;full-copy&lt;/code&gt; - The new DB cluster is restored as a full copy of the source DB cluster.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;copy-on-write&lt;/code&gt; - The new DB cluster is restored as a clone of the source DB cluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Constraints: You can&#39;t specify &lt;code&gt;copy-on-write&lt;/code&gt; if the engine version of the source DB cluster is earlier than 1.11.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a &lt;code&gt;RestoreType&lt;/code&gt; value, then the new DB cluster is restored as a full copy of the source DB cluster.&lt;/p&gt;
    :type restore_type: str
    :param restore_to_time: &lt;p&gt;The date and time to restore the cluster to.&lt;/p&gt; &lt;p&gt;Valid values: A time in Universal Coordinated Time (UTC) format.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be before the latest restorable time for the instance.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be specified if the &lt;code&gt;UseLatestRestorableTime&lt;/code&gt; parameter is not provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be specified if the &lt;code&gt;UseLatestRestorableTime&lt;/code&gt; parameter is &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be specified if the &lt;code&gt;RestoreType&lt;/code&gt; parameter is &lt;code&gt;copy-on-write&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;2015-03-07T23:45:00Z&lt;/code&gt; &lt;/p&gt;
    :type restore_to_time: str
    :param use_latest_restorable_time: &lt;p&gt;A value that is set to &lt;code&gt;true&lt;/code&gt; to restore the cluster to the latest restorable backup time, and &lt;code&gt;false&lt;/code&gt; otherwise. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: Cannot be specified if the &lt;code&gt;RestoreToTime&lt;/code&gt; parameter is provided.&lt;/p&gt;
    :type use_latest_restorable_time: bool
    :param port: &lt;p&gt;The port number on which the new cluster accepts connections.&lt;/p&gt; &lt;p&gt;Constraints: Must be a value from &lt;code&gt;1150&lt;/code&gt; to &lt;code&gt;65535&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Default: The default port for the engine.&lt;/p&gt;
    :type port: int
    :param db_subnet_group_name: &lt;p&gt;The subnet group name to use for the new cluster.&lt;/p&gt; &lt;p&gt;Constraints: If provided, must match the name of an existing &lt;code&gt;DBSubnetGroup&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param vpc_security_group_ids: A list of VPC security groups that the new cluster belongs to.
    :type vpc_security_group_ids: List[]
    :param tags: The tags to be assigned to the restored cluster.
    :type tags: list | bytes
    :param kms_key_id: &lt;p&gt;The KMS key identifier to use when restoring an encrypted cluster from an encrypted cluster.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a cluster with the same Amazon Web Services account that owns the KMS encryption key used to encrypt the new cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.&lt;/p&gt; &lt;p&gt;You can restore to a new cluster and encrypt the new cluster with an KMS key that is different from the KMS key used to encrypt the source cluster. The new DB cluster is encrypted with the KMS key identified by the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you do not specify a value for the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter, then the following occurs:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the cluster is encrypted, then the restored cluster is encrypted using the KMS key that was used to encrypt the source cluster.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the cluster is not encrypted, then the restored cluster is not encrypted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If &lt;code&gt;DBClusterIdentifier&lt;/code&gt; refers to a cluster that is not encrypted, then the restore request is rejected.&lt;/p&gt;
    :type kms_key_id: str
    :param enable_cloudwatch_logs_exports: A list of log types that must be enabled for exporting to Amazon CloudWatch Logs.
    :type enable_cloudwatch_logs_exports: List[str]
    :param deletion_protection: Specifies whether this cluster can be deleted. If &lt;code&gt;DeletionProtection&lt;/code&gt; is enabled, the cluster cannot be deleted unless it is modified and &lt;code&gt;DeletionProtection&lt;/code&gt; is disabled. &lt;code&gt;DeletionProtection&lt;/code&gt; protects clusters from being accidentally deleted.
    :type deletion_protection: bool

    """
    restore_to_time = util.deserialize_datetime(restore_to_time)
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_start_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_start_db_cluster

    Restarts the stopped cluster that is specified by &lt;code&gt;DBClusterIdentifier&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-stop-start.html\&quot;&gt;Stopping and Starting an Amazon DocumentDB Cluster&lt;/a&gt;.

    :param db_cluster_identifier: The identifier of the cluster to restart. Example: &lt;code&gt;docdb-2019-05-28-15-24-52&lt;/code&gt; 
    :type db_cluster_identifier: str
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


async def g_et_stop_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_stop_db_cluster

    Stops the running cluster that is specified by &lt;code&gt;DBClusterIdentifier&lt;/code&gt;. The cluster must be in the &lt;i&gt;available&lt;/i&gt; state. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-stop-start.html\&quot;&gt;Stopping and Starting an Amazon DocumentDB Cluster&lt;/a&gt;.

    :param db_cluster_identifier: The identifier of the cluster to stop. Example: &lt;code&gt;docdb-2019-05-28-15-24-52&lt;/code&gt; 
    :type db_cluster_identifier: str
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


async def p_ost_add_source_identifier_to_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_source_identifier_to_subscription

    Adds a source identifier to an existing event notification subscription.

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
    body = AddSourceIdentifierToSubscriptionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_add_tags_to_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_tags_to_resource

    Adds metadata tags to an Amazon DocumentDB resource. You can use these tags with cost allocation reporting to track costs that are associated with Amazon DocumentDB resources or in a &lt;code&gt;Condition&lt;/code&gt; statement in an Identity and Access Management (IAM) policy for Amazon DocumentDB.

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
    body = AddTagsToResourceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_apply_pending_maintenance_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_apply_pending_maintenance_action

    Applies a pending maintenance action to a resource (for example, to an Amazon DocumentDB instance).

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
    body = ApplyPendingMaintenanceActionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_copy_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_copy_db_cluster_parameter_group

    Copies the specified cluster parameter group.

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
    body = CopyDBClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_copy_db_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_copy_db_cluster_snapshot

    &lt;p&gt;Copies a snapshot of a cluster.&lt;/p&gt; &lt;p&gt;To copy a cluster snapshot from a shared manual cluster snapshot, &lt;code&gt;SourceDBClusterSnapshotIdentifier&lt;/code&gt; must be the Amazon Resource Name (ARN) of the shared cluster snapshot. You can only copy a shared DB cluster snapshot, whether encrypted or not, in the same Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;To cancel the copy operation after it is in progress, delete the target cluster snapshot identified by &lt;code&gt;TargetDBClusterSnapshotIdentifier&lt;/code&gt; while that cluster snapshot is in the &lt;i&gt;copying&lt;/i&gt; status.&lt;/p&gt;

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
    body = CopyDBClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_cluster

    Creates a new Amazon DocumentDB cluster.

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
    body = CreateDBClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_cluster_parameter_group

    &lt;p&gt;Creates a new cluster parameter group.&lt;/p&gt; &lt;p&gt;Parameters in a cluster parameter group apply to all of the instances in a cluster.&lt;/p&gt; &lt;p&gt;A cluster parameter group is initially created with the default parameters for the database engine used by instances in the cluster. In Amazon DocumentDB, you cannot make modifications directly to the &lt;code&gt;default.docdb3.6&lt;/code&gt; cluster parameter group. If your Amazon DocumentDB cluster is using the default cluster parameter group and you want to modify a value in it, you must first &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_group-create.html\&quot;&gt; create a new parameter group&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_group-copy.html\&quot;&gt; copy an existing parameter group&lt;/a&gt;, modify it, and then apply the modified parameter group to your cluster. For the new cluster parameter group and associated settings to take effect, you must then reboot the instances in the cluster without failover. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/cluster_parameter_group-modify.html\&quot;&gt; Modifying Amazon DocumentDB Cluster Parameter Groups&lt;/a&gt;. &lt;/p&gt;

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
    body = CreateDBClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_cluster_snapshot

    Creates a snapshot of a cluster. 

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
    body = CreateDBClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_instance(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_instance

    Creates a new instance.

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
    body = CreateDBInstanceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_subnet_group

    Creates a new subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the Amazon Web Services Region.

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
    body = CreateDBSubnetGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_event_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_event_subscription

    &lt;p&gt;Creates an Amazon DocumentDB event notification subscription. This action requires a topic Amazon Resource Name (ARN) created by using the Amazon DocumentDB console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the Amazon SNS console.&lt;/p&gt; &lt;p&gt;You can specify the type of source (&lt;code&gt;SourceType&lt;/code&gt;) that you want to be notified of. You can also provide a list of Amazon DocumentDB sources (&lt;code&gt;SourceIds&lt;/code&gt;) that trigger the events, and you can provide a list of event categories (&lt;code&gt;EventCategories&lt;/code&gt;) for events that you want to be notified of. For example, you can specify &lt;code&gt;SourceType &#x3D; db-instance&lt;/code&gt;, &lt;code&gt;SourceIds &#x3D; mydbinstance1, mydbinstance2&lt;/code&gt; and &lt;code&gt;EventCategories &#x3D; Availability, Backup&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you specify both the &lt;code&gt;SourceType&lt;/code&gt; and &lt;code&gt;SourceIds&lt;/code&gt; (such as &lt;code&gt;SourceType &#x3D; db-instance&lt;/code&gt; and &lt;code&gt;SourceIdentifier &#x3D; myDBInstance1&lt;/code&gt;), you are notified of all the &lt;code&gt;db-instance&lt;/code&gt; events for the specified source. If you specify a &lt;code&gt;SourceType&lt;/code&gt; but do not specify a &lt;code&gt;SourceIdentifier&lt;/code&gt;, you receive notice of the events for that source type for all your Amazon DocumentDB sources. If you do not specify either the &lt;code&gt;SourceType&lt;/code&gt; or the &lt;code&gt;SourceIdentifier&lt;/code&gt;, you are notified of events generated from all Amazon DocumentDB sources belonging to your customer account.&lt;/p&gt;

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
    body = CreateEventSubscriptionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_global_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_global_cluster

    &lt;p&gt;Creates an Amazon DocumentDB global cluster that can span multiple multiple Amazon Web Services Regions. The global cluster contains one primary cluster with read-write capability, and up-to give read-only secondary clusters. Global clusters uses storage-based fast replication across regions with latencies less than one second, using dedicated infrastructure with no impact to your workload’s performance.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;You can create a global cluster that is initially empty, and then add a primary and a secondary to it. Or you can specify an existing cluster during the create operation, and this cluster becomes the primary of the global cluster. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateGlobalClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_cluster

    &lt;p&gt;Deletes a previously provisioned cluster. When you delete a cluster, all automated backups for that cluster are deleted and can&#39;t be recovered. Manual DB cluster snapshots of the specified cluster are not deleted.&lt;/p&gt; &lt;p/&gt;

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
    body = DeleteDBClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_cluster_parameter_group

    Deletes a specified cluster parameter group. The cluster parameter group to be deleted can&#39;t be associated with any clusters.

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
    body = DeleteDBClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_db_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_cluster_snapshot

    &lt;p&gt;Deletes a cluster snapshot. If the snapshot is being copied, the copy operation is terminated.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The cluster snapshot must be in the &lt;code&gt;available&lt;/code&gt; state to be deleted.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteDBClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_db_instance(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_instance

    Deletes a previously provisioned instance.

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
    body = DeleteDBInstanceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_db_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_subnet_group

    &lt;p&gt;Deletes a subnet group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The specified database subnet group must not be associated with any DB instances.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteDBSubnetGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_event_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_event_subscription

    Deletes an Amazon DocumentDB event notification subscription.

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
    body = DeleteEventSubscriptionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_global_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_global_cluster

    &lt;p&gt;Deletes a global cluster. The primary and secondary clusters must already be detached or deleted before attempting to delete a global cluster.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteGlobalClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_certificates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_certificates

    Returns a list of certificate authority (CA) certificates provided by Amazon DocumentDB for this Amazon Web Services account.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeCertificatesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_cluster_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_cluster_parameter_groups

    Returns a list of &lt;code&gt;DBClusterParameterGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; parameter is specified, the list contains only the description of the specified cluster parameter group. 

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDBClusterParameterGroupsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_cluster_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_cluster_parameters

    Returns the detailed parameter list for a particular cluster parameter group.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDBClusterParametersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_cluster_snapshot_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_db_cluster_snapshot_attributes

    &lt;p&gt;Returns a list of cluster snapshot attribute names and values for a manual DB cluster snapshot.&lt;/p&gt; &lt;p&gt;When you share snapshots with other Amazon Web Services accounts, &lt;code&gt;DescribeDBClusterSnapshotAttributes&lt;/code&gt; returns the &lt;code&gt;restore&lt;/code&gt; attribute and a list of IDs for the Amazon Web Services accounts that are authorized to copy or restore the manual cluster snapshot. If &lt;code&gt;all&lt;/code&gt; is included in the list of values for the &lt;code&gt;restore&lt;/code&gt; attribute, then the manual cluster snapshot is public and can be copied or restored by all Amazon Web Services accounts.&lt;/p&gt;

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
    body = DescribeDBClusterSnapshotAttributesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_cluster_snapshots(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_cluster_snapshots

    Returns information about cluster snapshots. This API operation supports pagination.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDBClusterSnapshotsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_clusters

    Returns information about provisioned Amazon DocumentDB clusters. This API operation supports pagination. For certain management features such as cluster and instance lifecycle management, Amazon DocumentDB leverages operational technology that is shared with Amazon RDS and Amazon Neptune. Use the &lt;code&gt;filterName&#x3D;engine,Values&#x3D;docdb&lt;/code&gt; filter parameter to return only Amazon DocumentDB clusters.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDBClustersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_engine_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_engine_versions

    Returns a list of the available engines.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDBEngineVersionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_instances

    Returns information about provisioned Amazon DocumentDB instances. This API supports pagination.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDBInstancesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_subnet_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_subnet_groups

    Returns a list of &lt;code&gt;DBSubnetGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBSubnetGroupName&lt;/code&gt; is specified, the list will contain only the descriptions of the specified &lt;code&gt;DBSubnetGroup&lt;/code&gt;.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDBSubnetGroupsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_engine_default_cluster_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_engine_default_cluster_parameters

    Returns the default engine and system parameter information for the cluster database engine.

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
    body = DescribeEngineDefaultClusterParametersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_event_categories(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_event_categories

    Displays a list of categories for all event source types, or, if specified, for a specified source type. 

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
    body = DescribeEventCategoriesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_event_subscriptions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_event_subscriptions

    &lt;p&gt;Lists all the subscription descriptions for a customer account. The description for a subscription includes &lt;code&gt;SubscriptionName&lt;/code&gt;, &lt;code&gt;SNSTopicARN&lt;/code&gt;, &lt;code&gt;CustomerID&lt;/code&gt;, &lt;code&gt;SourceType&lt;/code&gt;, &lt;code&gt;SourceID&lt;/code&gt;, &lt;code&gt;CreationTime&lt;/code&gt;, and &lt;code&gt;Status&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you specify a &lt;code&gt;SubscriptionName&lt;/code&gt;, lists the description for that subscription.&lt;/p&gt;

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEventSubscriptionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_events

    Returns events related to instances, security groups, snapshots, and DB parameter groups for the past 14 days. You can obtain events specific to a particular DB instance, security group, snapshot, or parameter group by providing the name as a parameter. By default, the events of the past hour are returned.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEventsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_global_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_global_clusters

    &lt;p&gt;Returns information about Amazon DocumentDB global clusters. This API supports pagination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeGlobalClustersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_orderable_db_instance_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_orderable_db_instance_options

    Returns a list of orderable instance options for the specified engine.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeOrderableDBInstanceOptionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_pending_maintenance_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_pending_maintenance_actions

    Returns a list of resources (for example, instances) that have at least one pending maintenance action.

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
    :param max_records: Pagination limit
    :type max_records: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribePendingMaintenanceActionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_failover_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_failover_db_cluster

    &lt;p&gt;Forces a failover for a cluster.&lt;/p&gt; &lt;p&gt;A failover for a cluster promotes one of the Amazon DocumentDB replicas (read-only instances) in the cluster to be the primary instance (the cluster writer).&lt;/p&gt; &lt;p&gt;If the primary instance fails, Amazon DocumentDB automatically fails over to an Amazon DocumentDB replica, if one exists. You can force a failover when you want to simulate a failure of a primary instance for testing.&lt;/p&gt;

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
    body = FailoverDBClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_tags_for_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_tags_for_resource

    Lists all tags on an Amazon DocumentDB resource.

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
    body = ListTagsForResourceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_cluster

    Modifies a setting for an Amazon DocumentDB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. 

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
    body = ModifyDBClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_cluster_parameter_group

    &lt;p&gt; Modifies the parameters of a cluster parameter group. To modify more than one parameter, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt;, &lt;code&gt;ParameterValue&lt;/code&gt;, and &lt;code&gt;ApplyMethod&lt;/code&gt;. A maximum of 20 parameters can be modified in a single request. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot or maintenance window before the change can take effect.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;After you create a cluster parameter group, you should wait at least 5 minutes before creating your first cluster that uses that cluster parameter group as the default parameter group. This allows Amazon DocumentDB to fully complete the create action before the parameter group is used as the default for a new cluster. This step is especially important for parameters that are critical when creating the default database for a cluster, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter.&lt;/p&gt; &lt;/important&gt;

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
    body = ModifyDBClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_db_cluster_snapshot_attribute(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_cluster_snapshot_attribute

    &lt;p&gt;Adds an attribute and values to, or removes an attribute and values from, a manual cluster snapshot.&lt;/p&gt; &lt;p&gt;To share a manual cluster snapshot with other Amazon Web Services accounts, specify &lt;code&gt;restore&lt;/code&gt; as the &lt;code&gt;AttributeName&lt;/code&gt;, and use the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter to add a list of IDs of the Amazon Web Services accounts that are authorized to restore the manual cluster snapshot. Use the value &lt;code&gt;all&lt;/code&gt; to make the manual cluster snapshot public, which means that it can be copied or restored by all Amazon Web Services accounts. Do not add the &lt;code&gt;all&lt;/code&gt; value for any manual cluster snapshots that contain private information that you don&#39;t want available to all Amazon Web Services accounts. If a manual cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized Amazon Web Services account IDs for the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter. You can&#39;t use &lt;code&gt;all&lt;/code&gt; as a value for that parameter in this case.&lt;/p&gt;

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
    body = ModifyDBClusterSnapshotAttributeMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_db_instance(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_instance

    Modifies settings for an instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.

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
    body = ModifyDBInstanceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_db_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_subnet_group

    Modifies an existing subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the Amazon Web Services Region.

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
    body = ModifyDBSubnetGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_event_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_event_subscription

    Modifies an existing Amazon DocumentDB event notification subscription.

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
    body = ModifyEventSubscriptionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_global_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_global_cluster

    &lt;p&gt;Modify a setting for an Amazon DocumentDB global cluster. You can change one or more configuration parameters (for example: deletion protection), or the global cluster identifier by specifying these parameters and the new values in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    body = ModifyGlobalClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_reboot_db_instance(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reboot_db_instance

    &lt;p&gt;You might need to reboot your instance, usually for maintenance reasons. For example, if you make certain changes, or if you change the cluster parameter group that is associated with the instance, you must reboot the instance for the changes to take effect. &lt;/p&gt; &lt;p&gt;Rebooting an instance restarts the database engine service. Rebooting an instance results in a momentary outage, during which the instance status is set to &lt;i&gt;rebooting&lt;/i&gt;. &lt;/p&gt;

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
    body = RebootDBInstanceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_from_global_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_from_global_cluster

    &lt;p&gt;Detaches an Amazon DocumentDB secondary cluster from a global cluster. The cluster becomes a standalone cluster with read-write capability instead of being read-only and receiving data from a primary in a different region. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only applies to Amazon DocumentDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    body = RemoveFromGlobalClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_source_identifier_from_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_source_identifier_from_subscription

    Removes a source identifier from an existing Amazon DocumentDB event notification subscription.

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
    body = RemoveSourceIdentifierFromSubscriptionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_tags_from_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_tags_from_resource

    Removes metadata tags from an Amazon DocumentDB resource.

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
    body = RemoveTagsFromResourceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_reset_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reset_db_cluster_parameter_group

    &lt;p&gt; Modifies the parameters of a cluster parameter group to the default value. To reset specific parameters, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt; and &lt;code&gt;ApplyMethod&lt;/code&gt;. To reset the entire cluster parameter group, specify the &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; and &lt;code&gt;ResetAllParameters&lt;/code&gt; parameters. &lt;/p&gt; &lt;p&gt; When you reset the entire group, dynamic parameters are updated immediately and static parameters are set to &lt;code&gt;pending-reboot&lt;/code&gt; to take effect on the next DB instance reboot.&lt;/p&gt;

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
    body = ResetDBClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_restore_db_cluster_from_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_restore_db_cluster_from_snapshot

    &lt;p&gt;Creates a new cluster from a snapshot or cluster snapshot.&lt;/p&gt; &lt;p&gt;If a snapshot is specified, the target cluster is created from the source DB snapshot with a default configuration and default security group.&lt;/p&gt; &lt;p&gt;If a cluster snapshot is specified, the target cluster is created from the source cluster restore point with the same configuration as the original source DB cluster, except that the new cluster is created with the default security group.&lt;/p&gt;

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
    body = RestoreDBClusterFromSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_restore_db_cluster_to_point_in_time(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_restore_db_cluster_to_point_in_time

    Restores a cluster to an arbitrary point in time. Users can restore to any point in time before &lt;code&gt;LatestRestorableTime&lt;/code&gt; for up to &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; days. The target cluster is created from the source cluster with the same configuration as the original cluster, except that the new cluster is created with the default security group. 

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
    body = RestoreDBClusterToPointInTimeMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_start_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_start_db_cluster

    Restarts the stopped cluster that is specified by &lt;code&gt;DBClusterIdentifier&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-stop-start.html\&quot;&gt;Stopping and Starting an Amazon DocumentDB Cluster&lt;/a&gt;.

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
    body = StartDBClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_stop_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_stop_db_cluster

    Stops the running cluster that is specified by &lt;code&gt;DBClusterIdentifier&lt;/code&gt;. The cluster must be in the &lt;i&gt;available&lt;/i&gt; state. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-stop-start.html\&quot;&gt;Stopping and Starting an Amazon DocumentDB Cluster&lt;/a&gt;.

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
    body = StopDBClusterMessage.from_dict(body)
    return web.Response(status=200)
