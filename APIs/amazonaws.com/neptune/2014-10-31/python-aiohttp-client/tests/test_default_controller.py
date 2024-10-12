# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_g_et_add_role_to_db_cluster(client):
    """Test case for g_et_add_role_to_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('RoleArn', 'role_arn_example'),
                    ('FeatureName', 'feature_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=AddRoleToDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_add_source_identifier_to_subscription(client):
    """Test case for g_et_add_source_identifier_to_subscription

    
    """
    params = [('SubscriptionName', 'subscription_name_example'),
                    ('SourceIdentifier', 'source_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=AddSourceIdentifierToSubscription',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_add_tags_to_resource(client):
    """Test case for g_et_add_tags_to_resource

    
    """
    params = [('ResourceName', 'resource_name_example'),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=AddTagsToResource',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_apply_pending_maintenance_action(client):
    """Test case for g_et_apply_pending_maintenance_action

    
    """
    params = [('ResourceIdentifier', 'resource_identifier_example'),
                    ('ApplyAction', 'apply_action_example'),
                    ('OptInType', 'opt_in_type_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ApplyPendingMaintenanceAction',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_copy_db_cluster_parameter_group(client):
    """Test case for g_et_copy_db_cluster_parameter_group

    
    """
    params = [('SourceDBClusterParameterGroupIdentifier', 'source_db_cluster_parameter_group_identifier_example'),
                    ('TargetDBClusterParameterGroupIdentifier', 'target_db_cluster_parameter_group_identifier_example'),
                    ('TargetDBClusterParameterGroupDescription', 'target_db_cluster_parameter_group_description_example'),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CopyDBClusterParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_copy_db_cluster_snapshot(client):
    """Test case for g_et_copy_db_cluster_snapshot

    
    """
    params = [('SourceDBClusterSnapshotIdentifier', 'source_db_cluster_snapshot_identifier_example'),
                    ('TargetDBClusterSnapshotIdentifier', 'target_db_cluster_snapshot_identifier_example'),
                    ('KmsKeyId', 'kms_key_id_example'),
                    ('PreSignedUrl', 'pre_signed_url_example'),
                    ('CopyTags', True),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CopyDBClusterSnapshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_copy_db_parameter_group(client):
    """Test case for g_et_copy_db_parameter_group

    
    """
    params = [('SourceDBParameterGroupIdentifier', 'source_db_parameter_group_identifier_example'),
                    ('TargetDBParameterGroupIdentifier', 'target_db_parameter_group_identifier_example'),
                    ('TargetDBParameterGroupDescription', 'target_db_parameter_group_description_example'),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CopyDBParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_db_cluster(client):
    """Test case for g_et_create_db_cluster

    
    """
    params = [('AvailabilityZones', ['availability_zones_example']),
                    ('BackupRetentionPeriod', 56),
                    ('CharacterSetName', 'character_set_name_example'),
                    ('CopyTagsToSnapshot', True),
                    ('DatabaseName', 'database_name_example'),
                    ('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('VpcSecurityGroupIds', ['vpc_security_group_ids_example']),
                    ('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('Engine', 'engine_example'),
                    ('EngineVersion', 'engine_version_example'),
                    ('Port', 56),
                    ('MasterUsername', 'master_username_example'),
                    ('MasterUserPassword', 'master_user_password_example'),
                    ('OptionGroupName', 'option_group_name_example'),
                    ('PreferredBackupWindow', 'preferred_backup_window_example'),
                    ('PreferredMaintenanceWindow', 'preferred_maintenance_window_example'),
                    ('ReplicationSourceIdentifier', 'replication_source_identifier_example'),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('StorageEncrypted', True),
                    ('KmsKeyId', 'kms_key_id_example'),
                    ('PreSignedUrl', 'pre_signed_url_example'),
                    ('EnableIAMDatabaseAuthentication', True),
                    ('EnableCloudwatchLogsExports', ['enable_cloudwatch_logs_exports_example']),
                    ('DeletionProtection', True),
                    ('ServerlessV2ScalingConfiguration', openapi_server.GETCreateDBClusterServerlessV2ScalingConfigurationParameter()),
                    ('GlobalClusterIdentifier', 'global_cluster_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_db_cluster_endpoint(client):
    """Test case for g_et_create_db_cluster_endpoint

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('DBClusterEndpointIdentifier', 'db_cluster_endpoint_identifier_example'),
                    ('EndpointType', 'endpoint_type_example'),
                    ('StaticMembers', ['static_members_example']),
                    ('ExcludedMembers', ['excluded_members_example']),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDBClusterEndpoint',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_db_cluster_parameter_group(client):
    """Test case for g_et_create_db_cluster_parameter_group

    
    """
    params = [('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('DBParameterGroupFamily', 'db_parameter_group_family_example'),
                    ('Description', 'description_example'),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDBClusterParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_db_cluster_snapshot(client):
    """Test case for g_et_create_db_cluster_snapshot

    
    """
    params = [('DBClusterSnapshotIdentifier', 'db_cluster_snapshot_identifier_example'),
                    ('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDBClusterSnapshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_db_instance(client):
    """Test case for g_et_create_db_instance

    
    """
    params = [('DBName', 'db_name_example'),
                    ('DBInstanceIdentifier', 'db_instance_identifier_example'),
                    ('AllocatedStorage', 56),
                    ('DBInstanceClass', 'db_instance_class_example'),
                    ('Engine', 'engine_example'),
                    ('MasterUsername', 'master_username_example'),
                    ('MasterUserPassword', 'master_user_password_example'),
                    ('DBSecurityGroups', ['db_security_groups_example']),
                    ('VpcSecurityGroupIds', ['vpc_security_group_ids_example']),
                    ('AvailabilityZone', 'availability_zone_example'),
                    ('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('PreferredMaintenanceWindow', 'preferred_maintenance_window_example'),
                    ('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('BackupRetentionPeriod', 56),
                    ('PreferredBackupWindow', 'preferred_backup_window_example'),
                    ('Port', 56),
                    ('MultiAZ', True),
                    ('EngineVersion', 'engine_version_example'),
                    ('AutoMinorVersionUpgrade', True),
                    ('LicenseModel', 'license_model_example'),
                    ('Iops', 56),
                    ('OptionGroupName', 'option_group_name_example'),
                    ('CharacterSetName', 'character_set_name_example'),
                    ('PubliclyAccessible', True),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('StorageType', 'storage_type_example'),
                    ('TdeCredentialArn', 'tde_credential_arn_example'),
                    ('TdeCredentialPassword', 'tde_credential_password_example'),
                    ('StorageEncrypted', True),
                    ('KmsKeyId', 'kms_key_id_example'),
                    ('Domain', 'domain_example'),
                    ('CopyTagsToSnapshot', True),
                    ('MonitoringInterval', 56),
                    ('MonitoringRoleArn', 'monitoring_role_arn_example'),
                    ('DomainIAMRoleName', 'domain_iam_role_name_example'),
                    ('PromotionTier', 56),
                    ('Timezone', 'timezone_example'),
                    ('EnableIAMDatabaseAuthentication', True),
                    ('EnablePerformanceInsights', True),
                    ('PerformanceInsightsKMSKeyId', 'performance_insights_kms_key_id_example'),
                    ('EnableCloudwatchLogsExports', ['enable_cloudwatch_logs_exports_example']),
                    ('DeletionProtection', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDBInstance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_db_parameter_group(client):
    """Test case for g_et_create_db_parameter_group

    
    """
    params = [('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('DBParameterGroupFamily', 'db_parameter_group_family_example'),
                    ('Description', 'description_example'),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDBParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_db_subnet_group(client):
    """Test case for g_et_create_db_subnet_group

    
    """
    params = [('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('DBSubnetGroupDescription', 'db_subnet_group_description_example'),
                    ('SubnetIds', ['subnet_ids_example']),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateDBSubnetGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_event_subscription(client):
    """Test case for g_et_create_event_subscription

    
    """
    params = [('SubscriptionName', 'subscription_name_example'),
                    ('SnsTopicArn', 'sns_topic_arn_example'),
                    ('SourceType', 'source_type_example'),
                    ('EventCategories', ['event_categories_example']),
                    ('SourceIds', ['source_ids_example']),
                    ('Enabled', True),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateEventSubscription',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_global_cluster(client):
    """Test case for g_et_create_global_cluster

    
    """
    params = [('GlobalClusterIdentifier', 'global_cluster_identifier_example'),
                    ('SourceDBClusterIdentifier', 'source_db_cluster_identifier_example'),
                    ('Engine', 'engine_example'),
                    ('EngineVersion', 'engine_version_example'),
                    ('DeletionProtection', True),
                    ('StorageEncrypted', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=CreateGlobalCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_db_cluster(client):
    """Test case for g_et_delete_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('SkipFinalSnapshot', True),
                    ('FinalDBSnapshotIdentifier', 'final_db_snapshot_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_db_cluster_endpoint(client):
    """Test case for g_et_delete_db_cluster_endpoint

    
    """
    params = [('DBClusterEndpointIdentifier', 'db_cluster_endpoint_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDBClusterEndpoint',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_db_cluster_parameter_group(client):
    """Test case for g_et_delete_db_cluster_parameter_group

    
    """
    params = [('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDBClusterParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_db_cluster_snapshot(client):
    """Test case for g_et_delete_db_cluster_snapshot

    
    """
    params = [('DBClusterSnapshotIdentifier', 'db_cluster_snapshot_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDBClusterSnapshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_db_instance(client):
    """Test case for g_et_delete_db_instance

    
    """
    params = [('DBInstanceIdentifier', 'db_instance_identifier_example'),
                    ('SkipFinalSnapshot', True),
                    ('FinalDBSnapshotIdentifier', 'final_db_snapshot_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDBInstance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_db_parameter_group(client):
    """Test case for g_et_delete_db_parameter_group

    
    """
    params = [('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDBParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_db_subnet_group(client):
    """Test case for g_et_delete_db_subnet_group

    
    """
    params = [('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteDBSubnetGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_event_subscription(client):
    """Test case for g_et_delete_event_subscription

    
    """
    params = [('SubscriptionName', 'subscription_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteEventSubscription',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_delete_global_cluster(client):
    """Test case for g_et_delete_global_cluster

    
    """
    params = [('GlobalClusterIdentifier', 'global_cluster_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DeleteGlobalCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_cluster_endpoints(client):
    """Test case for g_et_describe_db_cluster_endpoints

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('DBClusterEndpointIdentifier', 'db_cluster_endpoint_identifier_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBClusterEndpoints',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_cluster_parameter_groups(client):
    """Test case for g_et_describe_db_cluster_parameter_groups

    
    """
    params = [('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBClusterParameterGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_cluster_parameters(client):
    """Test case for g_et_describe_db_cluster_parameters

    
    """
    params = [('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('Source', 'source_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBClusterParameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_cluster_snapshot_attributes(client):
    """Test case for g_et_describe_db_cluster_snapshot_attributes

    
    """
    params = [('DBClusterSnapshotIdentifier', 'db_cluster_snapshot_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBClusterSnapshotAttributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_cluster_snapshots(client):
    """Test case for g_et_describe_db_cluster_snapshots

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('DBClusterSnapshotIdentifier', 'db_cluster_snapshot_identifier_example'),
                    ('SnapshotType', 'snapshot_type_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('IncludeShared', True),
                    ('IncludePublic', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBClusterSnapshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_clusters(client):
    """Test case for g_et_describe_db_clusters

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBClusters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_engine_versions(client):
    """Test case for g_et_describe_db_engine_versions

    
    """
    params = [('Engine', 'engine_example'),
                    ('EngineVersion', 'engine_version_example'),
                    ('DBParameterGroupFamily', 'db_parameter_group_family_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('DefaultOnly', True),
                    ('ListSupportedCharacterSets', True),
                    ('ListSupportedTimezones', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBEngineVersions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_instances(client):
    """Test case for g_et_describe_db_instances

    
    """
    params = [('DBInstanceIdentifier', 'db_instance_identifier_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBInstances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_parameter_groups(client):
    """Test case for g_et_describe_db_parameter_groups

    
    """
    params = [('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBParameterGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_parameters(client):
    """Test case for g_et_describe_db_parameters

    
    """
    params = [('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('Source', 'source_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBParameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_db_subnet_groups(client):
    """Test case for g_et_describe_db_subnet_groups

    
    """
    params = [('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeDBSubnetGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_engine_default_cluster_parameters(client):
    """Test case for g_et_describe_engine_default_cluster_parameters

    
    """
    params = [('DBParameterGroupFamily', 'db_parameter_group_family_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeEngineDefaultClusterParameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_engine_default_parameters(client):
    """Test case for g_et_describe_engine_default_parameters

    
    """
    params = [('DBParameterGroupFamily', 'db_parameter_group_family_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeEngineDefaultParameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_event_categories(client):
    """Test case for g_et_describe_event_categories

    
    """
    params = [('SourceType', 'source_type_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeEventCategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_event_subscriptions(client):
    """Test case for g_et_describe_event_subscriptions

    
    """
    params = [('SubscriptionName', 'subscription_name_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeEventSubscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_events(client):
    """Test case for g_et_describe_events

    
    """
    params = [('SourceIdentifier', 'source_identifier_example'),
                    ('SourceType', 'source_type_example'),
                    ('StartTime', '2013-10-20T19:20:30+01:00'),
                    ('EndTime', '2013-10-20T19:20:30+01:00'),
                    ('Duration', 56),
                    ('EventCategories', ['event_categories_example']),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeEvents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_global_clusters(client):
    """Test case for g_et_describe_global_clusters

    
    """
    params = [('GlobalClusterIdentifier', 'global_cluster_identifier_example'),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeGlobalClusters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_orderable_db_instance_options(client):
    """Test case for g_et_describe_orderable_db_instance_options

    
    """
    params = [('Engine', 'engine_example'),
                    ('EngineVersion', 'engine_version_example'),
                    ('DBInstanceClass', 'db_instance_class_example'),
                    ('LicenseModel', 'license_model_example'),
                    ('Vpc', True),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('MaxRecords', 56),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeOrderableDBInstanceOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_pending_maintenance_actions(client):
    """Test case for g_et_describe_pending_maintenance_actions

    
    """
    params = [('ResourceIdentifier', 'resource_identifier_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('Marker', 'marker_example'),
                    ('MaxRecords', 56),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribePendingMaintenanceActions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_describe_valid_db_instance_modifications(client):
    """Test case for g_et_describe_valid_db_instance_modifications

    
    """
    params = [('DBInstanceIdentifier', 'db_instance_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=DescribeValidDBInstanceModifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_failover_db_cluster(client):
    """Test case for g_et_failover_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('TargetDBInstanceIdentifier', 'target_db_instance_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=FailoverDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_failover_global_cluster(client):
    """Test case for g_et_failover_global_cluster

    
    """
    params = [('GlobalClusterIdentifier', 'global_cluster_identifier_example'),
                    ('TargetDbClusterIdentifier', 'target_db_cluster_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=FailoverGlobalCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_list_tags_for_resource(client):
    """Test case for g_et_list_tags_for_resource

    
    """
    params = [('ResourceName', 'resource_name_example'),
                    ('Filters', [openapi_server.GETDescribeDBClusterEndpointsFiltersParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ListTagsForResource',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_db_cluster(client):
    """Test case for g_et_modify_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('NewDBClusterIdentifier', 'new_db_cluster_identifier_example'),
                    ('ApplyImmediately', True),
                    ('BackupRetentionPeriod', 56),
                    ('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('VpcSecurityGroupIds', ['vpc_security_group_ids_example']),
                    ('Port', 56),
                    ('MasterUserPassword', 'master_user_password_example'),
                    ('OptionGroupName', 'option_group_name_example'),
                    ('PreferredBackupWindow', 'preferred_backup_window_example'),
                    ('PreferredMaintenanceWindow', 'preferred_maintenance_window_example'),
                    ('EnableIAMDatabaseAuthentication', True),
                    ('CloudwatchLogsExportConfiguration', openapi_server.GETModifyDBClusterCloudwatchLogsExportConfigurationParameter()),
                    ('EngineVersion', 'engine_version_example'),
                    ('AllowMajorVersionUpgrade', True),
                    ('DBInstanceParameterGroupName', 'db_instance_parameter_group_name_example'),
                    ('DeletionProtection', True),
                    ('CopyTagsToSnapshot', True),
                    ('ServerlessV2ScalingConfiguration', openapi_server.GETCreateDBClusterServerlessV2ScalingConfigurationParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_db_cluster_endpoint(client):
    """Test case for g_et_modify_db_cluster_endpoint

    
    """
    params = [('DBClusterEndpointIdentifier', 'db_cluster_endpoint_identifier_example'),
                    ('EndpointType', 'endpoint_type_example'),
                    ('StaticMembers', ['static_members_example']),
                    ('ExcludedMembers', ['excluded_members_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyDBClusterEndpoint',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_db_cluster_parameter_group(client):
    """Test case for g_et_modify_db_cluster_parameter_group

    
    """
    params = [('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('Parameters', [openapi_server.GETModifyDBClusterParameterGroupParametersParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyDBClusterParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_db_cluster_snapshot_attribute(client):
    """Test case for g_et_modify_db_cluster_snapshot_attribute

    
    """
    params = [('DBClusterSnapshotIdentifier', 'db_cluster_snapshot_identifier_example'),
                    ('AttributeName', 'attribute_name_example'),
                    ('ValuesToAdd', ['values_to_add_example']),
                    ('ValuesToRemove', ['values_to_remove_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyDBClusterSnapshotAttribute',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_db_instance(client):
    """Test case for g_et_modify_db_instance

    
    """
    params = [('DBInstanceIdentifier', 'db_instance_identifier_example'),
                    ('AllocatedStorage', 56),
                    ('DBInstanceClass', 'db_instance_class_example'),
                    ('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('DBSecurityGroups', ['db_security_groups_example']),
                    ('VpcSecurityGroupIds', ['vpc_security_group_ids_example']),
                    ('ApplyImmediately', True),
                    ('MasterUserPassword', 'master_user_password_example'),
                    ('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('BackupRetentionPeriod', 56),
                    ('PreferredBackupWindow', 'preferred_backup_window_example'),
                    ('PreferredMaintenanceWindow', 'preferred_maintenance_window_example'),
                    ('MultiAZ', True),
                    ('EngineVersion', 'engine_version_example'),
                    ('AllowMajorVersionUpgrade', True),
                    ('AutoMinorVersionUpgrade', True),
                    ('LicenseModel', 'license_model_example'),
                    ('Iops', 56),
                    ('OptionGroupName', 'option_group_name_example'),
                    ('NewDBInstanceIdentifier', 'new_db_instance_identifier_example'),
                    ('StorageType', 'storage_type_example'),
                    ('TdeCredentialArn', 'tde_credential_arn_example'),
                    ('TdeCredentialPassword', 'tde_credential_password_example'),
                    ('CACertificateIdentifier', 'ca_certificate_identifier_example'),
                    ('Domain', 'domain_example'),
                    ('CopyTagsToSnapshot', True),
                    ('MonitoringInterval', 56),
                    ('DBPortNumber', 56),
                    ('PubliclyAccessible', True),
                    ('MonitoringRoleArn', 'monitoring_role_arn_example'),
                    ('DomainIAMRoleName', 'domain_iam_role_name_example'),
                    ('PromotionTier', 56),
                    ('EnableIAMDatabaseAuthentication', True),
                    ('EnablePerformanceInsights', True),
                    ('PerformanceInsightsKMSKeyId', 'performance_insights_kms_key_id_example'),
                    ('CloudwatchLogsExportConfiguration', openapi_server.GETModifyDBClusterCloudwatchLogsExportConfigurationParameter()),
                    ('DeletionProtection', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyDBInstance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_db_parameter_group(client):
    """Test case for g_et_modify_db_parameter_group

    
    """
    params = [('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('Parameters', [openapi_server.GETModifyDBClusterParameterGroupParametersParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyDBParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_db_subnet_group(client):
    """Test case for g_et_modify_db_subnet_group

    
    """
    params = [('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('DBSubnetGroupDescription', 'db_subnet_group_description_example'),
                    ('SubnetIds', ['subnet_ids_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyDBSubnetGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_event_subscription(client):
    """Test case for g_et_modify_event_subscription

    
    """
    params = [('SubscriptionName', 'subscription_name_example'),
                    ('SnsTopicArn', 'sns_topic_arn_example'),
                    ('SourceType', 'source_type_example'),
                    ('EventCategories', ['event_categories_example']),
                    ('Enabled', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyEventSubscription',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_modify_global_cluster(client):
    """Test case for g_et_modify_global_cluster

    
    """
    params = [('GlobalClusterIdentifier', 'global_cluster_identifier_example'),
                    ('NewGlobalClusterIdentifier', 'new_global_cluster_identifier_example'),
                    ('DeletionProtection', True),
                    ('EngineVersion', 'engine_version_example'),
                    ('AllowMajorVersionUpgrade', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ModifyGlobalCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_promote_read_replica_db_cluster(client):
    """Test case for g_et_promote_read_replica_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=PromoteReadReplicaDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_reboot_db_instance(client):
    """Test case for g_et_reboot_db_instance

    
    """
    params = [('DBInstanceIdentifier', 'db_instance_identifier_example'),
                    ('ForceFailover', True),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=RebootDBInstance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_remove_from_global_cluster(client):
    """Test case for g_et_remove_from_global_cluster

    
    """
    params = [('GlobalClusterIdentifier', 'global_cluster_identifier_example'),
                    ('DbClusterIdentifier', 'db_cluster_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=RemoveFromGlobalCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_remove_role_from_db_cluster(client):
    """Test case for g_et_remove_role_from_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('RoleArn', 'role_arn_example'),
                    ('FeatureName', 'feature_name_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=RemoveRoleFromDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_remove_source_identifier_from_subscription(client):
    """Test case for g_et_remove_source_identifier_from_subscription

    
    """
    params = [('SubscriptionName', 'subscription_name_example'),
                    ('SourceIdentifier', 'source_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=RemoveSourceIdentifierFromSubscription',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_remove_tags_from_resource(client):
    """Test case for g_et_remove_tags_from_resource

    
    """
    params = [('ResourceName', 'resource_name_example'),
                    ('TagKeys', ['tag_keys_example']),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=RemoveTagsFromResource',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_reset_db_cluster_parameter_group(client):
    """Test case for g_et_reset_db_cluster_parameter_group

    
    """
    params = [('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('ResetAllParameters', True),
                    ('Parameters', [openapi_server.GETModifyDBClusterParameterGroupParametersParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ResetDBClusterParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_reset_db_parameter_group(client):
    """Test case for g_et_reset_db_parameter_group

    
    """
    params = [('DBParameterGroupName', 'db_parameter_group_name_example'),
                    ('ResetAllParameters', True),
                    ('Parameters', [openapi_server.GETModifyDBClusterParameterGroupParametersParameterInner()]),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=ResetDBParameterGroup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_restore_db_cluster_from_snapshot(client):
    """Test case for g_et_restore_db_cluster_from_snapshot

    
    """
    params = [('AvailabilityZones', ['availability_zones_example']),
                    ('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('SnapshotIdentifier', 'snapshot_identifier_example'),
                    ('Engine', 'engine_example'),
                    ('EngineVersion', 'engine_version_example'),
                    ('Port', 56),
                    ('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('DatabaseName', 'database_name_example'),
                    ('OptionGroupName', 'option_group_name_example'),
                    ('VpcSecurityGroupIds', ['vpc_security_group_ids_example']),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('KmsKeyId', 'kms_key_id_example'),
                    ('EnableIAMDatabaseAuthentication', True),
                    ('EnableCloudwatchLogsExports', ['enable_cloudwatch_logs_exports_example']),
                    ('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('DeletionProtection', True),
                    ('CopyTagsToSnapshot', True),
                    ('ServerlessV2ScalingConfiguration', openapi_server.GETCreateDBClusterServerlessV2ScalingConfigurationParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=RestoreDBClusterFromSnapshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_restore_db_cluster_to_point_in_time(client):
    """Test case for g_et_restore_db_cluster_to_point_in_time

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('RestoreType', 'restore_type_example'),
                    ('SourceDBClusterIdentifier', 'source_db_cluster_identifier_example'),
                    ('RestoreToTime', '2013-10-20T19:20:30+01:00'),
                    ('UseLatestRestorableTime', True),
                    ('Port', 56),
                    ('DBSubnetGroupName', 'db_subnet_group_name_example'),
                    ('OptionGroupName', 'option_group_name_example'),
                    ('VpcSecurityGroupIds', ['vpc_security_group_ids_example']),
                    ('Tags', [openapi_server.GETAddTagsToResourceTagsParameterInner()]),
                    ('KmsKeyId', 'kms_key_id_example'),
                    ('EnableIAMDatabaseAuthentication', True),
                    ('EnableCloudwatchLogsExports', ['enable_cloudwatch_logs_exports_example']),
                    ('DBClusterParameterGroupName', 'db_cluster_parameter_group_name_example'),
                    ('DeletionProtection', True),
                    ('ServerlessV2ScalingConfiguration', openapi_server.GETCreateDBClusterServerlessV2ScalingConfigurationParameter()),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=RestoreDBClusterToPointInTime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_start_db_cluster(client):
    """Test case for g_et_start_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=StartDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_stop_db_cluster(client):
    """Test case for g_et_stop_db_cluster

    
    """
    params = [('DBClusterIdentifier', 'db_cluster_identifier_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Action=StopDBCluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_add_role_to_db_cluster(client):
    """Test case for p_ost_add_role_to_db_cluster

    
    """
    body = openapi_server.AddRoleToDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=AddRoleToDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_add_source_identifier_to_subscription(client):
    """Test case for p_ost_add_source_identifier_to_subscription

    
    """
    body = openapi_server.AddSourceIdentifierToSubscriptionMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=AddSourceIdentifierToSubscription',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_add_tags_to_resource(client):
    """Test case for p_ost_add_tags_to_resource

    
    """
    body = openapi_server.AddTagsToResourceMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=AddTagsToResource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_apply_pending_maintenance_action(client):
    """Test case for p_ost_apply_pending_maintenance_action

    
    """
    body = openapi_server.ApplyPendingMaintenanceActionMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ApplyPendingMaintenanceAction',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_copy_db_cluster_parameter_group(client):
    """Test case for p_ost_copy_db_cluster_parameter_group

    
    """
    body = openapi_server.CopyDBClusterParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CopyDBClusterParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_copy_db_cluster_snapshot(client):
    """Test case for p_ost_copy_db_cluster_snapshot

    
    """
    body = openapi_server.CopyDBClusterSnapshotMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CopyDBClusterSnapshot',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_copy_db_parameter_group(client):
    """Test case for p_ost_copy_db_parameter_group

    
    """
    body = openapi_server.CopyDBParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CopyDBParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_db_cluster(client):
    """Test case for p_ost_create_db_cluster

    
    """
    body = openapi_server.CreateDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_db_cluster_endpoint(client):
    """Test case for p_ost_create_db_cluster_endpoint

    
    """
    body = openapi_server.CreateDBClusterEndpointMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDBClusterEndpoint',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_db_cluster_parameter_group(client):
    """Test case for p_ost_create_db_cluster_parameter_group

    
    """
    body = openapi_server.CreateDBClusterParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDBClusterParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_db_cluster_snapshot(client):
    """Test case for p_ost_create_db_cluster_snapshot

    
    """
    body = openapi_server.CreateDBClusterSnapshotMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDBClusterSnapshot',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_db_instance(client):
    """Test case for p_ost_create_db_instance

    
    """
    body = openapi_server.CreateDBInstanceMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDBInstance',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_db_parameter_group(client):
    """Test case for p_ost_create_db_parameter_group

    
    """
    body = openapi_server.CreateDBParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDBParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_db_subnet_group(client):
    """Test case for p_ost_create_db_subnet_group

    
    """
    body = openapi_server.CreateDBSubnetGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateDBSubnetGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_event_subscription(client):
    """Test case for p_ost_create_event_subscription

    
    """
    body = openapi_server.CreateEventSubscriptionMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateEventSubscription',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_global_cluster(client):
    """Test case for p_ost_create_global_cluster

    
    """
    body = openapi_server.CreateGlobalClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=CreateGlobalCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_db_cluster(client):
    """Test case for p_ost_delete_db_cluster

    
    """
    body = openapi_server.DeleteDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_db_cluster_endpoint(client):
    """Test case for p_ost_delete_db_cluster_endpoint

    
    """
    body = openapi_server.DeleteDBClusterEndpointMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDBClusterEndpoint',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_db_cluster_parameter_group(client):
    """Test case for p_ost_delete_db_cluster_parameter_group

    
    """
    body = openapi_server.DeleteDBClusterParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDBClusterParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_db_cluster_snapshot(client):
    """Test case for p_ost_delete_db_cluster_snapshot

    
    """
    body = openapi_server.DeleteDBClusterSnapshotMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDBClusterSnapshot',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_db_instance(client):
    """Test case for p_ost_delete_db_instance

    
    """
    body = openapi_server.DeleteDBInstanceMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDBInstance',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_db_parameter_group(client):
    """Test case for p_ost_delete_db_parameter_group

    
    """
    body = openapi_server.DeleteDBParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDBParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_db_subnet_group(client):
    """Test case for p_ost_delete_db_subnet_group

    
    """
    body = openapi_server.DeleteDBSubnetGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteDBSubnetGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_event_subscription(client):
    """Test case for p_ost_delete_event_subscription

    
    """
    body = openapi_server.DeleteEventSubscriptionMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteEventSubscription',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_delete_global_cluster(client):
    """Test case for p_ost_delete_global_cluster

    
    """
    body = openapi_server.DeleteGlobalClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DeleteGlobalCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_cluster_endpoints(client):
    """Test case for p_ost_describe_db_cluster_endpoints

    
    """
    body = openapi_server.DescribeDBClusterEndpointsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBClusterEndpoints',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_cluster_parameter_groups(client):
    """Test case for p_ost_describe_db_cluster_parameter_groups

    
    """
    body = openapi_server.DescribeDBClusterParameterGroupsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBClusterParameterGroups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_cluster_parameters(client):
    """Test case for p_ost_describe_db_cluster_parameters

    
    """
    body = openapi_server.DescribeDBClusterParametersMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBClusterParameters',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_cluster_snapshot_attributes(client):
    """Test case for p_ost_describe_db_cluster_snapshot_attributes

    
    """
    body = openapi_server.DescribeDBClusterSnapshotAttributesMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBClusterSnapshotAttributes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_cluster_snapshots(client):
    """Test case for p_ost_describe_db_cluster_snapshots

    
    """
    body = openapi_server.DescribeDBClusterSnapshotsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBClusterSnapshots',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_clusters(client):
    """Test case for p_ost_describe_db_clusters

    
    """
    body = openapi_server.DescribeDBClustersMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBClusters',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_engine_versions(client):
    """Test case for p_ost_describe_db_engine_versions

    
    """
    body = openapi_server.DescribeDBEngineVersionsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBEngineVersions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_instances(client):
    """Test case for p_ost_describe_db_instances

    
    """
    body = openapi_server.DescribeDBInstancesMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBInstances',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_parameter_groups(client):
    """Test case for p_ost_describe_db_parameter_groups

    
    """
    body = openapi_server.DescribeDBParameterGroupsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBParameterGroups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_parameters(client):
    """Test case for p_ost_describe_db_parameters

    
    """
    body = openapi_server.DescribeDBParametersMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBParameters',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_db_subnet_groups(client):
    """Test case for p_ost_describe_db_subnet_groups

    
    """
    body = openapi_server.DescribeDBSubnetGroupsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeDBSubnetGroups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_engine_default_cluster_parameters(client):
    """Test case for p_ost_describe_engine_default_cluster_parameters

    
    """
    body = openapi_server.DescribeEngineDefaultClusterParametersMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeEngineDefaultClusterParameters',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_engine_default_parameters(client):
    """Test case for p_ost_describe_engine_default_parameters

    
    """
    body = openapi_server.DescribeEngineDefaultParametersMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeEngineDefaultParameters',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_event_categories(client):
    """Test case for p_ost_describe_event_categories

    
    """
    body = openapi_server.DescribeEventCategoriesMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeEventCategories',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_event_subscriptions(client):
    """Test case for p_ost_describe_event_subscriptions

    
    """
    body = openapi_server.DescribeEventSubscriptionsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeEventSubscriptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_events(client):
    """Test case for p_ost_describe_events

    
    """
    body = openapi_server.DescribeEventsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeEvents',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_global_clusters(client):
    """Test case for p_ost_describe_global_clusters

    
    """
    body = openapi_server.DescribeGlobalClustersMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeGlobalClusters',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_orderable_db_instance_options(client):
    """Test case for p_ost_describe_orderable_db_instance_options

    
    """
    body = openapi_server.DescribeOrderableDBInstanceOptionsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeOrderableDBInstanceOptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_pending_maintenance_actions(client):
    """Test case for p_ost_describe_pending_maintenance_actions

    
    """
    body = openapi_server.DescribePendingMaintenanceActionsMessage()
    params = [('MaxRecords', 'max_records_example'),
                    ('Marker', 'marker_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribePendingMaintenanceActions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_describe_valid_db_instance_modifications(client):
    """Test case for p_ost_describe_valid_db_instance_modifications

    
    """
    body = openapi_server.DescribeValidDBInstanceModificationsMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=DescribeValidDBInstanceModifications',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_failover_db_cluster(client):
    """Test case for p_ost_failover_db_cluster

    
    """
    body = openapi_server.FailoverDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=FailoverDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_failover_global_cluster(client):
    """Test case for p_ost_failover_global_cluster

    
    """
    body = openapi_server.FailoverGlobalClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=FailoverGlobalCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_list_tags_for_resource(client):
    """Test case for p_ost_list_tags_for_resource

    
    """
    body = openapi_server.ListTagsForResourceMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ListTagsForResource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_db_cluster(client):
    """Test case for p_ost_modify_db_cluster

    
    """
    body = openapi_server.ModifyDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_db_cluster_endpoint(client):
    """Test case for p_ost_modify_db_cluster_endpoint

    
    """
    body = openapi_server.ModifyDBClusterEndpointMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyDBClusterEndpoint',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_db_cluster_parameter_group(client):
    """Test case for p_ost_modify_db_cluster_parameter_group

    
    """
    body = openapi_server.ModifyDBClusterParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyDBClusterParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_db_cluster_snapshot_attribute(client):
    """Test case for p_ost_modify_db_cluster_snapshot_attribute

    
    """
    body = openapi_server.ModifyDBClusterSnapshotAttributeMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyDBClusterSnapshotAttribute',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_db_instance(client):
    """Test case for p_ost_modify_db_instance

    
    """
    body = openapi_server.ModifyDBInstanceMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyDBInstance',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_db_parameter_group(client):
    """Test case for p_ost_modify_db_parameter_group

    
    """
    body = openapi_server.ModifyDBParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyDBParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_db_subnet_group(client):
    """Test case for p_ost_modify_db_subnet_group

    
    """
    body = openapi_server.ModifyDBSubnetGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyDBSubnetGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_event_subscription(client):
    """Test case for p_ost_modify_event_subscription

    
    """
    body = openapi_server.ModifyEventSubscriptionMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyEventSubscription',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_modify_global_cluster(client):
    """Test case for p_ost_modify_global_cluster

    
    """
    body = openapi_server.ModifyGlobalClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ModifyGlobalCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_promote_read_replica_db_cluster(client):
    """Test case for p_ost_promote_read_replica_db_cluster

    
    """
    body = openapi_server.PromoteReadReplicaDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=PromoteReadReplicaDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_reboot_db_instance(client):
    """Test case for p_ost_reboot_db_instance

    
    """
    body = openapi_server.RebootDBInstanceMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=RebootDBInstance',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_remove_from_global_cluster(client):
    """Test case for p_ost_remove_from_global_cluster

    
    """
    body = openapi_server.RemoveFromGlobalClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=RemoveFromGlobalCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_remove_role_from_db_cluster(client):
    """Test case for p_ost_remove_role_from_db_cluster

    
    """
    body = openapi_server.RemoveRoleFromDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=RemoveRoleFromDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_remove_source_identifier_from_subscription(client):
    """Test case for p_ost_remove_source_identifier_from_subscription

    
    """
    body = openapi_server.RemoveSourceIdentifierFromSubscriptionMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=RemoveSourceIdentifierFromSubscription',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_remove_tags_from_resource(client):
    """Test case for p_ost_remove_tags_from_resource

    
    """
    body = openapi_server.RemoveTagsFromResourceMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=RemoveTagsFromResource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_reset_db_cluster_parameter_group(client):
    """Test case for p_ost_reset_db_cluster_parameter_group

    
    """
    body = openapi_server.ResetDBClusterParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ResetDBClusterParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_reset_db_parameter_group(client):
    """Test case for p_ost_reset_db_parameter_group

    
    """
    body = openapi_server.ResetDBParameterGroupMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=ResetDBParameterGroup',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_restore_db_cluster_from_snapshot(client):
    """Test case for p_ost_restore_db_cluster_from_snapshot

    
    """
    body = openapi_server.RestoreDBClusterFromSnapshotMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=RestoreDBClusterFromSnapshot',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_restore_db_cluster_to_point_in_time(client):
    """Test case for p_ost_restore_db_cluster_to_point_in_time

    
    """
    body = openapi_server.RestoreDBClusterToPointInTimeMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=RestoreDBClusterToPointInTime',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_start_db_cluster(client):
    """Test case for p_ost_start_db_cluster

    
    """
    body = openapi_server.StartDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=StartDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_stop_db_cluster(client):
    """Test case for p_ost_stop_db_cluster

    
    """
    body = openapi_server.StopDBClusterMessage()
    params = [('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Action=StopDBCluster',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

