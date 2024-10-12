from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_match_input import AcceptMatchInput
from openapi_server.models.claim_game_server_input import ClaimGameServerInput
from openapi_server.models.claim_game_server_output import ClaimGameServerOutput
from openapi_server.models.create_alias_input import CreateAliasInput
from openapi_server.models.create_alias_output import CreateAliasOutput
from openapi_server.models.create_build_input import CreateBuildInput
from openapi_server.models.create_build_output import CreateBuildOutput
from openapi_server.models.create_fleet_input import CreateFleetInput
from openapi_server.models.create_fleet_locations_input import CreateFleetLocationsInput
from openapi_server.models.create_fleet_locations_output import CreateFleetLocationsOutput
from openapi_server.models.create_fleet_output import CreateFleetOutput
from openapi_server.models.create_game_server_group_input import CreateGameServerGroupInput
from openapi_server.models.create_game_server_group_output import CreateGameServerGroupOutput
from openapi_server.models.create_game_session_input import CreateGameSessionInput
from openapi_server.models.create_game_session_output import CreateGameSessionOutput
from openapi_server.models.create_game_session_queue_input import CreateGameSessionQueueInput
from openapi_server.models.create_game_session_queue_output import CreateGameSessionQueueOutput
from openapi_server.models.create_location_input import CreateLocationInput
from openapi_server.models.create_location_output import CreateLocationOutput
from openapi_server.models.create_matchmaking_configuration_input import CreateMatchmakingConfigurationInput
from openapi_server.models.create_matchmaking_configuration_output import CreateMatchmakingConfigurationOutput
from openapi_server.models.create_matchmaking_rule_set_input import CreateMatchmakingRuleSetInput
from openapi_server.models.create_matchmaking_rule_set_output import CreateMatchmakingRuleSetOutput
from openapi_server.models.create_player_session_input import CreatePlayerSessionInput
from openapi_server.models.create_player_session_output import CreatePlayerSessionOutput
from openapi_server.models.create_player_sessions_input import CreatePlayerSessionsInput
from openapi_server.models.create_player_sessions_output import CreatePlayerSessionsOutput
from openapi_server.models.create_script_input import CreateScriptInput
from openapi_server.models.create_script_output import CreateScriptOutput
from openapi_server.models.create_vpc_peering_authorization_input import CreateVpcPeeringAuthorizationInput
from openapi_server.models.create_vpc_peering_authorization_output import CreateVpcPeeringAuthorizationOutput
from openapi_server.models.create_vpc_peering_connection_input import CreateVpcPeeringConnectionInput
from openapi_server.models.delete_alias_input import DeleteAliasInput
from openapi_server.models.delete_build_input import DeleteBuildInput
from openapi_server.models.delete_fleet_input import DeleteFleetInput
from openapi_server.models.delete_fleet_locations_input import DeleteFleetLocationsInput
from openapi_server.models.delete_fleet_locations_output import DeleteFleetLocationsOutput
from openapi_server.models.delete_game_server_group_input import DeleteGameServerGroupInput
from openapi_server.models.delete_game_server_group_output import DeleteGameServerGroupOutput
from openapi_server.models.delete_game_session_queue_input import DeleteGameSessionQueueInput
from openapi_server.models.delete_location_input import DeleteLocationInput
from openapi_server.models.delete_matchmaking_configuration_input import DeleteMatchmakingConfigurationInput
from openapi_server.models.delete_matchmaking_rule_set_input import DeleteMatchmakingRuleSetInput
from openapi_server.models.delete_scaling_policy_input import DeleteScalingPolicyInput
from openapi_server.models.delete_script_input import DeleteScriptInput
from openapi_server.models.delete_vpc_peering_authorization_input import DeleteVpcPeeringAuthorizationInput
from openapi_server.models.delete_vpc_peering_connection_input import DeleteVpcPeeringConnectionInput
from openapi_server.models.deregister_compute_input import DeregisterComputeInput
from openapi_server.models.deregister_game_server_input import DeregisterGameServerInput
from openapi_server.models.describe_alias_input import DescribeAliasInput
from openapi_server.models.describe_alias_output import DescribeAliasOutput
from openapi_server.models.describe_build_input import DescribeBuildInput
from openapi_server.models.describe_build_output import DescribeBuildOutput
from openapi_server.models.describe_compute_input import DescribeComputeInput
from openapi_server.models.describe_compute_output import DescribeComputeOutput
from openapi_server.models.describe_ec2_instance_limits_input import DescribeEC2InstanceLimitsInput
from openapi_server.models.describe_ec2_instance_limits_output import DescribeEC2InstanceLimitsOutput
from openapi_server.models.describe_fleet_attributes_input import DescribeFleetAttributesInput
from openapi_server.models.describe_fleet_attributes_output import DescribeFleetAttributesOutput
from openapi_server.models.describe_fleet_capacity_input import DescribeFleetCapacityInput
from openapi_server.models.describe_fleet_capacity_output import DescribeFleetCapacityOutput
from openapi_server.models.describe_fleet_events_input import DescribeFleetEventsInput
from openapi_server.models.describe_fleet_events_output import DescribeFleetEventsOutput
from openapi_server.models.describe_fleet_location_attributes_input import DescribeFleetLocationAttributesInput
from openapi_server.models.describe_fleet_location_attributes_output import DescribeFleetLocationAttributesOutput
from openapi_server.models.describe_fleet_location_capacity_input import DescribeFleetLocationCapacityInput
from openapi_server.models.describe_fleet_location_capacity_output import DescribeFleetLocationCapacityOutput
from openapi_server.models.describe_fleet_location_utilization_input import DescribeFleetLocationUtilizationInput
from openapi_server.models.describe_fleet_location_utilization_output import DescribeFleetLocationUtilizationOutput
from openapi_server.models.describe_fleet_port_settings_input import DescribeFleetPortSettingsInput
from openapi_server.models.describe_fleet_port_settings_output import DescribeFleetPortSettingsOutput
from openapi_server.models.describe_fleet_utilization_input import DescribeFleetUtilizationInput
from openapi_server.models.describe_fleet_utilization_output import DescribeFleetUtilizationOutput
from openapi_server.models.describe_game_server_group_input import DescribeGameServerGroupInput
from openapi_server.models.describe_game_server_group_output import DescribeGameServerGroupOutput
from openapi_server.models.describe_game_server_input import DescribeGameServerInput
from openapi_server.models.describe_game_server_instances_input import DescribeGameServerInstancesInput
from openapi_server.models.describe_game_server_instances_output import DescribeGameServerInstancesOutput
from openapi_server.models.describe_game_server_output import DescribeGameServerOutput
from openapi_server.models.describe_game_session_details_input import DescribeGameSessionDetailsInput
from openapi_server.models.describe_game_session_details_output import DescribeGameSessionDetailsOutput
from openapi_server.models.describe_game_session_placement_input import DescribeGameSessionPlacementInput
from openapi_server.models.describe_game_session_placement_output import DescribeGameSessionPlacementOutput
from openapi_server.models.describe_game_session_queues_input import DescribeGameSessionQueuesInput
from openapi_server.models.describe_game_session_queues_output import DescribeGameSessionQueuesOutput
from openapi_server.models.describe_game_sessions_input import DescribeGameSessionsInput
from openapi_server.models.describe_game_sessions_output import DescribeGameSessionsOutput
from openapi_server.models.describe_instances_input import DescribeInstancesInput
from openapi_server.models.describe_instances_output import DescribeInstancesOutput
from openapi_server.models.describe_matchmaking_configurations_input import DescribeMatchmakingConfigurationsInput
from openapi_server.models.describe_matchmaking_configurations_output import DescribeMatchmakingConfigurationsOutput
from openapi_server.models.describe_matchmaking_input import DescribeMatchmakingInput
from openapi_server.models.describe_matchmaking_output import DescribeMatchmakingOutput
from openapi_server.models.describe_matchmaking_rule_sets_input import DescribeMatchmakingRuleSetsInput
from openapi_server.models.describe_matchmaking_rule_sets_output import DescribeMatchmakingRuleSetsOutput
from openapi_server.models.describe_player_sessions_input import DescribePlayerSessionsInput
from openapi_server.models.describe_player_sessions_output import DescribePlayerSessionsOutput
from openapi_server.models.describe_runtime_configuration_input import DescribeRuntimeConfigurationInput
from openapi_server.models.describe_runtime_configuration_output import DescribeRuntimeConfigurationOutput
from openapi_server.models.describe_scaling_policies_input import DescribeScalingPoliciesInput
from openapi_server.models.describe_scaling_policies_output import DescribeScalingPoliciesOutput
from openapi_server.models.describe_script_input import DescribeScriptInput
from openapi_server.models.describe_script_output import DescribeScriptOutput
from openapi_server.models.describe_vpc_peering_authorizations_output import DescribeVpcPeeringAuthorizationsOutput
from openapi_server.models.describe_vpc_peering_connections_input import DescribeVpcPeeringConnectionsInput
from openapi_server.models.describe_vpc_peering_connections_output import DescribeVpcPeeringConnectionsOutput
from openapi_server.models.get_compute_access_input import GetComputeAccessInput
from openapi_server.models.get_compute_access_output import GetComputeAccessOutput
from openapi_server.models.get_compute_auth_token_input import GetComputeAuthTokenInput
from openapi_server.models.get_compute_auth_token_output import GetComputeAuthTokenOutput
from openapi_server.models.get_game_session_log_url_input import GetGameSessionLogUrlInput
from openapi_server.models.get_game_session_log_url_output import GetGameSessionLogUrlOutput
from openapi_server.models.get_instance_access_input import GetInstanceAccessInput
from openapi_server.models.get_instance_access_output import GetInstanceAccessOutput
from openapi_server.models.list_aliases_input import ListAliasesInput
from openapi_server.models.list_aliases_output import ListAliasesOutput
from openapi_server.models.list_builds_input import ListBuildsInput
from openapi_server.models.list_builds_output import ListBuildsOutput
from openapi_server.models.list_compute_input import ListComputeInput
from openapi_server.models.list_compute_output import ListComputeOutput
from openapi_server.models.list_fleets_input import ListFleetsInput
from openapi_server.models.list_fleets_output import ListFleetsOutput
from openapi_server.models.list_game_server_groups_input import ListGameServerGroupsInput
from openapi_server.models.list_game_server_groups_output import ListGameServerGroupsOutput
from openapi_server.models.list_game_servers_input import ListGameServersInput
from openapi_server.models.list_game_servers_output import ListGameServersOutput
from openapi_server.models.list_locations_input import ListLocationsInput
from openapi_server.models.list_locations_output import ListLocationsOutput
from openapi_server.models.list_scripts_input import ListScriptsInput
from openapi_server.models.list_scripts_output import ListScriptsOutput
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_scaling_policy_input import PutScalingPolicyInput
from openapi_server.models.put_scaling_policy_output import PutScalingPolicyOutput
from openapi_server.models.register_compute_input import RegisterComputeInput
from openapi_server.models.register_compute_output import RegisterComputeOutput
from openapi_server.models.register_game_server_input import RegisterGameServerInput
from openapi_server.models.register_game_server_output import RegisterGameServerOutput
from openapi_server.models.request_upload_credentials_input import RequestUploadCredentialsInput
from openapi_server.models.request_upload_credentials_output import RequestUploadCredentialsOutput
from openapi_server.models.resolve_alias_input import ResolveAliasInput
from openapi_server.models.resolve_alias_output import ResolveAliasOutput
from openapi_server.models.resume_game_server_group_input import ResumeGameServerGroupInput
from openapi_server.models.resume_game_server_group_output import ResumeGameServerGroupOutput
from openapi_server.models.search_game_sessions_input import SearchGameSessionsInput
from openapi_server.models.search_game_sessions_output import SearchGameSessionsOutput
from openapi_server.models.start_fleet_actions_input import StartFleetActionsInput
from openapi_server.models.start_fleet_actions_output import StartFleetActionsOutput
from openapi_server.models.start_game_session_placement_input import StartGameSessionPlacementInput
from openapi_server.models.start_game_session_placement_output import StartGameSessionPlacementOutput
from openapi_server.models.start_match_backfill_input import StartMatchBackfillInput
from openapi_server.models.start_match_backfill_output import StartMatchBackfillOutput
from openapi_server.models.start_matchmaking_input import StartMatchmakingInput
from openapi_server.models.start_matchmaking_output import StartMatchmakingOutput
from openapi_server.models.stop_fleet_actions_input import StopFleetActionsInput
from openapi_server.models.stop_fleet_actions_output import StopFleetActionsOutput
from openapi_server.models.stop_game_session_placement_input import StopGameSessionPlacementInput
from openapi_server.models.stop_game_session_placement_output import StopGameSessionPlacementOutput
from openapi_server.models.stop_matchmaking_input import StopMatchmakingInput
from openapi_server.models.suspend_game_server_group_input import SuspendGameServerGroupInput
from openapi_server.models.suspend_game_server_group_output import SuspendGameServerGroupOutput
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_alias_input import UpdateAliasInput
from openapi_server.models.update_alias_output import UpdateAliasOutput
from openapi_server.models.update_build_input import UpdateBuildInput
from openapi_server.models.update_build_output import UpdateBuildOutput
from openapi_server.models.update_fleet_attributes_input import UpdateFleetAttributesInput
from openapi_server.models.update_fleet_attributes_output import UpdateFleetAttributesOutput
from openapi_server.models.update_fleet_capacity_input import UpdateFleetCapacityInput
from openapi_server.models.update_fleet_capacity_output import UpdateFleetCapacityOutput
from openapi_server.models.update_fleet_port_settings_input import UpdateFleetPortSettingsInput
from openapi_server.models.update_fleet_port_settings_output import UpdateFleetPortSettingsOutput
from openapi_server.models.update_game_server_group_input import UpdateGameServerGroupInput
from openapi_server.models.update_game_server_group_output import UpdateGameServerGroupOutput
from openapi_server.models.update_game_server_input import UpdateGameServerInput
from openapi_server.models.update_game_server_output import UpdateGameServerOutput
from openapi_server.models.update_game_session_input import UpdateGameSessionInput
from openapi_server.models.update_game_session_output import UpdateGameSessionOutput
from openapi_server.models.update_game_session_queue_input import UpdateGameSessionQueueInput
from openapi_server.models.update_game_session_queue_output import UpdateGameSessionQueueOutput
from openapi_server.models.update_matchmaking_configuration_input import UpdateMatchmakingConfigurationInput
from openapi_server.models.update_matchmaking_configuration_output import UpdateMatchmakingConfigurationOutput
from openapi_server.models.update_runtime_configuration_input import UpdateRuntimeConfigurationInput
from openapi_server.models.update_runtime_configuration_output import UpdateRuntimeConfigurationOutput
from openapi_server.models.update_script_input import UpdateScriptInput
from openapi_server.models.update_script_output import UpdateScriptOutput
from openapi_server.models.validate_matchmaking_rule_set_input import ValidateMatchmakingRuleSetInput
from openapi_server.models.validate_matchmaking_rule_set_output import ValidateMatchmakingRuleSetOutput
from openapi_server import util


async def accept_match(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_match

    &lt;p&gt;Registers a player&#39;s acceptance or rejection of a proposed FlexMatch match. A matchmaking configuration may require player acceptance; if so, then matches built with that configuration cannot be completed unless all players accept the proposed match within a specified time limit. &lt;/p&gt; &lt;p&gt;When FlexMatch builds a match, all the matchmaking tickets involved in the proposed match are placed into status &lt;code&gt;REQUIRES_ACCEPTANCE&lt;/code&gt;. This is a trigger for your game to get acceptance from all players in the ticket. Acceptances are only valid for tickets when they are in this status; all other acceptances result in an error.&lt;/p&gt; &lt;p&gt;To register acceptance, specify the ticket ID, a response, and one or more players. Once all players have registered acceptance, the matchmaking tickets advance to status &lt;code&gt;PLACING&lt;/code&gt;, where a new game session is created for the match. &lt;/p&gt; &lt;p&gt;If any player rejects the match, or if acceptances are not received before a specified timeout, the proposed match is dropped. The matchmaking tickets are then handled in one of two ways: For tickets where one or more players rejected the match or failed to respond, the ticket status is set to &lt;code&gt;CANCELLED&lt;/code&gt;, and processing is terminated. For tickets where players have accepted or not yet responded, the ticket status is returned to &lt;code&gt;SEARCHING&lt;/code&gt; to find a new match. A new matchmaking request for these players can be submitted as needed. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html\&quot;&gt; Add FlexMatch to a game client&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html\&quot;&gt; FlexMatch events&lt;/a&gt; (reference)&lt;/p&gt;

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
    body = AcceptMatchInput.from_dict(body)
    return web.Response(status=200)


async def claim_game_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """claim_game_server

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Locates an available game server and temporarily reserves it to host gameplay and players. This operation is called from a game client or client service (such as a matchmaker) to request hosting resources for a new game session. In response, Amazon GameLift FleetIQ locates an available game server, places it in &lt;code&gt;CLAIMED&lt;/code&gt; status for 60 seconds, and returns connection information that players can use to connect to the game server. &lt;/p&gt; &lt;p&gt;To claim a game server, identify a game server group. You can also specify a game server ID, although this approach bypasses Amazon GameLift FleetIQ placement optimization. Optionally, include game data to pass to the game server at the start of a game session, such as a game map or player information. Add filter options to further restrict how a game server is chosen, such as only allowing game servers on &lt;code&gt;ACTIVE&lt;/code&gt; instances to be claimed.&lt;/p&gt; &lt;p&gt;When a game server is successfully claimed, connection information is returned. A claimed game server&#39;s utilization status remains &lt;code&gt;AVAILABLE&lt;/code&gt; while the claim status is set to &lt;code&gt;CLAIMED&lt;/code&gt; for up to 60 seconds. This time period gives the game server time to update its status to &lt;code&gt;UTILIZED&lt;/code&gt; after players join. If the game server&#39;s status is not updated within 60 seconds, the game server reverts to unclaimed status and is available to be claimed by another request. The claim time period is a fixed value and is not configurable.&lt;/p&gt; &lt;p&gt;If you try to claim a specific game server, this request will fail in the following cases:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the game server utilization status is &lt;code&gt;UTILIZED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the game server claim status is &lt;code&gt;CLAIMED&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the game server is running on an instance in &lt;code&gt;DRAINING&lt;/code&gt; status and the provided filter option does not allow placing on &lt;code&gt;DRAINING&lt;/code&gt; instances.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = ClaimGameServerInput.from_dict(body)
    return web.Response(status=200)


async def create_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_alias

    &lt;p&gt;Creates an alias for a fleet. In most situations, you can use an alias ID in place of a fleet ID. An alias provides a level of abstraction for a fleet that is useful when redirecting player traffic from one fleet to another, such as when updating your game build. &lt;/p&gt; &lt;p&gt;Amazon GameLift supports two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias is used to display messaging or link to a URL instead of routing players to an active fleet. For example, you might use a terminal alias when a game version is no longer supported and you want to direct players to an upgrade site. &lt;/p&gt; &lt;p&gt;To create a fleet alias, specify an alias name, routing strategy, and optional description. Each simple alias can point to only one fleet, but a fleet can have multiple aliases. If successful, a new alias record is returned, including an alias ID and an ARN. You can reassign an alias to another fleet by calling &lt;code&gt;UpdateAlias&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreateAliasInput.from_dict(body)
    return web.Response(status=200)


async def create_build(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_build

    &lt;p&gt;Creates a new Amazon GameLift build resource for your game server binary files. Combine game server binaries into a zip file for use with Amazon GameLift. &lt;/p&gt; &lt;important&gt; &lt;p&gt;When setting up a new game build for Amazon GameLift, we recommend using the CLI command &lt;b&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/gamelift/upload-build.html\&quot;&gt;upload-build&lt;/a&gt; &lt;/b&gt;. This helper command combines two tasks: (1) it uploads your build files from a file directory to an Amazon GameLift Amazon S3 location, and (2) it creates a new build resource.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You can use the &lt;code&gt;CreateBuild&lt;/code&gt; operation in the following scenarios:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Create a new game build with build files that are in an Amazon S3 location under an Amazon Web Services account that you control. To use this option, you give Amazon GameLift access to the Amazon S3 bucket. With permissions in place, specify a build name, operating system, and the Amazon S3 storage location of your game build.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Upload your build files to a Amazon GameLift Amazon S3 location. To use this option, specify a build name and operating system. This operation creates a new build resource and also returns an Amazon S3 location with temporary access credentials. Use the credentials to manually upload your build files to the specified Amazon S3 location. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html\&quot;&gt;Uploading Objects&lt;/a&gt; in the &lt;i&gt;Amazon S3 Developer Guide&lt;/i&gt;. After you upload build files to the Amazon GameLift Amazon S3 location, you can&#39;t update them. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, this operation creates a new build resource with a unique build ID and places it in &lt;code&gt;INITIALIZED&lt;/code&gt; status. A build must be in &lt;code&gt;READY&lt;/code&gt; status before you can create fleets with it.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html\&quot;&gt;Uploading Your Game&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build\&quot;&gt; Create a Build with Files in Amazon S3&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreateBuildInput.from_dict(body)
    return web.Response(status=200)


async def create_fleet(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_fleet

    &lt;p&gt;Creates a fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances to host your custom game server or Realtime Servers. Use this operation to configure the computing resources for your fleet and provide instructions for running game servers on each instance.&lt;/p&gt; &lt;p&gt;Most Amazon GameLift fleets can deploy instances to multiple locations, including the home Region (where the fleet is created) and an optional set of remote locations. Fleets that are created in the following Amazon Web Services Regions support multiple locations: us-east-1 (N. Virginia), us-west-2 (Oregon), eu-central-1 (Frankfurt), eu-west-1 (Ireland), ap-southeast-2 (Sydney), ap-northeast-1 (Tokyo), and ap-northeast-2 (Seoul). Fleets that are created in other Amazon GameLift Regions can deploy instances in the fleet&#39;s home Region only. All fleet instances use the same configuration regardless of location; however, you can adjust capacity settings and turn auto-scaling on/off for each location.&lt;/p&gt; &lt;p&gt;To create a fleet, choose the hardware for your instances, specify a game server build or Realtime script to deploy, and provide a runtime configuration to direct Amazon GameLift how to start and run game servers on each instance in the fleet. Set permissions for inbound traffic to your game servers, and enable optional features as needed. When creating a multi-location fleet, provide a list of additional remote locations.&lt;/p&gt; &lt;p&gt;If you need to debug your fleet, fetch logs, view performance metrics or other actions on the fleet, create the development fleet with port 22/3389 open. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you&#39;re finished. &lt;/p&gt; &lt;p&gt;If successful, this operation creates a new Fleet resource and places it in &lt;code&gt;NEW&lt;/code&gt; status, which prompts Amazon GameLift to initiate the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-all.html#fleets-creation-workflow\&quot;&gt;fleet creation workflow&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up fleets&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html#fleets-creating-debug-creation\&quot;&gt;Debug fleet creation issues&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Multi-location fleets&lt;/a&gt; &lt;/p&gt;

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
    body = CreateFleetInput.from_dict(body)
    return web.Response(status=200)


async def create_fleet_locations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_fleet_locations

    &lt;p&gt;Adds remote locations to a fleet and begins populating the new locations with EC2 instances. The new instances conform to the fleet&#39;s instance type, auto-scaling, and other configuration settings. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation cannot be used with fleets that don&#39;t support remote locations. Fleets can have multiple locations only if they reside in Amazon Web Services Regions that support this feature and were created after the feature was released in March 2021.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To add fleet locations, specify the fleet to be updated and provide a list of one or more locations. &lt;/p&gt; &lt;p&gt;If successful, this operation returns the list of added locations with their status set to &lt;code&gt;NEW&lt;/code&gt;. Amazon GameLift initiates the process of starting an instance in each added location. You can track the status of each new location by monitoring location creation events using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetEvents.html\&quot;&gt;DescribeFleetEvents&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up fleets&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Multi-location fleets&lt;/a&gt; &lt;/p&gt;

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
    body = CreateFleetLocationsInput.from_dict(body)
    return web.Response(status=200)


async def create_game_server_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_game_server_group

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Creates a Amazon GameLift FleetIQ game server group for managing game hosting on a collection of Amazon Elastic Compute Cloud instances for game hosting. This operation creates the game server group, creates an Auto Scaling group in your Amazon Web Services account, and establishes a link between the two groups. You can view the status of your game server groups in the Amazon GameLift console. Game server group metrics and events are emitted to Amazon CloudWatch.&lt;/p&gt; &lt;p&gt;Before creating a new game server group, you must have the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An Amazon Elastic Compute Cloud launch template that specifies how to launch Amazon Elastic Compute Cloud instances with your game server build. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html\&quot;&gt; Launching an Instance from a Launch Template&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An IAM role that extends limited access to your Amazon Web Services account to allow Amazon GameLift FleetIQ to create and interact with the Auto Scaling group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-iam-permissions-roles.html\&quot;&gt;Create IAM roles for cross-service interaction&lt;/a&gt; in the &lt;i&gt;Amazon GameLift FleetIQ Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To create a new game server group, specify a unique group name, IAM role and Amazon Elastic Compute Cloud launch template, and provide a list of instance types that can be used in the group. You must also set initial maximum and minimum limits on the group&#39;s instance count. You can optionally set an Auto Scaling policy with target tracking based on a Amazon GameLift FleetIQ metric.&lt;/p&gt; &lt;p&gt;Once the game server group and corresponding Auto Scaling group are created, you have full access to change the Auto Scaling group&#39;s configuration as needed. Several properties that are set when creating a game server group, including maximum/minimum size and auto-scaling policy settings, must be updated directly in the Auto Scaling group. Keep in mind that some Auto Scaling group properties are periodically updated by Amazon GameLift FleetIQ as part of its balancing activities to optimize for availability and cost.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = CreateGameServerGroupInput.from_dict(body)
    return web.Response(status=200)


async def create_game_session(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_game_session

    &lt;p&gt;Creates a multiplayer game session for players in a specific fleet location. This operation prompts an available server process to start a game session and retrieves connection information for the new game session. As an alternative, consider using the Amazon GameLift game session placement feature with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html\&quot;&gt;StartGameSessionPlacement&lt;/a&gt; , which uses FleetIQ algorithms and queues to optimize the placement process.&lt;/p&gt; &lt;p&gt;When creating a game session, you specify exactly where you want to place it and provide a set of game session configuration settings. The fleet must be in &lt;code&gt;ACTIVE&lt;/code&gt; status before a game session can be created in it. &lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To create a game session on an instance in a fleet&#39;s home Region, provide a fleet or alias ID along with your game session configuration. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To create a game session on an instance in a fleet&#39;s remote location, provide a fleet or alias ID and a location name, along with your game session configuration. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, a workflow is initiated to start a new game session. A &lt;code&gt;GameSession&lt;/code&gt; object is returned containing the game session configuration and status. When the status is &lt;code&gt;ACTIVE&lt;/code&gt;, game session connection information is provided and player sessions can be created for the game session. By default, newly created game sessions are open to new players. You can restrict new player access by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html\&quot;&gt;UpdateGameSession&lt;/a&gt; to change the game session&#39;s player session creation policy.&lt;/p&gt; &lt;p&gt;Game session logs are retained for all active game sessions for 14 days. To access the logs, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetGameSessionLogUrl.html\&quot;&gt;GetGameSessionLogUrl&lt;/a&gt; to download the log files.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Available in Amazon GameLift Local.&lt;/i&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession\&quot;&gt;Start a game session&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreateGameSessionInput.from_dict(body)
    return web.Response(status=200)


async def create_game_session_queue(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_game_session_queue

    &lt;p&gt;Creates a placement queue that processes requests for new game sessions. A queue uses FleetIQ algorithms to determine the best placement locations and find an available game server there, then prompts the game server process to start a new game session. &lt;/p&gt; &lt;p&gt;A game session queue is configured with a set of destinations (Amazon GameLift fleets or aliases), which determine the locations where the queue can place new game sessions. These destinations can span multiple fleet types (Spot and On-Demand), instance types, and Amazon Web Services Regions. If the queue includes multi-location fleets, the queue is able to place game sessions in all of a fleet&#39;s remote locations. You can opt to filter out individual locations if needed.&lt;/p&gt; &lt;p&gt;The queue configuration also determines how FleetIQ selects the best available placement for a new game session. Before searching for an available game server, FleetIQ first prioritizes the queue&#39;s destinations and locations, with the best placement locations on top. You can set up the queue to use the FleetIQ default prioritization or provide an alternate set of priorities.&lt;/p&gt; &lt;p&gt;To create a new queue, provide a name, timeout value, and a list of destinations. Optionally, specify a sort configuration and/or a filter, and define a set of latency cap policies. You can also include the ARN for an Amazon Simple Notification Service (SNS) topic to receive notifications of game session placement activity. Notifications using SNS or CloudWatch events is the preferred way to track placement activity.&lt;/p&gt; &lt;p&gt;If successful, a new &lt;code&gt;GameSessionQueue&lt;/code&gt; object is returned with an assigned queue ARN. New game session requests, which are submitted to queue with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html\&quot;&gt;StartGameSessionPlacement&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchmaking.html\&quot;&gt;StartMatchmaking&lt;/a&gt;, reference a queue&#39;s name or ARN. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-design.html\&quot;&gt; Design a game session queue&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-creating.html\&quot;&gt; Create a game session queue&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateGameSessionQueue.html\&quot;&gt;CreateGameSessionQueue&lt;/a&gt; | &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessionQueues.html\&quot;&gt;DescribeGameSessionQueues&lt;/a&gt; | &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSessionQueue.html\&quot;&gt;UpdateGameSessionQueue&lt;/a&gt; | &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteGameSessionQueue.html\&quot;&gt;DeleteGameSessionQueue&lt;/a&gt; | &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreateGameSessionQueueInput.from_dict(body)
    return web.Response(status=200)


async def create_location(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location

    Creates a custom location for use in an Anywhere fleet.

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
    body = CreateLocationInput.from_dict(body)
    return web.Response(status=200)


async def create_matchmaking_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_matchmaking_configuration

    &lt;p&gt;Defines a new matchmaking configuration for use with FlexMatch. Whether your are using FlexMatch with Amazon GameLift hosting or as a standalone matchmaking service, the matchmaking configuration sets out rules for matching players and forming teams. If you&#39;re also using Amazon GameLift hosting, it defines how to start game sessions for each match. Your matchmaking system can use multiple configurations to handle different game scenarios. All matchmaking requests identify the matchmaking configuration to use and provide player attributes consistent with that configuration. &lt;/p&gt; &lt;p&gt;To create a matchmaking configuration, you must provide the following: configuration name and FlexMatch mode (with or without Amazon GameLift hosting); a rule set that specifies how to evaluate players and find acceptable matches; whether player acceptance is required; and the maximum time allowed for a matchmaking attempt. When using FlexMatch with Amazon GameLift hosting, you also need to identify the game session queue to use when starting a game session for the match.&lt;/p&gt; &lt;p&gt;In addition, you must set up an Amazon Simple Notification Service topic to receive matchmaking notifications. Provide the topic ARN in the matchmaking configuration.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html\&quot;&gt; Design a FlexMatch matchmaker&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html\&quot;&gt; Set up FlexMatch event notification&lt;/a&gt; &lt;/p&gt;

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
    body = CreateMatchmakingConfigurationInput.from_dict(body)
    return web.Response(status=200)


async def create_matchmaking_rule_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_matchmaking_rule_set

    &lt;p&gt;Creates a new rule set for FlexMatch matchmaking. A rule set describes the type of match to create, such as the number and size of teams. It also sets the parameters for acceptable player matches, such as minimum skill level or character type.&lt;/p&gt; &lt;p&gt;To create a matchmaking rule set, provide unique rule set name and the rule set body in JSON format. Rule sets must be defined in the same Region as the matchmaking configuration they are used with.&lt;/p&gt; &lt;p&gt;Since matchmaking rule sets cannot be edited, it is a good idea to check the rule set syntax using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_ValidateMatchmakingRuleSet.html\&quot;&gt;ValidateMatchmakingRuleSet&lt;/a&gt; before creating a new rule set.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html\&quot;&gt;Build a rule set&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html\&quot;&gt;Design a matchmaker&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-intro.html\&quot;&gt;Matchmaking with FlexMatch&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateMatchmakingRuleSetInput.from_dict(body)
    return web.Response(status=200)


async def create_player_session(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_player_session

    &lt;p&gt;Reserves an open player slot in a game session for a player. New player sessions can be created in any game session with an open slot that is in &lt;code&gt;ACTIVE&lt;/code&gt; status and has a player creation policy of &lt;code&gt;ACCEPT_ALL&lt;/code&gt;. You can add a group of players to a game session with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreatePlayerSessions.html\&quot;&gt;CreatePlayerSessions&lt;/a&gt; . &lt;/p&gt; &lt;p&gt;To create a player session, specify a game session ID, player ID, and optionally a set of player data. &lt;/p&gt; &lt;p&gt;If successful, a slot is reserved in the game session for the player and a new &lt;code&gt;PlayerSessions&lt;/code&gt; object is returned with a player session ID. The player references the player session ID when sending a connection request to the game session, and the game server can use it to validate the player reservation with the Amazon GameLift service. Player sessions cannot be updated. &lt;/p&gt; &lt;p&gt;The maximum number of players per game session is 200. It is not adjustable. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreatePlayerSessionInput.from_dict(body)
    return web.Response(status=200)


async def create_player_sessions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_player_sessions

    &lt;p&gt;Reserves open slots in a game session for a group of players. New player sessions can be created in any game session with an open slot that is in &lt;code&gt;ACTIVE&lt;/code&gt; status and has a player creation policy of &lt;code&gt;ACCEPT_ALL&lt;/code&gt;. To add a single player to a game session, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreatePlayerSession.html\&quot;&gt;CreatePlayerSession&lt;/a&gt; &lt;/p&gt; &lt;p&gt;To create player sessions, specify a game session ID and a list of player IDs. Optionally, provide a set of player data for each player ID. &lt;/p&gt; &lt;p&gt;If successful, a slot is reserved in the game session for each player, and new &lt;code&gt;PlayerSession&lt;/code&gt; objects are returned with player session IDs. Each player references their player session ID when sending a connection request to the game session, and the game server can use it to validate the player reservation with the Amazon GameLift service. Player sessions cannot be updated.&lt;/p&gt; &lt;p&gt;The maximum number of players per game session is 200. It is not adjustable. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreatePlayerSessionsInput.from_dict(body)
    return web.Response(status=200)


async def create_script(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_script

    &lt;p&gt;Creates a new script record for your Realtime Servers script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session. &lt;/p&gt; &lt;p&gt;To create a new script record, specify a script name and provide the script file(s). The script files and all dependencies must be zipped into a single file. You can pull the zip file from either of these locations: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A locally available directory. Use the &lt;i&gt;ZipFile&lt;/i&gt; parameter for this option.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An Amazon Simple Storage Service (Amazon S3) bucket under your Amazon Web Services account. Use the &lt;i&gt;StorageLocation&lt;/i&gt; parameter for this option. You&#39;ll need to have an Identity Access Management (IAM) role that allows the Amazon GameLift service to access your S3 bucket. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If the call is successful, a new script record is created with a unique script ID. If the script file is provided as a local file, the file is uploaded to an Amazon GameLift-owned S3 bucket and the script record&#39;s storage location reflects this location. If the script file is provided as an S3 bucket, Amazon GameLift accesses the file at this storage location as needed for deployment.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html\&quot;&gt;Amazon GameLift Realtime Servers&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html\&quot;&gt;Set Up a Role for Amazon GameLift Access&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreateScriptInput.from_dict(body)
    return web.Response(status=200)


async def create_vpc_peering_authorization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vpc_peering_authorization

    &lt;p&gt;Requests authorization to create or delete a peer connection between the VPC for your Amazon GameLift fleet and a virtual private cloud (VPC) in your Amazon Web Services account. VPC peering enables the game servers on your fleet to communicate directly with other Amazon Web Services resources. After you&#39;ve received authorization, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringConnection.html\&quot;&gt;CreateVpcPeeringConnection&lt;/a&gt; to establish the peering connection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html\&quot;&gt;VPC Peering with Amazon GameLift Fleets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can peer with VPCs that are owned by any Amazon Web Services account you have access to, including the account that you use to manage your Amazon GameLift fleets. You cannot peer with VPCs that are in different Regions.&lt;/p&gt; &lt;p&gt;To request authorization to create a connection, call this operation from the Amazon Web Services account with the VPC that you want to peer to your Amazon GameLift fleet. For example, to enable your game servers to retrieve data from a DynamoDB table, use the account that manages that DynamoDB resource. Identify the following values: (1) The ID of the VPC that you want to peer with, and (2) the ID of the Amazon Web Services account that you use to manage Amazon GameLift. If successful, VPC peering is authorized for the specified VPC. &lt;/p&gt; &lt;p&gt;To request authorization to delete a connection, call this operation from the Amazon Web Services account with the VPC that is peered with your Amazon GameLift fleet. Identify the following values: (1) VPC ID that you want to delete the peering connection for, and (2) ID of the Amazon Web Services account that you use to manage Amazon GameLift. &lt;/p&gt; &lt;p&gt;The authorization remains valid for 24 hours unless it is canceled. You must create or delete the peering connection while the authorization is valid. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreateVpcPeeringAuthorizationInput.from_dict(body)
    return web.Response(status=200)


async def create_vpc_peering_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vpc_peering_connection

    &lt;p&gt;Establishes a VPC peering connection between a virtual private cloud (VPC) in an Amazon Web Services account with the VPC for your Amazon GameLift fleet. VPC peering enables the game servers on your fleet to communicate directly with other Amazon Web Services resources. You can peer with VPCs in any Amazon Web Services account that you have access to, including the account that you use to manage your Amazon GameLift fleets. You cannot peer with VPCs that are in different Regions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html\&quot;&gt;VPC Peering with Amazon GameLift Fleets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Before calling this operation to establish the peering connection, you first need to use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.html\&quot;&gt;CreateVpcPeeringAuthorization&lt;/a&gt; and identify the VPC you want to peer with. Once the authorization for the specified VPC is issued, you have 24 hours to establish the connection. These two operations handle all tasks necessary to peer the two VPCs, including acceptance, updating routing tables, etc. &lt;/p&gt; &lt;p&gt;To establish the connection, call this operation from the Amazon Web Services account that is used to manage the Amazon GameLift fleets. Identify the following values: (1) The ID of the fleet you want to be enable a VPC peering connection for; (2) The Amazon Web Services account with the VPC that you want to peer with; and (3) The ID of the VPC you want to peer with. This operation is asynchronous. If successful, a connection request is created. You can use continuous polling to track the request&#39;s status using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeVpcPeeringConnections.html\&quot;&gt;DescribeVpcPeeringConnections&lt;/a&gt; , or by monitoring fleet events for success or failure using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetEvents.html\&quot;&gt;DescribeFleetEvents&lt;/a&gt; . &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = CreateVpcPeeringConnectionInput.from_dict(body)
    return web.Response(status=200)


async def delete_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_alias

    &lt;p&gt;Deletes an alias. This operation removes all record of the alias. Game clients attempting to access a server process using the deleted alias receive an error. To delete an alias, specify the alias ID to be deleted.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteAliasInput.from_dict(body)
    return web.Response(status=200)


async def delete_build(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_build

    &lt;p&gt;Deletes a build. This operation permanently deletes the build resource and any uploaded build files. Deleting a build does not affect the status of any active fleets using the build, but you can no longer create new fleets with the deleted build.&lt;/p&gt; &lt;p&gt;To delete a build, specify the build ID. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html\&quot;&gt; Upload a Custom Server Build&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteBuildInput.from_dict(body)
    return web.Response(status=200)


async def delete_fleet(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_fleet

    &lt;p&gt;Deletes all resources and information related a fleet. Any current fleet instances, including those in remote locations, are shut down. You don&#39;t need to call &lt;code&gt;DeleteFleetLocations&lt;/code&gt; separately.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the fleet being deleted has a VPC peering connection, you first need to get a valid authorization (good for 24 hours) by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.html\&quot;&gt;CreateVpcPeeringAuthorization&lt;/a&gt;. You do not need to explicitly delete the VPC peering connection.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To delete a fleet, specify the fleet ID to be terminated. During the deletion process the fleet status is changed to &lt;code&gt;DELETING&lt;/code&gt;. When completed, the status switches to &lt;code&gt;TERMINATED&lt;/code&gt; and the fleet event &lt;code&gt;FLEET_DELETED&lt;/code&gt; is sent.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift Fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteFleetInput.from_dict(body)
    return web.Response(status=200)


async def delete_fleet_locations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_fleet_locations

    &lt;p&gt;Removes locations from a multi-location fleet. When deleting a location, all game server process and all instances that are still active in the location are shut down. &lt;/p&gt; &lt;p&gt;To delete fleet locations, identify the fleet ID and provide a list of the locations to be deleted. &lt;/p&gt; &lt;p&gt;If successful, GameLift sets the location status to &lt;code&gt;DELETING&lt;/code&gt;, and begins to shut down existing server processes and terminate instances in each location being deleted. When completed, the location status changes to &lt;code&gt;TERMINATED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteFleetLocationsInput.from_dict(body)
    return web.Response(status=200)


async def delete_game_server_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_game_server_group

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Terminates a game server group and permanently deletes the game server group record. You have several options for how these resources are impacted when deleting the game server group. Depending on the type of delete operation selected, this operation might affect these resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The game server group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The corresponding Auto Scaling group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All game servers that are currently running in the group&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To delete a game server group, identify the game server group to delete and specify the type of delete operation to initiate. Game server groups can only be deleted if they are in &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;ERROR&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt;If the delete request is successful, a series of operations are kicked off. The game server group status is changed to &lt;code&gt;DELETE_SCHEDULED&lt;/code&gt;, which prevents new game servers from being registered and stops automatic scaling activity. Once all game servers in the game server group are deregistered, Amazon GameLift FleetIQ can begin deleting resources. If any of the delete operations fail, the game server group is placed in &lt;code&gt;ERROR&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt;Amazon GameLift FleetIQ emits delete events to Amazon CloudWatch.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteGameServerGroupInput.from_dict(body)
    return web.Response(status=200)


async def delete_game_session_queue(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_game_session_queue

    Deletes a game session queue. Once a queue is successfully deleted, unfulfilled &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html\&quot;&gt;StartGameSessionPlacement&lt;/a&gt; requests that reference the queue will fail. To delete a queue, specify the queue name.

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
    body = DeleteGameSessionQueueInput.from_dict(body)
    return web.Response(status=200)


async def delete_location(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_location

    &lt;p&gt;Deletes a custom location.&lt;/p&gt; &lt;p&gt;Before deleting a custom location, review any fleets currently using the custom location and deregister the location if it is in use. For more information see, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeregisterCompute.html\&quot;&gt;DeregisterCompute&lt;/a&gt;.&lt;/p&gt;

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
    body = DeleteLocationInput.from_dict(body)
    return web.Response(status=200)


async def delete_matchmaking_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_matchmaking_configuration

    Permanently removes a FlexMatch matchmaking configuration. To delete, specify the configuration name. A matchmaking configuration cannot be deleted if it is being used in any active matchmaking tickets.

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
    body = DeleteMatchmakingConfigurationInput.from_dict(body)
    return web.Response(status=200)


async def delete_matchmaking_rule_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_matchmaking_rule_set

    &lt;p&gt;Deletes an existing matchmaking rule set. To delete the rule set, provide the rule set name. Rule sets cannot be deleted if they are currently being used by a matchmaking configuration. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html\&quot;&gt;Build a rule set&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DeleteMatchmakingRuleSetInput.from_dict(body)
    return web.Response(status=200)


async def delete_scaling_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_scaling_policy

    &lt;p&gt;Deletes a fleet scaling policy. Once deleted, the policy is no longer in force and Amazon GameLift removes all record of it. To delete a scaling policy, specify both the scaling policy name and the fleet ID it is associated with.&lt;/p&gt; &lt;p&gt;To temporarily suspend scaling policies, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html\&quot;&gt;StopFleetActions&lt;/a&gt;. This operation suspends all policies for the fleet.&lt;/p&gt;

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
    body = DeleteScalingPolicyInput.from_dict(body)
    return web.Response(status=200)


async def delete_script(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_script

    &lt;p&gt;Deletes a Realtime script. This operation permanently deletes the script record. If script files were uploaded, they are also deleted (files stored in an S3 bucket are not deleted). &lt;/p&gt; &lt;p&gt;To delete a script, specify the script ID. Before deleting a script, be sure to terminate all fleets that are deployed with the script being deleted. Fleet instances periodically check for script updates, and if the script record no longer exists, the instance will go into an error state and be unable to host game sessions.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html\&quot;&gt;Amazon GameLift Realtime Servers&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteScriptInput.from_dict(body)
    return web.Response(status=200)


async def delete_vpc_peering_authorization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vpc_peering_authorization

    &lt;p&gt;Cancels a pending VPC peering authorization for the specified VPC. If you need to delete an existing VPC peering connection, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteVpcPeeringConnection.html\&quot;&gt;DeleteVpcPeeringConnection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteVpcPeeringAuthorizationInput.from_dict(body)
    return web.Response(status=200)


async def delete_vpc_peering_connection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vpc_peering_connection

    &lt;p&gt;Removes a VPC peering connection. To delete the connection, you must have a valid authorization for the VPC peering connection that you want to delete.. &lt;/p&gt; &lt;p&gt;Once a valid authorization exists, call this operation from the Amazon Web Services account that is used to manage the Amazon GameLift fleets. Identify the connection to delete by the connection ID and fleet ID. If successful, the connection is removed. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DeleteVpcPeeringConnectionInput.from_dict(body)
    return web.Response(status=200)


async def deregister_compute(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_compute

    Removes a compute resource from the specified fleet. Deregister your compute resources before you delete the compute.

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
    body = DeregisterComputeInput.from_dict(body)
    return web.Response(status=200)


async def deregister_game_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_game_server

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Removes the game server from a game server group. As a result of this operation, the deregistered game server can no longer be claimed and will not be returned in a list of active game servers. &lt;/p&gt; &lt;p&gt;To deregister a game server, specify the game server group and game server ID. If successful, this operation emits a CloudWatch event with termination timestamp and reason.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = DeregisterGameServerInput.from_dict(body)
    return web.Response(status=200)


async def describe_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_alias

    &lt;p&gt;Retrieves properties for an alias. This operation returns all alias metadata and settings. To get an alias&#39;s target fleet ID only, use &lt;code&gt;ResolveAlias&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;To get alias properties, specify the alias ID. If successful, the requested alias record is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeAliasInput.from_dict(body)
    return web.Response(status=200)


async def describe_build(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_build

    &lt;p&gt;Retrieves properties for a custom game build. To request a build resource, specify a build ID. If successful, an object containing the build properties is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html\&quot;&gt; Upload a Custom Server Build&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeBuildInput.from_dict(body)
    return web.Response(status=200)


async def describe_compute(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_compute

    Retrieves properties for a compute resource. To request a compute resource specify the fleet ID and compute name. If successful, Amazon GameLift returns an object containing the build properties.

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
    body = DescribeComputeInput.from_dict(body)
    return web.Response(status=200)


async def describe_ec2_instance_limits(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_ec2_instance_limits

    &lt;p&gt;Retrieves the instance limits and current utilization for an Amazon Web Services Region or location. Instance limits control the number of instances, per instance type, per location, that your Amazon Web Services account can use. Learn more at &lt;a href&#x3D;\&quot;http://aws.amazon.com/ec2/instance-types/\&quot;&gt;Amazon EC2 Instance Types&lt;/a&gt;. The information returned includes the maximum number of instances allowed and your account&#39;s current usage across all fleets. This information can affect your ability to scale your Amazon GameLift fleets. You can request a limit increase for your account by using the &lt;b&gt;Service limits&lt;/b&gt; page in the Amazon GameLift console.&lt;/p&gt; &lt;p&gt;Instance limits differ based on whether the instances are deployed in a fleet&#39;s home Region or in a remote location. For remote locations, limits also differ based on the combination of home Region and remote location. All requests must specify an Amazon Web Services Region (either explicitly or as your default settings). To get the limit for a remote location, you must also specify the location. For example, the following requests all return different results: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Request specifies the Region &lt;code&gt;ap-northeast-1&lt;/code&gt; with no location. The result is limits and usage data on all instance types that are deployed in &lt;code&gt;us-east-2&lt;/code&gt;, by all of the fleets that reside in &lt;code&gt;ap-northeast-1&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Request specifies the Region &lt;code&gt;us-east-1&lt;/code&gt; with location &lt;code&gt;ca-central-1&lt;/code&gt;. The result is limits and usage data on all instance types that are deployed in &lt;code&gt;ca-central-1&lt;/code&gt;, by all of the fleets that reside in &lt;code&gt;us-east-2&lt;/code&gt;. These limits do not affect fleets in any other Regions that deploy instances to &lt;code&gt;ca-central-1&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Request specifies the Region &lt;code&gt;eu-west-1&lt;/code&gt; with location &lt;code&gt;ca-central-1&lt;/code&gt;. The result is limits and usage data on all instance types that are deployed in &lt;code&gt;ca-central-1&lt;/code&gt;, by all of the fleets that reside in &lt;code&gt;eu-west-1&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation can be used in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To get limit and usage data for all instance types that are deployed in an Amazon Web Services Region by fleets that reside in the same Region: Specify the Region only. Optionally, specify a single instance type to retrieve information for.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get limit and usage data for all instance types that are deployed to a remote location by fleets that reside in different Amazon Web Services Region: Provide both the Amazon Web Services Region and the remote location. Optionally, specify a single instance type to retrieve information for.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, an &lt;code&gt;EC2InstanceLimits&lt;/code&gt; object is returned with limits and usage data for each requested instance type.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeEC2InstanceLimitsInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_fleet_attributes

    &lt;p&gt;Retrieves core fleet-wide properties, including the computing hardware and deployment configuration for all instances in the fleet.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To get attributes for one or more specific fleets, provide a list of fleet IDs or fleet ARNs. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get attributes for all fleets, do not provide a fleet identifier. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When requesting attributes for multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;FleetAttributes&lt;/code&gt; object is returned for each fleet requested, unless the fleet identifier is not found. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Some API operations limit the number of fleet IDs that allowed in one request. If a request exceeds this limit, the request fails and the error message contains the maximum allowed number.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetAttributesInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_capacity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_fleet_capacity

    &lt;p&gt;Retrieves the resource capacity settings for one or more fleets. The data returned includes the current fleet capacity (number of EC2 instances), and settings that can control how capacity scaling. For fleets with remote locations, this operation retrieves data for the fleet&#39;s home Region only.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To get capacity data for one or more specific fleets, provide a list of fleet IDs or fleet ARNs. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get capacity data for all fleets, do not provide a fleet identifier. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;FleetCapacity&lt;/code&gt; object is returned for each requested fleet ID. Each FleetCapacity object includes a &lt;code&gt;Location&lt;/code&gt; property, which is set to the fleet&#39;s home Region. When a list of fleet IDs is provided, attribute objects are returned only for fleets that currently exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Some API operations may limit the number of fleet IDs that are allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet\&quot;&gt;GameLift metrics for fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetCapacityInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_fleet_events

    &lt;p&gt;Retrieves entries from a fleet&#39;s event log. Fleet events are initiated by changes in status, such as during fleet creation and termination, changes in capacity, etc. If a fleet has multiple locations, events are also initiated by changes to status and capacity in remote locations. &lt;/p&gt; &lt;p&gt;You can specify a time range to limit the result set. Use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a collection of event log entries matching the request are returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetEventsInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_location_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_fleet_location_attributes

    &lt;p&gt;Retrieves information on a fleet&#39;s remote locations, including life-cycle status and any suspended fleet activity. &lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To get data for specific locations, provide a fleet identifier and a list of locations. Location data is returned in the order that it is requested. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get data for all locations, provide a fleet identifier only. Location data is returned in no particular order. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When requesting attributes for multiple locations, use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;LocationAttributes&lt;/code&gt; object is returned for each requested location. If the fleet does not have a requested location, no information is returned. This operation does not return the home Region. To get information on a fleet&#39;s home Region, call &lt;code&gt;DescribeFleetAttributes&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetLocationAttributesInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_location_capacity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_fleet_location_capacity

    &lt;p&gt;Retrieves the resource capacity settings for a fleet location. The data returned includes the current capacity (number of EC2 instances) and some scaling settings for the requested fleet location. Use this operation to retrieve capacity information for a fleet&#39;s remote location or home Region (you can also retrieve home Region capacity by calling &lt;code&gt;DescribeFleetCapacity&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;To retrieve capacity data, identify a fleet and location. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;FleetCapacity&lt;/code&gt; object is returned for the requested fleet location. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet\&quot;&gt;GameLift metrics for fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetLocationCapacityInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_location_utilization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_fleet_location_utilization

    &lt;p&gt;Retrieves current usage data for a fleet location. Utilization data provides a snapshot of current game hosting activity at the requested location. Use this operation to retrieve utilization information for a fleet&#39;s remote location or home Region (you can also retrieve home Region utilization by calling &lt;code&gt;DescribeFleetUtilization&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;To retrieve utilization data, identify a fleet and location. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;FleetUtilization&lt;/code&gt; object is returned for the requested fleet location. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet\&quot;&gt;GameLift metrics for fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetLocationUtilizationInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_port_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_fleet_port_settings

    &lt;p&gt;Retrieves a fleet&#39;s inbound connection permissions. Connection permissions specify the range of IP addresses and port settings that incoming traffic can use to access server processes in the fleet. Game sessions that are running on instances in the fleet must use connections that fall in this range.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To retrieve the inbound connection permissions for a fleet, identify the fleet&#39;s unique identifier. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To check the status of recent updates to a fleet remote location, specify the fleet ID and a location. Port setting updates can take time to propagate across all locations. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, a set of &lt;code&gt;IpPermission&lt;/code&gt; objects is returned for the requested fleet ID. When a location is specified, a pending status is included. If the requested fleet has been deleted, the result set is empty.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetPortSettingsInput.from_dict(body)
    return web.Response(status=200)


async def describe_fleet_utilization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_fleet_utilization

    &lt;p&gt;Retrieves utilization statistics for one or more fleets. Utilization data provides a snapshot of how the fleet&#39;s hosting resources are currently being used. For fleets with remote locations, this operation retrieves data for the fleet&#39;s home Region only. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationUtilization.html\&quot;&gt;DescribeFleetLocationUtilization&lt;/a&gt; to get utilization statistics for a fleet&#39;s remote locations.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To get utilization data for one or more specific fleets, provide a list of fleet IDs or fleet ARNs. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get utilization data for all fleets, do not provide a fleet identifier. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_FleetUtilization.html\&quot;&gt;FleetUtilization&lt;/a&gt; object is returned for each requested fleet ID, unless the fleet identifier is not found. Each fleet utilization object includes a &lt;code&gt;Location&lt;/code&gt; property, which is set to the fleet&#39;s home Region. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Some API operations may limit the number of fleet IDs allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift Fleets&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet\&quot;&gt;GameLift Metrics for Fleets&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeFleetUtilizationInput.from_dict(body)
    return web.Response(status=200)


async def describe_game_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_game_server

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Retrieves information for a registered game server. Information includes game server status, health check info, and the instance that the game server is running on. &lt;/p&gt; &lt;p&gt;To retrieve game server information, specify the game server ID. If successful, the requested game server object is returned. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeGameServerInput.from_dict(body)
    return web.Response(status=200)


async def describe_game_server_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_game_server_group

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Retrieves information on a game server group. This operation returns only properties related to Amazon GameLift FleetIQ. To view or update properties for the corresponding Auto Scaling group, such as launch template, auto scaling policies, and maximum/minimum group size, access the Auto Scaling group directly.&lt;/p&gt; &lt;p&gt;To get attributes for a game server group, provide a group name or ARN value. If successful, a &lt;code&gt;GameServerGroup&lt;/code&gt; object is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeGameServerGroupInput.from_dict(body)
    return web.Response(status=200)


async def describe_game_server_instances(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_game_server_instances

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Retrieves status information about the Amazon EC2 instances associated with a Amazon GameLift FleetIQ game server group. Use this operation to detect when instances are active or not available to host new game servers.&lt;/p&gt; &lt;p&gt;To request status for all instances in the game server group, provide a game server group ID only. To request status for specific instances, provide the game server group ID and one or more instance IDs. Use the pagination parameters to retrieve results in sequential segments. If successful, a collection of &lt;code&gt;GameServerInstance&lt;/code&gt; objects is returned. &lt;/p&gt; &lt;p&gt;This operation is not designed to be called with every game server claim request; this practice can cause you to exceed your API limit, which results in errors. Instead, as a best practice, cache the results and refresh your cache no more than once every 10 seconds.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeGameServerInstancesInput.from_dict(body)
    return web.Response(status=200)


async def describe_game_session_details(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_game_session_details

    &lt;p&gt;Retrieves additional game session properties, including the game session protection policy in force, a set of one or more game sessions in a specific fleet location. You can optionally filter the results by current game session status.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To retrieve details for all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID, with an optional status filter. This approach returns details from the fleet&#39;s home Region and all remote locations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To retrieve details for all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name, with optional status filter. The location can be the fleet&#39;s home Region or any remote location.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To retrieve details for a specific game session, provide the game session ID. This approach looks for the game session ID in all fleets that reside in the Amazon Web Services Region defined in the request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;GameSessionDetail&lt;/code&gt; object is returned for each game session that matches the request.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-find\&quot;&gt;Find a game session&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeGameSessionDetailsInput.from_dict(body)
    return web.Response(status=200)


async def describe_game_session_placement(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_game_session_placement

    &lt;p&gt;Retrieves information, including current status, about a game session placement request. &lt;/p&gt; &lt;p&gt;To get game session placement details, specify the placement ID.&lt;/p&gt; &lt;p&gt;This operation is not designed to be continually called to track game session status. This practice can cause you to exceed your API limit, which results in errors. Instead, you must configure configure an Amazon Simple Notification Service (SNS) topic to receive notifications from FlexMatch or queues. Continuously polling with &lt;code&gt;DescribeGameSessionPlacement&lt;/code&gt; should only be used for games in development with low game session usage. &lt;/p&gt;

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
    body = DescribeGameSessionPlacementInput.from_dict(body)
    return web.Response(status=200)


async def describe_game_session_queues(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_game_session_queues

    &lt;p&gt;Retrieves the properties for one or more game session queues. When requesting multiple queues, use the pagination parameters to retrieve results as a set of sequential pages. When specifying a list of queues, objects are returned only for queues that currently exist in the Region.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-console.html\&quot;&gt; View Your Queues&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeGameSessionQueuesInput.from_dict(body)
    return web.Response(status=200)


async def describe_game_sessions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_game_sessions

    &lt;p&gt;Retrieves a set of one or more game sessions in a specific fleet location. You can optionally filter the results by current game session status.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To retrieve all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID, with an optional status filter. This approach returns all game sessions in the fleet&#39;s home Region and all remote locations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To retrieve all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name, with optional status filter. The location can be the fleet&#39;s home Region or any remote location.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To retrieve a specific game session, provide the game session ID. This approach looks for the game session ID in all fleets that reside in the Amazon Web Services Region defined in the request.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;GameSession&lt;/code&gt; object is returned for each game session that matches the request.&lt;/p&gt; &lt;p&gt;This operation is not designed to be continually called to track game session status. This practice can cause you to exceed your API limit, which results in errors. Instead, you must configure an Amazon Simple Notification Service (SNS) topic to receive notifications from FlexMatch or queues. Continuously polling with &lt;code&gt;DescribeGameSessions&lt;/code&gt; should only be used for games in development with low game session usage. &lt;/p&gt; &lt;p&gt; &lt;i&gt;Available in Amazon GameLift Local.&lt;/i&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-find\&quot;&gt;Find a game session&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeGameSessionsInput.from_dict(body)
    return web.Response(status=200)


async def describe_instances(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_instances

    &lt;p&gt;Retrieves information about a fleet&#39;s instances, including instance IDs, connection data, and status. &lt;/p&gt; &lt;p&gt;This operation can be used in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To get information on all instances that are deployed to a fleet&#39;s home Region, provide the fleet ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get information on all instances that are deployed to a fleet&#39;s remote location, provide the fleet ID and location name.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get information on a specific instance in a fleet, provide the fleet ID and instance ID.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, an &lt;code&gt;Instance&lt;/code&gt; object is returned for each requested instance. Instances are not returned in any particular order. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html\&quot;&gt;Remotely Access Fleet Instances&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html\&quot;&gt;Debug Fleet Issues&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeInstancesInput.from_dict(body)
    return web.Response(status=200)


async def describe_matchmaking(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_matchmaking

    &lt;p&gt;Retrieves one or more matchmaking tickets. Use this operation to retrieve ticket information, including--after a successful match is made--connection information for the resulting new game session. &lt;/p&gt; &lt;p&gt;To request matchmaking tickets, provide a list of up to 10 ticket IDs. If the request is successful, a ticket object is returned for each requested ID that currently exists.&lt;/p&gt; &lt;p&gt;This operation is not designed to be continually called to track matchmaking ticket status. This practice can cause you to exceed your API limit, which results in errors. Instead, as a best practice, set up an Amazon Simple Notification Service to receive notifications, and provide the topic ARN in the matchmaking configuration.&lt;/p&gt; &lt;p/&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html\&quot;&gt; Add FlexMatch to a game client&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html\&quot;&gt; Set Up FlexMatch event notification&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeMatchmakingInput.from_dict(body)
    return web.Response(status=200)


async def describe_matchmaking_configurations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_matchmaking_configurations

    &lt;p&gt;Retrieves the details of FlexMatch matchmaking configurations. &lt;/p&gt; &lt;p&gt;This operation offers the following options: (1) retrieve all matchmaking configurations, (2) retrieve configurations for a specified list, or (3) retrieve all configurations that use a specified rule set name. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a configuration is returned for each requested name. When specifying a list of names, only configurations that currently exist are returned. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/matchmaker-build.html\&quot;&gt; Setting up FlexMatch matchmakers&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeMatchmakingConfigurationsInput.from_dict(body)
    return web.Response(status=200)


async def describe_matchmaking_rule_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_matchmaking_rule_sets

    &lt;p&gt;Retrieves the details for FlexMatch matchmaking rule sets. You can request all existing rule sets for the Region, or provide a list of one or more rule set names. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a rule set is returned for each requested name. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html\&quot;&gt;Build a rule set&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = DescribeMatchmakingRuleSetsInput.from_dict(body)
    return web.Response(status=200)


async def describe_player_sessions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_player_sessions

    &lt;p&gt;Retrieves properties for one or more player sessions. &lt;/p&gt; &lt;p&gt;This action can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To retrieve a specific player session, provide the player session ID only.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To retrieve all player sessions in a game session, provide the game session ID only.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To retrieve all player sessions for a specific player, provide a player ID only.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To request player sessions, specify either a player session ID, game session ID, or player ID. You can filter this request by player session status. Use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;PlayerSession&lt;/code&gt; object is returned for each session that matches the request.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribePlayerSessionsInput.from_dict(body)
    return web.Response(status=200)


async def describe_runtime_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_runtime_configuration

    &lt;p&gt;Retrieves a fleet&#39;s runtime configuration settings. The runtime configuration tells Amazon GameLift which server processes to run (and how) on each instance in the fleet.&lt;/p&gt; &lt;p&gt;To get the runtime configuration that is currently in forces for a fleet, provide the fleet ID. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;RuntimeConfiguration&lt;/code&gt; object is returned for the requested fleet. If the requested fleet has been deleted, the result set is empty.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html\&quot;&gt;Running multiple processes on a fleet&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeRuntimeConfigurationInput.from_dict(body)
    return web.Response(status=200)


async def describe_scaling_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """describe_scaling_policies

    &lt;p&gt;Retrieves all scaling policies applied to a fleet.&lt;/p&gt; &lt;p&gt;To get a fleet&#39;s scaling policies, specify the fleet ID. You can filter this request by policy status, such as to retrieve only active scaling policies. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, set of &lt;code&gt;ScalingPolicy&lt;/code&gt; objects is returned for the fleet.&lt;/p&gt; &lt;p&gt;A fleet may have all of its scaling policies suspended. This operation does not affect the status of the scaling policies, which remains ACTIVE.&lt;/p&gt;

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
    body = DescribeScalingPoliciesInput.from_dict(body)
    return web.Response(status=200)


async def describe_script(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_script

    &lt;p&gt;Retrieves properties for a Realtime script. &lt;/p&gt; &lt;p&gt;To request a script record, specify the script ID. If successful, an object containing the script properties is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html\&quot;&gt;Amazon GameLift Realtime Servers&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeScriptInput.from_dict(body)
    return web.Response(status=200)


async def describe_vpc_peering_authorizations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_vpc_peering_authorizations

    &lt;p&gt;Retrieves valid VPC peering authorizations that are pending for the Amazon Web Services account. This operation returns all VPC peering authorizations and requests for peering. This includes those initiated and received by this account. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_vpc_peering_connections(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_vpc_peering_connections

    &lt;p&gt;Retrieves information on VPC peering connections. Use this operation to get peering information for all fleets or for one specific fleet ID. &lt;/p&gt; &lt;p&gt;To retrieve connection information, call this operation from the Amazon Web Services account that is used to manage the Amazon GameLift fleets. Specify a fleet ID or leave the parameter empty to retrieve all connection records. If successful, the retrieved information includes both active and pending connections. Active connections identify the IpV4 CIDR block that the VPC uses to connect. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = DescribeVpcPeeringConnectionsInput.from_dict(body)
    return web.Response(status=200)


async def get_compute_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_compute_access

    &lt;p&gt;Requests remote access to a fleet instance. Remote access is useful for debugging, gathering benchmarking data, or observing activity in real time. &lt;/p&gt; &lt;p&gt;To remotely access an instance, you need credentials that match the operating system of the instance. For a Windows instance, Amazon GameLift returns a user name and password as strings for use with a Windows Remote Desktop client. For a Linux instance, Amazon GameLift returns a user name and RSA private key, also as strings, for use with an SSH client. The private key must be saved in the proper format to a &lt;code&gt;.pem&lt;/code&gt; file before using. If you&#39;re making this request using the CLI, saving the secret can be handled as part of the &lt;code&gt;GetInstanceAccess&lt;/code&gt; request, as shown in one of the examples for this operation. &lt;/p&gt; &lt;p&gt;To request access to a specific instance, specify the IDs of both the instance and the fleet it belongs to.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html\&quot;&gt;Remotely Access Fleet Instances&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html\&quot;&gt;Debug Fleet Issues&lt;/a&gt; &lt;/p&gt;

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
    body = GetComputeAccessInput.from_dict(body)
    return web.Response(status=200)


async def get_compute_auth_token(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_compute_auth_token

    Requests an authentication token from Amazon GameLift. The authentication token is used by your game server to authenticate with Amazon GameLift. Each authentication token has an expiration time. To continue using the compute resource to host your game server, regularly retrieve a new authorization token.

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
    body = GetComputeAuthTokenInput.from_dict(body)
    return web.Response(status=200)


async def get_game_session_log_url(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_game_session_log_url

    &lt;p&gt;Retrieves the location of stored game session logs for a specified game session on Amazon GameLift managed fleets. When a game session is terminated, Amazon GameLift automatically stores the logs in Amazon S3 and retains them for 14 days. Use this URL to download the logs.&lt;/p&gt; &lt;note&gt; &lt;p&gt;See the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_gamelift\&quot;&gt;Amazon Web Services Service Limits&lt;/a&gt; page for maximum log file sizes. Log files that exceed this limit are not saved.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = GetGameSessionLogUrlInput.from_dict(body)
    return web.Response(status=200)


async def get_instance_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_instance_access

    &lt;p&gt;Requests remote access to a fleet instance. Remote access is useful for debugging, gathering benchmarking data, or observing activity in real time. &lt;/p&gt; &lt;p&gt;To remotely access an instance, you need credentials that match the operating system of the instance. For a Windows instance, Amazon GameLift returns a user name and password as strings for use with a Windows Remote Desktop client. For a Linux instance, Amazon GameLift returns a user name and RSA private key, also as strings, for use with an SSH client. The private key must be saved in the proper format to a &lt;code&gt;.pem&lt;/code&gt; file before using. If you&#39;re making this request using the CLI, saving the secret can be handled as part of the &lt;code&gt;GetInstanceAccess&lt;/code&gt; request, as shown in one of the examples for this operation. &lt;/p&gt; &lt;p&gt;To request access to a specific instance, specify the IDs of both the instance and the fleet it belongs to. You can retrieve a fleet&#39;s instance IDs by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeInstances.html\&quot;&gt;DescribeInstances&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html\&quot;&gt;Remotely Access Fleet Instances&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html\&quot;&gt;Debug Fleet Issues&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = GetInstanceAccessInput.from_dict(body)
    return web.Response(status=200)


async def list_aliases(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_aliases

    &lt;p&gt;Retrieves all aliases for this Amazon Web Services account. You can filter the result set by alias name and/or routing strategy type. Use the pagination parameters to retrieve results in sequential pages.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Returned aliases are not listed in any particular order.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = ListAliasesInput.from_dict(body)
    return web.Response(status=200)


async def list_builds(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_builds

    &lt;p&gt;Retrieves build resources for all builds associated with the Amazon Web Services account in use. You can limit results to builds that are in a specific status by using the &lt;code&gt;Status&lt;/code&gt; parameter. Use the pagination parameters to retrieve results in a set of sequential pages. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Build resources are not listed in any particular order.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html\&quot;&gt; Upload a Custom Server Build&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = ListBuildsInput.from_dict(body)
    return web.Response(status=200)


async def list_compute(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_compute

    Retrieves all compute resources registered to a fleet in your Amazon Web Services account. You can filter the result set by location.

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
    body = ListComputeInput.from_dict(body)
    return web.Response(status=200)


async def list_fleets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_fleets

    &lt;p&gt;Retrieves a collection of fleet resources in an Amazon Web Services Region. You can call this operation to get fleets in a previously selected default Region (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/credref/latest/refdocs/setting-global-region.html\&quot;&gt;https://docs.aws.amazon.com/credref/latest/refdocs/setting-global-region.html&lt;/a&gt;or specify a Region in your request. You can filter the result set to find only those fleets that are deployed with a specific build or script. For fleets that have multiple locations, this operation retrieves fleets based on their home Region only.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To get a list of all fleets in a Region, don&#39;t provide a build or script identifier. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get a list of all fleets where a specific custom game build is deployed, provide the build ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To get a list of all Realtime Servers fleets with a specific configuration script, provide the script ID. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a list of fleet IDs that match the request parameters is returned. A NextToken value is also returned if there are more result pages to retrieve.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Fleet resources are not listed in a particular order.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = ListFleetsInput.from_dict(body)
    return web.Response(status=200)


async def list_game_server_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_game_server_groups

    Lists a game server groups.

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
    body = ListGameServerGroupsInput.from_dict(body)
    return web.Response(status=200)


async def list_game_servers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_game_servers

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Retrieves information on all game servers that are currently active in a specified game server group. You can opt to sort the list by game server age. Use the pagination parameters to retrieve results in a set of sequential segments. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = ListGameServersInput.from_dict(body)
    return web.Response(status=200)


async def list_locations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_locations

    Lists all custom and Amazon Web Services locations.

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
    body = ListLocationsInput.from_dict(body)
    return web.Response(status=200)


async def list_scripts(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_scripts

    &lt;p&gt;Retrieves script records for all Realtime scripts that are associated with the Amazon Web Services account in use. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html\&quot;&gt;Amazon GameLift Realtime Servers&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = ListScriptsInput.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Retrieves all tags assigned to a Amazon GameLift resource. Use resource tags to organize Amazon Web Services resources for a range of purposes. This operation handles the permissions necessary to manage tags for Amazon GameLift resources that support tagging.&lt;/p&gt; &lt;p&gt;To list tags for a resource, specify the unique ARN value for the resource.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/answers/account-management/aws-tagging-strategies/\&quot;&gt; Amazon Web Services Tagging Strategies&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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


async def put_scaling_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_scaling_policy

    &lt;p&gt;Creates or updates a scaling policy for a fleet. Scaling policies are used to automatically scale a fleet&#39;s hosting capacity to meet player demand. An active scaling policy instructs Amazon GameLift to track a fleet metric and automatically change the fleet&#39;s capacity when a certain threshold is reached. There are two types of scaling policies: target-based and rule-based. Use a target-based policy to quickly and efficiently manage fleet scaling; this option is the most commonly used. Use rule-based policies when you need to exert fine-grained control over auto-scaling. &lt;/p&gt; &lt;p&gt;Fleets can have multiple scaling policies of each type in force at the same time; you can have one target-based policy, one or multiple rule-based scaling policies, or both. We recommend caution, however, because multiple auto-scaling policies can have unintended consequences.&lt;/p&gt; &lt;p&gt;Learn more about how to work with auto-scaling in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-autoscaling.html\&quot;&gt;Set Up Fleet Automatic Scaling&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Target-based policy&lt;/b&gt; &lt;/p&gt; &lt;p&gt;A target-based policy tracks a single metric: PercentAvailableGameSessions. This metric tells us how much of a fleet&#39;s hosting capacity is ready to host game sessions but is not currently in use. This is the fleet&#39;s buffer; it measures the additional player demand that the fleet could handle at current capacity. With a target-based policy, you set your ideal buffer size and leave it to Amazon GameLift to take whatever action is needed to maintain that target. &lt;/p&gt; &lt;p&gt;For example, you might choose to maintain a 10% buffer for a fleet that has the capacity to host 100 simultaneous game sessions. This policy tells Amazon GameLift to take action whenever the fleet&#39;s available capacity falls below or rises above 10 game sessions. Amazon GameLift will start new instances or stop unused instances in order to return to the 10% buffer. &lt;/p&gt; &lt;p&gt;To create or update a target-based policy, specify a fleet ID and name, and set the policy type to \&quot;TargetBased\&quot;. Specify the metric to track (PercentAvailableGameSessions) and reference a &lt;code&gt;TargetConfiguration&lt;/code&gt; object with your desired buffer value. Exclude all other parameters. On a successful request, the policy name is returned. The scaling policy is automatically in force as soon as it&#39;s successfully created. If the fleet&#39;s auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Rule-based policy&lt;/b&gt; &lt;/p&gt; &lt;p&gt;A rule-based policy tracks specified fleet metric, sets a threshold value, and specifies the type of action to initiate when triggered. With a rule-based policy, you can select from several available fleet metrics. Each policy specifies whether to scale up or scale down (and by how much), so you need one policy for each type of action. &lt;/p&gt; &lt;p&gt;For example, a policy may make the following statement: \&quot;If the percentage of idle instances is greater than 20% for more than 15 minutes, then reduce the fleet capacity by 10%.\&quot;&lt;/p&gt; &lt;p&gt;A policy&#39;s rule statement has the following structure:&lt;/p&gt; &lt;p&gt;If &lt;code&gt;[MetricName]&lt;/code&gt; is &lt;code&gt;[ComparisonOperator]&lt;/code&gt; &lt;code&gt;[Threshold]&lt;/code&gt; for &lt;code&gt;[EvaluationPeriods]&lt;/code&gt; minutes, then &lt;code&gt;[ScalingAdjustmentType]&lt;/code&gt; to/by &lt;code&gt;[ScalingAdjustment]&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To implement the example, the rule statement would look like this:&lt;/p&gt; &lt;p&gt;If &lt;code&gt;[PercentIdleInstances]&lt;/code&gt; is &lt;code&gt;[GreaterThanThreshold]&lt;/code&gt; &lt;code&gt;[20]&lt;/code&gt; for &lt;code&gt;[15]&lt;/code&gt; minutes, then &lt;code&gt;[PercentChangeInCapacity]&lt;/code&gt; to/by &lt;code&gt;[10]&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To create or update a scaling policy, specify a unique combination of name and fleet ID, and set the policy type to \&quot;RuleBased\&quot;. Specify the parameter values for a policy rule statement. On a successful request, the policy name is returned. Scaling policies are automatically in force as soon as they&#39;re successfully created. If the fleet&#39;s auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.&lt;/p&gt;

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
    body = PutScalingPolicyInput.from_dict(body)
    return web.Response(status=200)


async def register_compute(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_compute

    &lt;p&gt;Registers your compute resources in a fleet you previously created. After you register a compute to your fleet, you can monitor and manage your compute using Amazon GameLift. The operation returns the compute resource containing SDK endpoint you can use to connect your game server to Amazon GameLift.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html\&quot;&gt;Create an Anywhere fleet&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-testing.html\&quot;&gt;Test your integration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = RegisterComputeInput.from_dict(body)
    return web.Response(status=200)


async def register_game_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_game_server

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Creates a new game server resource and notifies Amazon GameLift FleetIQ that the game server is ready to host gameplay and players. This operation is called by a game server process that is running on an instance in a game server group. Registering game servers enables Amazon GameLift FleetIQ to track available game servers and enables game clients and services to claim a game server for a new game session. &lt;/p&gt; &lt;p&gt;To register a game server, identify the game server group and instance where the game server is running, and provide a unique identifier for the game server. You can also include connection and game server data.&lt;/p&gt; &lt;p&gt;Once a game server is successfully registered, it is put in status &lt;code&gt;AVAILABLE&lt;/code&gt;. A request to register a game server may fail if the instance it is running on is in the process of shutting down as part of instance balancing or scale-down activity. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = RegisterGameServerInput.from_dict(body)
    return web.Response(status=200)


async def request_upload_credentials(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """request_upload_credentials

    &lt;p&gt;Retrieves a fresh set of credentials for use when uploading a new set of game build files to Amazon GameLift&#39;s Amazon S3. This is done as part of the build creation process; see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateBuild.html\&quot;&gt;GameSession&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To request new credentials, specify the build ID as returned with an initial &lt;code&gt;CreateBuild&lt;/code&gt; request. If successful, a new set of credentials are returned, along with the S3 storage location associated with the build ID.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build\&quot;&gt; Create a Build with Files in S3&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = RequestUploadCredentialsInput.from_dict(body)
    return web.Response(status=200)


async def resolve_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resolve_alias

    &lt;p&gt;Retrieves the fleet ID that an alias is currently pointing to.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = ResolveAliasInput.from_dict(body)
    return web.Response(status=200)


async def resume_game_server_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resume_game_server_group

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Reinstates activity on a game server group after it has been suspended. A game server group might be suspended by the &lt;a href&#x3D;\&quot;gamelift/latest/apireference/API_SuspendGameServerGroup.html\&quot;&gt;SuspendGameServerGroup&lt;/a&gt; operation, or it might be suspended involuntarily due to a configuration problem. In the second case, you can manually resume activity on the group once the configuration problem has been resolved. Refer to the game server group status and status reason for more information on why group activity is suspended.&lt;/p&gt; &lt;p&gt;To resume activity, specify a game server group ARN and the type of activity to be resumed. If successful, a &lt;code&gt;GameServerGroup&lt;/code&gt; object is returned showing that the resumed activity is no longer listed in &lt;code&gt;SuspendedActions&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = ResumeGameServerGroupInput.from_dict(body)
    return web.Response(status=200)


async def search_game_sessions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """search_game_sessions

    &lt;p&gt;Retrieves all active game sessions that match a set of search criteria and sorts them into a specified order. &lt;/p&gt; &lt;p&gt;This operation is not designed to be continually called to track game session status. This practice can cause you to exceed your API limit, which results in errors. Instead, you must configure configure an Amazon Simple Notification Service (SNS) topic to receive notifications from FlexMatch or queues. Continuously polling game session status with &lt;code&gt;DescribeGameSessions&lt;/code&gt; should only be used for games in development with low game session usage. &lt;/p&gt; &lt;p&gt;When searching for game sessions, you specify exactly where you want to search and provide a search filter expression, a sort expression, or both. A search request can search only one fleet, but it can search all of a fleet&#39;s locations. &lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To search all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID. This approach returns game sessions in the fleet&#39;s home Region and all remote locations that fit the search criteria.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To search all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name. For location, you can specify a fleet&#39;s home Region or any remote location.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Use the pagination parameters to retrieve results as a set of sequential pages. &lt;/p&gt; &lt;p&gt;If successful, a &lt;code&gt;GameSession&lt;/code&gt; object is returned for each game session that matches the request. Search finds game sessions that are in &lt;code&gt;ACTIVE&lt;/code&gt; status only. To retrieve information on game sessions in other statuses, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessions.html\&quot;&gt;DescribeGameSessions&lt;/a&gt; .&lt;/p&gt; &lt;p&gt;You can search or sort by the following game session attributes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;gameSessionId&lt;/b&gt; -- A unique identifier for the game session. You can use either a &lt;code&gt;GameSessionId&lt;/code&gt; or &lt;code&gt;GameSessionArn&lt;/code&gt; value. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;gameSessionName&lt;/b&gt; -- Name assigned to a game session. Game session names do not need to be unique to a game session.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;gameSessionProperties&lt;/b&gt; -- Custom data defined in a game session&#39;s &lt;code&gt;GameProperty&lt;/code&gt; parameter. &lt;code&gt;GameProperty&lt;/code&gt; values are stored as key:value pairs; the filter expression must indicate the key and a string to search the data values for. For example, to search for game sessions with custom data containing the key:value pair \&quot;gameMode:brawl\&quot;, specify the following: &lt;code&gt;gameSessionProperties.gameMode &#x3D; \&quot;brawl\&quot;&lt;/code&gt;. All custom data values are searched as strings.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;maximumSessions&lt;/b&gt; -- Maximum number of player sessions allowed for a game session.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;creationTimeMillis&lt;/b&gt; -- Value indicating when a game session was created. It is expressed in Unix time as milliseconds.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;playerSessionCount&lt;/b&gt; -- Number of players currently connected to a game session. This value changes rapidly as players join the session or drop out.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;hasAvailablePlayerSessions&lt;/b&gt; -- Boolean value indicating whether a game session has reached its maximum number of players. It is highly recommended that all search requests include this filter attribute to optimize search performance and return only sessions that players can join. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Returned values for &lt;code&gt;playerSessionCount&lt;/code&gt; and &lt;code&gt;hasAvailablePlayerSessions&lt;/code&gt; change quickly as players join sessions and others drop out. Results should be considered a snapshot in time. Be sure to refresh search results often, and handle sessions that fill up before a player can join. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = SearchGameSessionsInput.from_dict(body)
    return web.Response(status=200)


async def start_fleet_actions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_fleet_actions

    &lt;p&gt;Resumes certain types of activity on fleet instances that were suspended with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html\&quot;&gt;StopFleetActions&lt;/a&gt;. For multi-location fleets, fleet actions are managed separately for each location. Currently, this operation is used to restart a fleet&#39;s auto-scaling activity.&lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To restart actions on instances in the fleet&#39;s home Region, provide a fleet ID and the type of actions to resume. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To restart actions on instances in one of the fleet&#39;s remote locations, provide a fleet ID, a location name, and the type of actions to resume. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, Amazon GameLift once again initiates scaling events as triggered by the fleet&#39;s scaling policies. If actions on the fleet location were never stopped, this operation will have no effect.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = StartFleetActionsInput.from_dict(body)
    return web.Response(status=200)


async def start_game_session_placement(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_game_session_placement

    &lt;p&gt;Places a request for a new game session in a queue. When processing a placement request, Amazon GameLift searches for available resources on the queue&#39;s destinations, scanning each until it finds resources or the placement request times out.&lt;/p&gt; &lt;p&gt;A game session placement request can also request player sessions. When a new game session is successfully created, Amazon GameLift creates a player session for each player included in the request.&lt;/p&gt; &lt;p&gt;When placing a game session, by default Amazon GameLift tries each fleet in the order they are listed in the queue configuration. Ideally, a queue&#39;s destinations are listed in preference order.&lt;/p&gt; &lt;p&gt;Alternatively, when requesting a game session with players, you can also provide latency data for each player in relevant Regions. Latency data indicates the performance lag a player experiences when connected to a fleet in the Region. Amazon GameLift uses latency data to reorder the list of destinations to place the game session in a Region with minimal lag. If latency data is provided for multiple players, Amazon GameLift calculates each Region&#39;s average lag for all players and reorders to get the best game play across all players. &lt;/p&gt; &lt;p&gt;To place a new game session request, specify the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The queue name and a set of game session properties and settings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A unique ID (such as a UUID) for the placement. You use this ID to track the status of the placement request&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) A set of player data and a unique player ID for each player that you are joining to the new game session (player data is optional, but if you include it, you must also provide a unique ID for each player)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Latency data for all players (if you want to optimize game play for the players)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, a new game session placement is created.&lt;/p&gt; &lt;p&gt;To track the status of a placement request, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessionPlacement.html\&quot;&gt;DescribeGameSessionPlacement&lt;/a&gt; and check the request&#39;s status. If the status is &lt;code&gt;FULFILLED&lt;/code&gt;, a new game session has been created and a game session ARN and Region are referenced. If the placement request times out, you can resubmit the request or retry it with a different queue. &lt;/p&gt;

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
    body = StartGameSessionPlacementInput.from_dict(body)
    return web.Response(status=200)


async def start_match_backfill(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_match_backfill

    &lt;p&gt;Finds new players to fill open slots in currently running game sessions. The backfill match process is essentially identical to the process of forming new matches. Backfill requests use the same matchmaker that was used to make the original match, and they provide matchmaking data for all players currently in the game session. FlexMatch uses this information to select new players so that backfilled match continues to meet the original match requirements. &lt;/p&gt; &lt;p&gt;When using FlexMatch with Amazon GameLift managed hosting, you can request a backfill match from a client service by calling this operation with a &lt;code&gt;GameSessions&lt;/code&gt; ID. You also have the option of making backfill requests directly from your game server. In response to a request, FlexMatch creates player sessions for the new players, updates the &lt;code&gt;GameSession&lt;/code&gt; resource, and sends updated matchmaking data to the game server. You can request a backfill match at any point after a game session is started. Each game session can have only one active backfill request at a time; a subsequent request automatically replaces the earlier request.&lt;/p&gt; &lt;p&gt;When using FlexMatch as a standalone component, request a backfill match by calling this operation without a game session identifier. As with newly formed matches, matchmaking results are returned in a matchmaking event so that your game can update the game session that is being backfilled.&lt;/p&gt; &lt;p&gt;To request a backfill match, specify a unique ticket ID, the original matchmaking configuration, and matchmaking data for all current players in the game session being backfilled. Optionally, specify the &lt;code&gt;GameSession&lt;/code&gt; ARN. If successful, a match backfill ticket is created and returned with status set to QUEUED. Track the status of backfill tickets using the same method for tracking tickets for new matches.&lt;/p&gt; &lt;p&gt;Only game sessions created by FlexMatch are supported for match backfill.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html\&quot;&gt; Backfill existing games with FlexMatch&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html\&quot;&gt; Matchmaking events&lt;/a&gt; (reference)&lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/gamelift-match.html\&quot;&gt; How Amazon GameLift FlexMatch works&lt;/a&gt; &lt;/p&gt;

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
    body = StartMatchBackfillInput.from_dict(body)
    return web.Response(status=200)


async def start_matchmaking(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_matchmaking

    &lt;p&gt;Uses FlexMatch to create a game match for a group of players based on custom matchmaking rules. With games that use Amazon GameLift managed hosting, this operation also triggers Amazon GameLift to find hosting resources and start a new game session for the new match. Each matchmaking request includes information on one or more players and specifies the FlexMatch matchmaker to use. When a request is for multiple players, FlexMatch attempts to build a match that includes all players in the request, placing them in the same team and finding additional players as needed to fill the match. &lt;/p&gt; &lt;p&gt;To start matchmaking, provide a unique ticket ID, specify a matchmaking configuration, and include the players to be matched. You must also include any player attributes that are required by the matchmaking configuration&#39;s rule set. If successful, a matchmaking ticket is returned with status set to &lt;code&gt;QUEUED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Track matchmaking events to respond as needed and acquire game session connection information for successfully completed matches. Ticket status updates are tracked using event notification through Amazon Simple Notification Service, which is defined in the matchmaking configuration.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html\&quot;&gt; Add FlexMatch to a game client&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html\&quot;&gt; Set Up FlexMatch event notification&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/gamelift-match.html\&quot;&gt; How Amazon GameLift FlexMatch works&lt;/a&gt; &lt;/p&gt;

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
    body = StartMatchmakingInput.from_dict(body)
    return web.Response(status=200)


async def stop_fleet_actions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_fleet_actions

    &lt;p&gt;Suspends certain types of activity in a fleet location. Currently, this operation is used to stop auto-scaling activity. For multi-location fleets, fleet actions are managed separately for each location. &lt;/p&gt; &lt;p&gt;Stopping fleet actions has several potential purposes. It allows you to temporarily stop auto-scaling activity but retain your scaling policies for use in the future. For multi-location fleets, you can set up fleet-wide auto-scaling, and then opt out of it for certain locations. &lt;/p&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To stop actions on instances in the fleet&#39;s home Region, provide a fleet ID and the type of actions to suspend. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To stop actions on instances in one of the fleet&#39;s remote locations, provide a fleet ID, a location name, and the type of actions to suspend. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, Amazon GameLift no longer initiates scaling events except in response to manual changes using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html\&quot;&gt;UpdateFleetCapacity&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift Fleets&lt;/a&gt; &lt;/p&gt;

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
    body = StopFleetActionsInput.from_dict(body)
    return web.Response(status=200)


async def stop_game_session_placement(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_game_session_placement

    Cancels a game session placement that is in &lt;code&gt;PENDING&lt;/code&gt; status. To stop a placement, provide the placement ID values. If successful, the placement is moved to &lt;code&gt;CANCELLED&lt;/code&gt; status.

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
    body = StopGameSessionPlacementInput.from_dict(body)
    return web.Response(status=200)


async def stop_matchmaking(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_matchmaking

    &lt;p&gt;Cancels a matchmaking ticket or match backfill ticket that is currently being processed. To stop the matchmaking operation, specify the ticket ID. If successful, work on the ticket is stopped, and the ticket status is changed to &lt;code&gt;CANCELLED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This call is also used to turn off automatic backfill for an individual game session. This is for game sessions that are created with a matchmaking configuration that has automatic backfill enabled. The ticket ID is included in the &lt;code&gt;MatchmakerData&lt;/code&gt; of an updated game session object, which is provided to the game server.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the operation is successful, the service sends back an empty JSON struct with the HTTP 200 response (not an empty HTTP body).&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html\&quot;&gt; Add FlexMatch to a game client&lt;/a&gt; &lt;/p&gt;

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
    body = StopMatchmakingInput.from_dict(body)
    return web.Response(status=200)


async def suspend_game_server_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """suspend_game_server_group

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Temporarily stops activity on a game server group without terminating instances or the game server group. You can restart activity by calling &lt;a href&#x3D;\&quot;gamelift/latest/apireference/API_ResumeGameServerGroup.html\&quot;&gt;ResumeGameServerGroup&lt;/a&gt;. You can suspend the following activity:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Instance type replacement&lt;/b&gt; - This activity evaluates the current game hosting viability of all Spot instance types that are defined for the game server group. It updates the Auto Scaling group to remove nonviable Spot Instance types, which have a higher chance of game server interruptions. It then balances capacity across the remaining viable Spot Instance types. When this activity is suspended, the Auto Scaling group continues with its current balance, regardless of viability. Instance protection, utilization metrics, and capacity scaling activities continue to be active. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To suspend activity, specify a game server group ARN and the type of activity to be suspended. If successful, a &lt;code&gt;GameServerGroup&lt;/code&gt; object is returned showing that the activity is listed in &lt;code&gt;SuspendedActions&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = SuspendGameServerGroupInput.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns a tag to an Amazon GameLift resource. You can use tags to organize resources, create IAM permissions policies to manage access to groups of resources, customize Amazon Web Services cost breakdowns, and more. This operation handles the permissions necessary to manage tags for Amazon GameLift resources that support tagging.&lt;/p&gt; &lt;p&gt;To add a tag to a resource, specify the unique ARN value for the resource and provide a tag list containing one or more tags. The operation succeeds even if the list includes tags that are already assigned to the resource. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/answers/account-management/aws-tagging-strategies/\&quot;&gt; Amazon Web Services Tagging Strategies&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Removes a tag assigned to a Amazon GameLift resource. You can use resource tags to organize Amazon Web Services resources for a range of purposes. This operation handles the permissions necessary to manage tags for Amazon GameLift resources that support tagging.&lt;/p&gt; &lt;p&gt;To remove a tag from a resource, specify the unique ARN value for the resource and provide a string list containing one or more tags to remove. This operation succeeds even if the list includes tags that aren&#39;t assigned to the resource.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/answers/account-management/aws-tagging-strategies/\&quot;&gt; Amazon Web Services Tagging Strategies&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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


async def update_alias(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_alias

    &lt;p&gt;Updates properties for an alias. To update properties, specify the alias ID to be updated and provide the information to be changed. To reassign an alias to another fleet, provide an updated routing strategy. If successful, the updated alias record is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateAliasInput.from_dict(body)
    return web.Response(status=200)


async def update_build(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_build

    &lt;p&gt;Updates metadata in a build resource, including the build name and version. To update the metadata, specify the build ID to update and provide the new values. If successful, a build object containing the updated metadata is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html\&quot;&gt; Upload a Custom Server Build&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateBuildInput.from_dict(body)
    return web.Response(status=200)


async def update_fleet_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_fleet_attributes

    &lt;p&gt;Updates a fleet&#39;s mutable attributes, including game session protection and resource creation limits.&lt;/p&gt; &lt;p&gt;To update fleet attributes, specify the fleet ID and the property values that you want to change. &lt;/p&gt; &lt;p&gt;If successful, an updated &lt;code&gt;FleetAttributes&lt;/code&gt; object is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateFleetAttributesInput.from_dict(body)
    return web.Response(status=200)


async def update_fleet_capacity(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_fleet_capacity

    &lt;p&gt;Updates capacity settings for a fleet. For fleets with multiple locations, use this operation to manage capacity settings in each location individually. Fleet capacity determines the number of game sessions and players that can be hosted based on the fleet configuration. Use this operation to set the following fleet capacity properties: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Minimum/maximum size: Set hard limits on fleet capacity. Amazon GameLift cannot set the fleet&#39;s capacity to a value outside of this range, whether the capacity is changed manually or through automatic scaling. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Desired capacity: Manually set the number of Amazon EC2 instances to be maintained in a fleet location. Before changing a fleet&#39;s desired capacity, you may want to call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeEC2InstanceLimits.html\&quot;&gt;DescribeEC2InstanceLimits&lt;/a&gt; to get the maximum capacity of the fleet&#39;s Amazon EC2 instance type. Alternatively, consider using automatic scaling to adjust capacity based on player demand.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation can be used in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To update capacity for a fleet&#39;s home Region, or if the fleet has no remote locations, omit the &lt;code&gt;Location&lt;/code&gt; parameter. The fleet must be in &lt;code&gt;ACTIVE&lt;/code&gt; status. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To update capacity for a fleet&#39;s remote location, include the &lt;code&gt;Location&lt;/code&gt; parameter set to the location to be updated. The location must be in &lt;code&gt;ACTIVE&lt;/code&gt; status.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If successful, capacity settings are updated immediately. In response a change in desired capacity, Amazon GameLift initiates steps to start new instances or terminate existing instances in the requested fleet location. This continues until the location&#39;s active instance count matches the new desired instance count. You can track a fleet&#39;s current capacity by calling &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html\&quot;&gt;DescribeFleetCapacity&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html\&quot;&gt;DescribeFleetLocationCapacity&lt;/a&gt;. If the requested desired instance count is higher than the instance type&#39;s limit, the &lt;code&gt;LimitExceeded&lt;/code&gt; exception occurs.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-manage-capacity.html\&quot;&gt;Scaling fleet capacity&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateFleetCapacityInput.from_dict(body)
    return web.Response(status=200)


async def update_fleet_port_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_fleet_port_settings

    &lt;p&gt;Updates permissions that allow inbound traffic to connect to game sessions that are being hosted on instances in the fleet. &lt;/p&gt; &lt;p&gt;To update settings, specify the fleet ID to be updated and specify the changes to be made. List the permissions you want to add in &lt;code&gt;InboundPermissionAuthorizations&lt;/code&gt;, and permissions you want to remove in &lt;code&gt;InboundPermissionRevocations&lt;/code&gt;. Permissions to be removed must match existing fleet permissions. &lt;/p&gt; &lt;p&gt;If successful, the fleet ID for the updated fleet is returned. For fleets with remote locations, port setting updates can take time to propagate across all locations. You can check the status of updates in each location by calling &lt;code&gt;DescribeFleetPortSettings&lt;/code&gt; with a location name.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateFleetPortSettingsInput.from_dict(body)
    return web.Response(status=200)


async def update_game_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_game_server

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Updates information about a registered game server to help Amazon GameLift FleetIQ to track game server availability. This operation is called by a game server process that is running on an instance in a game server group. &lt;/p&gt; &lt;p&gt;Use this operation to update the following types of game server information. You can make all three types of updates in the same request:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To update the game server&#39;s utilization status, identify the game server and game server group and specify the current utilization status. Use this status to identify when game servers are currently hosting games and when they are available to be claimed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To report health status, identify the game server and game server group and set health check to &lt;code&gt;HEALTHY&lt;/code&gt;. If a game server does not report health status for a certain length of time, the game server is no longer considered healthy. As a result, it will be eventually deregistered from the game server group to avoid affecting utilization metrics. The best practice is to report health every 60 seconds.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To change game server metadata, provide updated game server data.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Once a game server is successfully updated, the relevant statuses and timestamps are updated.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateGameServerInput.from_dict(body)
    return web.Response(status=200)


async def update_game_server_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_game_server_group

    &lt;p&gt; &lt;b&gt;This operation is used with the Amazon GameLift FleetIQ solution and game server groups.&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Updates Amazon GameLift FleetIQ-specific properties for a game server group. Many Auto Scaling group properties are updated on the Auto Scaling group directly, including the launch template, Auto Scaling policies, and maximum/minimum/desired instance counts.&lt;/p&gt; &lt;p&gt;To update the game server group, specify the game server group ID and provide the updated values. Before applying the updates, the new values are validated to ensure that Amazon GameLift FleetIQ can continue to perform instance balancing activity. If successful, a &lt;code&gt;GameServerGroup&lt;/code&gt; object is returned.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html\&quot;&gt;Amazon GameLift FleetIQ Guide&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateGameServerGroupInput.from_dict(body)
    return web.Response(status=200)


async def update_game_session(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_game_session

    &lt;p&gt;Updates the mutable properties of a game session. &lt;/p&gt; &lt;p&gt;To update a game session, specify the game session ID and the values you want to change. &lt;/p&gt; &lt;p&gt;If successful, the updated &lt;code&gt;GameSession&lt;/code&gt; object is returned. &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateGameSessionInput.from_dict(body)
    return web.Response(status=200)


async def update_game_session_queue(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_game_session_queue

    &lt;p&gt;Updates the configuration of a game session queue, which determines how the queue processes new game session requests. To update settings, specify the queue name to be updated and provide the new settings. When updating destinations, provide a complete list of destinations. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html\&quot;&gt; Using Multi-Region Queues&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateGameSessionQueueInput.from_dict(body)
    return web.Response(status=200)


async def update_matchmaking_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_matchmaking_configuration

    &lt;p&gt;Updates settings for a FlexMatch matchmaking configuration. These changes affect all matches and game sessions that are created after the update. To update settings, specify the configuration name to be updated and provide the new settings. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html\&quot;&gt; Design a FlexMatch matchmaker&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateMatchmakingConfigurationInput.from_dict(body)
    return web.Response(status=200)


async def update_runtime_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_runtime_configuration

    &lt;p&gt;Updates the current runtime configuration for the specified fleet, which tells Amazon GameLift how to launch server processes on all instances in the fleet. You can update a fleet&#39;s runtime configuration at any time after the fleet is created; it does not need to be in &lt;code&gt;ACTIVE&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt;To update runtime configuration, specify the fleet ID and provide a &lt;code&gt;RuntimeConfiguration&lt;/code&gt; with an updated set of server process configurations.&lt;/p&gt; &lt;p&gt;If successful, the fleet&#39;s runtime configuration settings are updated. Each instance in the fleet regularly checks for and retrieves updated runtime configurations. Instances immediately begin complying with the new configuration by launching new server processes or not replacing existing processes when they shut down. Updating a fleet&#39;s runtime configuration never affects existing server processes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html\&quot;&gt;Setting up Amazon GameLift fleets&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateRuntimeConfigurationInput.from_dict(body)
    return web.Response(status=200)


async def update_script(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_script

    &lt;p&gt;Updates Realtime script metadata and content.&lt;/p&gt; &lt;p&gt;To update script metadata, specify the script ID and provide updated name and/or version values. &lt;/p&gt; &lt;p&gt;To update script content, provide an updated zip file by pointing to either a local file or an Amazon S3 bucket location. You can use either method regardless of how the original script was uploaded. Use the &lt;i&gt;Version&lt;/i&gt; parameter to track updates to the script.&lt;/p&gt; &lt;p&gt;If the call is successful, the updated metadata is stored in the script record and a revised script is uploaded to the Amazon GameLift service. Once the script is updated and acquired by a fleet instance, the new version is used for all new game sessions. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html\&quot;&gt;Amazon GameLift Realtime Servers&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Related actions&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\&quot;&gt;All APIs by task&lt;/a&gt; &lt;/p&gt;

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
    body = UpdateScriptInput.from_dict(body)
    return web.Response(status=200)


async def validate_matchmaking_rule_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """validate_matchmaking_rule_set

    &lt;p&gt;Validates the syntax of a matchmaking rule or rule set. This operation checks that the rule set is using syntactically correct JSON and that it conforms to allowed property expressions. To validate syntax, provide a rule set JSON string.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html\&quot;&gt;Build a rule set&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = ValidateMatchmakingRuleSetInput.from_dict(body)
    return web.Response(status=200)
