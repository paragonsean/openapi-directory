from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_evaluation_form_request import ActivateEvaluationFormRequest
from openapi_server.models.activate_evaluation_form_response import ActivateEvaluationFormResponse
from openapi_server.models.agent_status_type import AgentStatusType
from openapi_server.models.associate_approved_origin_request import AssociateApprovedOriginRequest
from openapi_server.models.associate_bot_request import AssociateBotRequest
from openapi_server.models.associate_default_vocabulary_request import AssociateDefaultVocabularyRequest
from openapi_server.models.associate_instance_storage_config_request import AssociateInstanceStorageConfigRequest
from openapi_server.models.associate_instance_storage_config_response import AssociateInstanceStorageConfigResponse
from openapi_server.models.associate_lambda_function_request import AssociateLambdaFunctionRequest
from openapi_server.models.associate_lex_bot_request import AssociateLexBotRequest
from openapi_server.models.associate_phone_number_contact_flow_request import AssociatePhoneNumberContactFlowRequest
from openapi_server.models.associate_queue_quick_connects_request import AssociateQueueQuickConnectsRequest
from openapi_server.models.associate_routing_profile_queues_request import AssociateRoutingProfileQueuesRequest
from openapi_server.models.associate_security_key_request import AssociateSecurityKeyRequest
from openapi_server.models.associate_security_key_response import AssociateSecurityKeyResponse
from openapi_server.models.claim_phone_number_request import ClaimPhoneNumberRequest
from openapi_server.models.claim_phone_number_response import ClaimPhoneNumberResponse
from openapi_server.models.contact_flow_type import ContactFlowType
from openapi_server.models.create_agent_status_request import CreateAgentStatusRequest
from openapi_server.models.create_agent_status_response import CreateAgentStatusResponse
from openapi_server.models.create_contact_flow_module_request import CreateContactFlowModuleRequest
from openapi_server.models.create_contact_flow_module_response import CreateContactFlowModuleResponse
from openapi_server.models.create_contact_flow_request import CreateContactFlowRequest
from openapi_server.models.create_contact_flow_response import CreateContactFlowResponse
from openapi_server.models.create_evaluation_form_request import CreateEvaluationFormRequest
from openapi_server.models.create_evaluation_form_response import CreateEvaluationFormResponse
from openapi_server.models.create_hours_of_operation_request import CreateHoursOfOperationRequest
from openapi_server.models.create_hours_of_operation_response import CreateHoursOfOperationResponse
from openapi_server.models.create_instance_request import CreateInstanceRequest
from openapi_server.models.create_instance_response import CreateInstanceResponse
from openapi_server.models.create_integration_association_request import CreateIntegrationAssociationRequest
from openapi_server.models.create_integration_association_response import CreateIntegrationAssociationResponse
from openapi_server.models.create_participant_request import CreateParticipantRequest
from openapi_server.models.create_participant_response import CreateParticipantResponse
from openapi_server.models.create_prompt_request import CreatePromptRequest
from openapi_server.models.create_prompt_response import CreatePromptResponse
from openapi_server.models.create_queue_request import CreateQueueRequest
from openapi_server.models.create_queue_response import CreateQueueResponse
from openapi_server.models.create_quick_connect_request import CreateQuickConnectRequest
from openapi_server.models.create_quick_connect_response import CreateQuickConnectResponse
from openapi_server.models.create_routing_profile_request import CreateRoutingProfileRequest
from openapi_server.models.create_routing_profile_response import CreateRoutingProfileResponse
from openapi_server.models.create_rule_request import CreateRuleRequest
from openapi_server.models.create_rule_response import CreateRuleResponse
from openapi_server.models.create_security_profile_request import CreateSecurityProfileRequest
from openapi_server.models.create_security_profile_response import CreateSecurityProfileResponse
from openapi_server.models.create_task_template_request import CreateTaskTemplateRequest
from openapi_server.models.create_task_template_response import CreateTaskTemplateResponse
from openapi_server.models.create_traffic_distribution_group_request import CreateTrafficDistributionGroupRequest
from openapi_server.models.create_traffic_distribution_group_response import CreateTrafficDistributionGroupResponse
from openapi_server.models.create_use_case_request import CreateUseCaseRequest
from openapi_server.models.create_use_case_response import CreateUseCaseResponse
from openapi_server.models.create_user_hierarchy_group_request import CreateUserHierarchyGroupRequest
from openapi_server.models.create_user_hierarchy_group_response import CreateUserHierarchyGroupResponse
from openapi_server.models.create_user_request import CreateUserRequest
from openapi_server.models.create_user_response import CreateUserResponse
from openapi_server.models.create_vocabulary_request import CreateVocabularyRequest
from openapi_server.models.create_vocabulary_response import CreateVocabularyResponse
from openapi_server.models.deactivate_evaluation_form_request import DeactivateEvaluationFormRequest
from openapi_server.models.deactivate_evaluation_form_response import DeactivateEvaluationFormResponse
from openapi_server.models.delete_vocabulary_response import DeleteVocabularyResponse
from openapi_server.models.describe_agent_status_response import DescribeAgentStatusResponse
from openapi_server.models.describe_contact_evaluation_response import DescribeContactEvaluationResponse
from openapi_server.models.describe_contact_flow_module_response import DescribeContactFlowModuleResponse
from openapi_server.models.describe_contact_flow_response import DescribeContactFlowResponse
from openapi_server.models.describe_contact_response import DescribeContactResponse
from openapi_server.models.describe_evaluation_form_response import DescribeEvaluationFormResponse
from openapi_server.models.describe_hours_of_operation_response import DescribeHoursOfOperationResponse
from openapi_server.models.describe_instance_attribute_response import DescribeInstanceAttributeResponse
from openapi_server.models.describe_instance_response import DescribeInstanceResponse
from openapi_server.models.describe_instance_storage_config_response import DescribeInstanceStorageConfigResponse
from openapi_server.models.describe_phone_number_response import DescribePhoneNumberResponse
from openapi_server.models.describe_prompt_response import DescribePromptResponse
from openapi_server.models.describe_queue_response import DescribeQueueResponse
from openapi_server.models.describe_quick_connect_response import DescribeQuickConnectResponse
from openapi_server.models.describe_routing_profile_response import DescribeRoutingProfileResponse
from openapi_server.models.describe_rule_response import DescribeRuleResponse
from openapi_server.models.describe_security_profile_response import DescribeSecurityProfileResponse
from openapi_server.models.describe_traffic_distribution_group_response import DescribeTrafficDistributionGroupResponse
from openapi_server.models.describe_user_hierarchy_group_response import DescribeUserHierarchyGroupResponse
from openapi_server.models.describe_user_hierarchy_structure_response import DescribeUserHierarchyStructureResponse
from openapi_server.models.describe_user_response import DescribeUserResponse
from openapi_server.models.describe_vocabulary_response import DescribeVocabularyResponse
from openapi_server.models.disassociate_queue_quick_connects_request import DisassociateQueueQuickConnectsRequest
from openapi_server.models.disassociate_routing_profile_queues_request import DisassociateRoutingProfileQueuesRequest
from openapi_server.models.dismiss_user_contact_request import DismissUserContactRequest
from openapi_server.models.get_contact_attributes_response import GetContactAttributesResponse
from openapi_server.models.get_current_metric_data_request import GetCurrentMetricDataRequest
from openapi_server.models.get_current_metric_data_response import GetCurrentMetricDataResponse
from openapi_server.models.get_current_user_data_request import GetCurrentUserDataRequest
from openapi_server.models.get_current_user_data_response import GetCurrentUserDataResponse
from openapi_server.models.get_federation_token_response import GetFederationTokenResponse
from openapi_server.models.get_metric_data_request import GetMetricDataRequest
from openapi_server.models.get_metric_data_response import GetMetricDataResponse
from openapi_server.models.get_metric_data_v2_request import GetMetricDataV2Request
from openapi_server.models.get_metric_data_v2_response import GetMetricDataV2Response
from openapi_server.models.get_prompt_file_response import GetPromptFileResponse
from openapi_server.models.get_task_template_response import GetTaskTemplateResponse
from openapi_server.models.get_traffic_distribution_response import GetTrafficDistributionResponse
from openapi_server.models.list_agent_status_response import ListAgentStatusResponse
from openapi_server.models.list_approved_origins_response import ListApprovedOriginsResponse
from openapi_server.models.list_bots_response import ListBotsResponse
from openapi_server.models.list_contact_evaluations_response import ListContactEvaluationsResponse
from openapi_server.models.list_contact_flow_modules_response import ListContactFlowModulesResponse
from openapi_server.models.list_contact_flows_response import ListContactFlowsResponse
from openapi_server.models.list_contact_references_response import ListContactReferencesResponse
from openapi_server.models.list_default_vocabularies_request import ListDefaultVocabulariesRequest
from openapi_server.models.list_default_vocabularies_response import ListDefaultVocabulariesResponse
from openapi_server.models.list_evaluation_form_versions_response import ListEvaluationFormVersionsResponse
from openapi_server.models.list_evaluation_forms_response import ListEvaluationFormsResponse
from openapi_server.models.list_hours_of_operations_response import ListHoursOfOperationsResponse
from openapi_server.models.list_instance_attributes_response import ListInstanceAttributesResponse
from openapi_server.models.list_instance_storage_configs_response import ListInstanceStorageConfigsResponse
from openapi_server.models.list_instances_response import ListInstancesResponse
from openapi_server.models.list_integration_associations_response import ListIntegrationAssociationsResponse
from openapi_server.models.list_lambda_functions_response import ListLambdaFunctionsResponse
from openapi_server.models.list_lex_bots_response import ListLexBotsResponse
from openapi_server.models.list_phone_numbers_response import ListPhoneNumbersResponse
from openapi_server.models.list_phone_numbers_v2_request import ListPhoneNumbersV2Request
from openapi_server.models.list_phone_numbers_v2_response import ListPhoneNumbersV2Response
from openapi_server.models.list_prompts_response import ListPromptsResponse
from openapi_server.models.list_queue_quick_connects_response import ListQueueQuickConnectsResponse
from openapi_server.models.list_queues_response import ListQueuesResponse
from openapi_server.models.list_quick_connects_response import ListQuickConnectsResponse
from openapi_server.models.list_routing_profile_queues_response import ListRoutingProfileQueuesResponse
from openapi_server.models.list_routing_profiles_response import ListRoutingProfilesResponse
from openapi_server.models.list_rules_response import ListRulesResponse
from openapi_server.models.list_security_keys_response import ListSecurityKeysResponse
from openapi_server.models.list_security_profile_permissions_response import ListSecurityProfilePermissionsResponse
from openapi_server.models.list_security_profiles_response import ListSecurityProfilesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_task_templates_response import ListTaskTemplatesResponse
from openapi_server.models.list_traffic_distribution_groups_response import ListTrafficDistributionGroupsResponse
from openapi_server.models.list_use_cases_response import ListUseCasesResponse
from openapi_server.models.list_user_hierarchy_groups_response import ListUserHierarchyGroupsResponse
from openapi_server.models.list_users_response import ListUsersResponse
from openapi_server.models.monitor_contact_request import MonitorContactRequest
from openapi_server.models.monitor_contact_response import MonitorContactResponse
from openapi_server.models.phone_number_country_code import PhoneNumberCountryCode
from openapi_server.models.phone_number_type import PhoneNumberType
from openapi_server.models.put_user_status_request import PutUserStatusRequest
from openapi_server.models.queue_type import QueueType
from openapi_server.models.quick_connect_type import QuickConnectType
from openapi_server.models.reference_type import ReferenceType
from openapi_server.models.replicate_instance_request import ReplicateInstanceRequest
from openapi_server.models.replicate_instance_response import ReplicateInstanceResponse
from openapi_server.models.resume_contact_recording_request import ResumeContactRecordingRequest
from openapi_server.models.search_available_phone_numbers_request import SearchAvailablePhoneNumbersRequest
from openapi_server.models.search_available_phone_numbers_response import SearchAvailablePhoneNumbersResponse
from openapi_server.models.search_hours_of_operations_request import SearchHoursOfOperationsRequest
from openapi_server.models.search_hours_of_operations_response import SearchHoursOfOperationsResponse
from openapi_server.models.search_prompts_request import SearchPromptsRequest
from openapi_server.models.search_prompts_response import SearchPromptsResponse
from openapi_server.models.search_queues_request import SearchQueuesRequest
from openapi_server.models.search_queues_response import SearchQueuesResponse
from openapi_server.models.search_quick_connects_request import SearchQuickConnectsRequest
from openapi_server.models.search_quick_connects_response import SearchQuickConnectsResponse
from openapi_server.models.search_resource_tags_request import SearchResourceTagsRequest
from openapi_server.models.search_resource_tags_response import SearchResourceTagsResponse
from openapi_server.models.search_routing_profiles_request import SearchRoutingProfilesRequest
from openapi_server.models.search_routing_profiles_response import SearchRoutingProfilesResponse
from openapi_server.models.search_security_profiles_request import SearchSecurityProfilesRequest
from openapi_server.models.search_security_profiles_response import SearchSecurityProfilesResponse
from openapi_server.models.search_users_request import SearchUsersRequest
from openapi_server.models.search_users_response import SearchUsersResponse
from openapi_server.models.search_vocabularies_request import SearchVocabulariesRequest
from openapi_server.models.search_vocabularies_response import SearchVocabulariesResponse
from openapi_server.models.start_chat_contact_request import StartChatContactRequest
from openapi_server.models.start_chat_contact_response import StartChatContactResponse
from openapi_server.models.start_contact_evaluation_request import StartContactEvaluationRequest
from openapi_server.models.start_contact_evaluation_response import StartContactEvaluationResponse
from openapi_server.models.start_contact_recording_request import StartContactRecordingRequest
from openapi_server.models.start_contact_streaming_request import StartContactStreamingRequest
from openapi_server.models.start_contact_streaming_response import StartContactStreamingResponse
from openapi_server.models.start_outbound_voice_contact_request import StartOutboundVoiceContactRequest
from openapi_server.models.start_outbound_voice_contact_response import StartOutboundVoiceContactResponse
from openapi_server.models.start_task_contact_request import StartTaskContactRequest
from openapi_server.models.start_task_contact_response import StartTaskContactResponse
from openapi_server.models.stop_contact_request import StopContactRequest
from openapi_server.models.stop_contact_streaming_request import StopContactStreamingRequest
from openapi_server.models.submit_contact_evaluation_response import SubmitContactEvaluationResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.transfer_contact_request import TransferContactRequest
from openapi_server.models.transfer_contact_response import TransferContactResponse
from openapi_server.models.update_agent_status_request import UpdateAgentStatusRequest
from openapi_server.models.update_contact_attributes_request import UpdateContactAttributesRequest
from openapi_server.models.update_contact_evaluation_request import UpdateContactEvaluationRequest
from openapi_server.models.update_contact_evaluation_response import UpdateContactEvaluationResponse
from openapi_server.models.update_contact_flow_content_request import UpdateContactFlowContentRequest
from openapi_server.models.update_contact_flow_metadata_request import UpdateContactFlowMetadataRequest
from openapi_server.models.update_contact_flow_module_content_request import UpdateContactFlowModuleContentRequest
from openapi_server.models.update_contact_flow_module_metadata_request import UpdateContactFlowModuleMetadataRequest
from openapi_server.models.update_contact_flow_name_request import UpdateContactFlowNameRequest
from openapi_server.models.update_contact_request import UpdateContactRequest
from openapi_server.models.update_contact_schedule_request import UpdateContactScheduleRequest
from openapi_server.models.update_evaluation_form_request import UpdateEvaluationFormRequest
from openapi_server.models.update_evaluation_form_response import UpdateEvaluationFormResponse
from openapi_server.models.update_hours_of_operation_request import UpdateHoursOfOperationRequest
from openapi_server.models.update_instance_attribute_request import UpdateInstanceAttributeRequest
from openapi_server.models.update_instance_storage_config_request import UpdateInstanceStorageConfigRequest
from openapi_server.models.update_participant_role_config_request import UpdateParticipantRoleConfigRequest
from openapi_server.models.update_phone_number_request import UpdatePhoneNumberRequest
from openapi_server.models.update_phone_number_response import UpdatePhoneNumberResponse
from openapi_server.models.update_prompt_request import UpdatePromptRequest
from openapi_server.models.update_prompt_response import UpdatePromptResponse
from openapi_server.models.update_queue_hours_of_operation_request import UpdateQueueHoursOfOperationRequest
from openapi_server.models.update_queue_max_contacts_request import UpdateQueueMaxContactsRequest
from openapi_server.models.update_queue_name_request import UpdateQueueNameRequest
from openapi_server.models.update_queue_outbound_caller_config_request import UpdateQueueOutboundCallerConfigRequest
from openapi_server.models.update_queue_status_request import UpdateQueueStatusRequest
from openapi_server.models.update_quick_connect_config_request import UpdateQuickConnectConfigRequest
from openapi_server.models.update_quick_connect_name_request import UpdateQuickConnectNameRequest
from openapi_server.models.update_routing_profile_agent_availability_timer_request import UpdateRoutingProfileAgentAvailabilityTimerRequest
from openapi_server.models.update_routing_profile_concurrency_request import UpdateRoutingProfileConcurrencyRequest
from openapi_server.models.update_routing_profile_default_outbound_queue_request import UpdateRoutingProfileDefaultOutboundQueueRequest
from openapi_server.models.update_routing_profile_name_request import UpdateRoutingProfileNameRequest
from openapi_server.models.update_routing_profile_queues_request import UpdateRoutingProfileQueuesRequest
from openapi_server.models.update_rule_request import UpdateRuleRequest
from openapi_server.models.update_security_profile_request import UpdateSecurityProfileRequest
from openapi_server.models.update_task_template_request import UpdateTaskTemplateRequest
from openapi_server.models.update_task_template_response import UpdateTaskTemplateResponse
from openapi_server.models.update_traffic_distribution_request import UpdateTrafficDistributionRequest
from openapi_server.models.update_user_hierarchy_group_name_request import UpdateUserHierarchyGroupNameRequest
from openapi_server.models.update_user_hierarchy_request import UpdateUserHierarchyRequest
from openapi_server.models.update_user_hierarchy_structure_request import UpdateUserHierarchyStructureRequest
from openapi_server.models.update_user_identity_info_request import UpdateUserIdentityInfoRequest
from openapi_server.models.update_user_phone_config_request import UpdateUserPhoneConfigRequest
from openapi_server.models.update_user_routing_profile_request import UpdateUserRoutingProfileRequest
from openapi_server.models.update_user_security_profiles_request import UpdateUserSecurityProfilesRequest
from openapi_server import util


async def activate_evaluation_form(request: web.Request, instance_id, evaluation_form_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """activate_evaluation_form

    Activates an evaluation form in the specified Amazon Connect instance. After the evaluation form is activated, it is available to start new evaluations based on the form. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_form_id: The unique identifier for the evaluation form.
    :type evaluation_form_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ActivateEvaluationFormRequest.from_dict(body)
    return web.Response(status=200)


async def associate_approved_origin(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_approved_origin

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates an approved origin to an Amazon Connect instance.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateApprovedOriginRequest.from_dict(body)
    return web.Response(status=200)


async def associate_bot(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_bot

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Allows the specified Amazon Connect instance to access the specified Amazon Lex or Amazon Lex V2 bot.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateBotRequest.from_dict(body)
    return web.Response(status=200)


async def associate_default_vocabulary(request: web.Request, instance_id, language_code, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_default_vocabulary

    Associates an existing vocabulary as the default. Contact Lens for Amazon Connect uses the vocabulary in post-call and real-time analysis sessions for the given language.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param language_code: The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\&quot;&gt;What is Amazon Transcribe?&lt;/a&gt; 
    :type language_code: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateDefaultVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def associate_instance_storage_config(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_instance_storage_config

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates a storage resource type for the first time. You can only associate one type of storage configuration in a single call. This means, for example, that you can&#39;t define an instance with multiple S3 buckets for storing chat transcripts.&lt;/p&gt; &lt;p&gt;This API does not create a resource that doesn&#39;t exist. It only associates it to the instance. Ensure that the resource being specified in the storage configuration, like an S3 bucket, exists when being used for association.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateInstanceStorageConfigRequest.from_dict(body)
    return web.Response(status=200)


async def associate_lambda_function(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_lambda_function

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Allows the specified Amazon Connect instance to access the specified Lambda function.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateLambdaFunctionRequest.from_dict(body)
    return web.Response(status=200)


async def associate_lex_bot(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_lex_bot

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Allows the specified Amazon Connect instance to access the specified Amazon Lex V1 bot. This API only supports the association of Amazon Lex V1 bots.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateLexBotRequest.from_dict(body)
    return web.Response(status=200)


async def associate_phone_number_contact_flow(request: web.Request, phone_number_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_phone_number_contact_flow

    &lt;p&gt;Associates a flow with a phone number claimed to your Amazon Connect instance.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;PhoneNumberId&lt;/code&gt; URI request parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

    :param phone_number_id: A unique identifier for the phone number.
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
    body = AssociatePhoneNumberContactFlowRequest.from_dict(body)
    return web.Response(status=200)


async def associate_queue_quick_connects(request: web.Request, instance_id, queue_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_queue_quick_connects

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates a set of quick connects with a queue.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateQueueQuickConnectsRequest.from_dict(body)
    return web.Response(status=200)


async def associate_routing_profile_queues(request: web.Request, instance_id, routing_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_routing_profile_queues

    Associates a set of queues with a routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateRoutingProfileQueuesRequest.from_dict(body)
    return web.Response(status=200)


async def associate_security_key(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_security_key

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates a security key to the instance.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateSecurityKeyRequest.from_dict(body)
    return web.Response(status=200)


async def claim_phone_number(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """claim_phone_number

    &lt;p&gt;Claims an available phone number to your Amazon Connect instance or traffic distribution group. You can call this API only in the same Amazon Web Services Region where the Amazon Connect instance or traffic distribution group was created.&lt;/p&gt; &lt;p&gt;For more information about how to use this operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/claim-phone-number.html\&quot;&gt;Claim a phone number in your country&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/claim-phone-numbers-traffic-distribution-groups.html\&quot;&gt;Claim phone numbers to traffic distribution groups&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchAvailablePhoneNumbers.html\&quot;&gt;SearchAvailablePhoneNumbers&lt;/a&gt; API for available phone numbers that you can claim. Call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html\&quot;&gt;DescribePhoneNumber&lt;/a&gt; API to verify the status of a previous &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html\&quot;&gt;ClaimPhoneNumber&lt;/a&gt; operation.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you plan to claim and release numbers frequently during a 30 day period, contact us for a service quota exception. Otherwise, it is possible you will be blocked from claiming and releasing any more numbers until 30 days past the oldest number released has expired.&lt;/p&gt; &lt;p&gt;By default you can claim and release up to 200% of your maximum number of active phone numbers during any 30 day period. If you claim and release phone numbers using the UI or API during a rolling 30 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming any more numbers until 30 days past the oldest number released has expired. &lt;/p&gt; &lt;p&gt;For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 30 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an Amazon Web Services support ticket.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ClaimPhoneNumberRequest.from_dict(body)
    return web.Response(status=200)


async def create_agent_status(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_agent_status

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates an agent status for the specified Amazon Connect instance.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAgentStatusRequest.from_dict(body)
    return web.Response(status=200)


async def create_contact_flow(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_contact_flow

    &lt;p&gt;Creates a flow for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateContactFlowRequest.from_dict(body)
    return web.Response(status=200)


async def create_contact_flow_module(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_contact_flow_module

    Creates a flow module for the specified Amazon Connect instance. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateContactFlowModuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_evaluation_form(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_evaluation_form

    Creates an evaluation form in the specified Amazon Connect instance. The form can be used to define questions related to agent performance, and create sections to organize such questions. Question and section identifiers cannot be duplicated within the same evaluation form.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEvaluationFormRequest.from_dict(body)
    return web.Response(status=200)


async def create_hours_of_operation(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_hours_of_operation

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates hours of operation. &lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateHoursOfOperationRequest.from_dict(body)
    return web.Response(status=200)


async def create_instance(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_instance

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Initiates an Amazon Connect instance with all the supported channels enabled. It does not attach any storage, such as Amazon Simple Storage Service (Amazon S3) or Amazon Kinesis. It also does not allow for any configurations on features, such as Contact Lens for Amazon Connect. &lt;/p&gt; &lt;p&gt;Amazon Connect enforces a limit on the total number of instances that you can create or delete in 30 days. If you exceed this limit, you will get an error message indicating there has been an excessive number of attempts at creating or deleting instances. You must wait 30 days before you can restart creating and deleting instances in your account.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def create_integration_association(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_integration_association

    Creates an Amazon Web Services resource association with an Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateIntegrationAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def create_participant(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_participant

    Adds a new participant into an on-going chat contact. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-customize-flow.html\&quot;&gt;Customize chat flow experiences by integrating custom participants&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateParticipantRequest.from_dict(body)
    return web.Response(status=200)


async def create_prompt(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_prompt

    Creates a prompt. For more information about prompts, such as supported file types and maximum length, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/prompts.html\&quot;&gt;Create prompts&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator&#39;s Guide&lt;/i&gt;.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePromptRequest.from_dict(body)
    return web.Response(status=200)


async def create_queue(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_queue

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates a new queue for the specified Amazon Connect instance.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number being used in the input is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;OutboundCallerIdNumberId&lt;/code&gt; value of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_OutboundCallerConfig\&quot;&gt;OutboundCallerConfig&lt;/a&gt; request body parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Only use the phone number ARN format that doesn&#39;t contain &lt;code&gt;instance&lt;/code&gt; in the path, for example, &lt;code&gt;arn:aws:connect:us-east-1:1234567890:phone-number/uuid&lt;/code&gt;. This is the same ARN format that is returned when you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html\&quot;&gt;ListPhoneNumbersV2&lt;/a&gt; API.&lt;/p&gt; &lt;/important&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateQueueRequest.from_dict(body)
    return web.Response(status=200)


async def create_quick_connect(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_quick_connect

    Creates a quick connect for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateQuickConnectRequest.from_dict(body)
    return web.Response(status=200)


async def create_routing_profile(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_routing_profile

    Creates a new routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRoutingProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_rule(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_rule

    &lt;p&gt;Creates a rule for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/connect-rules-language.html\&quot;&gt;Rules Function language&lt;/a&gt; to code conditions for the rule. &lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_security_profile(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_security_profile

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates a security profile.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateSecurityProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_task_template(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_task_template

    Creates a new task template in the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateTaskTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_traffic_distribution_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_traffic_distribution_group

    &lt;p&gt;Creates a traffic distribution group given an Amazon Connect instance that has been replicated. &lt;/p&gt; &lt;p&gt;For more information about creating traffic distribution groups, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html\&quot;&gt;Set up traffic distribution groups&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateTrafficDistributionGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_use_case(request: web.Request, instance_id, integration_association_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_use_case

    Creates a use case for an integration association.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param integration_association_id: The identifier for the integration association.
    :type integration_association_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateUseCaseRequest.from_dict(body)
    return web.Response(status=200)


async def create_user(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user

    &lt;p&gt;Creates a user account for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For information about how to create user accounts using the Amazon Connect console, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html\&quot;&gt;Add Users&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def create_user_hierarchy_group(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user_hierarchy_group

    Creates a new user hierarchy group.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateUserHierarchyGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_vocabulary(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vocabulary

    Creates a custom vocabulary associated with your Amazon Connect instance. You can set a custom vocabulary to be your default vocabulary for a given language. Contact Lens for Amazon Connect uses the default vocabulary in post-call and real-time contact analysis sessions for that language.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateVocabularyRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_evaluation_form(request: web.Request, instance_id, evaluation_form_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deactivate_evaluation_form

    Deactivates an evaluation form in the specified Amazon Connect instance. After a form is deactivated, it is no longer available for users to start new evaluations based on the form. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_form_id: The unique identifier for the evaluation form.
    :type evaluation_form_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeactivateEvaluationFormRequest.from_dict(body)
    return web.Response(status=200)


async def delete_contact_evaluation(request: web.Request, instance_id, evaluation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_contact_evaluation

    Deletes a contact evaluation in the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_id: A unique identifier for the contact evaluation.
    :type evaluation_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_contact_flow(request: web.Request, instance_id, contact_flow_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_contact_flow

    Deletes a flow for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_flow_id: The identifier of the flow.
    :type contact_flow_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_contact_flow_module(request: web.Request, instance_id, contact_flow_module_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_contact_flow_module

    Deletes the specified flow module.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_flow_module_id: The identifier of the flow module.
    :type contact_flow_module_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_evaluation_form(request: web.Request, instance_id, evaluation_form_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """delete_evaluation_form

    &lt;p&gt;Deletes an evaluation form in the specified Amazon Connect instance. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the version property is provided, only the specified version of the evaluation form is deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If no version is provided, then the full form (all versions) is deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_form_id: The unique identifier for the evaluation form.
    :type evaluation_form_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: The unique identifier for the evaluation form.
    :type version: int

    """
    return web.Response(status=200)


async def delete_hours_of_operation(request: web.Request, instance_id, hours_of_operation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_hours_of_operation

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes an hours of operation.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param hours_of_operation_id: The identifier for the hours of operation.
    :type hours_of_operation_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_instance(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_instance

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes the Amazon Connect instance.&lt;/p&gt; &lt;p&gt;Amazon Connect enforces a limit on the total number of instances that you can create or delete in 30 days. If you exceed this limit, you will get an error message indicating there has been an excessive number of attempts at creating or deleting instances. You must wait 30 days before you can restart creating and deleting instances in your account.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_integration_association(request: web.Request, instance_id, integration_association_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_integration_association

    Deletes an Amazon Web Services resource association from an Amazon Connect instance. The association must not have any use cases associated with it.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param integration_association_id: The identifier for the integration association.
    :type integration_association_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_prompt(request: web.Request, instance_id, prompt_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_prompt

    Deletes a prompt.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param prompt_id: A unique identifier for the prompt.
    :type prompt_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_queue(request: web.Request, instance_id, queue_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_queue

    Deletes a queue.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_quick_connect(request: web.Request, instance_id, quick_connect_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_quick_connect

    Deletes a quick connect.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param quick_connect_id: The identifier for the quick connect.
    :type quick_connect_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_routing_profile(request: web.Request, instance_id, routing_profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_routing_profile

    Deletes a routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_rule(request: web.Request, instance_id, rule_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rule

    Deletes a rule for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param rule_id: A unique identifier for the rule.
    :type rule_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_security_profile(request: web.Request, instance_id, security_profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_security_profile

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes a security profile.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param security_profile_id: The identifier for the security profle.
    :type security_profile_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_task_template(request: web.Request, instance_id, task_template_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_task_template

    Deletes the task template.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param task_template_id: A unique identifier for the task template.
    :type task_template_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_traffic_distribution_group(request: web.Request, traffic_distribution_group_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_traffic_distribution_group

    &lt;p&gt;Deletes a traffic distribution group. This API can be called only in the Region where the traffic distribution group is created.&lt;/p&gt; &lt;p&gt;For more information about deleting traffic distribution groups, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/delete-traffic-distribution-groups.html\&quot;&gt;Delete traffic distribution groups&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param traffic_distribution_group_id: The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
    :type traffic_distribution_group_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_use_case(request: web.Request, instance_id, integration_association_id, use_case_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_use_case

    Deletes a use case from an integration association.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param integration_association_id: The identifier for the integration association.
    :type integration_association_id: str
    :param use_case_id: The identifier for the use case.
    :type use_case_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_user(request: web.Request, instance_id, user_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user

    &lt;p&gt;Deletes a user account from the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For information about what happens to a user&#39;s data when their account is deleted, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/delete-users.html\&quot;&gt;Delete Users from Your Amazon Connect Instance&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param user_id: The identifier of the user.
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


async def delete_user_hierarchy_group(request: web.Request, hierarchy_group_id, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user_hierarchy_group

    Deletes an existing user hierarchy group. It must not be associated with any agents or have any active child groups.

    :param hierarchy_group_id: The identifier of the hierarchy group.
    :type hierarchy_group_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_vocabulary(request: web.Request, instance_id, vocabulary_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vocabulary

    Deletes the vocabulary that has the given identifier.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param vocabulary_id: The identifier of the custom vocabulary.
    :type vocabulary_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_agent_status(request: web.Request, instance_id, agent_status_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_agent_status

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes an agent status.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param agent_status_id: The identifier for the agent status.
    :type agent_status_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_contact(request: web.Request, instance_id, contact_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_contact

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the specified contact. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Contact information remains available in Amazon Connect for 24 months, and then it is deleted.&lt;/p&gt; &lt;p&gt;Only data from November 12, 2021, and later is returned by this API.&lt;/p&gt; &lt;/important&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_id: The identifier of the contact.
    :type contact_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_contact_evaluation(request: web.Request, instance_id, evaluation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_contact_evaluation

    Describes a contact evaluation in the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_id: A unique identifier for the contact evaluation.
    :type evaluation_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_contact_flow(request: web.Request, instance_id, contact_flow_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_contact_flow

    &lt;p&gt;Describes the specified flow.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance.
    :type instance_id: str
    :param contact_flow_id: The identifier of the flow.
    :type contact_flow_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_contact_flow_module(request: web.Request, instance_id, contact_flow_module_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_contact_flow_module

    Describes the specified flow module.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_flow_module_id: The identifier of the flow module.
    :type contact_flow_module_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_evaluation_form(request: web.Request, instance_id, evaluation_form_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """describe_evaluation_form

    Describes an evaluation form in the specified Amazon Connect instance. If the version property is not provided, the latest version of the evaluation form is described.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_form_id: A unique identifier for the contact evaluation.
    :type evaluation_form_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: A version of the evaluation form.
    :type version: int

    """
    return web.Response(status=200)


async def describe_hours_of_operation(request: web.Request, instance_id, hours_of_operation_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_hours_of_operation

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the hours of operation.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param hours_of_operation_id: The identifier for the hours of operation.
    :type hours_of_operation_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_instance(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_instance

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns the current state of the specified instance identifier. It tracks the instance while it is being created and returns an error status, if applicable. &lt;/p&gt; &lt;p&gt;If an instance is not created successfully, the instance status reason field returns details relevant to the reason. The instance in a failed state is returned only for 24 hours after the CreateInstance API was invoked.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_instance_attribute(request: web.Request, instance_id, attribute_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_instance_attribute

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the specified instance attribute.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param attribute_type: The type of attribute.
    :type attribute_type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_instance_storage_config(request: web.Request, instance_id, association_id, resource_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_instance_storage_config

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Retrieves the current storage configurations for the specified resource type, association ID, and instance ID.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param association_id: The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
    :type association_id: str
    :param resource_type: A valid resource type.
    :type resource_type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_phone_number(request: web.Request, phone_number_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_phone_number

    &lt;p&gt;Gets details and status of a phone number that’s claimed to your Amazon Connect instance or traffic distribution group.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number is claimed to a traffic distribution group, and you are calling in the Amazon Web Services Region where the traffic distribution group was created, you can use either a phone number ARN or UUID value for the &lt;code&gt;PhoneNumberId&lt;/code&gt; URI request parameter. However, if the number is claimed to a traffic distribution group and you are calling this API in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

    :param phone_number_id: A unique identifier for the phone number.
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


async def describe_prompt(request: web.Request, instance_id, prompt_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_prompt

    Describes the prompt.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param prompt_id: A unique identifier for the prompt.
    :type prompt_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_queue(request: web.Request, instance_id, queue_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_queue

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the specified queue.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_quick_connect(request: web.Request, instance_id, quick_connect_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_quick_connect

    Describes the quick connect.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param quick_connect_id: The identifier for the quick connect.
    :type quick_connect_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_routing_profile(request: web.Request, instance_id, routing_profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_routing_profile

    Describes the specified routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_rule(request: web.Request, instance_id, rule_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_rule

    Describes a rule for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param rule_id: A unique identifier for the rule.
    :type rule_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_security_profile(request: web.Request, security_profile_id, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_security_profile

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Gets basic information about the security profle.&lt;/p&gt;

    :param security_profile_id: The identifier for the security profle.
    :type security_profile_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_traffic_distribution_group(request: web.Request, traffic_distribution_group_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_traffic_distribution_group

    Gets details and status of a traffic distribution group.

    :param traffic_distribution_group_id: The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
    :type traffic_distribution_group_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_user(request: web.Request, user_id, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user

    Describes the specified user account. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID in the Amazon Connect console&lt;/a&gt; (it’s the final part of the ARN). The console does not display the user IDs. Instead, list the users and note the IDs provided in the output.

    :param user_id: The identifier of the user account.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_user_hierarchy_group(request: web.Request, hierarchy_group_id, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user_hierarchy_group

    Describes the specified hierarchy group.

    :param hierarchy_group_id: The identifier of the hierarchy group.
    :type hierarchy_group_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_user_hierarchy_structure(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user_hierarchy_structure

    Describes the hierarchy structure of the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_vocabulary(request: web.Request, instance_id, vocabulary_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_vocabulary

    Describes the specified vocabulary.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param vocabulary_id: The identifier of the custom vocabulary.
    :type vocabulary_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def disassociate_approved_origin(request: web.Request, instance_id, origin, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_approved_origin

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Revokes access to integrated applications from Amazon Connect.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param origin: The domain URL of the integrated application.
    :type origin: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def disassociate_bot(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_bot

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Revokes authorization from the specified instance to access the specified Amazon Lex or Amazon Lex V2 bot. &lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateBotRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_instance_storage_config(request: web.Request, instance_id, association_id, resource_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_instance_storage_config

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Removes the storage type configurations for the specified resource type and association ID.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param association_id: The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
    :type association_id: str
    :param resource_type: A valid resource type.
    :type resource_type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def disassociate_lambda_function(request: web.Request, instance_id, function_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_lambda_function

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Remove the Lambda function from the dropdown options available in the relevant flow blocks.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance..
    :type instance_id: str
    :param function_arn: The Amazon Resource Name (ARN) of the Lambda function being disassociated.
    :type function_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def disassociate_lex_bot(request: web.Request, instance_id, bot_name, lex_region, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_lex_bot

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Revokes authorization from the specified instance to access the specified Amazon Lex bot.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param bot_name: The name of the Amazon Lex bot. Maximum character limit of 50.
    :type bot_name: str
    :param lex_region: The Amazon Web Services Region in which the Amazon Lex bot has been created.
    :type lex_region: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def disassociate_phone_number_contact_flow(request: web.Request, phone_number_id, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_phone_number_contact_flow

    &lt;p&gt;Removes the flow association from a phone number claimed to your Amazon Connect instance.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;PhoneNumberId&lt;/code&gt; URI request parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

    :param phone_number_id: A unique identifier for the phone number.
    :type phone_number_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def disassociate_queue_quick_connects(request: web.Request, instance_id, queue_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_queue_quick_connects

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Disassociates a set of quick connects from a queue.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateQueueQuickConnectsRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_routing_profile_queues(request: web.Request, instance_id, routing_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_routing_profile_queues

    Disassociates a set of queues from a routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateRoutingProfileQueuesRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_security_key(request: web.Request, instance_id, association_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_security_key

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes the specified security key.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param association_id: The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
    :type association_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def dismiss_user_contact(request: web.Request, user_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """dismiss_user_contact

    Dismisses contacts from an agent’s CCP and returns the agent to an available state, which allows the agent to receive a new routed contact. Contacts can only be dismissed if they are in a &lt;code&gt;MISSED&lt;/code&gt;, &lt;code&gt;ERROR&lt;/code&gt;, &lt;code&gt;ENDED&lt;/code&gt;, or &lt;code&gt;REJECTED&lt;/code&gt; state in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html\&quot;&gt;Agent Event Stream&lt;/a&gt;.

    :param user_id: The identifier of the user account.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DismissUserContactRequest.from_dict(body)
    return web.Response(status=200)


async def get_contact_attributes(request: web.Request, instance_id, initial_contact_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_contact_attributes

    Retrieves the contact attributes for the specified contact.

    :param instance_id: The identifier of the Amazon Connect instance.
    :type instance_id: str
    :param initial_contact_id: The identifier of the initial contact.
    :type initial_contact_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_current_metric_data(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_current_metric_data

    &lt;p&gt;Gets the real-time metric data from the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For a description of each metric, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-definitions.html\&quot;&gt;Real-time Metrics Definitions&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetCurrentMetricDataRequest.from_dict(body)
    return web.Response(status=200)


async def get_current_user_data(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_current_user_data

    Gets the real-time active user data from the specified Amazon Connect instance. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetCurrentUserDataRequest.from_dict(body)
    return web.Response(status=200)


async def get_federation_token(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_federation_token

    &lt;p&gt;Retrieves a token for federation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API doesn&#39;t support root users. If you try to invoke GetFederationToken with root credentials, an error message similar to the following one appears: &lt;/p&gt; &lt;p&gt; &lt;code&gt;Provided identity: Principal: .... User: .... cannot be used for federation with Amazon Connect&lt;/code&gt; &lt;/p&gt; &lt;/note&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_metric_data(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_metric_data

    &lt;p&gt;Gets historical metric data from the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For a description of each historical metric, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/historical-metrics-definitions.html\&quot;&gt;Historical Metrics Definitions&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetMetricDataRequest.from_dict(body)
    return web.Response(status=200)


async def get_metric_data_v2(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_metric_data_v2

    &lt;p&gt;Gets metric data from the specified Amazon Connect instance. &lt;/p&gt; &lt;p&gt; &lt;code&gt;GetMetricDataV2&lt;/code&gt; offers more features than &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt;, the previous version of this API. It has new metrics, offers filtering at a metric level, and offers the ability to filter and group data by channels, queues, routing profiles, agents, and agent hierarchy levels. It can retrieve historical data for the last 35 days, in 24-hour intervals.&lt;/p&gt; &lt;p&gt;For a description of the historical metrics that are supported by &lt;code&gt;GetMetricDataV2&lt;/code&gt; and &lt;code&gt;GetMetricData&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/historical-metrics-definitions.html\&quot;&gt;Historical metrics definitions&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator&#39;s Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetMetricDataV2Request.from_dict(body)
    return web.Response(status=200)


async def get_prompt_file(request: web.Request, instance_id, prompt_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_prompt_file

    Gets the prompt file.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param prompt_id: A unique identifier for the prompt.
    :type prompt_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_task_template(request: web.Request, instance_id, task_template_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, snapshot_version=None) -> web.Response:
    """get_task_template

    Gets details about a specific task template in the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param task_template_id: A unique identifier for the task template.
    :type task_template_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param snapshot_version: The system generated version of a task template that is associated with a task, when the task is created.
    :type snapshot_version: str

    """
    return web.Response(status=200)


async def get_traffic_distribution(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_traffic_distribution

    Retrieves the current traffic distribution for a given traffic distribution group.

    :param id: The identifier of the traffic distribution group.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def list_agent_statuses(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, agent_status_types=None, max_results2=None, next_token2=None) -> web.Response:
    """list_agent_statuses

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Lists agent statuses.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param agent_status_types: Available agent status types.
    :type agent_status_types: list | bytes
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    agent_status_types = [AgentStatusType.from_dict(d) for d in agent_status_types]
    return web.Response(status=200)


async def list_approved_origins(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_approved_origins

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all approved origins associated with the instance.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_bots(request: web.Request, instance_id, lex_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_bots

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;For the specified version of Amazon Lex, returns a paginated list of all the Amazon Lex bots currently associated with the instance. Use this API to returns both Amazon Lex V1 and V2 bots.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param lex_version: The version of Amazon Lex or Amazon Lex V2.
    :type lex_version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_contact_evaluations(request: web.Request, instance_id, contact_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, next_token2=None) -> web.Response:
    """list_contact_evaluations

    Lists contact evaluations in the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_id: The identifier of the contact in this instance of Amazon Connect. 
    :type contact_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: &lt;p&gt;The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This is not expected to be set because the value returned in the previous response is always null.&lt;/p&gt; &lt;/important&gt;
    :type next_token: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_contact_flow_modules(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, state=None, max_results2=None, next_token2=None) -> web.Response:
    """list_contact_flow_modules

    Provides information about the flow modules for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param state: The state of the flow module.
    :type state: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_contact_flows(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, contact_flow_types=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_contact_flows

    &lt;p&gt;Provides information about the flows for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about flows, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/concepts-contact-flows.html\&quot;&gt;Flows&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param contact_flow_types: The type of flow.
    :type contact_flow_types: list | bytes
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    contact_flow_types = [ContactFlowType.from_dict(d) for d in contact_flow_types]
    return web.Response(status=200)


async def list_contact_references(request: web.Request, instance_id, contact_id, reference_types, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, next_token2=None) -> web.Response:
    """list_contact_references

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;For the specified &lt;code&gt;referenceTypes&lt;/code&gt;, returns a list of references associated with the contact. &lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_id: The identifier of the initial contact.
    :type contact_id: str
    :param reference_types: The type of reference.
    :type reference_types: list | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: &lt;p&gt;The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This is not expected to be set, because the value returned in the previous response is always null.&lt;/p&gt; &lt;/important&gt;
    :type next_token: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    reference_types = [ReferenceType.from_dict(d) for d in reference_types]
    return web.Response(status=200)


async def list_default_vocabularies(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_default_vocabularies

    Lists the default vocabularies for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListDefaultVocabulariesRequest.from_dict(body)
    return web.Response(status=200)


async def list_evaluation_form_versions(request: web.Request, instance_id, evaluation_form_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_evaluation_form_versions

    Lists versions of an evaluation form in the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_form_id: The unique identifier for the evaluation form.
    :type evaluation_form_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_evaluation_forms(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_evaluation_forms

    Lists evaluation forms in the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_hours_of_operations(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_hours_of_operations

    &lt;p&gt;Provides information about the hours of operation for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about hours of operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/set-hours-operation.html\&quot;&gt;Set the Hours of Operation for a Queue&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_instance_attributes(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_instance_attributes

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all attribute types for the given instance.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_instance_storage_configs(request: web.Request, instance_id, resource_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_instance_storage_configs

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of storage configs for the identified instance and resource type.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param resource_type: A valid resource type.
    :type resource_type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_instances

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Return a list of instances which are in active state, creation-in-progress state, and failed state. Instances that aren&#39;t successfully created (they are in a failed state) are returned only for 24 hours after the CreateInstance API was invoked.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_integration_associations(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, integration_type=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_integration_associations

    Provides summary information about the Amazon Web Services resource associations for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param integration_type: The integration type.
    :type integration_type: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_lambda_functions(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_lambda_functions

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all Lambda functions that display in the dropdown options in the relevant flow blocks.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_lex_bots(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_lex_bots

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all the Amazon Lex V1 bots currently associated with the instance. To return both Amazon Lex V1 and V2 bots, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListBots.html\&quot;&gt;ListBots&lt;/a&gt; API. &lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. If no value is specified, the default is 10. 
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_phone_numbers(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, phone_number_types=None, phone_number_country_codes=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_phone_numbers

    &lt;p&gt;Provides information about the phone numbers for the specified Amazon Connect instance. &lt;/p&gt; &lt;p&gt;For more information about phone numbers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/contact-center-phone-number.html\&quot;&gt;Set Up Phone Numbers for Your Contact Center&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The phone number &lt;code&gt;Arn&lt;/code&gt; value that is returned from each of the items in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbers.html#connect-ListPhoneNumbers-response-PhoneNumberSummaryList\&quot;&gt;PhoneNumberSummaryList&lt;/a&gt; cannot be used to tag phone number resources. It will fail with a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;. Instead, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html\&quot;&gt;ListPhoneNumbersV2&lt;/a&gt; API. It returns the new phone number ARN that can be used to tag phone number resources.&lt;/p&gt; &lt;/important&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param phone_number_types: The type of phone number.
    :type phone_number_types: list | bytes
    :param phone_number_country_codes: The ISO country code.
    :type phone_number_country_codes: list | bytes
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    phone_number_types = [PhoneNumberType.from_dict(d) for d in phone_number_types]
    phone_number_country_codes = [PhoneNumberCountryCode.from_dict(d) for d in phone_number_country_codes]
    return web.Response(status=200)


async def list_phone_numbers_v2(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_phone_numbers_v2

    &lt;p&gt;Lists phone numbers claimed to your Amazon Connect instance or traffic distribution group. If the provided &lt;code&gt;TargetArn&lt;/code&gt; is a traffic distribution group, you can call this API in both Amazon Web Services Regions associated with traffic distribution group.&lt;/p&gt; &lt;p&gt;For more information about phone numbers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/contact-center-phone-number.html\&quot;&gt;Set Up Phone Numbers for Your Contact Center&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListPhoneNumbersV2Request.from_dict(body)
    return web.Response(status=200)


async def list_prompts(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_prompts

    Provides information about the prompts for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_queue_quick_connects(request: web.Request, instance_id, queue_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_queue_quick_connects

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Lists the quick connects associated with a queue.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_queues(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, queue_types=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_queues

    &lt;p&gt;Provides information about the queues for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;If you do not specify a &lt;code&gt;QueueTypes&lt;/code&gt; parameter, both standard and agent queues are returned. This might cause an unexpected truncation of results if you have more than 1000 agents and you limit the number of results of the API call in code.&lt;/p&gt; &lt;p&gt;For more information about queues, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/concepts-queues-standard-and-agent.html\&quot;&gt;Queues: Standard and Agent&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param queue_types: The type of queue.
    :type queue_types: list | bytes
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    queue_types = [QueueType.from_dict(d) for d in queue_types]
    return web.Response(status=200)


async def list_quick_connects(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, quick_connect_types=None, max_results2=None, next_token2=None) -> web.Response:
    """list_quick_connects

    Provides information about the quick connects for the specified Amazon Connect instance. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param quick_connect_types: The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).
    :type quick_connect_types: list | bytes
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    quick_connect_types = [QuickConnectType.from_dict(d) for d in quick_connect_types]
    return web.Response(status=200)


async def list_routing_profile_queues(request: web.Request, instance_id, routing_profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_routing_profile_queues

    Lists the queues associated with a routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_routing_profiles(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_routing_profiles

    &lt;p&gt;Provides summary information about the routing profiles for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about routing profiles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing.html\&quot;&gt;Routing Profiles&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html\&quot;&gt;Create a Routing Profile&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_rules(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, publish_status=None, event_source_name=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_rules

    List all rules for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param publish_status: The publish status of the rule.
    :type publish_status: str
    :param event_source_name: The name of the event source.
    :type event_source_name: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_security_keys(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_security_keys

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all security keys associated with the instance.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_security_profile_permissions(request: web.Request, security_profile_id, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_security_profile_permissions

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Lists the permissions granted to a security profile.&lt;/p&gt;

    :param security_profile_id: The identifier for the security profle.
    :type security_profile_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_security_profiles(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_security_profiles

    &lt;p&gt;Provides summary information about the security profiles for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about security profiles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html\&quot;&gt;Security Profiles&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists the tags for the specified resource.&lt;/p&gt; &lt;p&gt;For sample policies that use tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_id-based-policy-examples.html\&quot;&gt;Amazon Connect Identity-Based Policy Examples&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param resource_arn: The Amazon Resource Name (ARN) of the resource. All Amazon Connect resources (instances, queues, flows, routing profiles, etc) have an ARN. To locate the ARN for an instance, for example, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;Find your Amazon Connect instance ID/ARN&lt;/a&gt;. 
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


async def list_task_templates(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, status=None, name=None, max_results2=None, next_token2=None) -> web.Response:
    """list_task_templates

    Lists task templates for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: &lt;p&gt;The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It is not expected that you set this because the value returned in the previous response is always null.&lt;/p&gt; &lt;/important&gt;
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return per page.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It is not expected that you set this.&lt;/p&gt; &lt;/important&gt;
    :type max_results: int
    :param status: Marks a template as &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;INACTIVE&lt;/code&gt; for a task to refer to it. Tasks can only be created from &lt;code&gt;ACTIVE&lt;/code&gt; templates. If a template is marked as &lt;code&gt;INACTIVE&lt;/code&gt;, then a task that refers to this template cannot be created.
    :type status: str
    :param name: The name of the task template.
    :type name: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_traffic_distribution_groups(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, instance_id=None, max_results2=None, next_token2=None) -> web.Response:
    """list_traffic_distribution_groups

    Lists traffic distribution groups.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_use_cases(request: web.Request, instance_id, integration_association_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_use_cases

    Lists the use cases for the integration association. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param integration_association_id: The identifier for the integration association.
    :type integration_association_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_user_hierarchy_groups(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_user_hierarchy_groups

    &lt;p&gt;Provides summary information about the hierarchy groups for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about agent hierarchies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/agent-hierarchy.html\&quot;&gt;Set Up Agent Hierarchies&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_users(request: web.Request, instance_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_users

    Provides summary information about the users for the specified Amazon Connect instance.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page. The default MaxResult size is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def monitor_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """monitor_contact

    Initiates silent monitoring of a contact. The Contact Control Panel (CCP) of the user specified by &lt;i&gt;userId&lt;/i&gt; will be set to silent monitoring mode on the contact.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = MonitorContactRequest.from_dict(body)
    return web.Response(status=200)


async def put_user_status(request: web.Request, user_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_user_status

    &lt;p&gt;Changes the current status of a user or agent in Amazon Connect. If the agent is currently handling a contact, this sets the agent&#39;s next status.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html\&quot;&gt;Agent status&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/set-next-status.html\&quot;&gt;Set your next status&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param user_id: The identifier of the user.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutUserStatusRequest.from_dict(body)
    return web.Response(status=200)


async def release_phone_number(request: web.Request, phone_number_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """release_phone_number

    &lt;p&gt;Releases a phone number previously claimed to an Amazon Connect instance or traffic distribution group. You can call this API only in the Amazon Web Services Region where the number was claimed.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To release phone numbers from a traffic distribution group, use the &lt;code&gt;ReleasePhoneNumber&lt;/code&gt; API, not the Amazon Connect console.&lt;/p&gt; &lt;p&gt;After releasing a phone number, the phone number enters into a cooldown period of 30 days. It cannot be searched for or claimed again until the period has ended. If you accidentally release a phone number, contact Amazon Web Services Support.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you plan to claim and release numbers frequently during a 30 day period, contact us for a service quota exception. Otherwise, it is possible you will be blocked from claiming and releasing any more numbers until 30 days past the oldest number released has expired.&lt;/p&gt; &lt;p&gt;By default you can claim and release up to 200% of your maximum number of active phone numbers during any 30 day period. If you claim and release phone numbers using the UI or API during a rolling 30 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming any more numbers until 30 days past the oldest number released has expired. &lt;/p&gt; &lt;p&gt;For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 30 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an Amazon Web Services support ticket.&lt;/p&gt;

    :param phone_number_id: A unique identifier for the phone number.
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
    :param client_token: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;.
    :type client_token: str

    """
    return web.Response(status=200)


async def replicate_instance(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """replicate_instance

    &lt;p&gt;Replicates an Amazon Connect instance in the specified Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;For more information about replicating an Amazon Connect instance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/create-replica-connect-instance.html\&quot;&gt;Create a replica of your existing Amazon Connect instance&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. You can provide the &lt;code&gt;InstanceId&lt;/code&gt;, or the entire ARN.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ReplicateInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def resume_contact_recording(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resume_contact_recording

    &lt;p&gt;When a contact is being recorded, and the recording has been suspended using SuspendContactRecording, this API resumes recording the call or screen.&lt;/p&gt; &lt;p&gt;Voice and screen recordings are supported.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ResumeContactRecordingRequest.from_dict(body)
    return web.Response(status=200)


async def search_available_phone_numbers(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_available_phone_numbers

    Searches for available phone numbers that you can claim to your Amazon Connect instance or traffic distribution group. If the provided &lt;code&gt;TargetArn&lt;/code&gt; is a traffic distribution group, you can call this API in both Amazon Web Services Regions associated with the traffic distribution group.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchAvailablePhoneNumbersRequest.from_dict(body)
    return web.Response(status=200)


async def search_hours_of_operations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_hours_of_operations

    Searches the hours of operation in an Amazon Connect instance, with optional filtering.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchHoursOfOperationsRequest.from_dict(body)
    return web.Response(status=200)


async def search_prompts(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_prompts

    Searches prompts in an Amazon Connect instance, with optional filtering.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchPromptsRequest.from_dict(body)
    return web.Response(status=200)


async def search_queues(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_queues

    Searches queues in an Amazon Connect instance, with optional filtering.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchQueuesRequest.from_dict(body)
    return web.Response(status=200)


async def search_quick_connects(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_quick_connects

    Searches quick connects in an Amazon Connect instance, with optional filtering.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchQuickConnectsRequest.from_dict(body)
    return web.Response(status=200)


async def search_resource_tags(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_resource_tags

    Searches tags used in an Amazon Connect instance using optional search criteria.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchResourceTagsRequest.from_dict(body)
    return web.Response(status=200)


async def search_routing_profiles(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_routing_profiles

    Searches routing profiles in an Amazon Connect instance, with optional filtering.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchRoutingProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def search_security_profiles(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_security_profiles

    Searches security profiles in an Amazon Connect instance, with optional filtering.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchSecurityProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def search_users(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_users

    &lt;p&gt;Searches users in an Amazon Connect instance, with optional filtering.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;AfterContactWorkTimeLimit&lt;/code&gt; is returned in milliseconds. &lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchUsersRequest.from_dict(body)
    return web.Response(status=200)


async def search_vocabularies(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_vocabularies

    Searches for vocabularies within a specific Amazon Connect instance using &lt;code&gt;State&lt;/code&gt;, &lt;code&gt;NameStartsWith&lt;/code&gt;, and &lt;code&gt;LanguageCode&lt;/code&gt;.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SearchVocabulariesRequest.from_dict(body)
    return web.Response(status=200)


async def start_chat_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_chat_contact

    &lt;p&gt;Initiates a flow to start a new chat for the customer. Response of this API provides a token required to obtain credentials from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html\&quot;&gt;CreateParticipantConnection&lt;/a&gt; API in the Amazon Connect Participant Service.&lt;/p&gt; &lt;p&gt;When a new chat contact is successfully created, clients must subscribe to the participant’s connection for the created chat within 5 minutes. This is achieved by invoking &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html\&quot;&gt;CreateParticipantConnection&lt;/a&gt; with WEBSOCKET and CONNECTION_CREDENTIALS. &lt;/p&gt; &lt;p&gt;A 429 error occurs in the following situations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;API rate limit is exceeded. API TPS throttling returns a &lt;code&gt;TooManyRequests&lt;/code&gt; exception.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\&quot;&gt;quota for concurrent active chats&lt;/a&gt; is exceeded. Active chat throttling returns a &lt;code&gt;LimitExceededException&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you use the &lt;code&gt;ChatDurationInMinutes&lt;/code&gt; parameter and receive a 400 error, your account may not support the ability to configure custom chat durations. For more information, contact Amazon Web Services Support. &lt;/p&gt; &lt;p&gt;For more information about chat, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat.html\&quot;&gt;Chat&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartChatContactRequest.from_dict(body)
    return web.Response(status=200)


async def start_contact_evaluation(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_contact_evaluation

    &lt;p&gt;Starts an empty evaluation in the specified Amazon Connect instance, using the given evaluation form for the particular contact. The evaluation form version used for the contact evaluation corresponds to the currently activated version. If no version is activated for the evaluation form, the contact evaluation cannot be started. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Evaluations created through the public API do not contain answer values suggested from automation.&lt;/p&gt; &lt;/note&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartContactEvaluationRequest.from_dict(body)
    return web.Response(status=200)


async def start_contact_recording(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_contact_recording

    &lt;p&gt;Starts recording the contact: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the API is called &lt;i&gt;before&lt;/i&gt; the agent joins the call, recording starts when the agent joins the call.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the API is called &lt;i&gt;after&lt;/i&gt; the agent joins the call, recording starts at the time of the API call.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;StartContactRecording is a one-time action. For example, if you use StopContactRecording to stop recording an ongoing call, you can&#39;t use StartContactRecording to restart it. For scenarios where the recording has started and you want to suspend and resume it, such as when collecting sensitive information (for example, a credit card number), use SuspendContactRecording and ResumeContactRecording.&lt;/p&gt; &lt;p&gt;You can use this API to override the recording behavior configured in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-behavior.html\&quot;&gt;Set recording behavior&lt;/a&gt; block.&lt;/p&gt; &lt;p&gt;Only voice recordings are supported at this time.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartContactRecordingRequest.from_dict(body)
    return web.Response(status=200)


async def start_contact_streaming(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_contact_streaming

    &lt;p&gt; Initiates real-time message streaming for a new chat contact.&lt;/p&gt; &lt;p&gt; For more information about message streaming, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html\&quot;&gt;Enable real-time chat message streaming&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartContactStreamingRequest.from_dict(body)
    return web.Response(status=200)


async def start_outbound_voice_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_outbound_voice_contact

    &lt;p&gt;Places an outbound call to a contact, and then initiates the flow. It performs the actions in the flow that&#39;s specified (in &lt;code&gt;ContactFlowId&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;Agents do not initiate the outbound API, which means that they do not dial the contact. If the flow places an outbound call to a contact, and then puts the contact in queue, the call is then routed to the agent, like any other inbound case.&lt;/p&gt; &lt;p&gt;There is a 60-second dialing timeout for this operation. If the call is not connected after 60 seconds, it fails.&lt;/p&gt; &lt;note&gt; &lt;p&gt;UK numbers with a 447 prefix are not allowed by default. Before you can dial these UK mobile numbers, you must submit a service quota increase request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\&quot;&gt;Amazon Connect Service Quotas&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Campaign calls are not allowed by default. Before you can make a call with &lt;code&gt;TrafficType&lt;/code&gt; &#x3D; &lt;code&gt;CAMPAIGN&lt;/code&gt;, you must submit a service quota increase request to the quota &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#outbound-communications-quotas\&quot;&gt;Amazon Connect campaigns&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartOutboundVoiceContactRequest.from_dict(body)
    return web.Response(status=200)


async def start_task_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_task_contact

    Initiates a flow to start a new task.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartTaskContactRequest.from_dict(body)
    return web.Response(status=200)


async def stop_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_contact

    &lt;p&gt;Ends the specified contact. This call does not work for the following initiation methods:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;DISCONNECT&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;TRANSFER&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;QUEUE_TRANSFER&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopContactRequest.from_dict(body)
    return web.Response(status=200)


async def stop_contact_recording(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_contact_recording

    &lt;p&gt;Stops recording a call when a contact is being recorded. StopContactRecording is a one-time action. If you use StopContactRecording to stop recording an ongoing call, you can&#39;t use StartContactRecording to restart it. For scenarios where the recording has started and you want to suspend it for sensitive information (for example, to collect a credit card number), and then restart it, use SuspendContactRecording and ResumeContactRecording.&lt;/p&gt; &lt;p&gt;Only voice recordings are supported at this time.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ResumeContactRecordingRequest.from_dict(body)
    return web.Response(status=200)


async def stop_contact_streaming(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_contact_streaming

     Ends message streaming on a specified contact. To restart message streaming on that contact, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html\&quot;&gt;StartContactStreaming&lt;/a&gt; API. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopContactStreamingRequest.from_dict(body)
    return web.Response(status=200)


async def submit_contact_evaluation(request: web.Request, instance_id, evaluation_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """submit_contact_evaluation

    &lt;p&gt;Submits a contact evaluation in the specified Amazon Connect instance. Answers included in the request are merged with existing answers for the given evaluation. If no answers or notes are passed, the evaluation is submitted with the existing answers and notes. You can delete an answer or note by passing an empty object (&lt;code&gt;{}&lt;/code&gt;) to the question identifier. &lt;/p&gt; &lt;p&gt;If a contact evaluation is already in submitted state, this operation will trigger a resubmission.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_id: A unique identifier for the contact evaluation.
    :type evaluation_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactEvaluationRequest.from_dict(body)
    return web.Response(status=200)


async def suspend_contact_recording(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """suspend_contact_recording

    &lt;p&gt;When a contact is being recorded, this API suspends recording the call or screen. For example, you might suspend the call or screen recording while collecting sensitive information, such as a credit card number. Then use ResumeContactRecording to restart recording.&lt;/p&gt; &lt;p&gt;The period of time that the recording is suspended is filled with silence in the final recording.&lt;/p&gt; &lt;p&gt;Voice and screen recordings are supported.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ResumeContactRecordingRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds the specified tags to the specified resource.&lt;/p&gt; &lt;p&gt;Some of the supported resource types are agents, routing profiles, queues, quick connects, contact flows, agent statuses, hours of operation, phone numbers, security profiles, and task templates. For a complete list, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/tagging.html\&quot;&gt;Tagging resources in Amazon Connect&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For sample policies that use tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_id-based-policy-examples.html\&quot;&gt;Amazon Connect Identity-Based Policy Examples&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

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


async def transfer_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """transfer_contact

    &lt;p&gt;Transfers contacts from one agent or queue to another agent or queue at any point after a contact is created. You can transfer a contact to another queue by providing the flow which orchestrates the contact to the destination queue. This gives you more control over contact handling and helps you adhere to the service level agreement (SLA) guaranteed to your customers.&lt;/p&gt; &lt;p&gt;Note the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Transfer is supported for only &lt;code&gt;TASK&lt;/code&gt; contacts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Do not use both &lt;code&gt;QueueId&lt;/code&gt; and &lt;code&gt;UserId&lt;/code&gt; in the same call.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following flow types are supported: Inbound flow, Transfer to agent flow, and Transfer to queue flow.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;TransferContact&lt;/code&gt; API can be called only on active contacts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A contact cannot be transferred more than 11 times.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TransferContactRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the specified tags from the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
    :param tag_keys: The tag keys.
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


async def update_agent_status(request: web.Request, instance_id, agent_status_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_agent_status

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates agent status.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param agent_status_id: The identifier of the agent status.
    :type agent_status_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAgentStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact(request: web.Request, instance_id, contact_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Adds or updates user-defined contact information associated with the specified contact. At least one field to be updated must be present in the request.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can add or update user-defined contact information for both ongoing and completed contacts.&lt;/p&gt; &lt;/important&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_id: The identifier of the contact. This is the identifier of the contact associated with the first interaction with your contact center.
    :type contact_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_attributes(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_attributes

    &lt;p&gt;Creates or updates user-defined contact attributes associated with the specified contact.&lt;/p&gt; &lt;p&gt;You can create or update user-defined attributes for both ongoing and completed contacts. For example, while the call is active, you can update the customer&#39;s name or the reason the customer called. You can add notes about steps that the agent took during the call that display to the next agent that takes the call. You can also update attributes for a contact using data from your CRM application and save the data with the contact in Amazon Connect. You could also flag calls for additional analysis, such as legal review or to identify abusive callers.&lt;/p&gt; &lt;p&gt;Contact attributes are available in Amazon Connect for 24 months, and are then deleted. For information about contact record retention and the maximum size of the contact record attributes section, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits\&quot;&gt;Feature specifications&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_evaluation(request: web.Request, instance_id, evaluation_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_evaluation

    Updates details about a contact evaluation in the specified Amazon Connect instance. A contact evaluation must be in draft state. Answers included in the request are merged with existing answers for the given evaluation. An answer or note can be deleted by passing an empty object (&lt;code&gt;{}&lt;/code&gt;) to the question identifier. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_id: A unique identifier for the contact evaluation.
    :type evaluation_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactEvaluationRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_flow_content(request: web.Request, instance_id, contact_flow_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_flow_content

    &lt;p&gt;Updates the specified flow.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance.
    :type instance_id: str
    :param contact_flow_id: The identifier of the flow.
    :type contact_flow_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactFlowContentRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_flow_metadata(request: web.Request, instance_id, contact_flow_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_flow_metadata

    Updates metadata about specified flow.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_flow_id: The identifier of the flow.
    :type contact_flow_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactFlowMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_flow_module_content(request: web.Request, instance_id, contact_flow_module_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_flow_module_content

    Updates specified flow module for the specified Amazon Connect instance. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_flow_module_id: The identifier of the flow module.
    :type contact_flow_module_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactFlowModuleContentRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_flow_module_metadata(request: web.Request, instance_id, contact_flow_module_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_flow_module_metadata

    Updates metadata about specified flow module.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_flow_module_id: The identifier of the flow module.
    :type contact_flow_module_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactFlowModuleMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_flow_name(request: web.Request, instance_id, contact_flow_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_flow_name

    &lt;p&gt;The name of the flow.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance.
    :type instance_id: str
    :param contact_flow_id: The identifier of the flow.
    :type contact_flow_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactFlowNameRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact_schedule(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_schedule

    Updates the scheduled time of a task contact that is already scheduled.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactScheduleRequest.from_dict(body)
    return web.Response(status=200)


async def update_evaluation_form(request: web.Request, instance_id, evaluation_form_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_evaluation_form

    &lt;p&gt;Updates details about a specific evaluation form version in the specified Amazon Connect instance. Question and section identifiers cannot be duplicated within the same evaluation form.&lt;/p&gt; &lt;p&gt;This operation does not support partial updates. Instead it does a full update of evaluation form content.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param evaluation_form_id: The unique identifier for the evaluation form.
    :type evaluation_form_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEvaluationFormRequest.from_dict(body)
    return web.Response(status=200)


async def update_hours_of_operation(request: web.Request, instance_id, hours_of_operation_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_hours_of_operation

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the hours of operation.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param hours_of_operation_id: The identifier of the hours of operation.
    :type hours_of_operation_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateHoursOfOperationRequest.from_dict(body)
    return web.Response(status=200)


async def update_instance_attribute(request: web.Request, instance_id, attribute_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_instance_attribute

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the value for the specified attribute type.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param attribute_type: &lt;p&gt;The type of attribute.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only allowlisted customers can consume USE_CUSTOM_TTS_VOICES. To access this feature, contact Amazon Web Services Support for allowlisting.&lt;/p&gt; &lt;/note&gt;
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
    body = UpdateInstanceAttributeRequest.from_dict(body)
    return web.Response(status=200)


async def update_instance_storage_config(request: web.Request, instance_id, association_id, resource_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_instance_storage_config

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates an existing configuration for a resource type. This API is idempotent.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param association_id: The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
    :type association_id: str
    :param resource_type: A valid resource type.
    :type resource_type: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateInstanceStorageConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_participant_role_config(request: web.Request, instance_id, contact_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_participant_role_config

    &lt;p&gt;Updates timeouts for when human chat participants are to be considered idle, and when agents are automatically disconnected from a chat due to idleness. You can set four timers:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Customer idle timeout&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Customer auto-disconnect timeout&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Agent idle timeout&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Agent auto-disconnect timeout&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about how chat timeouts work, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/setup-chat-timeouts.html\&quot;&gt;Set up chat timeouts for human participants&lt;/a&gt;. &lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param contact_id: The identifier of the contact in this instance of Amazon Connect. 
    :type contact_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateParticipantRoleConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_phone_number(request: web.Request, phone_number_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_phone_number

    &lt;p&gt;Updates your claimed phone number from its current Amazon Connect instance or traffic distribution group to another Amazon Connect instance or traffic distribution group in the same Amazon Web Services Region.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After using this API, you must verify that the phone number is attached to the correct flow in the target instance or traffic distribution group. You need to do this because the API switches only the phone number to a new instance or traffic distribution group. It doesn&#39;t migrate the flow configuration of the phone number, too.&lt;/p&gt; &lt;p&gt;You can call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html\&quot;&gt;DescribePhoneNumber&lt;/a&gt; API to verify the status of a previous &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html\&quot;&gt;UpdatePhoneNumber&lt;/a&gt; operation.&lt;/p&gt; &lt;/important&gt;

    :param phone_number_id: A unique identifier for the phone number.
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


async def update_prompt(request: web.Request, instance_id, prompt_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_prompt

    Updates a prompt.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param prompt_id: A unique identifier for the prompt.
    :type prompt_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePromptRequest.from_dict(body)
    return web.Response(status=200)


async def update_queue_hours_of_operation(request: web.Request, instance_id, queue_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_queue_hours_of_operation

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the hours of operation for the specified queue.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQueueHoursOfOperationRequest.from_dict(body)
    return web.Response(status=200)


async def update_queue_max_contacts(request: web.Request, instance_id, queue_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_queue_max_contacts

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the maximum number of contacts allowed in a queue before it is considered full.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQueueMaxContactsRequest.from_dict(body)
    return web.Response(status=200)


async def update_queue_name(request: web.Request, instance_id, queue_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_queue_name

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the name and description of a queue. At least &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;Description&lt;/code&gt; must be provided.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQueueNameRequest.from_dict(body)
    return web.Response(status=200)


async def update_queue_outbound_caller_config(request: web.Request, instance_id, queue_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_queue_outbound_caller_config

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the outbound caller ID name, number, and outbound whisper flow for a specified queue.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number being used in the input is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;OutboundCallerIdNumberId&lt;/code&gt; value of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_OutboundCallerConfig\&quot;&gt;OutboundCallerConfig&lt;/a&gt; request body parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Only use the phone number ARN format that doesn&#39;t contain &lt;code&gt;instance&lt;/code&gt; in the path, for example, &lt;code&gt;arn:aws:connect:us-east-1:1234567890:phone-number/uuid&lt;/code&gt;. This is the same ARN format that is returned when you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html\&quot;&gt;ListPhoneNumbersV2&lt;/a&gt; API.&lt;/p&gt; &lt;/important&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQueueOutboundCallerConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_queue_status(request: web.Request, instance_id, queue_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_queue_status

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the status of the queue.&lt;/p&gt;

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param queue_id: The identifier for the queue.
    :type queue_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQueueStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_quick_connect_config(request: web.Request, instance_id, quick_connect_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_quick_connect_config

    Updates the configuration settings for the specified quick connect.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param quick_connect_id: The identifier for the quick connect.
    :type quick_connect_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQuickConnectConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_quick_connect_name(request: web.Request, instance_id, quick_connect_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_quick_connect_name

    Updates the name and description of a quick connect. The request accepts the following data in JSON format. At least &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;Description&lt;/code&gt; must be provided.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param quick_connect_id: The identifier for the quick connect.
    :type quick_connect_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateQuickConnectNameRequest.from_dict(body)
    return web.Response(status=200)


async def update_routing_profile_agent_availability_timer(request: web.Request, instance_id, routing_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_routing_profile_agent_availability_timer

    Whether agents with this routing profile will have their routing order calculated based on &lt;i&gt;time since their last inbound contact&lt;/i&gt; or &lt;i&gt;longest idle time&lt;/i&gt;. 

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRoutingProfileAgentAvailabilityTimerRequest.from_dict(body)
    return web.Response(status=200)


async def update_routing_profile_concurrency(request: web.Request, instance_id, routing_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_routing_profile_concurrency

    Updates the channels that agents can handle in the Contact Control Panel (CCP) for a routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRoutingProfileConcurrencyRequest.from_dict(body)
    return web.Response(status=200)


async def update_routing_profile_default_outbound_queue(request: web.Request, instance_id, routing_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_routing_profile_default_outbound_queue

    Updates the default outbound queue of a routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRoutingProfileDefaultOutboundQueueRequest.from_dict(body)
    return web.Response(status=200)


async def update_routing_profile_name(request: web.Request, instance_id, routing_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_routing_profile_name

    Updates the name and description of a routing profile. The request accepts the following data in JSON format. At least &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;Description&lt;/code&gt; must be provided.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRoutingProfileNameRequest.from_dict(body)
    return web.Response(status=200)


async def update_routing_profile_queues(request: web.Request, instance_id, routing_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_routing_profile_queues

    Updates the properties associated with a set of queues for a routing profile.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param routing_profile_id: The identifier of the routing profile.
    :type routing_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRoutingProfileQueuesRequest.from_dict(body)
    return web.Response(status=200)


async def update_rule(request: web.Request, rule_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rule

    &lt;p&gt;Updates a rule for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/connect-rules-language.html\&quot;&gt;Rules Function language&lt;/a&gt; to code conditions for the rule. &lt;/p&gt;

    :param rule_id: A unique identifier for the rule.
    :type rule_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_security_profile(request: web.Request, security_profile_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_security_profile

    &lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates a security profile.&lt;/p&gt;

    :param security_profile_id: The identifier for the security profle.
    :type security_profile_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateSecurityProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_task_template(request: web.Request, task_template_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_task_template

    Updates details about a specific task template in the specified Amazon Connect instance. This operation does not support partial updates. Instead it does a full update of template content.

    :param task_template_id: A unique identifier for the task template.
    :type task_template_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTaskTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_traffic_distribution(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_traffic_distribution

    &lt;p&gt;Updates the traffic distribution for a given traffic distribution group. &lt;/p&gt; &lt;p&gt;For more information about updating a traffic distribution group, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/update-telephony-traffic-distribution.html\&quot;&gt;Update telephony traffic distribution across Amazon Web Services Regions &lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt;

    :param id: The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTrafficDistributionRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_hierarchy(request: web.Request, user_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_hierarchy

    Assigns the specified hierarchy group to the specified user.

    :param user_id: The identifier of the user account.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserHierarchyRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_hierarchy_group_name(request: web.Request, hierarchy_group_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_hierarchy_group_name

    Updates the name of the user hierarchy group. 

    :param hierarchy_group_id: The identifier of the hierarchy group.
    :type hierarchy_group_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserHierarchyGroupNameRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_hierarchy_structure(request: web.Request, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_hierarchy_structure

    Updates the user hierarchy structure: add, remove, and rename user hierarchy levels.

    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserHierarchyStructureRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_identity_info(request: web.Request, user_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_identity_info

    &lt;p&gt;Updates the identity information for the specified user.&lt;/p&gt; &lt;important&gt; &lt;p&gt;We strongly recommend limiting who has the ability to invoke &lt;code&gt;UpdateUserIdentityInfo&lt;/code&gt;. Someone with that ability can change the login credentials of other users by changing their email address. This poses a security risk to your organization. They can change the email address of a user to the attacker&#39;s email address, and then reset the password through email. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-best-practices.html\&quot;&gt;Best Practices for Security Profiles&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param user_id: The identifier of the user account.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserIdentityInfoRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_phone_config(request: web.Request, user_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_phone_config

    Updates the phone configuration settings for the specified user.

    :param user_id: The identifier of the user account.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserPhoneConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_routing_profile(request: web.Request, user_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_routing_profile

    Assigns the specified routing profile to the specified user.

    :param user_id: The identifier of the user account.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserRoutingProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_security_profiles(request: web.Request, user_id, instance_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_security_profiles

    Assigns the specified security profiles to the specified user.

    :param user_id: The identifier of the user account.
    :type user_id: str
    :param instance_id: The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.
    :type instance_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateUserSecurityProfilesRequest.from_dict(body)
    return web.Response(status=200)
