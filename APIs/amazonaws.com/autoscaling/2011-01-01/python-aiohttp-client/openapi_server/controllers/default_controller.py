from typing import List, Dict
from aiohttp import web

from openapi_server.models.activities_type import ActivitiesType
from openapi_server.models.activity_type import ActivityType
from openapi_server.models.attach_instances_query import AttachInstancesQuery
from openapi_server.models.attach_load_balancer_target_groups_type import AttachLoadBalancerTargetGroupsType
from openapi_server.models.attach_load_balancers_type import AttachLoadBalancersType
from openapi_server.models.attach_traffic_sources_type import AttachTrafficSourcesType
from openapi_server.models.auto_scaling_group_names_type import AutoScalingGroupNamesType
from openapi_server.models.auto_scaling_groups_type import AutoScalingGroupsType
from openapi_server.models.auto_scaling_instances_type import AutoScalingInstancesType
from openapi_server.models.batch_delete_scheduled_action_answer import BatchDeleteScheduledActionAnswer
from openapi_server.models.batch_delete_scheduled_action_type import BatchDeleteScheduledActionType
from openapi_server.models.batch_put_scheduled_update_group_action_answer import BatchPutScheduledUpdateGroupActionAnswer
from openapi_server.models.batch_put_scheduled_update_group_action_type import BatchPutScheduledUpdateGroupActionType
from openapi_server.models.block_device_mapping import BlockDeviceMapping
from openapi_server.models.cancel_instance_refresh_answer import CancelInstanceRefreshAnswer
from openapi_server.models.cancel_instance_refresh_type import CancelInstanceRefreshType
from openapi_server.models.complete_lifecycle_action_type import CompleteLifecycleActionType
from openapi_server.models.create_auto_scaling_group_type import CreateAutoScalingGroupType
from openapi_server.models.create_launch_configuration_type import CreateLaunchConfigurationType
from openapi_server.models.create_or_update_tags_type import CreateOrUpdateTagsType
from openapi_server.models.delete_auto_scaling_group_type import DeleteAutoScalingGroupType
from openapi_server.models.delete_lifecycle_hook_type import DeleteLifecycleHookType
from openapi_server.models.delete_notification_configuration_type import DeleteNotificationConfigurationType
from openapi_server.models.delete_policy_type import DeletePolicyType
from openapi_server.models.delete_scheduled_action_type import DeleteScheduledActionType
from openapi_server.models.delete_tags_type import DeleteTagsType
from openapi_server.models.delete_warm_pool_type import DeleteWarmPoolType
from openapi_server.models.describe_account_limits_answer import DescribeAccountLimitsAnswer
from openapi_server.models.describe_adjustment_types_answer import DescribeAdjustmentTypesAnswer
from openapi_server.models.describe_auto_scaling_instances_type import DescribeAutoScalingInstancesType
from openapi_server.models.describe_auto_scaling_notification_types_answer import DescribeAutoScalingNotificationTypesAnswer
from openapi_server.models.describe_instance_refreshes_answer import DescribeInstanceRefreshesAnswer
from openapi_server.models.describe_instance_refreshes_type import DescribeInstanceRefreshesType
from openapi_server.models.describe_lifecycle_hook_types_answer import DescribeLifecycleHookTypesAnswer
from openapi_server.models.describe_lifecycle_hooks_answer import DescribeLifecycleHooksAnswer
from openapi_server.models.describe_lifecycle_hooks_type import DescribeLifecycleHooksType
from openapi_server.models.describe_load_balancer_target_groups_request import DescribeLoadBalancerTargetGroupsRequest
from openapi_server.models.describe_load_balancer_target_groups_response import DescribeLoadBalancerTargetGroupsResponse
from openapi_server.models.describe_load_balancers_request import DescribeLoadBalancersRequest
from openapi_server.models.describe_load_balancers_response import DescribeLoadBalancersResponse
from openapi_server.models.describe_metric_collection_types_answer import DescribeMetricCollectionTypesAnswer
from openapi_server.models.describe_notification_configurations_answer import DescribeNotificationConfigurationsAnswer
from openapi_server.models.describe_notification_configurations_type import DescribeNotificationConfigurationsType
from openapi_server.models.describe_policies_type import DescribePoliciesType
from openapi_server.models.describe_scaling_activities_type import DescribeScalingActivitiesType
from openapi_server.models.describe_scheduled_actions_type import DescribeScheduledActionsType
from openapi_server.models.describe_tags_type import DescribeTagsType
from openapi_server.models.describe_termination_policy_types_answer import DescribeTerminationPolicyTypesAnswer
from openapi_server.models.describe_traffic_sources_request import DescribeTrafficSourcesRequest
from openapi_server.models.describe_traffic_sources_response import DescribeTrafficSourcesResponse
from openapi_server.models.describe_warm_pool_answer import DescribeWarmPoolAnswer
from openapi_server.models.describe_warm_pool_type import DescribeWarmPoolType
from openapi_server.models.detach_instances_answer import DetachInstancesAnswer
from openapi_server.models.detach_instances_query import DetachInstancesQuery
from openapi_server.models.detach_load_balancer_target_groups_type import DetachLoadBalancerTargetGroupsType
from openapi_server.models.detach_load_balancers_type import DetachLoadBalancersType
from openapi_server.models.detach_traffic_sources_type import DetachTrafficSourcesType
from openapi_server.models.disable_metrics_collection_query import DisableMetricsCollectionQuery
from openapi_server.models.enable_metrics_collection_query import EnableMetricsCollectionQuery
from openapi_server.models.enter_standby_answer import EnterStandbyAnswer
from openapi_server.models.enter_standby_query import EnterStandbyQuery
from openapi_server.models.execute_policy_type import ExecutePolicyType
from openapi_server.models.exit_standby_answer import ExitStandbyAnswer
from openapi_server.models.exit_standby_query import ExitStandbyQuery
from openapi_server.models.filter import Filter
from openapi_server.models.get_create_auto_scaling_group_launch_template_parameter import GETCreateAutoScalingGroupLaunchTemplateParameter
from openapi_server.models.get_create_auto_scaling_group_mixed_instances_policy_parameter import GETCreateAutoScalingGroupMixedInstancesPolicyParameter
from openapi_server.models.get_create_launch_configuration_instance_monitoring_parameter import GETCreateLaunchConfigurationInstanceMonitoringParameter
from openapi_server.models.get_create_launch_configuration_metadata_options_parameter import GETCreateLaunchConfigurationMetadataOptionsParameter
from openapi_server.models.get_put_scaling_policy_predictive_scaling_configuration_parameter import GETPutScalingPolicyPredictiveScalingConfigurationParameter
from openapi_server.models.get_put_scaling_policy_target_tracking_configuration_parameter import GETPutScalingPolicyTargetTrackingConfigurationParameter
from openapi_server.models.get_put_warm_pool_instance_reuse_policy_parameter import GETPutWarmPoolInstanceReusePolicyParameter
from openapi_server.models.get_start_instance_refresh_desired_configuration_parameter import GETStartInstanceRefreshDesiredConfigurationParameter
from openapi_server.models.get_start_instance_refresh_preferences_parameter import GETStartInstanceRefreshPreferencesParameter
from openapi_server.models.get_predictive_scaling_forecast_answer import GetPredictiveScalingForecastAnswer
from openapi_server.models.get_predictive_scaling_forecast_type import GetPredictiveScalingForecastType
from openapi_server.models.launch_configuration_name_type import LaunchConfigurationNameType
from openapi_server.models.launch_configuration_names_type import LaunchConfigurationNamesType
from openapi_server.models.launch_configurations_type import LaunchConfigurationsType
from openapi_server.models.lifecycle_hook_specification import LifecycleHookSpecification
from openapi_server.models.policies_type import PoliciesType
from openapi_server.models.policy_arn_type import PolicyARNType
from openapi_server.models.processes_type import ProcessesType
from openapi_server.models.put_lifecycle_hook_type import PutLifecycleHookType
from openapi_server.models.put_notification_configuration_type import PutNotificationConfigurationType
from openapi_server.models.put_scaling_policy_type import PutScalingPolicyType
from openapi_server.models.put_scheduled_update_group_action_type import PutScheduledUpdateGroupActionType
from openapi_server.models.put_warm_pool_type import PutWarmPoolType
from openapi_server.models.record_lifecycle_action_heartbeat_type import RecordLifecycleActionHeartbeatType
from openapi_server.models.rollback_instance_refresh_answer import RollbackInstanceRefreshAnswer
from openapi_server.models.rollback_instance_refresh_type import RollbackInstanceRefreshType
from openapi_server.models.scaling_process_query import ScalingProcessQuery
from openapi_server.models.scheduled_actions_type import ScheduledActionsType
from openapi_server.models.scheduled_update_group_action_request import ScheduledUpdateGroupActionRequest
from openapi_server.models.set_desired_capacity_type import SetDesiredCapacityType
from openapi_server.models.set_instance_health_query import SetInstanceHealthQuery
from openapi_server.models.set_instance_protection_query import SetInstanceProtectionQuery
from openapi_server.models.start_instance_refresh_answer import StartInstanceRefreshAnswer
from openapi_server.models.start_instance_refresh_type import StartInstanceRefreshType
from openapi_server.models.step_adjustment import StepAdjustment
from openapi_server.models.tag import Tag
from openapi_server.models.tags_type import TagsType
from openapi_server.models.terminate_instance_in_auto_scaling_group_type import TerminateInstanceInAutoScalingGroupType
from openapi_server.models.traffic_source_identifier import TrafficSourceIdentifier
from openapi_server.models.update_auto_scaling_group_type import UpdateAutoScalingGroupType
from openapi_server import util


async def g_et_attach_instances(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, instance_ids=None) -> web.Response:
    """g_et_attach_instances

    &lt;p&gt;Attaches one or more EC2 instances to the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you attach instances, Amazon EC2 Auto Scaling increases the desired capacity of the group by the number of instances being attached. If the number of instances being attached plus the desired capacity of the group exceeds the maximum size of the group, the operation fails.&lt;/p&gt; &lt;p&gt;If there is a Classic Load Balancer attached to your Auto Scaling group, the instances are also registered with the load balancer. If there are target groups attached to your Auto Scaling group, the instances are also registered with the target groups.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-instance-asg.html\&quot;&gt;Attach EC2 instances to your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param instance_ids: The IDs of the instances. You can specify up to 20 instances.
    :type instance_ids: List[str]

    """
    return web.Response(status=200)


async def g_et_attach_load_balancer_target_groups(request: web.Request, auto_scaling_group_name, target_group_arns, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_attach_load_balancer_target_groups

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;AttachTrafficSources&lt;/a&gt;, which can attach multiple traffic sources types. We recommend using &lt;code&gt;AttachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;AttachLoadBalancerTargetGroups&lt;/code&gt;. You can use both the original &lt;code&gt;AttachLoadBalancerTargetGroups&lt;/code&gt; API operation and &lt;code&gt;AttachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Attaches one or more target groups to the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation is used with the following load balancer types: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Application Load Balancer - Operates at the application layer (layer 7) and supports HTTP and HTTPS. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Network Load Balancer - Operates at the transport layer (layer 4) and supports TCP, TLS, and UDP. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Gateway Load Balancer - Operates at the network layer (layer 3).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To describe the target groups for an Auto Scaling group, call the &lt;a&gt;DescribeLoadBalancerTargetGroups&lt;/a&gt; API. To detach the target group from the Auto Scaling group, call the &lt;a&gt;DetachLoadBalancerTargetGroups&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;This operation is additive and does not detach existing target groups or Classic Load Balancers from the Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param target_group_arns: The Amazon Resource Names (ARNs) of the target groups. You can specify up to 10 target groups. To get the ARN of a target group, use the Elastic Load Balancing &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html\&quot;&gt;DescribeTargetGroups&lt;/a&gt; API operation.
    :type target_group_arns: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_attach_load_balancers(request: web.Request, auto_scaling_group_name, load_balancer_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_attach_load_balancers

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;AttachTrafficSources&lt;/a&gt;, which can attach multiple traffic sources types. We recommend using &lt;code&gt;AttachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;AttachLoadBalancers&lt;/code&gt;. You can use both the original &lt;code&gt;AttachLoadBalancers&lt;/code&gt; API operation and &lt;code&gt;AttachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Attaches one or more Classic Load Balancers to the specified Auto Scaling group. Amazon EC2 Auto Scaling registers the running instances with these Classic Load Balancers.&lt;/p&gt; &lt;p&gt;To describe the load balancers for an Auto Scaling group, call the &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; API. To detach a load balancer from the Auto Scaling group, call the &lt;a&gt;DetachLoadBalancers&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;This operation is additive and does not detach existing Classic Load Balancers or target groups from the Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param load_balancer_names: The names of the load balancers. You can specify up to 10 load balancers.
    :type load_balancer_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_attach_traffic_sources(request: web.Request, auto_scaling_group_name, traffic_sources, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_attach_traffic_sources

    &lt;p&gt;Attaches one or more traffic sources to the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;You can use any of the following as traffic sources for an Auto Scaling group:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Application Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Classic Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Gateway Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Network Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VPC Lattice&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is additive and does not detach existing traffic sources from the Auto Scaling group. &lt;/p&gt; &lt;p&gt;After the operation completes, use the &lt;a&gt;DescribeTrafficSources&lt;/a&gt; API to return details about the state of the attachments between traffic sources and your Auto Scaling group. To detach a traffic source from the Auto Scaling group, call the &lt;a&gt;DetachTrafficSources&lt;/a&gt; API.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param traffic_sources: The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.
    :type traffic_sources: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    traffic_sources = [TrafficSourceIdentifier.from_dict(d) for d in traffic_sources]
    return web.Response(status=200)


async def g_et_batch_delete_scheduled_action(request: web.Request, auto_scaling_group_name, scheduled_action_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_batch_delete_scheduled_action

    Deletes one or more scheduled actions for the specified Auto Scaling group.

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param scheduled_action_names: The names of the scheduled actions to delete. The maximum number allowed is 50. 
    :type scheduled_action_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_batch_put_scheduled_update_group_action(request: web.Request, auto_scaling_group_name, scheduled_update_group_actions, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_batch_put_scheduled_update_group_action

    Creates or updates one or more scheduled scaling actions for an Auto Scaling group.

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param scheduled_update_group_actions: One or more scheduled actions. The maximum number allowed is 50.
    :type scheduled_update_group_actions: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    scheduled_update_group_actions = [ScheduledUpdateGroupActionRequest.from_dict(d) for d in scheduled_update_group_actions]
    return web.Response(status=200)


async def g_et_cancel_instance_refresh(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_cancel_instance_refresh

    &lt;p&gt;Cancels an instance refresh or rollback that is in progress. If an instance refresh or rollback is not in progress, an &lt;code&gt;ActiveInstanceRefreshNotFound&lt;/code&gt; error occurs.&lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.&lt;/p&gt; &lt;p&gt;When you cancel an instance refresh, this does not roll back any changes that it made. Use the &lt;a&gt;RollbackInstanceRefresh&lt;/a&gt; API to roll back instead.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_complete_lifecycle_action(request: web.Request, lifecycle_hook_name, auto_scaling_group_name, lifecycle_action_result, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, lifecycle_action_token=None, instance_id=None) -> web.Response:
    """g_et_complete_lifecycle_action

    &lt;p&gt;Completes the lifecycle action for the specified token or instance with the specified result.&lt;/p&gt; &lt;p&gt;This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If you finish before the timeout period ends, send a callback by using the &lt;a&gt;CompleteLifecycleAction&lt;/a&gt; API call.&lt;/b&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/completing-lifecycle-hooks.html\&quot;&gt;Complete a lifecycle action&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param lifecycle_hook_name: The name of the lifecycle hook.
    :type lifecycle_hook_name: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param lifecycle_action_result: The action for the group to take. You can specify either &lt;code&gt;CONTINUE&lt;/code&gt; or &lt;code&gt;ABANDON&lt;/code&gt;.
    :type lifecycle_action_result: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param lifecycle_action_token: A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
    :type lifecycle_action_token: str
    :param instance_id: The ID of the instance.
    :type instance_id: str

    """
    return web.Response(status=200)


async def g_et_create_auto_scaling_group(request: web.Request, auto_scaling_group_name, min_size, max_size, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, launch_configuration_name=None, launch_template=None, mixed_instances_policy=None, instance_id=None, desired_capacity=None, default_cooldown=None, availability_zones=None, load_balancer_names=None, target_group_arns=None, health_check_type=None, health_check_grace_period=None, placement_group=None, vpc_zone_identifier=None, termination_policies=None, new_instances_protected_from_scale_in=None, capacity_rebalance=None, lifecycle_hook_specification_list=None, tags=None, service_linked_role_arn=None, max_instance_lifetime=None, context=None, desired_capacity_type=None, default_instance_warmup=None, traffic_sources=None) -> web.Response:
    """g_et_create_auto_scaling_group

    &lt;p&gt; &lt;b&gt;We strongly recommend using a launch template when calling this operation to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Creates an Auto Scaling group with the specified name and attributes. &lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of Auto Scaling groups, the call fails. To query this limit, call the &lt;a&gt;DescribeAccountLimits&lt;/a&gt; API. For information about updating this limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html\&quot;&gt;Quotas for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For introductory exercises for creating an Auto Scaling group, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html\&quot;&gt;Getting started with Amazon EC2 Auto Scaling&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-register-lbs-with-asg.html\&quot;&gt;Tutorial: Set up a scaled and load-balanced application&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html\&quot;&gt;Auto Scaling groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Every Auto Scaling group has three size properties (&lt;code&gt;DesiredCapacity&lt;/code&gt;, &lt;code&gt;MaxSize&lt;/code&gt;, and &lt;code&gt;MinSize&lt;/code&gt;). Usually, you set these sizes based on a specific number of instances. However, if you configure a mixed instances policy that defines weights for the instance types, you must specify these sizes with the same units that you use for weighting instances.&lt;/p&gt;

    :param auto_scaling_group_name: &lt;p&gt;The name of the Auto Scaling group. This name must be unique per Region per account.&lt;/p&gt; &lt;p&gt;The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot use a colon (:) in the name.&lt;/p&gt; &lt;/note&gt;
    :type auto_scaling_group_name: str
    :param min_size: The minimum size of the group.
    :type min_size: int
    :param max_size: &lt;p&gt;The maximum size of the group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above &lt;code&gt;MaxSize&lt;/code&gt; to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above &lt;code&gt;MaxSize&lt;/code&gt; by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).&lt;/p&gt; &lt;/note&gt;
    :type max_size: int
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param launch_configuration_name: &lt;p&gt;The name of the launch configuration to use to launch instances. &lt;/p&gt; &lt;p&gt;Conditional: You must specify either a launch template (&lt;code&gt;LaunchTemplate&lt;/code&gt; or &lt;code&gt;MixedInstancesPolicy&lt;/code&gt;) or a launch configuration (&lt;code&gt;LaunchConfigurationName&lt;/code&gt; or &lt;code&gt;InstanceId&lt;/code&gt;).&lt;/p&gt;
    :type launch_configuration_name: str
    :param launch_template: &lt;p&gt;Information used to specify the launch template and version to use to launch instances. &lt;/p&gt; &lt;p&gt;Conditional: You must specify either a launch template (&lt;code&gt;LaunchTemplate&lt;/code&gt; or &lt;code&gt;MixedInstancesPolicy&lt;/code&gt;) or a launch configuration (&lt;code&gt;LaunchConfigurationName&lt;/code&gt; or &lt;code&gt;InstanceId&lt;/code&gt;).&lt;/p&gt; &lt;note&gt; &lt;p&gt;The launch template that is specified must be configured for use with an Auto Scaling group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html\&quot;&gt;Creating a launch template for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
    :type launch_template: dict | bytes
    :param mixed_instances_policy: The mixed instances policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html\&quot;&gt;Auto Scaling groups with multiple instance types and purchase options&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type mixed_instances_policy: dict | bytes
    :param instance_id: The ID of the instance used to base the launch configuration on. If specified, Amazon EC2 Auto Scaling uses the configuration values from the specified instance to create a new launch configuration. To get the instance ID, use the Amazon EC2 &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html\&quot;&gt;DescribeInstances&lt;/a&gt; API operation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-from-instance.html\&quot;&gt;Creating an Auto Scaling group using an EC2 instance&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type instance_id: str
    :param desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group at the time of its creation and the capacity it attempts to maintain. It can scale beyond this capacity if you configure auto scaling. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity, the default is the minimum size of the group.
    :type desired_capacity: int
    :param default_cooldown: &lt;p&gt; &lt;i&gt;Only needed if you use simple scaling policies.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html\&quot;&gt;Scaling cooldowns for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;300&lt;/code&gt; seconds&lt;/p&gt;
    :type default_cooldown: int
    :param availability_zones: A list of Availability Zones where instances in the Auto Scaling group can be created. Used for launching into the default VPC subnet in each Availability Zone when not using the &lt;code&gt;VPCZoneIdentifier&lt;/code&gt; property, or for attaching a network interface when an existing network interface ID is specified in a launch template.
    :type availability_zones: List[str]
    :param load_balancer_names: A list of Classic Load Balancers associated with this Auto Scaling group. For Application Load Balancers, Network Load Balancers, and Gateway Load Balancers, specify the &lt;code&gt;TargetGroupARNs&lt;/code&gt; property instead.
    :type load_balancer_names: List[str]
    :param target_group_arns: The Amazon Resource Names (ARN) of the Elastic Load Balancing target groups to associate with the Auto Scaling group. Instances are registered as targets with the target groups. The target groups receive incoming traffic and route requests to one or more registered targets. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type target_group_arns: List[str]
    :param health_check_type: &lt;p&gt;A comma-separated value string of one or more health check types.&lt;/p&gt; &lt;p&gt;The valid values are &lt;code&gt;EC2&lt;/code&gt;, &lt;code&gt;ELB&lt;/code&gt;, and &lt;code&gt;VPC_LATTICE&lt;/code&gt;. &lt;code&gt;EC2&lt;/code&gt; is the default health check and cannot be disabled. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html\&quot;&gt;Health checks for Auto Scaling instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Only specify &lt;code&gt;EC2&lt;/code&gt; if you must clear a value that was previously set.&lt;/p&gt;
    :type health_check_type: str
    :param health_check_grace_period: &lt;p&gt;The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the &lt;code&gt;InService&lt;/code&gt; state. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html\&quot;&gt;Set the health check grace period for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;0&lt;/code&gt; seconds&lt;/p&gt;
    :type health_check_grace_period: int
    :param placement_group: &lt;p&gt;The name of the placement group into which to launch your instances. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html\&quot;&gt;Placement groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A &lt;i&gt;cluster&lt;/i&gt; placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group. &lt;/p&gt; &lt;/note&gt;
    :type placement_group: str
    :param vpc_zone_identifier: A comma-separated list of subnet IDs for a virtual private cloud (VPC) where instances in the Auto Scaling group can be created. If you specify &lt;code&gt;VPCZoneIdentifier&lt;/code&gt; with &lt;code&gt;AvailabilityZones&lt;/code&gt;, the subnets that you specify must reside in those Availability Zones.
    :type vpc_zone_identifier: str
    :param termination_policies: &lt;p&gt;A policy or a list of policies that are used to select the instance to terminate. These policies are executed in the order that you list them. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html\&quot;&gt;Work with Amazon EC2 Auto Scaling termination policies&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;Default&lt;/code&gt; | &lt;code&gt;AllocationStrategy&lt;/code&gt; | &lt;code&gt;ClosestToNextInstanceHour&lt;/code&gt; | &lt;code&gt;NewestInstance&lt;/code&gt; | &lt;code&gt;OldestInstance&lt;/code&gt; | &lt;code&gt;OldestLaunchConfiguration&lt;/code&gt; | &lt;code&gt;OldestLaunchTemplate&lt;/code&gt; | &lt;code&gt;arn:aws:lambda:region:account-id:function:my-function:my-alias&lt;/code&gt; &lt;/p&gt;
    :type termination_policies: List[str]
    :param new_instances_protected_from_scale_in: Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html\&quot;&gt;Using instance scale-in protection&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type new_instances_protected_from_scale_in: bool
    :param capacity_rebalance: Indicates whether Capacity Rebalancing is enabled. Otherwise, Capacity Rebalancing is disabled. When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of interruption. After launching a new instance, it then terminates an old instance. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html\&quot;&gt;Use Capacity Rebalancing to handle Amazon EC2 Spot Interruptions&lt;/a&gt; in the in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type capacity_rebalance: bool
    :param lifecycle_hook_specification_list: One or more lifecycle hooks to add to the Auto Scaling group before instances are launched.
    :type lifecycle_hook_specification_list: list | bytes
    :param tags: One or more tags. You can tag your Auto Scaling group and propagate the tags to the Amazon EC2 instances it launches. Tags are not propagated to Amazon EBS volumes. To add tags to Amazon EBS volumes, specify the tags in a launch template but use caution. If the launch template specifies an instance tag with a key that is also specified for the Auto Scaling group, Amazon EC2 Auto Scaling overrides the value of that instance tag with the value specified by the Auto Scaling group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html\&quot;&gt;Tag Auto Scaling groups and instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type tags: list | bytes
    :param service_linked_role_arn: The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services service on your behalf. By default, Amazon EC2 Auto Scaling uses a service-linked role named &lt;code&gt;AWSServiceRoleForAutoScaling&lt;/code&gt;, which it creates if it does not exist. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html\&quot;&gt;Service-linked roles&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type service_linked_role_arn: str
    :param max_instance_lifetime: The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html\&quot;&gt;Replacing Auto Scaling instances based on maximum instance lifetime&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type max_instance_lifetime: int
    :param context: Reserved.
    :type context: str
    :param desired_capacity_type: &lt;p&gt;The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports &lt;code&gt;DesiredCapacityType&lt;/code&gt; for attribute-based instance type selection only. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-instance-type-requirements.html\&quot;&gt;Creating an Auto Scaling group using attribute-based instance type selection&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;By default, Amazon EC2 Auto Scaling specifies &lt;code&gt;units&lt;/code&gt;, which translates into number of instances.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;units&lt;/code&gt; | &lt;code&gt;vcpu&lt;/code&gt; | &lt;code&gt;memory-mib&lt;/code&gt; &lt;/p&gt;
    :type desired_capacity_type: str
    :param default_instance_warmup: &lt;p&gt;The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the &lt;code&gt;InService&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt;During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html\&quot;&gt;Set the default instance warmup for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, &lt;i&gt;even if it is set to 0 seconds&lt;/i&gt;. To remove a value that you previously set, include the property but specify &lt;code&gt;-1&lt;/code&gt; for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of &lt;code&gt;0&lt;/code&gt; or other nominal value.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Default: None &lt;/p&gt;
    :type default_instance_warmup: int
    :param traffic_sources: The list of traffic sources to attach to this Auto Scaling group. You can use any of the following as traffic sources for an Auto Scaling group: Classic Load Balancer, Application Load Balancer, Gateway Load Balancer, Network Load Balancer, and VPC Lattice.
    :type traffic_sources: list | bytes

    """
    launch_template = .from_dict(launch_template)
    mixed_instances_policy = .from_dict(mixed_instances_policy)
    lifecycle_hook_specification_list = [LifecycleHookSpecification.from_dict(d) for d in lifecycle_hook_specification_list]
    tags = [Tag.from_dict(d) for d in tags]
    traffic_sources = [TrafficSourceIdentifier.from_dict(d) for d in traffic_sources]
    return web.Response(status=200)


async def g_et_create_launch_configuration(request: web.Request, launch_configuration_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, image_id=None, key_name=None, security_groups=None, classic_link_vpcid=None, classic_link_vpc_security_groups=None, user_data=None, instance_id=None, instance_type=None, kernel_id=None, ramdisk_id=None, block_device_mappings=None, instance_monitoring=None, spot_price=None, iam_instance_profile=None, ebs_optimized=None, associate_public_ip_address=None, placement_tenancy=None, metadata_options=None) -> web.Response:
    """g_et_create_launch_configuration

    &lt;p&gt;Creates a launch configuration.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of launch configurations, the call fails. To query this limit, call the &lt;a&gt;DescribeAccountLimits&lt;/a&gt; API. For information about updating this limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html\&quot;&gt;Quotas for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html\&quot;&gt;Launch configurations&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a launch template or a launch configuration. We strongly recommend that you do not use launch configurations. They do not provide full functionality for Amazon EC2 Auto Scaling or Amazon EC2. For information about using launch templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html\&quot;&gt;Launch templates&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param launch_configuration_name: The name of the launch configuration. This name must be unique per Region per account.
    :type launch_configuration_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param image_id: &lt;p&gt;The ID of the Amazon Machine Image (AMI) that was assigned during registration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html\&quot;&gt;Finding a Linux AMI&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;InstanceId&lt;/code&gt;, an &lt;code&gt;ImageId&lt;/code&gt; is not required.&lt;/p&gt;
    :type image_id: str
    :param key_name: The name of the key pair. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html\&quot;&gt;Amazon EC2 key pairs and Linux instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.
    :type key_name: str
    :param security_groups: A list that contains the security group IDs to assign to the instances in the Auto Scaling group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html\&quot;&gt;Control traffic to resources using security groups&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.
    :type security_groups: List[str]
    :param classic_link_vpcid: Available for backward compatibility.
    :type classic_link_vpcid: str
    :param classic_link_vpc_security_groups: Available for backward compatibility.
    :type classic_link_vpc_security_groups: List[str]
    :param user_data: The user data to make available to the launched EC2 instances. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html\&quot;&gt;Instance metadata and user data&lt;/a&gt; (Linux) and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-metadata.html\&quot;&gt;Instance metadata and user data&lt;/a&gt; (Windows). If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text. User data is limited to 16 KB.
    :type user_data: str
    :param instance_id: &lt;p&gt;The ID of the instance to use to create the launch configuration. The new launch configuration derives attributes from the instance, except for the block device mapping.&lt;/p&gt; &lt;p&gt;To create a launch configuration with a block device mapping or override any other instance attributes, specify them as part of the same request.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-lc-with-instanceID.html\&quot;&gt;Creating a launch configuration using an EC2 instance&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;
    :type instance_id: str
    :param instance_type: &lt;p&gt;Specifies the instance type of the EC2 instance. For information about available instance types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes\&quot;&gt;Available instance types&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;InstanceId&lt;/code&gt;, an &lt;code&gt;InstanceType&lt;/code&gt; is not required.&lt;/p&gt;
    :type instance_type: str
    :param kernel_id: &lt;p&gt;The ID of the kernel associated with the AMI.&lt;/p&gt; &lt;note&gt; &lt;p&gt;We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html\&quot;&gt;User provided kernels&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
    :type kernel_id: str
    :param ramdisk_id: &lt;p&gt;The ID of the RAM disk to select.&lt;/p&gt; &lt;note&gt; &lt;p&gt;We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html\&quot;&gt;User provided kernels&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;
    :type ramdisk_id: str
    :param block_device_mappings: The block device mapping entries that define the block devices to attach to the instances at launch. By default, the block devices specified in the block device mapping for the AMI are used. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html\&quot;&gt;Block device mappings&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.
    :type block_device_mappings: list | bytes
    :param instance_monitoring: &lt;p&gt;Controls whether instances in this group are launched with detailed (&lt;code&gt;true&lt;/code&gt;) or basic (&lt;code&gt;false&lt;/code&gt;) monitoring.&lt;/p&gt; &lt;p&gt;The default value is &lt;code&gt;true&lt;/code&gt; (enabled).&lt;/p&gt; &lt;important&gt; &lt;p&gt;When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/latest/userguide/enable-as-instance-metrics.html\&quot;&gt;Configure Monitoring for Auto Scaling Instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;
    :type instance_monitoring: dict | bytes
    :param spot_price: &lt;p&gt;The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot price. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-spot-instances.html\&quot;&gt;Request Spot Instances for fault-tolerant and flexible applications&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Valid Range: Minimum value of 0.001&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you change your maximum price by creating a new launch configuration, running instances will continue to run as long as the maximum price for those running instances is higher than the current Spot price.&lt;/p&gt; &lt;/note&gt;
    :type spot_price: str
    :param iam_instance_profile: The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html\&quot;&gt;IAM role for applications that run on Amazon EC2 instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type iam_instance_profile: str
    :param ebs_optimized: &lt;p&gt;Specifies whether the launch configuration is optimized for EBS I/O (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). The optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization is not available with all instance types. Additional fees are incurred when you enable EBS optimization for an instance type that is not EBS-optimized by default. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html\&quot;&gt;Amazon EBS-optimized instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The default value is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt;
    :type ebs_optimized: bool
    :param associate_public_ip_address: &lt;p&gt;Specifies whether to assign a public IPv4 address to the group&#39;s instances. If the instance is launched into a default subnet, the default is to assign a public IPv4 address, unless you disabled the option to assign a public IPv4 address on the subnet. If the instance is launched into a nondefault subnet, the default is not to assign a public IPv4 address, unless you enabled the option to assign a public IPv4 address on the subnet.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;true&lt;/code&gt;, each instance in the Auto Scaling group receives a unique public IPv4 address. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html\&quot;&gt;Launching Auto Scaling instances in a VPC&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify this property, you must specify at least one subnet for &lt;code&gt;VPCZoneIdentifier&lt;/code&gt; when you create your group.&lt;/p&gt;
    :type associate_public_ip_address: bool
    :param placement_tenancy: &lt;p&gt;The tenancy of the instance, either &lt;code&gt;default&lt;/code&gt; or &lt;code&gt;dedicated&lt;/code&gt;. An instance with &lt;code&gt;dedicated&lt;/code&gt; tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC. To launch dedicated instances into a shared tenancy VPC (a VPC with the instance placement tenancy attribute set to &lt;code&gt;default&lt;/code&gt;), you must set the value of this property to &lt;code&gt;dedicated&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-dedicated-instances.html\&quot;&gt;Configuring instance tenancy with Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;PlacementTenancy&lt;/code&gt;, you must specify at least one subnet for &lt;code&gt;VPCZoneIdentifier&lt;/code&gt; when you create your group.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;default&lt;/code&gt; | &lt;code&gt;dedicated&lt;/code&gt; &lt;/p&gt;
    :type placement_tenancy: str
    :param metadata_options: The metadata options for the instances. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html#launch-configurations-imds\&quot;&gt;Configuring the Instance Metadata Options&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type metadata_options: dict | bytes

    """
    block_device_mappings = [BlockDeviceMapping.from_dict(d) for d in block_device_mappings]
    instance_monitoring = .from_dict(instance_monitoring)
    metadata_options = .from_dict(metadata_options)
    return web.Response(status=200)


async def g_et_create_or_update_tags(request: web.Request, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_or_update_tags

    &lt;p&gt;Creates or updates tags for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html\&quot;&gt;Tag Auto Scaling groups and instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param tags: One or more tags.
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
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_delete_auto_scaling_group(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, force_delete=None) -> web.Response:
    """g_et_delete_auto_scaling_group

    &lt;p&gt;Deletes the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;If the group has instances or scaling activities in progress, you must specify the option to force the deletion in order for it to succeed. The force delete operation will also terminate the EC2 instances. If the group has a warm pool, the force delete option also deletes the warm pool.&lt;/p&gt; &lt;p&gt;To remove instances from the Auto Scaling group before deleting it, call the &lt;a&gt;DetachInstances&lt;/a&gt; API with the list of instances and the option to decrement the desired capacity. This ensures that Amazon EC2 Auto Scaling does not launch replacement instances.&lt;/p&gt; &lt;p&gt;To terminate all instances before deleting the Auto Scaling group, call the &lt;a&gt;UpdateAutoScalingGroup&lt;/a&gt; API and set the minimum size and desired capacity of the Auto Scaling group to zero.&lt;/p&gt; &lt;p&gt;If the group has scaling policies, deleting the group deletes the policies, the underlying alarm actions, and any alarm that no longer has an associated action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html\&quot;&gt;Delete your Auto Scaling infrastructure&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param force_delete: Specifies that the group is to be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This action also deletes any outstanding lifecycle actions associated with the group.
    :type force_delete: bool

    """
    return web.Response(status=200)


async def g_et_delete_launch_configuration(request: web.Request, launch_configuration_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_launch_configuration

    &lt;p&gt;Deletes the specified launch configuration.&lt;/p&gt; &lt;p&gt;The launch configuration must not be attached to an Auto Scaling group. When this call completes, the launch configuration is no longer available for use.&lt;/p&gt;

    :param launch_configuration_name: The name of the launch configuration.
    :type launch_configuration_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_lifecycle_hook(request: web.Request, lifecycle_hook_name, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_lifecycle_hook

    &lt;p&gt;Deletes the specified lifecycle hook.&lt;/p&gt; &lt;p&gt;If there are any outstanding lifecycle actions, they are completed first (&lt;code&gt;ABANDON&lt;/code&gt; for launching instances, &lt;code&gt;CONTINUE&lt;/code&gt; for terminating instances).&lt;/p&gt;

    :param lifecycle_hook_name: The name of the lifecycle hook.
    :type lifecycle_hook_name: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_notification_configuration(request: web.Request, auto_scaling_group_name, topic_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_notification_configuration

    Deletes the specified notification.

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic.
    :type topic_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_delete_policy(request: web.Request, policy_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, auto_scaling_group_name=None) -> web.Response:
    """g_et_delete_policy

    &lt;p&gt;Deletes the specified scaling policy.&lt;/p&gt; &lt;p&gt;Deleting either a step scaling policy or a simple scaling policy deletes the underlying alarm action, but does not delete the alarm, even if it no longer has an associated action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/deleting-scaling-policy.html\&quot;&gt;Deleting a scaling policy&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param policy_name: The name or Amazon Resource Name (ARN) of the policy.
    :type policy_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str

    """
    return web.Response(status=200)


async def g_et_delete_scheduled_action(request: web.Request, auto_scaling_group_name, scheduled_action_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_scheduled_action

    Deletes the specified scheduled action.

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param scheduled_action_name: The name of the action to delete.
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


async def g_et_delete_tags(request: web.Request, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_tags

    Deletes the specified tags.

    :param tags: One or more tags.
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
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_delete_warm_pool(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, force_delete=None) -> web.Response:
    """g_et_delete_warm_pool

    &lt;p&gt;Deletes the warm pool for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html\&quot;&gt;Warm pools for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param force_delete: Specifies that the warm pool is to be deleted along with all of its associated instances, without waiting for all instances to be terminated. This parameter also deletes any outstanding lifecycle actions associated with the warm pool instances.
    :type force_delete: bool

    """
    return web.Response(status=200)


async def g_et_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_account_limits

    &lt;p&gt;Describes the current Amazon EC2 Auto Scaling resource quotas for your account.&lt;/p&gt; &lt;p&gt;When you establish an Amazon Web Services account, the account has initial quotas on the maximum number of Auto Scaling groups and launch configurations that you can create in a given Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html\&quot;&gt;Quotas for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_adjustment_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_adjustment_types

    &lt;p&gt;Describes the available adjustment types for step scaling and simple scaling policies.&lt;/p&gt; &lt;p&gt;The following adjustment types are supported:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ChangeInCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ExactCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PercentChangeInCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_auto_scaling_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, auto_scaling_group_names=None, next_token=None, max_records=None, filters=None) -> web.Response:
    """g_et_describe_auto_scaling_groups

    &lt;p&gt;Gets information about the Auto Scaling groups in the account and Region.&lt;/p&gt; &lt;p&gt;If you specify Auto Scaling group names, the output includes information for only the specified Auto Scaling groups. If you specify filters, the output includes information for only those Auto Scaling groups that meet the filter criteria. If you do not specify group names or filters, the output includes information for all Auto Scaling groups. &lt;/p&gt; &lt;p&gt;This operation also returns information about instances in Auto Scaling groups. To retrieve information about the instances in a warm pool, you must call the &lt;a&gt;DescribeWarmPool&lt;/a&gt; API. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param auto_scaling_group_names: &lt;p&gt;The names of the Auto Scaling groups. By default, you can only specify up to 50 names. You can optionally increase this limit using the &lt;code&gt;MaxRecords&lt;/code&gt; property.&lt;/p&gt; &lt;p&gt;If you omit this property, all Auto Scaling groups are described.&lt;/p&gt;
    :type auto_scaling_group_names: List[str]
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int
    :param filters: One or more filters to limit the results based on specific tags. 
    :type filters: list | bytes

    """
    filters = [Filter.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_auto_scaling_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, instance_ids=None, max_records=None, next_token=None) -> web.Response:
    """g_et_describe_auto_scaling_instances

    Gets information about the Auto Scaling instances in the account and Region.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param instance_ids: &lt;p&gt;The IDs of the instances. If you omit this property, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.&lt;/p&gt; &lt;p&gt;Array Members: Maximum number of 50 items.&lt;/p&gt;
    :type instance_ids: List[str]
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;50&lt;/code&gt;.
    :type max_records: int
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_describe_auto_scaling_notification_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_auto_scaling_notification_types

    Describes the notification types that are supported by Amazon EC2 Auto Scaling.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_instance_refreshes(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, instance_refresh_ids=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_instance_refreshes

    &lt;p&gt;Gets information about the instance refreshes for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.&lt;/p&gt; &lt;p&gt;To help you determine the status of an instance refresh, Amazon EC2 Auto Scaling returns information about the instance refreshes you previously initiated, including their status, start time, end time, the percentage of the instance refresh that is complete, and the number of instances remaining to update before the instance refresh is complete. If a rollback is initiated while an instance refresh is in progress, Amazon EC2 Auto Scaling also returns information about the rollback of the instance refresh.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param instance_refresh_ids: One or more instance refresh IDs.
    :type instance_refresh_ids: List[str]
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_launch_configurations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, launch_configuration_names=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_launch_configurations

    Gets information about the launch configurations in the account and Region.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param launch_configuration_names: &lt;p&gt;The launch configuration names. If you omit this property, all launch configurations are described.&lt;/p&gt; &lt;p&gt;Array Members: Maximum number of 50 items.&lt;/p&gt;
    :type launch_configuration_names: List[str]
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_lifecycle_hook_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_lifecycle_hook_types

    &lt;p&gt;Describes the available types of lifecycle hooks.&lt;/p&gt; &lt;p&gt;The following hook types are supported:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;autoscaling:EC2_INSTANCE_LAUNCHING&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;autoscaling:EC2_INSTANCE_TERMINATING&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_lifecycle_hooks(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, lifecycle_hook_names=None) -> web.Response:
    """g_et_describe_lifecycle_hooks

    Gets information about the lifecycle hooks for the specified Auto Scaling group.

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param lifecycle_hook_names: The names of one or more lifecycle hooks. If you omit this property, all lifecycle hooks are described.
    :type lifecycle_hook_names: List[str]

    """
    return web.Response(status=200)


async def g_et_describe_load_balancer_target_groups(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_load_balancer_target_groups

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DescribeTrafficSources&lt;/a&gt;, which can describe multiple traffic sources types. We recommend using &lt;code&gt;DetachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DescribeLoadBalancerTargetGroups&lt;/code&gt;. You can use both the original &lt;code&gt;DescribeLoadBalancerTargetGroups&lt;/code&gt; API operation and &lt;code&gt;DescribeTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Gets information about the Elastic Load Balancing target groups for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;To determine the attachment status of the target group, use the &lt;code&gt;State&lt;/code&gt; element in the response. When you attach a target group to an Auto Scaling group, the initial &lt;code&gt;State&lt;/code&gt; value is &lt;code&gt;Adding&lt;/code&gt;. The state transitions to &lt;code&gt;Added&lt;/code&gt; after all Auto Scaling instances are registered with the target group. If Elastic Load Balancing health checks are enabled for the Auto Scaling group, the state transitions to &lt;code&gt;InService&lt;/code&gt; after at least one Auto Scaling instance passes the health check. When the target group is in the &lt;code&gt;InService&lt;/code&gt; state, Amazon EC2 Auto Scaling can terminate and replace any instances that are reported as unhealthy. If no registered instances pass the health checks, the target group doesn&#39;t enter the &lt;code&gt;InService&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt;Target groups also have an &lt;code&gt;InService&lt;/code&gt; state if you attach them in the &lt;a&gt;CreateAutoScalingGroup&lt;/a&gt; API call. If your target group state is &lt;code&gt;InService&lt;/code&gt;, but it is not working properly, check the scaling activities by calling &lt;a&gt;DescribeScalingActivities&lt;/a&gt; and take any corrective actions necessary.&lt;/p&gt; &lt;p&gt;For help with failed health checks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html\&quot;&gt;Troubleshooting Amazon EC2 Auto Scaling: Health checks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can use this operation to describe target groups that were attached by using &lt;a&gt;AttachLoadBalancerTargetGroups&lt;/a&gt;, but not for target groups that were attached by using &lt;a&gt;AttachTrafficSources&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;100&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_load_balancers(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_load_balancers

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DescribeTrafficSources&lt;/a&gt;, which can describe multiple traffic sources types. We recommend using &lt;code&gt;DescribeTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DescribeLoadBalancers&lt;/code&gt;. You can use both the original &lt;code&gt;DescribeLoadBalancers&lt;/code&gt; API operation and &lt;code&gt;DescribeTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Gets information about the load balancers for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation describes only Classic Load Balancers. If you have Application Load Balancers, Network Load Balancers, or Gateway Load Balancers, use the &lt;a&gt;DescribeLoadBalancerTargetGroups&lt;/a&gt; API instead.&lt;/p&gt; &lt;p&gt;To determine the attachment status of the load balancer, use the &lt;code&gt;State&lt;/code&gt; element in the response. When you attach a load balancer to an Auto Scaling group, the initial &lt;code&gt;State&lt;/code&gt; value is &lt;code&gt;Adding&lt;/code&gt;. The state transitions to &lt;code&gt;Added&lt;/code&gt; after all Auto Scaling instances are registered with the load balancer. If Elastic Load Balancing health checks are enabled for the Auto Scaling group, the state transitions to &lt;code&gt;InService&lt;/code&gt; after at least one Auto Scaling instance passes the health check. When the load balancer is in the &lt;code&gt;InService&lt;/code&gt; state, Amazon EC2 Auto Scaling can terminate and replace any instances that are reported as unhealthy. If no registered instances pass the health checks, the load balancer doesn&#39;t enter the &lt;code&gt;InService&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt;Load balancers also have an &lt;code&gt;InService&lt;/code&gt; state if you attach them in the &lt;a&gt;CreateAutoScalingGroup&lt;/a&gt; API call. If your load balancer state is &lt;code&gt;InService&lt;/code&gt;, but it is not working properly, check the scaling activities by calling &lt;a&gt;DescribeScalingActivities&lt;/a&gt; and take any corrective actions necessary.&lt;/p&gt; &lt;p&gt;For help with failed health checks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html\&quot;&gt;Troubleshooting Amazon EC2 Auto Scaling: Health checks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;100&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_metric_collection_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_metric_collection_types

    Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_notification_configurations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, auto_scaling_group_names=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_notification_configurations

    Gets information about the Amazon SNS notifications that are configured for one or more Auto Scaling groups.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param auto_scaling_group_names: The name of the Auto Scaling group.
    :type auto_scaling_group_names: List[str]
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, auto_scaling_group_name=None, policy_names=None, policy_types=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_policies

    Gets information about the scaling policies in the account and Region.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param policy_names: &lt;p&gt;The names of one or more policies. If you omit this property, all policies are described. If a group name is provided, the results are limited to that group. If you specify an unknown policy name, it is ignored with no error.&lt;/p&gt; &lt;p&gt;Array Members: Maximum number of 50 items.&lt;/p&gt;
    :type policy_names: List[str]
    :param policy_types: One or more policy types. The valid values are &lt;code&gt;SimpleScaling&lt;/code&gt;, &lt;code&gt;StepScaling&lt;/code&gt;, &lt;code&gt;TargetTrackingScaling&lt;/code&gt;, and &lt;code&gt;PredictiveScaling&lt;/code&gt;.
    :type policy_types: List[str]
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to be returned with each call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_scaling_activities(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, activity_ids=None, auto_scaling_group_name=None, include_deleted_groups=None, max_records=None, next_token=None) -> web.Response:
    """g_et_describe_scaling_activities

    &lt;p&gt;Gets information about the scaling activities in the account and Region.&lt;/p&gt; &lt;p&gt;When scaling events occur, you see a record of the scaling activity in the scaling activities. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html\&quot;&gt;Verifying a scaling activity for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If the scaling event succeeds, the value of the &lt;code&gt;StatusCode&lt;/code&gt; element in the response is &lt;code&gt;Successful&lt;/code&gt;. If an attempt to launch instances failed, the &lt;code&gt;StatusCode&lt;/code&gt; value is &lt;code&gt;Failed&lt;/code&gt; or &lt;code&gt;Cancelled&lt;/code&gt; and the &lt;code&gt;StatusMessage&lt;/code&gt; element in the response indicates the cause of the failure. For help interpreting the &lt;code&gt;StatusMessage&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html\&quot;&gt;Troubleshooting Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param activity_ids: &lt;p&gt;The activity IDs of the desired scaling activities. If you omit this property, all activities for the past six weeks are described. If unknown activities are requested, they are ignored with no error. If you specify an Auto Scaling group, the results are limited to that group.&lt;/p&gt; &lt;p&gt;Array Members: Maximum number of 50 IDs.&lt;/p&gt;
    :type activity_ids: List[str]
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param include_deleted_groups: Indicates whether to include scaling activity from deleted Auto Scaling groups.
    :type include_deleted_groups: bool
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;100&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_describe_scaling_process_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_scaling_process_types

    Describes the scaling process types for use with the &lt;a&gt;ResumeProcesses&lt;/a&gt; and &lt;a&gt;SuspendProcesses&lt;/a&gt; APIs.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_scheduled_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, auto_scaling_group_name=None, scheduled_action_names=None, start_time=None, end_time=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_scheduled_actions

    &lt;p&gt;Gets information about the scheduled actions that haven&#39;t run or that have not reached their end time.&lt;/p&gt; &lt;p&gt;To describe the scaling activities for scheduled actions that have already run, call the &lt;a&gt;DescribeScalingActivities&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param scheduled_action_names: &lt;p&gt;The names of one or more scheduled actions. If you omit this property, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.&lt;/p&gt; &lt;p&gt;Array Members: Maximum number of 50 actions.&lt;/p&gt;
    :type scheduled_action_names: List[str]
    :param start_time: The earliest scheduled start time to return. If scheduled action names are provided, this property is ignored.
    :type start_time: str
    :param end_time: The latest scheduled start time to return. If scheduled action names are provided, this property is ignored.
    :type end_time: str
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_describe_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_tags

    &lt;p&gt;Describes the specified tags.&lt;/p&gt; &lt;p&gt;You can use filters to limit the results. For example, you can query for the tags for a specific Auto Scaling group. You can specify multiple values for a filter. A tag must match at least one of the specified values for it to be included in the results.&lt;/p&gt; &lt;p&gt;You can also specify multiple filters. The result includes information for a particular tag only if it matches all the filters. If there&#39;s no match, no special message is returned.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html\&quot;&gt;Tag Auto Scaling groups and instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param filters: One or more filters to scope the tags to return. The maximum number of filters per filter type (for example, &lt;code&gt;auto-scaling-group&lt;/code&gt;) is 1000.
    :type filters: list | bytes
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The default value is &lt;code&gt;50&lt;/code&gt; and the maximum value is &lt;code&gt;100&lt;/code&gt;.
    :type max_records: int

    """
    filters = [Filter.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_describe_termination_policy_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_termination_policy_types

    &lt;p&gt;Describes the termination policies supported by Amazon EC2 Auto Scaling.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html\&quot;&gt;Work with Amazon EC2 Auto Scaling termination policies&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_describe_traffic_sources(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, traffic_source_type=None, next_token=None, max_records=None) -> web.Response:
    """g_et_describe_traffic_sources

    &lt;p&gt;Gets information about the traffic sources for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;You can optionally provide a traffic source type. If you provide a traffic source type, then the results only include that traffic source type.&lt;/p&gt; &lt;p&gt;If you do not provide a traffic source type, then the results include all the traffic sources for the specified Auto Scaling group. &lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param traffic_source_type: &lt;p&gt;The traffic source type that you want to describe.&lt;/p&gt; &lt;p&gt;The following lists the valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;elb&lt;/code&gt; if the traffic source is a Classic Load Balancer.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;elbv2&lt;/code&gt; if the traffic source is a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;vpc-lattice&lt;/code&gt; if the traffic source is VPC Lattice.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type traffic_source_type: str
    :param next_token: The token for the next set of items to return. (You received this token from a previous call.)
    :type next_token: str
    :param max_records: The maximum number of items to return with this call. The maximum value is &lt;code&gt;50&lt;/code&gt;.
    :type max_records: int

    """
    return web.Response(status=200)


async def g_et_describe_warm_pool(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None) -> web.Response:
    """g_et_describe_warm_pool

    &lt;p&gt;Gets information about a warm pool and its instances.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html\&quot;&gt;Warm pools for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_records: The maximum number of instances to return with this call. The maximum value is &lt;code&gt;50&lt;/code&gt;.
    :type max_records: int
    :param next_token: The token for the next set of instances to return. (You received this token from a previous call.)
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_detach_instances(request: web.Request, auto_scaling_group_name, should_decrement_desired_capacity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, instance_ids=None) -> web.Response:
    """g_et_detach_instances

    &lt;p&gt;Removes one or more instances from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;After the instances are detached, you can manage them independent of the Auto Scaling group.&lt;/p&gt; &lt;p&gt;If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are detached.&lt;/p&gt; &lt;p&gt;If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/detach-instance-asg.html\&quot;&gt;Detach EC2 instances from your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param should_decrement_desired_capacity: Indicates whether the Auto Scaling group decrements the desired capacity value by the number of instances detached.
    :type should_decrement_desired_capacity: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param instance_ids: The IDs of the instances. You can specify up to 20 instances.
    :type instance_ids: List[str]

    """
    return web.Response(status=200)


async def g_et_detach_load_balancer_target_groups(request: web.Request, auto_scaling_group_name, target_group_arns, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_detach_load_balancer_target_groups

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DetachTrafficSources&lt;/a&gt;, which can detach multiple traffic sources types. We recommend using &lt;code&gt;DetachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DetachLoadBalancerTargetGroups&lt;/code&gt;. You can use both the original &lt;code&gt;DetachLoadBalancerTargetGroups&lt;/code&gt; API operation and &lt;code&gt;DetachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Detaches one or more target groups from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you detach a target group, it enters the &lt;code&gt;Removing&lt;/code&gt; state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the target group using the &lt;a&gt;DescribeLoadBalancerTargetGroups&lt;/a&gt; API call. The instances remain running.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can use this operation to detach target groups that were attached by using &lt;a&gt;AttachLoadBalancerTargetGroups&lt;/a&gt;, but not for target groups that were attached by using &lt;a&gt;AttachTrafficSources&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param target_group_arns: The Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.
    :type target_group_arns: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_detach_load_balancers(request: web.Request, auto_scaling_group_name, load_balancer_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_detach_load_balancers

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DetachTrafficSources&lt;/a&gt;, which can detach multiple traffic sources types. We recommend using &lt;code&gt;DetachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DetachLoadBalancers&lt;/code&gt;. You can use both the original &lt;code&gt;DetachLoadBalancers&lt;/code&gt; API operation and &lt;code&gt;DetachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Detaches one or more Classic Load Balancers from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation detaches only Classic Load Balancers. If you have Application Load Balancers, Network Load Balancers, or Gateway Load Balancers, use the &lt;a&gt;DetachLoadBalancerTargetGroups&lt;/a&gt; API instead.&lt;/p&gt; &lt;p&gt;When you detach a load balancer, it enters the &lt;code&gt;Removing&lt;/code&gt; state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using the &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; API call. The instances remain running.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param load_balancer_names: The names of the load balancers. You can specify up to 10 load balancers.
    :type load_balancer_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_detach_traffic_sources(request: web.Request, auto_scaling_group_name, traffic_sources, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_detach_traffic_sources

    &lt;p&gt;Detaches one or more traffic sources from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you detach a traffic source, it enters the &lt;code&gt;Removing&lt;/code&gt; state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the traffic source using the &lt;a&gt;DescribeTrafficSources&lt;/a&gt; API call. The instances continue to run.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param traffic_sources: The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.
    :type traffic_sources: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    traffic_sources = [TrafficSourceIdentifier.from_dict(d) for d in traffic_sources]
    return web.Response(status=200)


async def g_et_disable_metrics_collection(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, metrics=None) -> web.Response:
    """g_et_disable_metrics_collection

    Disables group metrics collection for the specified Auto Scaling group.

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param metrics: &lt;p&gt;Identifies the metrics to disable.&lt;/p&gt; &lt;p&gt;You can specify one or more of the following metrics:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupMinSize&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupMaxSize&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupDesiredCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupInServiceInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupPendingInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupStandbyInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTerminatingInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTotalInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupInServiceCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupPendingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupStandbyCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTerminatingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTotalCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolDesiredCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolWarmedCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolPendingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolTerminatingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolTotalCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupAndWarmPoolDesiredCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupAndWarmPoolTotalCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you omit this property, all metrics are disabled.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html#as-group-metrics\&quot;&gt;Auto Scaling group metrics&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;
    :type metrics: List[str]

    """
    return web.Response(status=200)


async def g_et_enable_metrics_collection(request: web.Request, auto_scaling_group_name, granularity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, metrics=None) -> web.Response:
    """g_et_enable_metrics_collection

    &lt;p&gt;Enables group metrics collection for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;You can use these metrics to track changes in an Auto Scaling group and to set alarms on threshold values. You can view group metrics using the Amazon EC2 Auto Scaling console or the CloudWatch console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html\&quot;&gt;Monitor CloudWatch metrics for your Auto Scaling groups and instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param granularity: The frequency at which Amazon EC2 Auto Scaling sends aggregated data to CloudWatch. The only valid value is &lt;code&gt;1Minute&lt;/code&gt;.
    :type granularity: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param metrics: &lt;p&gt;Identifies the metrics to enable.&lt;/p&gt; &lt;p&gt;You can specify one or more of the following metrics:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupMinSize&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupMaxSize&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupDesiredCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupInServiceInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupPendingInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupStandbyInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTerminatingInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTotalInstances&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupInServiceCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupPendingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupStandbyCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTerminatingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupTotalCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolDesiredCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolWarmedCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolPendingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolTerminatingCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WarmPoolTotalCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupAndWarmPoolDesiredCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GroupAndWarmPoolTotalCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify &lt;code&gt;Granularity&lt;/code&gt; and don&#39;t specify any metrics, all metrics are enabled.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html#as-group-metrics\&quot;&gt;Auto Scaling group metrics&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;
    :type metrics: List[str]

    """
    return web.Response(status=200)


async def g_et_enter_standby(request: web.Request, auto_scaling_group_name, should_decrement_desired_capacity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, instance_ids=None) -> web.Response:
    """g_et_enter_standby

    &lt;p&gt;Moves the specified instances into the standby state.&lt;/p&gt; &lt;p&gt;If you choose to decrement the desired capacity of the Auto Scaling group, the instances can enter standby as long as the desired capacity of the Auto Scaling group after the instances are placed into standby is equal to or greater than the minimum capacity of the group.&lt;/p&gt; &lt;p&gt;If you choose not to decrement the desired capacity of the Auto Scaling group, the Auto Scaling group launches new instances to replace the instances on standby.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html\&quot;&gt;Temporarily removing instances from your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param should_decrement_desired_capacity: Indicates whether to decrement the desired capacity of the Auto Scaling group by the number of instances moved to &lt;code&gt;Standby&lt;/code&gt; mode.
    :type should_decrement_desired_capacity: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param instance_ids: The IDs of the instances. You can specify up to 20 instances.
    :type instance_ids: List[str]

    """
    return web.Response(status=200)


async def g_et_execute_policy(request: web.Request, policy_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, auto_scaling_group_name=None, honor_cooldown=None, metric_value=None, breach_threshold=None) -> web.Response:
    """g_et_execute_policy

    Executes the specified policy. This can be useful for testing the design of your scaling policy.

    :param policy_name: The name or ARN of the policy.
    :type policy_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param honor_cooldown: &lt;p&gt;Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before executing the policy.&lt;/p&gt; &lt;p&gt;Valid only if the policy type is &lt;code&gt;SimpleScaling&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html\&quot;&gt;Scaling cooldowns for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;
    :type honor_cooldown: bool
    :param metric_value: &lt;p&gt;The metric value to compare to &lt;code&gt;BreachThreshold&lt;/code&gt;. This enables you to execute a policy of type &lt;code&gt;StepScaling&lt;/code&gt; and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.&lt;/p&gt; &lt;p&gt;If you specify a metric value that doesn&#39;t correspond to a step adjustment for the policy, the call returns an error.&lt;/p&gt; &lt;p&gt;Required if the policy type is &lt;code&gt;StepScaling&lt;/code&gt; and not supported otherwise.&lt;/p&gt;
    :type metric_value: float
    :param breach_threshold: &lt;p&gt;The breach threshold for the alarm.&lt;/p&gt; &lt;p&gt;Required if the policy type is &lt;code&gt;StepScaling&lt;/code&gt; and not supported otherwise.&lt;/p&gt;
    :type breach_threshold: float

    """
    return web.Response(status=200)


async def g_et_exit_standby(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, instance_ids=None) -> web.Response:
    """g_et_exit_standby

    &lt;p&gt;Moves the specified instances out of the standby state.&lt;/p&gt; &lt;p&gt;After you put the instances back in service, the desired capacity is incremented.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html\&quot;&gt;Temporarily removing instances from your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param instance_ids: The IDs of the instances. You can specify up to 20 instances.
    :type instance_ids: List[str]

    """
    return web.Response(status=200)


async def g_et_get_predictive_scaling_forecast(request: web.Request, auto_scaling_group_name, policy_name, start_time, end_time, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_predictive_scaling_forecast

    &lt;p&gt;Retrieves the forecast data for a predictive scaling policy.&lt;/p&gt; &lt;p&gt;Load forecasts are predictions of the hourly load values using historical load data from CloudWatch and an analysis of historical trends. Capacity forecasts are represented as predicted values for the minimum capacity that is needed on an hourly basis, based on the hourly load forecast.&lt;/p&gt; &lt;p&gt;A minimum of 24 hours of data is required to create the initial forecasts. However, having a full 14 days of historical data results in more accurate forecasts.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html\&quot;&gt;Predictive scaling for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param policy_name: The name of the policy.
    :type policy_name: str
    :param start_time: The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time.
    :type start_time: str
    :param end_time: &lt;p&gt;The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days. &lt;/p&gt; &lt;p&gt;Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. Amazon EC2 Auto Scaling only issues forecasts for periods of two days in advance.&lt;/p&gt;
    :type end_time: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_put_lifecycle_hook(request: web.Request, lifecycle_hook_name, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, lifecycle_transition=None, role_arn=None, notification_target_arn=None, notification_metadata=None, heartbeat_timeout=None, default_result=None) -> web.Response:
    """g_et_put_lifecycle_hook

    &lt;p&gt;Creates or updates a lifecycle hook for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;Lifecycle hooks let you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.&lt;/p&gt; &lt;p&gt;This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.&lt;/b&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state using the &lt;a&gt;RecordLifecycleActionHeartbeat&lt;/a&gt; API call.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you finish before the timeout period ends, send a callback by using the &lt;a&gt;CompleteLifecycleAction&lt;/a&gt; API call.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html\&quot;&gt;Amazon EC2 Auto Scaling lifecycle hooks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails.&lt;/p&gt; &lt;p&gt;You can view the lifecycle hooks for an Auto Scaling group using the &lt;a&gt;DescribeLifecycleHooks&lt;/a&gt; API call. If you are no longer using a lifecycle hook, you can delete it by calling the &lt;a&gt;DeleteLifecycleHook&lt;/a&gt; API.&lt;/p&gt;

    :param lifecycle_hook_name: The name of the lifecycle hook.
    :type lifecycle_hook_name: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param lifecycle_transition: &lt;p&gt;The lifecycle transition. For Auto Scaling groups, there are two major lifecycle transitions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To create a lifecycle hook for scale-out events, specify &lt;code&gt;autoscaling:EC2_INSTANCE_LAUNCHING&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To create a lifecycle hook for scale-in events, specify &lt;code&gt;autoscaling:EC2_INSTANCE_TERMINATING&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Required for new lifecycle hooks, but optional when updating existing hooks.&lt;/p&gt;
    :type lifecycle_transition: str
    :param role_arn: &lt;p&gt;The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.&lt;/p&gt; &lt;p&gt;Valid only if the notification target is an Amazon SNS topic or an Amazon SQS queue. Required for new lifecycle hooks, but optional when updating existing hooks.&lt;/p&gt;
    :type role_arn: str
    :param notification_target_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in a wait state for the lifecycle hook. You can specify either an Amazon SNS topic or an Amazon SQS queue.&lt;/p&gt; &lt;p&gt;If you specify an empty string, this overrides the current ARN.&lt;/p&gt; &lt;p&gt;This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key-value pair format when sending notifications to an Amazon SNS topic.&lt;/p&gt; &lt;p&gt;When you specify a notification target, Amazon EC2 Auto Scaling sends it a test message. Test messages contain the following additional key-value pair: &lt;code&gt;\&quot;Event\&quot;: \&quot;autoscaling:TEST_NOTIFICATION\&quot;&lt;/code&gt;.&lt;/p&gt;
    :type notification_target_arn: str
    :param notification_metadata: Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.
    :type notification_metadata: str
    :param heartbeat_timeout: The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from &lt;code&gt;30&lt;/code&gt; to &lt;code&gt;7200&lt;/code&gt; seconds. The default value is &lt;code&gt;3600&lt;/code&gt; seconds (1 hour).
    :type heartbeat_timeout: int
    :param default_result: &lt;p&gt;The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The default value is &lt;code&gt;ABANDON&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;CONTINUE&lt;/code&gt; | &lt;code&gt;ABANDON&lt;/code&gt; &lt;/p&gt;
    :type default_result: str

    """
    return web.Response(status=200)


async def g_et_put_notification_configuration(request: web.Request, auto_scaling_group_name, topic_arn, notification_types, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_put_notification_configuration

    &lt;p&gt;Configures an Auto Scaling group to send notifications when specified events take place. Subscribers to the specified topic can have messages delivered to an endpoint such as a web server or an email address.&lt;/p&gt; &lt;p&gt;This configuration overwrites any existing configuration.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html\&quot;&gt;Getting Amazon SNS notifications when your Auto Scaling group scales&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of SNS topics, which is 10 per Auto Scaling group, the call fails.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic.
    :type topic_arn: str
    :param notification_types: The type of event that causes the notification to be sent. To query the notification types supported by Amazon EC2 Auto Scaling, call the &lt;a&gt;DescribeAutoScalingNotificationTypes&lt;/a&gt; API.
    :type notification_types: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_put_scaling_policy(request: web.Request, auto_scaling_group_name, policy_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, policy_type=None, adjustment_type=None, min_adjustment_step=None, min_adjustment_magnitude=None, scaling_adjustment=None, cooldown=None, metric_aggregation_type=None, step_adjustments=None, estimated_instance_warmup=None, target_tracking_configuration=None, enabled=None, predictive_scaling_configuration=None) -> web.Response:
    """g_et_put_scaling_policy

    &lt;p&gt;Creates or updates a scaling policy for an Auto Scaling group. Scaling policies are used to scale an Auto Scaling group based on configurable metrics. If no policies are defined, the dynamic scaling and predictive scaling features are not used. &lt;/p&gt; &lt;p&gt;For more information about using dynamic scaling, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html\&quot;&gt;Target tracking scaling policies&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html\&quot;&gt;Step and simple scaling policies&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information about using predictive scaling, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html\&quot;&gt;Predictive scaling for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can view the scaling policies for an Auto Scaling group using the &lt;a&gt;DescribePolicies&lt;/a&gt; API call. If you are no longer using a scaling policy, you can delete it by calling the &lt;a&gt;DeletePolicy&lt;/a&gt; API.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param policy_name: The name of the policy.
    :type policy_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param policy_type: &lt;p&gt;One of the following policy types: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TargetTrackingScaling&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;StepScaling&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SimpleScaling&lt;/code&gt; (default)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PredictiveScaling&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type policy_type: str
    :param adjustment_type: &lt;p&gt;Specifies how the scaling adjustment is interpreted (for example, an absolute number or a percentage). The valid values are &lt;code&gt;ChangeInCapacity&lt;/code&gt;, &lt;code&gt;ExactCapacity&lt;/code&gt;, and &lt;code&gt;PercentChangeInCapacity&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Required if the policy type is &lt;code&gt;StepScaling&lt;/code&gt; or &lt;code&gt;SimpleScaling&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment\&quot;&gt;Scaling adjustment types&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;
    :type adjustment_type: str
    :param min_adjustment_step: Available for backward compatibility. Use &lt;code&gt;MinAdjustmentMagnitude&lt;/code&gt; instead.
    :type min_adjustment_step: int
    :param min_adjustment_magnitude: &lt;p&gt;The minimum value to scale by when the adjustment type is &lt;code&gt;PercentChangeInCapacity&lt;/code&gt;. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a &lt;code&gt;MinAdjustmentMagnitude&lt;/code&gt; of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a &lt;code&gt;MinAdjustmentMagnitude&lt;/code&gt; of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.&lt;/p&gt; &lt;p&gt;Valid only if the policy type is &lt;code&gt;StepScaling&lt;/code&gt; or &lt;code&gt;SimpleScaling&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment\&quot;&gt;Scaling adjustment types&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Some Auto Scaling groups use instance weights. In this case, set the &lt;code&gt;MinAdjustmentMagnitude&lt;/code&gt; to a value that is at least as large as your largest instance weight.&lt;/p&gt; &lt;/note&gt;
    :type min_adjustment_magnitude: int
    :param scaling_adjustment: &lt;p&gt;The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a non-negative value.&lt;/p&gt; &lt;p&gt;Required if the policy type is &lt;code&gt;SimpleScaling&lt;/code&gt;. (Not used with any other policy type.) &lt;/p&gt;
    :type scaling_adjustment: int
    :param cooldown: &lt;p&gt;A cooldown period, in seconds, that applies to a specific simple scaling policy. When a cooldown period is specified here, it overrides the default cooldown.&lt;/p&gt; &lt;p&gt;Valid only if the policy type is &lt;code&gt;SimpleScaling&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html\&quot;&gt;Scaling cooldowns for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Default: None&lt;/p&gt;
    :type cooldown: int
    :param metric_aggregation_type: &lt;p&gt;The aggregation type for the CloudWatch metrics. The valid values are &lt;code&gt;Minimum&lt;/code&gt;, &lt;code&gt;Maximum&lt;/code&gt;, and &lt;code&gt;Average&lt;/code&gt;. If the aggregation type is null, the value is treated as &lt;code&gt;Average&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Valid only if the policy type is &lt;code&gt;StepScaling&lt;/code&gt;.&lt;/p&gt;
    :type metric_aggregation_type: str
    :param step_adjustments: &lt;p&gt;A set of adjustments that enable you to scale based on the size of the alarm breach.&lt;/p&gt; &lt;p&gt;Required if the policy type is &lt;code&gt;StepScaling&lt;/code&gt;. (Not used with any other policy type.) &lt;/p&gt;
    :type step_adjustments: list | bytes
    :param estimated_instance_warmup: &lt;p&gt; &lt;i&gt;Not needed if the default instance warmup is defined for the group.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This warm-up period applies to instances launched due to a specific target tracking or step scaling policy. When a warm-up period is specified here, it overrides the default instance warmup.&lt;/p&gt; &lt;p&gt;Valid only if the policy type is &lt;code&gt;TargetTrackingScaling&lt;/code&gt; or &lt;code&gt;StepScaling&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The default is to use the value for the default instance warmup defined for the group. If default instance warmup is null, then &lt;code&gt;EstimatedInstanceWarmup&lt;/code&gt; falls back to the value of default cooldown.&lt;/p&gt; &lt;/note&gt;
    :type estimated_instance_warmup: int
    :param target_tracking_configuration: &lt;p&gt;A target tracking scaling policy. Provides support for predefined or custom metrics.&lt;/p&gt; &lt;p&gt;The following predefined metrics are available:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ASGAverageCPUUtilization&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ASGAverageNetworkIn&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ASGAverageNetworkOut&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALBRequestCountPerTarget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify &lt;code&gt;ALBRequestCountPerTarget&lt;/code&gt; for the metric, you must specify the &lt;code&gt;ResourceLabel&lt;/code&gt; property with the &lt;code&gt;PredefinedMetricSpecification&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingConfiguration.html\&quot;&gt;TargetTrackingConfiguration&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Required if the policy type is &lt;code&gt;TargetTrackingScaling&lt;/code&gt;.&lt;/p&gt;
    :type target_tracking_configuration: dict | bytes
    :param enabled: Indicates whether the scaling policy is enabled or disabled. The default is enabled. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enable-disable-scaling-policy.html\&quot;&gt;Disabling a scaling policy for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type enabled: bool
    :param predictive_scaling_configuration: &lt;p&gt;A predictive scaling policy. Provides support for predefined and custom metrics.&lt;/p&gt; &lt;p&gt;Predefined metrics include CPU utilization, network in/out, and the Application Load Balancer request count.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PredictiveScalingConfiguration.html\&quot;&gt;PredictiveScalingConfiguration&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Required if the policy type is &lt;code&gt;PredictiveScaling&lt;/code&gt;.&lt;/p&gt;
    :type predictive_scaling_configuration: dict | bytes

    """
    step_adjustments = [StepAdjustment.from_dict(d) for d in step_adjustments]
    target_tracking_configuration = .from_dict(target_tracking_configuration)
    predictive_scaling_configuration = .from_dict(predictive_scaling_configuration)
    return web.Response(status=200)


async def g_et_put_scheduled_update_group_action(request: web.Request, auto_scaling_group_name, scheduled_action_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, time=None, start_time=None, end_time=None, recurrence=None, min_size=None, max_size=None, desired_capacity=None, time_zone=None) -> web.Response:
    """g_et_put_scheduled_update_group_action

    &lt;p&gt;Creates or updates a scheduled scaling action for an Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html\&quot;&gt;Scheduled scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can view the scheduled actions for an Auto Scaling group using the &lt;a&gt;DescribeScheduledActions&lt;/a&gt; API call. If you are no longer using a scheduled action, you can delete it by calling the &lt;a&gt;DeleteScheduledAction&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;If you try to schedule your action in the past, Amazon EC2 Auto Scaling returns an error message.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param scheduled_action_name: The name of this scaling action.
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
    :param time: This property is no longer used.
    :type time: str
    :param start_time: &lt;p&gt;The date and time for this action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, &lt;code&gt;\&quot;2021-06-01T00:00:00Z\&quot;&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;Recurrence&lt;/code&gt; and &lt;code&gt;StartTime&lt;/code&gt;, Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.&lt;/p&gt;
    :type start_time: str
    :param end_time: The date and time for the recurring schedule to end, in UTC. For example, &lt;code&gt;\&quot;2021-06-01T00:00:00Z\&quot;&lt;/code&gt;.
    :type end_time: str
    :param recurrence: &lt;p&gt;The recurring schedule for this action. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, &lt;code&gt;\&quot;30 0 1 1,6,12 *\&quot;&lt;/code&gt;). For more information about this format, see &lt;a href&#x3D;\&quot;http://crontab.org\&quot;&gt;Crontab&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When &lt;code&gt;StartTime&lt;/code&gt; and &lt;code&gt;EndTime&lt;/code&gt; are specified with &lt;code&gt;Recurrence&lt;/code&gt;, they form the boundaries of when the recurring action starts and stops.&lt;/p&gt; &lt;p&gt;Cron expressions use Universal Coordinated Time (UTC) by default.&lt;/p&gt;
    :type recurrence: str
    :param min_size: The minimum size of the Auto Scaling group.
    :type min_size: int
    :param max_size: The maximum size of the Auto Scaling group.
    :type max_size: int
    :param desired_capacity: &lt;p&gt;The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain. It can scale beyond this capacity if you add more scaling conditions. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You must specify at least one of the following properties: &lt;code&gt;MaxSize&lt;/code&gt;, &lt;code&gt;MinSize&lt;/code&gt;, or &lt;code&gt;DesiredCapacity&lt;/code&gt;. &lt;/p&gt; &lt;/note&gt;
    :type desired_capacity: int
    :param time_zone: &lt;p&gt;Specifies the time zone for a cron expression. If a time zone is not provided, UTC is used by default. &lt;/p&gt; &lt;p&gt;Valid values are the canonical names of the IANA time zones, derived from the IANA Time Zone Database (such as &lt;code&gt;Etc/GMT+9&lt;/code&gt; or &lt;code&gt;Pacific/Tahiti&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones&lt;/a&gt;.&lt;/p&gt;
    :type time_zone: str

    """
    time = util.deserialize_datetime(time)
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_put_warm_pool(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_group_prepared_capacity=None, min_size=None, pool_state=None, instance_reuse_policy=None) -> web.Response:
    """g_et_put_warm_pool

    &lt;p&gt;Creates or updates a warm pool for the specified Auto Scaling group. A warm pool is a pool of pre-initialized EC2 instances that sits alongside the Auto Scaling group. Whenever your application needs to scale out, the Auto Scaling group can draw on the warm pool to meet its new desired capacity. For more information and example configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html\&quot;&gt;Warm pools for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation must be called from the Region in which the Auto Scaling group was created. This operation cannot be called on an Auto Scaling group that has a mixed instances policy or a launch template or launch configuration that requests Spot Instances.&lt;/p&gt; &lt;p&gt;You can view the instances in the warm pool using the &lt;a&gt;DescribeWarmPool&lt;/a&gt; API call. If you are no longer using a warm pool, you can delete it by calling the &lt;a&gt;DeleteWarmPool&lt;/a&gt; API.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_group_prepared_capacity: &lt;p&gt;Specifies the maximum number of instances that are allowed to be in the warm pool or in any state except &lt;code&gt;Terminated&lt;/code&gt; for the Auto Scaling group. This is an optional property. Specify it only if you do not want the warm pool size to be determined by the difference between the group&#39;s maximum capacity and its desired capacity. &lt;/p&gt; &lt;important&gt; &lt;p&gt;If a value for &lt;code&gt;MaxGroupPreparedCapacity&lt;/code&gt; is not specified, Amazon EC2 Auto Scaling launches and maintains the difference between the group&#39;s maximum capacity and its desired capacity. If you specify a value for &lt;code&gt;MaxGroupPreparedCapacity&lt;/code&gt;, Amazon EC2 Auto Scaling uses the difference between the &lt;code&gt;MaxGroupPreparedCapacity&lt;/code&gt; and the desired capacity instead. &lt;/p&gt; &lt;p&gt;The size of the warm pool is dynamic. Only when &lt;code&gt;MaxGroupPreparedCapacity&lt;/code&gt; and &lt;code&gt;MinSize&lt;/code&gt; are set to the same value does the warm pool have an absolute size.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If the desired capacity of the Auto Scaling group is higher than the &lt;code&gt;MaxGroupPreparedCapacity&lt;/code&gt;, the capacity of the warm pool is 0, unless you specify a value for &lt;code&gt;MinSize&lt;/code&gt;. To remove a value that you previously set, include the property but specify -1 for the value. &lt;/p&gt;
    :type max_group_prepared_capacity: int
    :param min_size: Specifies the minimum number of instances to maintain in the warm pool. This helps you to ensure that there is always a certain number of warmed instances available to handle traffic spikes. Defaults to 0 if not specified.
    :type min_size: int
    :param pool_state: Sets the instance state to transition to after the lifecycle actions are complete. Default is &lt;code&gt;Stopped&lt;/code&gt;.
    :type pool_state: str
    :param instance_reuse_policy: Indicates whether instances in the Auto Scaling group can be returned to the warm pool on scale in. The default is to terminate instances in the Auto Scaling group when the group scales in.
    :type instance_reuse_policy: dict | bytes

    """
    instance_reuse_policy = .from_dict(instance_reuse_policy)
    return web.Response(status=200)


async def g_et_record_lifecycle_action_heartbeat(request: web.Request, lifecycle_hook_name, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, lifecycle_action_token=None, instance_id=None) -> web.Response:
    """g_et_record_lifecycle_action_heartbeat

    &lt;p&gt;Records a heartbeat for the lifecycle action associated with the specified token or instance. This extends the timeout by the length of time defined using the &lt;a&gt;PutLifecycleHook&lt;/a&gt; API call.&lt;/p&gt; &lt;p&gt;This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state.&lt;/b&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you finish before the timeout period ends, send a callback by using the &lt;a&gt;CompleteLifecycleAction&lt;/a&gt; API call.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html\&quot;&gt;Amazon EC2 Auto Scaling lifecycle hooks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param lifecycle_hook_name: The name of the lifecycle hook.
    :type lifecycle_hook_name: str
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param lifecycle_action_token: A token that uniquely identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target that you specified when you created the lifecycle hook.
    :type lifecycle_action_token: str
    :param instance_id: The ID of the instance.
    :type instance_id: str

    """
    return web.Response(status=200)


async def g_et_resume_processes(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, scaling_processes=None) -> web.Response:
    """g_et_resume_processes

    &lt;p&gt;Resumes the specified suspended auto scaling processes, or all suspended process, for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html\&quot;&gt;Suspending and resuming scaling processes&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param scaling_processes: &lt;p&gt;One or more of the following processes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Launch&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Terminate&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AddToLoadBalancer&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AlarmNotification&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AZRebalance&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HealthCheck&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;InstanceRefresh&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ReplaceUnhealthy&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ScheduledActions&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you omit this property, all processes are specified.&lt;/p&gt;
    :type scaling_processes: List[str]

    """
    return web.Response(status=200)


async def g_et_rollback_instance_refresh(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_rollback_instance_refresh

    &lt;p&gt;Cancels an instance refresh that is in progress and rolls back any changes that it made. Amazon EC2 Auto Scaling replaces any instances that were replaced during the instance refresh. This restores your Auto Scaling group to the configuration that it was using before the start of the instance refresh. &lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.&lt;/p&gt; &lt;p&gt;A rollback is not supported in the following situations: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;There is no desired configuration specified for the instance refresh.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Auto Scaling group has a launch template that uses an Amazon Web Services Systems Manager parameter instead of an AMI ID for the &lt;code&gt;ImageId&lt;/code&gt; property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Auto Scaling group uses the launch template&#39;s &lt;code&gt;$Latest&lt;/code&gt; or &lt;code&gt;$Default&lt;/code&gt; version.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you receive a successful response from this operation, Amazon EC2 Auto Scaling immediately begins replacing instances. You can check the status of this operation through the &lt;a&gt;DescribeInstanceRefreshes&lt;/a&gt; API operation. &lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_set_desired_capacity(request: web.Request, auto_scaling_group_name, desired_capacity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, honor_cooldown=None) -> web.Response:
    """g_et_set_desired_capacity

    &lt;p&gt;Sets the size of the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;If a scale-in activity occurs as a result of a new &lt;code&gt;DesiredCapacity&lt;/code&gt; value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-manual-scaling.html\&quot;&gt;Manual scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain.
    :type desired_capacity: int
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param honor_cooldown: Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity. By default, Amazon EC2 Auto Scaling does not honor the cooldown period during manual scaling activities.
    :type honor_cooldown: bool

    """
    return web.Response(status=200)


async def g_et_set_instance_health(request: web.Request, instance_id, health_status, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, should_respect_grace_period=None) -> web.Response:
    """g_et_set_instance_health

    &lt;p&gt;Sets the health status of the specified instance.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html\&quot;&gt;Health checks for Auto Scaling instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The ID of the instance.
    :type instance_id: str
    :param health_status: The health status of the instance. Set to &lt;code&gt;Healthy&lt;/code&gt; to have the instance remain in service. Set to &lt;code&gt;Unhealthy&lt;/code&gt; to have the instance be out of service. Amazon EC2 Auto Scaling terminates and replaces the unhealthy instance.
    :type health_status: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param should_respect_grace_period: &lt;p&gt;If the Auto Scaling group of the specified instance has a &lt;code&gt;HealthCheckGracePeriod&lt;/code&gt; specified for the group, by default, this call respects the grace period. Set this to &lt;code&gt;False&lt;/code&gt;, to have the call not respect the grace period associated with the group.&lt;/p&gt; &lt;p&gt;For more information about the health check grace period, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html\&quot;&gt;CreateAutoScalingGroup&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling API Reference&lt;/i&gt;.&lt;/p&gt;
    :type should_respect_grace_period: bool

    """
    return web.Response(status=200)


async def g_et_set_instance_protection(request: web.Request, instance_ids, auto_scaling_group_name, protected_from_scale_in, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_instance_protection

    &lt;p&gt;Updates the instance protection settings of the specified instances. This operation cannot be called on instances in a warm pool.&lt;/p&gt; &lt;p&gt;For more information about preventing instances that are part of an Auto Scaling group from terminating on scale in, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html\&quot;&gt;Using instance scale-in protection&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of instance IDs, which is 50 per Auto Scaling group, the call fails.&lt;/p&gt;

    :param instance_ids: One or more instance IDs. You can specify up to 50 instances.
    :type instance_ids: List[str]
    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param protected_from_scale_in: Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
    :type protected_from_scale_in: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_start_instance_refresh(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, strategy=None, desired_configuration=None, preferences=None) -> web.Response:
    """g_et_start_instance_refresh

    &lt;p&gt;Starts an instance refresh. During an instance refresh, Amazon EC2 Auto Scaling performs a rolling update of instances in an Auto Scaling group. Instances are terminated first and then replaced, which temporarily reduces the capacity available within your Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group. This feature is helpful, for example, when you have a new AMI or a new user data script. You just need to create a new launch template that specifies the new AMI or user data script. Then start an instance refresh to immediately begin the process of updating instances in the group. &lt;/p&gt; &lt;p&gt;If successful, the request&#39;s response contains a unique ID that you can use to track the progress of the instance refresh. To query its status, call the &lt;a&gt;DescribeInstanceRefreshes&lt;/a&gt; API. To describe the instance refreshes that have already run, call the &lt;a&gt;DescribeInstanceRefreshes&lt;/a&gt; API. To cancel an instance refresh that is in progress, use the &lt;a&gt;CancelInstanceRefresh&lt;/a&gt; API. &lt;/p&gt; &lt;p&gt;An instance refresh might fail for several reasons, such as EC2 launch failures, misconfigured health checks, or not ignoring or allowing the termination of instances that are in &lt;code&gt;Standby&lt;/code&gt; state or protected from scale in. You can monitor for failed EC2 launches using the scaling activities. To find the scaling activities, call the &lt;a&gt;DescribeScalingActivities&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;If you enable auto rollback, your Auto Scaling group will be rolled back automatically when the instance refresh fails. You can enable this feature before starting an instance refresh by specifying the &lt;code&gt;AutoRollback&lt;/code&gt; property in the instance refresh preferences. Otherwise, to roll back an instance refresh before it finishes, use the &lt;a&gt;RollbackInstanceRefresh&lt;/a&gt; API. &lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param strategy: The strategy to use for the instance refresh. The only valid value is &lt;code&gt;Rolling&lt;/code&gt;.
    :type strategy: str
    :param desired_configuration: &lt;p&gt;The desired configuration. For example, the desired configuration can specify a new launch template or a new version of the current launch template.&lt;/p&gt; &lt;p&gt;Once the instance refresh succeeds, Amazon EC2 Auto Scaling updates the settings of the Auto Scaling group to reflect the new desired configuration. &lt;/p&gt; &lt;note&gt; &lt;p&gt;When you specify a new launch template or a new version of the current launch template for your desired configuration, consider enabling the &lt;code&gt;SkipMatching&lt;/code&gt; property in preferences. If it&#39;s enabled, Amazon EC2 Auto Scaling skips replacing instances that already use the specified launch template and instance types. This can help you reduce the number of replacements that are required to apply updates. &lt;/p&gt; &lt;/note&gt;
    :type desired_configuration: dict | bytes
    :param preferences: &lt;p&gt;Sets your preferences for the instance refresh so that it performs as expected when you start it. Includes the instance warmup time, the minimum healthy percentage, and the behaviors that you want Amazon EC2 Auto Scaling to use if instances that are in &lt;code&gt;Standby&lt;/code&gt; state or protected from scale in are found. You can also choose to enable additional features, such as the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Auto rollback&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Checkpoints&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CloudWatch alarms&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Skip matching&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type preferences: dict | bytes

    """
    desired_configuration = .from_dict(desired_configuration)
    preferences = .from_dict(preferences)
    return web.Response(status=200)


async def g_et_suspend_processes(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, scaling_processes=None) -> web.Response:
    """g_et_suspend_processes

    &lt;p&gt;Suspends the specified auto scaling processes, or all processes, for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;If you suspend either the &lt;code&gt;Launch&lt;/code&gt; or &lt;code&gt;Terminate&lt;/code&gt; process types, it can prevent other process types from functioning properly. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html\&quot;&gt;Suspending and resuming scaling processes&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To resume processes that have been suspended, call the &lt;a&gt;ResumeProcesses&lt;/a&gt; API.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param scaling_processes: &lt;p&gt;One or more of the following processes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Launch&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Terminate&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AddToLoadBalancer&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AlarmNotification&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AZRebalance&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HealthCheck&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;InstanceRefresh&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ReplaceUnhealthy&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ScheduledActions&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you omit this property, all processes are specified.&lt;/p&gt;
    :type scaling_processes: List[str]

    """
    return web.Response(status=200)


async def g_et_terminate_instance_in_auto_scaling_group(request: web.Request, instance_id, should_decrement_desired_capacity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_terminate_instance_in_auto_scaling_group

    &lt;p&gt;Terminates the specified instance and optionally adjusts the desired group size. This operation cannot be called on instances in a warm pool.&lt;/p&gt; &lt;p&gt;This call simply makes a termination request. The instance is not terminated immediately. When an instance is terminated, the instance status changes to &lt;code&gt;terminated&lt;/code&gt;. You can&#39;t connect to or start an instance after you&#39;ve terminated it.&lt;/p&gt; &lt;p&gt;If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are terminated. &lt;/p&gt; &lt;p&gt;By default, Amazon EC2 Auto Scaling balances instances across all Availability Zones. If you decrement the desired capacity, your Auto Scaling group can become unbalanced between Availability Zones. Amazon EC2 Auto Scaling tries to rebalance the group, and rebalancing might terminate instances in other zones. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#AutoScalingBehavior.InstanceUsage\&quot;&gt;Rebalancing activities&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The ID of the instance.
    :type instance_id: str
    :param should_decrement_desired_capacity: Indicates whether terminating the instance also decrements the size of the Auto Scaling group.
    :type should_decrement_desired_capacity: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def g_et_update_auto_scaling_group(request: web.Request, auto_scaling_group_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, launch_configuration_name=None, launch_template=None, mixed_instances_policy=None, min_size=None, max_size=None, desired_capacity=None, default_cooldown=None, availability_zones=None, health_check_type=None, health_check_grace_period=None, placement_group=None, vpc_zone_identifier=None, termination_policies=None, new_instances_protected_from_scale_in=None, service_linked_role_arn=None, max_instance_lifetime=None, capacity_rebalance=None, context=None, desired_capacity_type=None, default_instance_warmup=None) -> web.Response:
    """g_et_update_auto_scaling_group

    &lt;p&gt; &lt;b&gt;We strongly recommend that all Auto Scaling groups use launch templates to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Updates the configuration for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;To update an Auto Scaling group, specify the name of the group and the property that you want to change. Any properties that you don&#39;t specify are not changed by this update request. The new settings take effect on any scaling activities after this call returns. &lt;/p&gt; &lt;p&gt;If you associate a new launch configuration or template with an Auto Scaling group, all new instances will get the updated configuration. Existing instances continue to run with the configuration that they were originally launched with. When you update a group to specify a mixed instances policy instead of a launch configuration or template, existing instances may be replaced to match the new purchasing options that you specified in the policy. For example, if the group currently has 100% On-Demand capacity and the policy specifies 50% Spot capacity, this means that half of your instances will be gradually terminated and relaunched as Spot Instances. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that updating your group does not compromise the performance or availability of your application.&lt;/p&gt; &lt;p&gt;Note the following about changing &lt;code&gt;DesiredCapacity&lt;/code&gt;, &lt;code&gt;MaxSize&lt;/code&gt;, or &lt;code&gt;MinSize&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If a scale-in activity occurs as a result of a new &lt;code&gt;DesiredCapacity&lt;/code&gt; value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you specify a new value for &lt;code&gt;MinSize&lt;/code&gt; without specifying a value for &lt;code&gt;DesiredCapacity&lt;/code&gt;, and the new &lt;code&gt;MinSize&lt;/code&gt; is larger than the current size of the group, this sets the group&#39;s &lt;code&gt;DesiredCapacity&lt;/code&gt; to the new &lt;code&gt;MinSize&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you specify a new value for &lt;code&gt;MaxSize&lt;/code&gt; without specifying a value for &lt;code&gt;DesiredCapacity&lt;/code&gt;, and the new &lt;code&gt;MaxSize&lt;/code&gt; is smaller than the current size of the group, this sets the group&#39;s &lt;code&gt;DesiredCapacity&lt;/code&gt; to the new &lt;code&gt;MaxSize&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To see which properties have been set, call the &lt;a&gt;DescribeAutoScalingGroups&lt;/a&gt; API. To view the scaling policies for an Auto Scaling group, call the &lt;a&gt;DescribePolicies&lt;/a&gt; API. If the group has scaling policies, you can update them by calling the &lt;a&gt;PutScalingPolicy&lt;/a&gt; API.&lt;/p&gt;

    :param auto_scaling_group_name: The name of the Auto Scaling group.
    :type auto_scaling_group_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param launch_configuration_name: The name of the launch configuration. If you specify &lt;code&gt;LaunchConfigurationName&lt;/code&gt; in your update request, you can&#39;t specify &lt;code&gt;LaunchTemplate&lt;/code&gt; or &lt;code&gt;MixedInstancesPolicy&lt;/code&gt;.
    :type launch_configuration_name: str
    :param launch_template: The launch template and version to use to specify the updates. If you specify &lt;code&gt;LaunchTemplate&lt;/code&gt; in your update request, you can&#39;t specify &lt;code&gt;LaunchConfigurationName&lt;/code&gt; or &lt;code&gt;MixedInstancesPolicy&lt;/code&gt;.
    :type launch_template: dict | bytes
    :param mixed_instances_policy: The mixed instances policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html\&quot;&gt;Auto Scaling groups with multiple instance types and purchase options&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type mixed_instances_policy: dict | bytes
    :param min_size: The minimum size of the Auto Scaling group.
    :type min_size: int
    :param max_size: &lt;p&gt;The maximum size of the Auto Scaling group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above &lt;code&gt;MaxSize&lt;/code&gt; to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above &lt;code&gt;MaxSize&lt;/code&gt; by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).&lt;/p&gt; &lt;/note&gt;
    :type max_size: int
    :param desired_capacity: The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.
    :type desired_capacity: int
    :param default_cooldown: &lt;p&gt; &lt;i&gt;Only needed if you use simple scaling policies.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html\&quot;&gt;Scaling cooldowns for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;
    :type default_cooldown: int
    :param availability_zones: One or more Availability Zones for the group.
    :type availability_zones: List[str]
    :param health_check_type: &lt;p&gt;A comma-separated value string of one or more health check types.&lt;/p&gt; &lt;p&gt;The valid values are &lt;code&gt;EC2&lt;/code&gt;, &lt;code&gt;ELB&lt;/code&gt;, and &lt;code&gt;VPC_LATTICE&lt;/code&gt;. &lt;code&gt;EC2&lt;/code&gt; is the default health check and cannot be disabled. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html\&quot;&gt;Health checks for Auto Scaling instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Only specify &lt;code&gt;EC2&lt;/code&gt; if you must clear a value that was previously set.&lt;/p&gt;
    :type health_check_type: str
    :param health_check_grace_period: The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the &lt;code&gt;InService&lt;/code&gt; state. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html\&quot;&gt;Set the health check grace period for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type health_check_grace_period: int
    :param placement_group: &lt;p&gt;The name of an existing placement group into which to launch your instances. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html\&quot;&gt;Placement groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A &lt;i&gt;cluster&lt;/i&gt; placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group. &lt;/p&gt; &lt;/note&gt;
    :type placement_group: str
    :param vpc_zone_identifier: A comma-separated list of subnet IDs for a virtual private cloud (VPC). If you specify &lt;code&gt;VPCZoneIdentifier&lt;/code&gt; with &lt;code&gt;AvailabilityZones&lt;/code&gt;, the subnets that you specify must reside in those Availability Zones.
    :type vpc_zone_identifier: str
    :param termination_policies: &lt;p&gt;A policy or a list of policies that are used to select the instances to terminate. The policies are executed in the order that you list them. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html\&quot;&gt;Work with Amazon EC2 Auto Scaling termination policies&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;Default&lt;/code&gt; | &lt;code&gt;AllocationStrategy&lt;/code&gt; | &lt;code&gt;ClosestToNextInstanceHour&lt;/code&gt; | &lt;code&gt;NewestInstance&lt;/code&gt; | &lt;code&gt;OldestInstance&lt;/code&gt; | &lt;code&gt;OldestLaunchConfiguration&lt;/code&gt; | &lt;code&gt;OldestLaunchTemplate&lt;/code&gt; | &lt;code&gt;arn:aws:lambda:region:account-id:function:my-function:my-alias&lt;/code&gt; &lt;/p&gt;
    :type termination_policies: List[str]
    :param new_instances_protected_from_scale_in: Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html\&quot;&gt;Using instance scale-in protection&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type new_instances_protected_from_scale_in: bool
    :param service_linked_role_arn: The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html\&quot;&gt;Service-linked roles&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type service_linked_role_arn: str
    :param max_instance_lifetime: The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). To clear a previously set value, specify a new value of 0. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html\&quot;&gt;Replacing Auto Scaling instances based on maximum instance lifetime&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type max_instance_lifetime: int
    :param capacity_rebalance: Enables or disables Capacity Rebalancing. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html\&quot;&gt;Use Capacity Rebalancing to handle Amazon EC2 Spot Interruptions&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.
    :type capacity_rebalance: bool
    :param context: Reserved.
    :type context: str
    :param desired_capacity_type: &lt;p&gt;The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports &lt;code&gt;DesiredCapacityType&lt;/code&gt; for attribute-based instance type selection only. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-instance-type-requirements.html\&quot;&gt;Creating an Auto Scaling group using attribute-based instance type selection&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;By default, Amazon EC2 Auto Scaling specifies &lt;code&gt;units&lt;/code&gt;, which translates into number of instances.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;units&lt;/code&gt; | &lt;code&gt;vcpu&lt;/code&gt; | &lt;code&gt;memory-mib&lt;/code&gt; &lt;/p&gt;
    :type desired_capacity_type: str
    :param default_instance_warmup: &lt;p&gt;The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the &lt;code&gt;InService&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt;During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html\&quot;&gt;Set the default instance warmup for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, &lt;i&gt;even if it is set to 0 seconds&lt;/i&gt;. To remove a value that you previously set, include the property but specify &lt;code&gt;-1&lt;/code&gt; for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of &lt;code&gt;0&lt;/code&gt; or other nominal value.&lt;/p&gt; &lt;/important&gt;
    :type default_instance_warmup: int

    """
    launch_template = .from_dict(launch_template)
    mixed_instances_policy = .from_dict(mixed_instances_policy)
    return web.Response(status=200)


async def p_ost_attach_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_attach_instances

    &lt;p&gt;Attaches one or more EC2 instances to the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you attach instances, Amazon EC2 Auto Scaling increases the desired capacity of the group by the number of instances being attached. If the number of instances being attached plus the desired capacity of the group exceeds the maximum size of the group, the operation fails.&lt;/p&gt; &lt;p&gt;If there is a Classic Load Balancer attached to your Auto Scaling group, the instances are also registered with the load balancer. If there are target groups attached to your Auto Scaling group, the instances are also registered with the target groups.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-instance-asg.html\&quot;&gt;Attach EC2 instances to your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AttachInstancesQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_attach_load_balancer_target_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_attach_load_balancer_target_groups

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;AttachTrafficSources&lt;/a&gt;, which can attach multiple traffic sources types. We recommend using &lt;code&gt;AttachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;AttachLoadBalancerTargetGroups&lt;/code&gt;. You can use both the original &lt;code&gt;AttachLoadBalancerTargetGroups&lt;/code&gt; API operation and &lt;code&gt;AttachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Attaches one or more target groups to the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation is used with the following load balancer types: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Application Load Balancer - Operates at the application layer (layer 7) and supports HTTP and HTTPS. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Network Load Balancer - Operates at the transport layer (layer 4) and supports TCP, TLS, and UDP. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Gateway Load Balancer - Operates at the network layer (layer 3).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To describe the target groups for an Auto Scaling group, call the &lt;a&gt;DescribeLoadBalancerTargetGroups&lt;/a&gt; API. To detach the target group from the Auto Scaling group, call the &lt;a&gt;DetachLoadBalancerTargetGroups&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;This operation is additive and does not detach existing target groups or Classic Load Balancers from the Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AttachLoadBalancerTargetGroupsType.from_dict(body)
    return web.Response(status=200)


async def p_ost_attach_load_balancers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_attach_load_balancers

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;AttachTrafficSources&lt;/a&gt;, which can attach multiple traffic sources types. We recommend using &lt;code&gt;AttachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;AttachLoadBalancers&lt;/code&gt;. You can use both the original &lt;code&gt;AttachLoadBalancers&lt;/code&gt; API operation and &lt;code&gt;AttachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Attaches one or more Classic Load Balancers to the specified Auto Scaling group. Amazon EC2 Auto Scaling registers the running instances with these Classic Load Balancers.&lt;/p&gt; &lt;p&gt;To describe the load balancers for an Auto Scaling group, call the &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; API. To detach a load balancer from the Auto Scaling group, call the &lt;a&gt;DetachLoadBalancers&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;This operation is additive and does not detach existing Classic Load Balancers or target groups from the Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AttachLoadBalancersType.from_dict(body)
    return web.Response(status=200)


async def p_ost_attach_traffic_sources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_attach_traffic_sources

    &lt;p&gt;Attaches one or more traffic sources to the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;You can use any of the following as traffic sources for an Auto Scaling group:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Application Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Classic Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Gateway Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Network Load Balancer&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;VPC Lattice&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is additive and does not detach existing traffic sources from the Auto Scaling group. &lt;/p&gt; &lt;p&gt;After the operation completes, use the &lt;a&gt;DescribeTrafficSources&lt;/a&gt; API to return details about the state of the attachments between traffic sources and your Auto Scaling group. To detach a traffic source from the Auto Scaling group, call the &lt;a&gt;DetachTrafficSources&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AttachTrafficSourcesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_batch_delete_scheduled_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_batch_delete_scheduled_action

    Deletes one or more scheduled actions for the specified Auto Scaling group.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = BatchDeleteScheduledActionType.from_dict(body)
    return web.Response(status=200)


async def p_ost_batch_put_scheduled_update_group_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_batch_put_scheduled_update_group_action

    Creates or updates one or more scheduled scaling actions for an Auto Scaling group.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = BatchPutScheduledUpdateGroupActionType.from_dict(body)
    return web.Response(status=200)


async def p_ost_cancel_instance_refresh(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_cancel_instance_refresh

    &lt;p&gt;Cancels an instance refresh or rollback that is in progress. If an instance refresh or rollback is not in progress, an &lt;code&gt;ActiveInstanceRefreshNotFound&lt;/code&gt; error occurs.&lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.&lt;/p&gt; &lt;p&gt;When you cancel an instance refresh, this does not roll back any changes that it made. Use the &lt;a&gt;RollbackInstanceRefresh&lt;/a&gt; API to roll back instead.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CancelInstanceRefreshType.from_dict(body)
    return web.Response(status=200)


async def p_ost_complete_lifecycle_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_complete_lifecycle_action

    &lt;p&gt;Completes the lifecycle action for the specified token or instance with the specified result.&lt;/p&gt; &lt;p&gt;This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If you finish before the timeout period ends, send a callback by using the &lt;a&gt;CompleteLifecycleAction&lt;/a&gt; API call.&lt;/b&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/completing-lifecycle-hooks.html\&quot;&gt;Complete a lifecycle action&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CompleteLifecycleActionType.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_auto_scaling_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_auto_scaling_group

    &lt;p&gt; &lt;b&gt;We strongly recommend using a launch template when calling this operation to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Creates an Auto Scaling group with the specified name and attributes. &lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of Auto Scaling groups, the call fails. To query this limit, call the &lt;a&gt;DescribeAccountLimits&lt;/a&gt; API. For information about updating this limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html\&quot;&gt;Quotas for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For introductory exercises for creating an Auto Scaling group, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html\&quot;&gt;Getting started with Amazon EC2 Auto Scaling&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-register-lbs-with-asg.html\&quot;&gt;Tutorial: Set up a scaled and load-balanced application&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html\&quot;&gt;Auto Scaling groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Every Auto Scaling group has three size properties (&lt;code&gt;DesiredCapacity&lt;/code&gt;, &lt;code&gt;MaxSize&lt;/code&gt;, and &lt;code&gt;MinSize&lt;/code&gt;). Usually, you set these sizes based on a specific number of instances. However, if you configure a mixed instances policy that defines weights for the instance types, you must specify these sizes with the same units that you use for weighting instances.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateAutoScalingGroupType.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_launch_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_launch_configuration

    &lt;p&gt;Creates a launch configuration.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of launch configurations, the call fails. To query this limit, call the &lt;a&gt;DescribeAccountLimits&lt;/a&gt; API. For information about updating this limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html\&quot;&gt;Quotas for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html\&quot;&gt;Launch configurations&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a launch template or a launch configuration. We strongly recommend that you do not use launch configurations. They do not provide full functionality for Amazon EC2 Auto Scaling or Amazon EC2. For information about using launch templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html\&quot;&gt;Launch templates&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateLaunchConfigurationType.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_or_update_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_or_update_tags

    &lt;p&gt;Creates or updates tags for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html\&quot;&gt;Tag Auto Scaling groups and instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateOrUpdateTagsType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_auto_scaling_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_auto_scaling_group

    &lt;p&gt;Deletes the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;If the group has instances or scaling activities in progress, you must specify the option to force the deletion in order for it to succeed. The force delete operation will also terminate the EC2 instances. If the group has a warm pool, the force delete option also deletes the warm pool.&lt;/p&gt; &lt;p&gt;To remove instances from the Auto Scaling group before deleting it, call the &lt;a&gt;DetachInstances&lt;/a&gt; API with the list of instances and the option to decrement the desired capacity. This ensures that Amazon EC2 Auto Scaling does not launch replacement instances.&lt;/p&gt; &lt;p&gt;To terminate all instances before deleting the Auto Scaling group, call the &lt;a&gt;UpdateAutoScalingGroup&lt;/a&gt; API and set the minimum size and desired capacity of the Auto Scaling group to zero.&lt;/p&gt; &lt;p&gt;If the group has scaling policies, deleting the group deletes the policies, the underlying alarm actions, and any alarm that no longer has an associated action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html\&quot;&gt;Delete your Auto Scaling infrastructure&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteAutoScalingGroupType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_launch_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_launch_configuration

    &lt;p&gt;Deletes the specified launch configuration.&lt;/p&gt; &lt;p&gt;The launch configuration must not be attached to an Auto Scaling group. When this call completes, the launch configuration is no longer available for use.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = LaunchConfigurationNameType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_lifecycle_hook(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_lifecycle_hook

    &lt;p&gt;Deletes the specified lifecycle hook.&lt;/p&gt; &lt;p&gt;If there are any outstanding lifecycle actions, they are completed first (&lt;code&gt;ABANDON&lt;/code&gt; for launching instances, &lt;code&gt;CONTINUE&lt;/code&gt; for terminating instances).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteLifecycleHookType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_notification_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_notification_configuration

    Deletes the specified notification.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteNotificationConfigurationType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_policy

    &lt;p&gt;Deletes the specified scaling policy.&lt;/p&gt; &lt;p&gt;Deleting either a step scaling policy or a simple scaling policy deletes the underlying alarm action, but does not delete the alarm, even if it no longer has an associated action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/deleting-scaling-policy.html\&quot;&gt;Deleting a scaling policy&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeletePolicyType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_scheduled_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_scheduled_action

    Deletes the specified scheduled action.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteScheduledActionType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_tags

    Deletes the specified tags.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteTagsType.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_warm_pool(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_warm_pool

    &lt;p&gt;Deletes the warm pool for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html\&quot;&gt;Warm pools for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteWarmPoolType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_account_limits

    &lt;p&gt;Describes the current Amazon EC2 Auto Scaling resource quotas for your account.&lt;/p&gt; &lt;p&gt;When you establish an Amazon Web Services account, the account has initial quotas on the maximum number of Auto Scaling groups and launch configurations that you can create in a given Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html\&quot;&gt;Quotas for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_adjustment_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_adjustment_types

    &lt;p&gt;Describes the available adjustment types for step scaling and simple scaling policies.&lt;/p&gt; &lt;p&gt;The following adjustment types are supported:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ChangeInCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ExactCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PercentChangeInCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_auto_scaling_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_auto_scaling_groups

    &lt;p&gt;Gets information about the Auto Scaling groups in the account and Region.&lt;/p&gt; &lt;p&gt;If you specify Auto Scaling group names, the output includes information for only the specified Auto Scaling groups. If you specify filters, the output includes information for only those Auto Scaling groups that meet the filter criteria. If you do not specify group names or filters, the output includes information for all Auto Scaling groups. &lt;/p&gt; &lt;p&gt;This operation also returns information about instances in Auto Scaling groups. To retrieve information about the instances in a warm pool, you must call the &lt;a&gt;DescribeWarmPool&lt;/a&gt; API. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AutoScalingGroupNamesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_auto_scaling_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_auto_scaling_instances

    Gets information about the Auto Scaling instances in the account and Region.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAutoScalingInstancesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_auto_scaling_notification_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_auto_scaling_notification_types

    Describes the notification types that are supported by Amazon EC2 Auto Scaling.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_instance_refreshes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_instance_refreshes

    &lt;p&gt;Gets information about the instance refreshes for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.&lt;/p&gt; &lt;p&gt;To help you determine the status of an instance refresh, Amazon EC2 Auto Scaling returns information about the instance refreshes you previously initiated, including their status, start time, end time, the percentage of the instance refresh that is complete, and the number of instances remaining to update before the instance refresh is complete. If a rollback is initiated while an instance refresh is in progress, Amazon EC2 Auto Scaling also returns information about the rollback of the instance refresh.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeInstanceRefreshesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_launch_configurations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_launch_configurations

    Gets information about the launch configurations in the account and Region.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = LaunchConfigurationNamesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_lifecycle_hook_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_lifecycle_hook_types

    &lt;p&gt;Describes the available types of lifecycle hooks.&lt;/p&gt; &lt;p&gt;The following hook types are supported:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;autoscaling:EC2_INSTANCE_LAUNCHING&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;autoscaling:EC2_INSTANCE_TERMINATING&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_lifecycle_hooks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_lifecycle_hooks

    Gets information about the lifecycle hooks for the specified Auto Scaling group.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeLifecycleHooksType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_load_balancer_target_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_load_balancer_target_groups

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DescribeTrafficSources&lt;/a&gt;, which can describe multiple traffic sources types. We recommend using &lt;code&gt;DetachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DescribeLoadBalancerTargetGroups&lt;/code&gt;. You can use both the original &lt;code&gt;DescribeLoadBalancerTargetGroups&lt;/code&gt; API operation and &lt;code&gt;DescribeTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Gets information about the Elastic Load Balancing target groups for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;To determine the attachment status of the target group, use the &lt;code&gt;State&lt;/code&gt; element in the response. When you attach a target group to an Auto Scaling group, the initial &lt;code&gt;State&lt;/code&gt; value is &lt;code&gt;Adding&lt;/code&gt;. The state transitions to &lt;code&gt;Added&lt;/code&gt; after all Auto Scaling instances are registered with the target group. If Elastic Load Balancing health checks are enabled for the Auto Scaling group, the state transitions to &lt;code&gt;InService&lt;/code&gt; after at least one Auto Scaling instance passes the health check. When the target group is in the &lt;code&gt;InService&lt;/code&gt; state, Amazon EC2 Auto Scaling can terminate and replace any instances that are reported as unhealthy. If no registered instances pass the health checks, the target group doesn&#39;t enter the &lt;code&gt;InService&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt;Target groups also have an &lt;code&gt;InService&lt;/code&gt; state if you attach them in the &lt;a&gt;CreateAutoScalingGroup&lt;/a&gt; API call. If your target group state is &lt;code&gt;InService&lt;/code&gt;, but it is not working properly, check the scaling activities by calling &lt;a&gt;DescribeScalingActivities&lt;/a&gt; and take any corrective actions necessary.&lt;/p&gt; &lt;p&gt;For help with failed health checks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html\&quot;&gt;Troubleshooting Amazon EC2 Auto Scaling: Health checks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can use this operation to describe target groups that were attached by using &lt;a&gt;AttachLoadBalancerTargetGroups&lt;/a&gt;, but not for target groups that were attached by using &lt;a&gt;AttachTrafficSources&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeLoadBalancerTargetGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_load_balancers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_load_balancers

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DescribeTrafficSources&lt;/a&gt;, which can describe multiple traffic sources types. We recommend using &lt;code&gt;DescribeTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DescribeLoadBalancers&lt;/code&gt;. You can use both the original &lt;code&gt;DescribeLoadBalancers&lt;/code&gt; API operation and &lt;code&gt;DescribeTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Gets information about the load balancers for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation describes only Classic Load Balancers. If you have Application Load Balancers, Network Load Balancers, or Gateway Load Balancers, use the &lt;a&gt;DescribeLoadBalancerTargetGroups&lt;/a&gt; API instead.&lt;/p&gt; &lt;p&gt;To determine the attachment status of the load balancer, use the &lt;code&gt;State&lt;/code&gt; element in the response. When you attach a load balancer to an Auto Scaling group, the initial &lt;code&gt;State&lt;/code&gt; value is &lt;code&gt;Adding&lt;/code&gt;. The state transitions to &lt;code&gt;Added&lt;/code&gt; after all Auto Scaling instances are registered with the load balancer. If Elastic Load Balancing health checks are enabled for the Auto Scaling group, the state transitions to &lt;code&gt;InService&lt;/code&gt; after at least one Auto Scaling instance passes the health check. When the load balancer is in the &lt;code&gt;InService&lt;/code&gt; state, Amazon EC2 Auto Scaling can terminate and replace any instances that are reported as unhealthy. If no registered instances pass the health checks, the load balancer doesn&#39;t enter the &lt;code&gt;InService&lt;/code&gt; state. &lt;/p&gt; &lt;p&gt;Load balancers also have an &lt;code&gt;InService&lt;/code&gt; state if you attach them in the &lt;a&gt;CreateAutoScalingGroup&lt;/a&gt; API call. If your load balancer state is &lt;code&gt;InService&lt;/code&gt;, but it is not working properly, check the scaling activities by calling &lt;a&gt;DescribeScalingActivities&lt;/a&gt; and take any corrective actions necessary.&lt;/p&gt; &lt;p&gt;For help with failed health checks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html\&quot;&gt;Troubleshooting Amazon EC2 Auto Scaling: Health checks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html\&quot;&gt;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeLoadBalancersRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_metric_collection_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_metric_collection_types

    Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_notification_configurations(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_notification_configurations

    Gets information about the Amazon SNS notifications that are configured for one or more Auto Scaling groups.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeNotificationConfigurationsType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_policies

    Gets information about the scaling policies in the account and Region.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribePoliciesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_scaling_activities(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_scaling_activities

    &lt;p&gt;Gets information about the scaling activities in the account and Region.&lt;/p&gt; &lt;p&gt;When scaling events occur, you see a record of the scaling activity in the scaling activities. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html\&quot;&gt;Verifying a scaling activity for an Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If the scaling event succeeds, the value of the &lt;code&gt;StatusCode&lt;/code&gt; element in the response is &lt;code&gt;Successful&lt;/code&gt;. If an attempt to launch instances failed, the &lt;code&gt;StatusCode&lt;/code&gt; value is &lt;code&gt;Failed&lt;/code&gt; or &lt;code&gt;Cancelled&lt;/code&gt; and the &lt;code&gt;StatusMessage&lt;/code&gt; element in the response indicates the cause of the failure. For help interpreting the &lt;code&gt;StatusMessage&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html\&quot;&gt;Troubleshooting Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeScalingActivitiesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_scaling_process_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_scaling_process_types

    Describes the scaling process types for use with the &lt;a&gt;ResumeProcesses&lt;/a&gt; and &lt;a&gt;SuspendProcesses&lt;/a&gt; APIs.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_scheduled_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_scheduled_actions

    &lt;p&gt;Gets information about the scheduled actions that haven&#39;t run or that have not reached their end time.&lt;/p&gt; &lt;p&gt;To describe the scaling activities for scheduled actions that have already run, call the &lt;a&gt;DescribeScalingActivities&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeScheduledActionsType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_tags

    &lt;p&gt;Describes the specified tags.&lt;/p&gt; &lt;p&gt;You can use filters to limit the results. For example, you can query for the tags for a specific Auto Scaling group. You can specify multiple values for a filter. A tag must match at least one of the specified values for it to be included in the results.&lt;/p&gt; &lt;p&gt;You can also specify multiple filters. The result includes information for a particular tag only if it matches all the filters. If there&#39;s no match, no special message is returned.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html\&quot;&gt;Tag Auto Scaling groups and instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTagsType.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_termination_policy_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_termination_policy_types

    &lt;p&gt;Describes the termination policies supported by Amazon EC2 Auto Scaling.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html\&quot;&gt;Work with Amazon EC2 Auto Scaling termination policies&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def p_ost_describe_traffic_sources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_traffic_sources

    &lt;p&gt;Gets information about the traffic sources for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;You can optionally provide a traffic source type. If you provide a traffic source type, then the results only include that traffic source type.&lt;/p&gt; &lt;p&gt;If you do not provide a traffic source type, then the results include all the traffic sources for the specified Auto Scaling group. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTrafficSourcesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_warm_pool(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_warm_pool

    &lt;p&gt;Gets information about a warm pool and its instances.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html\&quot;&gt;Warm pools for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeWarmPoolType.from_dict(body)
    return web.Response(status=200)


async def p_ost_detach_instances(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detach_instances

    &lt;p&gt;Removes one or more instances from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;After the instances are detached, you can manage them independent of the Auto Scaling group.&lt;/p&gt; &lt;p&gt;If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are detached.&lt;/p&gt; &lt;p&gt;If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/detach-instance-asg.html\&quot;&gt;Detach EC2 instances from your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DetachInstancesQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_detach_load_balancer_target_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detach_load_balancer_target_groups

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DetachTrafficSources&lt;/a&gt;, which can detach multiple traffic sources types. We recommend using &lt;code&gt;DetachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DetachLoadBalancerTargetGroups&lt;/code&gt;. You can use both the original &lt;code&gt;DetachLoadBalancerTargetGroups&lt;/code&gt; API operation and &lt;code&gt;DetachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Detaches one or more target groups from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you detach a target group, it enters the &lt;code&gt;Removing&lt;/code&gt; state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the target group using the &lt;a&gt;DescribeLoadBalancerTargetGroups&lt;/a&gt; API call. The instances remain running.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can use this operation to detach target groups that were attached by using &lt;a&gt;AttachLoadBalancerTargetGroups&lt;/a&gt;, but not for target groups that were attached by using &lt;a&gt;AttachTrafficSources&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DetachLoadBalancerTargetGroupsType.from_dict(body)
    return web.Response(status=200)


async def p_ost_detach_load_balancers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detach_load_balancers

    &lt;note&gt; &lt;p&gt;This API operation is superseded by &lt;a&gt;DetachTrafficSources&lt;/a&gt;, which can detach multiple traffic sources types. We recommend using &lt;code&gt;DetachTrafficSources&lt;/code&gt; to simplify how you manage traffic sources. However, we continue to support &lt;code&gt;DetachLoadBalancers&lt;/code&gt;. You can use both the original &lt;code&gt;DetachLoadBalancers&lt;/code&gt; API operation and &lt;code&gt;DetachTrafficSources&lt;/code&gt; on the same Auto Scaling group.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Detaches one or more Classic Load Balancers from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation detaches only Classic Load Balancers. If you have Application Load Balancers, Network Load Balancers, or Gateway Load Balancers, use the &lt;a&gt;DetachLoadBalancerTargetGroups&lt;/a&gt; API instead.&lt;/p&gt; &lt;p&gt;When you detach a load balancer, it enters the &lt;code&gt;Removing&lt;/code&gt; state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using the &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; API call. The instances remain running.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DetachLoadBalancersType.from_dict(body)
    return web.Response(status=200)


async def p_ost_detach_traffic_sources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detach_traffic_sources

    &lt;p&gt;Detaches one or more traffic sources from the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;When you detach a traffic source, it enters the &lt;code&gt;Removing&lt;/code&gt; state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the traffic source using the &lt;a&gt;DescribeTrafficSources&lt;/a&gt; API call. The instances continue to run.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DetachTrafficSourcesType.from_dict(body)
    return web.Response(status=200)


async def p_ost_disable_metrics_collection(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disable_metrics_collection

    Disables group metrics collection for the specified Auto Scaling group.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DisableMetricsCollectionQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_enable_metrics_collection(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_enable_metrics_collection

    &lt;p&gt;Enables group metrics collection for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;You can use these metrics to track changes in an Auto Scaling group and to set alarms on threshold values. You can view group metrics using the Amazon EC2 Auto Scaling console or the CloudWatch console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html\&quot;&gt;Monitor CloudWatch metrics for your Auto Scaling groups and instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = EnableMetricsCollectionQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_enter_standby(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_enter_standby

    &lt;p&gt;Moves the specified instances into the standby state.&lt;/p&gt; &lt;p&gt;If you choose to decrement the desired capacity of the Auto Scaling group, the instances can enter standby as long as the desired capacity of the Auto Scaling group after the instances are placed into standby is equal to or greater than the minimum capacity of the group.&lt;/p&gt; &lt;p&gt;If you choose not to decrement the desired capacity of the Auto Scaling group, the Auto Scaling group launches new instances to replace the instances on standby.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html\&quot;&gt;Temporarily removing instances from your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = EnterStandbyQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_execute_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_execute_policy

    Executes the specified policy. This can be useful for testing the design of your scaling policy.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ExecutePolicyType.from_dict(body)
    return web.Response(status=200)


async def p_ost_exit_standby(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_exit_standby

    &lt;p&gt;Moves the specified instances out of the standby state.&lt;/p&gt; &lt;p&gt;After you put the instances back in service, the desired capacity is incremented.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html\&quot;&gt;Temporarily removing instances from your Auto Scaling group&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ExitStandbyQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_predictive_scaling_forecast(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_predictive_scaling_forecast

    &lt;p&gt;Retrieves the forecast data for a predictive scaling policy.&lt;/p&gt; &lt;p&gt;Load forecasts are predictions of the hourly load values using historical load data from CloudWatch and an analysis of historical trends. Capacity forecasts are represented as predicted values for the minimum capacity that is needed on an hourly basis, based on the hourly load forecast.&lt;/p&gt; &lt;p&gt;A minimum of 24 hours of data is required to create the initial forecasts. However, having a full 14 days of historical data results in more accurate forecasts.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html\&quot;&gt;Predictive scaling for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetPredictiveScalingForecastType.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_lifecycle_hook(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_lifecycle_hook

    &lt;p&gt;Creates or updates a lifecycle hook for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;Lifecycle hooks let you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.&lt;/p&gt; &lt;p&gt;This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.&lt;/b&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state using the &lt;a&gt;RecordLifecycleActionHeartbeat&lt;/a&gt; API call.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you finish before the timeout period ends, send a callback by using the &lt;a&gt;CompleteLifecycleAction&lt;/a&gt; API call.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html\&quot;&gt;Amazon EC2 Auto Scaling lifecycle hooks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails.&lt;/p&gt; &lt;p&gt;You can view the lifecycle hooks for an Auto Scaling group using the &lt;a&gt;DescribeLifecycleHooks&lt;/a&gt; API call. If you are no longer using a lifecycle hook, you can delete it by calling the &lt;a&gt;DeleteLifecycleHook&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutLifecycleHookType.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_notification_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_notification_configuration

    &lt;p&gt;Configures an Auto Scaling group to send notifications when specified events take place. Subscribers to the specified topic can have messages delivered to an endpoint such as a web server or an email address.&lt;/p&gt; &lt;p&gt;This configuration overwrites any existing configuration.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html\&quot;&gt;Getting Amazon SNS notifications when your Auto Scaling group scales&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of SNS topics, which is 10 per Auto Scaling group, the call fails.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutNotificationConfigurationType.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_scaling_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_scaling_policy

    &lt;p&gt;Creates or updates a scaling policy for an Auto Scaling group. Scaling policies are used to scale an Auto Scaling group based on configurable metrics. If no policies are defined, the dynamic scaling and predictive scaling features are not used. &lt;/p&gt; &lt;p&gt;For more information about using dynamic scaling, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html\&quot;&gt;Target tracking scaling policies&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html\&quot;&gt;Step and simple scaling policies&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information about using predictive scaling, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html\&quot;&gt;Predictive scaling for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can view the scaling policies for an Auto Scaling group using the &lt;a&gt;DescribePolicies&lt;/a&gt; API call. If you are no longer using a scaling policy, you can delete it by calling the &lt;a&gt;DeletePolicy&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutScalingPolicyType.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_scheduled_update_group_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_scheduled_update_group_action

    &lt;p&gt;Creates or updates a scheduled scaling action for an Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html\&quot;&gt;Scheduled scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can view the scheduled actions for an Auto Scaling group using the &lt;a&gt;DescribeScheduledActions&lt;/a&gt; API call. If you are no longer using a scheduled action, you can delete it by calling the &lt;a&gt;DeleteScheduledAction&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;If you try to schedule your action in the past, Amazon EC2 Auto Scaling returns an error message.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutScheduledUpdateGroupActionType.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_warm_pool(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_warm_pool

    &lt;p&gt;Creates or updates a warm pool for the specified Auto Scaling group. A warm pool is a pool of pre-initialized EC2 instances that sits alongside the Auto Scaling group. Whenever your application needs to scale out, the Auto Scaling group can draw on the warm pool to meet its new desired capacity. For more information and example configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html\&quot;&gt;Warm pools for Amazon EC2 Auto Scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This operation must be called from the Region in which the Auto Scaling group was created. This operation cannot be called on an Auto Scaling group that has a mixed instances policy or a launch template or launch configuration that requests Spot Instances.&lt;/p&gt; &lt;p&gt;You can view the instances in the warm pool using the &lt;a&gt;DescribeWarmPool&lt;/a&gt; API call. If you are no longer using a warm pool, you can delete it by calling the &lt;a&gt;DeleteWarmPool&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutWarmPoolType.from_dict(body)
    return web.Response(status=200)


async def p_ost_record_lifecycle_action_heartbeat(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_record_lifecycle_action_heartbeat

    &lt;p&gt;Records a heartbeat for the lifecycle action associated with the specified token or instance. This extends the timeout by the length of time defined using the &lt;a&gt;PutLifecycleHook&lt;/a&gt; API call.&lt;/p&gt; &lt;p&gt;This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state.&lt;/b&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you finish before the timeout period ends, send a callback by using the &lt;a&gt;CompleteLifecycleAction&lt;/a&gt; API call.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html\&quot;&gt;Amazon EC2 Auto Scaling lifecycle hooks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RecordLifecycleActionHeartbeatType.from_dict(body)
    return web.Response(status=200)


async def p_ost_resume_processes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_resume_processes

    &lt;p&gt;Resumes the specified suspended auto scaling processes, or all suspended process, for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html\&quot;&gt;Suspending and resuming scaling processes&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ScalingProcessQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_rollback_instance_refresh(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_rollback_instance_refresh

    &lt;p&gt;Cancels an instance refresh that is in progress and rolls back any changes that it made. Amazon EC2 Auto Scaling replaces any instances that were replaced during the instance refresh. This restores your Auto Scaling group to the configuration that it was using before the start of the instance refresh. &lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.&lt;/p&gt; &lt;p&gt;A rollback is not supported in the following situations: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;There is no desired configuration specified for the instance refresh.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Auto Scaling group has a launch template that uses an Amazon Web Services Systems Manager parameter instead of an AMI ID for the &lt;code&gt;ImageId&lt;/code&gt; property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Auto Scaling group uses the launch template&#39;s &lt;code&gt;$Latest&lt;/code&gt; or &lt;code&gt;$Default&lt;/code&gt; version.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you receive a successful response from this operation, Amazon EC2 Auto Scaling immediately begins replacing instances. You can check the status of this operation through the &lt;a&gt;DescribeInstanceRefreshes&lt;/a&gt; API operation. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RollbackInstanceRefreshType.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_desired_capacity(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_desired_capacity

    &lt;p&gt;Sets the size of the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;If a scale-in activity occurs as a result of a new &lt;code&gt;DesiredCapacity&lt;/code&gt; value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-manual-scaling.html\&quot;&gt;Manual scaling&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetDesiredCapacityType.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_instance_health(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_instance_health

    &lt;p&gt;Sets the health status of the specified instance.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html\&quot;&gt;Health checks for Auto Scaling instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetInstanceHealthQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_instance_protection(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_instance_protection

    &lt;p&gt;Updates the instance protection settings of the specified instances. This operation cannot be called on instances in a warm pool.&lt;/p&gt; &lt;p&gt;For more information about preventing instances that are part of an Auto Scaling group from terminating on scale in, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html\&quot;&gt;Using instance scale-in protection&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you exceed your maximum limit of instance IDs, which is 50 per Auto Scaling group, the call fails.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetInstanceProtectionQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_start_instance_refresh(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_start_instance_refresh

    &lt;p&gt;Starts an instance refresh. During an instance refresh, Amazon EC2 Auto Scaling performs a rolling update of instances in an Auto Scaling group. Instances are terminated first and then replaced, which temporarily reduces the capacity available within your Auto Scaling group.&lt;/p&gt; &lt;p&gt;This operation is part of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html\&quot;&gt;instance refresh feature&lt;/a&gt; in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group. This feature is helpful, for example, when you have a new AMI or a new user data script. You just need to create a new launch template that specifies the new AMI or user data script. Then start an instance refresh to immediately begin the process of updating instances in the group. &lt;/p&gt; &lt;p&gt;If successful, the request&#39;s response contains a unique ID that you can use to track the progress of the instance refresh. To query its status, call the &lt;a&gt;DescribeInstanceRefreshes&lt;/a&gt; API. To describe the instance refreshes that have already run, call the &lt;a&gt;DescribeInstanceRefreshes&lt;/a&gt; API. To cancel an instance refresh that is in progress, use the &lt;a&gt;CancelInstanceRefresh&lt;/a&gt; API. &lt;/p&gt; &lt;p&gt;An instance refresh might fail for several reasons, such as EC2 launch failures, misconfigured health checks, or not ignoring or allowing the termination of instances that are in &lt;code&gt;Standby&lt;/code&gt; state or protected from scale in. You can monitor for failed EC2 launches using the scaling activities. To find the scaling activities, call the &lt;a&gt;DescribeScalingActivities&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;If you enable auto rollback, your Auto Scaling group will be rolled back automatically when the instance refresh fails. You can enable this feature before starting an instance refresh by specifying the &lt;code&gt;AutoRollback&lt;/code&gt; property in the instance refresh preferences. Otherwise, to roll back an instance refresh before it finishes, use the &lt;a&gt;RollbackInstanceRefresh&lt;/a&gt; API. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = StartInstanceRefreshType.from_dict(body)
    return web.Response(status=200)


async def p_ost_suspend_processes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_suspend_processes

    &lt;p&gt;Suspends the specified auto scaling processes, or all processes, for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;If you suspend either the &lt;code&gt;Launch&lt;/code&gt; or &lt;code&gt;Terminate&lt;/code&gt; process types, it can prevent other process types from functioning properly. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html\&quot;&gt;Suspending and resuming scaling processes&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To resume processes that have been suspended, call the &lt;a&gt;ResumeProcesses&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ScalingProcessQuery.from_dict(body)
    return web.Response(status=200)


async def p_ost_terminate_instance_in_auto_scaling_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_terminate_instance_in_auto_scaling_group

    &lt;p&gt;Terminates the specified instance and optionally adjusts the desired group size. This operation cannot be called on instances in a warm pool.&lt;/p&gt; &lt;p&gt;This call simply makes a termination request. The instance is not terminated immediately. When an instance is terminated, the instance status changes to &lt;code&gt;terminated&lt;/code&gt;. You can&#39;t connect to or start an instance after you&#39;ve terminated it.&lt;/p&gt; &lt;p&gt;If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are terminated. &lt;/p&gt; &lt;p&gt;By default, Amazon EC2 Auto Scaling balances instances across all Availability Zones. If you decrement the desired capacity, your Auto Scaling group can become unbalanced between Availability Zones. Amazon EC2 Auto Scaling tries to rebalance the group, and rebalancing might terminate instances in other zones. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#AutoScalingBehavior.InstanceUsage\&quot;&gt;Rebalancing activities&lt;/a&gt; in the &lt;i&gt;Amazon EC2 Auto Scaling User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = TerminateInstanceInAutoScalingGroupType.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_auto_scaling_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_auto_scaling_group

    &lt;p&gt; &lt;b&gt;We strongly recommend that all Auto Scaling groups use launch templates to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Updates the configuration for the specified Auto Scaling group.&lt;/p&gt; &lt;p&gt;To update an Auto Scaling group, specify the name of the group and the property that you want to change. Any properties that you don&#39;t specify are not changed by this update request. The new settings take effect on any scaling activities after this call returns. &lt;/p&gt; &lt;p&gt;If you associate a new launch configuration or template with an Auto Scaling group, all new instances will get the updated configuration. Existing instances continue to run with the configuration that they were originally launched with. When you update a group to specify a mixed instances policy instead of a launch configuration or template, existing instances may be replaced to match the new purchasing options that you specified in the policy. For example, if the group currently has 100% On-Demand capacity and the policy specifies 50% Spot capacity, this means that half of your instances will be gradually terminated and relaunched as Spot Instances. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that updating your group does not compromise the performance or availability of your application.&lt;/p&gt; &lt;p&gt;Note the following about changing &lt;code&gt;DesiredCapacity&lt;/code&gt;, &lt;code&gt;MaxSize&lt;/code&gt;, or &lt;code&gt;MinSize&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If a scale-in activity occurs as a result of a new &lt;code&gt;DesiredCapacity&lt;/code&gt; value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you specify a new value for &lt;code&gt;MinSize&lt;/code&gt; without specifying a value for &lt;code&gt;DesiredCapacity&lt;/code&gt;, and the new &lt;code&gt;MinSize&lt;/code&gt; is larger than the current size of the group, this sets the group&#39;s &lt;code&gt;DesiredCapacity&lt;/code&gt; to the new &lt;code&gt;MinSize&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you specify a new value for &lt;code&gt;MaxSize&lt;/code&gt; without specifying a value for &lt;code&gt;DesiredCapacity&lt;/code&gt;, and the new &lt;code&gt;MaxSize&lt;/code&gt; is smaller than the current size of the group, this sets the group&#39;s &lt;code&gt;DesiredCapacity&lt;/code&gt; to the new &lt;code&gt;MaxSize&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To see which properties have been set, call the &lt;a&gt;DescribeAutoScalingGroups&lt;/a&gt; API. To view the scaling policies for an Auto Scaling group, call the &lt;a&gt;DescribePolicies&lt;/a&gt; API. If the group has scaling policies, you can update them by calling the &lt;a&gt;PutScalingPolicy&lt;/a&gt; API.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateAutoScalingGroupType.from_dict(body)
    return web.Response(status=200)
