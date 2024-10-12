from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_phone_number_with_user_request import AssociatePhoneNumberWithUserRequest
from openapi_server.models.associate_phone_numbers_with_voice_connector_group_request import AssociatePhoneNumbersWithVoiceConnectorGroupRequest
from openapi_server.models.associate_phone_numbers_with_voice_connector_group_response import AssociatePhoneNumbersWithVoiceConnectorGroupResponse
from openapi_server.models.associate_phone_numbers_with_voice_connector_request import AssociatePhoneNumbersWithVoiceConnectorRequest
from openapi_server.models.associate_phone_numbers_with_voice_connector_response import AssociatePhoneNumbersWithVoiceConnectorResponse
from openapi_server.models.associate_signin_delegate_groups_with_account_request import AssociateSigninDelegateGroupsWithAccountRequest
from openapi_server.models.batch_create_attendee_request import BatchCreateAttendeeRequest
from openapi_server.models.batch_create_attendee_response import BatchCreateAttendeeResponse
from openapi_server.models.batch_create_channel_membership_request import BatchCreateChannelMembershipRequest
from openapi_server.models.batch_create_channel_membership_response import BatchCreateChannelMembershipResponse
from openapi_server.models.batch_create_room_membership_request import BatchCreateRoomMembershipRequest
from openapi_server.models.batch_create_room_membership_response import BatchCreateRoomMembershipResponse
from openapi_server.models.batch_delete_phone_number_request import BatchDeletePhoneNumberRequest
from openapi_server.models.batch_delete_phone_number_response import BatchDeletePhoneNumberResponse
from openapi_server.models.batch_suspend_user_request import BatchSuspendUserRequest
from openapi_server.models.batch_suspend_user_response import BatchSuspendUserResponse
from openapi_server.models.batch_unsuspend_user_request import BatchUnsuspendUserRequest
from openapi_server.models.batch_unsuspend_user_response import BatchUnsuspendUserResponse
from openapi_server.models.batch_update_phone_number_request import BatchUpdatePhoneNumberRequest
from openapi_server.models.batch_update_phone_number_response import BatchUpdatePhoneNumberResponse
from openapi_server.models.batch_update_user_request import BatchUpdateUserRequest
from openapi_server.models.batch_update_user_response import BatchUpdateUserResponse
from openapi_server.models.create_account_request import CreateAccountRequest
from openapi_server.models.create_account_response import CreateAccountResponse
from openapi_server.models.create_app_instance_admin_request import CreateAppInstanceAdminRequest
from openapi_server.models.create_app_instance_admin_response import CreateAppInstanceAdminResponse
from openapi_server.models.create_app_instance_request import CreateAppInstanceRequest
from openapi_server.models.create_app_instance_response import CreateAppInstanceResponse
from openapi_server.models.create_app_instance_user_request import CreateAppInstanceUserRequest
from openapi_server.models.create_app_instance_user_response import CreateAppInstanceUserResponse
from openapi_server.models.create_attendee_request import CreateAttendeeRequest
from openapi_server.models.create_attendee_response import CreateAttendeeResponse
from openapi_server.models.create_bot_request import CreateBotRequest
from openapi_server.models.create_bot_response import CreateBotResponse
from openapi_server.models.create_channel_ban_request import CreateChannelBanRequest
from openapi_server.models.create_channel_ban_response import CreateChannelBanResponse
from openapi_server.models.create_channel_membership_request import CreateChannelMembershipRequest
from openapi_server.models.create_channel_membership_response import CreateChannelMembershipResponse
from openapi_server.models.create_channel_moderator_request import CreateChannelModeratorRequest
from openapi_server.models.create_channel_moderator_response import CreateChannelModeratorResponse
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.create_channel_response import CreateChannelResponse
from openapi_server.models.create_media_capture_pipeline_request import CreateMediaCapturePipelineRequest
from openapi_server.models.create_media_capture_pipeline_response import CreateMediaCapturePipelineResponse
from openapi_server.models.create_meeting_dial_out_request import CreateMeetingDialOutRequest
from openapi_server.models.create_meeting_dial_out_response import CreateMeetingDialOutResponse
from openapi_server.models.create_meeting_request import CreateMeetingRequest
from openapi_server.models.create_meeting_response import CreateMeetingResponse
from openapi_server.models.create_meeting_with_attendees_request import CreateMeetingWithAttendeesRequest
from openapi_server.models.create_meeting_with_attendees_response import CreateMeetingWithAttendeesResponse
from openapi_server.models.create_phone_number_order_request import CreatePhoneNumberOrderRequest
from openapi_server.models.create_phone_number_order_response import CreatePhoneNumberOrderResponse
from openapi_server.models.create_proxy_session_request import CreateProxySessionRequest
from openapi_server.models.create_proxy_session_response import CreateProxySessionResponse
from openapi_server.models.create_room_membership_request import CreateRoomMembershipRequest
from openapi_server.models.create_room_membership_response import CreateRoomMembershipResponse
from openapi_server.models.create_room_request import CreateRoomRequest
from openapi_server.models.create_room_response import CreateRoomResponse
from openapi_server.models.create_sip_media_application_call_request import CreateSipMediaApplicationCallRequest
from openapi_server.models.create_sip_media_application_call_response import CreateSipMediaApplicationCallResponse
from openapi_server.models.create_sip_media_application_request import CreateSipMediaApplicationRequest
from openapi_server.models.create_sip_media_application_response import CreateSipMediaApplicationResponse
from openapi_server.models.create_sip_rule_request import CreateSipRuleRequest
from openapi_server.models.create_sip_rule_response import CreateSipRuleResponse
from openapi_server.models.create_user_request import CreateUserRequest
from openapi_server.models.create_user_response import CreateUserResponse
from openapi_server.models.create_voice_connector_group_request import CreateVoiceConnectorGroupRequest
from openapi_server.models.create_voice_connector_group_response import CreateVoiceConnectorGroupResponse
from openapi_server.models.create_voice_connector_request import CreateVoiceConnectorRequest
from openapi_server.models.create_voice_connector_response import CreateVoiceConnectorResponse
from openapi_server.models.delete_voice_connector_termination_credentials_request import DeleteVoiceConnectorTerminationCredentialsRequest
from openapi_server.models.describe_app_instance_admin_response import DescribeAppInstanceAdminResponse
from openapi_server.models.describe_app_instance_response import DescribeAppInstanceResponse
from openapi_server.models.describe_app_instance_user_response import DescribeAppInstanceUserResponse
from openapi_server.models.describe_channel_ban_response import DescribeChannelBanResponse
from openapi_server.models.describe_channel_membership_for_app_instance_user_response import DescribeChannelMembershipForAppInstanceUserResponse
from openapi_server.models.describe_channel_membership_response import DescribeChannelMembershipResponse
from openapi_server.models.describe_channel_moderated_by_app_instance_user_response import DescribeChannelModeratedByAppInstanceUserResponse
from openapi_server.models.describe_channel_moderator_response import DescribeChannelModeratorResponse
from openapi_server.models.describe_channel_response import DescribeChannelResponse
from openapi_server.models.disassociate_phone_numbers_from_voice_connector_group_response import DisassociatePhoneNumbersFromVoiceConnectorGroupResponse
from openapi_server.models.disassociate_phone_numbers_from_voice_connector_request import DisassociatePhoneNumbersFromVoiceConnectorRequest
from openapi_server.models.disassociate_phone_numbers_from_voice_connector_response import DisassociatePhoneNumbersFromVoiceConnectorResponse
from openapi_server.models.disassociate_signin_delegate_groups_from_account_request import DisassociateSigninDelegateGroupsFromAccountRequest
from openapi_server.models.get_account_response import GetAccountResponse
from openapi_server.models.get_account_settings_response import GetAccountSettingsResponse
from openapi_server.models.get_app_instance_retention_settings_response import GetAppInstanceRetentionSettingsResponse
from openapi_server.models.get_app_instance_streaming_configurations_response import GetAppInstanceStreamingConfigurationsResponse
from openapi_server.models.get_attendee_response import GetAttendeeResponse
from openapi_server.models.get_bot_response import GetBotResponse
from openapi_server.models.get_channel_message_response import GetChannelMessageResponse
from openapi_server.models.get_events_configuration_response import GetEventsConfigurationResponse
from openapi_server.models.get_global_settings_response import GetGlobalSettingsResponse
from openapi_server.models.get_media_capture_pipeline_response import GetMediaCapturePipelineResponse
from openapi_server.models.get_meeting_response import GetMeetingResponse
from openapi_server.models.get_messaging_session_endpoint_response import GetMessagingSessionEndpointResponse
from openapi_server.models.get_phone_number_order_response import GetPhoneNumberOrderResponse
from openapi_server.models.get_phone_number_response import GetPhoneNumberResponse
from openapi_server.models.get_phone_number_settings_response import GetPhoneNumberSettingsResponse
from openapi_server.models.get_proxy_session_response import GetProxySessionResponse
from openapi_server.models.get_retention_settings_response import GetRetentionSettingsResponse
from openapi_server.models.get_room_response import GetRoomResponse
from openapi_server.models.get_sip_media_application_logging_configuration_response import GetSipMediaApplicationLoggingConfigurationResponse
from openapi_server.models.get_sip_media_application_response import GetSipMediaApplicationResponse
from openapi_server.models.get_sip_rule_response import GetSipRuleResponse
from openapi_server.models.get_user_response import GetUserResponse
from openapi_server.models.get_user_settings_response import GetUserSettingsResponse
from openapi_server.models.get_voice_connector_emergency_calling_configuration_response import GetVoiceConnectorEmergencyCallingConfigurationResponse
from openapi_server.models.get_voice_connector_group_response import GetVoiceConnectorGroupResponse
from openapi_server.models.get_voice_connector_logging_configuration_response import GetVoiceConnectorLoggingConfigurationResponse
from openapi_server.models.get_voice_connector_origination_response import GetVoiceConnectorOriginationResponse
from openapi_server.models.get_voice_connector_proxy_response import GetVoiceConnectorProxyResponse
from openapi_server.models.get_voice_connector_response import GetVoiceConnectorResponse
from openapi_server.models.get_voice_connector_streaming_configuration_response import GetVoiceConnectorStreamingConfigurationResponse
from openapi_server.models.get_voice_connector_termination_health_response import GetVoiceConnectorTerminationHealthResponse
from openapi_server.models.get_voice_connector_termination_response import GetVoiceConnectorTerminationResponse
from openapi_server.models.invite_users_request import InviteUsersRequest
from openapi_server.models.invite_users_response import InviteUsersResponse
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server.models.list_app_instance_admins_response import ListAppInstanceAdminsResponse
from openapi_server.models.list_app_instance_users_response import ListAppInstanceUsersResponse
from openapi_server.models.list_app_instances_response import ListAppInstancesResponse
from openapi_server.models.list_attendee_tags_response import ListAttendeeTagsResponse
from openapi_server.models.list_attendees_response import ListAttendeesResponse
from openapi_server.models.list_bots_response import ListBotsResponse
from openapi_server.models.list_channel_bans_response import ListChannelBansResponse
from openapi_server.models.list_channel_memberships_for_app_instance_user_response import ListChannelMembershipsForAppInstanceUserResponse
from openapi_server.models.list_channel_memberships_response import ListChannelMembershipsResponse
from openapi_server.models.list_channel_messages_response import ListChannelMessagesResponse
from openapi_server.models.list_channel_moderators_response import ListChannelModeratorsResponse
from openapi_server.models.list_channels_moderated_by_app_instance_user_response import ListChannelsModeratedByAppInstanceUserResponse
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_media_capture_pipelines_response import ListMediaCapturePipelinesResponse
from openapi_server.models.list_meeting_tags_response import ListMeetingTagsResponse
from openapi_server.models.list_meetings_response import ListMeetingsResponse
from openapi_server.models.list_phone_number_orders_response import ListPhoneNumberOrdersResponse
from openapi_server.models.list_phone_numbers_response import ListPhoneNumbersResponse
from openapi_server.models.list_proxy_sessions_response import ListProxySessionsResponse
from openapi_server.models.list_room_memberships_response import ListRoomMembershipsResponse
from openapi_server.models.list_rooms_response import ListRoomsResponse
from openapi_server.models.list_sip_media_applications_response import ListSipMediaApplicationsResponse
from openapi_server.models.list_sip_rules_response import ListSipRulesResponse
from openapi_server.models.list_supported_phone_number_countries_response import ListSupportedPhoneNumberCountriesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_users_response import ListUsersResponse
from openapi_server.models.list_voice_connector_groups_response import ListVoiceConnectorGroupsResponse
from openapi_server.models.list_voice_connector_termination_credentials_response import ListVoiceConnectorTerminationCredentialsResponse
from openapi_server.models.list_voice_connectors_response import ListVoiceConnectorsResponse
from openapi_server.models.put_app_instance_retention_settings_request import PutAppInstanceRetentionSettingsRequest
from openapi_server.models.put_app_instance_retention_settings_response import PutAppInstanceRetentionSettingsResponse
from openapi_server.models.put_app_instance_streaming_configurations_request import PutAppInstanceStreamingConfigurationsRequest
from openapi_server.models.put_app_instance_streaming_configurations_response import PutAppInstanceStreamingConfigurationsResponse
from openapi_server.models.put_events_configuration_request import PutEventsConfigurationRequest
from openapi_server.models.put_events_configuration_response import PutEventsConfigurationResponse
from openapi_server.models.put_retention_settings_request import PutRetentionSettingsRequest
from openapi_server.models.put_retention_settings_response import PutRetentionSettingsResponse
from openapi_server.models.put_sip_media_application_logging_configuration_request import PutSipMediaApplicationLoggingConfigurationRequest
from openapi_server.models.put_sip_media_application_logging_configuration_response import PutSipMediaApplicationLoggingConfigurationResponse
from openapi_server.models.put_voice_connector_emergency_calling_configuration_request import PutVoiceConnectorEmergencyCallingConfigurationRequest
from openapi_server.models.put_voice_connector_emergency_calling_configuration_response import PutVoiceConnectorEmergencyCallingConfigurationResponse
from openapi_server.models.put_voice_connector_logging_configuration_request import PutVoiceConnectorLoggingConfigurationRequest
from openapi_server.models.put_voice_connector_logging_configuration_response import PutVoiceConnectorLoggingConfigurationResponse
from openapi_server.models.put_voice_connector_origination_request import PutVoiceConnectorOriginationRequest
from openapi_server.models.put_voice_connector_origination_response import PutVoiceConnectorOriginationResponse
from openapi_server.models.put_voice_connector_proxy_request import PutVoiceConnectorProxyRequest
from openapi_server.models.put_voice_connector_proxy_response import PutVoiceConnectorProxyResponse
from openapi_server.models.put_voice_connector_streaming_configuration_request import PutVoiceConnectorStreamingConfigurationRequest
from openapi_server.models.put_voice_connector_streaming_configuration_response import PutVoiceConnectorStreamingConfigurationResponse
from openapi_server.models.put_voice_connector_termination_credentials_request import PutVoiceConnectorTerminationCredentialsRequest
from openapi_server.models.put_voice_connector_termination_request import PutVoiceConnectorTerminationRequest
from openapi_server.models.put_voice_connector_termination_response import PutVoiceConnectorTerminationResponse
from openapi_server.models.redact_channel_message_response import RedactChannelMessageResponse
from openapi_server.models.regenerate_security_token_response import RegenerateSecurityTokenResponse
from openapi_server.models.reset_personal_pin_response import ResetPersonalPINResponse
from openapi_server.models.restore_phone_number_response import RestorePhoneNumberResponse
from openapi_server.models.search_available_phone_numbers_response import SearchAvailablePhoneNumbersResponse
from openapi_server.models.send_channel_message_request import SendChannelMessageRequest
from openapi_server.models.send_channel_message_response import SendChannelMessageResponse
from openapi_server.models.start_meeting_transcription_request import StartMeetingTranscriptionRequest
from openapi_server.models.tag_attendee_request import TagAttendeeRequest
from openapi_server.models.tag_meeting_request import TagMeetingRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_attendee_request import UntagAttendeeRequest
from openapi_server.models.untag_meeting_request import UntagMeetingRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_account_request import UpdateAccountRequest
from openapi_server.models.update_account_response import UpdateAccountResponse
from openapi_server.models.update_account_settings_request import UpdateAccountSettingsRequest
from openapi_server.models.update_app_instance_request import UpdateAppInstanceRequest
from openapi_server.models.update_app_instance_response import UpdateAppInstanceResponse
from openapi_server.models.update_app_instance_user_request import UpdateAppInstanceUserRequest
from openapi_server.models.update_app_instance_user_response import UpdateAppInstanceUserResponse
from openapi_server.models.update_bot_request import UpdateBotRequest
from openapi_server.models.update_bot_response import UpdateBotResponse
from openapi_server.models.update_channel_message_request import UpdateChannelMessageRequest
from openapi_server.models.update_channel_message_response import UpdateChannelMessageResponse
from openapi_server.models.update_channel_read_marker_response import UpdateChannelReadMarkerResponse
from openapi_server.models.update_channel_request import UpdateChannelRequest
from openapi_server.models.update_channel_response import UpdateChannelResponse
from openapi_server.models.update_global_settings_request import UpdateGlobalSettingsRequest
from openapi_server.models.update_phone_number_request import UpdatePhoneNumberRequest
from openapi_server.models.update_phone_number_response import UpdatePhoneNumberResponse
from openapi_server.models.update_phone_number_settings_request import UpdatePhoneNumberSettingsRequest
from openapi_server.models.update_proxy_session_request import UpdateProxySessionRequest
from openapi_server.models.update_proxy_session_response import UpdateProxySessionResponse
from openapi_server.models.update_room_membership_request import UpdateRoomMembershipRequest
from openapi_server.models.update_room_membership_response import UpdateRoomMembershipResponse
from openapi_server.models.update_room_request import UpdateRoomRequest
from openapi_server.models.update_room_response import UpdateRoomResponse
from openapi_server.models.update_sip_media_application_call_request import UpdateSipMediaApplicationCallRequest
from openapi_server.models.update_sip_media_application_call_response import UpdateSipMediaApplicationCallResponse
from openapi_server.models.update_sip_media_application_request import UpdateSipMediaApplicationRequest
from openapi_server.models.update_sip_media_application_response import UpdateSipMediaApplicationResponse
from openapi_server.models.update_sip_rule_request import UpdateSipRuleRequest
from openapi_server.models.update_sip_rule_response import UpdateSipRuleResponse
from openapi_server.models.update_user_request import UpdateUserRequest
from openapi_server.models.update_user_response import UpdateUserResponse
from openapi_server.models.update_user_settings_request import UpdateUserSettingsRequest
from openapi_server.models.update_voice_connector_group_request import UpdateVoiceConnectorGroupRequest
from openapi_server.models.update_voice_connector_group_response import UpdateVoiceConnectorGroupResponse
from openapi_server.models.update_voice_connector_request import UpdateVoiceConnectorRequest
from openapi_server.models.update_voice_connector_response import UpdateVoiceConnectorResponse
from openapi_server.models.validate_e911_address_request import ValidateE911AddressRequest
from openapi_server.models.validate_e911_address_response import ValidateE911AddressResponse
from openapi_server import util


async def associate_phone_number_with_user(request: web.Request, account_id, user_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_phone_number_with_user

    Associates a phone number with the specified Amazon Chime user.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociatePhoneNumberWithUserRequest.from_dict(body)
    return web.Response(status=200)


async def associate_phone_numbers_with_voice_connector(request: web.Request, voice_connector_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_phone_numbers_with_voice_connector

    &lt;p&gt;Associates phone numbers with the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html\&quot;&gt;AssociatePhoneNumbersWithVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociatePhoneNumbersWithVoiceConnectorRequest.from_dict(body)
    return web.Response(status=200)


async def associate_phone_numbers_with_voice_connector_group(request: web.Request, voice_connector_group_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_phone_numbers_with_voice_connector_group

    &lt;p&gt;Associates phone numbers with the specified Amazon Chime Voice Connector group.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnectorGroup.html\&quot;&gt;AssociatePhoneNumbersWithVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_group_id: The Amazon Chime Voice Connector group ID.
    :type voice_connector_group_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociatePhoneNumbersWithVoiceConnectorGroupRequest.from_dict(body)
    return web.Response(status=200)


async def associate_signin_delegate_groups_with_account(request: web.Request, account_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_signin_delegate_groups_with_account

    Associates the specified sign-in delegate groups with the specified Amazon Chime account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateSigninDelegateGroupsWithAccountRequest.from_dict(body)
    return web.Response(status=200)


async def batch_create_attendee(request: web.Request, meeting_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_create_attendee

    &lt;p&gt;Creates up to 100 new attendees for an active Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html\&quot;&gt;BatchCreateAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchCreateAttendeeRequest.from_dict(body)
    return web.Response(status=200)


async def batch_create_channel_membership(request: web.Request, channel_arn, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """batch_create_channel_membership

    &lt;p&gt;Adds a specified number of users to a channel.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html\&quot;&gt;BatchCreateChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel to which you&#39;re adding users.
    :type channel_arn: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = BatchCreateChannelMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def batch_create_room_membership(request: web.Request, account_id, room_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_create_room_membership

    Adds up to 50 members to a chat room in an Amazon Chime Enterprise account. Members can be users or bots. The member role designates whether the member is a chat room administrator or a general chat room member.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchCreateRoomMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_phone_number(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_phone_number

    &lt;p&gt; Moves phone numbers into the &lt;b&gt;Deletion queue&lt;/b&gt;. Phone numbers must be disassociated from any users or Amazon Chime Voice Connectors before they can be deleted. &lt;/p&gt; &lt;p&gt; Phone numbers remain in the &lt;b&gt;Deletion queue&lt;/b&gt; for 7 days before they are deleted permanently. &lt;/p&gt;

    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchDeletePhoneNumberRequest.from_dict(body)
    return web.Response(status=200)


async def batch_suspend_user(request: web.Request, account_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_suspend_user

    &lt;p&gt;Suspends up to 50 users from a &lt;code&gt;Team&lt;/code&gt; or &lt;code&gt;EnterpriseLWA&lt;/code&gt; Amazon Chime account. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt;Managing Your Amazon Chime Accounts&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Users suspended from a &lt;code&gt;Team&lt;/code&gt; account are disassociated from the account,but they can continue to use Amazon Chime as free users. To remove the suspension from suspended &lt;code&gt;Team&lt;/code&gt; account users, invite them to the &lt;code&gt;Team&lt;/code&gt; account again. You can use the &lt;a&gt;InviteUsers&lt;/a&gt; action to do so.&lt;/p&gt; &lt;p&gt;Users suspended from an &lt;code&gt;EnterpriseLWA&lt;/code&gt; account are immediately signed out of Amazon Chime and can no longer sign in. To remove the suspension from suspended &lt;code&gt;EnterpriseLWA&lt;/code&gt; account users, use the &lt;a&gt;BatchUnsuspendUser&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt; To sign out users without suspending them, use the &lt;a&gt;LogoutUser&lt;/a&gt; action.&lt;/p&gt;

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchSuspendUserRequest.from_dict(body)
    return web.Response(status=200)


async def batch_unsuspend_user(request: web.Request, account_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_unsuspend_user

    &lt;p&gt;Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime &lt;code&gt;EnterpriseLWA&lt;/code&gt; account. Only users on &lt;code&gt;EnterpriseLWA&lt;/code&gt; accounts can be unsuspended using this action. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt; Managing Your Amazon Chime Accounts &lt;/a&gt; in the account types, in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;Previously suspended users who are unsuspended using this action are returned to &lt;code&gt;Registered&lt;/code&gt; status. Users who are not previously suspended are ignored.&lt;/p&gt;

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchUnsuspendUserRequest.from_dict(body)
    return web.Response(status=200)


async def batch_update_phone_number(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_update_phone_number

    &lt;p&gt;Updates phone number product types or calling names. You can update one attribute at a time for each &lt;code&gt;UpdatePhoneNumberRequestItem&lt;/code&gt;. For example, you can update the product type or the calling name.&lt;/p&gt; &lt;p&gt;For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.&lt;/p&gt; &lt;p&gt;Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.&lt;/p&gt;

    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchUpdatePhoneNumberRequest.from_dict(body)
    return web.Response(status=200)


async def batch_update_user(request: web.Request, account_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_update_user

    Updates user details within the &lt;a&gt;UpdateUserRequestItem&lt;/a&gt; object for up to 20 users for the specified Amazon Chime account. Currently, only &lt;code&gt;LicenseType&lt;/code&gt; updates are supported for this action.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchUpdateUserRequest.from_dict(body)
    return web.Response(status=200)


async def create_account(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_account

    Creates an Amazon Chime account under the administrator&#39;s AWS account. Only &lt;code&gt;Team&lt;/code&gt; account types are currently supported for this action. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt;Managing Your Amazon Chime Accounts&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAccountRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_instance(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_instance

    &lt;p&gt;Creates an Amazon Chime SDK messaging &lt;code&gt;AppInstance&lt;/code&gt; under an AWS account. Only SDK messaging customers use this API. &lt;code&gt;CreateAppInstance&lt;/code&gt; supports idempotency behavior as described in the AWS API Standard.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstance.html\&quot;&gt;CreateAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_instance_admin(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_instance_admin

    &lt;p&gt;Promotes an &lt;code&gt;AppInstanceUser&lt;/code&gt; to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;. The promoted user can perform the following actions. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceAdmin.html\&quot;&gt;CreateAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ChannelModerator&lt;/code&gt; actions across all channels in the &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteChannelMessage&lt;/code&gt; actions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceUser&lt;/code&gt; can be promoted to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; role.&lt;/p&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppInstanceAdminRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_instance_user(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_instance_user

    &lt;p&gt;Creates a user under an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. The request consists of a unique &lt;code&gt;appInstanceUserId&lt;/code&gt; and &lt;code&gt;Name&lt;/code&gt; for that user.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceUser.html\&quot;&gt;CreateAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppInstanceUserRequest.from_dict(body)
    return web.Response(status=200)


async def create_attendee(request: web.Request, meeting_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_attendee

    &lt;p&gt; Creates a new attendee for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html\&quot;&gt;CreateAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAttendeeRequest.from_dict(body)
    return web.Response(status=200)


async def create_bot(request: web.Request, account_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_bot

    Creates a bot for an Amazon Chime Enterprise account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateBotRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """create_channel

    &lt;p&gt;Creates a channel to which you can add users and send messages.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html\&quot;&gt;CreateChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = CreateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_ban(request: web.Request, channel_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """create_channel_ban

    &lt;p&gt;Permanently bans a member from a channel. Moderators can&#39;t add banned members to a channel. To undo a ban, you first have to &lt;code&gt;DeleteChannelBan&lt;/code&gt;, and then &lt;code&gt;CreateChannelMembership&lt;/code&gt;. Bans are cleaned up when you delete users or channels.&lt;/p&gt; &lt;p&gt;If you ban a user who is already part of a channel, that user is automatically kicked from the channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelBan.html\&quot;&gt;CreateChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the ban request.
    :type channel_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = CreateChannelBanRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_membership(request: web.Request, channel_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """create_channel_membership

    &lt;p&gt;Adds a user to a channel. The &lt;code&gt;InvitedBy&lt;/code&gt; response field is derived from the request header. A channel member can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Send messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Receive messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Edit their own messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Leave the channel&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Privacy settings impact this action as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Private Channels: You must be a member to list or send messages.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html\&quot;&gt;CreateChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel to which you&#39;re adding users.
    :type channel_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = CreateChannelMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def create_channel_moderator(request: web.Request, channel_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """create_channel_moderator

    &lt;p&gt;Creates a new &lt;code&gt;ChannelModerator&lt;/code&gt;. A channel moderator can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Add and remove other members of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove other moderators of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove user bans for the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redact messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html\&quot;&gt;CreateChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = CreateChannelModeratorRequest.from_dict(body)
    return web.Response(status=200)


async def create_media_capture_pipeline(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_media_capture_pipeline

    &lt;p&gt;Creates a media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline\&quot;&gt;CreateMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateMediaCapturePipelineRequest.from_dict(body)
    return web.Response(status=200)


async def create_meeting(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_meeting

    &lt;p&gt;Creates a new Amazon Chime SDK meeting in the specified media Region with no initial attendees. For more information about specifying media Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\&quot;&gt;Amazon Chime SDK Media Regions&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html\&quot;&gt;CreateMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateMeetingRequest.from_dict(body)
    return web.Response(status=200)


async def create_meeting_dial_out(request: web.Request, meeting_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_meeting_dial_out

    &lt;p&gt;Uses the join token and call metadata in a meeting request (From number, To number, and so forth) to initiate an outbound call to a public switched telephone network (PSTN) and join them into a Chime meeting. Also ensures that the From number belongs to the customer.&lt;/p&gt; &lt;p&gt;To play welcome audio or implement an interactive voice response (IVR), use the &lt;code&gt;CreateSipMediaApplicationCall&lt;/code&gt; action with the corresponding SIP media application ID.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is not available in a dedicated namespace.&lt;/b&gt; &lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateMeetingDialOutRequest.from_dict(body)
    return web.Response(status=200)


async def create_meeting_with_attendees(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_meeting_with_attendees

    &lt;p&gt; Creates a new Amazon Chime SDK meeting in the specified media Region, with attendees. For more information about specifying media Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\&quot;&gt;Amazon Chime SDK Media Regions&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html\&quot;&gt;CreateMeetingWithAttendees&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateMeetingWithAttendeesRequest.from_dict(body)
    return web.Response(status=200)


async def create_phone_number_order(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_phone_number_order

    Creates an order for phone numbers to be provisioned. For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePhoneNumberOrderRequest.from_dict(body)
    return web.Response(status=200)


async def create_proxy_session(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_proxy_session

    &lt;p&gt;Creates a proxy session on the specified Amazon Chime Voice Connector for the specified participant phone numbers.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html\&quot;&gt;CreateProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime voice connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateProxySessionRequest.from_dict(body)
    return web.Response(status=200)


async def create_room(request: web.Request, account_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_room

    Creates a chat room for the specified Amazon Chime Enterprise account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRoomRequest.from_dict(body)
    return web.Response(status=200)


async def create_room_membership(request: web.Request, account_id, room_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_room_membership

    Adds a member to a chat room in an Amazon Chime Enterprise account. A member can be either a user or a bot. The member role designates whether the member is a chat room administrator or a general chat room member.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRoomMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def create_sip_media_application(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sip_media_application

    &lt;p&gt;Creates a SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html\&quot;&gt;CreateSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSipMediaApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def create_sip_media_application_call(request: web.Request, sip_media_application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sip_media_application_call

    &lt;p&gt;Creates an outbound call to a phone number from the phone number specified in the request, and it invokes the endpoint of the specified &lt;code&gt;sipMediaApplicationId&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html\&quot;&gt;CreateSipMediaApplicationCall&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_media_application_id: The ID of the SIP media application.
    :type sip_media_application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSipMediaApplicationCallRequest.from_dict(body)
    return web.Response(status=200)


async def create_sip_rule(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sip_rule

    &lt;p&gt;Creates a SIP rule which can be used to run a SIP media application as a target for a specific trigger type.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html\&quot;&gt;CreateSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSipRuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_user(request: web.Request, account_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user

    Creates a user under the specified Amazon Chime account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateUserRequest.from_dict(body)
    return web.Response(status=200)


async def create_voice_connector(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_voice_connector

    &lt;p&gt;Creates an Amazon Chime Voice Connector under the administrator&#39;s AWS account. You can choose to create an Amazon Chime Voice Connector in a specific AWS Region.&lt;/p&gt; &lt;p&gt;Enabling &lt;a&gt;CreateVoiceConnectorRequest$RequireEncryption&lt;/a&gt; configures your Amazon Chime Voice Connector to use TLS transport for SIP signaling and Secure RTP (SRTP) for media. Inbound calls use TLS transport, and unencrypted outbound calls are blocked. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html\&quot;&gt;CreateVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateVoiceConnectorRequest.from_dict(body)
    return web.Response(status=200)


async def create_voice_connector_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_voice_connector_group

    &lt;p&gt;Creates an Amazon Chime Voice Connector group under the administrator&#39;s AWS account. You can associate Amazon Chime Voice Connectors with the Amazon Chime Voice Connector group by including &lt;code&gt;VoiceConnectorItems&lt;/code&gt; in the request.&lt;/p&gt; &lt;p&gt;You can include Amazon Chime Voice Connectors from different AWS Regions in your group. This creates a fault tolerant mechanism for fallback in case of availability events.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html\&quot;&gt;CreateVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateVoiceConnectorGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_account(request: web.Request, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_account

    &lt;p&gt;Deletes the specified Amazon Chime account. You must suspend all users before deleting &lt;code&gt;Team&lt;/code&gt; account. You can use the &lt;a&gt;BatchSuspendUser&lt;/a&gt; action to dodo.&lt;/p&gt; &lt;p&gt;For &lt;code&gt;EnterpriseLWA&lt;/code&gt; and &lt;code&gt;EnterpriseAD&lt;/code&gt; accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.&lt;/p&gt; &lt;p&gt;Deleted accounts appear in your &lt;code&gt;Disabled&lt;/code&gt; accounts list for 90 days. To restore deleted account from your &lt;code&gt;Disabled&lt;/code&gt; accounts list, you must contact AWS Support.&lt;/p&gt; &lt;p&gt;After 90 days, deleted accounts are permanently removed from your &lt;code&gt;Disabled&lt;/code&gt; accounts list.&lt;/p&gt;

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_app_instance(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance

    &lt;p&gt;Deletes an &lt;code&gt;AppInstance&lt;/code&gt; and all associated data asynchronously.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstance.html\&quot;&gt;DeleteAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_app_instance_admin(request: web.Request, app_instance_admin_arn, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance_admin

    &lt;p&gt;Demotes an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; to an &lt;code&gt;AppInstanceUser&lt;/code&gt;. This action does not delete the user.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceAdmin.html\&quot;&gt;DeleteAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_admin_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;&#39;s administrator.
    :type app_instance_admin_arn: str
    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_app_instance_streaming_configurations(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance_streaming_configurations

    &lt;p&gt;Deletes the streaming configurations of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceStreamingConfigurations.html\&quot;&gt;DeleteAppInstanceStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the streaming configurations being deleted.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_app_instance_user(request: web.Request, app_instance_user_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_instance_user

    &lt;p&gt;Deletes an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceUser.html\&quot;&gt;DeleteAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_user_arn: The ARN of the user request being deleted.
    :type app_instance_user_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_attendee(request: web.Request, meeting_id, attendee_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_attendee

    &lt;p&gt;Deletes an attendee from the specified Amazon Chime SDK meeting and deletes their &lt;code&gt;JoinToken&lt;/code&gt;. Attendees are automatically deleted when a Amazon Chime SDK meeting is deleted. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteAttendee.html\&quot;&gt;DeleteAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param attendee_id: The Amazon Chime SDK attendee ID.
    :type attendee_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_channel(request: web.Request, channel_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """delete_channel

    &lt;p&gt;Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannel.html\&quot;&gt;DeleteChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel being deleted.
    :type channel_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def delete_channel_ban(request: web.Request, channel_arn, member_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """delete_channel_ban

    &lt;p&gt;Removes a user from a channel&#39;s ban list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelBan.html\&quot;&gt;DeleteChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel from which the &lt;code&gt;AppInstanceUser&lt;/code&gt; was banned.
    :type channel_arn: str
    :param member_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; that you want to reinstate.
    :type member_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def delete_channel_membership(request: web.Request, channel_arn, member_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """delete_channel_membership

    &lt;p&gt;Removes a member from a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMembership.html\&quot;&gt;DeleteChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel from which you want to remove the user.
    :type channel_arn: str
    :param member_arn: The ARN of the member that you&#39;re removing from the channel.
    :type member_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def delete_channel_message(request: web.Request, channel_arn, message_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """delete_channel_message

    &lt;p&gt;Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by &lt;code&gt;UpdateChannelMessage&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMessage.html\&quot;&gt;DeleteChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param message_id: The ID of the message being deleted.
    :type message_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def delete_channel_moderator(request: web.Request, channel_arn, channel_moderator_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """delete_channel_moderator

    &lt;p&gt;Deletes a channel moderator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelModerator.html\&quot;&gt;DeleteChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param channel_moderator_arn: The ARN of the moderator being deleted.
    :type channel_moderator_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def delete_events_configuration(request: web.Request, account_id, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_events_configuration

    Deletes the events configuration that allows a bot to receive outgoing events.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param bot_id: The bot ID.
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_media_capture_pipeline(request: web.Request, media_pipeline_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_media_capture_pipeline

    &lt;p&gt;Deletes the media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html\&quot;&gt;DeleteMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param media_pipeline_id: The ID of the media capture pipeline being deleted. 
    :type media_pipeline_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_meeting(request: web.Request, meeting_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_meeting

    &lt;p&gt;Deletes the specified Amazon Chime SDK meeting. The operation deletes all attendees, disconnects all clients, and prevents new clients from joining the meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html\&quot;&gt;DeleteMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_phone_number(request: web.Request, phone_number_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_phone_number

    &lt;p&gt;Moves the specified phone number into the &lt;b&gt;Deletion queue&lt;/b&gt;. A phone number must be disassociated from any users or Amazon Chime Voice Connectors before it can be deleted.&lt;/p&gt; &lt;p&gt;Deleted phone numbers remain in the &lt;b&gt;Deletion queue&lt;/b&gt; for 7 days before they are deleted permanently.&lt;/p&gt;

    :param phone_number_id: The phone number ID.
    :type phone_number_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_proxy_session(request: web.Request, voice_connector_id, proxy_session_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_proxy_session

    &lt;p&gt;Deletes the specified proxy session from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteProxySession.html\&quot;&gt;DeleteProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime voice connector ID.
    :type voice_connector_id: str
    :param proxy_session_id: The proxy session ID.
    :type proxy_session_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_room(request: web.Request, account_id, room_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_room

    Deletes a chat room in an Amazon Chime Enterprise account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The chat room ID.
    :type room_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_room_membership(request: web.Request, account_id, room_id, member_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_room_membership

    Removes a member from a chat room in an Amazon Chime Enterprise account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param member_id: The member ID (user ID or bot ID).
    :type member_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_sip_media_application(request: web.Request, sip_media_application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sip_media_application

    &lt;p&gt;Deletes a SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipMediaApplication.html\&quot;&gt;DeleteSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_media_application_id: The SIP media application ID.
    :type sip_media_application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_sip_rule(request: web.Request, sip_rule_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sip_rule

    &lt;p&gt;Deletes a SIP rule. You must disable a SIP rule before you can delete it.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipRule.html\&quot;&gt;DeleteSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_rule_id: The SIP rule ID.
    :type sip_rule_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector

    &lt;p&gt;Deletes the specified Amazon Chime Voice Connector. Any phone numbers associated with the Amazon Chime Voice Connector must be disassociated from it before it can be deleted.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnector.html\&quot;&gt;DeleteVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector_emergency_calling_configuration(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector_emergency_calling_configuration

    &lt;p&gt;Deletes the emergency calling configuration details from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;DeleteVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector_group(request: web.Request, voice_connector_group_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector_group

    &lt;p&gt;Deletes the specified Amazon Chime Voice Connector group. Any &lt;code&gt;VoiceConnectorItems&lt;/code&gt; and phone numbers associated with the group must be removed before it can be deleted.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorGroup.html\&quot;&gt;DeleteVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_group_id: The Amazon Chime Voice Connector group ID.
    :type voice_connector_group_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector_origination(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector_origination

    &lt;p&gt;Deletes the origination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to deleting the origination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorOrigination.html\&quot;&gt;DeleteVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector_proxy(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector_proxy

    &lt;p&gt;Deletes the proxy configuration from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorProxy.html\&quot;&gt;DeleteVoiceProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector_streaming_configuration(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector_streaming_configuration

    &lt;p&gt;Deletes the streaming configuration for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html\&quot;&gt;DeleteVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector_termination(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector_termination

    &lt;p&gt;Deletes the termination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to deleting the termination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTermination.html\&quot;&gt;DeleteVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_connector_termination_credentials(request: web.Request, voice_connector_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_connector_termination_credentials

    &lt;p&gt;Deletes the specified SIP credentials used by your equipment to authenticate during call termination.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTerminationCredentials.html\&quot;&gt;DeleteVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteVoiceConnectorTerminationCredentialsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app_instance(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance

    &lt;p&gt;Returns the full details of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstance.html\&quot;&gt;DescribeAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_app_instance_admin(request: web.Request, app_instance_admin_arn, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance_admin

    &lt;p&gt;Returns the full details of an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceAdmin.html\&quot;&gt;DescribeAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_admin_arn: The ARN of the &lt;code&gt;AppInstanceAdmin&lt;/code&gt;.
    :type app_instance_admin_arn: str
    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_app_instance_user(request: web.Request, app_instance_user_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_instance_user

    &lt;p&gt;Returns the full details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceUser.html\&quot;&gt;DescribeAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_channel(request: web.Request, channel_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """describe_channel

    &lt;p&gt;Returns the full details of a channel in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html\&quot;&gt;DescribeChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def describe_channel_ban(request: web.Request, channel_arn, member_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """describe_channel_ban

    &lt;p&gt;Returns the full details of a channel ban.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelBan.html\&quot;&gt;DescribeChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel from which the user is banned.
    :type channel_arn: str
    :param member_arn: The ARN of the member being banned.
    :type member_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def describe_channel_membership(request: web.Request, channel_arn, member_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """describe_channel_membership

    &lt;p&gt;Returns the full details of a user&#39;s channel membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html\&quot;&gt;DescribeChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param member_arn: The ARN of the member.
    :type member_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def describe_channel_membership_for_app_instance_user(request: web.Request, channel_arn, app_instance_user_arn, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """describe_channel_membership_for_app_instance_user

    &lt;p&gt; Returns the details of a channel based on the membership of the specified &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembershipForAppInstanceUser.html\&quot;&gt;DescribeChannelMembershipForAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel to which the user belongs.
    :type channel_arn: str
    :param app_instance_user_arn: The ARN of the user in a channel.
    :type app_instance_user_arn: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def describe_channel_moderated_by_app_instance_user(request: web.Request, channel_arn, app_instance_user_arn, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """describe_channel_moderated_by_app_instance_user

    &lt;p&gt;Returns the full details of a channel moderated by the specified &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModeratedByAppInstanceUser.html\&quot;&gt;DescribeChannelModeratedByAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the moderated channel.
    :type channel_arn: str
    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; in the moderated channel.
    :type app_instance_user_arn: str
    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def describe_channel_moderator(request: web.Request, channel_arn, channel_moderator_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """describe_channel_moderator

    &lt;p&gt;Returns the full details of a single ChannelModerator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModerator.html\&quot;&gt;DescribeChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param channel_moderator_arn: The ARN of the channel moderator.
    :type channel_moderator_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def disassociate_phone_number_from_user(request: web.Request, account_id, user_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_phone_number_from_user

    Disassociates the primary provisioned phone number from the specified Amazon Chime user.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def disassociate_phone_numbers_from_voice_connector(request: web.Request, voice_connector_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_phone_numbers_from_voice_connector

    &lt;p&gt;Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnector.html\&quot;&gt;DisassociatePhoneNumbersFromVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociatePhoneNumbersFromVoiceConnectorRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_phone_numbers_from_voice_connector_group(request: web.Request, voice_connector_group_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_phone_numbers_from_voice_connector_group

    &lt;p&gt;Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector group.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnectorGroup.html\&quot;&gt;DisassociatePhoneNumbersFromVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_group_id: The Amazon Chime Voice Connector group ID.
    :type voice_connector_group_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociatePhoneNumbersFromVoiceConnectorRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_signin_delegate_groups_from_account(request: web.Request, account_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_signin_delegate_groups_from_account

    Disassociates the specified sign-in delegate groups from the specified Amazon Chime account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateSigninDelegateGroupsFromAccountRequest.from_dict(body)
    return web.Response(status=200)


async def get_account(request: web.Request, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account

    Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_account_settings(request: web.Request, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_settings

    Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dialout settings. For more information about these settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/policies.html\&quot;&gt;Use the Policies Page&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. 

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_app_instance_retention_settings(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_app_instance_retention_settings

    &lt;p&gt;Gets the retention settings for an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_GetAppInstanceRetentionSettings.html\&quot;&gt;GetMessagingRetentionSettings&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_app_instance_streaming_configurations(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_app_instance_streaming_configurations

    &lt;p&gt;Gets the streaming settings for an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingStreamingConfigurations.html\&quot;&gt;GetMessagingStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_attendee(request: web.Request, meeting_id, attendee_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_attendee

    &lt;p&gt; Gets the Amazon Chime SDK attendee details for a specified meeting ID and attendee ID. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetAttendee.html\&quot;&gt;GetAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param attendee_id: The Amazon Chime SDK attendee ID.
    :type attendee_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_bot(request: web.Request, account_id, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_bot

    Retrieves details for the specified bot, such as bot email address, bot type, status, and display name.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param bot_id: The bot ID.
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_channel_message(request: web.Request, channel_arn, message_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """get_channel_message

    &lt;p&gt;Gets the full details of a channel message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The x-amz-chime-bearer request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html\&quot;&gt;GetChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param message_id: The ID of the message.
    :type message_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def get_events_configuration(request: web.Request, account_id, bot_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_events_configuration

    Gets details for an events configuration that allows a bot to receive outgoing events, such as an HTTPS endpoint or Lambda function ARN.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param bot_id: The bot ID.
    :type bot_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_global_settings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_global_settings

    Retrieves global settings for the administrator&#39;s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_media_capture_pipeline(request: web.Request, media_pipeline_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_media_capture_pipeline

    &lt;p&gt;Gets an existing media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html\&quot;&gt;GetMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param media_pipeline_id: The ID of the pipeline that you want to get.
    :type media_pipeline_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_meeting(request: web.Request, meeting_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_meeting

    &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html\&quot;&gt;GetMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; Gets the Amazon Chime SDK meeting details for the specified meeting ID. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . &lt;/p&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_messaging_session_endpoint(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_messaging_session_endpoint

    &lt;p&gt;The details of the endpoint for the messaging session.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingSessionEndpoint.html\&quot;&gt;GetMessagingSessionEndpoint&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_phone_number(request: web.Request, phone_number_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_phone_number

    Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.

    :param phone_number_id: The phone number ID.
    :type phone_number_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_phone_number_order(request: web.Request, phone_number_order_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_phone_number_order

    Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.

    :param phone_number_order_id: The ID for the phone number order.
    :type phone_number_order_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_phone_number_settings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_phone_number_settings

    Retrieves the phone number settings for the administrator&#39;s AWS account, such as the default outbound calling name.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_proxy_session(request: web.Request, voice_connector_id, proxy_session_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_proxy_session

    &lt;p&gt;Gets the specified proxy session details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetProxySession.html\&quot;&gt;GetProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime voice connector ID.
    :type voice_connector_id: str
    :param proxy_session_id: The proxy session ID.
    :type proxy_session_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_retention_settings(request: web.Request, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_retention_settings

     Gets the retention settings for the specified Amazon Chime Enterprise account. For more information about retention settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\&quot;&gt;Managing Chat Retention Policies&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. 

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_room(request: web.Request, account_id, room_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_room

    Retrieves room details, such as the room name, for a room in an Amazon Chime Enterprise account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_sip_media_application(request: web.Request, sip_media_application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sip_media_application

    &lt;p&gt;Retrieves the information for a SIP media application, including name, AWS Region, and endpoints.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplication.html\&quot;&gt;GetSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_media_application_id: The SIP media application ID.
    :type sip_media_application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_sip_media_application_logging_configuration(request: web.Request, sip_media_application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sip_media_application_logging_configuration

    &lt;p&gt;Returns the logging configuration for the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationLoggingConfiguration.html\&quot;&gt;GetSipMediaApplicationLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_media_application_id: The SIP media application ID.
    :type sip_media_application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_sip_rule(request: web.Request, sip_rule_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sip_rule

    &lt;p&gt;Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and target endpoints.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipRule.html\&quot;&gt;GetSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_rule_id: The SIP rule ID.
    :type sip_rule_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_user(request: web.Request, account_id, user_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_user

    &lt;p&gt;Retrieves details for the specified user ID, such as primary email address, license type,and personal meeting PIN.&lt;/p&gt; &lt;p&gt; To retrieve user details with an email address instead of a user ID, use the &lt;a&gt;ListUsers&lt;/a&gt; action, and then filter by email address. &lt;/p&gt;

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_user_settings(request: web.Request, account_id, user_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_user_settings

    Retrieves settings for the specified user ID, such as any associated phone number settings.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector

    &lt;p&gt;Retrieves details for the specified Amazon Chime Voice Connector, such as timestamps,name, outbound host, and encryption requirements.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html\&quot;&gt;GetVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_emergency_calling_configuration(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_emergency_calling_configuration

    &lt;p&gt;Gets the emergency calling configuration details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;GetVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_group(request: web.Request, voice_connector_group_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_group

    &lt;p&gt; Retrieves details for the specified Amazon Chime Voice Connector group, such as timestamps,name, and associated &lt;code&gt;VoiceConnectorItems&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorGroup.html\&quot;&gt;GetVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_group_id: The Amazon Chime Voice Connector group ID.
    :type voice_connector_group_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_logging_configuration(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_logging_configuration

    &lt;p&gt;Retrieves the logging configuration details for the specified Amazon Chime Voice Connector. Shows whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorLoggingConfiguration.html\&quot;&gt;GetVoiceConnectorLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_origination(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_origination

    &lt;p&gt;Retrieves origination setting details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorOrigination.html\&quot;&gt;GetVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_proxy(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_proxy

    &lt;p&gt;Gets the proxy configuration details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorProxy.html\&quot;&gt;GetVoiceConnectorProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime voice connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_streaming_configuration(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_streaming_configuration

    &lt;p&gt;Retrieves the streaming configuration details for the specified Amazon Chime Voice Connector. Shows whether media streaming is enabled for sending to Amazon Kinesis. It also shows the retention period, in hours, for the Amazon Kinesis data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorStreamingConfiguration.html\&quot;&gt;GetVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_termination(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_termination

    &lt;p&gt;Retrieves termination setting details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTermination.html\&quot;&gt;GetVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_connector_termination_health(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_connector_termination_health

    &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTerminationHealth.html\&quot;&gt;GetVoiceConnectorTerminationHealth&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Retrieves information about the last time a SIP &lt;code&gt;OPTIONS&lt;/code&gt; ping was received from your SIP infrastructure for the specified Amazon Chime Voice Connector.&lt;/p&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def invite_users(request: web.Request, account_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """invite_users

    Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime &lt;code&gt;Team&lt;/code&gt; account. Only &lt;code&gt;Team&lt;/code&gt; account types are currently supported for this action.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = InviteUsersRequest.from_dict(body)
    return web.Response(status=200)


async def list_accounts(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, name=None, user_email=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_accounts

    Lists the Amazon Chime accounts under the administrator&#39;s AWS account. You can filter accounts by account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by the user&#39;s email address, which returns one account result.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param name: Amazon Chime account name prefix with which to filter results.
    :type name: str
    :param user_email: User email address with which to filter results.
    :type user_email: str
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call. Defaults to 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_app_instance_admins(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instance_admins

    &lt;p&gt;Returns a list of the administrators in the &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceAdmins.html\&quot;&gt;ListAppInstanceAdmins&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of administrators that you want to return.
    :type max_results: int
    :param next_token: The token returned from previous API requests until the number of administrators is reached.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_app_instance_users(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instance_users

    &lt;p&gt;List all &lt;code&gt;AppInstanceUsers&lt;/code&gt; created under a single &lt;code&gt;AppInstance&lt;/code&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceUsers.html\&quot;&gt;ListAppInstanceUsers&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of requests that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested users are returned.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_app_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_instances

    &lt;p&gt;Lists all Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;s created under a single AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstances.html\&quot;&gt;ListAppInstances&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of &lt;code&gt;AppInstance&lt;/code&gt;s that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API requests until you reach the maximum number of &lt;code&gt;AppInstance&lt;/code&gt;s.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_attendee_tags(request: web.Request, meeting_id, attendee_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_attendee_tags

    &lt;p&gt;Lists the tags applied to an Amazon Chime SDK attendee resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;ListAttendeeTags is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param attendee_id: The Amazon Chime SDK attendee ID.
    :type attendee_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def list_attendees(request: web.Request, meeting_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_attendees

    &lt;p&gt; Lists the attendees for the specified Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListAttendees.html\&quot;&gt;ListAttendees&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_bots(request: web.Request, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_bots

    Lists the bots associated with the administrator&#39;s Amazon Chime Enterprise account ID.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in a single call. The default is 10.
    :type max_results: int
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_bans(request: web.Request, channel_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, x_amz_chime_bearer=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_bans

    &lt;p&gt;Lists all the users banned from a particular channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelBans.html\&quot;&gt;ListChannelBans&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of bans that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested bans are returned.
    :type next_token: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_memberships(request: web.Request, channel_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, max_results=None, next_token=None, x_amz_chime_bearer=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_memberships

    &lt;p&gt;Lists all channel memberships in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html\&quot;&gt;ListChannelMemberships&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The maximum number of channel memberships that you want returned.
    :type channel_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param type: The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are always returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt;. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. Otherwise hidden members are not returned.
    :type type: str
    :param max_results: The maximum number of channel memberships that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested channel memberships are returned.
    :type next_token: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_memberships_for_app_instance_user(request: web.Request, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, app_instance_user_arn=None, max_results=None, next_token=None, x_amz_chime_bearer=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_memberships_for_app_instance_user

    &lt;p&gt; Lists all channels that a particular &lt;code&gt;AppInstanceUser&lt;/code&gt; is a part of. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can call the API with a user ARN that is not their own. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html\&quot;&gt;ListChannelMembershipsForAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;s
    :type app_instance_user_arn: str
    :param max_results: The maximum number of users that you want returned.
    :type max_results: int
    :param next_token: The token returned from previous API requests until the number of channel memberships is reached.
    :type next_token: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channel_messages(request: web.Request, channel_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sort_order=None, not_before=None, not_after=None, max_results=None, next_token=None, x_amz_chime_bearer=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_messages

    &lt;p&gt;List all the messages in a channel. Returns a paginated list of &lt;code&gt;ChannelMessages&lt;/code&gt;. By default, sorted by creation timestamp in descending order.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.&lt;/p&gt; &lt;p&gt;Also, the x-amz-chime-bearer request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html\&quot;&gt;ListChannelMessages&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sort_order: The order in which you want messages sorted. Default is Descending, based on time created.
    :type sort_order: str
    :param not_before: The initial or starting time stamp for your requested messages.
    :type not_before: str
    :param not_after: The final or ending time stamp for your requested messages.
    :type not_after: str
    :param max_results: The maximum number of messages that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested messages are returned.
    :type next_token: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    not_before = util.deserialize_datetime(not_before)
    not_after = util.deserialize_datetime(not_after)
    return web.Response(status=200)


async def list_channel_moderators(request: web.Request, channel_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, x_amz_chime_bearer=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channel_moderators

    &lt;p&gt;Lists all the moderators for a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelModerators.html\&quot;&gt;ListChannelModerators&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of moderators that you want returned.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested moderators are returned.
    :type next_token: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channels(request: web.Request, app_instance_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, privacy=None, max_results=None, next_token=None, x_amz_chime_bearer=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channels

    &lt;p&gt;Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Functionality &amp;amp; restrictions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use privacy &#x3D; &lt;code&gt;PUBLIC&lt;/code&gt; to retrieve all public channels in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can set privacy &#x3D; &lt;code&gt;PRIVATE&lt;/code&gt; to list the private channels in an account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html\&quot;&gt;ListChannels&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param privacy: The privacy setting. &lt;code&gt;PUBLIC&lt;/code&gt; retrieves all the public channels. &lt;code&gt;PRIVATE&lt;/code&gt; retrieves private channels. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can retrieve private channels. 
    :type privacy: str
    :param max_results: The maximum number of channels that you want to return.
    :type max_results: int
    :param next_token: The token passed by previous API calls until all requested channels are returned.
    :type next_token: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_channels_moderated_by_app_instance_user(request: web.Request, scope, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, app_instance_user_arn=None, max_results=None, next_token=None, x_amz_chime_bearer=None, max_results2=None, next_token2=None) -> web.Response:
    """list_channels_moderated_by_app_instance_user

    &lt;p&gt;A list of the channels moderated by an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html\&quot;&gt;ListChannelsModeratedByAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param scope: 
    :type scope: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param app_instance_user_arn: The ARN of the user in the moderated channel.
    :type app_instance_user_arn: str
    :param max_results: The maximum number of channels in the request.
    :type max_results: int
    :param next_token: The token returned from previous API requests until the number of channels moderated by the user is reached.
    :type next_token: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_media_capture_pipelines(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_media_capture_pipelines

    &lt;p&gt;Returns a list of media capture pipelines.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html\&quot;&gt;ListMediaCapturePipelines&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token used to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call. Valid Range: 1 - 99.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_meeting_tags(request: web.Request, meeting_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_meeting_tags

    &lt;p&gt;Lists the tags applied to an Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def list_meetings(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_meetings

    &lt;p&gt;Lists up to 100 active Amazon Chime SDK meetings.&lt;/p&gt; &lt;important&gt; &lt;p&gt;ListMeetings is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_phone_number_orders(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_phone_number_orders

    Lists the phone number orders for the administrator&#39;s Amazon Chime account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_phone_numbers(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, status=None, product_type=None, filter_name=None, filter_value=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_phone_numbers

    Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param status: The phone number status.
    :type status: str
    :param product_type: The phone number product type.
    :type product_type: str
    :param filter_name: The filter to use to limit the number of results.
    :type filter_name: str
    :param filter_value: The value to use for the filter.
    :type filter_value: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_proxy_sessions(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, status=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_proxy_sessions

    &lt;p&gt;Lists the proxy sessions for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListProxySessions.html\&quot;&gt;ListProxySessions&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime voice connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param status: The proxy session status.
    :type status: str
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_room_memberships(request: web.Request, account_id, room_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_room_memberships

    Lists the membership details for the specified room in an Amazon Chime Enterprise account, such as the members&#39; IDs, email addresses, and names.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_rooms(request: web.Request, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, member_id=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_rooms

    Lists the room details for the specified Amazon Chime Enterprise account. Optionally, filter the results by a member ID (user ID or bot ID) to see a list of rooms that the member belongs to.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param member_id: The member ID (user ID or bot ID).
    :type member_id: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_sip_media_applications(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_sip_media_applications

    &lt;p&gt;Lists the SIP media applications under the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipMediaApplications.html\&quot;&gt;ListSipMediaApplications&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in a single call. Defaults to 100.
    :type max_results: int
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_sip_rules(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sip_media_application=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_sip_rules

    &lt;p&gt;Lists the SIP rules under the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipRules.html\&quot;&gt;ListSipRules&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sip_media_application: The SIP media application ID.
    :type sip_media_application: str
    :param max_results: The maximum number of results to return in a single call. Defaults to 100.
    :type max_results: int
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_supported_phone_number_countries(request: web.Request, product_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_supported_phone_number_countries

    Lists supported phone number countries.

    :param product_type: The phone number product type.
    :type product_type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def list_tags_for_resource(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists the tags applied to an Amazon Chime SDK meeting and messaging resources.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the applicable latest version in the Amazon Chime SDK.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For meetings: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For messaging: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param arn: The resource ARN.
    :type arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def list_users(request: web.Request, account_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, user_email=None, user_type=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_users

    Lists the users that belong to the specified Amazon Chime account. You can specify an email address to list only the user that the email address belongs to.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param user_email: Optional. The user email address used to filter results. Maximum 1.
    :type user_email: str
    :param user_type: The user type.
    :type user_type: str
    :param max_results: The maximum number of results to return in a single call. Defaults to 100.
    :type max_results: int
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_voice_connector_groups(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_voice_connector_groups

    &lt;p&gt;Lists the Amazon Chime Voice Connector groups for the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorGroups.html\&quot;&gt;ListVoiceConnectorGroups&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_voice_connector_termination_credentials(request: web.Request, voice_connector_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_voice_connector_termination_credentials

    &lt;p&gt;Lists the SIP credentials for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorTerminationCredentials.html\&quot;&gt;ListVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def list_voice_connectors(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_voice_connectors

    &lt;p&gt;Lists the Amazon Chime Voice Connectors for the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectors.html\&quot;&gt;ListVoiceConnectors&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to use to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def logout_user(request: web.Request, account_id, user_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """logout_user

    Logs out the specified user from all of the devices they are currently logged into.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def put_app_instance_retention_settings(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_app_instance_retention_settings

    &lt;p&gt;Sets the amount of time in days that a given &lt;code&gt;AppInstance&lt;/code&gt; retains data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_PutAppInstanceRetentionSettings.html\&quot;&gt;PutAppInstanceRetentionSettings&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAppInstanceRetentionSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def put_app_instance_streaming_configurations(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_app_instance_streaming_configurations

    &lt;p&gt;The data streaming configurations of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html\&quot;&gt;PutMessagingStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAppInstanceStreamingConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def put_events_configuration(request: web.Request, account_id, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_events_configuration

    Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime. Choose either an HTTPS endpoint or a Lambda function ARN. For more information, see &lt;a&gt;Bot&lt;/a&gt;.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param bot_id: The bot ID.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEventsConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_retention_settings(request: web.Request, account_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_retention_settings

    &lt;p&gt; Puts retention settings for the specified Amazon Chime Enterprise account. We recommend using AWS CloudTrail to monitor usage of this API for your account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/cloudtrail.html\&quot;&gt;Logging Amazon Chime API Calls with AWS CloudTrail&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; To turn off existing retention settings, remove the number of days from the corresponding &lt;b&gt;RetentionDays&lt;/b&gt; field in the &lt;b&gt;RetentionSettings&lt;/b&gt; object. For more information about retention settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\&quot;&gt;Managing Chat Retention Policies&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt;

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutRetentionSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def put_sip_media_application_logging_configuration(request: web.Request, sip_media_application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_sip_media_application_logging_configuration

    &lt;p&gt;Updates the logging configuration for the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationLoggingConfiguration.html\&quot;&gt;PutSipMediaApplicationLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_media_application_id: The SIP media application ID.
    :type sip_media_application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutSipMediaApplicationLoggingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_voice_connector_emergency_calling_configuration(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_voice_connector_emergency_calling_configuration

    &lt;p&gt;Puts emergency calling configuration details to the specified Amazon Chime Voice Connector, such as emergency phone numbers and calling countries. Origination and termination settings must be enabled for the Amazon Chime Voice Connector before emergency calling can be configured.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;PutVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutVoiceConnectorEmergencyCallingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_voice_connector_logging_configuration(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_voice_connector_logging_configuration

    &lt;p&gt;Adds a logging configuration for the specified Amazon Chime Voice Connector. The logging configuration specifies whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorLoggingConfiguration.html\&quot;&gt;PutVoiceConnectorLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutVoiceConnectorLoggingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_voice_connector_origination(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_voice_connector_origination

    &lt;p&gt;Adds origination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to turning off origination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorOrigination.html\&quot;&gt;PutVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutVoiceConnectorOriginationRequest.from_dict(body)
    return web.Response(status=200)


async def put_voice_connector_proxy(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_voice_connector_proxy

    &lt;p&gt;Puts the specified proxy configuration to the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html\&quot;&gt;PutVoiceConnectorProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime voice connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutVoiceConnectorProxyRequest.from_dict(body)
    return web.Response(status=200)


async def put_voice_connector_streaming_configuration(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_voice_connector_streaming_configuration

    &lt;p&gt;Adds a streaming configuration for the specified Amazon Chime Voice Connector. The streaming configuration specifies whether media streaming is enabled for sending to Kinesis. It also sets the retention period, in hours, for the Amazon Kinesis data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html\&quot;&gt;PutVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutVoiceConnectorStreamingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_voice_connector_termination(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_voice_connector_termination

    &lt;p&gt;Adds termination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to turning off termination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTermination.html\&quot;&gt;PutVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutVoiceConnectorTerminationRequest.from_dict(body)
    return web.Response(status=200)


async def put_voice_connector_termination_credentials(request: web.Request, voice_connector_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_voice_connector_termination_credentials

    &lt;p&gt;Adds termination SIP credentials for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTerminationCredentials.html\&quot;&gt;PutVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutVoiceConnectorTerminationCredentialsRequest.from_dict(body)
    return web.Response(status=200)


async def redact_channel_message(request: web.Request, channel_arn, message_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """redact_channel_message

    &lt;p&gt;Redacts message content, but not metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html\&quot;&gt;RedactChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel containing the messages that you want to redact.
    :type channel_arn: str
    :param message_id: The ID of the message being redacted.
    :type message_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def redact_conversation_message(request: web.Request, account_id, conversation_id, message_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """redact_conversation_message

    Redacts the specified message from the specified Amazon Chime conversation.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param conversation_id: The conversation ID.
    :type conversation_id: str
    :param message_id: The message ID.
    :type message_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def redact_room_message(request: web.Request, account_id, room_id, message_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """redact_room_message

    Redacts the specified message from the specified Amazon Chime channel.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param message_id: The message ID.
    :type message_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def regenerate_security_token(request: web.Request, account_id, bot_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """regenerate_security_token

    Regenerates the security token for a bot.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param bot_id: The bot ID.
    :type bot_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def reset_personal_pin(request: web.Request, account_id, user_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reset_personal_pin

    Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the &lt;a&gt;User&lt;/a&gt; object with the updated personal meeting PIN.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def restore_phone_number(request: web.Request, phone_number_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """restore_phone_number

    Moves a phone number from the &lt;b&gt;Deletion queue&lt;/b&gt; back into the phone number &lt;b&gt;Inventory&lt;/b&gt;.

    :param phone_number_id: The phone number.
    :type phone_number_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def search_available_phone_numbers(request: web.Request, type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, area_code=None, city=None, country=None, state=None, toll_free_prefix=None, phone_number_type=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """search_available_phone_numbers

    Searches for phone numbers that can be ordered. For US numbers, provide at least one of the following search filters: &lt;code&gt;AreaCode&lt;/code&gt;, &lt;code&gt;City&lt;/code&gt;, &lt;code&gt;State&lt;/code&gt;, or &lt;code&gt;TollFreePrefix&lt;/code&gt;. If you provide &lt;code&gt;City&lt;/code&gt;, you must also provide &lt;code&gt;State&lt;/code&gt;. Numbers outside the US only support the &lt;code&gt;PhoneNumberType&lt;/code&gt; filter, which you must use.

    :param type: 
    :type type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param area_code: The area code used to filter results. Only applies to the US.
    :type area_code: str
    :param city: The city used to filter results. Only applies to the US.
    :type city: str
    :param country: The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2.
    :type country: str
    :param state: The state used to filter results. Required only if you provide &lt;code&gt;City&lt;/code&gt;. Only applies to the US.
    :type state: str
    :param toll_free_prefix: The toll-free prefix that you use to filter results. Only applies to the US.
    :type toll_free_prefix: str
    :param phone_number_type: The phone number type used to filter results. Required for non-US numbers.
    :type phone_number_type: str
    :param max_results: The maximum number of results to return in a single call.
    :type max_results: int
    :param next_token: The token used to retrieve the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def send_channel_message(request: web.Request, channel_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """send_channel_message

    &lt;p&gt;Sends a message to a particular channel that the member is a part of.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;p&gt;Also, &lt;code&gt;STANDARD&lt;/code&gt; messages can contain 4KB of data and the 1KB of metadata. &lt;code&gt;CONTROL&lt;/code&gt; messages can contain 30 bytes of data and no metadata.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html\&quot;&gt;SendChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = SendChannelMessageRequest.from_dict(body)
    return web.Response(status=200)


async def start_meeting_transcription(request: web.Request, meeting_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_meeting_transcription

    &lt;p&gt;Starts transcription for the specified &lt;code&gt;meetingId&lt;/code&gt;. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html\&quot;&gt; Using Amazon Chime SDK live transcription &lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify an invalid configuration, a &lt;code&gt;TranscriptFailed&lt;/code&gt; event will be sent with the contents of the &lt;code&gt;BadRequestException&lt;/code&gt; generated by Amazon Transcribe. For more information on each parameter and which combinations are valid, refer to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html\&quot;&gt;StartStreamTranscription&lt;/a&gt; API in the &lt;i&gt;Amazon Transcribe Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Chime SDK live transcription is powered by Amazon Transcribe. Use of Amazon Transcribe is subject to the &lt;a href&#x3D;\&quot;https://aws.amazon.com/service-terms/\&quot;&gt;AWS Service Terms&lt;/a&gt;, including the terms specific to the AWS Machine Learning and Artificial Intelligence Services.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html\&quot;&gt;StartMeetingTranscription&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The unique ID of the meeting being transcribed.
    :type meeting_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartMeetingTranscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def stop_meeting_transcription(request: web.Request, meeting_id, operation, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_meeting_transcription

    &lt;p&gt;Stops transcription for the specified &lt;code&gt;meetingId&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html\&quot;&gt;StopMeetingTranscription&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The unique ID of the meeting for which you stop transcription.
    :type meeting_id: str
    :param operation: 
    :type operation: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def tag_attendee(request: web.Request, meeting_id, attendee_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_attendee

    &lt;p&gt;Applies the specified tags to the specified Amazon Chime attendee.&lt;/p&gt; &lt;important&gt; &lt;p&gt;TagAttendee is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param attendee_id: The Amazon Chime SDK attendee ID.
    :type attendee_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagAttendeeRequest.from_dict(body)
    return web.Response(status=200)


async def tag_meeting(request: web.Request, meeting_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_meeting

    &lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagMeetingRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def untag_attendee(request: web.Request, meeting_id, attendee_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_attendee

    &lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK attendee.&lt;/p&gt; &lt;important&gt; &lt;p&gt;UntagAttendee is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param attendee_id: The Amazon Chime SDK attendee ID.
    :type attendee_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagAttendeeRequest.from_dict(body)
    return web.Response(status=200)


async def untag_meeting(request: web.Request, meeting_id, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_meeting

    &lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param meeting_id: The Amazon Chime SDK meeting ID.
    :type meeting_id: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagMeetingRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    &lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def update_account(request: web.Request, account_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_account

    Updates account details for the specified Amazon Chime account. Currently, only account name and default license updates are supported for this action.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAccountRequest.from_dict(body)
    return web.Response(status=200)


async def update_account_settings(request: web.Request, account_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_account_settings

    Updates the settings for the specified Amazon Chime account. You can update settings for remote control of shared screens, or for the dial-out option. For more information about these settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/policies.html\&quot;&gt;Use the Policies Page&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAccountSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_instance(request: web.Request, app_instance_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_instance

    &lt;p&gt;Updates &lt;code&gt;AppInstance&lt;/code&gt; metadata.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_UpdateAppInstance.html\&quot;&gt;UpdateAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_arn: The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;.
    :type app_instance_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAppInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_instance_user(request: web.Request, app_instance_user_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_instance_user

    &lt;p&gt;Updates the details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;. You can update names and metadata.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_UpdateAppInstanceUser.html\&quot;&gt;UpdateAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param app_instance_user_arn: The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;.
    :type app_instance_user_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAppInstanceUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_bot(request: web.Request, account_id, bot_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_bot

    Updates the status of the specified bot, such as starting or stopping the bot from running in your Amazon Chime Enterprise account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param bot_id: The bot ID.
    :type bot_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateBotRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel(request: web.Request, channel_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """update_channel

    &lt;p&gt;Update a channel&#39;s attributes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannel.html\&quot;&gt;UpdateChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = UpdateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel_message(request: web.Request, channel_arn, message_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """update_channel_message

    &lt;p&gt;Updates the content of a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html\&quot;&gt;UpdateChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param message_id: The ID string of the message being updated.
    :type message_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    body = UpdateChannelMessageRequest.from_dict(body)
    return web.Response(status=200)


async def update_channel_read_marker(request: web.Request, channel_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_chime_bearer=None) -> web.Response:
    """update_channel_read_marker

    &lt;p&gt;The details of the time when a user last read messages in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelReadMarker.html\&quot;&gt;UpdateChannelReadMarker&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param channel_arn: The ARN of the channel.
    :type channel_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amz_chime_bearer: The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call.
    :type x_amz_chime_bearer: str

    """
    return web.Response(status=200)


async def update_global_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_global_settings

    Updates global settings for the administrator&#39;s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def update_phone_number(request: web.Request, phone_number_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_phone_number

    &lt;p&gt;Updates phone number details, such as product type or calling name, for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type or the calling name in one action.&lt;/p&gt; &lt;p&gt;For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.&lt;/p&gt; &lt;p&gt;Updates to outbound calling names can take 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.&lt;/p&gt;

    :param phone_number_id: The phone number ID.
    :type phone_number_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePhoneNumberRequest.from_dict(body)
    return web.Response(status=200)


async def update_phone_number_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_phone_number_settings

    Updates the phone number settings for the administrator&#39;s AWS account, such as the default outbound calling name. You can update the default outbound calling name once every seven days. Outbound calling names can take up to 72 hours to update.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePhoneNumberSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_proxy_session(request: web.Request, voice_connector_id, proxy_session_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_proxy_session

    &lt;p&gt;Updates the specified proxy session details, such as voice or SMS capabilities.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html\&quot;&gt;UpdateProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime voice connector ID.
    :type voice_connector_id: str
    :param proxy_session_id: The proxy session ID.
    :type proxy_session_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateProxySessionRequest.from_dict(body)
    return web.Response(status=200)


async def update_room(request: web.Request, account_id, room_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_room

    Updates room details, such as the room name, for a room in an Amazon Chime Enterprise account.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRoomRequest.from_dict(body)
    return web.Response(status=200)


async def update_room_membership(request: web.Request, account_id, room_id, member_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_room_membership

    Updates room membership details, such as the member role, for a room in an Amazon Chime Enterprise account. The member role designates whether the member is a chat room administrator or a general chat room member. The member role can be updated only for user IDs.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param room_id: The room ID.
    :type room_id: str
    :param member_id: The member ID.
    :type member_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRoomMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def update_sip_media_application(request: web.Request, sip_media_application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sip_media_application

    &lt;p&gt;Updates the details of the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplication.html\&quot;&gt;UpdateSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_media_application_id: The SIP media application ID.
    :type sip_media_application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSipMediaApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def update_sip_media_application_call(request: web.Request, sip_media_application_id, transaction_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sip_media_application_call

    &lt;p&gt;Invokes the AWS Lambda function associated with the SIP media application and transaction ID in an update request. The Lambda function can then return a new set of actions.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html\&quot;&gt;UpdateSipMediaApplicationCall&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_media_application_id: The ID of the SIP media application handling the call.
    :type sip_media_application_id: str
    :param transaction_id: The ID of the call transaction.
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSipMediaApplicationCallRequest.from_dict(body)
    return web.Response(status=200)


async def update_sip_rule(request: web.Request, sip_rule_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sip_rule

    &lt;p&gt;Updates the details of the specified SIP rule.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html\&quot;&gt;UpdateSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param sip_rule_id: The SIP rule ID.
    :type sip_rule_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSipRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_user(request: web.Request, account_id, user_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user

    Updates user details for a specified user ID. Currently, only &lt;code&gt;LicenseType&lt;/code&gt; updates are supported for this action.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_settings(request: web.Request, account_id, user_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_settings

    Updates the settings for the specified user, such as phone number settings.

    :param account_id: The Amazon Chime account ID.
    :type account_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_voice_connector(request: web.Request, voice_connector_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_voice_connector

    &lt;p&gt;Updates details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html\&quot;&gt;UpdateVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_id: The Amazon Chime Voice Connector ID.
    :type voice_connector_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateVoiceConnectorRequest.from_dict(body)
    return web.Response(status=200)


async def update_voice_connector_group(request: web.Request, voice_connector_group_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_voice_connector_group

    &lt;p&gt;Updates details of the specified Amazon Chime Voice Connector group, such as the name and Amazon Chime Voice Connector priority ranking.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html\&quot;&gt;UpdateVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param voice_connector_group_id: The Amazon Chime Voice Connector group ID.
    :type voice_connector_group_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateVoiceConnectorGroupRequest.from_dict(body)
    return web.Response(status=200)


async def validate_e911_address(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """validate_e911_address

    &lt;p&gt;Validates an address to be used for 911 calls made with Amazon Chime Voice Connectors. You can use validated addresses in a Presence Information Data Format Location Object file that you include in SIP requests. That helps ensure that addresses are routed to the appropriate Public Safety Answering Point.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html\&quot;&gt;ValidateE911Address&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ValidateE911AddressRequest.from_dict(body)
    return web.Response(status=200)
