from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_app_request import CreateAppRequest
from openapi_server.models.create_app_response import CreateAppResponse
from openapi_server.models.create_campaign_request import CreateCampaignRequest
from openapi_server.models.create_campaign_response import CreateCampaignResponse
from openapi_server.models.create_email_template_response import CreateEmailTemplateResponse
from openapi_server.models.create_export_job_request import CreateExportJobRequest
from openapi_server.models.create_export_job_response import CreateExportJobResponse
from openapi_server.models.create_import_job_request import CreateImportJobRequest
from openapi_server.models.create_import_job_response import CreateImportJobResponse
from openapi_server.models.create_in_app_template_response import CreateInAppTemplateResponse
from openapi_server.models.create_journey_request import CreateJourneyRequest
from openapi_server.models.create_journey_response import CreateJourneyResponse
from openapi_server.models.create_push_template_response import CreatePushTemplateResponse
from openapi_server.models.create_recommender_configuration_request import CreateRecommenderConfigurationRequest
from openapi_server.models.create_recommender_configuration_response import CreateRecommenderConfigurationResponse
from openapi_server.models.create_segment_request import CreateSegmentRequest
from openapi_server.models.create_segment_response import CreateSegmentResponse
from openapi_server.models.create_sms_template_response import CreateSmsTemplateResponse
from openapi_server.models.create_voice_template_response import CreateVoiceTemplateResponse
from openapi_server.models.delete_adm_channel_response import DeleteAdmChannelResponse
from openapi_server.models.delete_apns_channel_response import DeleteApnsChannelResponse
from openapi_server.models.delete_apns_sandbox_channel_response import DeleteApnsSandboxChannelResponse
from openapi_server.models.delete_apns_voip_channel_response import DeleteApnsVoipChannelResponse
from openapi_server.models.delete_apns_voip_sandbox_channel_response import DeleteApnsVoipSandboxChannelResponse
from openapi_server.models.delete_app_response import DeleteAppResponse
from openapi_server.models.delete_baidu_channel_response import DeleteBaiduChannelResponse
from openapi_server.models.delete_campaign_response import DeleteCampaignResponse
from openapi_server.models.delete_email_channel_response import DeleteEmailChannelResponse
from openapi_server.models.delete_email_template_response import DeleteEmailTemplateResponse
from openapi_server.models.delete_endpoint_response import DeleteEndpointResponse
from openapi_server.models.delete_event_stream_response import DeleteEventStreamResponse
from openapi_server.models.delete_gcm_channel_response import DeleteGcmChannelResponse
from openapi_server.models.delete_in_app_template_response import DeleteInAppTemplateResponse
from openapi_server.models.delete_journey_response import DeleteJourneyResponse
from openapi_server.models.delete_push_template_response import DeletePushTemplateResponse
from openapi_server.models.delete_recommender_configuration_response import DeleteRecommenderConfigurationResponse
from openapi_server.models.delete_segment_response import DeleteSegmentResponse
from openapi_server.models.delete_sms_channel_response import DeleteSmsChannelResponse
from openapi_server.models.delete_sms_template_response import DeleteSmsTemplateResponse
from openapi_server.models.delete_user_endpoints_response import DeleteUserEndpointsResponse
from openapi_server.models.delete_voice_channel_response import DeleteVoiceChannelResponse
from openapi_server.models.delete_voice_template_response import DeleteVoiceTemplateResponse
from openapi_server.models.get_adm_channel_response import GetAdmChannelResponse
from openapi_server.models.get_apns_channel_response import GetApnsChannelResponse
from openapi_server.models.get_apns_sandbox_channel_response import GetApnsSandboxChannelResponse
from openapi_server.models.get_apns_voip_channel_response import GetApnsVoipChannelResponse
from openapi_server.models.get_apns_voip_sandbox_channel_response import GetApnsVoipSandboxChannelResponse
from openapi_server.models.get_app_response import GetAppResponse
from openapi_server.models.get_application_date_range_kpi_response import GetApplicationDateRangeKpiResponse
from openapi_server.models.get_application_settings_response import GetApplicationSettingsResponse
from openapi_server.models.get_apps_response import GetAppsResponse
from openapi_server.models.get_baidu_channel_response import GetBaiduChannelResponse
from openapi_server.models.get_campaign_activities_response import GetCampaignActivitiesResponse
from openapi_server.models.get_campaign_date_range_kpi_response import GetCampaignDateRangeKpiResponse
from openapi_server.models.get_campaign_response import GetCampaignResponse
from openapi_server.models.get_campaign_version_response import GetCampaignVersionResponse
from openapi_server.models.get_campaign_versions_response import GetCampaignVersionsResponse
from openapi_server.models.get_campaigns_response import GetCampaignsResponse
from openapi_server.models.get_channels_response import GetChannelsResponse
from openapi_server.models.get_email_channel_response import GetEmailChannelResponse
from openapi_server.models.get_email_template_response import GetEmailTemplateResponse
from openapi_server.models.get_endpoint_response import GetEndpointResponse
from openapi_server.models.get_event_stream_response import GetEventStreamResponse
from openapi_server.models.get_export_job_response import GetExportJobResponse
from openapi_server.models.get_export_jobs_response import GetExportJobsResponse
from openapi_server.models.get_gcm_channel_response import GetGcmChannelResponse
from openapi_server.models.get_import_job_response import GetImportJobResponse
from openapi_server.models.get_import_jobs_response import GetImportJobsResponse
from openapi_server.models.get_in_app_messages_response import GetInAppMessagesResponse
from openapi_server.models.get_in_app_template_response import GetInAppTemplateResponse
from openapi_server.models.get_journey_date_range_kpi_response import GetJourneyDateRangeKpiResponse
from openapi_server.models.get_journey_execution_activity_metrics_response import GetJourneyExecutionActivityMetricsResponse
from openapi_server.models.get_journey_execution_metrics_response import GetJourneyExecutionMetricsResponse
from openapi_server.models.get_journey_response import GetJourneyResponse
from openapi_server.models.get_journey_run_execution_activity_metrics_response import GetJourneyRunExecutionActivityMetricsResponse
from openapi_server.models.get_journey_run_execution_metrics_response import GetJourneyRunExecutionMetricsResponse
from openapi_server.models.get_journey_runs_response import GetJourneyRunsResponse
from openapi_server.models.get_push_template_response import GetPushTemplateResponse
from openapi_server.models.get_recommender_configuration_response import GetRecommenderConfigurationResponse
from openapi_server.models.get_recommender_configurations_response import GetRecommenderConfigurationsResponse
from openapi_server.models.get_segment_export_jobs_response import GetSegmentExportJobsResponse
from openapi_server.models.get_segment_import_jobs_response import GetSegmentImportJobsResponse
from openapi_server.models.get_segment_response import GetSegmentResponse
from openapi_server.models.get_segment_version_response import GetSegmentVersionResponse
from openapi_server.models.get_segment_versions_response import GetSegmentVersionsResponse
from openapi_server.models.get_segments_response import GetSegmentsResponse
from openapi_server.models.get_sms_channel_response import GetSmsChannelResponse
from openapi_server.models.get_sms_template_response import GetSmsTemplateResponse
from openapi_server.models.get_user_endpoints_response import GetUserEndpointsResponse
from openapi_server.models.get_voice_channel_response import GetVoiceChannelResponse
from openapi_server.models.get_voice_template_response import GetVoiceTemplateResponse
from openapi_server.models.list_journeys_response import ListJourneysResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_template_versions_response import ListTemplateVersionsResponse
from openapi_server.models.list_templates_response import ListTemplatesResponse
from openapi_server.models.phone_number_validate_request import PhoneNumberValidateRequest
from openapi_server.models.phone_number_validate_response import PhoneNumberValidateResponse
from openapi_server.models.put_event_stream_request import PutEventStreamRequest
from openapi_server.models.put_event_stream_response import PutEventStreamResponse
from openapi_server.models.put_events_request import PutEventsRequest
from openapi_server.models.put_events_response import PutEventsResponse
from openapi_server.models.remove_attributes_request import RemoveAttributesRequest
from openapi_server.models.remove_attributes_response import RemoveAttributesResponse
from openapi_server.models.send_messages_request import SendMessagesRequest
from openapi_server.models.send_messages_response import SendMessagesResponse
from openapi_server.models.send_otp_message_request import SendOTPMessageRequest
from openapi_server.models.send_otp_message_response import SendOTPMessageResponse
from openapi_server.models.send_users_messages_request import SendUsersMessagesRequest
from openapi_server.models.send_users_messages_response import SendUsersMessagesResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_adm_channel_request import UpdateAdmChannelRequest
from openapi_server.models.update_adm_channel_response import UpdateAdmChannelResponse
from openapi_server.models.update_apns_channel_request import UpdateApnsChannelRequest
from openapi_server.models.update_apns_channel_response import UpdateApnsChannelResponse
from openapi_server.models.update_apns_sandbox_channel_request import UpdateApnsSandboxChannelRequest
from openapi_server.models.update_apns_sandbox_channel_response import UpdateApnsSandboxChannelResponse
from openapi_server.models.update_apns_voip_channel_request import UpdateApnsVoipChannelRequest
from openapi_server.models.update_apns_voip_channel_response import UpdateApnsVoipChannelResponse
from openapi_server.models.update_apns_voip_sandbox_channel_request import UpdateApnsVoipSandboxChannelRequest
from openapi_server.models.update_apns_voip_sandbox_channel_response import UpdateApnsVoipSandboxChannelResponse
from openapi_server.models.update_application_settings_request import UpdateApplicationSettingsRequest
from openapi_server.models.update_application_settings_response import UpdateApplicationSettingsResponse
from openapi_server.models.update_baidu_channel_request import UpdateBaiduChannelRequest
from openapi_server.models.update_baidu_channel_response import UpdateBaiduChannelResponse
from openapi_server.models.update_campaign_response import UpdateCampaignResponse
from openapi_server.models.update_email_channel_request import UpdateEmailChannelRequest
from openapi_server.models.update_email_channel_response import UpdateEmailChannelResponse
from openapi_server.models.update_email_template_request import UpdateEmailTemplateRequest
from openapi_server.models.update_email_template_response import UpdateEmailTemplateResponse
from openapi_server.models.update_endpoint_request import UpdateEndpointRequest
from openapi_server.models.update_endpoint_response import UpdateEndpointResponse
from openapi_server.models.update_endpoints_batch_request import UpdateEndpointsBatchRequest
from openapi_server.models.update_endpoints_batch_response import UpdateEndpointsBatchResponse
from openapi_server.models.update_gcm_channel_request import UpdateGcmChannelRequest
from openapi_server.models.update_gcm_channel_response import UpdateGcmChannelResponse
from openapi_server.models.update_in_app_template_request import UpdateInAppTemplateRequest
from openapi_server.models.update_in_app_template_response import UpdateInAppTemplateResponse
from openapi_server.models.update_journey_response import UpdateJourneyResponse
from openapi_server.models.update_journey_state_request import UpdateJourneyStateRequest
from openapi_server.models.update_journey_state_response import UpdateJourneyStateResponse
from openapi_server.models.update_push_template_request import UpdatePushTemplateRequest
from openapi_server.models.update_push_template_response import UpdatePushTemplateResponse
from openapi_server.models.update_recommender_configuration_request import UpdateRecommenderConfigurationRequest
from openapi_server.models.update_recommender_configuration_response import UpdateRecommenderConfigurationResponse
from openapi_server.models.update_segment_response import UpdateSegmentResponse
from openapi_server.models.update_sms_channel_request import UpdateSmsChannelRequest
from openapi_server.models.update_sms_channel_response import UpdateSmsChannelResponse
from openapi_server.models.update_sms_template_request import UpdateSmsTemplateRequest
from openapi_server.models.update_sms_template_response import UpdateSmsTemplateResponse
from openapi_server.models.update_template_active_version_request import UpdateTemplateActiveVersionRequest
from openapi_server.models.update_template_active_version_response import UpdateTemplateActiveVersionResponse
from openapi_server.models.update_voice_channel_request import UpdateVoiceChannelRequest
from openapi_server.models.update_voice_channel_response import UpdateVoiceChannelResponse
from openapi_server.models.update_voice_template_request import UpdateVoiceTemplateRequest
from openapi_server.models.update_voice_template_response import UpdateVoiceTemplateResponse
from openapi_server.models.verify_otp_message_request import VerifyOTPMessageRequest
from openapi_server.models.verify_otp_message_response import VerifyOTPMessageResponse
from openapi_server import util


async def create_app(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app

     &lt;p&gt;Creates an application.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppRequest.from_dict(body)
    return web.Response(status=200)


async def create_campaign(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_campaign

    Creates a new campaign for an application or updates the settings of an existing campaign for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def create_email_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_email_template

    Creates a message template for messages that are sent through the email channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_export_job(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_export_job

    Creates an export job for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateExportJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_import_job(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_import_job

    Creates an import job for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_in_app_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_in_app_template

    Creates a new message template for messages using the in-app message channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateInAppTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_journey(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_journey

    Creates a journey for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateJourneyRequest.from_dict(body)
    return web.Response(status=200)


async def create_push_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_push_template

    Creates a message template for messages that are sent through a push notification channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePushTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_recommender_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_recommender_configuration

    Creates an Amazon Pinpoint configuration for a recommender model.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRecommenderConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def create_segment(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_segment

    Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that&#39;s associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSegmentRequest.from_dict(body)
    return web.Response(status=200)


async def create_sms_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sms_template

    Creates a message template for messages that are sent through the SMS channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSmsTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_voice_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_voice_template

    Creates a message template for messages that are sent through the voice channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateVoiceTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_adm_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_adm_channel

    Disables the ADM channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_apns_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_apns_channel

    Disables the APNs channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_apns_sandbox_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_apns_sandbox_channel

    Disables the APNs sandbox channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_apns_voip_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_apns_voip_channel

    Disables the APNs VoIP channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_apns_voip_sandbox_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_apns_voip_sandbox_channel

    Disables the APNs VoIP sandbox channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_app(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app

    Deletes an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_baidu_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_baidu_channel

    Disables the Baidu channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_campaign(request: web.Request, application_id, campaign_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_campaign

    Deletes a campaign from an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param campaign_id: The unique identifier for the campaign.
    :type campaign_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_email_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_email_channel

    Disables the email channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_email_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """delete_email_template

    Deletes a message template for messages that were sent through the email channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def delete_endpoint(request: web.Request, application_id, endpoint_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_endpoint

    Deletes an endpoint from an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param endpoint_id: The unique identifier for the endpoint.
    :type endpoint_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_event_stream(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_event_stream

    Deletes the event stream for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_gcm_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_gcm_channel

    Disables the GCM channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_in_app_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """delete_in_app_template

    Deletes a message template for messages sent using the in-app message channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def delete_journey(request: web.Request, application_id, journey_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_journey

    Deletes a journey from an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_push_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """delete_push_template

    Deletes a message template for messages that were sent through a push notification channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def delete_recommender_configuration(request: web.Request, recommender_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_recommender_configuration

    Deletes an Amazon Pinpoint configuration for a recommender model.

    :param recommender_id: The unique identifier for the recommender model configuration. This identifier is displayed as the &lt;b&gt;Recommender ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type recommender_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_segment(request: web.Request, application_id, segment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_segment

    Deletes a segment from an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param segment_id: The unique identifier for the segment.
    :type segment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_sms_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sms_channel

    Disables the SMS channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_sms_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """delete_sms_template

    Deletes a message template for messages that were sent through the SMS channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def delete_user_endpoints(request: web.Request, application_id, user_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user_endpoints

    Deletes all the endpoints that are associated with a specific user ID.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param user_id: The unique identifier for the user.
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


async def delete_voice_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_voice_channel

    Disables the voice channel for an application and deletes any existing settings for the channel.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_voice_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """delete_voice_template

    Deletes a message template for messages that were sent through the voice channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def get_adm_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_adm_channel

    Retrieves information about the status and settings of the ADM channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_apns_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_apns_channel

    Retrieves information about the status and settings of the APNs channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_apns_sandbox_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_apns_sandbox_channel

    Retrieves information about the status and settings of the APNs sandbox channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_apns_voip_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_apns_voip_channel

    Retrieves information about the status and settings of the APNs VoIP channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_apns_voip_sandbox_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_apns_voip_sandbox_channel

    Retrieves information about the status and settings of the APNs VoIP sandbox channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_app(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_app

    Retrieves information about an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_application_date_range_kpi(request: web.Request, application_id, kpi_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, end_time=None, next_token=None, page_size=None, start_time=None) -> web.Response:
    """get_application_date_range_kpi

    Retrieves (queries) pre-aggregated data for a standard metric that applies to an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param kpi_name: The name of the metric, also referred to as a &lt;i&gt;key performance indicator (KPI)&lt;/i&gt;, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\&quot;&gt;Amazon Pinpoint Developer Guide&lt;/a&gt;.
    :type kpi_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param end_time: The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.
    :type end_time: str
    :param next_token: The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param start_time: The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.
    :type start_time: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def get_application_settings(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_application_settings

    Retrieves information about the settings for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_apps(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_apps

    Retrieves information about all the applications that are associated with your Amazon Pinpoint account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_baidu_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_baidu_channel

    Retrieves information about the status and settings of the Baidu channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_campaign(request: web.Request, application_id, campaign_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_campaign

    Retrieves information about the status, configuration, and other settings for a campaign.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param campaign_id: The unique identifier for the campaign.
    :type campaign_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_campaign_activities(request: web.Request, application_id, campaign_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_campaign_activities

    Retrieves information about all the activities for a campaign.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param campaign_id: The unique identifier for the campaign.
    :type campaign_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_campaign_date_range_kpi(request: web.Request, application_id, campaign_id, kpi_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, end_time=None, next_token=None, page_size=None, start_time=None) -> web.Response:
    """get_campaign_date_range_kpi

    Retrieves (queries) pre-aggregated data for a standard metric that applies to a campaign.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param campaign_id: The unique identifier for the campaign.
    :type campaign_id: str
    :param kpi_name: The name of the metric, also referred to as a &lt;i&gt;key performance indicator (KPI)&lt;/i&gt;, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\&quot;&gt;Amazon Pinpoint Developer Guide&lt;/a&gt;.
    :type kpi_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param end_time: The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.
    :type end_time: str
    :param next_token: The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param start_time: The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.
    :type start_time: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def get_campaign_version(request: web.Request, application_id, campaign_id, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_campaign_version

    Retrieves information about the status, configuration, and other settings for a specific version of a campaign.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param campaign_id: The unique identifier for the campaign.
    :type campaign_id: str
    :param version: The unique version number (Version property) for the campaign version.
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_campaign_versions(request: web.Request, application_id, campaign_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_campaign_versions

    Retrieves information about the status, configuration, and other settings for all versions of a campaign.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param campaign_id: The unique identifier for the campaign.
    :type campaign_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_campaigns(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_campaigns

    Retrieves information about the status, configuration, and other settings for all the campaigns that are associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_channels(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_channels

    Retrieves information about the history and status of each channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_email_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_email_channel

    Retrieves information about the status and settings of the email channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_email_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """get_email_template

    Retrieves the content and settings of a message template for messages that are sent through the email channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def get_endpoint(request: web.Request, application_id, endpoint_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_endpoint

    Retrieves information about the settings and attributes of a specific endpoint for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param endpoint_id: The unique identifier for the endpoint.
    :type endpoint_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_event_stream(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_event_stream

    Retrieves information about the event stream settings for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_export_job(request: web.Request, application_id, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_export_job

    Retrieves information about the status and settings of a specific export job for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param job_id: The unique identifier for the job.
    :type job_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_export_jobs(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_export_jobs

    Retrieves information about the status and settings of all the export jobs for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_gcm_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_gcm_channel

    Retrieves information about the status and settings of the GCM channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_import_job(request: web.Request, application_id, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_import_job

    Retrieves information about the status and settings of a specific import job for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param job_id: The unique identifier for the job.
    :type job_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_import_jobs(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_import_jobs

    Retrieves information about the status and settings of all the import jobs for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_in_app_messages(request: web.Request, application_id, endpoint_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_in_app_messages

    Retrieves the in-app messages targeted for the provided endpoint ID.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param endpoint_id: The unique identifier for the endpoint.
    :type endpoint_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_in_app_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """get_in_app_template

    Retrieves the content and settings of a message template for messages sent through the in-app channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def get_journey(request: web.Request, application_id, journey_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_journey

    Retrieves information about the status, configuration, and other settings for a journey.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_journey_date_range_kpi(request: web.Request, application_id, journey_id, kpi_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, end_time=None, next_token=None, page_size=None, start_time=None) -> web.Response:
    """get_journey_date_range_kpi

    Retrieves (queries) pre-aggregated data for a standard engagement metric that applies to a journey.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param kpi_name: The name of the metric, also referred to as a &lt;i&gt;key performance indicator (KPI)&lt;/i&gt;, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\&quot;&gt;Amazon Pinpoint Developer Guide&lt;/a&gt;.
    :type kpi_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param end_time: The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.
    :type end_time: str
    :param next_token: The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param start_time: The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.
    :type start_time: str

    """
    end_time = util.deserialize_datetime(end_time)
    start_time = util.deserialize_datetime(start_time)
    return web.Response(status=200)


async def get_journey_execution_activity_metrics(request: web.Request, application_id, journey_activity_id, journey_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """get_journey_execution_activity_metrics

    Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey activity.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_activity_id: The unique identifier for the journey activity.
    :type journey_activity_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str

    """
    return web.Response(status=200)


async def get_journey_execution_metrics(request: web.Request, application_id, journey_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """get_journey_execution_metrics

    Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str

    """
    return web.Response(status=200)


async def get_journey_run_execution_activity_metrics(request: web.Request, application_id, journey_activity_id, journey_id, run_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """get_journey_run_execution_activity_metrics

    Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey activity.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_activity_id: The unique identifier for the journey activity.
    :type journey_activity_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param run_id: The unique identifier for the journey run.
    :type run_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str

    """
    return web.Response(status=200)


async def get_journey_run_execution_metrics(request: web.Request, application_id, journey_id, run_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """get_journey_run_execution_metrics

    Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param run_id: The unique identifier for the journey run.
    :type run_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str

    """
    return web.Response(status=200)


async def get_journey_runs(request: web.Request, application_id, journey_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_journey_runs

    Provides information about the runs of a journey.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_push_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """get_push_template

    Retrieves the content and settings of a message template for messages that are sent through a push notification channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def get_recommender_configuration(request: web.Request, recommender_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_recommender_configuration

    Retrieves information about an Amazon Pinpoint configuration for a recommender model.

    :param recommender_id: The unique identifier for the recommender model configuration. This identifier is displayed as the &lt;b&gt;Recommender ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type recommender_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_recommender_configurations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_recommender_configurations

    Retrieves information about all the recommender model configurations that are associated with your Amazon Pinpoint account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_segment(request: web.Request, application_id, segment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_segment

    Retrieves information about the configuration, dimension, and other settings for a specific segment that&#39;s associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param segment_id: The unique identifier for the segment.
    :type segment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_segment_export_jobs(request: web.Request, application_id, segment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_segment_export_jobs

    Retrieves information about the status and settings of the export jobs for a segment.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param segment_id: The unique identifier for the segment.
    :type segment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_segment_import_jobs(request: web.Request, application_id, segment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_segment_import_jobs

    Retrieves information about the status and settings of the import jobs for a segment.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param segment_id: The unique identifier for the segment.
    :type segment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_segment_version(request: web.Request, application_id, segment_id, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_segment_version

    Retrieves information about the configuration, dimension, and other settings for a specific version of a segment that&#39;s associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param segment_id: The unique identifier for the segment.
    :type segment_id: str
    :param version: The unique version number (Version property) for the campaign version.
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_segment_versions(request: web.Request, application_id, segment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_segment_versions

    Retrieves information about the configuration, dimension, and other settings for all the versions of a specific segment that&#39;s associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param segment_id: The unique identifier for the segment.
    :type segment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_segments(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """get_segments

    Retrieves information about the configuration, dimension, and other settings for all the segments that are associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def get_sms_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sms_channel

    Retrieves information about the status and settings of the SMS channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_sms_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """get_sms_template

    Retrieves the content and settings of a message template for messages that are sent through the SMS channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def get_user_endpoints(request: web.Request, application_id, user_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_user_endpoints

    Retrieves information about all the endpoints that are associated with a specific user ID.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param user_id: The unique identifier for the user.
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


async def get_voice_channel(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_voice_channel

    Retrieves information about the status and settings of the voice channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_voice_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """get_voice_template

    Retrieves the content and settings of a message template for messages that are sent through the voice channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    return web.Response(status=200)


async def list_journeys(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, token=None) -> web.Response:
    """list_journeys

    Retrieves information about the status, configuration, and other settings for all the journeys that are associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param token: The NextToken string that specifies which page of results to return in a paginated response.
    :type token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Retrieves all the tags (keys and values) that are associated with an application, campaign, message template, or segment.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
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


async def list_template_versions(request: web.Request, template_name, template_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_template_versions

    Retrieves information about all the versions of a specific message template.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param template_type: The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.
    :type template_type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str

    """
    return web.Response(status=200)


async def list_templates(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None, prefix=None, template_type=None) -> web.Response:
    """list_templates

    Retrieves information about all the message templates that are associated with your Amazon Pinpoint account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type next_token: str
    :param page_size: The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
    :type page_size: str
    :param prefix: The substring to match in the names of the message templates to include in the results. If you specify this value, Amazon Pinpoint returns only those templates whose names begin with the value that you specify.
    :type prefix: str
    :param template_type: The type of message template to include in the results. Valid values are: EMAIL, PUSH, SMS, and VOICE. To include all types of templates in the results, don&#39;t include this parameter in your request.
    :type template_type: str

    """
    return web.Response(status=200)


async def phone_number_validate(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """phone_number_validate

    Retrieves information about a phone number.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PhoneNumberValidateRequest.from_dict(body)
    return web.Response(status=200)


async def put_event_stream(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_event_stream

    Creates a new event stream for an application or updates the settings of an existing event stream for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEventStreamRequest.from_dict(body)
    return web.Response(status=200)


async def put_events(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_events

    Creates a new event to record for endpoints, or creates or updates endpoint data that existing events are associated with.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEventsRequest.from_dict(body)
    return web.Response(status=200)


async def remove_attributes(request: web.Request, application_id, attribute_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_attributes

    Removes one or more attributes, of the same attribute type, from all the endpoints that are associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param attribute_type:  &lt;p&gt;The type of attribute or attributes to remove. Valid values are:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;endpoint-custom-attributes - Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;endpoint-user-attributes - Custom attributes that describe users, such as first name, last name, and age.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type attribute_type: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RemoveAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def send_messages(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_messages

    Creates and sends a direct message.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SendMessagesRequest.from_dict(body)
    return web.Response(status=200)


async def send_otp_message(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_otp_message

    Send an OTP message

    :param application_id: The unique ID of your Amazon Pinpoint application.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SendOTPMessageRequest.from_dict(body)
    return web.Response(status=200)


async def send_users_messages(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_users_messages

    Creates and sends a message to a list of users.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SendUsersMessagesRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds one or more tags (keys and values) to an application, campaign, message template, or segment.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
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


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags (keys and values) from an application, campaign, message template, or segment.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
    :param tag_keys: The key of the tag to remove from the resource. To remove multiple tags, append the tagKeys parameter and argument for each additional tag to remove, separated by an ampersand (&amp;amp;).
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def update_adm_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_adm_channel

    Enables the ADM channel for an application or updates the status and settings of the ADM channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAdmChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_apns_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_apns_channel

    Enables the APNs channel for an application or updates the status and settings of the APNs channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateApnsChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_apns_sandbox_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_apns_sandbox_channel

    Enables the APNs sandbox channel for an application or updates the status and settings of the APNs sandbox channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateApnsSandboxChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_apns_voip_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_apns_voip_channel

    Enables the APNs VoIP channel for an application or updates the status and settings of the APNs VoIP channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateApnsVoipChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_apns_voip_sandbox_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_apns_voip_sandbox_channel

    Enables the APNs VoIP sandbox channel for an application or updates the status and settings of the APNs VoIP sandbox channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateApnsVoipSandboxChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_application_settings(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_application_settings

    Updates the settings for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateApplicationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_baidu_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_baidu_channel

    Enables the Baidu channel for an application or updates the status and settings of the Baidu channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateBaiduChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_campaign(request: web.Request, application_id, campaign_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_campaign

    Updates the configuration and other settings for a campaign.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param campaign_id: The unique identifier for the campaign.
    :type campaign_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def update_email_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_email_channel

    Enables the email channel for an application or updates the status and settings of the email channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEmailChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_email_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, create_new_version=None, version=None) -> web.Response:
    """update_email_template

    Updates an existing message template for messages that are sent through the email channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param create_new_version: &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt;
    :type create_new_version: bool
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    body = UpdateEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_endpoint(request: web.Request, application_id, endpoint_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_endpoint

    Creates a new endpoint for an application or updates the settings and attributes of an existing endpoint for an application. You can also use this operation to define custom attributes for an endpoint. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param endpoint_id: The unique identifier for the endpoint.
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def update_endpoints_batch(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_endpoints_batch

    Creates a new batch of endpoints for an application or updates the settings and attributes of a batch of existing endpoints for an application. You can also use this operation to define custom attributes for a batch of endpoints. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEndpointsBatchRequest.from_dict(body)
    return web.Response(status=200)


async def update_gcm_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_gcm_channel

    Enables the GCM channel for an application or updates the status and settings of the GCM channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateGcmChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_in_app_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, create_new_version=None, version=None) -> web.Response:
    """update_in_app_template

    Updates an existing message template for messages sent through the in-app message channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param create_new_version: &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt;
    :type create_new_version: bool
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    body = UpdateInAppTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_journey(request: web.Request, application_id, journey_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_journey

    Updates the configuration and other settings for a journey.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateJourneyRequest.from_dict(body)
    return web.Response(status=200)


async def update_journey_state(request: web.Request, application_id, journey_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_journey_state

    Cancels (stops) an active journey.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param journey_id: The unique identifier for the journey.
    :type journey_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateJourneyStateRequest.from_dict(body)
    return web.Response(status=200)


async def update_push_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, create_new_version=None, version=None) -> web.Response:
    """update_push_template

    Updates an existing message template for messages that are sent through a push notification channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param create_new_version: &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt;
    :type create_new_version: bool
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    body = UpdatePushTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_recommender_configuration(request: web.Request, recommender_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_recommender_configuration

    Updates an Amazon Pinpoint configuration for a recommender model.

    :param recommender_id: The unique identifier for the recommender model configuration. This identifier is displayed as the &lt;b&gt;Recommender ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type recommender_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRecommenderConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_segment(request: web.Request, application_id, segment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_segment

    Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that&#39;s associated with an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param segment_id: The unique identifier for the segment.
    :type segment_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSegmentRequest.from_dict(body)
    return web.Response(status=200)


async def update_sms_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sms_channel

    Enables the SMS channel for an application or updates the status and settings of the SMS channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSmsChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_sms_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, create_new_version=None, version=None) -> web.Response:
    """update_sms_template

    Updates an existing message template for messages that are sent through the SMS channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param create_new_version: &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt;
    :type create_new_version: bool
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    body = UpdateSmsTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_template_active_version(request: web.Request, template_name, template_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_template_active_version

    Changes the status of a specific version of a message template to &lt;i&gt;active&lt;/i&gt;.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param template_type: The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.
    :type template_type: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTemplateActiveVersionRequest.from_dict(body)
    return web.Response(status=200)


async def update_voice_channel(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_voice_channel

    Enables the voice channel for an application or updates the status and settings of the voice channel for an application.

    :param application_id: The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateVoiceChannelRequest.from_dict(body)
    return web.Response(status=200)


async def update_voice_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, create_new_version=None, version=None) -> web.Response:
    """update_voice_template

    Updates an existing message template for messages that are sent through the voice channel.

    :param template_name: The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    :type template_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param create_new_version: &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt;
    :type create_new_version: bool
    :param version: &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;
    :type version: str

    """
    body = UpdateVoiceTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def verify_otp_message(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """verify_otp_message

    Verify an OTP

    :param application_id: The unique ID of your Amazon Pinpoint application.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = VerifyOTPMessageRequest.from_dict(body)
    return web.Response(status=200)
