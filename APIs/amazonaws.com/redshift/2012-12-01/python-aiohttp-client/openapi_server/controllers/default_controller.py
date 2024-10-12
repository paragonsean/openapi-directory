from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_reserved_node_exchange_input_message import AcceptReservedNodeExchangeInputMessage
from openapi_server.models.accept_reserved_node_exchange_output_message import AcceptReservedNodeExchangeOutputMessage
from openapi_server.models.account_attribute_list import AccountAttributeList
from openapi_server.models.associate_data_share_consumer_message import AssociateDataShareConsumerMessage
from openapi_server.models.authorize_cluster_security_group_ingress_message import AuthorizeClusterSecurityGroupIngressMessage
from openapi_server.models.authorize_cluster_security_group_ingress_result import AuthorizeClusterSecurityGroupIngressResult
from openapi_server.models.authorize_data_share_message import AuthorizeDataShareMessage
from openapi_server.models.authorize_endpoint_access_message import AuthorizeEndpointAccessMessage
from openapi_server.models.authorize_snapshot_access_message import AuthorizeSnapshotAccessMessage
from openapi_server.models.authorize_snapshot_access_result import AuthorizeSnapshotAccessResult
from openapi_server.models.batch_delete_cluster_snapshots_request import BatchDeleteClusterSnapshotsRequest
from openapi_server.models.batch_delete_cluster_snapshots_result import BatchDeleteClusterSnapshotsResult
from openapi_server.models.batch_modify_cluster_snapshots_message import BatchModifyClusterSnapshotsMessage
from openapi_server.models.batch_modify_cluster_snapshots_output_message import BatchModifyClusterSnapshotsOutputMessage
from openapi_server.models.cancel_resize_message import CancelResizeMessage
from openapi_server.models.cluster_credentials import ClusterCredentials
from openapi_server.models.cluster_db_revisions_message import ClusterDbRevisionsMessage
from openapi_server.models.cluster_extended_credentials import ClusterExtendedCredentials
from openapi_server.models.cluster_parameter_group_details import ClusterParameterGroupDetails
from openapi_server.models.cluster_parameter_group_name_message import ClusterParameterGroupNameMessage
from openapi_server.models.cluster_parameter_groups_message import ClusterParameterGroupsMessage
from openapi_server.models.cluster_security_group_message import ClusterSecurityGroupMessage
from openapi_server.models.cluster_subnet_group_message import ClusterSubnetGroupMessage
from openapi_server.models.cluster_versions_message import ClusterVersionsMessage
from openapi_server.models.clusters_message import ClustersMessage
from openapi_server.models.copy_cluster_snapshot_message import CopyClusterSnapshotMessage
from openapi_server.models.copy_cluster_snapshot_result import CopyClusterSnapshotResult
from openapi_server.models.create_authentication_profile_message import CreateAuthenticationProfileMessage
from openapi_server.models.create_authentication_profile_result import CreateAuthenticationProfileResult
from openapi_server.models.create_cluster_message import CreateClusterMessage
from openapi_server.models.create_cluster_parameter_group_message import CreateClusterParameterGroupMessage
from openapi_server.models.create_cluster_parameter_group_result import CreateClusterParameterGroupResult
from openapi_server.models.create_cluster_result import CreateClusterResult
from openapi_server.models.create_cluster_security_group_message import CreateClusterSecurityGroupMessage
from openapi_server.models.create_cluster_security_group_result import CreateClusterSecurityGroupResult
from openapi_server.models.create_cluster_snapshot_message import CreateClusterSnapshotMessage
from openapi_server.models.create_cluster_snapshot_result import CreateClusterSnapshotResult
from openapi_server.models.create_cluster_subnet_group_message import CreateClusterSubnetGroupMessage
from openapi_server.models.create_cluster_subnet_group_result import CreateClusterSubnetGroupResult
from openapi_server.models.create_custom_domain_association_message import CreateCustomDomainAssociationMessage
from openapi_server.models.create_custom_domain_association_result import CreateCustomDomainAssociationResult
from openapi_server.models.create_endpoint_access_message import CreateEndpointAccessMessage
from openapi_server.models.create_event_subscription_message import CreateEventSubscriptionMessage
from openapi_server.models.create_event_subscription_result import CreateEventSubscriptionResult
from openapi_server.models.create_hsm_client_certificate_message import CreateHsmClientCertificateMessage
from openapi_server.models.create_hsm_client_certificate_result import CreateHsmClientCertificateResult
from openapi_server.models.create_hsm_configuration_message import CreateHsmConfigurationMessage
from openapi_server.models.create_hsm_configuration_result import CreateHsmConfigurationResult
from openapi_server.models.create_scheduled_action_message import CreateScheduledActionMessage
from openapi_server.models.create_snapshot_copy_grant_message import CreateSnapshotCopyGrantMessage
from openapi_server.models.create_snapshot_copy_grant_result import CreateSnapshotCopyGrantResult
from openapi_server.models.create_snapshot_schedule_message import CreateSnapshotScheduleMessage
from openapi_server.models.create_tags_message import CreateTagsMessage
from openapi_server.models.create_usage_limit_message import CreateUsageLimitMessage
from openapi_server.models.custom_domain_associations_message import CustomDomainAssociationsMessage
from openapi_server.models.customer_storage_message import CustomerStorageMessage
from openapi_server.models.data_share import DataShare
from openapi_server.models.deauthorize_data_share_message import DeauthorizeDataShareMessage
from openapi_server.models.delete_authentication_profile_message import DeleteAuthenticationProfileMessage
from openapi_server.models.delete_authentication_profile_result import DeleteAuthenticationProfileResult
from openapi_server.models.delete_cluster_message import DeleteClusterMessage
from openapi_server.models.delete_cluster_parameter_group_message import DeleteClusterParameterGroupMessage
from openapi_server.models.delete_cluster_result import DeleteClusterResult
from openapi_server.models.delete_cluster_security_group_message import DeleteClusterSecurityGroupMessage
from openapi_server.models.delete_cluster_snapshot_message import DeleteClusterSnapshotMessage
from openapi_server.models.delete_cluster_snapshot_result import DeleteClusterSnapshotResult
from openapi_server.models.delete_cluster_subnet_group_message import DeleteClusterSubnetGroupMessage
from openapi_server.models.delete_custom_domain_association_message import DeleteCustomDomainAssociationMessage
from openapi_server.models.delete_endpoint_access_message import DeleteEndpointAccessMessage
from openapi_server.models.delete_event_subscription_message import DeleteEventSubscriptionMessage
from openapi_server.models.delete_hsm_client_certificate_message import DeleteHsmClientCertificateMessage
from openapi_server.models.delete_hsm_configuration_message import DeleteHsmConfigurationMessage
from openapi_server.models.delete_scheduled_action_message import DeleteScheduledActionMessage
from openapi_server.models.delete_snapshot_copy_grant_message import DeleteSnapshotCopyGrantMessage
from openapi_server.models.delete_snapshot_schedule_message import DeleteSnapshotScheduleMessage
from openapi_server.models.delete_tags_message import DeleteTagsMessage
from openapi_server.models.delete_usage_limit_message import DeleteUsageLimitMessage
from openapi_server.models.describe_account_attributes_message import DescribeAccountAttributesMessage
from openapi_server.models.describe_authentication_profiles_message import DescribeAuthenticationProfilesMessage
from openapi_server.models.describe_authentication_profiles_result import DescribeAuthenticationProfilesResult
from openapi_server.models.describe_cluster_db_revisions_message import DescribeClusterDbRevisionsMessage
from openapi_server.models.describe_cluster_parameter_groups_message import DescribeClusterParameterGroupsMessage
from openapi_server.models.describe_cluster_parameters_message import DescribeClusterParametersMessage
from openapi_server.models.describe_cluster_security_groups_message import DescribeClusterSecurityGroupsMessage
from openapi_server.models.describe_cluster_snapshots_message import DescribeClusterSnapshotsMessage
from openapi_server.models.describe_cluster_subnet_groups_message import DescribeClusterSubnetGroupsMessage
from openapi_server.models.describe_cluster_tracks_message import DescribeClusterTracksMessage
from openapi_server.models.describe_cluster_versions_message import DescribeClusterVersionsMessage
from openapi_server.models.describe_clusters_message import DescribeClustersMessage
from openapi_server.models.describe_custom_domain_associations_message import DescribeCustomDomainAssociationsMessage
from openapi_server.models.describe_data_shares_for_consumer_message import DescribeDataSharesForConsumerMessage
from openapi_server.models.describe_data_shares_for_consumer_result import DescribeDataSharesForConsumerResult
from openapi_server.models.describe_data_shares_for_producer_message import DescribeDataSharesForProducerMessage
from openapi_server.models.describe_data_shares_for_producer_result import DescribeDataSharesForProducerResult
from openapi_server.models.describe_data_shares_message import DescribeDataSharesMessage
from openapi_server.models.describe_data_shares_result import DescribeDataSharesResult
from openapi_server.models.describe_default_cluster_parameters_message import DescribeDefaultClusterParametersMessage
from openapi_server.models.describe_default_cluster_parameters_result import DescribeDefaultClusterParametersResult
from openapi_server.models.describe_endpoint_access_message import DescribeEndpointAccessMessage
from openapi_server.models.describe_endpoint_authorization_message import DescribeEndpointAuthorizationMessage
from openapi_server.models.describe_event_categories_message import DescribeEventCategoriesMessage
from openapi_server.models.describe_event_subscriptions_message import DescribeEventSubscriptionsMessage
from openapi_server.models.describe_events_message import DescribeEventsMessage
from openapi_server.models.describe_hsm_client_certificates_message import DescribeHsmClientCertificatesMessage
from openapi_server.models.describe_hsm_configurations_message import DescribeHsmConfigurationsMessage
from openapi_server.models.describe_logging_status_message import DescribeLoggingStatusMessage
from openapi_server.models.describe_node_configuration_options_message import DescribeNodeConfigurationOptionsMessage
from openapi_server.models.describe_orderable_cluster_options_message import DescribeOrderableClusterOptionsMessage
from openapi_server.models.describe_partners_input_message import DescribePartnersInputMessage
from openapi_server.models.describe_partners_output_message import DescribePartnersOutputMessage
from openapi_server.models.describe_reserved_node_exchange_status_input_message import DescribeReservedNodeExchangeStatusInputMessage
from openapi_server.models.describe_reserved_node_exchange_status_output_message import DescribeReservedNodeExchangeStatusOutputMessage
from openapi_server.models.describe_reserved_node_offerings_message import DescribeReservedNodeOfferingsMessage
from openapi_server.models.describe_reserved_nodes_message import DescribeReservedNodesMessage
from openapi_server.models.describe_resize_message import DescribeResizeMessage
from openapi_server.models.describe_scheduled_actions_message import DescribeScheduledActionsMessage
from openapi_server.models.describe_snapshot_copy_grants_message import DescribeSnapshotCopyGrantsMessage
from openapi_server.models.describe_snapshot_schedules_message import DescribeSnapshotSchedulesMessage
from openapi_server.models.describe_snapshot_schedules_output_message import DescribeSnapshotSchedulesOutputMessage
from openapi_server.models.describe_table_restore_status_message import DescribeTableRestoreStatusMessage
from openapi_server.models.describe_tags_message import DescribeTagsMessage
from openapi_server.models.describe_usage_limits_message import DescribeUsageLimitsMessage
from openapi_server.models.disable_logging_message import DisableLoggingMessage
from openapi_server.models.disable_snapshot_copy_message import DisableSnapshotCopyMessage
from openapi_server.models.disable_snapshot_copy_result import DisableSnapshotCopyResult
from openapi_server.models.disassociate_data_share_consumer_message import DisassociateDataShareConsumerMessage
from openapi_server.models.enable_logging_message import EnableLoggingMessage
from openapi_server.models.enable_snapshot_copy_message import EnableSnapshotCopyMessage
from openapi_server.models.enable_snapshot_copy_result import EnableSnapshotCopyResult
from openapi_server.models.endpoint_access import EndpointAccess
from openapi_server.models.endpoint_access_list import EndpointAccessList
from openapi_server.models.endpoint_authorization import EndpointAuthorization
from openapi_server.models.endpoint_authorization_list import EndpointAuthorizationList
from openapi_server.models.event_categories_message import EventCategoriesMessage
from openapi_server.models.event_subscriptions_message import EventSubscriptionsMessage
from openapi_server.models.events_message import EventsMessage
from openapi_server.models.get_batch_delete_cluster_snapshots_identifiers_parameter_inner import GETBatchDeleteClusterSnapshotsIdentifiersParameterInner
from openapi_server.models.get_create_cluster_tags_parameter_inner import GETCreateClusterTagsParameterInner
from openapi_server.models.get_create_scheduled_action_target_action_parameter import GETCreateScheduledActionTargetActionParameter
from openapi_server.models.get_describe_cluster_snapshots_sorting_entities_parameter_inner import GETDescribeClusterSnapshotsSortingEntitiesParameterInner
from openapi_server.models.get_describe_node_configuration_options_filter_parameter_inner import GETDescribeNodeConfigurationOptionsFilterParameterInner
from openapi_server.models.get_describe_scheduled_actions_filters_parameter_inner import GETDescribeScheduledActionsFiltersParameterInner
from openapi_server.models.get_modify_cluster_parameter_group_parameters_parameter_inner import GETModifyClusterParameterGroupParametersParameterInner
from openapi_server.models.get_cluster_credentials_message import GetClusterCredentialsMessage
from openapi_server.models.get_cluster_credentials_with_iam_message import GetClusterCredentialsWithIAMMessage
from openapi_server.models.get_reserved_node_exchange_configuration_options_input_message import GetReservedNodeExchangeConfigurationOptionsInputMessage
from openapi_server.models.get_reserved_node_exchange_configuration_options_output_message import GetReservedNodeExchangeConfigurationOptionsOutputMessage
from openapi_server.models.get_reserved_node_exchange_offerings_input_message import GetReservedNodeExchangeOfferingsInputMessage
from openapi_server.models.get_reserved_node_exchange_offerings_output_message import GetReservedNodeExchangeOfferingsOutputMessage
from openapi_server.models.hsm_client_certificate_message import HsmClientCertificateMessage
from openapi_server.models.hsm_configuration_message import HsmConfigurationMessage
from openapi_server.models.logging_status import LoggingStatus
from openapi_server.models.modify_aqua_input_message import ModifyAquaInputMessage
from openapi_server.models.modify_aqua_output_message import ModifyAquaOutputMessage
from openapi_server.models.modify_authentication_profile_message import ModifyAuthenticationProfileMessage
from openapi_server.models.modify_authentication_profile_result import ModifyAuthenticationProfileResult
from openapi_server.models.modify_cluster_db_revision_message import ModifyClusterDbRevisionMessage
from openapi_server.models.modify_cluster_db_revision_result import ModifyClusterDbRevisionResult
from openapi_server.models.modify_cluster_iam_roles_message import ModifyClusterIamRolesMessage
from openapi_server.models.modify_cluster_iam_roles_result import ModifyClusterIamRolesResult
from openapi_server.models.modify_cluster_maintenance_message import ModifyClusterMaintenanceMessage
from openapi_server.models.modify_cluster_maintenance_result import ModifyClusterMaintenanceResult
from openapi_server.models.modify_cluster_message import ModifyClusterMessage
from openapi_server.models.modify_cluster_parameter_group_message import ModifyClusterParameterGroupMessage
from openapi_server.models.modify_cluster_result import ModifyClusterResult
from openapi_server.models.modify_cluster_snapshot_message import ModifyClusterSnapshotMessage
from openapi_server.models.modify_cluster_snapshot_result import ModifyClusterSnapshotResult
from openapi_server.models.modify_cluster_snapshot_schedule_message import ModifyClusterSnapshotScheduleMessage
from openapi_server.models.modify_cluster_subnet_group_message import ModifyClusterSubnetGroupMessage
from openapi_server.models.modify_cluster_subnet_group_result import ModifyClusterSubnetGroupResult
from openapi_server.models.modify_custom_domain_association_message import ModifyCustomDomainAssociationMessage
from openapi_server.models.modify_custom_domain_association_result import ModifyCustomDomainAssociationResult
from openapi_server.models.modify_endpoint_access_message import ModifyEndpointAccessMessage
from openapi_server.models.modify_event_subscription_message import ModifyEventSubscriptionMessage
from openapi_server.models.modify_event_subscription_result import ModifyEventSubscriptionResult
from openapi_server.models.modify_scheduled_action_message import ModifyScheduledActionMessage
from openapi_server.models.modify_snapshot_copy_retention_period_message import ModifySnapshotCopyRetentionPeriodMessage
from openapi_server.models.modify_snapshot_copy_retention_period_result import ModifySnapshotCopyRetentionPeriodResult
from openapi_server.models.modify_snapshot_schedule_message import ModifySnapshotScheduleMessage
from openapi_server.models.modify_usage_limit_message import ModifyUsageLimitMessage
from openapi_server.models.node_configuration_options_message import NodeConfigurationOptionsMessage
from openapi_server.models.orderable_cluster_options_message import OrderableClusterOptionsMessage
from openapi_server.models.partner_integration_input_message import PartnerIntegrationInputMessage
from openapi_server.models.partner_integration_output_message import PartnerIntegrationOutputMessage
from openapi_server.models.pause_cluster_message import PauseClusterMessage
from openapi_server.models.pause_cluster_result import PauseClusterResult
from openapi_server.models.purchase_reserved_node_offering_message import PurchaseReservedNodeOfferingMessage
from openapi_server.models.purchase_reserved_node_offering_result import PurchaseReservedNodeOfferingResult
from openapi_server.models.reboot_cluster_message import RebootClusterMessage
from openapi_server.models.reboot_cluster_result import RebootClusterResult
from openapi_server.models.reject_data_share_message import RejectDataShareMessage
from openapi_server.models.reserved_node_offerings_message import ReservedNodeOfferingsMessage
from openapi_server.models.reserved_nodes_message import ReservedNodesMessage
from openapi_server.models.reset_cluster_parameter_group_message import ResetClusterParameterGroupMessage
from openapi_server.models.resize_cluster_message import ResizeClusterMessage
from openapi_server.models.resize_cluster_result import ResizeClusterResult
from openapi_server.models.resize_progress_message import ResizeProgressMessage
from openapi_server.models.restore_from_cluster_snapshot_message import RestoreFromClusterSnapshotMessage
from openapi_server.models.restore_from_cluster_snapshot_result import RestoreFromClusterSnapshotResult
from openapi_server.models.restore_table_from_cluster_snapshot_message import RestoreTableFromClusterSnapshotMessage
from openapi_server.models.restore_table_from_cluster_snapshot_result import RestoreTableFromClusterSnapshotResult
from openapi_server.models.resume_cluster_message import ResumeClusterMessage
from openapi_server.models.resume_cluster_result import ResumeClusterResult
from openapi_server.models.revoke_cluster_security_group_ingress_message import RevokeClusterSecurityGroupIngressMessage
from openapi_server.models.revoke_cluster_security_group_ingress_result import RevokeClusterSecurityGroupIngressResult
from openapi_server.models.revoke_endpoint_access_message import RevokeEndpointAccessMessage
from openapi_server.models.revoke_snapshot_access_message import RevokeSnapshotAccessMessage
from openapi_server.models.revoke_snapshot_access_result import RevokeSnapshotAccessResult
from openapi_server.models.rotate_encryption_key_message import RotateEncryptionKeyMessage
from openapi_server.models.rotate_encryption_key_result import RotateEncryptionKeyResult
from openapi_server.models.scheduled_action import ScheduledAction
from openapi_server.models.scheduled_actions_message import ScheduledActionsMessage
from openapi_server.models.snapshot_copy_grant_message import SnapshotCopyGrantMessage
from openapi_server.models.snapshot_message import SnapshotMessage
from openapi_server.models.snapshot_schedule import SnapshotSchedule
from openapi_server.models.table_restore_status_message import TableRestoreStatusMessage
from openapi_server.models.tagged_resource_list_message import TaggedResourceListMessage
from openapi_server.models.track_list_message import TrackListMessage
from openapi_server.models.update_partner_status_input_message import UpdatePartnerStatusInputMessage
from openapi_server.models.usage_limit import UsageLimit
from openapi_server.models.usage_limit_list import UsageLimitList
from openapi_server import util


async def g_et_accept_reserved_node_exchange(request: web.Request, reserved_node_id, target_reserved_node_offering_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_accept_reserved_node_exchange

    Exchanges a DC1 Reserved Node for a DC2 Reserved Node with no changes to the configuration (term, payment type, or number of nodes) and no additional costs. 

    :param reserved_node_id: A string representing the node identifier of the DC1 Reserved Node to be exchanged.
    :type reserved_node_id: str
    :param target_reserved_node_offering_id: The unique identifier of the DC2 Reserved Node offering to be used for the exchange. You can obtain the value for the parameter by calling &lt;a&gt;GetReservedNodeExchangeOfferings&lt;/a&gt; 
    :type target_reserved_node_offering_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_add_partner(request: web.Request, account_id, cluster_identifier, database_name, partner_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_partner

    Adds a partner integration to a cluster. This operation authorizes a partner to push status updates for the specified database. To complete the integration, you also set up the integration on the partner website.

    :param account_id: The Amazon Web Services account ID that owns the cluster.
    :type account_id: str
    :param cluster_identifier: The cluster identifier of the cluster that receives data from the partner.
    :type cluster_identifier: str
    :param database_name: The name of the database that receives data from the partner.
    :type database_name: str
    :param partner_name: The name of the partner that is authorized to send data.
    :type partner_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_associate_data_share_consumer(request: web.Request, data_share_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, associate_entire_account=None, consumer_arn=None, consumer_region=None) -> web.Response:
    """g_et_associate_data_share_consumer

    From a datashare consumer account, associates a datashare with the account (AssociateEntireAccount) or the specified namespace (ConsumerArn). If you make this association, the consumer can consume the datashare.

    :param data_share_arn: The Amazon Resource Name (ARN) of the datashare that the consumer is to use with the account or the namespace.
    :type data_share_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param associate_entire_account: A value that specifies whether the datashare is associated with the entire account.
    :type associate_entire_account: bool
    :param consumer_arn: The Amazon Resource Name (ARN) of the consumer that is associated with the datashare.
    :type consumer_arn: str
    :param consumer_region: From a datashare consumer account, associates a datashare with all existing and future namespaces in the specified Amazon Web Services Region.
    :type consumer_region: str

    """
    return web.Response(status=200)


async def g_et_authorize_cluster_security_group_ingress(request: web.Request, cluster_security_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cidrip=None, ec2_security_group_name=None, ec2_security_group_owner_id=None) -> web.Response:
    """g_et_authorize_cluster_security_group_ingress

    &lt;p&gt;Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.&lt;/p&gt; &lt;p&gt;If you authorize access to an Amazon EC2 security group, specify &lt;i&gt;EC2SecurityGroupName&lt;/i&gt; and &lt;i&gt;EC2SecurityGroupOwnerId&lt;/i&gt;. The Amazon EC2 security group and Amazon Redshift cluster must be in the same Amazon Web Services Region. &lt;/p&gt; &lt;p&gt;If you authorize access to a CIDR/IP address range, specify &lt;i&gt;CIDRIP&lt;/i&gt;. For an overview of CIDR blocks, see the Wikipedia article on &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\&quot;&gt;Classless Inter-Domain Routing&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Working with Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_security_group_name: The name of the security group to which the ingress rule is added.
    :type cluster_security_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cidrip: The IP range to be added the Amazon Redshift security group.
    :type cidrip: str
    :param ec2_security_group_name: The EC2 security group to be added the Amazon Redshift security group.
    :type ec2_security_group_name: str
    :param ec2_security_group_owner_id: &lt;p&gt;The Amazon Web Services account number of the owner of the security group specified by the &lt;i&gt;EC2SecurityGroupName&lt;/i&gt; parameter. The Amazon Web Services Access Key ID is not an acceptable value. &lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;111122223333&lt;/code&gt; &lt;/p&gt;
    :type ec2_security_group_owner_id: str

    """
    return web.Response(status=200)


async def g_et_authorize_data_share(request: web.Request, data_share_arn, consumer_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_authorize_data_share

    From a data producer account, authorizes the sharing of a datashare with one or more consumer accounts or managing entities. To authorize a datashare for a data consumer, the producer account must have the correct access permissions.

    :param data_share_arn: The Amazon Resource Name (ARN) of the datashare that producers are to authorize sharing for.
    :type data_share_arn: str
    :param consumer_identifier: The identifier of the data consumer that is authorized to access the datashare. This identifier is an Amazon Web Services account ID or a keyword, such as ADX.
    :type consumer_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_authorize_endpoint_access(request: web.Request, account, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, vpc_ids=None) -> web.Response:
    """g_et_authorize_endpoint_access

    Grants access to a cluster.

    :param account: The Amazon Web Services account ID to grant access to.
    :type account: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The cluster identifier of the cluster to grant access to.
    :type cluster_identifier: str
    :param vpc_ids: The virtual private cloud (VPC) identifiers to grant access to.
    :type vpc_ids: List[]

    """
    return web.Response(status=200)


async def g_et_authorize_snapshot_access(request: web.Request, account_with_restore_access, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, snapshot_identifier=None, snapshot_arn=None, snapshot_cluster_identifier=None) -> web.Response:
    """g_et_authorize_snapshot_access

    &lt;p&gt;Authorizes the specified Amazon Web Services account to restore the specified snapshot.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param account_with_restore_access: &lt;p&gt;The identifier of the Amazon Web Services account authorized to restore the specified snapshot.&lt;/p&gt; &lt;p&gt;To share a snapshot with Amazon Web Services Support, specify amazon-redshift-support.&lt;/p&gt;
    :type account_with_restore_access: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param snapshot_identifier: The identifier of the snapshot the account is authorized to restore.
    :type snapshot_identifier: str
    :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot to authorize access to.
    :type snapshot_arn: str
    :param snapshot_cluster_identifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
    :type snapshot_cluster_identifier: str

    """
    return web.Response(status=200)


async def g_et_batch_delete_cluster_snapshots(request: web.Request, identifiers, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_batch_delete_cluster_snapshots

    Deletes a set of cluster snapshots.

    :param identifiers: A list of identifiers for the snapshots that you want to delete.
    :type identifiers: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    identifiers = [GETBatchDeleteClusterSnapshotsIdentifiersParameterInner.from_dict(d) for d in identifiers]
    return web.Response(status=200)


async def g_et_batch_modify_cluster_snapshots(request: web.Request, snapshot_identifier_list, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, manual_snapshot_retention_period=None, force=None) -> web.Response:
    """g_et_batch_modify_cluster_snapshots

    Modifies the settings for a set of cluster snapshots.

    :param snapshot_identifier_list: A list of snapshot identifiers you want to modify.
    :type snapshot_identifier_list: List[]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param manual_snapshot_retention_period: &lt;p&gt;The number of days that a manual snapshot is retained. If you specify the value -1, the manual snapshot is retained indefinitely.&lt;/p&gt; &lt;p&gt;The number must be either -1 or an integer between 1 and 3,653.&lt;/p&gt; &lt;p&gt;If you decrease the manual snapshot retention period from its current value, existing manual snapshots that fall outside of the new retention period will return an error. If you want to suppress the errors and delete the snapshots, use the force option. &lt;/p&gt;
    :type manual_snapshot_retention_period: int
    :param force: A boolean value indicating whether to override an exception if the retention period has passed. 
    :type force: bool

    """
    return web.Response(status=200)


async def g_et_cancel_resize(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_cancel_resize

    Cancels a resize operation for a cluster.

    :param cluster_identifier: The unique identifier for the cluster that you want to cancel a resize operation for.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_copy_cluster_snapshot(request: web.Request, source_snapshot_identifier, target_snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_snapshot_cluster_identifier=None, manual_snapshot_retention_period=None) -> web.Response:
    """g_et_copy_cluster_snapshot

    &lt;p&gt;Copies the specified automated cluster snapshot to a new manual cluster snapshot. The source must be an automated snapshot and it must be in the available state.&lt;/p&gt; &lt;p&gt;When you delete a cluster, Amazon Redshift deletes any automated snapshots of the cluster. Also, when the retention period of the snapshot expires, Amazon Redshift automatically deletes it. If you want to keep an automated snapshot for a longer period, you can make a manual copy of the snapshot. Manual snapshots are retained until you delete them.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param source_snapshot_identifier: &lt;p&gt;The identifier for the source snapshot.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be the identifier for a valid automated snapshot whose state is &lt;code&gt;available&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_snapshot_identifier: str
    :param target_snapshot_identifier: &lt;p&gt;The identifier given to the new manual snapshot.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cannot be null, empty, or blank.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 255 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique for the Amazon Web Services account that is making the request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type target_snapshot_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param source_snapshot_cluster_identifier: &lt;p&gt;The identifier of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be the identifier for a valid cluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_snapshot_cluster_identifier: str
    :param manual_snapshot_retention_period: &lt;p&gt;The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. &lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt; &lt;p&gt;The default value is -1.&lt;/p&gt;
    :type manual_snapshot_retention_period: int

    """
    return web.Response(status=200)


async def g_et_create_authentication_profile(request: web.Request, authentication_profile_name, authentication_profile_content, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_authentication_profile

    Creates an authentication profile with the specified parameters.

    :param authentication_profile_name: The name of the authentication profile to be created.
    :type authentication_profile_name: str
    :param authentication_profile_content: The content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.
    :type authentication_profile_content: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_create_cluster(request: web.Request, cluster_identifier, node_type, master_username, master_user_password, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_name=None, cluster_type=None, cluster_security_groups=None, vpc_security_group_ids=None, cluster_subnet_group_name=None, availability_zone=None, preferred_maintenance_window=None, cluster_parameter_group_name=None, automated_snapshot_retention_period=None, manual_snapshot_retention_period=None, port=None, cluster_version=None, allow_version_upgrade=None, number_of_nodes=None, publicly_accessible=None, encrypted=None, hsm_client_certificate_identifier=None, hsm_configuration_identifier=None, elastic_ip=None, tags=None, kms_key_id=None, enhanced_vpc_routing=None, additional_info=None, iam_roles=None, maintenance_track_name=None, snapshot_schedule_identifier=None, availability_zone_relocation=None, aqua_configuration_status=None, default_iam_role_arn=None, load_sample_data=None) -> web.Response:
    """g_et_create_cluster

    &lt;p&gt;Creates a new cluster with the specified parameters.&lt;/p&gt; &lt;p&gt;To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_identifier: &lt;p&gt;A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Alphabetic characters must be lowercase.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique for all clusters within an Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;myexamplecluster&lt;/code&gt; &lt;/p&gt;
    :type cluster_identifier: str
    :param node_type: &lt;p&gt;The node type to be provisioned for the cluster. For information about node types, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes\&quot;&gt; Working with Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;ds2.xlarge&lt;/code&gt; | &lt;code&gt;ds2.8xlarge&lt;/code&gt; | &lt;code&gt;dc1.large&lt;/code&gt; | &lt;code&gt;dc1.8xlarge&lt;/code&gt; | &lt;code&gt;dc2.large&lt;/code&gt; | &lt;code&gt;dc2.8xlarge&lt;/code&gt; | &lt;code&gt;ra3.xlplus&lt;/code&gt; | &lt;code&gt;ra3.4xlarge&lt;/code&gt; | &lt;code&gt;ra3.16xlarge&lt;/code&gt; &lt;/p&gt;
    :type node_type: str
    :param master_username: &lt;p&gt;The user name associated with the admin user account for the cluster that is being created.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 - 128 alphanumeric characters or hyphens. The user name can&#39;t be &lt;code&gt;PUBLIC&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not contain a colon (:) or a slash (/).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be a reserved word. A list of reserved words can be found in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\&quot;&gt;Reserved Words&lt;/a&gt; in the Amazon Redshift Database Developer Guide. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type master_username: str
    :param master_user_password: &lt;p&gt;The password associated with the admin user account for the cluster that is being created.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be between 8 and 64 characters in length.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain at least one uppercase letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain at least one lowercase letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain one number.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Can be any printable ASCII character (ASCII code 33-126) except &lt;code&gt;&#39;&lt;/code&gt; (single quote), &lt;code&gt;\&quot;&lt;/code&gt; (double quote), &lt;code&gt;\\&lt;/code&gt;, &lt;code&gt;/&lt;/code&gt;, or &lt;code&gt;@&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type master_user_password: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param db_name: &lt;p&gt;The name of the first database to be created when the cluster is created.&lt;/p&gt; &lt;p&gt;To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html\&quot;&gt;Create a Database&lt;/a&gt; in the Amazon Redshift Database Developer Guide. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;dev&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain 1 to 64 alphanumeric characters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain only lowercase letters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be a word that is reserved by the service. A list of reserved words can be found in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\&quot;&gt;Reserved Words&lt;/a&gt; in the Amazon Redshift Database Developer Guide. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_name: str
    :param cluster_type: &lt;p&gt;The type of the cluster. When cluster type is specified as&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;single-node&lt;/code&gt;, the &lt;b&gt;NumberOfNodes&lt;/b&gt; parameter is not required.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;multi-node&lt;/code&gt;, the &lt;b&gt;NumberOfNodes&lt;/b&gt; parameter is required.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Valid Values: &lt;code&gt;multi-node&lt;/code&gt; | &lt;code&gt;single-node&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;multi-node&lt;/code&gt; &lt;/p&gt;
    :type cluster_type: str
    :param cluster_security_groups: &lt;p&gt;A list of security groups to be associated with this cluster.&lt;/p&gt; &lt;p&gt;Default: The default cluster security group for Amazon Redshift.&lt;/p&gt;
    :type cluster_security_groups: List[]
    :param vpc_security_group_ids: &lt;p&gt;A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.&lt;/p&gt; &lt;p&gt;Default: The default VPC security group is associated with the cluster.&lt;/p&gt;
    :type vpc_security_group_ids: List[]
    :param cluster_subnet_group_name: &lt;p&gt;The name of a cluster subnet group to be associated with this cluster.&lt;/p&gt; &lt;p&gt;If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).&lt;/p&gt;
    :type cluster_subnet_group_name: str
    :param availability_zone: &lt;p&gt;The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.&lt;/p&gt; &lt;p&gt;Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;us-east-2d&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraint: The specified Availability Zone must be in the same region as the current endpoint.&lt;/p&gt;
    :type availability_zone: str
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range (in UTC) during which automated cluster maintenance can occur.&lt;/p&gt; &lt;p&gt; Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt; Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows\&quot;&gt;Maintenance Windows&lt;/a&gt; in Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param cluster_parameter_group_name: &lt;p&gt;The name of the parameter group to be associated with this cluster.&lt;/p&gt; &lt;p&gt;Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Working with Amazon Redshift Parameter Groups&lt;/a&gt; &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type cluster_parameter_group_name: str
    :param automated_snapshot_retention_period: &lt;p&gt;The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with &lt;a&gt;CreateClusterSnapshot&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You can&#39;t disable automated snapshots for RA3 node types. Set the automated retention period from 1-35 days.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;1&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: Must be a value from 0 to 35.&lt;/p&gt;
    :type automated_snapshot_retention_period: int
    :param manual_snapshot_retention_period: &lt;p&gt;The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn&#39;t change the retention period of existing snapshots.&lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt;
    :type manual_snapshot_retention_period: int
    :param port: &lt;p&gt;The port number on which the cluster accepts incoming connections.&lt;/p&gt; &lt;p&gt;The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;5439&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;1150-65535&lt;/code&gt; &lt;/p&gt;
    :type port: int
    :param cluster_version: &lt;p&gt;The version of the Amazon Redshift engine software that you want to deploy on the cluster.&lt;/p&gt; &lt;p&gt;The version selected runs on all the nodes in the cluster.&lt;/p&gt; &lt;p&gt;Constraints: Only version 1.0 is currently available.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;1.0&lt;/code&gt; &lt;/p&gt;
    :type cluster_version: str
    :param allow_version_upgrade: &lt;p&gt;If &lt;code&gt;true&lt;/code&gt;, major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.&lt;/p&gt; &lt;p&gt;When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;true&lt;/code&gt; &lt;/p&gt;
    :type allow_version_upgrade: bool
    :param number_of_nodes: &lt;p&gt;The number of compute nodes in the cluster. This parameter is required when the &lt;b&gt;ClusterType&lt;/b&gt; parameter is specified as &lt;code&gt;multi-node&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For information about determining how many nodes you need, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes\&quot;&gt; Working with Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;If you don&#39;t specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;1&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: Value must be at least 1 and no more than 100.&lt;/p&gt;
    :type number_of_nodes: int
    :param publicly_accessible: If &lt;code&gt;true&lt;/code&gt;, the cluster can be accessed from a public network. 
    :type publicly_accessible: bool
    :param encrypted: &lt;p&gt;If &lt;code&gt;true&lt;/code&gt;, the data in the cluster is encrypted at rest. &lt;/p&gt; &lt;p&gt;Default: false&lt;/p&gt;
    :type encrypted: bool
    :param hsm_client_certificate_identifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
    :type hsm_client_certificate_identifier: str
    :param hsm_configuration_identifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    :type hsm_configuration_identifier: str
    :param elastic_ip: &lt;p&gt;The Elastic IP (EIP) address for the cluster.&lt;/p&gt; &lt;p&gt;Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. Don&#39;t specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on. For more information about provisioning clusters in EC2-VPC, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms\&quot;&gt;Supported Platforms to Launch Your Cluster&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt;
    :type elastic_ip: str
    :param tags: A list of tag instances.
    :type tags: list | bytes
    :param kms_key_id: The Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
    :type kms_key_id: str
    :param enhanced_vpc_routing: &lt;p&gt;An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html\&quot;&gt;Enhanced VPC Routing&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;If this option is &lt;code&gt;true&lt;/code&gt;, enhanced VPC routing is enabled. &lt;/p&gt; &lt;p&gt;Default: false&lt;/p&gt;
    :type enhanced_vpc_routing: bool
    :param additional_info: Reserved.
    :type additional_info: str
    :param iam_roles: &lt;p&gt;A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. &lt;/p&gt; &lt;p&gt;The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html\&quot;&gt;Quotas and limits&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;
    :type iam_roles: List[]
    :param maintenance_track_name: An optional parameter for the name of the maintenance track for the cluster. If you don&#39;t provide a maintenance track name, the cluster is assigned to the &lt;code&gt;current&lt;/code&gt; track.
    :type maintenance_track_name: str
    :param snapshot_schedule_identifier: A unique identifier for the snapshot schedule.
    :type snapshot_schedule_identifier: str
    :param availability_zone_relocation: The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.
    :type availability_zone_relocation: bool
    :param aqua_configuration_status: This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).
    :type aqua_configuration_status: str
    :param default_iam_role_arn: The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was created. 
    :type default_iam_role_arn: str
    :param load_sample_data: A flag that specifies whether to load sample data once the cluster is created.
    :type load_sample_data: str

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_cluster_parameter_group(request: web.Request, parameter_group_name, parameter_group_family, description, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_cluster_parameter_group

    &lt;p&gt;Creates an Amazon Redshift parameter group.&lt;/p&gt; &lt;p&gt;Creating parameter groups is independent of creating clusters. You can associate a cluster with a parameter group when you create the cluster. You can also associate an existing cluster with a parameter group after the cluster is created by using &lt;a&gt;ModifyCluster&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Parameters in the parameter group define specific behavior that applies to the databases you create on the cluster. For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param parameter_group_name: &lt;p&gt;The name of the cluster parameter group.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 alphanumeric characters or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique withing your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;This value is stored as a lower-case string.&lt;/p&gt; &lt;/note&gt;
    :type parameter_group_name: str
    :param parameter_group_family: &lt;p&gt;The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.&lt;/p&gt; &lt;p&gt;To get a list of valid parameter group family names, you can call &lt;a&gt;DescribeClusterParameterGroups&lt;/a&gt;. By default, Amazon Redshift returns a list of all the parameter groups that are owned by your Amazon Web Services account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is \&quot;redshift-1.0\&quot;. &lt;/p&gt;
    :type parameter_group_family: str
    :param description: A description of the parameter group.
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
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_cluster_security_group(request: web.Request, cluster_security_group_name, description, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_cluster_security_group

    &lt;p&gt;Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.&lt;/p&gt; &lt;p&gt; For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_security_group_name: &lt;p&gt;The name for the security group. Amazon Redshift stores the value as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain no more than 255 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not be \&quot;Default\&quot;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique for all security groups that are created by your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;examplesecuritygroup&lt;/code&gt; &lt;/p&gt;
    :type cluster_security_group_name: str
    :param description: A description for the security group.
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
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_cluster_snapshot(request: web.Request, snapshot_identifier, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, manual_snapshot_retention_period=None, tags=None) -> web.Response:
    """g_et_create_cluster_snapshot

    &lt;p&gt;Creates a manual snapshot of the specified cluster. The cluster must be in the &lt;code&gt;available&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param snapshot_identifier: &lt;p&gt;A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the Amazon Web Services account.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cannot be null, empty, or blank&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 255 alphanumeric characters or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;my-snapshot-id&lt;/code&gt; &lt;/p&gt;
    :type snapshot_identifier: str
    :param cluster_identifier: The cluster identifier for which you want a snapshot.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param manual_snapshot_retention_period: &lt;p&gt;The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. &lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt; &lt;p&gt;The default value is -1.&lt;/p&gt;
    :type manual_snapshot_retention_period: int
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_cluster_subnet_group(request: web.Request, cluster_subnet_group_name, description, subnet_ids, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_cluster_subnet_group

    &lt;p&gt;Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.&lt;/p&gt; &lt;p&gt; For information about subnet groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html\&quot;&gt;Amazon Redshift Cluster Subnet Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_subnet_group_name: &lt;p&gt;The name for the subnet group. Amazon Redshift stores the value as a lowercase string.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain no more than 255 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not be \&quot;Default\&quot;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique for all subnet groups that are created by your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;examplesubnetgroup&lt;/code&gt; &lt;/p&gt;
    :type cluster_subnet_group_name: str
    :param description: A description for the subnet group.
    :type description: str
    :param subnet_ids: An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
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
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_custom_domain_association(request: web.Request, custom_domain_name, custom_domain_certificate_arn, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_custom_domain_association

    Used to create a custom domain name for a cluster. Properties include the custom domain name, the cluster the custom domain is associated with, and the certificate Amazon Resource Name (ARN).

    :param custom_domain_name: The custom domain name for a custom domain association.
    :type custom_domain_name: str
    :param custom_domain_certificate_arn: The certificate Amazon Resource Name (ARN) for the custom domain name association.
    :type custom_domain_certificate_arn: str
    :param cluster_identifier: The cluster identifier that the custom domain is associated with.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_create_endpoint_access(request: web.Request, endpoint_name, subnet_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, resource_owner=None, vpc_security_group_ids=None) -> web.Response:
    """g_et_create_endpoint_access

    Creates a Redshift-managed VPC endpoint.

    :param endpoint_name: &lt;p&gt;The Redshift-managed VPC endpoint name.&lt;/p&gt; &lt;p&gt;An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can&#39;t contain two consecutive hyphens or end with a hyphen.&lt;/p&gt;
    :type endpoint_name: str
    :param subnet_group_name: The subnet group from which Amazon Redshift chooses the subnet to deploy the endpoint.
    :type subnet_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The cluster identifier of the cluster to access.
    :type cluster_identifier: str
    :param resource_owner: The Amazon Web Services account ID of the owner of the cluster. This is only required if the cluster is in another Amazon Web Services account.
    :type resource_owner: str
    :param vpc_security_group_ids: The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
    :type vpc_security_group_ids: List[]

    """
    return web.Response(status=200)


async def g_et_create_event_subscription(request: web.Request, subscription_name, sns_topic_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_type=None, source_ids=None, event_categories=None, severity=None, enabled=None, tags=None) -> web.Response:
    """g_et_create_event_subscription

    &lt;p&gt;Creates an Amazon Redshift event notification subscription. This action requires an ARN (Amazon Resource Name) of an Amazon SNS topic created by either the Amazon Redshift console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.&lt;/p&gt; &lt;p&gt;You can specify the source type, and lists of Amazon Redshift source IDs, event categories, and event severities. Notifications will be sent for all events you want that match those criteria. For example, you can specify source type &#x3D; cluster, source ID &#x3D; my-cluster-1 and mycluster2, event categories &#x3D; Availability, Backup, and severity &#x3D; ERROR. The subscription will only send notifications for those ERROR events in the Availability and Backup categories for the specified clusters.&lt;/p&gt; &lt;p&gt;If you specify both the source type and source IDs, such as source type &#x3D; cluster and source identifier &#x3D; my-cluster-1, notifications will be sent for all the cluster events for my-cluster-1. If you specify a source type but do not specify a source identifier, you will receive notice of the events for the objects of that type in your Amazon Web Services account. If you do not specify either the SourceType nor the SourceIdentifier, you will be notified of events generated from all Amazon Redshift sources belonging to your Amazon Web Services account. You must specify a source type if you specify a source ID.&lt;/p&gt;

    :param subscription_name: &lt;p&gt;The name of the event subscription to be created.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cannot be null, empty, or blank.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 255 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type subscription_name: str
    :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
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
    :param source_type: &lt;p&gt;The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your Amazon Web Services account. You must specify a source type in order to specify source IDs.&lt;/p&gt; &lt;p&gt;Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.&lt;/p&gt;
    :type source_type: str
    :param source_ids: &lt;p&gt;A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.&lt;/p&gt; &lt;p&gt;Example: my-cluster-1, my-cluster-2&lt;/p&gt; &lt;p&gt;Example: my-snapshot-20131010&lt;/p&gt;
    :type source_ids: List[]
    :param event_categories: &lt;p&gt;Specifies the Amazon Redshift event categories to be published by the event notification subscription.&lt;/p&gt; &lt;p&gt;Values: configuration, management, monitoring, security, pending&lt;/p&gt;
    :type event_categories: List[]
    :param severity: &lt;p&gt;Specifies the Amazon Redshift event severity to be published by the event notification subscription.&lt;/p&gt; &lt;p&gt;Values: ERROR, INFO&lt;/p&gt;
    :type severity: str
    :param enabled: A boolean value; set to &lt;code&gt;true&lt;/code&gt; to activate the subscription, and set to &lt;code&gt;false&lt;/code&gt; to create the subscription but not activate it. 
    :type enabled: bool
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_hsm_client_certificate(request: web.Request, hsm_client_certificate_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_hsm_client_certificate

    &lt;p&gt;Creates an HSM client certificate that an Amazon Redshift cluster will use to connect to the client&#39;s HSM in order to store and retrieve the keys used to encrypt the cluster databases.&lt;/p&gt; &lt;p&gt;The command returns a public key, which you must store in the HSM. In addition to creating the HSM certificate, you must create an Amazon Redshift HSM configuration that provides a cluster the information needed to store and use encryption keys in the HSM. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM\&quot;&gt;Hardware Security Modules&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param hsm_client_certificate_identifier: The identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.
    :type hsm_client_certificate_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_hsm_configuration(request: web.Request, hsm_configuration_identifier, description, hsm_ip_address, hsm_partition_name, hsm_partition_password, hsm_server_public_certificate, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_hsm_configuration

    &lt;p&gt;Creates an HSM configuration that contains the information required by an Amazon Redshift cluster to store and use database encryption keys in a Hardware Security Module (HSM). After creating the HSM configuration, you can specify it as a parameter when creating a cluster. The cluster will then store its encryption keys in the HSM.&lt;/p&gt; &lt;p&gt;In addition to creating an HSM configuration, you must also create an HSM client certificate. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html\&quot;&gt;Hardware Security Modules&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt;

    :param hsm_configuration_identifier: The identifier to be assigned to the new Amazon Redshift HSM configuration.
    :type hsm_configuration_identifier: str
    :param description: A text description of the HSM configuration to be created.
    :type description: str
    :param hsm_ip_address: The IP address that the Amazon Redshift cluster must use to access the HSM.
    :type hsm_ip_address: str
    :param hsm_partition_name: The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
    :type hsm_partition_name: str
    :param hsm_partition_password: The password required to access the HSM partition.
    :type hsm_partition_password: str
    :param hsm_server_public_certificate: The HSMs public certificate file. When using Cloud HSM, the file name is server.pem.
    :type hsm_server_public_certificate: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_scheduled_action(request: web.Request, scheduled_action_name, target_action, schedule, iam_role, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, scheduled_action_description=None, start_time=None, end_time=None, enable=None) -> web.Response:
    """g_et_create_scheduled_action

    Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the &lt;code&gt;ResizeCluster&lt;/code&gt; API operation. 

    :param scheduled_action_name: The name of the scheduled action. The name must be unique within an account. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type scheduled_action_name: str
    :param target_action: A JSON format string of the Amazon Redshift API operation with input parameters. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type target_action: dict | bytes
    :param schedule: The schedule in &lt;code&gt;at( )&lt;/code&gt; or &lt;code&gt;cron( )&lt;/code&gt; format. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;.
    :type schedule: str
    :param iam_role: The IAM role to assume to run the target action. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type iam_role: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param scheduled_action_description: The description of the scheduled action. 
    :type scheduled_action_description: str
    :param start_time: The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;.
    :type start_time: str
    :param end_time: The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type end_time: str
    :param enable: If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about &lt;code&gt;state&lt;/code&gt; of the scheduled action, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type enable: bool

    """
    target_action = .from_dict(target_action)
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_create_snapshot_copy_grant(request: web.Request, snapshot_copy_grant_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, kms_key_id=None, tags=None) -> web.Response:
    """g_et_create_snapshot_copy_grant

    &lt;p&gt;Creates a snapshot copy grant that permits Amazon Redshift to use an encrypted symmetric key from Key Management Service (KMS) to encrypt copied snapshots in a destination region.&lt;/p&gt; &lt;p&gt; For more information about managing snapshot copy grants, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html\&quot;&gt;Amazon Redshift Database Encryption&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. &lt;/p&gt;

    :param snapshot_copy_grant_name: &lt;p&gt;The name of the snapshot copy grant. This name must be unique in the region for the Amazon Web Services account.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Alphabetic characters must be lowercase.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique for all clusters within an Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type snapshot_copy_grant_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param kms_key_id: The unique identifier of the encrypted symmetric key to which to grant Amazon Redshift permission. If no key is specified, the default key is used.
    :type kms_key_id: str
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_snapshot_schedule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, schedule_definitions=None, schedule_identifier=None, schedule_description=None, tags=None, dry_run=None, next_invocations=None) -> web.Response:
    """g_et_create_snapshot_schedule

    Create a snapshot schedule that can be associated to a cluster and which overrides the default system backup schedule. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param schedule_definitions: The definition of the snapshot schedule. The definition is made up of schedule expressions, for example \&quot;cron(30 12 *)\&quot; or \&quot;rate(12 hours)\&quot;. 
    :type schedule_definitions: List[]
    :param schedule_identifier: A unique identifier for a snapshot schedule. Only alphanumeric characters are allowed for the identifier.
    :type schedule_identifier: str
    :param schedule_description: The description of the snapshot schedule.
    :type schedule_description: str
    :param tags: An optional set of tags you can use to search for the schedule.
    :type tags: list | bytes
    :param dry_run: &lt;p/&gt;
    :type dry_run: bool
    :param next_invocations: &lt;p/&gt;
    :type next_invocations: int

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_tags(request: web.Request, resource_name, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_tags

    &lt;p&gt;Adds tags to a cluster.&lt;/p&gt; &lt;p&gt;A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, you will receive an error and the attempt will fail.&lt;/p&gt; &lt;p&gt;If you specify a key that already exists for the resource, the value for that key will be updated with the new value.&lt;/p&gt;

    :param resource_name: The Amazon Resource Name (ARN) to which you want to add the tag or tags. For example, &lt;code&gt;arn:aws:redshift:us-east-2:123456789:cluster:t1&lt;/code&gt;. 
    :type resource_name: str
    :param tags: One or more name/value pairs to add as tags to the specified resource. Each tag name is passed in with the parameter &lt;code&gt;Key&lt;/code&gt; and the corresponding value is passed in with the parameter &lt;code&gt;Value&lt;/code&gt;. The &lt;code&gt;Key&lt;/code&gt; and &lt;code&gt;Value&lt;/code&gt; parameters are separated by a comma (,). Separate multiple tags with a space. For example, &lt;code&gt;--tags \&quot;Key\&quot;&#x3D;\&quot;owner\&quot;,\&quot;Value\&quot;&#x3D;\&quot;admin\&quot; \&quot;Key\&quot;&#x3D;\&quot;environment\&quot;,\&quot;Value\&quot;&#x3D;\&quot;test\&quot; \&quot;Key\&quot;&#x3D;\&quot;version\&quot;,\&quot;Value\&quot;&#x3D;\&quot;1.0\&quot;&lt;/code&gt;. 
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
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_usage_limit(request: web.Request, cluster_identifier, feature_type, limit_type, amount, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, period=None, breach_action=None, tags=None) -> web.Response:
    """g_et_create_usage_limit

    Creates a usage limit for a specified Amazon Redshift feature on a cluster. The usage limit is identified by the returned usage limit identifier.

    :param cluster_identifier: The identifier of the cluster that you want to limit usage.
    :type cluster_identifier: str
    :param feature_type: The Amazon Redshift feature that you want to limit.
    :type feature_type: str
    :param limit_type: The type of limit. Depending on the feature type, this can be based on a time duration or data size. If &lt;code&gt;FeatureType&lt;/code&gt; is &lt;code&gt;spectrum&lt;/code&gt;, then &lt;code&gt;LimitType&lt;/code&gt; must be &lt;code&gt;data-scanned&lt;/code&gt;. If &lt;code&gt;FeatureType&lt;/code&gt; is &lt;code&gt;concurrency-scaling&lt;/code&gt;, then &lt;code&gt;LimitType&lt;/code&gt; must be &lt;code&gt;time&lt;/code&gt;. If &lt;code&gt;FeatureType&lt;/code&gt; is &lt;code&gt;cross-region-datasharing&lt;/code&gt;, then &lt;code&gt;LimitType&lt;/code&gt; must be &lt;code&gt;data-scanned&lt;/code&gt;. 
    :type limit_type: str
    :param amount: The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB). The value must be a positive number. 
    :type amount: int
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param period: The time period that the amount applies to. A &lt;code&gt;weekly&lt;/code&gt; period begins on Sunday. The default is &lt;code&gt;monthly&lt;/code&gt;. 
    :type period: str
    :param breach_action: The action that Amazon Redshift takes when the limit is reached. The default is log. For more information about this parameter, see &lt;a&gt;UsageLimit&lt;/a&gt;.
    :type breach_action: str
    :param tags: A list of tag instances.
    :type tags: list | bytes

    """
    tags = [GETCreateClusterTagsParameterInner.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_deauthorize_data_share(request: web.Request, data_share_arn, consumer_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_deauthorize_data_share

    From a datashare producer account, removes authorization from the specified datashare. 

    :param data_share_arn: The Amazon Resource Name (ARN) of the datashare to remove authorization from.
    :type data_share_arn: str
    :param consumer_identifier: The identifier of the data consumer that is to have authorization removed from the datashare. This identifier is an Amazon Web Services account ID or a keyword, such as ADX.
    :type consumer_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_authentication_profile(request: web.Request, authentication_profile_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_authentication_profile

    Deletes an authentication profile.

    :param authentication_profile_name: The name of the authentication profile to delete.
    :type authentication_profile_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_cluster(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, skip_final_cluster_snapshot=None, final_cluster_snapshot_identifier=None, final_cluster_snapshot_retention_period=None) -> web.Response:
    """g_et_delete_cluster

    &lt;p&gt;Deletes a previously provisioned cluster without its final snapshot being created. A successful response from the web service indicates that the request was received correctly. Use &lt;a&gt;DescribeClusters&lt;/a&gt; to monitor the status of the deletion. The delete operation cannot be canceled or reverted once submitted. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you want to shut down the cluster and retain it for future use, set &lt;i&gt;SkipFinalClusterSnapshot&lt;/i&gt; to &lt;code&gt;false&lt;/code&gt; and specify a name for &lt;i&gt;FinalClusterSnapshotIdentifier&lt;/i&gt;. You can later restore this snapshot to resume using the cluster. If a final cluster snapshot is requested, the status of the cluster will be \&quot;final-snapshot\&quot; while the snapshot is being taken, then it&#39;s \&quot;deleting\&quot; once Amazon Redshift begins deleting the cluster. &lt;/p&gt; &lt;p&gt; For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_identifier: &lt;p&gt;The identifier of the cluster to be deleted.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain lowercase characters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param skip_final_cluster_snapshot: &lt;p&gt;Determines whether a final snapshot of the cluster is created before Amazon Redshift deletes the cluster. If &lt;code&gt;true&lt;/code&gt;, a final cluster snapshot is not created. If &lt;code&gt;false&lt;/code&gt;, a final cluster snapshot is created before the cluster is deleted. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;i&gt;FinalClusterSnapshotIdentifier&lt;/i&gt; parameter must be specified if &lt;i&gt;SkipFinalClusterSnapshot&lt;/i&gt; is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type skip_final_cluster_snapshot: bool
    :param final_cluster_snapshot_identifier: &lt;p&gt;The identifier of the final snapshot that is to be created immediately before deleting the cluster. If this parameter is provided, &lt;i&gt;SkipFinalClusterSnapshot&lt;/i&gt; must be &lt;code&gt;false&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 alphanumeric characters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type final_cluster_snapshot_identifier: str
    :param final_cluster_snapshot_retention_period: &lt;p&gt;The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.&lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt; &lt;p&gt;The default value is -1.&lt;/p&gt;
    :type final_cluster_snapshot_retention_period: int

    """
    return web.Response(status=200)


async def g_et_delete_cluster_parameter_group(request: web.Request, parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_cluster_parameter_group

    &lt;p&gt;Deletes a specified Amazon Redshift parameter group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete a parameter group if it is associated with a cluster.&lt;/p&gt; &lt;/note&gt;

    :param parameter_group_name: &lt;p&gt;The name of the parameter group to be deleted.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be the name of an existing cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot delete a default cluster parameter group.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type parameter_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_cluster_security_group(request: web.Request, cluster_security_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_cluster_security_group

    &lt;p&gt;Deletes an Amazon Redshift security group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete a security group that is associated with any clusters. You cannot delete the default security group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_security_group_name: The name of the cluster security group to be deleted.
    :type cluster_security_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_cluster_snapshot(request: web.Request, snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, snapshot_cluster_identifier=None) -> web.Response:
    """g_et_delete_cluster_snapshot

    &lt;p&gt;Deletes the specified manual snapshot. The snapshot must be in the &lt;code&gt;available&lt;/code&gt; state, with no other users authorized to access the snapshot. &lt;/p&gt; &lt;p&gt;Unlike automated snapshots, manual snapshots are retained even after you delete your cluster. Amazon Redshift does not delete your manual snapshots. You must delete manual snapshot explicitly to avoid getting charged. If other accounts are authorized to access the snapshot, you must revoke all of the authorizations before you can delete the snapshot.&lt;/p&gt;

    :param snapshot_identifier: &lt;p&gt;The unique identifier of the manual snapshot to be deleted.&lt;/p&gt; &lt;p&gt;Constraints: Must be the name of an existing snapshot that is in the &lt;code&gt;available&lt;/code&gt;, &lt;code&gt;failed&lt;/code&gt;, or &lt;code&gt;cancelled&lt;/code&gt; state.&lt;/p&gt;
    :type snapshot_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param snapshot_cluster_identifier: &lt;p&gt;The unique identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.&lt;/p&gt; &lt;p&gt;Constraints: Must be the name of valid cluster.&lt;/p&gt;
    :type snapshot_cluster_identifier: str

    """
    return web.Response(status=200)


async def g_et_delete_cluster_subnet_group(request: web.Request, cluster_subnet_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_cluster_subnet_group

    Deletes the specified cluster subnet group.

    :param cluster_subnet_group_name: The name of the cluster subnet group name to be deleted.
    :type cluster_subnet_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_custom_domain_association(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_custom_domain_association

    Contains information about deleting a custom domain association for a cluster.

    :param cluster_identifier: The identifier of the cluster to delete a custom domain association for.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_endpoint_access(request: web.Request, endpoint_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_endpoint_access

    Deletes a Redshift-managed VPC endpoint.

    :param endpoint_name: The Redshift-managed VPC endpoint to delete.
    :type endpoint_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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

    Deletes an Amazon Redshift event notification subscription.

    :param subscription_name: The name of the Amazon Redshift event notification subscription to be deleted.
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


async def g_et_delete_hsm_client_certificate(request: web.Request, hsm_client_certificate_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_hsm_client_certificate

    Deletes the specified HSM client certificate.

    :param hsm_client_certificate_identifier: The identifier of the HSM client certificate to be deleted.
    :type hsm_client_certificate_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_hsm_configuration(request: web.Request, hsm_configuration_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_hsm_configuration

    Deletes the specified Amazon Redshift HSM configuration.

    :param hsm_configuration_identifier: The identifier of the Amazon Redshift HSM configuration to be deleted.
    :type hsm_configuration_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_partner(request: web.Request, account_id, cluster_identifier, database_name, partner_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_partner

    Deletes a partner integration from a cluster. Data can still flow to the cluster until the integration is deleted at the partner&#39;s website.

    :param account_id: The Amazon Web Services account ID that owns the cluster.
    :type account_id: str
    :param cluster_identifier: The cluster identifier of the cluster that receives data from the partner.
    :type cluster_identifier: str
    :param database_name: The name of the database that receives data from the partner.
    :type database_name: str
    :param partner_name: The name of the partner that is authorized to send data.
    :type partner_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_scheduled_action(request: web.Request, scheduled_action_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_scheduled_action

    Deletes a scheduled action. 

    :param scheduled_action_name: The name of the scheduled action to delete. 
    :type scheduled_action_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_snapshot_copy_grant(request: web.Request, snapshot_copy_grant_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_snapshot_copy_grant

    Deletes the specified snapshot copy grant.

    :param snapshot_copy_grant_name: The name of the snapshot copy grant to delete.
    :type snapshot_copy_grant_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_snapshot_schedule(request: web.Request, schedule_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_snapshot_schedule

    Deletes a snapshot schedule.

    :param schedule_identifier: A unique identifier of the snapshot schedule to delete.
    :type schedule_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_tags(request: web.Request, resource_name, tag_keys, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_tags

    Deletes tags from a resource. You must provide the ARN of the resource from which you want to delete the tag or tags.

    :param resource_name: The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, &lt;code&gt;arn:aws:redshift:us-east-2:123456789:cluster:t1&lt;/code&gt;. 
    :type resource_name: str
    :param tag_keys: The tag key that you want to delete.
    :type tag_keys: List[]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_usage_limit(request: web.Request, usage_limit_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_usage_limit

    Deletes a usage limit from a cluster.

    :param usage_limit_id: The identifier of the usage limit to delete.
    :type usage_limit_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_account_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, attribute_names=None) -> web.Response:
    """g_et_describe_account_attributes

    Returns a list of attributes attached to an account

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param attribute_names: A list of attribute names.
    :type attribute_names: List[]

    """
    return web.Response(status=200)


async def g_et_describe_authentication_profiles(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, authentication_profile_name=None) -> web.Response:
    """g_et_describe_authentication_profiles

    Describes an authentication profile.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param authentication_profile_name: The name of the authentication profile to describe. If not specified then all authentication profiles owned by the account are listed.
    :type authentication_profile_name: str

    """
    return web.Response(status=200)


async def g_et_describe_cluster_db_revisions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_cluster_db_revisions

    Returns an array of &lt;code&gt;ClusterDbRevision&lt;/code&gt; objects.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: A unique identifier for a cluster whose &lt;code&gt;ClusterDbRevisions&lt;/code&gt; you are requesting. This parameter is case sensitive. All clusters defined for an account are returned by default.
    :type cluster_identifier: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in the &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned &lt;code&gt;marker&lt;/code&gt; value in the &lt;code&gt;marker&lt;/code&gt; parameter and retrying the request. &lt;/p&gt; &lt;p&gt;Default: 100&lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: &lt;p&gt;An optional parameter that specifies the starting point for returning a set of response records. When the results of a &lt;code&gt;DescribeClusterDbRevisions&lt;/code&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Redshift returns a value in the &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned &lt;code&gt;marker&lt;/code&gt; value in the &lt;code&gt;marker&lt;/code&gt; parameter and retrying the request. &lt;/p&gt; &lt;p&gt;Constraints: You can specify either the &lt;code&gt;ClusterIdentifier&lt;/code&gt; parameter, or the &lt;code&gt;marker&lt;/code&gt; parameter, but not both.&lt;/p&gt;
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_cluster_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, parameter_group_name=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_cluster_parameter_groups

    &lt;p&gt;Returns a list of Amazon Redshift parameter groups, including parameter groups you created and the default parameter group. For each parameter group, the response includes the parameter group name, description, and parameter group family name. You can optionally specify a name to retrieve the description of a specific parameter group.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all parameter groups that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all parameter groups that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, parameter groups are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param parameter_group_name: The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.
    :type parameter_group_name: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeClusterParameterGroups&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_cluster_parameters(request: web.Request, parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_cluster_parameters

    &lt;p&gt;Returns a detailed list of parameters contained within the specified Amazon Redshift parameter group. For each parameter the response includes information such as parameter name, description, data type, value, whether the parameter value is modifiable, and so on.&lt;/p&gt; &lt;p&gt;You can specify &lt;i&gt;source&lt;/i&gt; filter to retrieve parameters of only specific type. For example, to retrieve parameters that were modified by a user action such as from &lt;a&gt;ModifyClusterParameterGroup&lt;/a&gt;, you can specify &lt;i&gt;source&lt;/i&gt; equal to &lt;i&gt;user&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param parameter_group_name: The name of a cluster parameter group for which to return details.
    :type parameter_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param source: &lt;p&gt;The parameter types to return. Specify &lt;code&gt;user&lt;/code&gt; to show parameters that are different form the default. Similarly, specify &lt;code&gt;engine-default&lt;/code&gt; to show parameters that are the same as the default parameter group. &lt;/p&gt; &lt;p&gt;Default: All parameter types returned.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;user&lt;/code&gt; | &lt;code&gt;engine-default&lt;/code&gt; &lt;/p&gt;
    :type source: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeClusterParameters&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_cluster_security_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_security_group_name=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_cluster_security_groups

    &lt;p&gt;Returns information about Amazon Redshift security groups. If the name of a security group is specified, the response will contain only information about only that security group.&lt;/p&gt; &lt;p&gt; For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all security groups that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all security groups that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, security groups are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_security_group_name: &lt;p&gt;The name of a cluster security group for which you are requesting details. You must specify either the &lt;b&gt;Marker&lt;/b&gt; parameter or a &lt;b&gt;ClusterSecurityGroupName&lt;/b&gt; parameter, but not both. &lt;/p&gt; &lt;p&gt; Example: &lt;code&gt;securitygroup1&lt;/code&gt; &lt;/p&gt;
    :type cluster_security_group_name: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: &lt;p&gt;An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeClusterSecurityGroups&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. &lt;/p&gt; &lt;p&gt;Constraints: You must specify either the &lt;b&gt;ClusterSecurityGroupName&lt;/b&gt; parameter or the &lt;b&gt;Marker&lt;/b&gt; parameter, but not both. &lt;/p&gt;
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_cluster_snapshots(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, snapshot_identifier=None, snapshot_arn=None, snapshot_type=None, start_time=None, end_time=None, max_records=None, marker=None, owner_account=None, tag_keys=None, tag_values=None, cluster_exists=None, sorting_entities=None) -> web.Response:
    """g_et_describe_cluster_snapshots

    &lt;p&gt;Returns one or more snapshot objects, which contain metadata about your cluster snapshots. By default, this operation returns information about all snapshots of all clusters that are owned by your Amazon Web Services account. No information is returned for snapshots owned by inactive Amazon Web Services accounts.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The identifier of the cluster which generated the requested snapshots.
    :type cluster_identifier: str
    :param snapshot_identifier: The snapshot identifier of the snapshot about which to return information.
    :type snapshot_identifier: str
    :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot associated with the message to describe cluster snapshots.
    :type snapshot_arn: str
    :param snapshot_type: &lt;p&gt;The type of snapshots for which you are requesting information. By default, snapshots of all types are returned.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;automated&lt;/code&gt; | &lt;code&gt;manual&lt;/code&gt; &lt;/p&gt;
    :type snapshot_type: str
    :param start_time: &lt;p&gt;A value that requests only snapshots created at or after the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/ISO_8601\&quot;&gt;ISO8601 Wikipedia page.&lt;/a&gt; &lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;2012-07-16T18:00:00Z&lt;/code&gt; &lt;/p&gt;
    :type start_time: str
    :param end_time: &lt;p&gt;A time value that requests only snapshots created at or before the specified time. The time value is specified in ISO 8601 format. For more information about ISO 8601, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/ISO_8601\&quot;&gt;ISO8601 Wikipedia page.&lt;/a&gt; &lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;2012-07-16T18:00:00Z&lt;/code&gt; &lt;/p&gt;
    :type end_time: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeClusterSnapshots&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param owner_account: The Amazon Web Services account used to create or copy the snapshot. Use this field to filter the results to snapshots owned by a particular account. To describe snapshots you own, either specify your Amazon Web Services account, or do not specify the parameter.
    :type owner_account: str
    :param tag_keys: A tag key or keys for which you want to return all matching cluster snapshots that are associated with the specified key or keys. For example, suppose that you have snapshots that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching cluster snapshots that are associated with the specified tag value or values. For example, suppose that you have snapshots that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the snapshots that have either or both of these tag values associated with them.
    :type tag_values: List[]
    :param cluster_exists: &lt;p&gt;A value that indicates whether to return snapshots only for an existing cluster. You can perform table-level restore only by using a snapshot of an existing cluster, that is, a cluster that has not been deleted. Values for this parameter work as follows: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;ClusterExists&lt;/code&gt; is set to &lt;code&gt;true&lt;/code&gt;, &lt;code&gt;ClusterIdentifier&lt;/code&gt; is required.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;ClusterExists&lt;/code&gt; is set to &lt;code&gt;false&lt;/code&gt; and &lt;code&gt;ClusterIdentifier&lt;/code&gt; isn&#39;t specified, all snapshots associated with deleted clusters (orphaned snapshots) are returned. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;ClusterExists&lt;/code&gt; is set to &lt;code&gt;false&lt;/code&gt; and &lt;code&gt;ClusterIdentifier&lt;/code&gt; is specified for a deleted cluster, snapshots associated with that cluster are returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;ClusterExists&lt;/code&gt; is set to &lt;code&gt;false&lt;/code&gt; and &lt;code&gt;ClusterIdentifier&lt;/code&gt; is specified for an existing cluster, no snapshots are returned. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type cluster_exists: bool
    :param sorting_entities: &lt;p/&gt;
    :type sorting_entities: list | bytes

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    sorting_entities = [GETDescribeClusterSnapshotsSortingEntitiesParameterInner.from_dict(d) for d in sorting_entities]
    return web.Response(status=200)


async def g_et_describe_cluster_subnet_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_subnet_group_name=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_cluster_subnet_groups

    &lt;p&gt;Returns one or more cluster subnet group objects, which contain metadata about your cluster subnet groups. By default, this operation returns information about all cluster subnet groups that are defined in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all subnet groups that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all subnet groups that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, subnet groups are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_subnet_group_name: The name of the cluster subnet group for which information is requested.
    :type cluster_subnet_group_name: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeClusterSubnetGroups&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_cluster_tracks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maintenance_track_name=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_cluster_tracks

    Returns a list of all the available maintenance tracks.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param maintenance_track_name: The name of the maintenance track. 
    :type maintenance_track_name: str
    :param max_records: An integer value for the maximum number of maintenance tracks to return.
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;code&gt;DescribeClusterTracks&lt;/code&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Redshift returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_cluster_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_version=None, cluster_parameter_group_family=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_cluster_versions

    Returns descriptions of the available Amazon Redshift cluster versions. You can call this operation even before creating any clusters to learn more about the Amazon Redshift versions. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_version: &lt;p&gt;The specific cluster version to return.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;1.0&lt;/code&gt; &lt;/p&gt;
    :type cluster_version: str
    :param cluster_parameter_group_family: &lt;p&gt;The name of a specific cluster parameter group family to return details for.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 alphanumeric characters&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type cluster_parameter_group_family: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeClusterVersions&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_clusters

    &lt;p&gt;Returns properties of provisioned clusters including general cluster properties, cluster database properties, maintenance and backup properties, and security and access properties. This operation supports pagination. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all clusters that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all clusters that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, clusters are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: &lt;p&gt;The unique identifier of a cluster whose properties you are requesting. This parameter is case sensitive.&lt;/p&gt; &lt;p&gt;The default is that all clusters defined for an account are returned.&lt;/p&gt;
    :type cluster_identifier: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: &lt;p&gt;An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeClusters&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. &lt;/p&gt; &lt;p&gt;Constraints: You can specify either the &lt;b&gt;ClusterIdentifier&lt;/b&gt; parameter or the &lt;b&gt;Marker&lt;/b&gt; parameter, but not both. &lt;/p&gt;
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching clusters that are associated with the specified key or keys. For example, suppose that you have clusters that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching clusters that are associated with the specified tag value or values. For example, suppose that you have clusters that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the clusters that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_custom_domain_associations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, custom_domain_name=None, custom_domain_certificate_arn=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_custom_domain_associations

    Contains information for custom domain associations for a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param custom_domain_name: The custom domain name for the custom domain association.
    :type custom_domain_name: str
    :param custom_domain_certificate_arn: The certificate Amazon Resource Name (ARN) for the custom domain association.
    :type custom_domain_certificate_arn: str
    :param max_records: The maximum records setting for the associated custom domain.
    :type max_records: int
    :param marker: The marker for the custom domain association.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_data_shares(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, data_share_arn=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_data_shares

    Shows the status of any inbound or outbound datashares available in the specified account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param data_share_arn: The identifier of the datashare to describe details of.
    :type data_share_arn: str
    :param max_records: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeDataShares&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_data_shares_for_consumer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, consumer_arn=None, status=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_data_shares_for_consumer

    Returns a list of datashares where the account identifier being called is a consumer account identifier.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param consumer_arn: The Amazon Resource Name (ARN) of the consumer that returns in the list of datashares.
    :type consumer_arn: str
    :param status: An identifier giving the status of a datashare in the consumer cluster. If this field is specified, Amazon Redshift returns the list of datashares that have the specified status.
    :type status: str
    :param max_records: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeDataSharesForConsumer&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_data_shares_for_producer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, producer_arn=None, status=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_data_shares_for_producer

    Returns a list of datashares when the account identifier being called is a producer account identifier.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param producer_arn: The Amazon Resource Name (ARN) of the producer that returns in the list of datashares.
    :type producer_arn: str
    :param status: An identifier giving the status of a datashare in the producer. If this field is specified, Amazon Redshift returns the list of datashares that have the specified status.
    :type status: str
    :param max_records: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. 
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeDataSharesForProducer&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_default_cluster_parameters(request: web.Request, parameter_group_family, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_default_cluster_parameters

    &lt;p&gt;Returns a list of parameter settings for the specified parameter group family.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param parameter_group_family: The name of the cluster parameter group family.
    :type parameter_group_family: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeDefaultClusterParameters&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, resource_owner=None, endpoint_name=None, vpc_id=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_endpoint_access

    Describes a Redshift-managed VPC endpoint.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The cluster identifier associated with the described endpoint.
    :type cluster_identifier: str
    :param resource_owner: The Amazon Web Services account ID of the owner of the cluster.
    :type resource_owner: str
    :param endpoint_name: The name of the endpoint to be described.
    :type endpoint_name: str
    :param vpc_id: The virtual private cloud (VPC) identifier with access to the cluster.
    :type vpc_id: str
    :param max_records: The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a &lt;code&gt;Marker&lt;/code&gt; is included in the response so that the remaining results can be retrieved.
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeEndpointAccess&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the &lt;code&gt;MaxRecords&lt;/code&gt; parameter.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_endpoint_authorization(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, account=None, grantee=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_endpoint_authorization

    Describes an endpoint authorization.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The cluster identifier of the cluster to access.
    :type cluster_identifier: str
    :param account: The Amazon Web Services account ID of either the cluster owner (grantor) or grantee. If &lt;code&gt;Grantee&lt;/code&gt; parameter is true, then the &lt;code&gt;Account&lt;/code&gt; value is of the grantor.
    :type account: str
    :param grantee: Indicates whether to check authorization from a grantor or grantee point of view. If true, Amazon Redshift returns endpoint authorizations that you&#39;ve been granted. If false (default), checks authorization from a grantor point of view.
    :type grantee: bool
    :param max_records: The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a &lt;code&gt;Marker&lt;/code&gt; is included in the response so that the remaining results can be retrieved.
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeEndpointAuthorization&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the &lt;code&gt;MaxRecords&lt;/code&gt; parameter.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_event_categories(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_type=None) -> web.Response:
    """g_et_describe_event_categories

    Displays a list of event categories for all event source types, or for a specified source type. For a list of the event categories and source types, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html\&quot;&gt;Amazon Redshift Event Notifications&lt;/a&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param source_type: &lt;p&gt;The source type, such as cluster or parameter group, to which the described event categories apply.&lt;/p&gt; &lt;p&gt;Valid values: cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, and scheduled-action.&lt;/p&gt;
    :type source_type: str

    """
    return web.Response(status=200)


async def g_et_describe_event_subscriptions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, subscription_name=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_event_subscriptions

    &lt;p&gt;Lists descriptions of all the Amazon Redshift event notification subscriptions for a customer account. If you specify a subscription name, lists the description for that subscription.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all event notification subscriptions that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all subscriptions that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, subscriptions are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param subscription_name: The name of the Amazon Redshift event notification subscription to be described.
    :type subscription_name: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching event notification subscriptions that are associated with the specified key or keys. For example, suppose that you have subscriptions that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching event notification subscriptions that are associated with the specified tag value or values. For example, suppose that you have subscriptions that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_identifier=None, source_type=None, start_time=None, end_time=None, duration=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_events

    Returns events related to clusters, security groups, snapshots, and parameter groups for the past 14 days. Events specific to a particular cluster, security group, snapshot or parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param source_identifier: &lt;p&gt;The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;p&gt;If &lt;i&gt;SourceIdentifier&lt;/i&gt; is supplied, &lt;i&gt;SourceType&lt;/i&gt; must also be provided.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Specify a cluster identifier when &lt;i&gt;SourceType&lt;/i&gt; is &lt;code&gt;cluster&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify a cluster security group name when &lt;i&gt;SourceType&lt;/i&gt; is &lt;code&gt;cluster-security-group&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify a cluster parameter group name when &lt;i&gt;SourceType&lt;/i&gt; is &lt;code&gt;cluster-parameter-group&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify a cluster snapshot identifier when &lt;i&gt;SourceType&lt;/i&gt; is &lt;code&gt;cluster-snapshot&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_identifier: str
    :param source_type: &lt;p&gt;The event source to retrieve events for. If no value is specified, all events are returned.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;p&gt;If &lt;i&gt;SourceType&lt;/i&gt; is supplied, &lt;i&gt;SourceIdentifier&lt;/i&gt; must also be provided.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Specify &lt;code&gt;cluster&lt;/code&gt; when &lt;i&gt;SourceIdentifier&lt;/i&gt; is a cluster identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify &lt;code&gt;cluster-security-group&lt;/code&gt; when &lt;i&gt;SourceIdentifier&lt;/i&gt; is a cluster security group name.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify &lt;code&gt;cluster-parameter-group&lt;/code&gt; when &lt;i&gt;SourceIdentifier&lt;/i&gt; is a cluster parameter group name.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specify &lt;code&gt;cluster-snapshot&lt;/code&gt; when &lt;i&gt;SourceIdentifier&lt;/i&gt; is a cluster snapshot identifier.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type source_type: str
    :param start_time: &lt;p&gt;The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/ISO_8601\&quot;&gt;ISO8601 Wikipedia page.&lt;/a&gt; &lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;2009-07-08T18:00Z&lt;/code&gt; &lt;/p&gt;
    :type start_time: str
    :param end_time: &lt;p&gt;The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/ISO_8601\&quot;&gt;ISO8601 Wikipedia page.&lt;/a&gt; &lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;2009-07-08T18:00Z&lt;/code&gt; &lt;/p&gt;
    :type end_time: str
    :param duration: &lt;p&gt;The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;60&lt;/code&gt; &lt;/p&gt;
    :type duration: int
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeEvents&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_describe_hsm_client_certificates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, hsm_client_certificate_identifier=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_hsm_client_certificates

    &lt;p&gt;Returns information about the specified HSM client certificate. If no certificate ID is specified, returns information about all the HSM certificates owned by your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM client certificates that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all HSM client certificates that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, HSM client certificates are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param hsm_client_certificate_identifier: The identifier of a specific HSM client certificate for which you want information. If no identifier is specified, information is returned for all HSM client certificates owned by your Amazon Web Services account.
    :type hsm_client_certificate_identifier: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeHsmClientCertificates&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching HSM client certificates that are associated with the specified key or keys. For example, suppose that you have HSM client certificates that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching HSM client certificates that are associated with the specified tag value or values. For example, suppose that you have HSM client certificates that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM client certificates that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_hsm_configurations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, hsm_configuration_identifier=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_hsm_configurations

    &lt;p&gt;Returns information about the specified Amazon Redshift HSM configuration. If no configuration ID is specified, returns information about all the HSM configurations owned by your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM connections that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all HSM connections that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, HSM connections are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param hsm_configuration_identifier: The identifier of a specific Amazon Redshift HSM configuration to be described. If no identifier is specified, information is returned for all HSM configurations owned by your Amazon Web Services account.
    :type hsm_configuration_identifier: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeHsmConfigurations&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_logging_status(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_logging_status

    Describes whether information, such as queries and connection attempts, is being logged for the specified Amazon Redshift cluster.

    :param cluster_identifier: &lt;p&gt;The identifier of the cluster from which to get the logging status.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;examplecluster&lt;/code&gt; &lt;/p&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_node_configuration_options(request: web.Request, action_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, snapshot_identifier=None, snapshot_arn=None, owner_account=None, filter=None, marker=None, max_records=None) -> web.Response:
    """g_et_describe_node_configuration_options

    Returns properties of possible node configurations such as node type, number of nodes, and disk usage for the specified action type.

    :param action_type: The action type to evaluate for possible node configurations. Specify \&quot;restore-cluster\&quot; to get configuration combinations based on an existing snapshot. Specify \&quot;recommend-node-config\&quot; to get configuration recommendations based on an existing cluster or snapshot. Specify \&quot;resize-cluster\&quot; to get configuration combinations for elastic resize based on an existing cluster. 
    :type action_type: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The identifier of the cluster to evaluate for possible node configurations.
    :type cluster_identifier: str
    :param snapshot_identifier: The identifier of the snapshot to evaluate for possible node configurations.
    :type snapshot_identifier: str
    :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot associated with the message to describe node configuration.
    :type snapshot_arn: str
    :param owner_account: The Amazon Web Services account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
    :type owner_account: str
    :param filter: A set of name, operator, and value items to filter the results.
    :type filter: list | bytes
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeNodeConfigurationOptions&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;500&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 100, maximum 500.&lt;/p&gt;
    :type max_records: int

    """
    filter = [GETDescribeNodeConfigurationOptionsFilterParameterInner.from_dict(d) for d in filter]
    return web.Response(status=200)


async def g_et_describe_orderable_cluster_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_version=None, node_type=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_orderable_cluster_options

    Returns a list of orderable cluster options. Before you create a new cluster you can use this operation to find what options are available, such as the EC2 Availability Zones (AZ) in the specific Amazon Web Services Region that you can specify, and the node types you can request. The node types differ by available storage, memory, CPU and price. With the cost involved you might want to obtain a list of cluster options in the specific region and specify values when creating a cluster. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_version: &lt;p&gt;The version filter value. Specify this parameter to show only the available offerings matching the specified version.&lt;/p&gt; &lt;p&gt;Default: All versions.&lt;/p&gt; &lt;p&gt;Constraints: Must be one of the version returned from &lt;a&gt;DescribeClusterVersions&lt;/a&gt;.&lt;/p&gt;
    :type cluster_version: str
    :param node_type: The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.
    :type node_type: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeOrderableClusterOptions&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_partners(request: web.Request, account_id, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, database_name=None, partner_name=None) -> web.Response:
    """g_et_describe_partners

    Returns information about the partner integrations defined for a cluster.

    :param account_id: The Amazon Web Services account ID that owns the cluster.
    :type account_id: str
    :param cluster_identifier: The cluster identifier of the cluster whose partner integration is being described.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param database_name: The name of the database whose partner integration is being described. If database name is not specified, then all databases in the cluster are described.
    :type database_name: str
    :param partner_name: The name of the partner that is being described. If partner name is not specified, then all partner integrations are described.
    :type partner_name: str

    """
    return web.Response(status=200)


async def g_et_describe_reserved_node_exchange_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reserved_node_id=None, reserved_node_exchange_request_id=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_reserved_node_exchange_status

    Returns exchange status details and associated metadata for a reserved-node exchange. Statuses include such values as in progress and requested.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reserved_node_id: The identifier of the source reserved node in a reserved-node exchange request.
    :type reserved_node_id: str
    :param reserved_node_exchange_request_id: The identifier of the reserved-node exchange request.
    :type reserved_node_exchange_request_id: str
    :param max_records: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeReservedNodeExchangeStatus&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the &lt;code&gt;MaxRecords&lt;/code&gt; parameter. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_reserved_node_offerings(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reserved_node_offering_id=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_reserved_node_offerings

    &lt;p&gt;Returns a list of the available reserved node offerings by Amazon Redshift with their descriptions including the node type, the fixed and recurring costs of reserving the node and duration the node will be reserved for you. These descriptions help you determine which reserve node offering you want to purchase. You then use the unique offering ID in you call to &lt;a&gt;PurchaseReservedNodeOffering&lt;/a&gt; to reserve one or more nodes for your Amazon Redshift cluster. &lt;/p&gt; &lt;p&gt; For more information about reserved node offerings, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html\&quot;&gt;Purchasing Reserved Nodes&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reserved_node_offering_id: The unique identifier for the offering.
    :type reserved_node_offering_id: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeReservedNodeOfferings&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_reserved_nodes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reserved_node_id=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_reserved_nodes

    Returns the descriptions of the reserved nodes.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reserved_node_id: Identifier for the node reservation.
    :type reserved_node_id: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeReservedNodes&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_resize(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_resize

    &lt;p&gt;Returns information about the last resize operation for the specified cluster. If no resize operation has ever been initiated for the specified cluster, a &lt;code&gt;HTTP 404&lt;/code&gt; error is returned. If a resize operation was initiated and completed, the status of the resize remains as &lt;code&gt;SUCCEEDED&lt;/code&gt; until the next resize. &lt;/p&gt; &lt;p&gt;A resize operation can be requested using &lt;a&gt;ModifyCluster&lt;/a&gt; and specifying a different number or type of nodes for the cluster. &lt;/p&gt;

    :param cluster_identifier: &lt;p&gt;The unique identifier of a cluster whose resize progress you are requesting. This parameter is case-sensitive.&lt;/p&gt; &lt;p&gt;By default, resize operations for all clusters defined for an Amazon Web Services account are returned.&lt;/p&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_scheduled_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, scheduled_action_name=None, target_action_type=None, start_time=None, end_time=None, active=None, filters=None, marker=None, max_records=None) -> web.Response:
    """g_et_describe_scheduled_actions

    Describes properties of scheduled actions. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param scheduled_action_name: The name of the scheduled action to retrieve. 
    :type scheduled_action_name: str
    :param target_action_type: The type of the scheduled actions to retrieve. 
    :type target_action_type: str
    :param start_time: The start time in UTC of the scheduled actions to retrieve. Only active scheduled actions that have invocations after this time are retrieved.
    :type start_time: str
    :param end_time: The end time in UTC of the scheduled action to retrieve. Only active scheduled actions that have invocations before this time are retrieved.
    :type end_time: str
    :param active: If true, retrieve only active scheduled actions. If false, retrieve only disabled scheduled actions. 
    :type active: bool
    :param filters: List of scheduled action filters. 
    :type filters: list | bytes
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeScheduledActions&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    filters = [GETDescribeScheduledActionsFiltersParameterInner.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_snapshot_copy_grants(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, snapshot_copy_grant_name=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_snapshot_copy_grants

    &lt;p&gt;Returns a list of snapshot copy grants owned by the Amazon Web Services account in the destination region.&lt;/p&gt; &lt;p&gt; For more information about managing snapshot copy grants, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html\&quot;&gt;Amazon Redshift Database Encryption&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param snapshot_copy_grant_name: The name of the snapshot copy grant.
    :type snapshot_copy_grant_name: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: &lt;p&gt;An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;code&gt;DescribeSnapshotCopyGrant&lt;/code&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. &lt;/p&gt; &lt;p&gt;Constraints: You can specify either the &lt;b&gt;SnapshotCopyGrantName&lt;/b&gt; parameter or the &lt;b&gt;Marker&lt;/b&gt; parameter, but not both. &lt;/p&gt;
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_snapshot_schedules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, schedule_identifier=None, tag_keys=None, tag_values=None, marker=None, max_records=None) -> web.Response:
    """g_et_describe_snapshot_schedules

    Returns a list of snapshot schedules. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The unique identifier for the cluster whose snapshot schedules you want to view.
    :type cluster_identifier: str
    :param schedule_identifier: A unique identifier for a snapshot schedule.
    :type schedule_identifier: str
    :param tag_keys: The key value for a snapshot schedule tag.
    :type tag_keys: List[]
    :param tag_values: The value corresponding to the key of the snapshot schedule tag.
    :type tag_values: List[]
    :param marker: A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the &lt;code&gt;marker&lt;/code&gt; parameter and retrying the command. If the &lt;code&gt;marker&lt;/code&gt; field is empty, all response records have been retrieved for the request.
    :type marker: str
    :param max_records: The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned &lt;code&gt;marker&lt;/code&gt; value.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_storage(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_storage

    Returns account level backups storage size and provisional storage.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_table_restore_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, table_restore_request_id=None, max_records=None, marker=None) -> web.Response:
    """g_et_describe_table_restore_status

    Lists the status of one or more table restore requests made using the &lt;a&gt;RestoreTableFromClusterSnapshot&lt;/a&gt; API action. If you don&#39;t specify a value for the &lt;code&gt;TableRestoreRequestId&lt;/code&gt; parameter, then &lt;code&gt;DescribeTableRestoreStatus&lt;/code&gt; returns the status of all table restore requests ordered by the date and time of the request in ascending order. Otherwise &lt;code&gt;DescribeTableRestoreStatus&lt;/code&gt; returns the status of the table specified by &lt;code&gt;TableRestoreRequestId&lt;/code&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The Amazon Redshift cluster that the table is being restored to.
    :type cluster_identifier: str
    :param table_restore_request_id: The identifier of the table restore request to return status for. If you don&#39;t specify a &lt;code&gt;TableRestoreRequestId&lt;/code&gt; value, then &lt;code&gt;DescribeTableRestoreStatus&lt;/code&gt; returns the status of all in-progress table restore requests.
    :type table_restore_request_id: str
    :param max_records: The maximum number of records to include in the response. If more records exist than the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;DescribeTableRestoreStatus&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the &lt;code&gt;MaxRecords&lt;/code&gt; parameter.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_describe_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, resource_name=None, resource_type=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_tags

    &lt;p&gt;Returns a list of tags. You can return tags from a specific resource by specifying an ARN, or you can return all tags for a given type of resource, such as clusters, snapshots, and so on.&lt;/p&gt; &lt;p&gt;The following are limitations for &lt;code&gt;DescribeTags&lt;/code&gt;: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You cannot specify an ARN and a resource-type value together in the same request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use the &lt;code&gt;MaxRecords&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters together with the ARN parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;MaxRecords&lt;/code&gt; parameter can be a range from 10 to 50 results to return in a request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all resources that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all resources that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, resources are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param resource_name: The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, &lt;code&gt;arn:aws:redshift:us-east-2:123456789:cluster:t1&lt;/code&gt;. 
    :type resource_name: str
    :param resource_type: &lt;p&gt;The type of resource with which you want to view tags. Valid resource types are: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cluster&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CIDR/IP&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EC2 security group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Snapshot&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cluster security group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Subnet group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;HSM connection&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;HSM certificate&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Parameter group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Snapshot copy grant&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about Amazon Redshift resource types and constructing ARNs, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions\&quot;&gt;Specifying Policy Elements: Actions, Effects, Resources, and Principals&lt;/a&gt; in the Amazon Redshift Cluster Management Guide. &lt;/p&gt;
    :type resource_type: str
    :param max_records: The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned &lt;code&gt;marker&lt;/code&gt; value. 
    :type max_records: int
    :param marker: A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the &lt;code&gt;marker&lt;/code&gt; parameter and retrying the command. If the &lt;code&gt;marker&lt;/code&gt; field is empty, all response records have been retrieved for the request. 
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_describe_usage_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, usage_limit_id=None, cluster_identifier=None, feature_type=None, max_records=None, marker=None, tag_keys=None, tag_values=None) -> web.Response:
    """g_et_describe_usage_limits

    &lt;p&gt;Shows usage limits on a cluster. Results are filtered based on the combination of input usage limit identifier, cluster identifier, and feature type parameters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If usage limit identifier, cluster identifier, and feature type are not provided, then all usage limit objects for the current account in the current region are returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If usage limit identifier is provided, then the corresponding usage limit object is returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If cluster identifier is provided, then all usage limit objects for the specified cluster are returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If cluster identifier and feature type are provided, then all usage limit objects for the combination of cluster and feature are returned.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param usage_limit_id: The identifier of the usage limit to describe.
    :type usage_limit_id: str
    :param cluster_identifier: The identifier of the cluster for which you want to describe usage limits.
    :type cluster_identifier: str
    :param feature_type: The feature type for which you want to describe usage limits.
    :type feature_type: str
    :param max_records: &lt;p&gt;The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Constraints: minimum 20, maximum 100.&lt;/p&gt;
    :type max_records: int
    :param marker: An optional parameter that specifies the starting point to return a set of response records. When the results of a &lt;a&gt;DescribeUsageLimits&lt;/a&gt; request exceed the value specified in &lt;code&gt;MaxRecords&lt;/code&gt;, Amazon Web Services returns a value in the &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request. 
    :type marker: str
    :param tag_keys: A tag key or keys for which you want to return all matching usage limit objects that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt;. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the usage limit objects have either or both of these tag keys associated with them.
    :type tag_keys: List[]
    :param tag_values: A tag value or values for which you want to return all matching usage limit objects that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt;. If you specify both of these tag values in the request, Amazon Redshift returns a response with the usage limit objects that have either or both of these tag values associated with them.
    :type tag_values: List[]

    """
    return web.Response(status=200)


async def g_et_disable_logging(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_disable_logging

    Stops logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

    :param cluster_identifier: &lt;p&gt;The identifier of the cluster on which logging is to be stopped.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;examplecluster&lt;/code&gt; &lt;/p&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_disable_snapshot_copy(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_disable_snapshot_copy

    &lt;p&gt;Disables the automatic copying of snapshots from one region to another region for a specified cluster.&lt;/p&gt; &lt;p&gt;If your cluster and its snapshots are encrypted using an encrypted symmetric key from Key Management Service, use &lt;a&gt;DeleteSnapshotCopyGrant&lt;/a&gt; to delete the grant that grants Amazon Redshift permission to the key in the destination region. &lt;/p&gt;

    :param cluster_identifier: &lt;p&gt;The unique identifier of the source cluster that you want to disable copying of snapshots to a destination region.&lt;/p&gt; &lt;p&gt;Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.&lt;/p&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_disassociate_data_share_consumer(request: web.Request, data_share_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, disassociate_entire_account=None, consumer_arn=None, consumer_region=None) -> web.Response:
    """g_et_disassociate_data_share_consumer

    From a datashare consumer account, remove association for the specified datashare. 

    :param data_share_arn: The Amazon Resource Name (ARN) of the datashare to remove association for. 
    :type data_share_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param disassociate_entire_account: A value that specifies whether association for the datashare is removed from the entire account.
    :type disassociate_entire_account: bool
    :param consumer_arn: The Amazon Resource Name (ARN) of the consumer that association for the datashare is removed from.
    :type consumer_arn: str
    :param consumer_region: From a datashare consumer account, removes association of a datashare from all the existing and future namespaces in the specified Amazon Web Services Region.
    :type consumer_region: str

    """
    return web.Response(status=200)


async def g_et_enable_logging(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, bucket_name=None, s3_key_prefix=None, log_destination_type=None, log_exports=None) -> web.Response:
    """g_et_enable_logging

    Starts logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

    :param cluster_identifier: &lt;p&gt;The identifier of the cluster on which logging is to be started.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;examplecluster&lt;/code&gt; &lt;/p&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param bucket_name: &lt;p&gt;The name of an existing S3 bucket where the log files are to be stored.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be in the same region as the cluster&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The cluster must have read bucket and put object permissions&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type bucket_name: str
    :param s3_key_prefix: &lt;p&gt;The prefix applied to the log file names.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cannot exceed 512 characters&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot contain spaces( ), double quotes (\&quot;), single quotes (&#39;), a backslash (\\), or control characters. The hexadecimal codes for invalid characters are: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;x00 to x20&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;x22&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;x27&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;x5c&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;x7f or larger&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;
    :type s3_key_prefix: str
    :param log_destination_type: The log destination type. An enum with possible values of &lt;code&gt;s3&lt;/code&gt; and &lt;code&gt;cloudwatch&lt;/code&gt;.
    :type log_destination_type: str
    :param log_exports: The collection of exported log types. Possible values are &lt;code&gt;connectionlog&lt;/code&gt;, &lt;code&gt;useractivitylog&lt;/code&gt;, and &lt;code&gt;userlog&lt;/code&gt;.
    :type log_exports: List[str]

    """
    return web.Response(status=200)


async def g_et_enable_snapshot_copy(request: web.Request, cluster_identifier, destination_region, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, retention_period=None, snapshot_copy_grant_name=None, manual_snapshot_retention_period=None) -> web.Response:
    """g_et_enable_snapshot_copy

    Enables the automatic copy of snapshots from one region to another region for a specified cluster.

    :param cluster_identifier: &lt;p&gt;The unique identifier of the source cluster to copy snapshots from.&lt;/p&gt; &lt;p&gt;Constraints: Must be the valid name of an existing cluster that does not already have cross-region snapshot copy enabled.&lt;/p&gt;
    :type cluster_identifier: str
    :param destination_region: &lt;p&gt;The destination Amazon Web Services Region that you want to copy snapshots to.&lt;/p&gt; &lt;p&gt;Constraints: Must be the name of a valid Amazon Web Services Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region\&quot;&gt;Regions and Endpoints&lt;/a&gt; in the Amazon Web Services General Reference. &lt;/p&gt;
    :type destination_region: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param retention_period: &lt;p&gt;The number of days to retain automated snapshots in the destination region after they are copied from the source region.&lt;/p&gt; &lt;p&gt;Default: 7.&lt;/p&gt; &lt;p&gt;Constraints: Must be at least 1 and no more than 35.&lt;/p&gt;
    :type retention_period: int
    :param snapshot_copy_grant_name: The name of the snapshot copy grant to use when snapshots of an Amazon Web Services KMS-encrypted cluster are copied to the destination region.
    :type snapshot_copy_grant_name: str
    :param manual_snapshot_retention_period: &lt;p&gt;The number of days to retain newly copied snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region. If the value is -1, the manual snapshot is retained indefinitely. &lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt;
    :type manual_snapshot_retention_period: int

    """
    return web.Response(status=200)


async def g_et_get_cluster_credentials(request: web.Request, db_user, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_name=None, cluster_identifier=None, duration_seconds=None, auto_create=None, db_groups=None, custom_domain_name=None) -> web.Response:
    """g_et_get_cluster_credentials

    &lt;p&gt;Returns a database user name and temporary password with temporary authorization to log on to an Amazon Redshift database. The action returns the database user name prefixed with &lt;code&gt;IAM:&lt;/code&gt; if &lt;code&gt;AutoCreate&lt;/code&gt; is &lt;code&gt;False&lt;/code&gt; or &lt;code&gt;IAMA:&lt;/code&gt; if &lt;code&gt;AutoCreate&lt;/code&gt; is &lt;code&gt;True&lt;/code&gt;. You can optionally specify one or more database user groups that the user will join at log on. By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html\&quot;&gt;Using IAM Authentication to Generate Database User Credentials&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;The Identity and Access Management (IAM) user or role that runs GetClusterCredentials must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html#redshift-policy-resources.getclustercredentials-resources\&quot;&gt;Resource Policies for GetClusterCredentials&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;DbGroups&lt;/code&gt; parameter is specified, the IAM policy must allow the &lt;code&gt;redshift:JoinGroup&lt;/code&gt; action with access to the listed &lt;code&gt;dbgroups&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;In addition, if the &lt;code&gt;AutoCreate&lt;/code&gt; parameter is set to &lt;code&gt;True&lt;/code&gt;, then the policy must include the &lt;code&gt;redshift:CreateClusterUser&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;DbName&lt;/code&gt; parameter is specified, the IAM policy must allow access to the resource &lt;code&gt;dbname&lt;/code&gt; for the specified database name. &lt;/p&gt;

    :param db_user: &lt;p&gt;The name of a database user. If a user name matching &lt;code&gt;DbUser&lt;/code&gt; exists in the database, the temporary user credentials have the same permissions as the existing user. If &lt;code&gt;DbUser&lt;/code&gt; doesn&#39;t exist in the database and &lt;code&gt;Autocreate&lt;/code&gt; is &lt;code&gt;True&lt;/code&gt;, a new user is created using the value for &lt;code&gt;DbUser&lt;/code&gt; with PUBLIC permissions. If a database user matching the value for &lt;code&gt;DbUser&lt;/code&gt; doesn&#39;t exist and &lt;code&gt;Autocreate&lt;/code&gt; is &lt;code&gt;False&lt;/code&gt;, then the command succeeds but the connection attempt will fail because the user doesn&#39;t exist in the database.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html\&quot;&gt;CREATE USER&lt;/a&gt; in the Amazon Redshift Database Developer Guide. &lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 64 alphanumeric characters or hyphens. The user name can&#39;t be &lt;code&gt;PUBLIC&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not contain a colon ( : ) or slash ( / ). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be a reserved word. A list of reserved words can be found in &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\&quot;&gt;Reserved Words&lt;/a&gt; in the Amazon Redshift Database Developer Guide.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_user: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param db_name: &lt;p&gt;The name of a database that &lt;code&gt;DbUser&lt;/code&gt; is authorized to log on to. If &lt;code&gt;DbName&lt;/code&gt; is not specified, &lt;code&gt;DbUser&lt;/code&gt; can log on to any existing database.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 64 alphanumeric characters or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not contain a colon ( : ) or slash ( / ). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be a reserved word. A list of reserved words can be found in &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\&quot;&gt;Reserved Words&lt;/a&gt; in the Amazon Redshift Database Developer Guide.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_name: str
    :param cluster_identifier: The unique identifier of the cluster that contains the database for which you are requesting credentials. This parameter is case sensitive.
    :type cluster_identifier: str
    :param duration_seconds: &lt;p&gt;The number of seconds until the returned temporary password expires.&lt;/p&gt; &lt;p&gt;Constraint: minimum 900, maximum 3600.&lt;/p&gt; &lt;p&gt;Default: 900&lt;/p&gt;
    :type duration_seconds: int
    :param auto_create: Create a database user with the name specified for the user named in &lt;code&gt;DbUser&lt;/code&gt; if one does not exist.
    :type auto_create: bool
    :param db_groups: &lt;p&gt;A list of the names of existing database groups that the user named in &lt;code&gt;DbUser&lt;/code&gt; will join for the current session, in addition to any group memberships for an existing user. If not specified, a new user is added only to PUBLIC.&lt;/p&gt; &lt;p&gt;Database group name constraints&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 64 alphanumeric characters or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must not contain a colon ( : ) or slash ( / ). &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be a reserved word. A list of reserved words can be found in &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\&quot;&gt;Reserved Words&lt;/a&gt; in the Amazon Redshift Database Developer Guide.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type db_groups: List[]
    :param custom_domain_name: The custom domain name for the cluster credentials.
    :type custom_domain_name: str

    """
    return web.Response(status=200)


async def g_et_get_cluster_credentials_with_iam(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, db_name=None, cluster_identifier=None, duration_seconds=None, custom_domain_name=None) -> web.Response:
    """g_et_get_cluster_credentials_with_iam

    &lt;p&gt;Returns a database user name and temporary password with temporary authorization to log in to an Amazon Redshift database. The database user is mapped 1:1 to the source Identity and Access Management (IAM) identity. For more information about IAM identities, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html\&quot;&gt;IAM Identities (users, user groups, and roles)&lt;/a&gt; in the Amazon Web Services Identity and Access Management User Guide.&lt;/p&gt; &lt;p&gt;The Identity and Access Management (IAM) identity that runs this operation must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html\&quot;&gt;Using identity-based policies (IAM policies)&lt;/a&gt; in the Amazon Redshift Cluster Management Guide. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param db_name: The name of the database for which you are requesting credentials. If the database name is specified, the IAM policy must allow access to the resource &lt;code&gt;dbname&lt;/code&gt; for the specified database name. If the database name is not specified, access to all databases is allowed.
    :type db_name: str
    :param cluster_identifier: The unique identifier of the cluster that contains the database for which you are requesting credentials. 
    :type cluster_identifier: str
    :param duration_seconds: &lt;p&gt;The number of seconds until the returned temporary password expires.&lt;/p&gt; &lt;p&gt;Range: 900-3600. Default: 900.&lt;/p&gt;
    :type duration_seconds: int
    :param custom_domain_name: The custom domain name for the IAM message cluster credentials.
    :type custom_domain_name: str

    """
    return web.Response(status=200)


async def g_et_get_reserved_node_exchange_configuration_options(request: web.Request, action_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, snapshot_identifier=None, max_records=None, marker=None) -> web.Response:
    """g_et_get_reserved_node_exchange_configuration_options

    Gets the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node offering. Details include the node type, the price, the node count, and the offering type.

    :param action_type: The action type of the reserved-node configuration. The action type can be an exchange initiated from either a snapshot or a resize.
    :type action_type: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The identifier for the cluster that is the source for a reserved-node exchange.
    :type cluster_identifier: str
    :param snapshot_identifier: The identifier for the snapshot that is the source for the reserved-node exchange.
    :type snapshot_identifier: str
    :param max_records: The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified &lt;code&gt;MaxRecords&lt;/code&gt; value, a value is returned in a &lt;code&gt;Marker&lt;/code&gt; field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
    :type max_records: int
    :param marker: An optional pagination token provided by a previous &lt;code&gt;GetReservedNodeExchangeConfigurationOptions&lt;/code&gt; request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the &lt;code&gt;MaxRecords&lt;/code&gt; parameter. You can retrieve the next set of response records by providing the returned marker value in the &lt;code&gt;Marker&lt;/code&gt; parameter and retrying the request.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_get_reserved_node_exchange_offerings(request: web.Request, reserved_node_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None) -> web.Response:
    """g_et_get_reserved_node_exchange_offerings

    Returns an array of DC2 ReservedNodeOfferings that matches the payment type, term, and usage price of the given DC1 reserved node.

    :param reserved_node_id: A string representing the node identifier for the DC1 Reserved Node to be exchanged.
    :type reserved_node_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_records: An integer setting the maximum number of ReservedNodeOfferings to retrieve.
    :type max_records: int
    :param marker: A value that indicates the starting point for the next set of ReservedNodeOfferings.
    :type marker: str

    """
    return web.Response(status=200)


async def g_et_modify_aqua_configuration(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, aqua_configuration_status=None) -> web.Response:
    """g_et_modify_aqua_configuration

    This operation is retired. Calling this operation does not change AQUA configuration. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator). 

    :param cluster_identifier: The identifier of the cluster to be modified.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param aqua_configuration_status: This parameter is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).
    :type aqua_configuration_status: str

    """
    return web.Response(status=200)


async def g_et_modify_authentication_profile(request: web.Request, authentication_profile_name, authentication_profile_content, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_authentication_profile

    Modifies an authentication profile.

    :param authentication_profile_name: The name of the authentication profile to replace.
    :type authentication_profile_name: str
    :param authentication_profile_content: The new content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.
    :type authentication_profile_content: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_modify_cluster(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_type=None, node_type=None, number_of_nodes=None, cluster_security_groups=None, vpc_security_group_ids=None, master_user_password=None, cluster_parameter_group_name=None, automated_snapshot_retention_period=None, manual_snapshot_retention_period=None, preferred_maintenance_window=None, cluster_version=None, allow_version_upgrade=None, hsm_client_certificate_identifier=None, hsm_configuration_identifier=None, new_cluster_identifier=None, publicly_accessible=None, elastic_ip=None, enhanced_vpc_routing=None, maintenance_track_name=None, encrypted=None, kms_key_id=None, availability_zone_relocation=None, availability_zone=None, port=None) -> web.Response:
    """g_et_modify_cluster

    &lt;p&gt;Modifies the settings for a cluster.&lt;/p&gt; &lt;p&gt;You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.&lt;/p&gt; &lt;p&gt;You can add another security or parameter group, or change the admin user password. Resetting a cluster password or modifying the security groups associated with a cluster do not need a reboot. However, modifying a parameter group requires a reboot for parameters to take effect. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_identifier: &lt;p&gt;The unique identifier of the cluster to be modified.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;examplecluster&lt;/code&gt; &lt;/p&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_type: &lt;p&gt;The new cluster type.&lt;/p&gt; &lt;p&gt;When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use &lt;a&gt;DescribeResize&lt;/a&gt; to track the progress of the resize request. &lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt; multi-node | single-node &lt;/code&gt; &lt;/p&gt;
    :type cluster_type: str
    :param node_type: &lt;p&gt;The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.&lt;/p&gt; &lt;p&gt; For more information about resizing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html\&quot;&gt;Resizing Clusters in Amazon Redshift&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;ds2.xlarge&lt;/code&gt; | &lt;code&gt;ds2.8xlarge&lt;/code&gt; | &lt;code&gt;dc1.large&lt;/code&gt; | &lt;code&gt;dc1.8xlarge&lt;/code&gt; | &lt;code&gt;dc2.large&lt;/code&gt; | &lt;code&gt;dc2.8xlarge&lt;/code&gt; | &lt;code&gt;ra3.xlplus&lt;/code&gt; | &lt;code&gt;ra3.4xlarge&lt;/code&gt; | &lt;code&gt;ra3.16xlarge&lt;/code&gt; &lt;/p&gt;
    :type node_type: str
    :param number_of_nodes: &lt;p&gt;The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.&lt;/p&gt; &lt;p&gt; For more information about resizing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html\&quot;&gt;Resizing Clusters in Amazon Redshift&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Valid Values: Integer greater than &lt;code&gt;0&lt;/code&gt;.&lt;/p&gt;
    :type number_of_nodes: int
    :param cluster_security_groups: &lt;p&gt;A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.&lt;/p&gt; &lt;p&gt;Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 alphanumeric characters or hyphens&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type cluster_security_groups: List[]
    :param vpc_security_group_ids: A list of virtual private cloud (VPC) security groups to be associated with the cluster. This change is asynchronously applied as soon as possible.
    :type vpc_security_group_ids: List[]
    :param master_user_password: &lt;p&gt;The new password for the cluster admin user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the &lt;code&gt;MasterUserPassword&lt;/code&gt; element exists in the &lt;code&gt;PendingModifiedValues&lt;/code&gt; element of the operation response. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Operations never return the password, so this operation provides a way to regain access to the admin user account for a cluster if the password is lost.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Default: Uses existing setting.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be between 8 and 64 characters in length.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain at least one uppercase letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain at least one lowercase letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must contain one number.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Can be any printable ASCII character (ASCII code 33-126) except &lt;code&gt;&#39;&lt;/code&gt; (single quote), &lt;code&gt;\&quot;&lt;/code&gt; (double quote), &lt;code&gt;\\&lt;/code&gt;, &lt;code&gt;/&lt;/code&gt;, or &lt;code&gt;@&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type master_user_password: str
    :param cluster_parameter_group_name: &lt;p&gt;The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use &lt;a&gt;RebootCluster&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Default: Uses existing setting.&lt;/p&gt; &lt;p&gt;Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.&lt;/p&gt;
    :type cluster_parameter_group_name: str
    :param automated_snapshot_retention_period: &lt;p&gt;The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with &lt;a&gt;CreateClusterSnapshot&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.&lt;/p&gt; &lt;p&gt;You can&#39;t disable automated snapshots for RA3 node types. Set the automated retention period from 1-35 days.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting.&lt;/p&gt; &lt;p&gt;Constraints: Must be a value from 0 to 35.&lt;/p&gt;
    :type automated_snapshot_retention_period: int
    :param manual_snapshot_retention_period: &lt;p&gt;The default for number of days that a newly created manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. This value doesn&#39;t retroactively change the retention periods of existing manual snapshots.&lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt; &lt;p&gt;The default value is -1.&lt;/p&gt;
    :type manual_snapshot_retention_period: int
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.&lt;/p&gt; &lt;p&gt;This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.&lt;/p&gt; &lt;p&gt;Default: Uses existing setting.&lt;/p&gt; &lt;p&gt;Format: ddd:hh24:mi-ddd:hh24:mi, for example &lt;code&gt;wed:07:30-wed:08:00&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun&lt;/p&gt; &lt;p&gt;Constraints: Must be at least 30 minutes.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param cluster_version: &lt;p&gt;The new version number of the Amazon Redshift engine to upgrade to.&lt;/p&gt; &lt;p&gt;For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;1.0&lt;/code&gt; &lt;/p&gt;
    :type cluster_version: str
    :param allow_version_upgrade: &lt;p&gt;If &lt;code&gt;true&lt;/code&gt;, major version upgrades will be applied automatically to the cluster during the maintenance window. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type allow_version_upgrade: bool
    :param hsm_client_certificate_identifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
    :type hsm_client_certificate_identifier: str
    :param hsm_configuration_identifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    :type hsm_configuration_identifier: str
    :param new_cluster_identifier: &lt;p&gt;The new identifier for the cluster.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Alphabetic characters must be lowercase.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique for all clusters within an Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Example: &lt;code&gt;examplecluster&lt;/code&gt; &lt;/p&gt;
    :type new_cluster_identifier: str
    :param publicly_accessible: If &lt;code&gt;true&lt;/code&gt;, the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.
    :type publicly_accessible: bool
    :param elastic_ip: &lt;p&gt;The Elastic IP (EIP) address for the cluster.&lt;/p&gt; &lt;p&gt;Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms\&quot;&gt;Supported Platforms to Launch Your Cluster&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt;
    :type elastic_ip: str
    :param enhanced_vpc_routing: &lt;p&gt;An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html\&quot;&gt;Enhanced VPC Routing&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;If this option is &lt;code&gt;true&lt;/code&gt;, enhanced VPC routing is enabled. &lt;/p&gt; &lt;p&gt;Default: false&lt;/p&gt;
    :type enhanced_vpc_routing: bool
    :param maintenance_track_name: The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the &lt;code&gt;PendingModifiedValues&lt;/code&gt; for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.
    :type maintenance_track_name: str
    :param encrypted: &lt;p&gt;Indicates whether the cluster is encrypted. If the value is encrypted (true) and you provide a value for the &lt;code&gt;KmsKeyId&lt;/code&gt; parameter, we encrypt the cluster with the provided &lt;code&gt;KmsKeyId&lt;/code&gt;. If you don&#39;t provide a &lt;code&gt;KmsKeyId&lt;/code&gt;, we encrypt with the default key. &lt;/p&gt; &lt;p&gt;If the value is not encrypted (false), then the cluster is decrypted. &lt;/p&gt;
    :type encrypted: bool
    :param kms_key_id: The Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
    :type kms_key_id: str
    :param availability_zone_relocation: The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.
    :type availability_zone_relocation: bool
    :param availability_zone: The option to initiate relocation for an Amazon Redshift cluster to the target Availability Zone.
    :type availability_zone: str
    :param port: The option to change the port of an Amazon Redshift cluster.
    :type port: int

    """
    return web.Response(status=200)


async def g_et_modify_cluster_db_revision(request: web.Request, cluster_identifier, revision_target, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_cluster_db_revision

    Modifies the database revision of a cluster. The database revision is a unique revision of the database running in a cluster.

    :param cluster_identifier: &lt;p&gt;The unique identifier of a cluster whose database revision you want to modify. &lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;examplecluster&lt;/code&gt; &lt;/p&gt;
    :type cluster_identifier: str
    :param revision_target: The identifier of the database revision. You can retrieve this value from the response to the &lt;a&gt;DescribeClusterDbRevisions&lt;/a&gt; request.
    :type revision_target: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_modify_cluster_iam_roles(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, add_iam_roles=None, remove_iam_roles=None, default_iam_role_arn=None) -> web.Response:
    """g_et_modify_cluster_iam_roles

    &lt;p&gt;Modifies the list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services.&lt;/p&gt; &lt;p&gt;The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html\&quot;&gt;Quotas and limits&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_identifier: The unique identifier of the cluster for which you want to associate or disassociate IAM roles.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param add_iam_roles: Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format. 
    :type add_iam_roles: List[]
    :param remove_iam_roles: Zero or more IAM roles in ARN format to disassociate from the cluster. 
    :type remove_iam_roles: List[]
    :param default_iam_role_arn: The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified.
    :type default_iam_role_arn: str

    """
    return web.Response(status=200)


async def g_et_modify_cluster_maintenance(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, defer_maintenance=None, defer_maintenance_identifier=None, defer_maintenance_start_time=None, defer_maintenance_end_time=None, defer_maintenance_duration=None) -> web.Response:
    """g_et_modify_cluster_maintenance

    Modifies the maintenance settings of a cluster.

    :param cluster_identifier: A unique identifier for the cluster.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param defer_maintenance: A boolean indicating whether to enable the deferred maintenance window. 
    :type defer_maintenance: bool
    :param defer_maintenance_identifier: A unique identifier for the deferred maintenance window.
    :type defer_maintenance_identifier: str
    :param defer_maintenance_start_time: A timestamp indicating the start time for the deferred maintenance window.
    :type defer_maintenance_start_time: str
    :param defer_maintenance_end_time: A timestamp indicating end time for the deferred maintenance window. If you specify an end time, you can&#39;t specify a duration.
    :type defer_maintenance_end_time: str
    :param defer_maintenance_duration: An integer indicating the duration of the maintenance window in days. If you specify a duration, you can&#39;t specify an end time. The duration must be 45 days or less.
    :type defer_maintenance_duration: int

    """
    defer_maintenance_start_time = util.deserialize_datetime(defer_maintenance_start_time)
    defer_maintenance_end_time = util.deserialize_datetime(defer_maintenance_end_time)
    return web.Response(status=200)


async def g_et_modify_cluster_parameter_group(request: web.Request, parameter_group_name, parameters, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_cluster_parameter_group

    &lt;p&gt;Modifies the parameters of a parameter group. For the parameters parameter, it can&#39;t contain ASCII characters.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param parameter_group_name: The name of the parameter group to be modified.
    :type parameter_group_name: str
    :param parameters: &lt;p&gt;An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.&lt;/p&gt; &lt;p&gt;For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.&lt;/p&gt; &lt;p&gt;For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.&lt;/p&gt;
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
    parameters = [GETModifyClusterParameterGroupParametersParameterInner.from_dict(d) for d in parameters]
    return web.Response(status=200)


async def g_et_modify_cluster_snapshot(request: web.Request, snapshot_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, manual_snapshot_retention_period=None, force=None) -> web.Response:
    """g_et_modify_cluster_snapshot

    &lt;p&gt;Modifies the settings for a snapshot.&lt;/p&gt; &lt;p&gt;This exanmple modifies the manual retention period setting for a cluster snapshot.&lt;/p&gt;

    :param snapshot_identifier: The identifier of the snapshot whose setting you want to modify.
    :type snapshot_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param manual_snapshot_retention_period: &lt;p&gt;The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.&lt;/p&gt; &lt;p&gt;If the manual snapshot falls outside of the new retention period, you can specify the force option to immediately delete the snapshot.&lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt;
    :type manual_snapshot_retention_period: int
    :param force: A Boolean option to override an exception if the retention period has already passed.
    :type force: bool

    """
    return web.Response(status=200)


async def g_et_modify_cluster_snapshot_schedule(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, schedule_identifier=None, disassociate_schedule=None) -> web.Response:
    """g_et_modify_cluster_snapshot_schedule

    Modifies a snapshot schedule for a cluster.

    :param cluster_identifier: A unique identifier for the cluster whose snapshot schedule you want to modify. 
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param schedule_identifier: A unique alphanumeric identifier for the schedule that you want to associate with the cluster.
    :type schedule_identifier: str
    :param disassociate_schedule: A boolean to indicate whether to remove the assoiciation between the cluster and the schedule.
    :type disassociate_schedule: bool

    """
    return web.Response(status=200)


async def g_et_modify_cluster_subnet_group(request: web.Request, cluster_subnet_group_name, subnet_ids, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None) -> web.Response:
    """g_et_modify_cluster_subnet_group

    Modifies a cluster subnet group to include the specified list of VPC subnets. The operation replaces the existing list of subnets with the new list of subnets.

    :param cluster_subnet_group_name: The name of the subnet group to be modified.
    :type cluster_subnet_group_name: str
    :param subnet_ids: An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
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
    :param description: A text description of the subnet group to be modified.
    :type description: str

    """
    return web.Response(status=200)


async def g_et_modify_custom_domain_association(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, custom_domain_name=None, custom_domain_certificate_arn=None) -> web.Response:
    """g_et_modify_custom_domain_association

    Contains information for changing a custom domain association.

    :param cluster_identifier: The identifier of the cluster to change a custom domain association for.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param custom_domain_name: The custom domain name for a changed custom domain association.
    :type custom_domain_name: str
    :param custom_domain_certificate_arn: The certificate Amazon Resource Name (ARN) for the changed custom domain association.
    :type custom_domain_certificate_arn: str

    """
    return web.Response(status=200)


async def g_et_modify_endpoint_access(request: web.Request, endpoint_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, vpc_security_group_ids=None) -> web.Response:
    """g_et_modify_endpoint_access

    Modifies a Redshift-managed VPC endpoint.

    :param endpoint_name: The endpoint to be modified.
    :type endpoint_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param vpc_security_group_ids: The complete list of VPC security groups associated with the endpoint after the endpoint is modified.
    :type vpc_security_group_ids: List[]

    """
    return web.Response(status=200)


async def g_et_modify_event_subscription(request: web.Request, subscription_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sns_topic_arn=None, source_type=None, source_ids=None, event_categories=None, severity=None, enabled=None) -> web.Response:
    """g_et_modify_event_subscription

    Modifies an existing Amazon Redshift event notification subscription.

    :param subscription_name: The name of the modified Amazon Redshift event notification subscription.
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
    :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic to be used by the event notification subscription.
    :type sns_topic_arn: str
    :param source_type: &lt;p&gt;The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your Amazon Web Services account. You must specify a source type in order to specify source IDs.&lt;/p&gt; &lt;p&gt;Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.&lt;/p&gt;
    :type source_type: str
    :param source_ids: &lt;p&gt;A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.&lt;/p&gt; &lt;p&gt;Example: my-cluster-1, my-cluster-2&lt;/p&gt; &lt;p&gt;Example: my-snapshot-20131010&lt;/p&gt;
    :type source_ids: List[]
    :param event_categories: &lt;p&gt;Specifies the Amazon Redshift event categories to be published by the event notification subscription.&lt;/p&gt; &lt;p&gt;Values: configuration, management, monitoring, security, pending&lt;/p&gt;
    :type event_categories: List[]
    :param severity: &lt;p&gt;Specifies the Amazon Redshift event severity to be published by the event notification subscription.&lt;/p&gt; &lt;p&gt;Values: ERROR, INFO&lt;/p&gt;
    :type severity: str
    :param enabled: A Boolean value indicating if the subscription is enabled. &lt;code&gt;true&lt;/code&gt; indicates the subscription is enabled 
    :type enabled: bool

    """
    return web.Response(status=200)


async def g_et_modify_scheduled_action(request: web.Request, scheduled_action_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, target_action=None, schedule=None, iam_role=None, scheduled_action_description=None, start_time=None, end_time=None, enable=None) -> web.Response:
    """g_et_modify_scheduled_action

    Modifies a scheduled action. 

    :param scheduled_action_name: The name of the scheduled action to modify. 
    :type scheduled_action_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param target_action: A modified JSON format of the scheduled action. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type target_action: dict | bytes
    :param schedule: A modified schedule in either &lt;code&gt;at( )&lt;/code&gt; or &lt;code&gt;cron( )&lt;/code&gt; format. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;.
    :type schedule: str
    :param iam_role: A different IAM role to assume to run the target action. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;.
    :type iam_role: str
    :param scheduled_action_description: A modified description of the scheduled action. 
    :type scheduled_action_description: str
    :param start_time: A modified start time of the scheduled action. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type start_time: str
    :param end_time: A modified end time of the scheduled action. For more information about this parameter, see &lt;a&gt;ScheduledAction&lt;/a&gt;. 
    :type end_time: str
    :param enable: A modified enable flag of the scheduled action. If true, the scheduled action is active. If false, the scheduled action is disabled. 
    :type enable: bool

    """
    target_action = .from_dict(target_action)
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_modify_snapshot_copy_retention_period(request: web.Request, cluster_identifier, retention_period, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, manual=None) -> web.Response:
    """g_et_modify_snapshot_copy_retention_period

    Modifies the number of days to retain snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region. By default, this operation only changes the retention period of copied automated snapshots. The retention periods for both new and existing copied automated snapshots are updated with the new retention period. You can set the manual option to change only the retention periods of copied manual snapshots. If you set this option, only newly copied manual snapshots have the new retention period. 

    :param cluster_identifier: &lt;p&gt;The unique identifier of the cluster for which you want to change the retention period for either automated or manual snapshots that are copied to a destination Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;Constraints: Must be the valid name of an existing cluster that has cross-region snapshot copy enabled.&lt;/p&gt;
    :type cluster_identifier: str
    :param retention_period: &lt;p&gt;The number of days to retain automated snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;By default, this only changes the retention period of copied automated snapshots. &lt;/p&gt; &lt;p&gt;If you decrease the retention period for automated snapshots that are copied to a destination Amazon Web Services Region, Amazon Redshift deletes any existing automated snapshots that were copied to the destination Amazon Web Services Region and that fall outside of the new retention period.&lt;/p&gt; &lt;p&gt;Constraints: Must be at least 1 and no more than 35 for automated snapshots. &lt;/p&gt; &lt;p&gt;If you specify the &lt;code&gt;manual&lt;/code&gt; option, only newly copied manual snapshots will have the new retention period. &lt;/p&gt; &lt;p&gt;If you specify the value of -1 newly copied manual snapshots are retained indefinitely.&lt;/p&gt; &lt;p&gt;Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.&lt;/p&gt;
    :type retention_period: int
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param manual: Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.
    :type manual: bool

    """
    return web.Response(status=200)


async def g_et_modify_snapshot_schedule(request: web.Request, schedule_identifier, schedule_definitions, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_snapshot_schedule

    Modifies a snapshot schedule. Any schedule associated with a cluster is modified asynchronously.

    :param schedule_identifier: A unique alphanumeric identifier of the schedule to modify.
    :type schedule_identifier: str
    :param schedule_definitions: An updated list of schedule definitions. A schedule definition is made up of schedule expressions, for example, \&quot;cron(30 12 *)\&quot; or \&quot;rate(12 hours)\&quot;.
    :type schedule_definitions: List[]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_modify_usage_limit(request: web.Request, usage_limit_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, amount=None, breach_action=None) -> web.Response:
    """g_et_modify_usage_limit

    Modifies a usage limit in a cluster. You can&#39;t modify the feature type or period of a usage limit.

    :param usage_limit_id: The identifier of the usage limit to modify.
    :type usage_limit_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param amount: The new limit amount. For more information about this parameter, see &lt;a&gt;UsageLimit&lt;/a&gt;. 
    :type amount: int
    :param breach_action: The new action that Amazon Redshift takes when the limit is reached. For more information about this parameter, see &lt;a&gt;UsageLimit&lt;/a&gt;. 
    :type breach_action: str

    """
    return web.Response(status=200)


async def g_et_pause_cluster(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_pause_cluster

    Pauses a cluster.

    :param cluster_identifier: The identifier of the cluster to be paused.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_purchase_reserved_node_offering(request: web.Request, reserved_node_offering_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, node_count=None) -> web.Response:
    """g_et_purchase_reserved_node_offering

    &lt;p&gt;Allows you to purchase reserved nodes. Amazon Redshift offers a predefined set of reserved node offerings. You can purchase one or more of the offerings. You can call the &lt;a&gt;DescribeReservedNodeOfferings&lt;/a&gt; API to obtain the available reserved node offerings. You can call this API by providing a specific reserved node offering and the number of nodes you want to reserve. &lt;/p&gt; &lt;p&gt; For more information about reserved node offerings, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html\&quot;&gt;Purchasing Reserved Nodes&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param reserved_node_offering_id: The unique identifier of the reserved node offering you want to purchase.
    :type reserved_node_offering_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param node_count: &lt;p&gt;The number of reserved nodes that you want to purchase.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;1&lt;/code&gt; &lt;/p&gt;
    :type node_count: int

    """
    return web.Response(status=200)


async def g_et_reboot_cluster(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_reboot_cluster

    Reboots a cluster. This action is taken as soon as possible. It results in a momentary outage to the cluster, during which the cluster status is set to &lt;code&gt;rebooting&lt;/code&gt;. A cluster event is created when the reboot is completed. Any pending cluster modifications (see &lt;a&gt;ModifyCluster&lt;/a&gt;) are applied at this reboot. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. 

    :param cluster_identifier: The cluster identifier.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_reject_data_share(request: web.Request, data_share_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_reject_data_share

    From a datashare consumer account, rejects the specified datashare.

    :param data_share_arn: The Amazon Resource Name (ARN) of the datashare to reject.
    :type data_share_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_reset_cluster_parameter_group(request: web.Request, parameter_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reset_all_parameters=None, parameters=None) -> web.Response:
    """g_et_reset_cluster_parameter_group

    Sets one or more parameters of the specified parameter group to their default values and sets the source values of the parameters to \&quot;engine-default\&quot;. To reset the entire parameter group specify the &lt;i&gt;ResetAllParameters&lt;/i&gt; parameter. For parameter changes to take effect you must reboot any associated clusters. 

    :param parameter_group_name: The name of the cluster parameter group to be reset.
    :type parameter_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reset_all_parameters: &lt;p&gt;If &lt;code&gt;true&lt;/code&gt;, all parameters in the specified parameter group will be reset to their default values. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;true&lt;/code&gt; &lt;/p&gt;
    :type reset_all_parameters: bool
    :param parameters: &lt;p&gt;An array of names of parameters to be reset. If &lt;i&gt;ResetAllParameters&lt;/i&gt; option is not used, then at least one parameter name must be supplied. &lt;/p&gt; &lt;p&gt;Constraints: A maximum of 20 parameters can be reset in a single request.&lt;/p&gt;
    :type parameters: list | bytes

    """
    parameters = [GETModifyClusterParameterGroupParametersParameterInner.from_dict(d) for d in parameters]
    return web.Response(status=200)


async def g_et_resize_cluster(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_type=None, node_type=None, number_of_nodes=None, classic=None, reserved_node_id=None, target_reserved_node_offering_id=None) -> web.Response:
    """g_et_resize_cluster

    &lt;p&gt;Changes the size of the cluster. You can change the cluster&#39;s type, or change the number or type of nodes. The default behavior is to use the elastic resize method. With an elastic resize, your cluster is available for read and write operations more quickly than with the classic resize method. &lt;/p&gt; &lt;p&gt;Elastic resize operations have the following restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can only resize clusters of the following types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;dc1.large (if your cluster is in a VPC)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;dc1.8xlarge (if your cluster is in a VPC)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;dc2.large&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;dc2.8xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ds2.xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ds2.8xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ra3.xlplus&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ra3.4xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ra3.16xlarge&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The type of nodes that you add must match the node type for the cluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param cluster_identifier: The unique identifier for the cluster to resize.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_type: The new cluster type for the specified cluster.
    :type cluster_type: str
    :param node_type: The new node type for the nodes you are adding. If not specified, the cluster&#39;s current node type is used.
    :type node_type: str
    :param number_of_nodes: The new number of nodes for the cluster. If not specified, the cluster&#39;s current number of nodes is used.
    :type number_of_nodes: int
    :param classic: A boolean value indicating whether the resize operation is using the classic resize process. If you don&#39;t provide this parameter or set the value to &lt;code&gt;false&lt;/code&gt;, the resize type is elastic. 
    :type classic: bool
    :param reserved_node_id: The identifier of the reserved node.
    :type reserved_node_id: str
    :param target_reserved_node_offering_id: The identifier of the target reserved node offering.
    :type target_reserved_node_offering_id: str

    """
    return web.Response(status=200)


async def g_et_restore_from_cluster_snapshot(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, snapshot_identifier=None, snapshot_arn=None, snapshot_cluster_identifier=None, port=None, availability_zone=None, allow_version_upgrade=None, cluster_subnet_group_name=None, publicly_accessible=None, owner_account=None, hsm_client_certificate_identifier=None, hsm_configuration_identifier=None, elastic_ip=None, cluster_parameter_group_name=None, cluster_security_groups=None, vpc_security_group_ids=None, preferred_maintenance_window=None, automated_snapshot_retention_period=None, manual_snapshot_retention_period=None, kms_key_id=None, node_type=None, enhanced_vpc_routing=None, additional_info=None, iam_roles=None, maintenance_track_name=None, snapshot_schedule_identifier=None, number_of_nodes=None, availability_zone_relocation=None, aqua_configuration_status=None, default_iam_role_arn=None, reserved_node_id=None, target_reserved_node_offering_id=None, encrypted=None) -> web.Response:
    """g_et_restore_from_cluster_snapshot

    &lt;p&gt;Creates a new cluster from a snapshot. By default, Amazon Redshift creates the resulting cluster with the same configuration as the original cluster from which the snapshot was created, except that the new cluster is created with the default cluster security and parameter groups. After Amazon Redshift creates the cluster, you can use the &lt;a&gt;ModifyCluster&lt;/a&gt; API to associate a different security group and different parameter group with the restored cluster. If you are using a DS node type, you can also choose to change to another DS node type of the same size during restore.&lt;/p&gt; &lt;p&gt;If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param cluster_identifier: &lt;p&gt;The identifier of the cluster that will be created from restoring the snapshot.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Alphabetic characters must be lowercase.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be unique for all clusters within an Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param snapshot_identifier: &lt;p&gt;The name of the snapshot from which to create the new cluster. This parameter isn&#39;t case sensitive. You must specify this parameter or &lt;code&gt;snapshotArn&lt;/code&gt;, but not both.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;my-snapshot-id&lt;/code&gt; &lt;/p&gt;
    :type snapshot_identifier: str
    :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot associated with the message to restore from a cluster. You must specify this parameter or &lt;code&gt;snapshotIdentifier&lt;/code&gt;, but not both.
    :type snapshot_arn: str
    :param snapshot_cluster_identifier: The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
    :type snapshot_cluster_identifier: str
    :param port: &lt;p&gt;The port number on which the cluster accepts connections.&lt;/p&gt; &lt;p&gt;Default: The same port as the original cluster.&lt;/p&gt; &lt;p&gt;Constraints: Must be between &lt;code&gt;1115&lt;/code&gt; and &lt;code&gt;65535&lt;/code&gt;.&lt;/p&gt;
    :type port: int
    :param availability_zone: &lt;p&gt;The Amazon EC2 Availability Zone in which to restore the cluster.&lt;/p&gt; &lt;p&gt;Default: A random, system-chosen Availability Zone.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;us-east-2a&lt;/code&gt; &lt;/p&gt;
    :type availability_zone: str
    :param allow_version_upgrade: &lt;p&gt;If &lt;code&gt;true&lt;/code&gt;, major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. &lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;true&lt;/code&gt; &lt;/p&gt;
    :type allow_version_upgrade: bool
    :param cluster_subnet_group_name: &lt;p&gt;The name of the subnet group where you want to cluster restored.&lt;/p&gt; &lt;p&gt;A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.&lt;/p&gt;
    :type cluster_subnet_group_name: str
    :param publicly_accessible: If &lt;code&gt;true&lt;/code&gt;, the cluster can be accessed from a public network. 
    :type publicly_accessible: bool
    :param owner_account: The Amazon Web Services account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
    :type owner_account: str
    :param hsm_client_certificate_identifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
    :type hsm_client_certificate_identifier: str
    :param hsm_configuration_identifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
    :type hsm_configuration_identifier: str
    :param elastic_ip: The Elastic IP (EIP) address for the cluster. Don&#39;t specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on.
    :type elastic_ip: str
    :param cluster_parameter_group_name: &lt;p&gt;The name of the parameter group to be associated with this cluster.&lt;/p&gt; &lt;p&gt;Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Working with Amazon Redshift Parameter Groups&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be 1 to 255 alphanumeric characters or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;First character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type cluster_parameter_group_name: str
    :param cluster_security_groups: &lt;p&gt;A list of security groups to be associated with this cluster.&lt;/p&gt; &lt;p&gt;Default: The default cluster security group for Amazon Redshift.&lt;/p&gt; &lt;p&gt;Cluster security groups only apply to clusters outside of VPCs.&lt;/p&gt;
    :type cluster_security_groups: List[]
    :param vpc_security_group_ids: &lt;p&gt;A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.&lt;/p&gt; &lt;p&gt;Default: The default VPC security group is associated with the cluster.&lt;/p&gt; &lt;p&gt;VPC security groups only apply to clusters in VPCs.&lt;/p&gt;
    :type vpc_security_group_ids: List[]
    :param preferred_maintenance_window: &lt;p&gt;The weekly time range (in UTC) during which automated cluster maintenance can occur.&lt;/p&gt; &lt;p&gt; Format: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt; Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows\&quot;&gt;Maintenance Windows&lt;/a&gt; in Amazon Redshift Cluster Management Guide. &lt;/p&gt; &lt;p&gt;Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun&lt;/p&gt; &lt;p&gt;Constraints: Minimum 30-minute window.&lt;/p&gt;
    :type preferred_maintenance_window: str
    :param automated_snapshot_retention_period: &lt;p&gt;The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with &lt;a&gt;CreateClusterSnapshot&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You can&#39;t disable automated snapshots for RA3 node types. Set the automated retention period from 1-35 days.&lt;/p&gt; &lt;p&gt;Default: The value selected for the cluster from which the snapshot was taken.&lt;/p&gt; &lt;p&gt;Constraints: Must be a value from 0 to 35.&lt;/p&gt;
    :type automated_snapshot_retention_period: int
    :param manual_snapshot_retention_period: &lt;p&gt;The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn&#39;t change the retention period of existing snapshots.&lt;/p&gt; &lt;p&gt;The value must be either -1 or an integer between 1 and 3,653.&lt;/p&gt;
    :type manual_snapshot_retention_period: int
    :param kms_key_id: The Key Management Service (KMS) key ID of the encryption key that encrypts data in the cluster restored from a shared snapshot. You can also provide the key ID when you restore from an unencrypted snapshot to an encrypted cluster in the same account. Additionally, you can specify a new KMS key ID when you restore from an encrypted snapshot in the same account in order to change it. In that case, the restored cluster is encrypted with the new KMS key ID.
    :type kms_key_id: str
    :param node_type: &lt;p&gt;The node type that the restored cluster will be provisioned with.&lt;/p&gt; &lt;p&gt;Default: The node type of the cluster from which the snapshot was taken. You can modify this if you are using any DS node type. In that case, you can choose to restore into another DS node type of the same size. For example, you can restore ds1.8xlarge into ds2.8xlarge, or ds1.xlarge into ds2.xlarge. If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc1.large instance type into another dc1.large instance type or dc2.large instance type. You can&#39;t restore dc1.8xlarge to dc2.8xlarge. First restore to a dc1.8xlarge cluster, then resize to a dc2.8large cluster. For more information about node types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-about-clusters-and-nodes\&quot;&gt; About Clusters and Nodes&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. &lt;/p&gt;
    :type node_type: str
    :param enhanced_vpc_routing: &lt;p&gt;An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html\&quot;&gt;Enhanced VPC Routing&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;If this option is &lt;code&gt;true&lt;/code&gt;, enhanced VPC routing is enabled. &lt;/p&gt; &lt;p&gt;Default: false&lt;/p&gt;
    :type enhanced_vpc_routing: bool
    :param additional_info: Reserved.
    :type additional_info: str
    :param iam_roles: &lt;p&gt;A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. &lt;/p&gt; &lt;p&gt;The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html\&quot;&gt;Quotas and limits&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;
    :type iam_roles: List[]
    :param maintenance_track_name: The name of the maintenance track for the restored cluster. When you take a snapshot, the snapshot inherits the &lt;code&gt;MaintenanceTrack&lt;/code&gt; value from the cluster. The snapshot might be on a different track than the cluster that was the source for the snapshot. For example, suppose that you take a snapshot of a cluster that is on the current track and then change the cluster to be on the trailing track. In this case, the snapshot and the source cluster are on different tracks.
    :type maintenance_track_name: str
    :param snapshot_schedule_identifier: A unique identifier for the snapshot schedule.
    :type snapshot_schedule_identifier: str
    :param number_of_nodes: The number of nodes specified when provisioning the restored cluster.
    :type number_of_nodes: int
    :param availability_zone_relocation: The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is restored.
    :type availability_zone_relocation: bool
    :param aqua_configuration_status: This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).
    :type aqua_configuration_status: str
    :param default_iam_role_arn: The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified while it was restored from a snapshot.
    :type default_iam_role_arn: str
    :param reserved_node_id: The identifier of the target reserved node offering.
    :type reserved_node_id: str
    :param target_reserved_node_offering_id: The identifier of the target reserved node offering.
    :type target_reserved_node_offering_id: str
    :param encrypted: Enables support for restoring an unencrypted snapshot to a cluster encrypted with Key Management Service (KMS) and a customer managed key.
    :type encrypted: bool

    """
    return web.Response(status=200)


async def g_et_restore_table_from_cluster_snapshot(request: web.Request, cluster_identifier, snapshot_identifier, source_database_name, source_table_name, new_table_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_schema_name=None, target_database_name=None, target_schema_name=None, enable_case_sensitive_identifier=None) -> web.Response:
    """g_et_restore_table_from_cluster_snapshot

    &lt;p&gt;Creates a new table from a table in an Amazon Redshift cluster snapshot. You must create the new table within the Amazon Redshift cluster that the snapshot was taken from.&lt;/p&gt; &lt;p&gt;You cannot use &lt;code&gt;RestoreTableFromClusterSnapshot&lt;/code&gt; to restore a table with the same name as an existing table in an Amazon Redshift cluster. That is, you cannot overwrite an existing table in a cluster with a restored table. If you want to replace your original table with a new, restored table, then rename or drop your original table before you call &lt;code&gt;RestoreTableFromClusterSnapshot&lt;/code&gt;. When you have renamed your original table, then you can pass the original name of the table as the &lt;code&gt;NewTableName&lt;/code&gt; parameter value in the call to &lt;code&gt;RestoreTableFromClusterSnapshot&lt;/code&gt;. This way, you can replace the original table with the table created from the snapshot.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to restore tables with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved\&quot;&gt;interleaved sort keys&lt;/a&gt;.&lt;/p&gt;

    :param cluster_identifier: The identifier of the Amazon Redshift cluster to restore the table to.
    :type cluster_identifier: str
    :param snapshot_identifier: The identifier of the snapshot to restore the table from. This snapshot must have been created from the Amazon Redshift cluster specified by the &lt;code&gt;ClusterIdentifier&lt;/code&gt; parameter.
    :type snapshot_identifier: str
    :param source_database_name: The name of the source database that contains the table to restore from.
    :type source_database_name: str
    :param source_table_name: The name of the source table to restore from.
    :type source_table_name: str
    :param new_table_name: The name of the table to create as a result of the current request.
    :type new_table_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param source_schema_name: The name of the source schema that contains the table to restore from. If you do not specify a &lt;code&gt;SourceSchemaName&lt;/code&gt; value, the default is &lt;code&gt;public&lt;/code&gt;.
    :type source_schema_name: str
    :param target_database_name: The name of the database to restore the table to.
    :type target_database_name: str
    :param target_schema_name: The name of the schema to restore the table to.
    :type target_schema_name: str
    :param enable_case_sensitive_identifier: Indicates whether name identifiers for database, schema, and table are case sensitive. If &lt;code&gt;true&lt;/code&gt;, the names are case sensitive. If &lt;code&gt;false&lt;/code&gt; (default), the names are not case sensitive.
    :type enable_case_sensitive_identifier: bool

    """
    return web.Response(status=200)


async def g_et_resume_cluster(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_resume_cluster

    Resumes a paused cluster.

    :param cluster_identifier: The identifier of the cluster to be resumed.
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_revoke_cluster_security_group_ingress(request: web.Request, cluster_security_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cidrip=None, ec2_security_group_name=None, ec2_security_group_owner_id=None) -> web.Response:
    """g_et_revoke_cluster_security_group_ingress

    Revokes an ingress rule in an Amazon Redshift security group for a previously authorized IP range or Amazon EC2 security group. To add an ingress rule, see &lt;a&gt;AuthorizeClusterSecurityGroupIngress&lt;/a&gt;. For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. 

    :param cluster_security_group_name: The name of the security Group from which to revoke the ingress rule.
    :type cluster_security_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cidrip: The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If &lt;code&gt;CIDRIP&lt;/code&gt; is specified, &lt;code&gt;EC2SecurityGroupName&lt;/code&gt; and &lt;code&gt;EC2SecurityGroupOwnerId&lt;/code&gt; cannot be provided. 
    :type cidrip: str
    :param ec2_security_group_name: The name of the EC2 Security Group whose access is to be revoked. If &lt;code&gt;EC2SecurityGroupName&lt;/code&gt; is specified, &lt;code&gt;EC2SecurityGroupOwnerId&lt;/code&gt; must also be provided and &lt;code&gt;CIDRIP&lt;/code&gt; cannot be provided. 
    :type ec2_security_group_name: str
    :param ec2_security_group_owner_id: &lt;p&gt;The Amazon Web Services account number of the owner of the security group specified in the &lt;code&gt;EC2SecurityGroupName&lt;/code&gt; parameter. The Amazon Web Services access key ID is not an acceptable value. If &lt;code&gt;EC2SecurityGroupOwnerId&lt;/code&gt; is specified, &lt;code&gt;EC2SecurityGroupName&lt;/code&gt; must also be provided. and &lt;code&gt;CIDRIP&lt;/code&gt; cannot be provided. &lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;111122223333&lt;/code&gt; &lt;/p&gt;
    :type ec2_security_group_owner_id: str

    """
    return web.Response(status=200)


async def g_et_revoke_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_identifier=None, account=None, vpc_ids=None, force=None) -> web.Response:
    """g_et_revoke_endpoint_access

    Revokes access to a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param cluster_identifier: The cluster to revoke access from.
    :type cluster_identifier: str
    :param account: The Amazon Web Services account ID whose access is to be revoked.
    :type account: str
    :param vpc_ids: The virtual private cloud (VPC) identifiers for which access is to be revoked.
    :type vpc_ids: List[]
    :param force: Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
    :type force: bool

    """
    return web.Response(status=200)


async def g_et_revoke_snapshot_access(request: web.Request, account_with_restore_access, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, snapshot_identifier=None, snapshot_arn=None, snapshot_cluster_identifier=None) -> web.Response:
    """g_et_revoke_snapshot_access

    &lt;p&gt;Removes the ability of the specified Amazon Web Services account to restore the specified snapshot. If the account is currently restoring the snapshot, the restore will run to completion.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param account_with_restore_access: The identifier of the Amazon Web Services account that can no longer restore the specified snapshot.
    :type account_with_restore_access: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param snapshot_identifier: The identifier of the snapshot that the account can no longer access.
    :type snapshot_identifier: str
    :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot associated with the message to revoke access.
    :type snapshot_arn: str
    :param snapshot_cluster_identifier: The identifier of the cluster the snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
    :type snapshot_cluster_identifier: str

    """
    return web.Response(status=200)


async def g_et_rotate_encryption_key(request: web.Request, cluster_identifier, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_rotate_encryption_key

    Rotates the encryption keys for a cluster.

    :param cluster_identifier: &lt;p&gt;The unique identifier of the cluster that you want to rotate the encryption keys for.&lt;/p&gt; &lt;p&gt;Constraints: Must be the name of valid cluster that has encryption enabled.&lt;/p&gt;
    :type cluster_identifier: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_update_partner_status(request: web.Request, account_id, cluster_identifier, database_name, partner_name, status, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, status_message=None) -> web.Response:
    """g_et_update_partner_status

    Updates the status of a partner integration.

    :param account_id: The Amazon Web Services account ID that owns the cluster.
    :type account_id: str
    :param cluster_identifier: The cluster identifier of the cluster whose partner integration status is being updated.
    :type cluster_identifier: str
    :param database_name: The name of the database whose partner integration status is being updated.
    :type database_name: str
    :param partner_name: The name of the partner whose integration status is being updated.
    :type partner_name: str
    :param status: The value of the updated status.
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
    :param status_message: The status message provided by the partner.
    :type status_message: str

    """
    return web.Response(status=200)


async def p_ost_accept_reserved_node_exchange(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_accept_reserved_node_exchange

    Exchanges a DC1 Reserved Node for a DC2 Reserved Node with no changes to the configuration (term, payment type, or number of nodes) and no additional costs. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AcceptReservedNodeExchangeInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_add_partner(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_partner

    Adds a partner integration to a cluster. This operation authorizes a partner to push status updates for the specified database. To complete the integration, you also set up the integration on the partner website.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PartnerIntegrationInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_associate_data_share_consumer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_associate_data_share_consumer

    From a datashare consumer account, associates a datashare with the account (AssociateEntireAccount) or the specified namespace (ConsumerArn). If you make this association, the consumer can consume the datashare.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AssociateDataShareConsumerMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_authorize_cluster_security_group_ingress(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_authorize_cluster_security_group_ingress

    &lt;p&gt;Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.&lt;/p&gt; &lt;p&gt;If you authorize access to an Amazon EC2 security group, specify &lt;i&gt;EC2SecurityGroupName&lt;/i&gt; and &lt;i&gt;EC2SecurityGroupOwnerId&lt;/i&gt;. The Amazon EC2 security group and Amazon Redshift cluster must be in the same Amazon Web Services Region. &lt;/p&gt; &lt;p&gt;If you authorize access to a CIDR/IP address range, specify &lt;i&gt;CIDRIP&lt;/i&gt;. For an overview of CIDR blocks, see the Wikipedia article on &lt;a href&#x3D;\&quot;http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\&quot;&gt;Classless Inter-Domain Routing&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Working with Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AuthorizeClusterSecurityGroupIngressMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_authorize_data_share(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_authorize_data_share

    From a data producer account, authorizes the sharing of a datashare with one or more consumer accounts or managing entities. To authorize a datashare for a data consumer, the producer account must have the correct access permissions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AuthorizeDataShareMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_authorize_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_authorize_endpoint_access

    Grants access to a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AuthorizeEndpointAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_authorize_snapshot_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_authorize_snapshot_access

    &lt;p&gt;Authorizes the specified Amazon Web Services account to restore the specified snapshot.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AuthorizeSnapshotAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_batch_delete_cluster_snapshots(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_batch_delete_cluster_snapshots

    Deletes a set of cluster snapshots.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = BatchDeleteClusterSnapshotsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_batch_modify_cluster_snapshots(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_batch_modify_cluster_snapshots

    Modifies the settings for a set of cluster snapshots.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = BatchModifyClusterSnapshotsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_cancel_resize(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_cancel_resize

    Cancels a resize operation for a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CancelResizeMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_copy_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_copy_cluster_snapshot

    &lt;p&gt;Copies the specified automated cluster snapshot to a new manual cluster snapshot. The source must be an automated snapshot and it must be in the available state.&lt;/p&gt; &lt;p&gt;When you delete a cluster, Amazon Redshift deletes any automated snapshots of the cluster. Also, when the retention period of the snapshot expires, Amazon Redshift automatically deletes it. If you want to keep an automated snapshot for a longer period, you can make a manual copy of the snapshot. Manual snapshots are retained until you delete them.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CopyClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_authentication_profile(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_authentication_profile

    Creates an authentication profile with the specified parameters.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateAuthenticationProfileMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_cluster

    &lt;p&gt;Creates a new cluster with the specified parameters.&lt;/p&gt; &lt;p&gt;To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_cluster_parameter_group

    &lt;p&gt;Creates an Amazon Redshift parameter group.&lt;/p&gt; &lt;p&gt;Creating parameter groups is independent of creating clusters. You can associate a cluster with a parameter group when you create the cluster. You can also associate an existing cluster with a parameter group after the cluster is created by using &lt;a&gt;ModifyCluster&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Parameters in the parameter group define specific behavior that applies to the databases you create on the cluster. For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_cluster_security_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_cluster_security_group

    &lt;p&gt;Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.&lt;/p&gt; &lt;p&gt; For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateClusterSecurityGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_cluster_snapshot

    &lt;p&gt;Creates a manual snapshot of the specified cluster. The cluster must be in the &lt;code&gt;available&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_cluster_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_cluster_subnet_group

    &lt;p&gt;Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.&lt;/p&gt; &lt;p&gt; For information about subnet groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html\&quot;&gt;Amazon Redshift Cluster Subnet Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateClusterSubnetGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_custom_domain_association(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_custom_domain_association

    Used to create a custom domain name for a cluster. Properties include the custom domain name, the cluster the custom domain is associated with, and the certificate Amazon Resource Name (ARN).

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateCustomDomainAssociationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_endpoint_access

    Creates a Redshift-managed VPC endpoint.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateEndpointAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_event_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_event_subscription

    &lt;p&gt;Creates an Amazon Redshift event notification subscription. This action requires an ARN (Amazon Resource Name) of an Amazon SNS topic created by either the Amazon Redshift console, the Amazon SNS console, or the Amazon SNS API. To obtain an ARN with Amazon SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.&lt;/p&gt; &lt;p&gt;You can specify the source type, and lists of Amazon Redshift source IDs, event categories, and event severities. Notifications will be sent for all events you want that match those criteria. For example, you can specify source type &#x3D; cluster, source ID &#x3D; my-cluster-1 and mycluster2, event categories &#x3D; Availability, Backup, and severity &#x3D; ERROR. The subscription will only send notifications for those ERROR events in the Availability and Backup categories for the specified clusters.&lt;/p&gt; &lt;p&gt;If you specify both the source type and source IDs, such as source type &#x3D; cluster and source identifier &#x3D; my-cluster-1, notifications will be sent for all the cluster events for my-cluster-1. If you specify a source type but do not specify a source identifier, you will receive notice of the events for the objects of that type in your Amazon Web Services account. If you do not specify either the SourceType nor the SourceIdentifier, you will be notified of events generated from all Amazon Redshift sources belonging to your Amazon Web Services account. You must specify a source type if you specify a source ID.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def p_ost_create_hsm_client_certificate(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_hsm_client_certificate

    &lt;p&gt;Creates an HSM client certificate that an Amazon Redshift cluster will use to connect to the client&#39;s HSM in order to store and retrieve the keys used to encrypt the cluster databases.&lt;/p&gt; &lt;p&gt;The command returns a public key, which you must store in the HSM. In addition to creating the HSM certificate, you must create an Amazon Redshift HSM configuration that provides a cluster the information needed to store and use encryption keys in the HSM. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM\&quot;&gt;Hardware Security Modules&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateHsmClientCertificateMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_hsm_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_hsm_configuration

    &lt;p&gt;Creates an HSM configuration that contains the information required by an Amazon Redshift cluster to store and use database encryption keys in a Hardware Security Module (HSM). After creating the HSM configuration, you can specify it as a parameter when creating a cluster. The cluster will then store its encryption keys in the HSM.&lt;/p&gt; &lt;p&gt;In addition to creating an HSM configuration, you must also create an HSM client certificate. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html\&quot;&gt;Hardware Security Modules&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateHsmConfigurationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_scheduled_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_scheduled_action

    Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the &lt;code&gt;ResizeCluster&lt;/code&gt; API operation. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateScheduledActionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_snapshot_copy_grant(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_snapshot_copy_grant

    &lt;p&gt;Creates a snapshot copy grant that permits Amazon Redshift to use an encrypted symmetric key from Key Management Service (KMS) to encrypt copied snapshots in a destination region.&lt;/p&gt; &lt;p&gt; For more information about managing snapshot copy grants, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html\&quot;&gt;Amazon Redshift Database Encryption&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateSnapshotCopyGrantMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_snapshot_schedule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_snapshot_schedule

    Create a snapshot schedule that can be associated to a cluster and which overrides the default system backup schedule. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateSnapshotScheduleMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_tags

    &lt;p&gt;Adds tags to a cluster.&lt;/p&gt; &lt;p&gt;A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, you will receive an error and the attempt will fail.&lt;/p&gt; &lt;p&gt;If you specify a key that already exists for the resource, the value for that key will be updated with the new value.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateTagsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_usage_limit(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_usage_limit

    Creates a usage limit for a specified Amazon Redshift feature on a cluster. The usage limit is identified by the returned usage limit identifier.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateUsageLimitMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_deauthorize_data_share(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_deauthorize_data_share

    From a datashare producer account, removes authorization from the specified datashare. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeauthorizeDataShareMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_authentication_profile(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_authentication_profile

    Deletes an authentication profile.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteAuthenticationProfileMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_cluster

    &lt;p&gt;Deletes a previously provisioned cluster without its final snapshot being created. A successful response from the web service indicates that the request was received correctly. Use &lt;a&gt;DescribeClusters&lt;/a&gt; to monitor the status of the deletion. The delete operation cannot be canceled or reverted once submitted. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you want to shut down the cluster and retain it for future use, set &lt;i&gt;SkipFinalClusterSnapshot&lt;/i&gt; to &lt;code&gt;false&lt;/code&gt; and specify a name for &lt;i&gt;FinalClusterSnapshotIdentifier&lt;/i&gt;. You can later restore this snapshot to resume using the cluster. If a final cluster snapshot is requested, the status of the cluster will be \&quot;final-snapshot\&quot; while the snapshot is being taken, then it&#39;s \&quot;deleting\&quot; once Amazon Redshift begins deleting the cluster. &lt;/p&gt; &lt;p&gt; For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_cluster_parameter_group

    &lt;p&gt;Deletes a specified Amazon Redshift parameter group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete a parameter group if it is associated with a cluster.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_cluster_security_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_cluster_security_group

    &lt;p&gt;Deletes an Amazon Redshift security group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete a security group that is associated with any clusters. You cannot delete the default security group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteClusterSecurityGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_cluster_snapshot

    &lt;p&gt;Deletes the specified manual snapshot. The snapshot must be in the &lt;code&gt;available&lt;/code&gt; state, with no other users authorized to access the snapshot. &lt;/p&gt; &lt;p&gt;Unlike automated snapshots, manual snapshots are retained even after you delete your cluster. Amazon Redshift does not delete your manual snapshots. You must delete manual snapshot explicitly to avoid getting charged. If other accounts are authorized to access the snapshot, you must revoke all of the authorizations before you can delete the snapshot.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_cluster_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_cluster_subnet_group

    Deletes the specified cluster subnet group.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteClusterSubnetGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_custom_domain_association(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_custom_domain_association

    Contains information about deleting a custom domain association for a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteCustomDomainAssociationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_endpoint_access

    Deletes a Redshift-managed VPC endpoint.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteEndpointAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_event_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_event_subscription

    Deletes an Amazon Redshift event notification subscription.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def p_ost_delete_hsm_client_certificate(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_hsm_client_certificate

    Deletes the specified HSM client certificate.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteHsmClientCertificateMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_hsm_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_hsm_configuration

    Deletes the specified Amazon Redshift HSM configuration.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteHsmConfigurationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_partner(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_partner

    Deletes a partner integration from a cluster. Data can still flow to the cluster until the integration is deleted at the partner&#39;s website.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PartnerIntegrationInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_scheduled_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_scheduled_action

    Deletes a scheduled action. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteScheduledActionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_snapshot_copy_grant(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_snapshot_copy_grant

    Deletes the specified snapshot copy grant.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteSnapshotCopyGrantMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_snapshot_schedule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_snapshot_schedule

    Deletes a snapshot schedule.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteSnapshotScheduleMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_tags

    Deletes tags from a resource. You must provide the ARN of the resource from which you want to delete the tag or tags.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteTagsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_usage_limit(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_usage_limit

    Deletes a usage limit from a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteUsageLimitMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_account_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_account_attributes

    Returns a list of attributes attached to an account

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeAccountAttributesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_authentication_profiles(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_authentication_profiles

    Describes an authentication profile.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeAuthenticationProfilesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_db_revisions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_db_revisions

    Returns an array of &lt;code&gt;ClusterDbRevision&lt;/code&gt; objects.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterDbRevisionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_parameter_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_parameter_groups

    &lt;p&gt;Returns a list of Amazon Redshift parameter groups, including parameter groups you created and the default parameter group. For each parameter group, the response includes the parameter group name, description, and parameter group family name. You can optionally specify a name to retrieve the description of a specific parameter group.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all parameter groups that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all parameter groups that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, parameter groups are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterParameterGroupsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_parameters

    &lt;p&gt;Returns a detailed list of parameters contained within the specified Amazon Redshift parameter group. For each parameter the response includes information such as parameter name, description, data type, value, whether the parameter value is modifiable, and so on.&lt;/p&gt; &lt;p&gt;You can specify &lt;i&gt;source&lt;/i&gt; filter to retrieve parameters of only specific type. For example, to retrieve parameters that were modified by a user action such as from &lt;a&gt;ModifyClusterParameterGroup&lt;/a&gt;, you can specify &lt;i&gt;source&lt;/i&gt; equal to &lt;i&gt;user&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterParametersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_security_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_security_groups

    &lt;p&gt;Returns information about Amazon Redshift security groups. If the name of a security group is specified, the response will contain only information about only that security group.&lt;/p&gt; &lt;p&gt; For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all security groups that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all security groups that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, security groups are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterSecurityGroupsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_snapshots(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_snapshots

    &lt;p&gt;Returns one or more snapshot objects, which contain metadata about your cluster snapshots. By default, this operation returns information about all snapshots of all clusters that are owned by your Amazon Web Services account. No information is returned for snapshots owned by inactive Amazon Web Services accounts.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all snapshots that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all snapshots that have any combination of those values are returned. Only snapshots that you own are returned in the response; shared snapshots are not returned with the tag key and tag value request parameters.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, snapshots are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterSnapshotsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_subnet_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_subnet_groups

    &lt;p&gt;Returns one or more cluster subnet group objects, which contain metadata about your cluster subnet groups. By default, this operation returns information about all cluster subnet groups that are defined in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all subnet groups that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all subnet groups that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, subnet groups are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterSubnetGroupsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_tracks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_tracks

    Returns a list of all the available maintenance tracks.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterTracksMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_cluster_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_cluster_versions

    Returns descriptions of the available Amazon Redshift cluster versions. You can call this operation even before creating any clusters to learn more about the Amazon Redshift versions. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClusterVersionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_clusters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_clusters

    &lt;p&gt;Returns properties of provisioned clusters including general cluster properties, cluster database properties, maintenance and backup properties, and security and access properties. This operation supports pagination. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all clusters that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all clusters that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, clusters are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeClustersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_custom_domain_associations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_custom_domain_associations

    Contains information for custom domain associations for a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeCustomDomainAssociationsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_data_shares(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_data_shares

    Shows the status of any inbound or outbound datashares available in the specified account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeDataSharesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_data_shares_for_consumer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_data_shares_for_consumer

    Returns a list of datashares where the account identifier being called is a consumer account identifier.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeDataSharesForConsumerMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_data_shares_for_producer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_data_shares_for_producer

    Returns a list of datashares when the account identifier being called is a producer account identifier.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeDataSharesForProducerMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_default_cluster_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_default_cluster_parameters

    &lt;p&gt;Returns a list of parameter settings for the specified parameter group family.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeDefaultClusterParametersMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_endpoint_access

    Describes a Redshift-managed VPC endpoint.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeEndpointAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_endpoint_authorization(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_endpoint_authorization

    Describes an endpoint authorization.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeEndpointAuthorizationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_event_categories(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_event_categories

    Displays a list of event categories for all event source types, or for a specified source type. For a list of the event categories and source types, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html\&quot;&gt;Amazon Redshift Event Notifications&lt;/a&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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

    &lt;p&gt;Lists descriptions of all the Amazon Redshift event notification subscriptions for a customer account. If you specify a subscription name, lists the description for that subscription.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all event notification subscriptions that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all subscriptions that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, subscriptions are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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

    Returns events related to clusters, security groups, snapshots, and parameter groups for the past 14 days. Events specific to a particular cluster, security group, snapshot or parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def p_ost_describe_hsm_client_certificates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_hsm_client_certificates

    &lt;p&gt;Returns information about the specified HSM client certificate. If no certificate ID is specified, returns information about all the HSM certificates owned by your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM client certificates that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all HSM client certificates that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, HSM client certificates are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeHsmClientCertificatesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_hsm_configurations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_hsm_configurations

    &lt;p&gt;Returns information about the specified Amazon Redshift HSM configuration. If no configuration ID is specified, returns information about all the HSM configurations owned by your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM connections that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all HSM connections that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, HSM connections are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeHsmConfigurationsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_logging_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_logging_status

    Describes whether information, such as queries and connection attempts, is being logged for the specified Amazon Redshift cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeLoggingStatusMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_node_configuration_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_node_configuration_options

    Returns properties of possible node configurations such as node type, number of nodes, and disk usage for the specified action type.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeNodeConfigurationOptionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_orderable_cluster_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_orderable_cluster_options

    Returns a list of orderable cluster options. Before you create a new cluster you can use this operation to find what options are available, such as the EC2 Availability Zones (AZ) in the specific Amazon Web Services Region that you can specify, and the node types you can request. The node types differ by available storage, memory, CPU and price. With the cost involved you might want to obtain a list of cluster options in the specific region and specify values when creating a cluster. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeOrderableClusterOptionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_partners(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_partners

    Returns information about the partner integrations defined for a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribePartnersInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_reserved_node_exchange_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_reserved_node_exchange_status

    Returns exchange status details and associated metadata for a reserved-node exchange. Statuses include such values as in progress and requested.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeReservedNodeExchangeStatusInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_reserved_node_offerings(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_reserved_node_offerings

    &lt;p&gt;Returns a list of the available reserved node offerings by Amazon Redshift with their descriptions including the node type, the fixed and recurring costs of reserving the node and duration the node will be reserved for you. These descriptions help you determine which reserve node offering you want to purchase. You then use the unique offering ID in you call to &lt;a&gt;PurchaseReservedNodeOffering&lt;/a&gt; to reserve one or more nodes for your Amazon Redshift cluster. &lt;/p&gt; &lt;p&gt; For more information about reserved node offerings, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html\&quot;&gt;Purchasing Reserved Nodes&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeReservedNodeOfferingsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_reserved_nodes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_reserved_nodes

    Returns the descriptions of the reserved nodes.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeReservedNodesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_resize(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_resize

    &lt;p&gt;Returns information about the last resize operation for the specified cluster. If no resize operation has ever been initiated for the specified cluster, a &lt;code&gt;HTTP 404&lt;/code&gt; error is returned. If a resize operation was initiated and completed, the status of the resize remains as &lt;code&gt;SUCCEEDED&lt;/code&gt; until the next resize. &lt;/p&gt; &lt;p&gt;A resize operation can be requested using &lt;a&gt;ModifyCluster&lt;/a&gt; and specifying a different number or type of nodes for the cluster. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeResizeMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_scheduled_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_scheduled_actions

    Describes properties of scheduled actions. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeScheduledActionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_snapshot_copy_grants(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_snapshot_copy_grants

    &lt;p&gt;Returns a list of snapshot copy grants owned by the Amazon Web Services account in the destination region.&lt;/p&gt; &lt;p&gt; For more information about managing snapshot copy grants, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html\&quot;&gt;Amazon Redshift Database Encryption&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeSnapshotCopyGrantsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_snapshot_schedules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_snapshot_schedules

    Returns a list of snapshot schedules. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeSnapshotSchedulesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_storage(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_storage

    Returns account level backups storage size and provisional storage.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_table_restore_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_table_restore_status

    Lists the status of one or more table restore requests made using the &lt;a&gt;RestoreTableFromClusterSnapshot&lt;/a&gt; API action. If you don&#39;t specify a value for the &lt;code&gt;TableRestoreRequestId&lt;/code&gt; parameter, then &lt;code&gt;DescribeTableRestoreStatus&lt;/code&gt; returns the status of all table restore requests ordered by the date and time of the request in ascending order. Otherwise &lt;code&gt;DescribeTableRestoreStatus&lt;/code&gt; returns the status of the table specified by &lt;code&gt;TableRestoreRequestId&lt;/code&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeTableRestoreStatusMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_tags

    &lt;p&gt;Returns a list of tags. You can return tags from a specific resource by specifying an ARN, or you can return all tags for a given type of resource, such as clusters, snapshots, and so on.&lt;/p&gt; &lt;p&gt;The following are limitations for &lt;code&gt;DescribeTags&lt;/code&gt;: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You cannot specify an ARN and a resource-type value together in the same request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You cannot use the &lt;code&gt;MaxRecords&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters together with the ARN parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;MaxRecords&lt;/code&gt; parameter can be a range from 10 to 50 results to return in a request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify both tag keys and tag values in the same request, Amazon Redshift returns all resources that match any combination of the specified keys and values. For example, if you have &lt;code&gt;owner&lt;/code&gt; and &lt;code&gt;environment&lt;/code&gt; for tag keys, and &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;test&lt;/code&gt; for tag values, all resources that have any combination of those values are returned.&lt;/p&gt; &lt;p&gt;If both tag keys and values are omitted from the request, resources are returned regardless of whether they have tag keys or values associated with them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeTagsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_usage_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_usage_limits

    &lt;p&gt;Shows usage limits on a cluster. Results are filtered based on the combination of input usage limit identifier, cluster identifier, and feature type parameters:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If usage limit identifier, cluster identifier, and feature type are not provided, then all usage limit objects for the current account in the current region are returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If usage limit identifier is provided, then the corresponding usage limit object is returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If cluster identifier is provided, then all usage limit objects for the specified cluster are returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If cluster identifier and feature type are provided, then all usage limit objects for the combination of cluster and feature are returned.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeUsageLimitsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_disable_logging(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disable_logging

    Stops logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DisableLoggingMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_disable_snapshot_copy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disable_snapshot_copy

    &lt;p&gt;Disables the automatic copying of snapshots from one region to another region for a specified cluster.&lt;/p&gt; &lt;p&gt;If your cluster and its snapshots are encrypted using an encrypted symmetric key from Key Management Service, use &lt;a&gt;DeleteSnapshotCopyGrant&lt;/a&gt; to delete the grant that grants Amazon Redshift permission to the key in the destination region. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DisableSnapshotCopyMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_disassociate_data_share_consumer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disassociate_data_share_consumer

    From a datashare consumer account, remove association for the specified datashare. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DisassociateDataShareConsumerMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_enable_logging(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_enable_logging

    Starts logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = EnableLoggingMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_enable_snapshot_copy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_enable_snapshot_copy

    Enables the automatic copy of snapshots from one region to another region for a specified cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = EnableSnapshotCopyMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_cluster_credentials(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_cluster_credentials

    &lt;p&gt;Returns a database user name and temporary password with temporary authorization to log on to an Amazon Redshift database. The action returns the database user name prefixed with &lt;code&gt;IAM:&lt;/code&gt; if &lt;code&gt;AutoCreate&lt;/code&gt; is &lt;code&gt;False&lt;/code&gt; or &lt;code&gt;IAMA:&lt;/code&gt; if &lt;code&gt;AutoCreate&lt;/code&gt; is &lt;code&gt;True&lt;/code&gt;. You can optionally specify one or more database user groups that the user will join at log on. By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html\&quot;&gt;Using IAM Authentication to Generate Database User Credentials&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;The Identity and Access Management (IAM) user or role that runs GetClusterCredentials must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html#redshift-policy-resources.getclustercredentials-resources\&quot;&gt;Resource Policies for GetClusterCredentials&lt;/a&gt; in the Amazon Redshift Cluster Management Guide.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;DbGroups&lt;/code&gt; parameter is specified, the IAM policy must allow the &lt;code&gt;redshift:JoinGroup&lt;/code&gt; action with access to the listed &lt;code&gt;dbgroups&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;In addition, if the &lt;code&gt;AutoCreate&lt;/code&gt; parameter is set to &lt;code&gt;True&lt;/code&gt;, then the policy must include the &lt;code&gt;redshift:CreateClusterUser&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;DbName&lt;/code&gt; parameter is specified, the IAM policy must allow access to the resource &lt;code&gt;dbname&lt;/code&gt; for the specified database name. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetClusterCredentialsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_cluster_credentials_with_iam(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_cluster_credentials_with_iam

    &lt;p&gt;Returns a database user name and temporary password with temporary authorization to log in to an Amazon Redshift database. The database user is mapped 1:1 to the source Identity and Access Management (IAM) identity. For more information about IAM identities, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html\&quot;&gt;IAM Identities (users, user groups, and roles)&lt;/a&gt; in the Amazon Web Services Identity and Access Management User Guide.&lt;/p&gt; &lt;p&gt;The Identity and Access Management (IAM) identity that runs this operation must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html\&quot;&gt;Using identity-based policies (IAM policies)&lt;/a&gt; in the Amazon Redshift Cluster Management Guide. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetClusterCredentialsWithIAMMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_reserved_node_exchange_configuration_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_get_reserved_node_exchange_configuration_options

    Gets the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node offering. Details include the node type, the price, the node count, and the offering type.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetReservedNodeExchangeConfigurationOptionsInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_reserved_node_exchange_offerings(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, marker=None, body=None) -> web.Response:
    """p_ost_get_reserved_node_exchange_offerings

    Returns an array of DC2 ReservedNodeOfferings that matches the payment type, term, and usage price of the given DC1 reserved node.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetReservedNodeExchangeOfferingsInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_aqua_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_aqua_configuration

    This operation is retired. Calling this operation does not change AQUA configuration. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator). 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyAquaInputMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_authentication_profile(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_authentication_profile

    Modifies an authentication profile.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyAuthenticationProfileMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster

    &lt;p&gt;Modifies the settings for a cluster.&lt;/p&gt; &lt;p&gt;You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.&lt;/p&gt; &lt;p&gt;You can add another security or parameter group, or change the admin user password. Resetting a cluster password or modifying the security groups associated with a cluster do not need a reboot. However, modifying a parameter group requires a reboot for parameters to take effect. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster_db_revision(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster_db_revision

    Modifies the database revision of a cluster. The database revision is a unique revision of the database running in a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterDbRevisionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster_iam_roles(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster_iam_roles

    &lt;p&gt;Modifies the list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services.&lt;/p&gt; &lt;p&gt;The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html\&quot;&gt;Quotas and limits&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterIamRolesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster_maintenance(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster_maintenance

    Modifies the maintenance settings of a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterMaintenanceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster_parameter_group

    &lt;p&gt;Modifies the parameters of a parameter group. For the parameters parameter, it can&#39;t contain ASCII characters.&lt;/p&gt; &lt;p&gt; For more information about parameters and parameter groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html\&quot;&gt;Amazon Redshift Parameter Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster_snapshot

    &lt;p&gt;Modifies the settings for a snapshot.&lt;/p&gt; &lt;p&gt;This exanmple modifies the manual retention period setting for a cluster snapshot.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster_snapshot_schedule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster_snapshot_schedule

    Modifies a snapshot schedule for a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterSnapshotScheduleMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_cluster_subnet_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_cluster_subnet_group

    Modifies a cluster subnet group to include the specified list of VPC subnets. The operation replaces the existing list of subnets with the new list of subnets.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyClusterSubnetGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_custom_domain_association(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_custom_domain_association

    Contains information for changing a custom domain association.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyCustomDomainAssociationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_endpoint_access

    Modifies a Redshift-managed VPC endpoint.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyEndpointAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_event_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_event_subscription

    Modifies an existing Amazon Redshift event notification subscription.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def p_ost_modify_scheduled_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_scheduled_action

    Modifies a scheduled action. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyScheduledActionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_snapshot_copy_retention_period(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_snapshot_copy_retention_period

    Modifies the number of days to retain snapshots in the destination Amazon Web Services Region after they are copied from the source Amazon Web Services Region. By default, this operation only changes the retention period of copied automated snapshots. The retention periods for both new and existing copied automated snapshots are updated with the new retention period. You can set the manual option to change only the retention periods of copied manual snapshots. If you set this option, only newly copied manual snapshots have the new retention period. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifySnapshotCopyRetentionPeriodMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_snapshot_schedule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_snapshot_schedule

    Modifies a snapshot schedule. Any schedule associated with a cluster is modified asynchronously.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifySnapshotScheduleMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_usage_limit(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_usage_limit

    Modifies a usage limit in a cluster. You can&#39;t modify the feature type or period of a usage limit.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ModifyUsageLimitMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_pause_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_pause_cluster

    Pauses a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PauseClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_purchase_reserved_node_offering(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_purchase_reserved_node_offering

    &lt;p&gt;Allows you to purchase reserved nodes. Amazon Redshift offers a predefined set of reserved node offerings. You can purchase one or more of the offerings. You can call the &lt;a&gt;DescribeReservedNodeOfferings&lt;/a&gt; API to obtain the available reserved node offerings. You can call this API by providing a specific reserved node offering and the number of nodes you want to reserve. &lt;/p&gt; &lt;p&gt; For more information about reserved node offerings, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html\&quot;&gt;Purchasing Reserved Nodes&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PurchaseReservedNodeOfferingMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_reboot_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reboot_cluster

    Reboots a cluster. This action is taken as soon as possible. It results in a momentary outage to the cluster, during which the cluster status is set to &lt;code&gt;rebooting&lt;/code&gt;. A cluster event is created when the reboot is completed. Any pending cluster modifications (see &lt;a&gt;ModifyCluster&lt;/a&gt;) are applied at this reboot. For more information about managing clusters, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html\&quot;&gt;Amazon Redshift Clusters&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RebootClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_reject_data_share(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reject_data_share

    From a datashare consumer account, rejects the specified datashare.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RejectDataShareMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_reset_cluster_parameter_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reset_cluster_parameter_group

    Sets one or more parameters of the specified parameter group to their default values and sets the source values of the parameters to \&quot;engine-default\&quot;. To reset the entire parameter group specify the &lt;i&gt;ResetAllParameters&lt;/i&gt; parameter. For parameter changes to take effect you must reboot any associated clusters. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ResetClusterParameterGroupMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_resize_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_resize_cluster

    &lt;p&gt;Changes the size of the cluster. You can change the cluster&#39;s type, or change the number or type of nodes. The default behavior is to use the elastic resize method. With an elastic resize, your cluster is available for read and write operations more quickly than with the classic resize method. &lt;/p&gt; &lt;p&gt;Elastic resize operations have the following restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can only resize clusters of the following types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;dc1.large (if your cluster is in a VPC)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;dc1.8xlarge (if your cluster is in a VPC)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;dc2.large&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;dc2.8xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ds2.xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ds2.8xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ra3.xlplus&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ra3.4xlarge&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;ra3.16xlarge&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The type of nodes that you add must match the node type for the cluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ResizeClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_restore_from_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_restore_from_cluster_snapshot

    &lt;p&gt;Creates a new cluster from a snapshot. By default, Amazon Redshift creates the resulting cluster with the same configuration as the original cluster from which the snapshot was created, except that the new cluster is created with the default cluster security and parameter groups. After Amazon Redshift creates the cluster, you can use the &lt;a&gt;ModifyCluster&lt;/a&gt; API to associate a different security group and different parameter group with the restored cluster. If you are using a DS node type, you can also choose to change to another DS node type of the same size during restore.&lt;/p&gt; &lt;p&gt;If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RestoreFromClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_restore_table_from_cluster_snapshot(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_restore_table_from_cluster_snapshot

    &lt;p&gt;Creates a new table from a table in an Amazon Redshift cluster snapshot. You must create the new table within the Amazon Redshift cluster that the snapshot was taken from.&lt;/p&gt; &lt;p&gt;You cannot use &lt;code&gt;RestoreTableFromClusterSnapshot&lt;/code&gt; to restore a table with the same name as an existing table in an Amazon Redshift cluster. That is, you cannot overwrite an existing table in a cluster with a restored table. If you want to replace your original table with a new, restored table, then rename or drop your original table before you call &lt;code&gt;RestoreTableFromClusterSnapshot&lt;/code&gt;. When you have renamed your original table, then you can pass the original name of the table as the &lt;code&gt;NewTableName&lt;/code&gt; parameter value in the call to &lt;code&gt;RestoreTableFromClusterSnapshot&lt;/code&gt;. This way, you can replace the original table with the table created from the snapshot.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to restore tables with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved\&quot;&gt;interleaved sort keys&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RestoreTableFromClusterSnapshotMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_resume_cluster(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_resume_cluster

    Resumes a paused cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ResumeClusterMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_revoke_cluster_security_group_ingress(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_revoke_cluster_security_group_ingress

    Revokes an ingress rule in an Amazon Redshift security group for a previously authorized IP range or Amazon EC2 security group. To add an ingress rule, see &lt;a&gt;AuthorizeClusterSecurityGroupIngress&lt;/a&gt;. For information about managing security groups, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html\&quot;&gt;Amazon Redshift Cluster Security Groups&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RevokeClusterSecurityGroupIngressMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_revoke_endpoint_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_revoke_endpoint_access

    Revokes access to a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RevokeEndpointAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_revoke_snapshot_access(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_revoke_snapshot_access

    &lt;p&gt;Removes the ability of the specified Amazon Web Services account to restore the specified snapshot. If the account is currently restoring the snapshot, the restore will run to completion.&lt;/p&gt; &lt;p&gt; For more information about working with snapshots, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html\&quot;&gt;Amazon Redshift Snapshots&lt;/a&gt; in the &lt;i&gt;Amazon Redshift Cluster Management Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RevokeSnapshotAccessMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_rotate_encryption_key(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_rotate_encryption_key

    Rotates the encryption keys for a cluster.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RotateEncryptionKeyMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_partner_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_partner_status

    Updates the status of a partner integration.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdatePartnerStatusInputMessage.from_dict(body)
    return web.Response(status=200)
