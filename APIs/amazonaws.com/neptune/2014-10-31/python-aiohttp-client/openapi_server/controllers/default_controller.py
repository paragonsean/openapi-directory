from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_role_to_db_cluster_message import AddRoleToDBClusterMessage
from openapi_server.models.add_source_identifier_to_subscription_message import AddSourceIdentifierToSubscriptionMessage
from openapi_server.models.add_source_identifier_to_subscription_result import AddSourceIdentifierToSubscriptionResult
from openapi_server.models.add_tags_to_resource_message import AddTagsToResourceMessage
from openapi_server.models.apply_pending_maintenance_action_message import ApplyPendingMaintenanceActionMessage
from openapi_server.models.apply_pending_maintenance_action_result import ApplyPendingMaintenanceActionResult
from openapi_server.models.copy_db_cluster_parameter_group_message import CopyDBClusterParameterGroupMessage
from openapi_server.models.copy_db_cluster_parameter_group_result import CopyDBClusterParameterGroupResult
from openapi_server.models.copy_db_cluster_snapshot_message import CopyDBClusterSnapshotMessage
from openapi_server.models.copy_db_cluster_snapshot_result import CopyDBClusterSnapshotResult
from openapi_server.models.copy_db_parameter_group_message import CopyDBParameterGroupMessage
from openapi_server.models.copy_db_parameter_group_result import CopyDBParameterGroupResult
from openapi_server.models.create_db_cluster_endpoint_message import CreateDBClusterEndpointMessage
from openapi_server.models.create_db_cluster_endpoint_output import CreateDBClusterEndpointOutput
from openapi_server.models.create_db_cluster_message import CreateDBClusterMessage
from openapi_server.models.create_db_cluster_parameter_group_message import CreateDBClusterParameterGroupMessage
from openapi_server.models.create_db_cluster_parameter_group_result import CreateDBClusterParameterGroupResult
from openapi_server.models.create_db_cluster_result import CreateDBClusterResult
from openapi_server.models.create_db_cluster_snapshot_message import CreateDBClusterSnapshotMessage
from openapi_server.models.create_db_cluster_snapshot_result import CreateDBClusterSnapshotResult
from openapi_server.models.create_db_instance_message import CreateDBInstanceMessage
from openapi_server.models.create_db_instance_result import CreateDBInstanceResult
from openapi_server.models.create_db_parameter_group_message import CreateDBParameterGroupMessage
from openapi_server.models.create_db_parameter_group_result import CreateDBParameterGroupResult
from openapi_server.models.create_db_subnet_group_message import CreateDBSubnetGroupMessage
from openapi_server.models.create_db_subnet_group_result import CreateDBSubnetGroupResult
from openapi_server.models.create_event_subscription_message import CreateEventSubscriptionMessage
from openapi_server.models.create_event_subscription_result import CreateEventSubscriptionResult
from openapi_server.models.create_global_cluster_message import CreateGlobalClusterMessage
from openapi_server.models.create_global_cluster_result import CreateGlobalClusterResult
from openapi_server.models.db_cluster_endpoint_message import DBClusterEndpointMessage
from openapi_server.models.db_cluster_message import DBClusterMessage
from openapi_server.models.db_cluster_parameter_group_details import DBClusterParameterGroupDetails
from openapi_server.models.db_cluster_parameter_group_name_message import DBClusterParameterGroupNameMessage
from openapi_server.models.db_cluster_parameter_groups_message import DBClusterParameterGroupsMessage
from openapi_server.models.db_cluster_snapshot_message import DBClusterSnapshotMessage
from openapi_server.models.db_engine_version_message import DBEngineVersionMessage
from openapi_server.models.db_instance_message import DBInstanceMessage
from openapi_server.models.db_parameter_group_details import DBParameterGroupDetails
from openapi_server.models.db_parameter_group_name_message import DBParameterGroupNameMessage
from openapi_server.models.db_parameter_groups_message import DBParameterGroupsMessage
from openapi_server.models.db_subnet_group_message import DBSubnetGroupMessage
from openapi_server.models.delete_db_cluster_endpoint_message import DeleteDBClusterEndpointMessage
from openapi_server.models.delete_db_cluster_endpoint_output import DeleteDBClusterEndpointOutput
from openapi_server.models.delete_db_cluster_message import DeleteDBClusterMessage
from openapi_server.models.delete_db_cluster_parameter_group_message import DeleteDBClusterParameterGroupMessage
from openapi_server.models.delete_db_cluster_result import DeleteDBClusterResult
from openapi_server.models.delete_db_cluster_snapshot_message import DeleteDBClusterSnapshotMessage
from openapi_server.models.delete_db_cluster_snapshot_result import DeleteDBClusterSnapshotResult
from openapi_server.models.delete_db_instance_message import DeleteDBInstanceMessage
from openapi_server.models.delete_db_instance_result import DeleteDBInstanceResult
from openapi_server.models.delete_db_parameter_group_message import DeleteDBParameterGroupMessage
from openapi_server.models.delete_db_subnet_group_message import DeleteDBSubnetGroupMessage
from openapi_server.models.delete_event_subscription_message import DeleteEventSubscriptionMessage
from openapi_server.models.delete_event_subscription_result import DeleteEventSubscriptionResult
from openapi_server.models.delete_global_cluster_message import DeleteGlobalClusterMessage
from openapi_server.models.delete_global_cluster_result import DeleteGlobalClusterResult
from openapi_server.models.describe_db_cluster_endpoints_message import DescribeDBClusterEndpointsMessage
from openapi_server.models.describe_db_cluster_parameter_groups_message import DescribeDBClusterParameterGroupsMessage
from openapi_server.models.describe_db_cluster_parameters_message import DescribeDBClusterParametersMessage
from openapi_server.models.describe_db_cluster_snapshot_attributes_message import DescribeDBClusterSnapshotAttributesMessage
from openapi_server.models.describe_db_cluster_snapshot_attributes_result import DescribeDBClusterSnapshotAttributesResult
from openapi_server.models.describe_db_cluster_snapshots_message import DescribeDBClusterSnapshotsMessage
from openapi_server.models.describe_db_clusters_message import DescribeDBClustersMessage
from openapi_server.models.describe_db_engine_versions_message import DescribeDBEngineVersionsMessage
from openapi_server.models.describe_db_instances_message import DescribeDBInstancesMessage
from openapi_server.models.describe_db_parameter_groups_message import DescribeDBParameterGroupsMessage
from openapi_server.models.describe_db_parameters_message import DescribeDBParametersMessage
from openapi_server.models.describe_db_subnet_groups_message import DescribeDBSubnetGroupsMessage
from openapi_server.models.describe_engine_default_cluster_parameters_message import DescribeEngineDefaultClusterParametersMessage
from openapi_server.models.describe_engine_default_cluster_parameters_result import DescribeEngineDefaultClusterParametersResult
from openapi_server.models.describe_engine_default_parameters_message import DescribeEngineDefaultParametersMessage
from openapi_server.models.describe_engine_default_parameters_result import DescribeEngineDefaultParametersResult
from openapi_server.models.describe_event_categories_message import DescribeEventCategoriesMessage
from openapi_server.models.describe_event_subscriptions_message import DescribeEventSubscriptionsMessage
from openapi_server.models.describe_events_message import DescribeEventsMessage
from openapi_server.models.describe_global_clusters_message import DescribeGlobalClustersMessage
from openapi_server.models.describe_orderable_db_instance_options_message import DescribeOrderableDBInstanceOptionsMessage
from openapi_server.models.describe_pending_maintenance_actions_message import DescribePendingMaintenanceActionsMessage
from openapi_server.models.describe_valid_db_instance_modifications_message import DescribeValidDBInstanceModificationsMessage
from openapi_server.models.describe_valid_db_instance_modifications_result import DescribeValidDBInstanceModificationsResult
from openapi_server.models.event_categories_message import EventCategoriesMessage
from openapi_server.models.event_subscriptions_message import EventSubscriptionsMessage
from openapi_server.models.events_message import EventsMessage
from openapi_server.models.failover_db_cluster_message import FailoverDBClusterMessage
from openapi_server.models.failover_db_cluster_result import FailoverDBClusterResult
from openapi_server.models.failover_global_cluster_message import FailoverGlobalClusterMessage
from openapi_server.models.failover_global_cluster_result import FailoverGlobalClusterResult
from openapi_server.models.get_add_tags_to_resource_tags_parameter_inner import GETAddTagsToResourceTagsParameterInner
from openapi_server.models.get_create_db_cluster_serverless_v2_scaling_configuration_parameter import GETCreateDBClusterServerlessV2ScalingConfigurationParameter
from openapi_server.models.get_describe_db_cluster_endpoints_filters_parameter_inner import GETDescribeDBClusterEndpointsFiltersParameterInner
from openapi_server.models.get_modify_db_cluster_cloudwatch_logs_export_configuration_parameter import GETModifyDBClusterCloudwatchLogsExportConfigurationParameter
from openapi_server.models.get_modify_db_cluster_parameter_group_parameters_parameter_inner import GETModifyDBClusterParameterGroupParametersParameterInner
from openapi_server.models.global_clusters_message import GlobalClustersMessage
from openapi_server.models.list_tags_for_resource_message import ListTagsForResourceMessage
from openapi_server.models.modify_db_cluster_endpoint_message import ModifyDBClusterEndpointMessage
from openapi_server.models.modify_db_cluster_endpoint_output import ModifyDBClusterEndpointOutput
from openapi_server.models.modify_db_cluster_message import ModifyDBClusterMessage
from openapi_server.models.modify_db_cluster_parameter_group_message import ModifyDBClusterParameterGroupMessage
from openapi_server.models.modify_db_cluster_result import ModifyDBClusterResult
from openapi_server.models.modify_db_cluster_snapshot_attribute_message import ModifyDBClusterSnapshotAttributeMessage
from openapi_server.models.modify_db_cluster_snapshot_attribute_result import ModifyDBClusterSnapshotAttributeResult
from openapi_server.models.modify_db_instance_message import ModifyDBInstanceMessage
from openapi_server.models.modify_db_instance_result import ModifyDBInstanceResult
from openapi_server.models.modify_db_parameter_group_message import ModifyDBParameterGroupMessage
from openapi_server.models.modify_db_subnet_group_message import ModifyDBSubnetGroupMessage
from openapi_server.models.modify_db_subnet_group_result import ModifyDBSubnetGroupResult
from openapi_server.models.modify_event_subscription_message import ModifyEventSubscriptionMessage
from openapi_server.models.modify_event_subscription_result import ModifyEventSubscriptionResult
from openapi_server.models.modify_global_cluster_message import ModifyGlobalClusterMessage
from openapi_server.models.modify_global_cluster_result import ModifyGlobalClusterResult
from openapi_server.models.orderable_db_instance_options_message import OrderableDBInstanceOptionsMessage
from openapi_server.models.pending_maintenance_actions_message import PendingMaintenanceActionsMessage
from openapi_server.models.promote_read_replica_db_cluster_message import PromoteReadReplicaDBClusterMessage
from openapi_server.models.promote_read_replica_db_cluster_result import PromoteReadReplicaDBClusterResult
from openapi_server.models.reboot_db_instance_message import RebootDBInstanceMessage
from openapi_server.models.reboot_db_instance_result import RebootDBInstanceResult
from openapi_server.models.remove_from_global_cluster_message import RemoveFromGlobalClusterMessage
from openapi_server.models.remove_from_global_cluster_result import RemoveFromGlobalClusterResult
from openapi_server.models.remove_role_from_db_cluster_message import RemoveRoleFromDBClusterMessage
from openapi_server.models.remove_source_identifier_from_subscription_message import RemoveSourceIdentifierFromSubscriptionMessage
from openapi_server.models.remove_source_identifier_from_subscription_result import RemoveSourceIdentifierFromSubscriptionResult
from openapi_server.models.remove_tags_from_resource_message import RemoveTagsFromResourceMessage
from openapi_server.models.reset_db_cluster_parameter_group_message import ResetDBClusterParameterGroupMessage
from openapi_server.models.reset_db_parameter_group_message import ResetDBParameterGroupMessage
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


async def g_et_add_role_to_db_cluster(request: web.Request, db_cluster_identifier, role_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, feature_name=None) -> web.Response:
    """g_et_add_role_to_db_cluster

    Associates an Identity and Access Management (IAM) role with an Neptune DB cluster.

    :param db_cluster_identifier: The name of the DB cluster to associate the IAM role with.
    :type db_cluster_identifier: str
    :param role_arn: The Amazon Resource Name (ARN) of the IAM role to associate with the Neptune DB cluster, for example &lt;code&gt;arn:aws:iam::123456789012:role/NeptuneAccessRole&lt;/code&gt;.
    :type role_arn: str
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
    :param feature_name: The name of the feature for the Neptune DB cluster that the IAM role is to be associated with. For the list of supported feature names, see &lt;a href&#x3D;\&quot;neptune/latest/userguide/api-other-apis.html#DBEngineVersion\&quot;&gt;DBEngineVersion&lt;/a&gt;.
    :type feature_name: str

    """
    return web.Response(status=200)


async def g_et_add_source_identifier_to_subscription(request: web.Request, subscription_name, source_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_source_identifier_to_subscription

    Adds a source identifier to an existing event notification subscription.

    :param subscription_name: The name of the event notification subscription you want to add a source identifier to.
    :type subscription_name: str
    :param source_identifier: &lt;p&gt;The identifier of the event source to be added.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB instance, then a &lt;code&gt;DBInstanceIdentifier&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB security group, a &lt;code&gt;DBSecurityGroupName&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB parameter group, a &lt;code&gt;DBParameterGroupName&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB snapshot, a &lt;code&gt;DBSnapshotIdentifier&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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

    Adds metadata tags to an Amazon Neptune resource. These tags can also be used with cost allocation reporting to track cost associated with Amazon Neptune resources, or used in a Condition statement in an IAM policy for Amazon Neptune.

    :param resource_name: The Amazon Neptune resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\&quot;&gt; Constructing an Amazon Resource Name (ARN)&lt;/a&gt;.
    :type resource_name: str
    :param tags: The tags to be assigned to the Amazon Neptune resource.
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

    Applies a pending maintenance action to a resource (for example, to a DB instance).

    :param resource_identifier: The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\&quot;&gt; Constructing an Amazon Resource Name (ARN)&lt;/a&gt;.
    :type resource_identifier: str
    :param apply_action: &lt;p&gt;The pending maintenance action to apply to this resource.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;system-update&lt;/code&gt;, &lt;code&gt;db-upgrade&lt;/code&gt; &lt;/p&gt;
    :type apply_action: str
    :param opt_in_type: &lt;p&gt;A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type &lt;code&gt;immediate&lt;/code&gt; can&#39;t be undone.&lt;/p&gt; &lt;p&gt;Valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;immediate&lt;/code&gt; - Apply the maintenance action immediately.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;next-maintenance&lt;/code&gt; - Apply the maintenance action during the next maintenance window for the resource.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;undo-opt-in&lt;/code&gt; - Cancel any existing &lt;code&gt;next-maintenance&lt;/code&gt; opt-in requests.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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

    Copies the specified DB cluster parameter group.

    :param source_db_cluster_parameter_group_identifier: &lt;p&gt;The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\&quot;&gt; Constructing an Amazon Resource Name (ARN)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must specify a valid DB cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source DB cluster parameter group is in the same Amazon Region as the copy, specify a valid DB parameter group identifier, for example &lt;code&gt;my-db-cluster-param-group&lt;/code&gt;, or a valid ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source DB parameter group is in a different Amazon Region than the copy, specify a valid DB cluster parameter group ARN, for example &lt;code&gt;arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_db_cluster_parameter_group_identifier: str
    :param target_db_cluster_parameter_group_identifier: &lt;p&gt;The identifier for the copied DB cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cannot be null, empty, or blank&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 255 letters, numbers, or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster-param-group1&lt;/code&gt; &lt;/p&gt;
    :type target_db_cluster_parameter_group_identifier: str
    :param target_db_cluster_parameter_group_description: A description for the copied DB cluster parameter group.
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
    :param tags: The tags to be assigned to the copied DB cluster parameter group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_copy_db_cluster_snapshot(request: web.Request, source_db_cluster_snapshot_identifier, target_db_cluster_snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, kms_key_id=None, pre_signed_url=None, copy_tags=None, tags=None) -> web.Response:
    """g_et_copy_db_cluster_snapshot

    &lt;p&gt;Copies a snapshot of a DB cluster.&lt;/p&gt; &lt;p&gt;To copy a DB cluster snapshot from a shared manual DB cluster snapshot, &lt;code&gt;SourceDBClusterSnapshotIdentifier&lt;/code&gt; must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.&lt;/p&gt;

    :param source_db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the DB cluster snapshot to copy. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must specify a valid system snapshot in the \&quot;available\&quot; state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify a valid DB snapshot identifier.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster-snapshot1&lt;/code&gt; &lt;/p&gt;
    :type source_db_cluster_snapshot_identifier: str
    :param target_db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the new DB cluster snapshot to create from the source DB cluster snapshot. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster-snapshot2&lt;/code&gt; &lt;/p&gt;
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
    :param kms_key_id: &lt;p&gt;The Amazon Amazon KMS key ID for an encrypted DB cluster snapshot. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.&lt;/p&gt; &lt;p&gt;If you copy an encrypted DB cluster snapshot from your Amazon account, you can specify a value for &lt;code&gt;KmsKeyId&lt;/code&gt; to encrypt the copy with a new KMS encryption key. If you don&#39;t specify a value for &lt;code&gt;KmsKeyId&lt;/code&gt;, then the copy of the DB cluster snapshot is encrypted with the same KMS key as the source DB cluster snapshot.&lt;/p&gt; &lt;p&gt;If you copy an encrypted DB cluster snapshot that is shared from another Amazon account, then you must specify a value for &lt;code&gt;KmsKeyId&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; KMS encryption keys are specific to the Amazon Region that they are created in, and you can&#39;t use encryption keys from one Amazon Region in another Amazon Region.&lt;/p&gt; &lt;p&gt;You cannot encrypt an unencrypted DB cluster snapshot when you copy it. If you try to copy an unencrypted DB cluster snapshot and specify a value for the KmsKeyId parameter, an error is returned.&lt;/p&gt;
    :type kms_key_id: str
    :param pre_signed_url: Not currently supported.
    :type pre_signed_url: str
    :param copy_tags: True to copy all tags from the source DB cluster snapshot to the target DB cluster snapshot, and otherwise false. The default is false.
    :type copy_tags: bool
    :param tags: The tags to assign to the new DB cluster snapshot copy.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_copy_db_parameter_group(request: web.Request, source_db_parameter_group_identifier, target_db_parameter_group_identifier, target_db_parameter_group_description, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_copy_db_parameter_group

    Copies the specified DB parameter group.

    :param source_db_parameter_group_identifier: &lt;p&gt;The identifier or ARN for the source DB parameter group. For information about creating an ARN, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\&quot;&gt; Constructing an Amazon Resource Name (ARN)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must specify a valid DB parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must specify a valid DB parameter group identifier, for example &lt;code&gt;my-db-param-group&lt;/code&gt;, or a valid ARN.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_db_parameter_group_identifier: str
    :param target_db_parameter_group_identifier: &lt;p&gt;The identifier for the copied DB parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cannot be null, empty, or blank.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 255 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-db-parameter-group&lt;/code&gt; &lt;/p&gt;
    :type target_db_parameter_group_identifier: str
    :param target_db_parameter_group_description: A description for the copied DB parameter group.
    :type target_db_parameter_group_description: str
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
    :param tags: The tags to be assigned to the copied DB parameter group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_cluster(request: web.Request, db_cluster_identifier, engine, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, availability_zones=None, backup_retention_period=None, character_set_name=None, copy_tags_to_snapshot=None, database_name=None, db_cluster_parameter_group_name=None, vpc_security_group_ids=None, db_subnet_group_name=None, engine_version=None, port=None, master_username=None, master_user_password=None, option_group_name=None, preferred_backup_window=None, preferred_maintenance_window=None, replication_source_identifier=None, tags=None, storage_encrypted=None, kms_key_id=None, pre_signed_url=None, enable_iam_database_authentication=None, enable_cloudwatch_logs_exports=None, deletion_protection=None, serverless_v2_scaling_configuration=None, global_cluster_identifier=None) -> web.Response:
    """g_et_create_db_cluster

    &lt;p&gt;Creates a new Amazon Neptune DB cluster.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;ReplicationSourceIdentifier&lt;/code&gt; parameter to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune DB instance.&lt;/p&gt; &lt;p&gt;Note that when you create a new cluster using &lt;code&gt;CreateDBCluster&lt;/code&gt; directly, deletion protection is disabled by default (when you create a new production cluster in the console, deletion protection is enabled by default). You can only delete a DB cluster if its &lt;code&gt;DeletionProtection&lt;/code&gt; field is set to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt;

    :param db_cluster_identifier: &lt;p&gt;The DB cluster identifier. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster1&lt;/code&gt; &lt;/p&gt;
    :type db_cluster_identifier: str
    :param engine: &lt;p&gt;The name of the database engine to be used for this DB cluster.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;neptune&lt;/code&gt; &lt;/p&gt;
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
    :param availability_zones: A list of EC2 Availability Zones that instances in the DB cluster can be created in.
    :type availability_zones: List[]
    :param backup_retention_period: &lt;p&gt;The number of days for which automated backups are retained. You must specify a minimum value of 1.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be a value from 1 to 35&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type backup_retention_period: int
    :param character_set_name:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type character_set_name: str
    :param copy_tags_to_snapshot:  &lt;i&gt;If set to &lt;code&gt;true&lt;/code&gt;, tags are copied to any snapshot of the DB cluster that is created.&lt;/i&gt; 
    :type copy_tags_to_snapshot: bool
    :param database_name: The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon Neptune will not create a database in the DB cluster you are creating.
    :type database_name: str
    :param db_cluster_parameter_group_name: &lt;p&gt; The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, the default is used.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBClusterParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_parameter_group_name: str
    :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this DB cluster.
    :type vpc_security_group_ids: List[]
    :param db_subnet_group_name: &lt;p&gt;A DB subnet group to associate with this DB cluster.&lt;/p&gt; &lt;p&gt;Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param engine_version: &lt;p&gt;The version number of the database engine to use for the new DB cluster.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;1.0.2.1&lt;/code&gt; &lt;/p&gt;
    :type engine_version: str
    :param port: &lt;p&gt;The port number on which the instances in the DB cluster accept connections.&lt;/p&gt; &lt;p&gt; Default: &lt;code&gt;8182&lt;/code&gt; &lt;/p&gt;
    :type port: int
    :param master_username: Not supported by Neptune.
    :type master_username: str
    :param master_user_password: Not supported by Neptune.
    :type master_user_password: str
    :param option_group_name:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type option_group_name: str
    :param preferred_backup_window: &lt;p&gt;The daily time range during which automated backups are created if automated backups are enabled using the &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region. To see the time blocks available, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html\&quot;&gt; Adjusting the Preferred Maintenance Window&lt;/a&gt; in the &lt;i&gt;Amazon Neptune User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be in the format &lt;code&gt;hh24:mi-hh24:mi&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not conflict with the preferred maintenance window.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be at least 30 minutes.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type preferred_backup_window: str
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week. To see the time blocks available, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html\&quot;&gt; Adjusting the Preferred Maintenance Window&lt;/a&gt; in the &lt;i&gt;Amazon Neptune User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param replication_source_identifier: The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
    :type replication_source_identifier: str
    :param tags: The tags to assign to the new DB cluster.
    :type tags: list | bytes
    :param storage_encrypted: Specifies whether the DB cluster is encrypted.
    :type storage_encrypted: bool
    :param kms_key_id: &lt;p&gt;The Amazon KMS key identifier for an encrypted DB cluster.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.&lt;/p&gt; &lt;p&gt;If an encryption key is not specified in &lt;code&gt;KmsKeyId&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;ReplicationSourceIdentifier&lt;/code&gt; identifies an encrypted source, then Amazon Neptune will use the encryption key used to encrypt the source. Otherwise, Amazon Neptune will use your default encryption key.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the &lt;code&gt;StorageEncrypted&lt;/code&gt; parameter is true and &lt;code&gt;ReplicationSourceIdentifier&lt;/code&gt; is not specified, then Amazon Neptune will use your default encryption key.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Amazon KMS creates the default encryption key for your Amazon account. Your Amazon account has a different default encryption key for each Amazon Region.&lt;/p&gt; &lt;p&gt;If you create a Read Replica of an encrypted DB cluster in another Amazon Region, you must set &lt;code&gt;KmsKeyId&lt;/code&gt; to a KMS key ID that is valid in the destination Amazon Region. This key is used to encrypt the Read Replica in that Amazon Region.&lt;/p&gt;
    :type kms_key_id: str
    :param pre_signed_url: This parameter is not currently supported.
    :type pre_signed_url: str
    :param enable_iam_database_authentication: &lt;p&gt;If set to &lt;code&gt;true&lt;/code&gt;, enables Amazon Identity and Access Management (IAM) authentication for the entire DB cluster (this cannot be set at an instance level).&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt;
    :type enable_iam_database_authentication: bool
    :param enable_cloudwatch_logs_exports: The list of log types that need to be enabled for exporting to CloudWatch Logs.
    :type enable_cloudwatch_logs_exports: List[str]
    :param deletion_protection: A value that indicates whether the DB cluster has deletion protection enabled. The database can&#39;t be deleted when deletion protection is enabled. By default, deletion protection is enabled.
    :type deletion_protection: bool
    :param serverless_v2_scaling_configuration: 
    :type serverless_v2_scaling_configuration: dict | bytes
    :param global_cluster_identifier: The ID of the Neptune global database to which this new DB cluster should be added.
    :type global_cluster_identifier: str

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    serverless_v2_scaling_configuration = .from_dict(serverless_v2_scaling_configuration)
    return web.Response(status=200)


async def g_et_create_db_cluster_endpoint(request: web.Request, db_cluster_identifier, db_cluster_endpoint_identifier, endpoint_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, static_members=None, excluded_members=None, tags=None) -> web.Response:
    """g_et_create_db_cluster_endpoint

    Creates a new custom endpoint and associates it with an Amazon Neptune DB cluster.

    :param db_cluster_identifier: The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.
    :type db_cluster_identifier: str
    :param db_cluster_endpoint_identifier: The identifier to use for the new endpoint. This parameter is stored as a lowercase string.
    :type db_cluster_endpoint_identifier: str
    :param endpoint_type: The type of the endpoint. One of: &lt;code&gt;READER&lt;/code&gt;, &lt;code&gt;WRITER&lt;/code&gt;, &lt;code&gt;ANY&lt;/code&gt;.
    :type endpoint_type: str
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
    :param static_members: List of DB instance identifiers that are part of the custom endpoint group.
    :type static_members: List[str]
    :param excluded_members: List of DB instance identifiers that aren&#39;t part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.
    :type excluded_members: List[str]
    :param tags: The tags to be assigned to the Amazon Neptune resource.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_cluster_parameter_group(request: web.Request, db_cluster_parameter_group_name, db_parameter_group_family, description, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_db_cluster_parameter_group

    &lt;p&gt;Creates a new DB cluster parameter group.&lt;/p&gt; &lt;p&gt;Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.&lt;/p&gt; &lt;p&gt; A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after creating it using &lt;a&gt;ModifyDBClusterParameterGroup&lt;/a&gt;. Once you&#39;ve created a DB cluster parameter group, you need to associate it with your DB cluster using &lt;a&gt;ModifyDBCluster&lt;/a&gt;. When you associate a new DB cluster parameter group with a running DB cluster, you need to reboot the DB instances in the DB cluster without failover for the new DB cluster parameter group and associated settings to take effect.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the DB cluster parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/rds/\&quot;&gt;Amazon Neptune console&lt;/a&gt; or the &lt;a&gt;DescribeDBClusterParameters&lt;/a&gt; command to verify that your DB cluster parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

    :param db_cluster_parameter_group_name: &lt;p&gt;The name of the DB cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the name of an existing DBClusterParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;This value is stored as a lowercase string.&lt;/p&gt; &lt;/note&gt;
    :type db_cluster_parameter_group_name: str
    :param db_parameter_group_family: The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a database engine and engine version compatible with that DB cluster parameter group family.
    :type db_parameter_group_family: str
    :param description: The description for the DB cluster parameter group.
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
    :param tags: The tags to be assigned to the new DB cluster parameter group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_cluster_snapshot(request: web.Request, db_cluster_snapshot_identifier, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_db_cluster_snapshot

    Creates a snapshot of a DB cluster.

    :param db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster1-snapshot1&lt;/code&gt; &lt;/p&gt;
    :type db_cluster_snapshot_identifier: str
    :param db_cluster_identifier: &lt;p&gt;The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing DBCluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster1&lt;/code&gt; &lt;/p&gt;
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
    :param tags: The tags to be assigned to the DB cluster snapshot.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_instance(request: web.Request, db_instance_identifier, db_instance_class, engine, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_name=None, allocated_storage=None, master_username=None, master_user_password=None, db_security_groups=None, vpc_security_group_ids=None, availability_zone=None, db_subnet_group_name=None, preferred_maintenance_window=None, db_parameter_group_name=None, backup_retention_period=None, preferred_backup_window=None, port=None, multi_az=None, engine_version=None, auto_minor_version_upgrade=None, license_model=None, iops=None, option_group_name=None, character_set_name=None, publicly_accessible=None, tags=None, storage_type=None, tde_credential_arn=None, tde_credential_password=None, storage_encrypted=None, kms_key_id=None, domain=None, copy_tags_to_snapshot=None, monitoring_interval=None, monitoring_role_arn=None, domain_iam_role_name=None, promotion_tier=None, timezone=None, enable_iam_database_authentication=None, enable_performance_insights=None, performance_insights_kms_key_id=None, enable_cloudwatch_logs_exports=None, deletion_protection=None) -> web.Response:
    """g_et_create_db_instance

    Creates a new DB instance.

    :param db_instance_identifier: &lt;p&gt;The DB instance identifier. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;mydbinstance&lt;/code&gt; &lt;/p&gt;
    :type db_instance_identifier: str
    :param db_instance_class: The compute and memory capacity of the DB instance, for example, &lt;code&gt;db.m4.large&lt;/code&gt;. Not all DB instance classes are available in all Amazon Regions.
    :type db_instance_class: str
    :param engine: &lt;p&gt;The name of the database engine to be used for this instance.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;neptune&lt;/code&gt; &lt;/p&gt;
    :type engine: str
    :param db_cluster_identifier: &lt;p&gt;The identifier of the DB cluster that the instance will belong to.&lt;/p&gt; &lt;p&gt;For information on creating a DB cluster, see &lt;a&gt;CreateDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Type: String&lt;/p&gt;
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
    :param db_name: Not supported.
    :type db_name: str
    :param allocated_storage: Not supported by Neptune.
    :type allocated_storage: int
    :param master_username: Not supported by Neptune.
    :type master_username: str
    :param master_user_password: Not supported by Neptune.
    :type master_user_password: str
    :param db_security_groups: &lt;p&gt;A list of DB security groups to associate with this DB instance.&lt;/p&gt; &lt;p&gt;Default: The default DB security group for the database engine.&lt;/p&gt;
    :type db_security_groups: List[]
    :param vpc_security_group_ids: &lt;p&gt;A list of EC2 VPC security groups to associate with this DB instance.&lt;/p&gt; &lt;p&gt;Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see &lt;a&gt;CreateDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Default: The default EC2 VPC security group for the DB subnet group&#39;s VPC.&lt;/p&gt;
    :type vpc_security_group_ids: List[]
    :param availability_zone: &lt;p&gt; The EC2 Availability Zone that the DB instance is created in&lt;/p&gt; &lt;p&gt;Default: A random, system-chosen Availability Zone in the endpoint&#39;s Amazon Region.&lt;/p&gt; &lt;p&gt; Example: &lt;code&gt;us-east-1d&lt;/code&gt; &lt;/p&gt; &lt;p&gt; Constraint: The AvailabilityZone parameter can&#39;t be specified if the MultiAZ parameter is set to &lt;code&gt;true&lt;/code&gt;. The specified Availability Zone must be in the same Amazon Region as the current endpoint.&lt;/p&gt;
    :type availability_zone: str
    :param db_subnet_group_name: &lt;p&gt;A DB subnet group to associate with this DB instance.&lt;/p&gt; &lt;p&gt;If there is no DB subnet group, then it is a non-VPC DB instance.&lt;/p&gt;
    :type db_subnet_group_name: str
    :param preferred_maintenance_window: &lt;p&gt;The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt; Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week.&lt;/p&gt; &lt;p&gt;Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param db_parameter_group_name: &lt;p&gt;The name of the DB parameter group to associate with this DB instance. If this argument is omitted, the default DBParameterGroup for the specified engine is used.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_name: str
    :param backup_retention_period: &lt;p&gt;The number of days for which automated backups are retained.&lt;/p&gt; &lt;p&gt;Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see &lt;a&gt;CreateDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be a value from 0 to 35&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be set to 0 if the DB instance is a source to Read Replicas&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type backup_retention_period: int
    :param preferred_backup_window: &lt;p&gt; The daily time range during which automated backups are created.&lt;/p&gt; &lt;p&gt;Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see &lt;a&gt;CreateDBCluster&lt;/a&gt;.&lt;/p&gt;
    :type preferred_backup_window: str
    :param port: &lt;p&gt;The port number on which the database accepts connections.&lt;/p&gt; &lt;p&gt;Not applicable. The port is managed by the DB cluster. For more information, see &lt;a&gt;CreateDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; Default: &lt;code&gt;8182&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Type: Integer&lt;/p&gt;
    :type port: int
    :param multi_az: Specifies if the DB instance is a Multi-AZ deployment. You can&#39;t set the AvailabilityZone parameter if the MultiAZ parameter is set to true.
    :type multi_az: bool
    :param engine_version: The version number of the database engine to use. Currently, setting this parameter has no effect.
    :type engine_version: str
    :param auto_minor_version_upgrade: &lt;p&gt;Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;true&lt;/code&gt; &lt;/p&gt;
    :type auto_minor_version_upgrade: bool
    :param license_model: &lt;p&gt;License model information for this DB instance.&lt;/p&gt; &lt;p&gt; Valid values: &lt;code&gt;license-included&lt;/code&gt; | &lt;code&gt;bring-your-own-license&lt;/code&gt; | &lt;code&gt;general-public-license&lt;/code&gt; &lt;/p&gt;
    :type license_model: str
    :param iops: The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.
    :type iops: int
    :param option_group_name:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type option_group_name: str
    :param character_set_name:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type character_set_name: str
    :param publicly_accessible: This flag should no longer be used.
    :type publicly_accessible: bool
    :param tags: The tags to assign to the new instance.
    :type tags: list | bytes
    :param storage_type: &lt;p&gt;Specifies the storage type to be associated with the DB instance.&lt;/p&gt; &lt;p&gt;Not applicable. Storage is managed by the DB Cluster.&lt;/p&gt;
    :type storage_type: str
    :param tde_credential_arn: The ARN from the key store with which to associate the instance for TDE encryption.
    :type tde_credential_arn: str
    :param tde_credential_password: The password for the given ARN from the key store in order to access the device.
    :type tde_credential_password: str
    :param storage_encrypted: &lt;p&gt;Specifies whether the DB instance is encrypted.&lt;/p&gt; &lt;p&gt;Not applicable. The encryption for DB instances is managed by the DB cluster. For more information, see &lt;a&gt;CreateDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Default: false&lt;/p&gt;
    :type storage_encrypted: bool
    :param kms_key_id: &lt;p&gt;The Amazon KMS key identifier for an encrypted DB instance.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB instance with the same Amazon account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.&lt;/p&gt; &lt;p&gt;Not applicable. The KMS key identifier is managed by the DB cluster. For more information, see &lt;a&gt;CreateDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;StorageEncrypted&lt;/code&gt; parameter is true, and you do not specify a value for the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter, then Amazon Neptune will use your default encryption key. Amazon KMS creates the default encryption key for your Amazon account. Your Amazon account has a different default encryption key for each Amazon Region.&lt;/p&gt;
    :type kms_key_id: str
    :param domain: Specify the Active Directory Domain to create the instance in.
    :type domain: str
    :param copy_tags_to_snapshot: True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.
    :type copy_tags_to_snapshot: bool
    :param monitoring_interval: &lt;p&gt;The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;MonitoringRoleArn&lt;/code&gt; is specified, then you must also set &lt;code&gt;MonitoringInterval&lt;/code&gt; to a value other than 0.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;0, 1, 5, 10, 15, 30, 60&lt;/code&gt; &lt;/p&gt;
    :type monitoring_interval: int
    :param monitoring_role_arn: &lt;p&gt;The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, &lt;code&gt;arn:aws:iam:123456789012:role/emaccess&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;MonitoringInterval&lt;/code&gt; is set to a value other than 0, then you must supply a &lt;code&gt;MonitoringRoleArn&lt;/code&gt; value.&lt;/p&gt;
    :type monitoring_role_arn: str
    :param domain_iam_role_name: Specify the name of the IAM role to be used when making API calls to the Directory Service.
    :type domain_iam_role_name: str
    :param promotion_tier: &lt;p&gt;A value that specifies the order in which an Read Replica is promoted to the primary instance after a failure of the existing primary instance. &lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Valid Values: 0 - 15&lt;/p&gt;
    :type promotion_tier: int
    :param timezone: The time zone of the DB instance.
    :type timezone: str
    :param enable_iam_database_authentication: Not supported by Neptune (ignored).
    :type enable_iam_database_authentication: bool
    :param enable_performance_insights:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type enable_performance_insights: bool
    :param performance_insights_kms_key_id:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type performance_insights_kms_key_id: str
    :param enable_cloudwatch_logs_exports: The list of log types that need to be enabled for exporting to CloudWatch Logs.
    :type enable_cloudwatch_logs_exports: List[str]
    :param deletion_protection: &lt;p&gt;A value that indicates whether the DB instance has deletion protection enabled. The database can&#39;t be deleted when deletion protection is enabled. By default, deletion protection is disabled. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html\&quot;&gt;Deleting a DB Instance&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;DB instances in a DB cluster can be deleted even when deletion protection is enabled in their parent DB cluster.&lt;/p&gt;
    :type deletion_protection: bool

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_parameter_group(request: web.Request, db_parameter_group_name, db_parameter_group_family, description, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_db_parameter_group

    &lt;p&gt;Creates a new DB parameter group.&lt;/p&gt; &lt;p&gt;A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using &lt;i&gt;ModifyDBParameterGroup&lt;/i&gt;. Once you&#39;ve created a DB parameter group, you need to associate it with your DB instance using &lt;i&gt;ModifyDBInstance&lt;/i&gt;. When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After you create a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the Amazon Neptune console or the &lt;i&gt;DescribeDBParameters&lt;/i&gt; command to verify that your DB parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

    :param db_parameter_group_name: &lt;p&gt;The name of the DB parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;This value is stored as a lowercase string.&lt;/p&gt; &lt;/note&gt;
    :type db_parameter_group_name: str
    :param db_parameter_group_family: The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.
    :type db_parameter_group_family: str
    :param description: The description for the DB parameter group.
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
    :param tags: The tags to be assigned to the new DB parameter group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_db_subnet_group(request: web.Request, db_subnet_group_name, db_subnet_group_description, subnet_ids, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_db_subnet_group

    Creates a new DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the Amazon Region.

    :param db_subnet_group_name: &lt;p&gt;The name for the DB subnet group. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param db_subnet_group_description: The description for the DB subnet group.
    :type db_subnet_group_description: str
    :param subnet_ids: The EC2 Subnet IDs for the DB subnet group.
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
    :param tags: The tags to be assigned to the new DB subnet group.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_event_subscription(request: web.Request, subscription_name, sns_topic_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_type=None, event_categories=None, source_ids=None, enabled=None, tags=None) -> web.Response:
    """g_et_create_event_subscription

    &lt;p&gt;Creates an event notification subscription. This action requires a topic ARN (Amazon Resource Name) created by either the Neptune console, the SNS console, or the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.&lt;/p&gt; &lt;p&gt;You can specify the type of source (SourceType) you want to be notified of, provide a list of Neptune sources (SourceIds) that triggers the events, and provide a list of event categories (EventCategories) for events you want to be notified of. For example, you can specify SourceType &#x3D; db-instance, SourceIds &#x3D; mydbinstance1, mydbinstance2 and EventCategories &#x3D; Availability, Backup.&lt;/p&gt; &lt;p&gt;If you specify both the SourceType and SourceIds, such as SourceType &#x3D; db-instance and SourceIdentifier &#x3D; myDBInstance1, you are notified of all the db-instance events for the specified source. If you specify a SourceType but do not specify a SourceIdentifier, you receive notice of the events for that source type for all your Neptune sources. If you do not specify either the SourceType nor the SourceIdentifier, you are notified of events generated from all Neptune sources belonging to your customer account.&lt;/p&gt;

    :param subscription_name: &lt;p&gt;The name of the subscription.&lt;/p&gt; &lt;p&gt;Constraints: The name must be less than 255 characters.&lt;/p&gt;
    :type subscription_name: str
    :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
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
    :param source_type: &lt;p&gt;The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;db-instance&lt;/code&gt; | &lt;code&gt;db-cluster&lt;/code&gt; | &lt;code&gt;db-parameter-group&lt;/code&gt; | &lt;code&gt;db-security-group&lt;/code&gt; | &lt;code&gt;db-snapshot&lt;/code&gt; | &lt;code&gt;db-cluster-snapshot&lt;/code&gt; &lt;/p&gt;
    :type source_type: str
    :param event_categories:  A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the &lt;b&gt;DescribeEventCategories&lt;/b&gt; action.
    :type event_categories: List[]
    :param source_ids: &lt;p&gt;The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can&#39;t end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If SourceIds are supplied, SourceType must also be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB instance, then a &lt;code&gt;DBInstanceIdentifier&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB security group, a &lt;code&gt;DBSecurityGroupName&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB parameter group, a &lt;code&gt;DBParameterGroupName&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is a DB snapshot, a &lt;code&gt;DBSnapshotIdentifier&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_ids: List[]
    :param enabled:  A Boolean value; set to &lt;b&gt;true&lt;/b&gt; to activate the subscription, set to &lt;b&gt;false&lt;/b&gt; to create the subscription but not active it.
    :type enabled: bool
    :param tags: The tags to be applied to the new event subscription.
    :type tags: list | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_global_cluster(request: web.Request, global_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_db_cluster_identifier=None, engine=None, engine_version=None, deletion_protection=None, storage_encrypted=None) -> web.Response:
    """g_et_create_global_cluster

    &lt;p&gt;Creates a Neptune global database spread across multiple Amazon Regions. The global database contains a single primary cluster with read-write capability, and read-only secondary clusters that receive data from the primary cluster through high-speed replication performed by the Neptune storage subsystem.&lt;/p&gt; &lt;p&gt;You can create a global database that is initially empty, and then add a primary cluster and secondary clusters to it, or you can specify an existing Neptune cluster during the create operation to become the primary cluster of the global database.&lt;/p&gt;

    :param global_cluster_identifier: The cluster identifier of the new global database cluster.
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
    :param source_db_cluster_identifier: (&lt;i&gt;Optional&lt;/i&gt;) The Amazon Resource Name (ARN) of an existing Neptune DB cluster to use as the primary cluster of the new global database.
    :type source_db_cluster_identifier: str
    :param engine: &lt;p&gt;The name of the database engine to be used in the global database.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;neptune&lt;/code&gt; &lt;/p&gt;
    :type engine: str
    :param engine_version: &lt;p&gt;The Neptune engine version to be used by the global database.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;1.2.0.0&lt;/code&gt; or above.&lt;/p&gt;
    :type engine_version: str
    :param deletion_protection: The deletion protection setting for the new global database. The global database can&#39;t be deleted when deletion protection is enabled.
    :type deletion_protection: bool
    :param storage_encrypted: The storage encryption setting for the new global database cluster.
    :type storage_encrypted: bool

    """
    return web.Response(status=200)


async def g_et_delete_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_final_snapshot=None, final_db_snapshot_identifier=None) -> web.Response:
    """g_et_delete_db_cluster

    &lt;p&gt;The DeleteDBCluster action deletes a previously provisioned DB cluster. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can&#39;t be recovered. Manual DB cluster snapshots of the specified DB cluster are not deleted.&lt;/p&gt; &lt;p&gt;Note that the DB Cluster cannot be deleted if deletion protection is enabled. To delete it, you must first set its &lt;code&gt;DeletionProtection&lt;/code&gt; field to &lt;code&gt;False&lt;/code&gt;.&lt;/p&gt;

    :param db_cluster_identifier: &lt;p&gt;The DB cluster identifier for the DB cluster to be deleted. This parameter isn&#39;t case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match an existing DBClusterIdentifier.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param skip_final_snapshot: &lt;p&gt; Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If &lt;code&gt;true&lt;/code&gt; is specified, no DB cluster snapshot is created. If &lt;code&gt;false&lt;/code&gt; is specified, a DB cluster snapshot is created before the DB cluster is deleted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You must specify a &lt;code&gt;FinalDBSnapshotIdentifier&lt;/code&gt; parameter if &lt;code&gt;SkipFinalSnapshot&lt;/code&gt; is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type skip_final_snapshot: bool
    :param final_db_snapshot_identifier: &lt;p&gt; The DB cluster snapshot identifier of the new DB cluster snapshot created when &lt;code&gt;SkipFinalSnapshot&lt;/code&gt; is set to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; Specifying this parameter and also setting the &lt;code&gt;SkipFinalShapshot&lt;/code&gt; parameter to true results in an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type final_db_snapshot_identifier: str

    """
    return web.Response(status=200)


async def g_et_delete_db_cluster_endpoint(request: web.Request, db_cluster_endpoint_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_db_cluster_endpoint

    Deletes a custom endpoint and removes it from an Amazon Neptune DB cluster.

    :param db_cluster_endpoint_identifier: The identifier associated with the custom endpoint. This parameter is stored as a lowercase string.
    :type db_cluster_endpoint_identifier: str
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


async def g_et_delete_db_cluster_parameter_group(request: web.Request, db_cluster_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_db_cluster_parameter_group

    Deletes a specified DB cluster parameter group. The DB cluster parameter group to be deleted can&#39;t be associated with any DB clusters.

    :param db_cluster_parameter_group_name: &lt;p&gt;The name of the DB cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be the name of an existing DB cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t delete a default DB cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be associated with any DB clusters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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

    &lt;p&gt;Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The DB cluster snapshot must be in the &lt;code&gt;available&lt;/code&gt; state to be deleted.&lt;/p&gt; &lt;/note&gt;

    :param db_cluster_snapshot_identifier: &lt;p&gt;The identifier of the DB cluster snapshot to delete.&lt;/p&gt; &lt;p&gt;Constraints: Must be the name of an existing DB cluster snapshot in the &lt;code&gt;available&lt;/code&gt; state.&lt;/p&gt;
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


async def g_et_delete_db_instance(request: web.Request, db_instance_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_final_snapshot=None, final_db_snapshot_identifier=None) -> web.Response:
    """g_et_delete_db_instance

    &lt;p&gt;The DeleteDBInstance action deletes a previously provisioned DB instance. When you delete a DB instance, all automated backups for that instance are deleted and can&#39;t be recovered. Manual DB snapshots of the DB instance to be deleted by &lt;code&gt;DeleteDBInstance&lt;/code&gt; are not deleted.&lt;/p&gt; &lt;p&gt; If you request a final DB snapshot the status of the Amazon Neptune DB instance is &lt;code&gt;deleting&lt;/code&gt; until the DB snapshot is created. The API action &lt;code&gt;DescribeDBInstance&lt;/code&gt; is used to monitor the status of this operation. The action can&#39;t be canceled or reverted once submitted.&lt;/p&gt; &lt;p&gt;Note that when a DB instance is in a failure state and has a status of &lt;code&gt;failed&lt;/code&gt;, &lt;code&gt;incompatible-restore&lt;/code&gt;, or &lt;code&gt;incompatible-network&lt;/code&gt;, you can only delete it when the &lt;code&gt;SkipFinalSnapshot&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a DB instance if it is the only instance in the DB cluster, or if it has deletion protection enabled.&lt;/p&gt;

    :param db_instance_identifier: &lt;p&gt;The DB instance identifier for the DB instance to be deleted. This parameter isn&#39;t case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the name of an existing DB instance.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param skip_final_snapshot: &lt;p&gt; Determines whether a final DB snapshot is created before the DB instance is deleted. If &lt;code&gt;true&lt;/code&gt; is specified, no DBSnapshot is created. If &lt;code&gt;false&lt;/code&gt; is specified, a DB snapshot is created before the DB instance is deleted.&lt;/p&gt; &lt;p&gt;Note that when a DB instance is in a failure state and has a status of &#39;failed&#39;, &#39;incompatible-restore&#39;, or &#39;incompatible-network&#39;, it can only be deleted when the SkipFinalSnapshot parameter is set to \&quot;true\&quot;.&lt;/p&gt; &lt;p&gt;Specify &lt;code&gt;true&lt;/code&gt; when deleting a Read Replica.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The FinalDBSnapshotIdentifier parameter must be specified if SkipFinalSnapshot is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type skip_final_snapshot: bool
    :param final_db_snapshot_identifier: &lt;p&gt; The DBSnapshotIdentifier of the new DBSnapshot created when SkipFinalSnapshot is set to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Specifying this parameter and also setting the SkipFinalShapshot parameter to true results in an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 letters or numbers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be specified when deleting a Read Replica.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type final_db_snapshot_identifier: str

    """
    return web.Response(status=200)


async def g_et_delete_db_parameter_group(request: web.Request, db_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_db_parameter_group

    Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted can&#39;t be associated with any DB instances.

    :param db_parameter_group_name: &lt;p&gt;The name of the DB parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be the name of an existing DB parameter group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t delete a default DB parameter group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be associated with any DB instances&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_name: str
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

    &lt;p&gt;Deletes a DB subnet group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The specified database subnet group must not be associated with any DB instances.&lt;/p&gt; &lt;/note&gt;

    :param db_subnet_group_name: &lt;p&gt;The name of the database subnet group to delete.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete the default subnet group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;p&gt;Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
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

    Deletes an event notification subscription.

    :param subscription_name: The name of the event notification subscription you want to delete.
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

    Deletes a global database. The primary and all secondary clusters must already be detached or deleted first.

    :param global_cluster_identifier: The cluster identifier of the global database cluster being deleted.
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


async def g_et_describe_db_cluster_endpoints(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_identifier=None, db_cluster_endpoint_identifier=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_cluster_endpoints

    &lt;p&gt;Returns information about endpoints for an Amazon Neptune DB cluster.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation can also return information for Amazon RDS clusters and Amazon DocDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    :param db_cluster_identifier: The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.
    :type db_cluster_identifier: str
    :param db_cluster_endpoint_identifier: The identifier of the endpoint to describe. This parameter is stored as a lowercase string.
    :type db_cluster_endpoint_identifier: str
    :param filters: A set of name-value pairs that define which endpoints to include in the output. The filters are specified as name-value pairs, in the format &lt;code&gt;Name&#x3D;&lt;i&gt;endpoint_type&lt;/i&gt;,Values&#x3D;&lt;i&gt;endpoint_type1&lt;/i&gt;,&lt;i&gt;endpoint_type2&lt;/i&gt;,...&lt;/code&gt;. &lt;code&gt;Name&lt;/code&gt; can be one of: &lt;code&gt;db-cluster-endpoint-type&lt;/code&gt;, &lt;code&gt;db-cluster-endpoint-custom-type&lt;/code&gt;, &lt;code&gt;db-cluster-endpoint-id&lt;/code&gt;, &lt;code&gt;db-cluster-endpoint-status&lt;/code&gt;. &lt;code&gt;Values&lt;/code&gt; for the &lt;code&gt; db-cluster-endpoint-type&lt;/code&gt; filter can be one or more of: &lt;code&gt;reader&lt;/code&gt;, &lt;code&gt;writer&lt;/code&gt;, &lt;code&gt;custom&lt;/code&gt;. &lt;code&gt;Values&lt;/code&gt; for the &lt;code&gt;db-cluster-endpoint-custom-type&lt;/code&gt; filter can be one or more of: &lt;code&gt;reader&lt;/code&gt;, &lt;code&gt;any&lt;/code&gt;. &lt;code&gt;Values&lt;/code&gt; for the &lt;code&gt;db-cluster-endpoint-status&lt;/code&gt; filter can be one or more of: &lt;code&gt;available&lt;/code&gt;, &lt;code&gt;creating&lt;/code&gt;, &lt;code&gt;deleting&lt;/code&gt;, &lt;code&gt;inactive&lt;/code&gt;, &lt;code&gt;modifying&lt;/code&gt;. 
    :type filters: list | bytes
    :param max_records: &lt;p&gt;The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so you can retrieve the remaining results. &lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous &lt;code&gt;DescribeDBClusterEndpoints&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;. 
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_cluster_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_parameter_group_name=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_cluster_parameter_groups

     Returns a list of &lt;code&gt;DBClusterParameterGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; parameter is specified, the list will contain only the description of the specified DB cluster parameter group.

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
    :param db_cluster_parameter_group_name: &lt;p&gt;The name of a specific DB cluster parameter group to return details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBClusterParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_parameter_group_name: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous &lt;code&gt;DescribeDBClusterParameterGroups&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_cluster_parameters(request: web.Request, db_cluster_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_cluster_parameters

    Returns the detailed parameter list for a particular DB cluster parameter group.

    :param db_cluster_parameter_group_name: &lt;p&gt;The name of a specific DB cluster parameter group to return parameter details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBClusterParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous &lt;code&gt;DescribeDBClusterParameters&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;. 
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_cluster_snapshot_attributes(request: web.Request, db_cluster_snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_db_cluster_snapshot_attributes

    &lt;p&gt;Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.&lt;/p&gt; &lt;p&gt;When sharing snapshots with other Amazon accounts, &lt;code&gt;DescribeDBClusterSnapshotAttributes&lt;/code&gt; returns the &lt;code&gt;restore&lt;/code&gt; attribute and a list of IDs for the Amazon accounts that are authorized to copy or restore the manual DB cluster snapshot. If &lt;code&gt;all&lt;/code&gt; is included in the list of values for the &lt;code&gt;restore&lt;/code&gt; attribute, then the manual DB cluster snapshot is public and can be copied or restored by all Amazon accounts.&lt;/p&gt; &lt;p&gt;To add or remove access for an Amazon account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the &lt;a&gt;ModifyDBClusterSnapshotAttribute&lt;/a&gt; API action.&lt;/p&gt;

    :param db_cluster_snapshot_identifier: The identifier for the DB cluster snapshot to describe the attributes for.
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

    Returns information about DB cluster snapshots. This API action supports pagination.

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
    :param db_cluster_identifier: &lt;p&gt;The ID of the DB cluster to retrieve the list of DB cluster snapshots for. This parameter can&#39;t be used in conjunction with the &lt;code&gt;DBClusterSnapshotIdentifier&lt;/code&gt; parameter. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the identifier of an existing DBCluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param db_cluster_snapshot_identifier: &lt;p&gt;A specific DB cluster snapshot identifier to describe. This parameter can&#39;t be used in conjunction with the &lt;code&gt;DBClusterIdentifier&lt;/code&gt; parameter. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the identifier of an existing DBClusterSnapshot.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If this identifier is for an automated snapshot, the &lt;code&gt;SnapshotType&lt;/code&gt; parameter must also be specified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_snapshot_identifier: str
    :param snapshot_type: &lt;p&gt;The type of DB cluster snapshots to be returned. You can specify one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;automated&lt;/code&gt; - Return all DB cluster snapshots that have been automatically taken by Amazon Neptune for my Amazon account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;manual&lt;/code&gt; - Return all DB cluster snapshots that have been taken by my Amazon account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;shared&lt;/code&gt; - Return all manual DB cluster snapshots that have been shared to my Amazon account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public&lt;/code&gt; - Return all DB cluster snapshots that have been marked as public.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you don&#39;t specify a &lt;code&gt;SnapshotType&lt;/code&gt; value, then both automated and manual DB cluster snapshots are returned. You can include shared DB cluster snapshots with these results by setting the &lt;code&gt;IncludeShared&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;. You can include public DB cluster snapshots with these results by setting the &lt;code&gt;IncludePublic&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;IncludeShared&lt;/code&gt; and &lt;code&gt;IncludePublic&lt;/code&gt; parameters don&#39;t apply for &lt;code&gt;SnapshotType&lt;/code&gt; values of &lt;code&gt;manual&lt;/code&gt; or &lt;code&gt;automated&lt;/code&gt;. The &lt;code&gt;IncludePublic&lt;/code&gt; parameter doesn&#39;t apply when &lt;code&gt;SnapshotType&lt;/code&gt; is set to &lt;code&gt;shared&lt;/code&gt;. The &lt;code&gt;IncludeShared&lt;/code&gt; parameter doesn&#39;t apply when &lt;code&gt;SnapshotType&lt;/code&gt; is set to &lt;code&gt;public&lt;/code&gt;.&lt;/p&gt;
    :type snapshot_type: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt;The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeDBClusterSnapshots&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;. 
    :type marker: str
    :param include_shared: &lt;p&gt;True to include shared manual DB cluster snapshots from other Amazon accounts that this Amazon account has been given permission to copy or restore, and otherwise false. The default is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can give an Amazon account permission to restore a manual DB cluster snapshot from another Amazon account by the &lt;a&gt;ModifyDBClusterSnapshotAttribute&lt;/a&gt; API action.&lt;/p&gt;
    :type include_shared: bool
    :param include_public: &lt;p&gt;True to include manual DB cluster snapshots that are public and can be copied or restored by any Amazon account, and otherwise false. The default is &lt;code&gt;false&lt;/code&gt;. The default is false.&lt;/p&gt; &lt;p&gt;You can share a manual DB cluster snapshot as public by using the &lt;a&gt;ModifyDBClusterSnapshotAttribute&lt;/a&gt; API action.&lt;/p&gt;
    :type include_public: bool

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_identifier=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_clusters

    &lt;p&gt;Returns information about provisioned DB clusters, and supports pagination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation can also return information for Amazon RDS clusters and Amazon DocDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    :param db_cluster_identifier: &lt;p&gt;The user-supplied DB cluster identifier. If this parameter is specified, information from only the specific DB cluster is returned. This parameter isn&#39;t case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match an existing DBClusterIdentifier.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param filters: &lt;p&gt;A filter that specifies one or more DB clusters to describe.&lt;/p&gt; &lt;p&gt;Supported filters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-cluster-id&lt;/code&gt; - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB clusters identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;engine&lt;/code&gt; - Accepts an engine name (such as &lt;code&gt;neptune&lt;/code&gt;), and restricts the results list to DB clusters created by that engine.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For example, to invoke this API from the Amazon CLI and filter so that only Neptune DB clusters are returned, you could use the following command:&lt;/p&gt;
    :type filters: list | bytes
    :param max_records: &lt;p&gt;The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;a&gt;DescribeDBClusters&lt;/a&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_engine_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine=None, engine_version=None, db_parameter_group_family=None, filters=None, max_records=None, marker=None, default_only=None, list_supported_character_sets=None, list_supported_timezones=None) -> web.Response:
    """g_et_describe_db_engine_versions

    Returns a list of the available DB engines.

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
    :param engine_version: &lt;p&gt;The database engine version to return.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;5.1.49&lt;/code&gt; &lt;/p&gt;
    :type engine_version: str
    :param db_parameter_group_family: &lt;p&gt;The name of a specific DB parameter group family to return details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match an existing DBParameterGroupFamily.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_family: str
    :param filters: Not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more than the &lt;code&gt;MaxRecords&lt;/code&gt; value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str
    :param default_only: Indicates that only the default version of the specified engine or engine and major version combination is returned.
    :type default_only: bool
    :param list_supported_character_sets: If this parameter is specified and the requested engine supports the &lt;code&gt;CharacterSetName&lt;/code&gt; parameter for &lt;code&gt;CreateDBInstance&lt;/code&gt;, the response includes a list of supported character sets for each engine version.
    :type list_supported_character_sets: bool
    :param list_supported_timezones: If this parameter is specified and the requested engine supports the &lt;code&gt;TimeZone&lt;/code&gt; parameter for &lt;code&gt;CreateDBInstance&lt;/code&gt;, the response includes a list of supported time zones for each engine version.
    :type list_supported_timezones: bool

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_instance_identifier=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_instances

    &lt;p&gt;Returns information about provisioned instances, and supports pagination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation can also return information for Amazon RDS instances and Amazon DocDB instances.&lt;/p&gt; &lt;/note&gt;

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
    :param db_instance_identifier: &lt;p&gt;The user-supplied instance identifier. If this parameter is specified, information from only the specific DB instance is returned. This parameter isn&#39;t case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the identifier of an existing DBInstance.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_instance_identifier: str
    :param filters: &lt;p&gt;A filter that specifies one or more DB instances to describe.&lt;/p&gt; &lt;p&gt;Supported filters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-cluster-id&lt;/code&gt; - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include information about the DB instances associated with the DB clusters identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;engine&lt;/code&gt; - Accepts an engine name (such as &lt;code&gt;neptune&lt;/code&gt;), and restricts the results list to DB instances created by that engine.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For example, to invoke this API from the Amazon CLI and filter so that only Neptune DB instances are returned, you could use the following command:&lt;/p&gt;
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous &lt;code&gt;DescribeDBInstances&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_parameter_group_name=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_parameter_groups

    Returns a list of &lt;code&gt;DBParameterGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBParameterGroupName&lt;/code&gt; is specified, the list will contain only the description of the specified DB parameter group.

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
    :param db_parameter_group_name: &lt;p&gt;The name of a specific DB parameter group to return details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBClusterParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_name: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt;The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeDBParameterGroups&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_parameters(request: web.Request, db_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_parameters

    Returns the detailed parameter list for a particular DB parameter group.

    :param db_parameter_group_name: &lt;p&gt;The name of a specific DB parameter group to return details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_name: str
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
    :param source: &lt;p&gt;The parameter types to return.&lt;/p&gt; &lt;p&gt;Default: All parameter types returned&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;user | system | engine-default&lt;/code&gt; &lt;/p&gt;
    :type source: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt;The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeDBParameters&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_db_subnet_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_subnet_group_name=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_db_subnet_groups

    &lt;p&gt;Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is specified, the list will contain only the descriptions of the specified DBSubnetGroup.&lt;/p&gt; &lt;p&gt;For an overview of CIDR ranges, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\&quot;&gt;Wikipedia Tutorial&lt;/a&gt;.&lt;/p&gt;

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
    :param db_subnet_group_name: The name of the DB subnet group to return details for.
    :type db_subnet_group_name: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous DescribeDBSubnetGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_engine_default_cluster_parameters(request: web.Request, db_parameter_group_family, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_engine_default_cluster_parameters

    Returns the default engine and system parameter information for the cluster database engine.

    :param db_parameter_group_family: The name of the DB cluster parameter group family to return engine parameter information for.
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
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous &lt;code&gt;DescribeEngineDefaultClusterParameters&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_engine_default_parameters(request: web.Request, db_parameter_group_family, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_engine_default_parameters

    Returns the default engine and system parameter information for the specified database engine.

    :param db_parameter_group_family: The name of the DB parameter group family.
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
    :param filters: Not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous &lt;code&gt;DescribeEngineDefaultParameters&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
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
    :param source_type: &lt;p&gt;The type of source that is generating the events.&lt;/p&gt; &lt;p&gt;Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot&lt;/p&gt;
    :type source_type: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_event_subscriptions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, subscription_name=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_event_subscriptions

    &lt;p&gt;Lists all the subscription descriptions for a customer account. The description for a subscription includes SubscriptionName, SNSTopicARN, CustomerID, SourceType, SourceID, CreationTime, and Status.&lt;/p&gt; &lt;p&gt;If you specify a SubscriptionName, lists the description for that subscription.&lt;/p&gt;

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
    :param subscription_name: The name of the event notification subscription you want to describe.
    :type subscription_name: str
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt; .
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_identifier=None, source_type=None, start_time=None, end_time=None, duration=None, event_categories=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_events

    Returns events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days. Events specific to a particular DB instance, DB security group, database snapshot, or DB parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.

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
    :param source_identifier: &lt;p&gt;The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If SourceIdentifier is supplied, SourceType must also be provided.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBInstance&lt;/code&gt;, then a &lt;code&gt;DBInstanceIdentifier&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBSecurityGroup&lt;/code&gt;, a &lt;code&gt;DBSecurityGroupName&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBParameterGroup&lt;/code&gt;, a &lt;code&gt;DBParameterGroupName&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the source type is &lt;code&gt;DBSnapshot&lt;/code&gt;, a &lt;code&gt;DBSnapshotIdentifier&lt;/code&gt; must be supplied.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_identifier: str
    :param source_type: The event source to retrieve events for. If no value is specified, all events are returned.
    :type source_type: str
    :param start_time: &lt;p&gt; The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/ISO_8601\&quot;&gt;ISO8601 Wikipedia page.&lt;/a&gt; &lt;/p&gt; &lt;p&gt;Example: 2009-07-08T18:00Z&lt;/p&gt;
    :type start_time: str
    :param end_time: &lt;p&gt; The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/ISO_8601\&quot;&gt;ISO8601 Wikipedia page.&lt;/a&gt; &lt;/p&gt; &lt;p&gt;Example: 2009-07-08T18:00Z&lt;/p&gt;
    :type end_time: str
    :param duration: &lt;p&gt;The number of minutes to retrieve events for.&lt;/p&gt; &lt;p&gt;Default: 60&lt;/p&gt;
    :type duration: int
    :param event_categories: A list of event categories that trigger notifications for a event notification subscription.
    :type event_categories: List[]
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_global_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, global_cluster_identifier=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_global_clusters

    Returns information about Neptune global database clusters. This API supports pagination.

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
    :param global_cluster_identifier: &lt;p&gt;The user-supplied DB cluster identifier. If this parameter is specified, only information about the specified DB cluster is returned. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints: If supplied, must match an existing DB cluster identifier.&lt;/p&gt;
    :type global_cluster_identifier: str
    :param max_records: &lt;p&gt;The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination marker token is included in the response that you can use to retrieve the remaining results.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: (&lt;i&gt;Optional&lt;/i&gt;) A pagination token returned by a previous call to &lt;code&gt;DescribeGlobalClusters&lt;/code&gt;. If this parameter is specified, the response will only include records beyond the marker, up to the number specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_orderable_db_instance_options(request: web.Request, engine, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, engine_version=None, db_instance_class=None, license_model=None, vpc=None, filters=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_orderable_db_instance_options

    Returns a list of orderable DB instance options for the specified engine.

    :param engine: The name of the engine to retrieve DB instance options for.
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
    :param engine_version: The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.
    :type engine_version: str
    :param db_instance_class: The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.
    :type db_instance_class: str
    :param license_model: The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.
    :type license_model: str
    :param vpc: The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.
    :type vpc: bool
    :param filters: This parameter is not currently supported.
    :type filters: list | bytes
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker:  An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by &lt;code&gt;MaxRecords&lt;/code&gt; .
    :type marker: str

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_pending_maintenance_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, resource_identifier=None, filters=None, marker=None, max_records=None) -> web.Response:
    """g_et_describe_pending_maintenance_actions

    Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.

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
    :param filters: &lt;p&gt;A filter that specifies one or more resources to return pending maintenance actions for.&lt;/p&gt; &lt;p&gt;Supported filters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-cluster-id&lt;/code&gt; - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (ARNs). The results list will only include pending maintenance actions for the DB clusters identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;db-instance-id&lt;/code&gt; - Accepts DB instance identifiers and DB instance ARNs. The results list will only include pending maintenance actions for the DB instances identified by these ARNs.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type filters: list | bytes
    :param marker:  An optional pagination token provided by a previous &lt;code&gt;DescribePendingMaintenanceActions&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to a number of records specified by &lt;code&gt;MaxRecords&lt;/code&gt;.
    :type marker: str
    :param max_records: &lt;p&gt; The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.&lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: Minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int

    """
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_valid_db_instance_modifications(request: web.Request, db_instance_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_valid_db_instance_modifications

    You can call &lt;a&gt;DescribeValidDBInstanceModifications&lt;/a&gt; to learn what modifications you can make to your DB instance. You can use this information when you call &lt;a&gt;ModifyDBInstance&lt;/a&gt;.

    :param db_instance_identifier: The customer identifier or the ARN of your DB instance.
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


async def g_et_failover_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_cluster_identifier=None, target_db_instance_identifier=None) -> web.Response:
    """g_et_failover_db_cluster

    &lt;p&gt;Forces a failover for a DB cluster.&lt;/p&gt; &lt;p&gt;A failover for a DB cluster promotes one of the Read Replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).&lt;/p&gt; &lt;p&gt;Amazon Neptune will automatically fail over to a Read Replica, if one exists, when the primary instance fails. You can force a failover when you want to simulate a failure of a primary instance for testing. Because each instance in a DB cluster has its own endpoint address, you will need to clean up and re-establish any existing connections that use those endpoint addresses when the failover is complete.&lt;/p&gt;

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
    :param db_cluster_identifier: &lt;p&gt;A DB cluster identifier to force a failover for. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing DBCluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param target_db_instance_identifier: &lt;p&gt;The name of the instance to promote to the primary instance.&lt;/p&gt; &lt;p&gt;You must specify the instance identifier for an Read Replica in the DB cluster. For example, &lt;code&gt;mydbcluster-replica1&lt;/code&gt;.&lt;/p&gt;
    :type target_db_instance_identifier: str

    """
    return web.Response(status=200)


async def g_et_failover_global_cluster(request: web.Request, global_cluster_identifier, target_db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_failover_global_cluster

    &lt;p&gt;Initiates the failover process for a Neptune global database.&lt;/p&gt; &lt;p&gt;A failover for a Neptune global database promotes one of secondary read-only DB clusters to be the primary DB cluster and demotes the primary DB cluster to being a secondary (read-only) DB cluster. In other words, the role of the current primary DB cluster and the selected target secondary DB cluster are switched. The selected secondary DB cluster assumes full read/write capabilities for the Neptune global database.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action applies &lt;b&gt;only&lt;/b&gt; to Neptune global databases. This action is only intended for use on healthy Neptune global databases with healthy Neptune DB clusters and no region-wide outages, to test disaster recovery scenarios or to reconfigure the global database topology.&lt;/p&gt; &lt;/note&gt;

    :param global_cluster_identifier: &lt;p&gt;Identifier of the Neptune global database that should be failed over. The identifier is the unique key assigned by the user when the Neptune global database was created. In other words, it&#39;s the name of the global database that you want to fail over.&lt;/p&gt; &lt;p&gt;Constraints: Must match the identifier of an existing Neptune global database.&lt;/p&gt;
    :type global_cluster_identifier: str
    :param target_db_cluster_identifier: The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that you want to promote to primary for the global database.
    :type target_db_cluster_identifier: str
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


async def g_et_list_tags_for_resource(request: web.Request, resource_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None) -> web.Response:
    """g_et_list_tags_for_resource

    Lists all tags on an Amazon Neptune resource.

    :param resource_name: The Amazon Neptune resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\&quot;&gt; Constructing an Amazon Resource Name (ARN)&lt;/a&gt;.
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
    filters = [GETDescribeDBClusterEndpointsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_modify_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, new_db_cluster_identifier=None, apply_immediately=None, backup_retention_period=None, db_cluster_parameter_group_name=None, vpc_security_group_ids=None, port=None, master_user_password=None, option_group_name=None, preferred_backup_window=None, preferred_maintenance_window=None, enable_iam_database_authentication=None, cloudwatch_logs_export_configuration=None, engine_version=None, allow_major_version_upgrade=None, db_instance_parameter_group_name=None, deletion_protection=None, copy_tags_to_snapshot=None, serverless_v2_scaling_configuration=None) -> web.Response:
    """g_et_modify_db_cluster

    Modify a setting for a DB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.

    :param db_cluster_identifier: &lt;p&gt;The DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing DBCluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param new_db_cluster_identifier: &lt;p&gt;The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster2&lt;/code&gt; &lt;/p&gt;
    :type new_db_cluster_identifier: str
    :param apply_immediately: &lt;p&gt;A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the &lt;code&gt;PreferredMaintenanceWindow&lt;/code&gt; setting for the DB cluster. If this parameter is set to &lt;code&gt;false&lt;/code&gt;, changes to the DB cluster are applied during the next maintenance window.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter only affects &lt;code&gt;NewDBClusterIdentifier&lt;/code&gt; values. If you set the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter value to false, then changes to &lt;code&gt;NewDBClusterIdentifier&lt;/code&gt; values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type apply_immediately: bool
    :param backup_retention_period: &lt;p&gt;The number of days for which automated backups are retained. You must specify a minimum value of 1.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be a value from 1 to 35&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type backup_retention_period: int
    :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to use for the DB cluster.
    :type db_cluster_parameter_group_name: str
    :param vpc_security_group_ids: A list of VPC security groups that the DB cluster will belong to.
    :type vpc_security_group_ids: List[]
    :param port: &lt;p&gt;The port number on which the DB cluster accepts connections.&lt;/p&gt; &lt;p&gt;Constraints: Value must be &lt;code&gt;1150-65535&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default: The same port as the original DB cluster.&lt;/p&gt;
    :type port: int
    :param master_user_password: Not supported by Neptune.
    :type master_user_password: str
    :param option_group_name:  &lt;i&gt;Not supported by Neptune.&lt;/i&gt; 
    :type option_group_name: str
    :param preferred_backup_window: &lt;p&gt;The daily time range during which automated backups are created if automated backups are enabled, using the &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be in the format &lt;code&gt;hh24:mi-hh24:mi&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not conflict with the preferred maintenance window.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be at least 30 minutes.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type preferred_backup_window: str
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt;Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week.&lt;/p&gt; &lt;p&gt;Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param enable_iam_database_authentication: &lt;p&gt;True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type enable_iam_database_authentication: bool
    :param cloudwatch_logs_export_configuration: The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB cluster.
    :type cloudwatch_logs_export_configuration: dict | bytes
    :param engine_version: &lt;p&gt;The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter is set to true.&lt;/p&gt; &lt;p&gt;For a list of valid engine versions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html\&quot;&gt;Engine Releases for Amazon Neptune&lt;/a&gt;, or call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/userguide/api-other-apis.html#DescribeDBEngineVersions\&quot;&gt;DescribeDBEngineVersions&lt;/a&gt;.&lt;/p&gt;
    :type engine_version: str
    :param allow_major_version_upgrade: &lt;p&gt;A value that indicates whether upgrades between different major versions are allowed.&lt;/p&gt; &lt;p&gt;Constraints: You must set the allow-major-version-upgrade flag when providing an &lt;code&gt;EngineVersion&lt;/code&gt; parameter that uses a different major version than the DB cluster&#39;s current version.&lt;/p&gt;
    :type allow_major_version_upgrade: bool
    :param db_instance_parameter_group_name: &lt;p&gt;The name of the DB parameter group to apply to all instances of the DB cluster. &lt;/p&gt; &lt;note&gt; &lt;p&gt;When you apply a parameter group using &lt;code&gt;DBInstanceParameterGroupName&lt;/code&gt;, parameter changes aren&#39;t applied during the next maintenance window but instead are applied immediately.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Default: The existing name setting&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The DB parameter group must be in the same DB parameter group family as the target DB cluster version.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;DBInstanceParameterGroupName&lt;/code&gt; parameter is only valid in combination with the &lt;code&gt;AllowMajorVersionUpgrade&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_instance_parameter_group_name: str
    :param deletion_protection: A value that indicates whether the DB cluster has deletion protection enabled. The database can&#39;t be deleted when deletion protection is enabled. By default, deletion protection is disabled.
    :type deletion_protection: bool
    :param copy_tags_to_snapshot:  &lt;i&gt;If set to &lt;code&gt;true&lt;/code&gt;, tags are copied to any snapshot of the DB cluster that is created.&lt;/i&gt; 
    :type copy_tags_to_snapshot: bool
    :param serverless_v2_scaling_configuration: 
    :type serverless_v2_scaling_configuration: dict | bytes

    """
    cloudwatch_logs_export_configuration = .from_dict(cloudwatch_logs_export_configuration)
    serverless_v2_scaling_configuration = .from_dict(serverless_v2_scaling_configuration)
    return web.Response(status=200)


async def g_et_modify_db_cluster_endpoint(request: web.Request, db_cluster_endpoint_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, endpoint_type=None, static_members=None, excluded_members=None) -> web.Response:
    """g_et_modify_db_cluster_endpoint

    Modifies the properties of an endpoint in an Amazon Neptune DB cluster.

    :param db_cluster_endpoint_identifier: The identifier of the endpoint to modify. This parameter is stored as a lowercase string.
    :type db_cluster_endpoint_identifier: str
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
    :param endpoint_type: The type of the endpoint. One of: &lt;code&gt;READER&lt;/code&gt;, &lt;code&gt;WRITER&lt;/code&gt;, &lt;code&gt;ANY&lt;/code&gt;.
    :type endpoint_type: str
    :param static_members: List of DB instance identifiers that are part of the custom endpoint group.
    :type static_members: List[str]
    :param excluded_members: List of DB instance identifiers that aren&#39;t part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.
    :type excluded_members: List[str]

    """
    return web.Response(status=200)


async def g_et_modify_db_cluster_parameter_group(request: web.Request, db_cluster_parameter_group_name, parameters, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_db_cluster_parameter_group

    &lt;p&gt; Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt;, &lt;code&gt;ParameterValue&lt;/code&gt;, and &lt;code&gt;ApplyMethod&lt;/code&gt;. A maximum of 20 parameters can be modified in a single request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB cluster associated with the parameter group before the change can take effect.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the Amazon Neptune console or the &lt;a&gt;DescribeDBClusterParameters&lt;/a&gt; command to verify that your DB cluster parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

    :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to modify.
    :type db_cluster_parameter_group_name: str
    :param parameters: A list of parameters in the DB cluster parameter group to modify.
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

    &lt;p&gt;Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.&lt;/p&gt; &lt;p&gt;To share a manual DB cluster snapshot with other Amazon accounts, specify &lt;code&gt;restore&lt;/code&gt; as the &lt;code&gt;AttributeName&lt;/code&gt; and use the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter to add a list of IDs of the Amazon accounts that are authorized to restore the manual DB cluster snapshot. Use the value &lt;code&gt;all&lt;/code&gt; to make the manual DB cluster snapshot public, which means that it can be copied or restored by all Amazon accounts. Do not add the &lt;code&gt;all&lt;/code&gt; value for any manual DB cluster snapshots that contain private information that you don&#39;t want available to all Amazon accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized Amazon account IDs for the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter. You can&#39;t use &lt;code&gt;all&lt;/code&gt; as a value for that parameter in this case.&lt;/p&gt; &lt;p&gt;To view which Amazon accounts have access to copy or restore a manual DB cluster snapshot, or whether a manual DB cluster snapshot public or private, use the &lt;a&gt;DescribeDBClusterSnapshotAttributes&lt;/a&gt; API action.&lt;/p&gt;

    :param db_cluster_snapshot_identifier: The identifier for the DB cluster snapshot to modify the attributes for.
    :type db_cluster_snapshot_identifier: str
    :param attribute_name: &lt;p&gt;The name of the DB cluster snapshot attribute to modify.&lt;/p&gt; &lt;p&gt;To manage authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this value to &lt;code&gt;restore&lt;/code&gt;.&lt;/p&gt;
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
    :param values_to_add: &lt;p&gt;A list of DB cluster snapshot attributes to add to the attribute specified by &lt;code&gt;AttributeName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To authorize other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account IDs, or &lt;code&gt;all&lt;/code&gt; to make the manual DB cluster snapshot restorable by any Amazon account. Do not add the &lt;code&gt;all&lt;/code&gt; value for any manual DB cluster snapshots that contain private information that you don&#39;t want available to all Amazon accounts.&lt;/p&gt;
    :type values_to_add: List[]
    :param values_to_remove: &lt;p&gt;A list of DB cluster snapshot attributes to remove from the attribute specified by &lt;code&gt;AttributeName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To remove authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account identifiers, or &lt;code&gt;all&lt;/code&gt; to remove authorization for any Amazon account to copy or restore the DB cluster snapshot. If you specify &lt;code&gt;all&lt;/code&gt;, an Amazon account whose account ID is explicitly added to the &lt;code&gt;restore&lt;/code&gt; attribute can still copy or restore a manual DB cluster snapshot.&lt;/p&gt;
    :type values_to_remove: List[]

    """
    return web.Response(status=200)


async def g_et_modify_db_instance(request: web.Request, db_instance_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, allocated_storage=None, db_instance_class=None, db_subnet_group_name=None, db_security_groups=None, vpc_security_group_ids=None, apply_immediately=None, master_user_password=None, db_parameter_group_name=None, backup_retention_period=None, preferred_backup_window=None, preferred_maintenance_window=None, multi_az=None, engine_version=None, allow_major_version_upgrade=None, auto_minor_version_upgrade=None, license_model=None, iops=None, option_group_name=None, new_db_instance_identifier=None, storage_type=None, tde_credential_arn=None, tde_credential_password=None, ca_certificate_identifier=None, domain=None, copy_tags_to_snapshot=None, monitoring_interval=None, db_port_number=None, publicly_accessible=None, monitoring_role_arn=None, domain_iam_role_name=None, promotion_tier=None, enable_iam_database_authentication=None, enable_performance_insights=None, performance_insights_kms_key_id=None, cloudwatch_logs_export_configuration=None, deletion_protection=None) -> web.Response:
    """g_et_modify_db_instance

    Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call &lt;a&gt;DescribeValidDBInstanceModifications&lt;/a&gt; before you call &lt;a&gt;ModifyDBInstance&lt;/a&gt;.

    :param db_instance_identifier: &lt;p&gt;The DB instance identifier. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing DBInstance.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param allocated_storage: Not supported by Neptune.
    :type allocated_storage: int
    :param db_instance_class: &lt;p&gt;The new compute and memory capacity of the DB instance, for example, &lt;code&gt;db.m4.large&lt;/code&gt;. Not all DB instance classes are available in all Amazon Regions.&lt;/p&gt; &lt;p&gt;If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless &lt;code&gt;ApplyImmediately&lt;/code&gt; is specified as &lt;code&gt;true&lt;/code&gt; for this request.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting&lt;/p&gt;
    :type db_instance_class: str
    :param db_subnet_group_name: &lt;p&gt;The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC.&lt;/p&gt; &lt;p&gt;Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you specify &lt;code&gt;true&lt;/code&gt; for the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;Constraints: If supplied, must match the name of an existing DBSubnetGroup.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetGroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param db_security_groups: &lt;p&gt;A list of DB security groups to authorize on this DB instance. Changing this setting doesn&#39;t result in an outage and the change is asynchronously applied as soon as possible.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match existing DBSecurityGroups.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_security_groups: List[]
    :param vpc_security_group_ids: &lt;p&gt;A list of EC2 VPC security groups to authorize on this DB instance. This change is asynchronously applied as soon as possible.&lt;/p&gt; &lt;p&gt;Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see &lt;a&gt;ModifyDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match existing VpcSecurityGroupIds.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type vpc_security_group_ids: List[]
    :param apply_immediately: &lt;p&gt;Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the &lt;code&gt;PreferredMaintenanceWindow&lt;/code&gt; setting for the DB instance.&lt;/p&gt; &lt;p&gt; If this parameter is set to &lt;code&gt;false&lt;/code&gt;, changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to &lt;a&gt;RebootDBInstance&lt;/a&gt;, or the next failure reboot.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type apply_immediately: bool
    :param master_user_password: Not supported by Neptune.
    :type master_user_password: str
    :param db_parameter_group_name: &lt;p&gt;The name of the DB parameter group to apply to the DB instance. Changing this setting doesn&#39;t result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. The db instance will NOT be rebooted automatically and the parameter changes will NOT be applied during the next maintenance window.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting&lt;/p&gt; &lt;p&gt;Constraints: The DB parameter group must be in the same DB parameter group family as this DB instance.&lt;/p&gt;
    :type db_parameter_group_name: str
    :param backup_retention_period: &lt;p&gt;Not applicable. The retention period for automated backups is managed by the DB cluster. For more information, see &lt;a&gt;ModifyDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting&lt;/p&gt;
    :type backup_retention_period: int
    :param preferred_backup_window: &lt;p&gt; The daily time range during which automated backups are created if automated backups are enabled.&lt;/p&gt; &lt;p&gt;Not applicable. The daily time range for creating automated backups is managed by the DB cluster. For more information, see &lt;a&gt;ModifyDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be in the format hh24:mi-hh24:mi&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be in Universal Time Coordinated (UTC)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not conflict with the preferred maintenance window&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be at least 30 minutes&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type preferred_backup_window: str
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter doesn&#39;t result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter will cause a reboot of the DB instance. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting&lt;/p&gt; &lt;p&gt;Format: ddd:hh24:mi-ddd:hh24:mi&lt;/p&gt; &lt;p&gt;Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun&lt;/p&gt; &lt;p&gt;Constraints: Must be at least 30 minutes&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param multi_az: Specifies if the DB instance is a Multi-AZ deployment. Changing this parameter doesn&#39;t result in an outage and the change is applied during the next maintenance window unless the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt; for this request.
    :type multi_az: bool
    :param engine_version: The version number of the database engine to upgrade to. Currently, setting this parameter has no effect. To upgrade your database engine to the most recent release, use the &lt;a&gt;ApplyPendingMaintenanceAction&lt;/a&gt; API.
    :type engine_version: str
    :param allow_major_version_upgrade: Indicates that major version upgrades are allowed. Changing this parameter doesn&#39;t result in an outage and the change is asynchronously applied as soon as possible.
    :type allow_major_version_upgrade: bool
    :param auto_minor_version_upgrade:  Indicates that minor version upgrades are applied automatically to the DB instance during the maintenance window. Changing this parameter doesn&#39;t result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to &lt;code&gt;true&lt;/code&gt; during the maintenance window, and a newer minor version is available, and Neptune has enabled auto patching for that engine version.
    :type auto_minor_version_upgrade: bool
    :param license_model: Not supported by Neptune.
    :type license_model: str
    :param iops: &lt;p&gt;The new Provisioned IOPS (I/O operations per second) value for the instance.&lt;/p&gt; &lt;p&gt;Changing this setting doesn&#39;t result in an outage and the change is applied during the next maintenance window unless the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt; for this request.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting&lt;/p&gt;
    :type iops: int
    :param option_group_name:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type option_group_name: str
    :param new_db_instance_identifier: &lt;p&gt; The new DB instance identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot will occur immediately if you set &lt;code&gt;Apply Immediately&lt;/code&gt; to true, or will occur during the next maintenance window if &lt;code&gt;Apply Immediately&lt;/code&gt; to false. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;mydbinstance&lt;/code&gt; &lt;/p&gt;
    :type new_db_instance_identifier: str
    :param storage_type: Not supported.
    :type storage_type: str
    :param tde_credential_arn: The ARN from the key store with which to associate the instance for TDE encryption.
    :type tde_credential_arn: str
    :param tde_credential_password: The password for the given ARN from the key store in order to access the device.
    :type tde_credential_password: str
    :param ca_certificate_identifier: Indicates the certificate that needs to be associated with the instance.
    :type ca_certificate_identifier: str
    :param domain: Not supported.
    :type domain: str
    :param copy_tags_to_snapshot: True to copy all tags from the DB instance to snapshots of the DB instance, and otherwise false. The default is false.
    :type copy_tags_to_snapshot: bool
    :param monitoring_interval: &lt;p&gt;The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;MonitoringRoleArn&lt;/code&gt; is specified, then you must also set &lt;code&gt;MonitoringInterval&lt;/code&gt; to a value other than 0.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;0, 1, 5, 10, 15, 30, 60&lt;/code&gt; &lt;/p&gt;
    :type monitoring_interval: int
    :param db_port_number: &lt;p&gt;The port number on which the database accepts connections.&lt;/p&gt; &lt;p&gt;The value of the &lt;code&gt;DBPortNumber&lt;/code&gt; parameter must not match any of the port values specified for options in the option group for the DB instance.&lt;/p&gt; &lt;p&gt;Your database will restart when you change the &lt;code&gt;DBPortNumber&lt;/code&gt; value regardless of the value of the &lt;code&gt;ApplyImmediately&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt; Default: &lt;code&gt;8182&lt;/code&gt; &lt;/p&gt;
    :type db_port_number: int
    :param publicly_accessible: This flag should no longer be used.
    :type publicly_accessible: bool
    :param monitoring_role_arn: &lt;p&gt;The ARN for the IAM role that permits Neptune to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, &lt;code&gt;arn:aws:iam:123456789012:role/emaccess&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;MonitoringInterval&lt;/code&gt; is set to a value other than 0, then you must supply a &lt;code&gt;MonitoringRoleArn&lt;/code&gt; value.&lt;/p&gt;
    :type monitoring_role_arn: str
    :param domain_iam_role_name: Not supported
    :type domain_iam_role_name: str
    :param promotion_tier: &lt;p&gt;A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.&lt;/p&gt; &lt;p&gt;Default: 1&lt;/p&gt; &lt;p&gt;Valid Values: 0 - 15&lt;/p&gt;
    :type promotion_tier: int
    :param enable_iam_database_authentication: &lt;p&gt;True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.&lt;/p&gt; &lt;p&gt;You can enable IAM database authentication for the following database engines&lt;/p&gt; &lt;p&gt;Not applicable. Mapping Amazon IAM accounts to database accounts is managed by the DB cluster. For more information, see &lt;a&gt;ModifyDBCluster&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type enable_iam_database_authentication: bool
    :param enable_performance_insights:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type enable_performance_insights: bool
    :param performance_insights_kms_key_id:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type performance_insights_kms_key_id: str
    :param cloudwatch_logs_export_configuration: The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB instance or DB cluster.
    :type cloudwatch_logs_export_configuration: dict | bytes
    :param deletion_protection: A value that indicates whether the DB instance has deletion protection enabled. The database can&#39;t be deleted when deletion protection is enabled. By default, deletion protection is disabled. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html\&quot;&gt;Deleting a DB Instance&lt;/a&gt;.
    :type deletion_protection: bool

    """
    cloudwatch_logs_export_configuration = .from_dict(cloudwatch_logs_export_configuration)
    return web.Response(status=200)


async def g_et_modify_db_parameter_group(request: web.Request, db_parameter_group_name, parameters, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_db_parameter_group

    &lt;p&gt;Modifies the parameters of a DB parameter group. To modify more than one parameter, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt;, &lt;code&gt;ParameterValue&lt;/code&gt;, and &lt;code&gt;ApplyMethod&lt;/code&gt;. A maximum of 20 parameters can be modified in a single request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB instance associated with the parameter group before the change can take effect.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;After you modify a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the modify action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the Amazon Neptune console or the &lt;i&gt;DescribeDBParameters&lt;/i&gt; command to verify that your DB parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

    :param db_parameter_group_name: &lt;p&gt;The name of the DB parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_name: str
    :param parameters: &lt;p&gt;An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.&lt;/p&gt; &lt;p&gt;Valid Values (for the application method): &lt;code&gt;immediate | pending-reboot&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.&lt;/p&gt; &lt;/note&gt;
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


async def g_et_modify_db_subnet_group(request: web.Request, db_subnet_group_name, subnet_ids, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_subnet_group_description=None) -> web.Response:
    """g_et_modify_db_subnet_group

    Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the Amazon Region.

    :param db_subnet_group_name: &lt;p&gt;The name for the DB subnet group. This value is stored as a lowercase string. You can&#39;t modify the default subnet group.&lt;/p&gt; &lt;p&gt;Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param subnet_ids: The EC2 subnet IDs for the DB subnet group.
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
    :param db_subnet_group_description: The description for the DB subnet group.
    :type db_subnet_group_description: str

    """
    return web.Response(status=200)


async def g_et_modify_event_subscription(request: web.Request, subscription_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sns_topic_arn=None, source_type=None, event_categories=None, enabled=None) -> web.Response:
    """g_et_modify_event_subscription

    &lt;p&gt;Modifies an existing event notification subscription. Note that you can&#39;t modify the source identifiers using this call; to change source identifiers for a subscription, use the &lt;a&gt;AddSourceIdentifierToSubscription&lt;/a&gt; and &lt;a&gt;RemoveSourceIdentifierFromSubscription&lt;/a&gt; calls.&lt;/p&gt; &lt;p&gt;You can see a list of the event categories for a given SourceType by using the &lt;b&gt;DescribeEventCategories&lt;/b&gt; action.&lt;/p&gt;

    :param subscription_name: The name of the event notification subscription.
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
    :param source_type: &lt;p&gt;The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.&lt;/p&gt; &lt;p&gt;Valid values: db-instance | db-parameter-group | db-security-group | db-snapshot&lt;/p&gt;
    :type source_type: str
    :param event_categories:  A list of event categories for a SourceType that you want to subscribe to. You can see a list of the categories for a given SourceType by using the &lt;b&gt;DescribeEventCategories&lt;/b&gt; action.
    :type event_categories: List[]
    :param enabled:  A Boolean value; set to &lt;b&gt;true&lt;/b&gt; to activate the subscription.
    :type enabled: bool

    """
    return web.Response(status=200)


async def g_et_modify_global_cluster(request: web.Request, global_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, new_global_cluster_identifier=None, deletion_protection=None, engine_version=None, allow_major_version_upgrade=None) -> web.Response:
    """g_et_modify_global_cluster

    Modify a setting for an Amazon Neptune global cluster. You can change one or more database configuration parameters by specifying these parameters and their new values in the request.

    :param global_cluster_identifier: &lt;p&gt;The DB cluster identifier for the global cluster being modified. This parameter is not case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints: Must match the identifier of an existing global database cluster.&lt;/p&gt;
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
    :param new_global_cluster_identifier: &lt;p&gt;A new cluster identifier to assign to the global database. This value is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Can&#39;t end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-cluster2&lt;/code&gt; &lt;/p&gt;
    :type new_global_cluster_identifier: str
    :param deletion_protection: Indicates whether the global database has deletion protection enabled. The global database cannot be deleted when deletion protection is enabled.
    :type deletion_protection: bool
    :param engine_version: &lt;p&gt;The version number of the database engine to which you want to upgrade. Changing this parameter will result in an outage. The change is applied during the next maintenance window unless &lt;code&gt;ApplyImmediately&lt;/code&gt; is enabled.&lt;/p&gt; &lt;p&gt;To list all of the available Neptune engine versions, use the following command:&lt;/p&gt;
    :type engine_version: str
    :param allow_major_version_upgrade: &lt;p&gt;A value that indicates whether major version upgrades are allowed.&lt;/p&gt; &lt;p&gt;Constraints: You must allow major version upgrades if you specify a value for the &lt;code&gt;EngineVersion&lt;/code&gt; parameter that is a different major version than the DB cluster&#39;s current version.&lt;/p&gt; &lt;p&gt;If you upgrade the major version of a global database, the cluster and DB instance parameter groups are set to the default parameter groups for the new version, so you will need to apply any custom parameter groups after completing the upgrade.&lt;/p&gt;
    :type allow_major_version_upgrade: bool

    """
    return web.Response(status=200)


async def g_et_promote_read_replica_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_promote_read_replica_db_cluster

    Not supported.

    :param db_cluster_identifier: Not supported.
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


async def g_et_reboot_db_instance(request: web.Request, db_instance_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, force_failover=None) -> web.Response:
    """g_et_reboot_db_instance

    &lt;p&gt;You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.&lt;/p&gt; &lt;p&gt;Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.&lt;/p&gt;

    :param db_instance_identifier: &lt;p&gt;The DB instance identifier. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing DBInstance.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param force_failover: &lt;p&gt; When &lt;code&gt;true&lt;/code&gt;, the reboot is conducted through a MultiAZ failover.&lt;/p&gt; &lt;p&gt;Constraint: You can&#39;t specify &lt;code&gt;true&lt;/code&gt; if the instance is not configured for MultiAZ.&lt;/p&gt;
    :type force_failover: bool

    """
    return web.Response(status=200)


async def g_et_remove_from_global_cluster(request: web.Request, global_cluster_identifier, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_from_global_cluster

    Detaches a Neptune DB cluster from a Neptune global database. A secondary cluster becomes a normal standalone cluster with read-write capability instead of being read-only, and no longer receives data from a the primary cluster.

    :param global_cluster_identifier: The identifier of the Neptune global database from which to detach the specified Neptune DB cluster.
    :type global_cluster_identifier: str
    :param db_cluster_identifier: The Amazon Resource Name (ARN) identifying the cluster to be detached from the Neptune global database cluster.
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


async def g_et_remove_role_from_db_cluster(request: web.Request, db_cluster_identifier, role_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, feature_name=None) -> web.Response:
    """g_et_remove_role_from_db_cluster

    Disassociates an Identity and Access Management (IAM) role from a DB cluster.

    :param db_cluster_identifier: The name of the DB cluster to disassociate the IAM role from.
    :type db_cluster_identifier: str
    :param role_arn: The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB cluster, for example &lt;code&gt;arn:aws:iam::123456789012:role/NeptuneAccessRole&lt;/code&gt;.
    :type role_arn: str
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
    :param feature_name: The name of the feature for the DB cluster that the IAM role is to be disassociated from. For the list of supported feature names, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/userguide/api-other-apis.html#DescribeDBEngineVersions\&quot;&gt;DescribeDBEngineVersions&lt;/a&gt;.
    :type feature_name: str

    """
    return web.Response(status=200)


async def g_et_remove_source_identifier_from_subscription(request: web.Request, subscription_name, source_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_source_identifier_from_subscription

    Removes a source identifier from an existing event notification subscription.

    :param subscription_name: The name of the event notification subscription you want to remove a source identifier from.
    :type subscription_name: str
    :param source_identifier:  The source identifier to be removed from the subscription, such as the &lt;b&gt;DB instance identifier&lt;/b&gt; for a DB instance or the name of a security group.
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

    Removes metadata tags from an Amazon Neptune resource.

    :param resource_name: The Amazon Neptune resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing\&quot;&gt; Constructing an Amazon Resource Name (ARN)&lt;/a&gt;.
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

    &lt;p&gt; Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt; and &lt;code&gt;ApplyMethod&lt;/code&gt;. To reset the entire DB cluster parameter group, specify the &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; and &lt;code&gt;ResetAllParameters&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt; When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to &lt;code&gt;pending-reboot&lt;/code&gt; to take effect on the next DB instance restart or &lt;a&gt;RebootDBInstance&lt;/a&gt; request. You must call &lt;a&gt;RebootDBInstance&lt;/a&gt; for every DB instance in your DB cluster that you want the updated static parameter to apply to.&lt;/p&gt;

    :param db_cluster_parameter_group_name: The name of the DB cluster parameter group to reset.
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
    :param reset_all_parameters: A value that is set to &lt;code&gt;true&lt;/code&gt; to reset all parameters in the DB cluster parameter group to their default values, and &lt;code&gt;false&lt;/code&gt; otherwise. You can&#39;t use this parameter if there is a list of parameter names specified for the &lt;code&gt;Parameters&lt;/code&gt; parameter.
    :type reset_all_parameters: bool
    :param parameters: A list of parameter names in the DB cluster parameter group to reset to the default values. You can&#39;t use this parameter if the &lt;code&gt;ResetAllParameters&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt;.
    :type parameters: list | bytes

    """
    parameters = [GETModifyDBClusterParameterGroupParametersParameterInner.from_dict(d) for d in parameters]
    return web.Response(status=200)


async def g_et_reset_db_parameter_group(request: web.Request, db_parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reset_all_parameters=None, parameters=None) -> web.Response:
    """g_et_reset_db_parameter_group

    Modifies the parameters of a DB parameter group to the engine/system default value. To reset specific parameters, provide a list of the following: &lt;code&gt;ParameterName&lt;/code&gt; and &lt;code&gt;ApplyMethod&lt;/code&gt;. To reset the entire DB parameter group, specify the &lt;code&gt;DBParameterGroup&lt;/code&gt; name and &lt;code&gt;ResetAllParameters&lt;/code&gt; parameters. When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to &lt;code&gt;pending-reboot&lt;/code&gt; to take effect on the next DB instance restart or &lt;code&gt;RebootDBInstance&lt;/code&gt; request.

    :param db_parameter_group_name: &lt;p&gt;The name of the DB parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the name of an existing DBParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_parameter_group_name: str
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
    :param reset_all_parameters: &lt;p&gt;Specifies whether (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;) to reset all parameters in the DB parameter group to default values.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;true&lt;/code&gt; &lt;/p&gt;
    :type reset_all_parameters: bool
    :param parameters: &lt;p&gt;To reset the entire DB parameter group, specify the &lt;code&gt;DBParameterGroup&lt;/code&gt; name and &lt;code&gt;ResetAllParameters&lt;/code&gt; parameters. To reset specific parameters, provide a list of the following: &lt;code&gt;ParameterName&lt;/code&gt; and &lt;code&gt;ApplyMethod&lt;/code&gt;. A maximum of 20 parameters can be modified in a single request.&lt;/p&gt; &lt;p&gt;Valid Values (for Apply method): &lt;code&gt;pending-reboot&lt;/code&gt; &lt;/p&gt;
    :type parameters: list | bytes

    """
    parameters = [GETModifyDBClusterParameterGroupParametersParameterInner.from_dict(d) for d in parameters]
    return web.Response(status=200)


async def g_et_restore_db_cluster_from_snapshot(request: web.Request, db_cluster_identifier, snapshot_identifier, engine, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, availability_zones=None, engine_version=None, port=None, db_subnet_group_name=None, database_name=None, option_group_name=None, vpc_security_group_ids=None, tags=None, kms_key_id=None, enable_iam_database_authentication=None, enable_cloudwatch_logs_exports=None, db_cluster_parameter_group_name=None, deletion_protection=None, copy_tags_to_snapshot=None, serverless_v2_scaling_configuration=None) -> web.Response:
    """g_et_restore_db_cluster_from_snapshot

    &lt;p&gt;Creates a new DB cluster from a DB snapshot or DB cluster snapshot.&lt;/p&gt; &lt;p&gt;If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.&lt;/p&gt; &lt;p&gt;If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.&lt;/p&gt;

    :param db_cluster_identifier: &lt;p&gt;The name of the DB cluster to create from the DB snapshot or DB cluster snapshot. This parameter isn&#39;t case-sensitive.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-snapshot-id&lt;/code&gt; &lt;/p&gt;
    :type db_cluster_identifier: str
    :param snapshot_identifier: &lt;p&gt;The identifier for the DB snapshot or DB cluster snapshot to restore from.&lt;/p&gt; &lt;p&gt;You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing Snapshot.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type snapshot_identifier: str
    :param engine: &lt;p&gt;The database engine to use for the new DB cluster.&lt;/p&gt; &lt;p&gt;Default: The same as source&lt;/p&gt; &lt;p&gt;Constraint: Must be compatible with the engine of the source&lt;/p&gt;
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
    :param availability_zones: Provides the list of EC2 Availability Zones that instances in the restored DB cluster can be created in.
    :type availability_zones: List[]
    :param engine_version: The version of the database engine to use for the new DB cluster.
    :type engine_version: str
    :param port: &lt;p&gt;The port number on which the new DB cluster accepts connections.&lt;/p&gt; &lt;p&gt;Constraints: Value must be &lt;code&gt;1150-65535&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default: The same port as the original DB cluster.&lt;/p&gt;
    :type port: int
    :param db_subnet_group_name: &lt;p&gt;The name of the DB subnet group to use for the new DB cluster.&lt;/p&gt; &lt;p&gt;Constraints: If supplied, must match the name of an existing DBSubnetGroup.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param database_name: Not supported.
    :type database_name: str
    :param option_group_name:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type option_group_name: str
    :param vpc_security_group_ids: A list of VPC security groups that the new DB cluster will belong to.
    :type vpc_security_group_ids: List[]
    :param tags: The tags to be assigned to the restored DB cluster.
    :type tags: list | bytes
    :param kms_key_id: &lt;p&gt;The Amazon KMS key identifier to use when restoring an encrypted DB cluster from a DB snapshot or DB cluster snapshot.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.&lt;/p&gt; &lt;p&gt;If you do not specify a value for the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter, then the following will occur:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the DB snapshot or DB cluster snapshot in &lt;code&gt;SnapshotIdentifier&lt;/code&gt; is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the DB snapshot or DB cluster snapshot.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the DB snapshot or DB cluster snapshot in &lt;code&gt;SnapshotIdentifier&lt;/code&gt; is not encrypted, then the restored DB cluster is not encrypted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type kms_key_id: str
    :param enable_iam_database_authentication: &lt;p&gt;True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type enable_iam_database_authentication: bool
    :param enable_cloudwatch_logs_exports: The list of logs that the restored DB cluster is to export to Amazon CloudWatch Logs.
    :type enable_cloudwatch_logs_exports: List[str]
    :param db_cluster_parameter_group_name: &lt;p&gt;The name of the DB cluster parameter group to associate with the new DB cluster.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBClusterParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_parameter_group_name: str
    :param deletion_protection: A value that indicates whether the DB cluster has deletion protection enabled. The database can&#39;t be deleted when deletion protection is enabled. By default, deletion protection is disabled. 
    :type deletion_protection: bool
    :param copy_tags_to_snapshot:  &lt;i&gt;If set to &lt;code&gt;true&lt;/code&gt;, tags are copied to any snapshot of the restored DB cluster that is created.&lt;/i&gt; 
    :type copy_tags_to_snapshot: bool
    :param serverless_v2_scaling_configuration: 
    :type serverless_v2_scaling_configuration: dict | bytes

    """
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    serverless_v2_scaling_configuration = .from_dict(serverless_v2_scaling_configuration)
    return web.Response(status=200)


async def g_et_restore_db_cluster_to_point_in_time(request: web.Request, db_cluster_identifier, source_db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, restore_type=None, restore_to_time=None, use_latest_restorable_time=None, port=None, db_subnet_group_name=None, option_group_name=None, vpc_security_group_ids=None, tags=None, kms_key_id=None, enable_iam_database_authentication=None, enable_cloudwatch_logs_exports=None, db_cluster_parameter_group_name=None, deletion_protection=None, serverless_v2_scaling_configuration=None) -> web.Response:
    """g_et_restore_db_cluster_to_point_in_time

    &lt;p&gt;Restores a DB cluster to an arbitrary point in time. Users can restore to any point in time before &lt;code&gt;LatestRestorableTime&lt;/code&gt; for up to &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; days. The target DB cluster is created from the source DB cluster with the same configuration as the original DB cluster, except that the new DB cluster is created with the default DB security group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only restores the DB cluster, not the DB instances for that DB cluster. You must invoke the &lt;a&gt;CreateDBInstance&lt;/a&gt; action to create DB instances for the restored DB cluster, specifying the identifier of the restored DB cluster in &lt;code&gt;DBClusterIdentifier&lt;/code&gt;. You can create DB instances only after the &lt;code&gt;RestoreDBClusterToPointInTime&lt;/code&gt; action has completed and the DB cluster is available.&lt;/p&gt; &lt;/note&gt;

    :param db_cluster_identifier: &lt;p&gt;The name of the new DB cluster to be created.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_identifier: str
    :param source_db_cluster_identifier: &lt;p&gt;The identifier of the source DB cluster from which to restore.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must match the identifier of an existing DBCluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param restore_type: &lt;p&gt;The type of restore to be performed. You can specify one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;full-copy&lt;/code&gt; - The new DB cluster is restored as a full copy of the source DB cluster.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;copy-on-write&lt;/code&gt; - The new DB cluster is restored as a clone of the source DB cluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you don&#39;t specify a &lt;code&gt;RestoreType&lt;/code&gt; value, then the new DB cluster is restored as a full copy of the source DB cluster.&lt;/p&gt;
    :type restore_type: str
    :param restore_to_time: &lt;p&gt;The date and time to restore the DB cluster to.&lt;/p&gt; &lt;p&gt;Valid Values: Value must be a time in Universal Coordinated Time (UTC) format&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be before the latest restorable time for the DB instance&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be specified if &lt;code&gt;UseLatestRestorableTime&lt;/code&gt; parameter is not provided&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be specified if &lt;code&gt;UseLatestRestorableTime&lt;/code&gt; parameter is true&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be specified if &lt;code&gt;RestoreType&lt;/code&gt; parameter is &lt;code&gt;copy-on-write&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;2015-03-07T23:45:00Z&lt;/code&gt; &lt;/p&gt;
    :type restore_to_time: str
    :param use_latest_restorable_time: &lt;p&gt;A value that is set to &lt;code&gt;true&lt;/code&gt; to restore the DB cluster to the latest restorable backup time, and &lt;code&gt;false&lt;/code&gt; otherwise.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: Cannot be specified if &lt;code&gt;RestoreToTime&lt;/code&gt; parameter is provided.&lt;/p&gt;
    :type use_latest_restorable_time: bool
    :param port: &lt;p&gt;The port number on which the new DB cluster accepts connections.&lt;/p&gt; &lt;p&gt;Constraints: Value must be &lt;code&gt;1150-65535&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default: The same port as the original DB cluster.&lt;/p&gt;
    :type port: int
    :param db_subnet_group_name: &lt;p&gt;The DB subnet group name to use for the new DB cluster.&lt;/p&gt; &lt;p&gt;Constraints: If supplied, must match the name of an existing DBSubnetGroup.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;mySubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type db_subnet_group_name: str
    :param option_group_name:  &lt;i&gt;(Not supported by Neptune)&lt;/i&gt; 
    :type option_group_name: str
    :param vpc_security_group_ids: A list of VPC security groups that the new DB cluster belongs to.
    :type vpc_security_group_ids: List[]
    :param tags: The tags to be applied to the restored DB cluster.
    :type tags: list | bytes
    :param kms_key_id: &lt;p&gt;The Amazon KMS key identifier to use when restoring an encrypted DB cluster from an encrypted DB cluster.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are restoring a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.&lt;/p&gt; &lt;p&gt;You can restore to a new DB cluster and encrypt the new DB cluster with a KMS key that is different than the KMS key used to encrypt the source DB cluster. The new DB cluster is encrypted with the KMS key identified by the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you do not specify a value for the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter, then the following will occur:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the DB cluster is encrypted, then the restored DB cluster is encrypted using the KMS key that was used to encrypt the source DB cluster.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the DB cluster is not encrypted, then the restored DB cluster is not encrypted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If &lt;code&gt;DBClusterIdentifier&lt;/code&gt; refers to a DB cluster that is not encrypted, then the restore request is rejected.&lt;/p&gt;
    :type kms_key_id: str
    :param enable_iam_database_authentication: &lt;p&gt;True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type enable_iam_database_authentication: bool
    :param enable_cloudwatch_logs_exports: The list of logs that the restored DB cluster is to export to CloudWatch Logs.
    :type enable_cloudwatch_logs_exports: List[str]
    :param db_cluster_parameter_group_name: &lt;p&gt;The name of the DB cluster parameter group to associate with the new DB cluster.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If supplied, must match the name of an existing DBClusterParameterGroup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_cluster_parameter_group_name: str
    :param deletion_protection: A value that indicates whether the DB cluster has deletion protection enabled. The database can&#39;t be deleted when deletion protection is enabled. By default, deletion protection is disabled. 
    :type deletion_protection: bool
    :param serverless_v2_scaling_configuration: 
    :type serverless_v2_scaling_configuration: dict | bytes

    """
    restore_to_time = util.deserialize_datetime(restore_to_time)
    tags = [GETAddTagsToResourceTagsParameterInner.from_dict(d) for d in tags]
    serverless_v2_scaling_configuration = .from_dict(serverless_v2_scaling_configuration)
    return web.Response(status=200)


async def g_et_start_db_cluster(request: web.Request, db_cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_start_db_cluster

    Starts an Amazon Neptune DB cluster that was stopped using the Amazon console, the Amazon CLI stop-db-cluster command, or the StopDBCluster API.

    :param db_cluster_identifier: The DB cluster identifier of the Neptune DB cluster to be started. This parameter is stored as a lowercase string.
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

    &lt;p&gt;Stops an Amazon Neptune DB cluster. When you stop a DB cluster, Neptune retains the DB cluster&#39;s metadata, including its endpoints and DB parameter groups.&lt;/p&gt; &lt;p&gt;Neptune also retains the transaction logs so you can do a point-in-time restore if necessary.&lt;/p&gt;

    :param db_cluster_identifier: The DB cluster identifier of the Neptune DB cluster to be stopped. This parameter is stored as a lowercase string.
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


async def p_ost_add_role_to_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_role_to_db_cluster

    Associates an Identity and Access Management (IAM) role with an Neptune DB cluster.

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
    body = AddRoleToDBClusterMessage.from_dict(body)
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

    Adds metadata tags to an Amazon Neptune resource. These tags can also be used with cost allocation reporting to track cost associated with Amazon Neptune resources, or used in a Condition statement in an IAM policy for Amazon Neptune.

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

    Applies a pending maintenance action to a resource (for example, to a DB instance).

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

    Copies the specified DB cluster parameter group.

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

    &lt;p&gt;Copies a snapshot of a DB cluster.&lt;/p&gt; &lt;p&gt;To copy a DB cluster snapshot from a shared manual DB cluster snapshot, &lt;code&gt;SourceDBClusterSnapshotIdentifier&lt;/code&gt; must be the Amazon Resource Name (ARN) of the shared DB cluster snapshot.&lt;/p&gt;

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


async def p_ost_copy_db_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_copy_db_parameter_group

    Copies the specified DB parameter group.

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
    body = CopyDBParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_cluster

    &lt;p&gt;Creates a new Amazon Neptune DB cluster.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;ReplicationSourceIdentifier&lt;/code&gt; parameter to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune DB instance.&lt;/p&gt; &lt;p&gt;Note that when you create a new cluster using &lt;code&gt;CreateDBCluster&lt;/code&gt; directly, deletion protection is disabled by default (when you create a new production cluster in the console, deletion protection is enabled by default). You can only delete a DB cluster if its &lt;code&gt;DeletionProtection&lt;/code&gt; field is set to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt;

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


async def p_ost_create_db_cluster_endpoint(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_cluster_endpoint

    Creates a new custom endpoint and associates it with an Amazon Neptune DB cluster.

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
    body = CreateDBClusterEndpointMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_cluster_parameter_group

    &lt;p&gt;Creates a new DB cluster parameter group.&lt;/p&gt; &lt;p&gt;Parameters in a DB cluster parameter group apply to all of the instances in a DB cluster.&lt;/p&gt; &lt;p&gt; A DB cluster parameter group is initially created with the default parameters for the database engine used by instances in the DB cluster. To provide custom values for any of the parameters, you must modify the group after creating it using &lt;a&gt;ModifyDBClusterParameterGroup&lt;/a&gt;. Once you&#39;ve created a DB cluster parameter group, you need to associate it with your DB cluster using &lt;a&gt;ModifyDBCluster&lt;/a&gt;. When you associate a new DB cluster parameter group with a running DB cluster, you need to reboot the DB instances in the DB cluster without failover for the new DB cluster parameter group and associated settings to take effect.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the DB cluster parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/rds/\&quot;&gt;Amazon Neptune console&lt;/a&gt; or the &lt;a&gt;DescribeDBClusterParameters&lt;/a&gt; command to verify that your DB cluster parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

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

    Creates a snapshot of a DB cluster.

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

    Creates a new DB instance.

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


async def p_ost_create_db_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_parameter_group

    &lt;p&gt;Creates a new DB parameter group.&lt;/p&gt; &lt;p&gt;A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using &lt;i&gt;ModifyDBParameterGroup&lt;/i&gt;. Once you&#39;ve created a DB parameter group, you need to associate it with your DB instance using &lt;i&gt;ModifyDBInstance&lt;/i&gt;. When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After you create a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the Amazon Neptune console or the &lt;i&gt;DescribeDBParameters&lt;/i&gt; command to verify that your DB parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateDBParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_db_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_db_subnet_group

    Creates a new DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the Amazon Region.

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

    &lt;p&gt;Creates an event notification subscription. This action requires a topic ARN (Amazon Resource Name) created by either the Neptune console, the SNS console, or the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.&lt;/p&gt; &lt;p&gt;You can specify the type of source (SourceType) you want to be notified of, provide a list of Neptune sources (SourceIds) that triggers the events, and provide a list of event categories (EventCategories) for events you want to be notified of. For example, you can specify SourceType &#x3D; db-instance, SourceIds &#x3D; mydbinstance1, mydbinstance2 and EventCategories &#x3D; Availability, Backup.&lt;/p&gt; &lt;p&gt;If you specify both the SourceType and SourceIds, such as SourceType &#x3D; db-instance and SourceIdentifier &#x3D; myDBInstance1, you are notified of all the db-instance events for the specified source. If you specify a SourceType but do not specify a SourceIdentifier, you receive notice of the events for that source type for all your Neptune sources. If you do not specify either the SourceType nor the SourceIdentifier, you are notified of events generated from all Neptune sources belonging to your customer account.&lt;/p&gt;

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

    &lt;p&gt;Creates a Neptune global database spread across multiple Amazon Regions. The global database contains a single primary cluster with read-write capability, and read-only secondary clusters that receive data from the primary cluster through high-speed replication performed by the Neptune storage subsystem.&lt;/p&gt; &lt;p&gt;You can create a global database that is initially empty, and then add a primary cluster and secondary clusters to it, or you can specify an existing Neptune cluster during the create operation to become the primary cluster of the global database.&lt;/p&gt;

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

    &lt;p&gt;The DeleteDBCluster action deletes a previously provisioned DB cluster. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can&#39;t be recovered. Manual DB cluster snapshots of the specified DB cluster are not deleted.&lt;/p&gt; &lt;p&gt;Note that the DB Cluster cannot be deleted if deletion protection is enabled. To delete it, you must first set its &lt;code&gt;DeletionProtection&lt;/code&gt; field to &lt;code&gt;False&lt;/code&gt;.&lt;/p&gt;

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


async def p_ost_delete_db_cluster_endpoint(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_cluster_endpoint

    Deletes a custom endpoint and removes it from an Amazon Neptune DB cluster.

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
    body = DeleteDBClusterEndpointMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_cluster_parameter_group

    Deletes a specified DB cluster parameter group. The DB cluster parameter group to be deleted can&#39;t be associated with any DB clusters.

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

    &lt;p&gt;Deletes a DB cluster snapshot. If the snapshot is being copied, the copy operation is terminated.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The DB cluster snapshot must be in the &lt;code&gt;available&lt;/code&gt; state to be deleted.&lt;/p&gt; &lt;/note&gt;

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

    &lt;p&gt;The DeleteDBInstance action deletes a previously provisioned DB instance. When you delete a DB instance, all automated backups for that instance are deleted and can&#39;t be recovered. Manual DB snapshots of the DB instance to be deleted by &lt;code&gt;DeleteDBInstance&lt;/code&gt; are not deleted.&lt;/p&gt; &lt;p&gt; If you request a final DB snapshot the status of the Amazon Neptune DB instance is &lt;code&gt;deleting&lt;/code&gt; until the DB snapshot is created. The API action &lt;code&gt;DescribeDBInstance&lt;/code&gt; is used to monitor the status of this operation. The action can&#39;t be canceled or reverted once submitted.&lt;/p&gt; &lt;p&gt;Note that when a DB instance is in a failure state and has a status of &lt;code&gt;failed&lt;/code&gt;, &lt;code&gt;incompatible-restore&lt;/code&gt;, or &lt;code&gt;incompatible-network&lt;/code&gt;, you can only delete it when the &lt;code&gt;SkipFinalSnapshot&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a DB instance if it is the only instance in the DB cluster, or if it has deletion protection enabled.&lt;/p&gt;

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


async def p_ost_delete_db_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_parameter_group

    Deletes a specified DBParameterGroup. The DBParameterGroup to be deleted can&#39;t be associated with any DB instances.

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
    body = DeleteDBParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_db_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_db_subnet_group

    &lt;p&gt;Deletes a DB subnet group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The specified database subnet group must not be associated with any DB instances.&lt;/p&gt; &lt;/note&gt;

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

    Deletes an event notification subscription.

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

    Deletes a global database. The primary and all secondary clusters must already be detached or deleted first.

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


async def p_ost_describe_db_cluster_endpoints(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_cluster_endpoints

    &lt;p&gt;Returns information about endpoints for an Amazon Neptune DB cluster.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation can also return information for Amazon RDS clusters and Amazon DocDB clusters.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeDBClusterEndpointsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_cluster_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_cluster_parameter_groups

     Returns a list of &lt;code&gt;DBClusterParameterGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; parameter is specified, the list will contain only the description of the specified DB cluster parameter group.

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

    Returns the detailed parameter list for a particular DB cluster parameter group.

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

    &lt;p&gt;Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.&lt;/p&gt; &lt;p&gt;When sharing snapshots with other Amazon accounts, &lt;code&gt;DescribeDBClusterSnapshotAttributes&lt;/code&gt; returns the &lt;code&gt;restore&lt;/code&gt; attribute and a list of IDs for the Amazon accounts that are authorized to copy or restore the manual DB cluster snapshot. If &lt;code&gt;all&lt;/code&gt; is included in the list of values for the &lt;code&gt;restore&lt;/code&gt; attribute, then the manual DB cluster snapshot is public and can be copied or restored by all Amazon accounts.&lt;/p&gt; &lt;p&gt;To add or remove access for an Amazon account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the &lt;a&gt;ModifyDBClusterSnapshotAttribute&lt;/a&gt; API action.&lt;/p&gt;

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

    Returns information about DB cluster snapshots. This API action supports pagination.

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

    &lt;p&gt;Returns information about provisioned DB clusters, and supports pagination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation can also return information for Amazon RDS clusters and Amazon DocDB clusters.&lt;/p&gt; &lt;/note&gt;

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

    Returns a list of the available DB engines.

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

    &lt;p&gt;Returns information about provisioned instances, and supports pagination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation can also return information for Amazon RDS instances and Amazon DocDB instances.&lt;/p&gt; &lt;/note&gt;

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


async def p_ost_describe_db_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_parameter_groups

    Returns a list of &lt;code&gt;DBParameterGroup&lt;/code&gt; descriptions. If a &lt;code&gt;DBParameterGroupName&lt;/code&gt; is specified, the list will contain only the description of the specified DB parameter group.

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
    body = DescribeDBParameterGroupsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_parameters

    Returns the detailed parameter list for a particular DB parameter group.

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
    body = DescribeDBParametersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_db_subnet_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_db_subnet_groups

    &lt;p&gt;Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is specified, the list will contain only the descriptions of the specified DBSubnetGroup.&lt;/p&gt; &lt;p&gt;For an overview of CIDR ranges, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\&quot;&gt;Wikipedia Tutorial&lt;/a&gt;.&lt;/p&gt;

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


async def p_ost_describe_engine_default_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_engine_default_parameters

    Returns the default engine and system parameter information for the specified database engine.

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
    body = DescribeEngineDefaultParametersMessage.from_dict(body)
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

    &lt;p&gt;Lists all the subscription descriptions for a customer account. The description for a subscription includes SubscriptionName, SNSTopicARN, CustomerID, SourceType, SourceID, CreationTime, and Status.&lt;/p&gt; &lt;p&gt;If you specify a SubscriptionName, lists the description for that subscription.&lt;/p&gt;

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

    Returns events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days. Events specific to a particular DB instance, DB security group, database snapshot, or DB parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.

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

    Returns information about Neptune global database clusters. This API supports pagination.

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

    Returns a list of orderable DB instance options for the specified engine.

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

    Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.

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


async def p_ost_describe_valid_db_instance_modifications(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_valid_db_instance_modifications

    You can call &lt;a&gt;DescribeValidDBInstanceModifications&lt;/a&gt; to learn what modifications you can make to your DB instance. You can use this information when you call &lt;a&gt;ModifyDBInstance&lt;/a&gt;.

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
    body = DescribeValidDBInstanceModificationsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_failover_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_failover_db_cluster

    &lt;p&gt;Forces a failover for a DB cluster.&lt;/p&gt; &lt;p&gt;A failover for a DB cluster promotes one of the Read Replicas (read-only instances) in the DB cluster to be the primary instance (the cluster writer).&lt;/p&gt; &lt;p&gt;Amazon Neptune will automatically fail over to a Read Replica, if one exists, when the primary instance fails. You can force a failover when you want to simulate a failure of a primary instance for testing. Because each instance in a DB cluster has its own endpoint address, you will need to clean up and re-establish any existing connections that use those endpoint addresses when the failover is complete.&lt;/p&gt;

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


async def p_ost_failover_global_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_failover_global_cluster

    &lt;p&gt;Initiates the failover process for a Neptune global database.&lt;/p&gt; &lt;p&gt;A failover for a Neptune global database promotes one of secondary read-only DB clusters to be the primary DB cluster and demotes the primary DB cluster to being a secondary (read-only) DB cluster. In other words, the role of the current primary DB cluster and the selected target secondary DB cluster are switched. The selected secondary DB cluster assumes full read/write capabilities for the Neptune global database.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action applies &lt;b&gt;only&lt;/b&gt; to Neptune global databases. This action is only intended for use on healthy Neptune global databases with healthy Neptune DB clusters and no region-wide outages, to test disaster recovery scenarios or to reconfigure the global database topology.&lt;/p&gt; &lt;/note&gt;

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
    body = FailoverGlobalClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_tags_for_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_tags_for_resource

    Lists all tags on an Amazon Neptune resource.

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

    Modify a setting for a DB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.

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


async def p_ost_modify_db_cluster_endpoint(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_cluster_endpoint

    Modifies the properties of an endpoint in an Amazon Neptune DB cluster.

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
    body = ModifyDBClusterEndpointMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_db_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_cluster_parameter_group

    &lt;p&gt; Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt;, &lt;code&gt;ParameterValue&lt;/code&gt;, and &lt;code&gt;ApplyMethod&lt;/code&gt;. A maximum of 20 parameters can be modified in a single request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB cluster associated with the parameter group before the change can take effect.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;After you create a DB cluster parameter group, you should wait at least 5 minutes before creating your first DB cluster that uses that DB cluster parameter group as the default parameter group. This allows Amazon Neptune to fully complete the create action before the parameter group is used as the default for a new DB cluster. This is especially important for parameters that are critical when creating the default database for a DB cluster, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the Amazon Neptune console or the &lt;a&gt;DescribeDBClusterParameters&lt;/a&gt; command to verify that your DB cluster parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

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

    &lt;p&gt;Adds an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot.&lt;/p&gt; &lt;p&gt;To share a manual DB cluster snapshot with other Amazon accounts, specify &lt;code&gt;restore&lt;/code&gt; as the &lt;code&gt;AttributeName&lt;/code&gt; and use the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter to add a list of IDs of the Amazon accounts that are authorized to restore the manual DB cluster snapshot. Use the value &lt;code&gt;all&lt;/code&gt; to make the manual DB cluster snapshot public, which means that it can be copied or restored by all Amazon accounts. Do not add the &lt;code&gt;all&lt;/code&gt; value for any manual DB cluster snapshots that contain private information that you don&#39;t want available to all Amazon accounts. If a manual DB cluster snapshot is encrypted, it can be shared, but only by specifying a list of authorized Amazon account IDs for the &lt;code&gt;ValuesToAdd&lt;/code&gt; parameter. You can&#39;t use &lt;code&gt;all&lt;/code&gt; as a value for that parameter in this case.&lt;/p&gt; &lt;p&gt;To view which Amazon accounts have access to copy or restore a manual DB cluster snapshot, or whether a manual DB cluster snapshot public or private, use the &lt;a&gt;DescribeDBClusterSnapshotAttributes&lt;/a&gt; API action.&lt;/p&gt;

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

    Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request. To learn what modifications you can make to your DB instance, call &lt;a&gt;DescribeValidDBInstanceModifications&lt;/a&gt; before you call &lt;a&gt;ModifyDBInstance&lt;/a&gt;.

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


async def p_ost_modify_db_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_parameter_group

    &lt;p&gt;Modifies the parameters of a DB parameter group. To modify more than one parameter, submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt;, &lt;code&gt;ParameterValue&lt;/code&gt;, and &lt;code&gt;ApplyMethod&lt;/code&gt;. A maximum of 20 parameters can be modified in a single request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to dynamic parameters are applied immediately. Changes to static parameters require a reboot without failover to the DB instance associated with the parameter group before the change can take effect.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;After you modify a DB parameter group, you should wait at least 5 minutes before creating your first DB instance that uses that DB parameter group as the default parameter group. This allows Amazon Neptune to fully complete the modify action before the parameter group is used as the default for a new DB instance. This is especially important for parameters that are critical when creating the default database for a DB instance, such as the character set for the default database defined by the &lt;code&gt;character_set_database&lt;/code&gt; parameter. You can use the &lt;i&gt;Parameter Groups&lt;/i&gt; option of the Amazon Neptune console or the &lt;i&gt;DescribeDBParameters&lt;/i&gt; command to verify that your DB parameter group has been created or modified.&lt;/p&gt; &lt;/important&gt;

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
    body = ModifyDBParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_db_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_db_subnet_group

    Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the Amazon Region.

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

    &lt;p&gt;Modifies an existing event notification subscription. Note that you can&#39;t modify the source identifiers using this call; to change source identifiers for a subscription, use the &lt;a&gt;AddSourceIdentifierToSubscription&lt;/a&gt; and &lt;a&gt;RemoveSourceIdentifierFromSubscription&lt;/a&gt; calls.&lt;/p&gt; &lt;p&gt;You can see a list of the event categories for a given SourceType by using the &lt;b&gt;DescribeEventCategories&lt;/b&gt; action.&lt;/p&gt;

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

    Modify a setting for an Amazon Neptune global cluster. You can change one or more database configuration parameters by specifying these parameters and their new values in the request.

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


async def p_ost_promote_read_replica_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_promote_read_replica_db_cluster

    Not supported.

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
    body = PromoteReadReplicaDBClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_reboot_db_instance(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reboot_db_instance

    &lt;p&gt;You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.&lt;/p&gt; &lt;p&gt;Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.&lt;/p&gt;

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

    Detaches a Neptune DB cluster from a Neptune global database. A secondary cluster becomes a normal standalone cluster with read-write capability instead of being read-only, and no longer receives data from a the primary cluster.

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


async def p_ost_remove_role_from_db_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_role_from_db_cluster

    Disassociates an Identity and Access Management (IAM) role from a DB cluster.

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
    body = RemoveRoleFromDBClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_source_identifier_from_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_source_identifier_from_subscription

    Removes a source identifier from an existing event notification subscription.

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

    Removes metadata tags from an Amazon Neptune resource.

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

    &lt;p&gt; Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters submit a list of the following: &lt;code&gt;ParameterName&lt;/code&gt; and &lt;code&gt;ApplyMethod&lt;/code&gt;. To reset the entire DB cluster parameter group, specify the &lt;code&gt;DBClusterParameterGroupName&lt;/code&gt; and &lt;code&gt;ResetAllParameters&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt; When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to &lt;code&gt;pending-reboot&lt;/code&gt; to take effect on the next DB instance restart or &lt;a&gt;RebootDBInstance&lt;/a&gt; request. You must call &lt;a&gt;RebootDBInstance&lt;/a&gt; for every DB instance in your DB cluster that you want the updated static parameter to apply to.&lt;/p&gt;

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


async def p_ost_reset_db_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reset_db_parameter_group

    Modifies the parameters of a DB parameter group to the engine/system default value. To reset specific parameters, provide a list of the following: &lt;code&gt;ParameterName&lt;/code&gt; and &lt;code&gt;ApplyMethod&lt;/code&gt;. To reset the entire DB parameter group, specify the &lt;code&gt;DBParameterGroup&lt;/code&gt; name and &lt;code&gt;ResetAllParameters&lt;/code&gt; parameters. When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to &lt;code&gt;pending-reboot&lt;/code&gt; to take effect on the next DB instance restart or &lt;code&gt;RebootDBInstance&lt;/code&gt; request.

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
    body = ResetDBParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_restore_db_cluster_from_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_restore_db_cluster_from_snapshot

    &lt;p&gt;Creates a new DB cluster from a DB snapshot or DB cluster snapshot.&lt;/p&gt; &lt;p&gt;If a DB snapshot is specified, the target DB cluster is created from the source DB snapshot with a default configuration and default security group.&lt;/p&gt; &lt;p&gt;If a DB cluster snapshot is specified, the target DB cluster is created from the source DB cluster restore point with the same configuration as the original source DB cluster, except that the new DB cluster is created with the default security group.&lt;/p&gt;

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

    &lt;p&gt;Restores a DB cluster to an arbitrary point in time. Users can restore to any point in time before &lt;code&gt;LatestRestorableTime&lt;/code&gt; for up to &lt;code&gt;BackupRetentionPeriod&lt;/code&gt; days. The target DB cluster is created from the source DB cluster with the same configuration as the original DB cluster, except that the new DB cluster is created with the default DB security group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action only restores the DB cluster, not the DB instances for that DB cluster. You must invoke the &lt;a&gt;CreateDBInstance&lt;/a&gt; action to create DB instances for the restored DB cluster, specifying the identifier of the restored DB cluster in &lt;code&gt;DBClusterIdentifier&lt;/code&gt;. You can create DB instances only after the &lt;code&gt;RestoreDBClusterToPointInTime&lt;/code&gt; action has completed and the DB cluster is available.&lt;/p&gt; &lt;/note&gt;

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

    Starts an Amazon Neptune DB cluster that was stopped using the Amazon console, the Amazon CLI stop-db-cluster command, or the StopDBCluster API.

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

    &lt;p&gt;Stops an Amazon Neptune DB cluster. When you stop a DB cluster, Neptune retains the DB cluster&#39;s metadata, including its endpoints and DB parameter groups.&lt;/p&gt; &lt;p&gt;Neptune also retains the transaction logs so you can do a point-in-time restore if necessary.&lt;/p&gt;

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
