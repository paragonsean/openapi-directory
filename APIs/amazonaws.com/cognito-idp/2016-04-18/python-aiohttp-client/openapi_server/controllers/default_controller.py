from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_custom_attributes_request import AddCustomAttributesRequest
from openapi_server.models.admin_add_user_to_group_request import AdminAddUserToGroupRequest
from openapi_server.models.admin_confirm_sign_up_request import AdminConfirmSignUpRequest
from openapi_server.models.admin_create_user_request import AdminCreateUserRequest
from openapi_server.models.admin_create_user_response import AdminCreateUserResponse
from openapi_server.models.admin_delete_user_attributes_request import AdminDeleteUserAttributesRequest
from openapi_server.models.admin_delete_user_request import AdminDeleteUserRequest
from openapi_server.models.admin_disable_provider_for_user_request import AdminDisableProviderForUserRequest
from openapi_server.models.admin_disable_user_request import AdminDisableUserRequest
from openapi_server.models.admin_enable_user_request import AdminEnableUserRequest
from openapi_server.models.admin_forget_device_request import AdminForgetDeviceRequest
from openapi_server.models.admin_get_device_request import AdminGetDeviceRequest
from openapi_server.models.admin_get_device_response import AdminGetDeviceResponse
from openapi_server.models.admin_get_user_request import AdminGetUserRequest
from openapi_server.models.admin_get_user_response import AdminGetUserResponse
from openapi_server.models.admin_initiate_auth_request import AdminInitiateAuthRequest
from openapi_server.models.admin_initiate_auth_response import AdminInitiateAuthResponse
from openapi_server.models.admin_link_provider_for_user_request import AdminLinkProviderForUserRequest
from openapi_server.models.admin_list_devices_request import AdminListDevicesRequest
from openapi_server.models.admin_list_devices_response import AdminListDevicesResponse
from openapi_server.models.admin_list_groups_for_user_request import AdminListGroupsForUserRequest
from openapi_server.models.admin_list_groups_for_user_response import AdminListGroupsForUserResponse
from openapi_server.models.admin_list_user_auth_events_request import AdminListUserAuthEventsRequest
from openapi_server.models.admin_list_user_auth_events_response import AdminListUserAuthEventsResponse
from openapi_server.models.admin_remove_user_from_group_request import AdminRemoveUserFromGroupRequest
from openapi_server.models.admin_reset_user_password_request import AdminResetUserPasswordRequest
from openapi_server.models.admin_respond_to_auth_challenge_request import AdminRespondToAuthChallengeRequest
from openapi_server.models.admin_respond_to_auth_challenge_response import AdminRespondToAuthChallengeResponse
from openapi_server.models.admin_set_user_mfa_preference_request import AdminSetUserMFAPreferenceRequest
from openapi_server.models.admin_set_user_password_request import AdminSetUserPasswordRequest
from openapi_server.models.admin_set_user_settings_request import AdminSetUserSettingsRequest
from openapi_server.models.admin_update_auth_event_feedback_request import AdminUpdateAuthEventFeedbackRequest
from openapi_server.models.admin_update_device_status_request import AdminUpdateDeviceStatusRequest
from openapi_server.models.admin_update_user_attributes_request import AdminUpdateUserAttributesRequest
from openapi_server.models.admin_user_global_sign_out_request import AdminUserGlobalSignOutRequest
from openapi_server.models.associate_software_token_request import AssociateSoftwareTokenRequest
from openapi_server.models.associate_software_token_response import AssociateSoftwareTokenResponse
from openapi_server.models.change_password_request import ChangePasswordRequest
from openapi_server.models.confirm_device_request import ConfirmDeviceRequest
from openapi_server.models.confirm_device_response import ConfirmDeviceResponse
from openapi_server.models.confirm_forgot_password_request import ConfirmForgotPasswordRequest
from openapi_server.models.confirm_sign_up_request import ConfirmSignUpRequest
from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.create_group_response import CreateGroupResponse
from openapi_server.models.create_identity_provider_request import CreateIdentityProviderRequest
from openapi_server.models.create_identity_provider_response import CreateIdentityProviderResponse
from openapi_server.models.create_resource_server_request import CreateResourceServerRequest
from openapi_server.models.create_resource_server_response import CreateResourceServerResponse
from openapi_server.models.create_user_import_job_request import CreateUserImportJobRequest
from openapi_server.models.create_user_import_job_response import CreateUserImportJobResponse
from openapi_server.models.create_user_pool_client_request import CreateUserPoolClientRequest
from openapi_server.models.create_user_pool_client_response import CreateUserPoolClientResponse
from openapi_server.models.create_user_pool_domain_request import CreateUserPoolDomainRequest
from openapi_server.models.create_user_pool_domain_response import CreateUserPoolDomainResponse
from openapi_server.models.create_user_pool_request import CreateUserPoolRequest
from openapi_server.models.create_user_pool_response import CreateUserPoolResponse
from openapi_server.models.delete_group_request import DeleteGroupRequest
from openapi_server.models.delete_identity_provider_request import DeleteIdentityProviderRequest
from openapi_server.models.delete_resource_server_request import DeleteResourceServerRequest
from openapi_server.models.delete_user_attributes_request import DeleteUserAttributesRequest
from openapi_server.models.delete_user_pool_client_request import DeleteUserPoolClientRequest
from openapi_server.models.delete_user_pool_domain_request import DeleteUserPoolDomainRequest
from openapi_server.models.delete_user_pool_request import DeleteUserPoolRequest
from openapi_server.models.delete_user_request import DeleteUserRequest
from openapi_server.models.describe_identity_provider_request import DescribeIdentityProviderRequest
from openapi_server.models.describe_identity_provider_response import DescribeIdentityProviderResponse
from openapi_server.models.describe_resource_server_request import DescribeResourceServerRequest
from openapi_server.models.describe_resource_server_response import DescribeResourceServerResponse
from openapi_server.models.describe_risk_configuration_request import DescribeRiskConfigurationRequest
from openapi_server.models.describe_risk_configuration_response import DescribeRiskConfigurationResponse
from openapi_server.models.describe_user_import_job_request import DescribeUserImportJobRequest
from openapi_server.models.describe_user_import_job_response import DescribeUserImportJobResponse
from openapi_server.models.describe_user_pool_client_request import DescribeUserPoolClientRequest
from openapi_server.models.describe_user_pool_client_response import DescribeUserPoolClientResponse
from openapi_server.models.describe_user_pool_domain_request import DescribeUserPoolDomainRequest
from openapi_server.models.describe_user_pool_domain_response import DescribeUserPoolDomainResponse
from openapi_server.models.describe_user_pool_request import DescribeUserPoolRequest
from openapi_server.models.describe_user_pool_response import DescribeUserPoolResponse
from openapi_server.models.forget_device_request import ForgetDeviceRequest
from openapi_server.models.forgot_password_request import ForgotPasswordRequest
from openapi_server.models.forgot_password_response import ForgotPasswordResponse
from openapi_server.models.get_csv_header_request import GetCSVHeaderRequest
from openapi_server.models.get_csv_header_response import GetCSVHeaderResponse
from openapi_server.models.get_device_request import GetDeviceRequest
from openapi_server.models.get_device_response import GetDeviceResponse
from openapi_server.models.get_group_request import GetGroupRequest
from openapi_server.models.get_group_response import GetGroupResponse
from openapi_server.models.get_identity_provider_by_identifier_request import GetIdentityProviderByIdentifierRequest
from openapi_server.models.get_identity_provider_by_identifier_response import GetIdentityProviderByIdentifierResponse
from openapi_server.models.get_log_delivery_configuration_request import GetLogDeliveryConfigurationRequest
from openapi_server.models.get_log_delivery_configuration_response import GetLogDeliveryConfigurationResponse
from openapi_server.models.get_signing_certificate_request import GetSigningCertificateRequest
from openapi_server.models.get_signing_certificate_response import GetSigningCertificateResponse
from openapi_server.models.get_ui_customization_request import GetUICustomizationRequest
from openapi_server.models.get_ui_customization_response import GetUICustomizationResponse
from openapi_server.models.get_user_attribute_verification_code_request import GetUserAttributeVerificationCodeRequest
from openapi_server.models.get_user_attribute_verification_code_response import GetUserAttributeVerificationCodeResponse
from openapi_server.models.get_user_pool_mfa_config_request import GetUserPoolMfaConfigRequest
from openapi_server.models.get_user_pool_mfa_config_response import GetUserPoolMfaConfigResponse
from openapi_server.models.get_user_request import GetUserRequest
from openapi_server.models.get_user_response import GetUserResponse
from openapi_server.models.global_sign_out_request import GlobalSignOutRequest
from openapi_server.models.initiate_auth_request import InitiateAuthRequest
from openapi_server.models.initiate_auth_response import InitiateAuthResponse
from openapi_server.models.list_devices_request import ListDevicesRequest
from openapi_server.models.list_devices_response import ListDevicesResponse
from openapi_server.models.list_groups_request import ListGroupsRequest
from openapi_server.models.list_groups_response import ListGroupsResponse
from openapi_server.models.list_identity_providers_request import ListIdentityProvidersRequest
from openapi_server.models.list_identity_providers_response import ListIdentityProvidersResponse
from openapi_server.models.list_resource_servers_request import ListResourceServersRequest
from openapi_server.models.list_resource_servers_response import ListResourceServersResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_user_import_jobs_request import ListUserImportJobsRequest
from openapi_server.models.list_user_import_jobs_response import ListUserImportJobsResponse
from openapi_server.models.list_user_pool_clients_request import ListUserPoolClientsRequest
from openapi_server.models.list_user_pool_clients_response import ListUserPoolClientsResponse
from openapi_server.models.list_user_pools_request import ListUserPoolsRequest
from openapi_server.models.list_user_pools_response import ListUserPoolsResponse
from openapi_server.models.list_users_in_group_request import ListUsersInGroupRequest
from openapi_server.models.list_users_in_group_response import ListUsersInGroupResponse
from openapi_server.models.list_users_request import ListUsersRequest
from openapi_server.models.list_users_response import ListUsersResponse
from openapi_server.models.resend_confirmation_code_request import ResendConfirmationCodeRequest
from openapi_server.models.resend_confirmation_code_response import ResendConfirmationCodeResponse
from openapi_server.models.respond_to_auth_challenge_request import RespondToAuthChallengeRequest
from openapi_server.models.respond_to_auth_challenge_response import RespondToAuthChallengeResponse
from openapi_server.models.revoke_token_request import RevokeTokenRequest
from openapi_server.models.set_log_delivery_configuration_request import SetLogDeliveryConfigurationRequest
from openapi_server.models.set_log_delivery_configuration_response import SetLogDeliveryConfigurationResponse
from openapi_server.models.set_risk_configuration_request import SetRiskConfigurationRequest
from openapi_server.models.set_risk_configuration_response import SetRiskConfigurationResponse
from openapi_server.models.set_ui_customization_request import SetUICustomizationRequest
from openapi_server.models.set_ui_customization_response import SetUICustomizationResponse
from openapi_server.models.set_user_mfa_preference_request import SetUserMFAPreferenceRequest
from openapi_server.models.set_user_pool_mfa_config_request import SetUserPoolMfaConfigRequest
from openapi_server.models.set_user_pool_mfa_config_response import SetUserPoolMfaConfigResponse
from openapi_server.models.set_user_settings_request import SetUserSettingsRequest
from openapi_server.models.sign_up_request import SignUpRequest
from openapi_server.models.sign_up_response import SignUpResponse
from openapi_server.models.start_user_import_job_request import StartUserImportJobRequest
from openapi_server.models.start_user_import_job_response import StartUserImportJobResponse
from openapi_server.models.stop_user_import_job_request import StopUserImportJobRequest
from openapi_server.models.stop_user_import_job_response import StopUserImportJobResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_auth_event_feedback_request import UpdateAuthEventFeedbackRequest
from openapi_server.models.update_device_status_request import UpdateDeviceStatusRequest
from openapi_server.models.update_group_request import UpdateGroupRequest
from openapi_server.models.update_group_response import UpdateGroupResponse
from openapi_server.models.update_identity_provider_request import UpdateIdentityProviderRequest
from openapi_server.models.update_identity_provider_response import UpdateIdentityProviderResponse
from openapi_server.models.update_resource_server_request import UpdateResourceServerRequest
from openapi_server.models.update_resource_server_response import UpdateResourceServerResponse
from openapi_server.models.update_user_attributes_request import UpdateUserAttributesRequest
from openapi_server.models.update_user_attributes_response import UpdateUserAttributesResponse
from openapi_server.models.update_user_pool_client_request import UpdateUserPoolClientRequest
from openapi_server.models.update_user_pool_client_response import UpdateUserPoolClientResponse
from openapi_server.models.update_user_pool_domain_request import UpdateUserPoolDomainRequest
from openapi_server.models.update_user_pool_domain_response import UpdateUserPoolDomainResponse
from openapi_server.models.update_user_pool_request import UpdateUserPoolRequest
from openapi_server.models.verify_software_token_request import VerifySoftwareTokenRequest
from openapi_server.models.verify_software_token_response import VerifySoftwareTokenResponse
from openapi_server.models.verify_user_attribute_request import VerifyUserAttributeRequest
from openapi_server import util


async def add_custom_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_custom_attributes

    &lt;p&gt;Adds additional user attributes to the user pool schema.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AddCustomAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def admin_add_user_to_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_add_user_to_group

    &lt;p&gt;Adds the specified user to the specified group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminAddUserToGroupRequest.from_dict(body)
    return web.Response(status=200)


async def admin_confirm_sign_up(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_confirm_sign_up

    &lt;p&gt;Confirms user registration as an admin without using a confirmation code. Works on any user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminConfirmSignUpRequest.from_dict(body)
    return web.Response(status=200)


async def admin_create_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_create_user

    &lt;p&gt;Creates a new user in the specified user pool.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;MessageAction&lt;/code&gt; isn&#39;t set, the default is to send a welcome message via email or phone (SMS).&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This message is based on a template that you configured in your call to create or update a user pool. This template includes your custom sign-up instructions and placeholders for user name and temporary password.&lt;/p&gt; &lt;p&gt;Alternatively, you can call &lt;code&gt;AdminCreateUser&lt;/code&gt; with &lt;code&gt;SUPPRESS&lt;/code&gt; for the &lt;code&gt;MessageAction&lt;/code&gt; parameter, and Amazon Cognito won&#39;t send any email. &lt;/p&gt; &lt;p&gt;In either case, the user will be in the &lt;code&gt;FORCE_CHANGE_PASSWORD&lt;/code&gt; state until they sign in and change their password.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminCreateUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_delete_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_delete_user

    &lt;p&gt;Deletes a user as an administrator. Works on any user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminDeleteUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_delete_user_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_delete_user_attributes

    &lt;p&gt;Deletes the user attributes in a user pool as an administrator. Works on any user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminDeleteUserAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def admin_disable_provider_for_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_disable_provider_for_user

    &lt;p&gt;Prevents the user from signing in with the specified external (SAML or social) identity provider (IdP). If the user that you want to deactivate is a Amazon Cognito user pools native username + password user, they can&#39;t use their password to sign in. If the user to deactivate is a linked external IdP user, any link between that user and an existing user is removed. When the external user signs in again, and the user is no longer attached to the previously linked &lt;code&gt;DestinationUser&lt;/code&gt;, the user must create a new user account. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.html\&quot;&gt;AdminLinkProviderForUser&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ProviderName&lt;/code&gt; must match the value specified when creating an IdP for the pool. &lt;/p&gt; &lt;p&gt;To deactivate a native username + password user, the &lt;code&gt;ProviderName&lt;/code&gt; value must be &lt;code&gt;Cognito&lt;/code&gt; and the &lt;code&gt;ProviderAttributeName&lt;/code&gt; must be &lt;code&gt;Cognito_Subject&lt;/code&gt;. The &lt;code&gt;ProviderAttributeValue&lt;/code&gt; must be the name that is used in the user pool for the user.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;ProviderAttributeName&lt;/code&gt; must always be &lt;code&gt;Cognito_Subject&lt;/code&gt; for social IdPs. The &lt;code&gt;ProviderAttributeValue&lt;/code&gt; must always be the exact subject that was used when the user was originally linked as a source user.&lt;/p&gt; &lt;p&gt;For de-linking a SAML identity, there are two scenarios. If the linked identity has not yet been used to sign in, the &lt;code&gt;ProviderAttributeName&lt;/code&gt; and &lt;code&gt;ProviderAttributeValue&lt;/code&gt; must be the same values that were used for the &lt;code&gt;SourceUser&lt;/code&gt; when the identities were originally linked using &lt;code&gt; AdminLinkProviderForUser&lt;/code&gt; call. (If the linking was done with &lt;code&gt;ProviderAttributeName&lt;/code&gt; set to &lt;code&gt;Cognito_Subject&lt;/code&gt;, the same applies here). However, if the user has already signed in, the &lt;code&gt;ProviderAttributeName&lt;/code&gt; must be &lt;code&gt;Cognito_Subject&lt;/code&gt; and &lt;code&gt;ProviderAttributeValue&lt;/code&gt; must be the subject of the SAML assertion.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminDisableProviderForUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_disable_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_disable_user

    &lt;p&gt;Deactivates a user and revokes all access tokens for the user. A deactivated user can&#39;t sign in, but still appears in the responses to &lt;code&gt;GetUser&lt;/code&gt; and &lt;code&gt;ListUsers&lt;/code&gt; API requests.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminDisableUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_enable_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_enable_user

    &lt;p&gt;Enables the specified user as an administrator. Works on any user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminEnableUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_forget_device(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_forget_device

    &lt;p&gt;Forgets the device, as an administrator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminForgetDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def admin_get_device(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_get_device

    &lt;p&gt;Gets the device, as an administrator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminGetDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def admin_get_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_get_user

    &lt;p&gt;Gets the specified user by user name in a user pool as an administrator. Works on any user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminGetUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_initiate_auth(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_initiate_auth

    &lt;p&gt;Initiates the authentication flow, as an administrator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminInitiateAuthRequest.from_dict(body)
    return web.Response(status=200)


async def admin_link_provider_for_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_link_provider_for_user

    &lt;p&gt;Links an existing user account in a user pool (&lt;code&gt;DestinationUser&lt;/code&gt;) to an identity from an external IdP (&lt;code&gt;SourceUser&lt;/code&gt;) based on a specified attribute name and value from the external IdP. This allows you to create a link from the existing user account to an external federated user identity that has not yet been used to sign in. You can then use the federated user identity to sign in as the existing user account. &lt;/p&gt; &lt;p&gt; For example, if there is an existing user with a username and password, this API links that user to a federated user identity. When the user signs in with a federated user identity, they sign in as the existing user account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The maximum number of federated identities linked to a user is five.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;Because this API allows a user with an external federated identity to sign in as an existing user in the user pool, it is critical that it only be used with external IdPs and provider attributes that have been trusted by the application owner.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminLinkProviderForUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_list_devices(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_list_devices

    &lt;p&gt;Lists devices, as an administrator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminListDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def admin_list_groups_for_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """admin_list_groups_for_user

    &lt;p&gt;Lists the groups that the user belongs to.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminListGroupsForUserRequest.from_dict(body)
    return web.Response(status=200)


async def admin_list_user_auth_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """admin_list_user_auth_events

    &lt;p&gt;A history of user activity and any risks detected as part of Amazon Cognito advanced security.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = AdminListUserAuthEventsRequest.from_dict(body)
    return web.Response(status=200)


async def admin_remove_user_from_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_remove_user_from_group

    &lt;p&gt;Removes the specified user from the specified group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminRemoveUserFromGroupRequest.from_dict(body)
    return web.Response(status=200)


async def admin_reset_user_password(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_reset_user_password

    &lt;p&gt;Resets the specified user&#39;s password in a user pool as an administrator. Works on any user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deactivates a user&#39;s password, requiring them to change it. If a user tries to sign in after the API is called, Amazon Cognito responds with a &lt;code&gt;PasswordResetRequiredException&lt;/code&gt; error. Your app must then perform the actions that reset your user&#39;s password: the forgot-password flow. In addition, if the user pool has phone verification selected and a verified phone number exists for the user, or if email verification is selected and a verified email exists for the user, calling this API will also result in sending a message to the end user with the code to change their password.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminResetUserPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def admin_respond_to_auth_challenge(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_respond_to_auth_challenge

    &lt;p&gt;Responds to an authentication challenge, as an administrator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminRespondToAuthChallengeRequest.from_dict(body)
    return web.Response(status=200)


async def admin_set_user_mfa_preference(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_set_user_mfa_preference

    &lt;p&gt;The user&#39;s multi-factor authentication (MFA) preference, including which MFA options are activated, and if any are preferred. Only one factor can be set as preferred. The preferred MFA factor will be used to authenticate a user if multiple factors are activated. If multiple options are activated and no preference is set, a challenge to choose an MFA option will be returned during sign-in.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminSetUserMFAPreferenceRequest.from_dict(body)
    return web.Response(status=200)


async def admin_set_user_password(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_set_user_password

    &lt;p&gt;Sets the specified user&#39;s password in a user pool as an administrator. Works on any user. &lt;/p&gt; &lt;p&gt;The password can be temporary or permanent. If it is temporary, the user status enters the &lt;code&gt;FORCE_CHANGE_PASSWORD&lt;/code&gt; state. When the user next tries to sign in, the InitiateAuth/AdminInitiateAuth response will contain the &lt;code&gt;NEW_PASSWORD_REQUIRED&lt;/code&gt; challenge. If the user doesn&#39;t sign in before it expires, the user won&#39;t be able to sign in, and an administrator must reset their password. &lt;/p&gt; &lt;p&gt;Once the user has set a new password, or the password is permanent, the user status is set to &lt;code&gt;Confirmed&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;AdminSetUserPassword&lt;/code&gt; can set a password for the user profile that Amazon Cognito creates for third-party federated users. When you set a password, the federated user&#39;s status changes from &lt;code&gt;EXTERNAL_PROVIDER&lt;/code&gt; to &lt;code&gt;CONFIRMED&lt;/code&gt;. A user in this state can sign in as a federated user, and initiate authentication flows in the API like a linked native user. They can also modify their password and attributes in token-authenticated API requests like &lt;code&gt;ChangePassword&lt;/code&gt; and &lt;code&gt;UpdateUserAttributes&lt;/code&gt;. As a best security practice and to keep users in sync with your external IdP, don&#39;t set passwords on federated user profiles. To set up a federated user for native sign-in with a linked native user, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html\&quot;&gt;Linking federated users to an existing user profile&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminSetUserPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def admin_set_user_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_set_user_settings

    &lt;p&gt; &lt;i&gt;This action is no longer supported.&lt;/i&gt; You can use it to configure only SMS MFA. You can&#39;t use it to configure time-based one-time password (TOTP) software token MFA. To configure either type of MFA, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.html\&quot;&gt;AdminSetUserMFAPreference&lt;/a&gt; instead.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminSetUserSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def admin_update_auth_event_feedback(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_update_auth_event_feedback

    &lt;p&gt;Provides feedback for an authentication event indicating if it was from a valid user. This feedback is used for improving the risk evaluation decision for the user pool as part of Amazon Cognito advanced security.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminUpdateAuthEventFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def admin_update_device_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_update_device_status

    &lt;p&gt;Updates the device status as an administrator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminUpdateDeviceStatusRequest.from_dict(body)
    return web.Response(status=200)


async def admin_update_user_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_update_user_attributes

    &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Updates the specified user&#39;s attributes, including developer attributes, as an administrator. Works on any user.&lt;/p&gt; &lt;p&gt;For custom attributes, you must prepend the &lt;code&gt;custom:&lt;/code&gt; prefix to the attribute name.&lt;/p&gt; &lt;p&gt;In addition to updating user attributes, this API can also be used to mark phone and email as verified.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminUpdateUserAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def admin_user_global_sign_out(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """admin_user_global_sign_out

    &lt;p&gt;Signs out a user from all devices. &lt;code&gt;AdminUserGlobalSignOut&lt;/code&gt; invalidates all identity, access and refresh tokens that Amazon Cognito has issued to a user. A user can still use a hosted UI cookie to retrieve new tokens for the duration of the 1-hour cookie validity period.&lt;/p&gt; &lt;p&gt;Your app isn&#39;t aware that a user&#39;s access token is revoked unless it attempts to authorize a user pools API request with an access token that contains the scope &lt;code&gt;aws.cognito.signin.user.admin&lt;/code&gt;. Your app might otherwise accept access tokens until they expire.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AdminUserGlobalSignOutRequest.from_dict(body)
    return web.Response(status=200)


async def associate_software_token(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_software_token

    &lt;p&gt;Begins setup of time-based one-time password (TOTP) multi-factor authentication (MFA) for a user, with a unique private key that Amazon Cognito generates and returns in the API response. You can authorize an &lt;code&gt;AssociateSoftwareToken&lt;/code&gt; request with either the user&#39;s access token, or a session string from a challenge response that you received from Amazon Cognito.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito disassociates an existing software token when you verify the new token in a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifySoftwareToken.html\&quot;&gt; VerifySoftwareToken&lt;/a&gt; API request. If you don&#39;t verify the software token and your user pool doesn&#39;t require MFA, the user can then authenticate with user name and password credentials alone. If your user pool requires TOTP MFA, Amazon Cognito generates an &lt;code&gt;MFA_SETUP&lt;/code&gt; or &lt;code&gt;SOFTWARE_TOKEN_SETUP&lt;/code&gt; challenge each time your user signs. Complete setup with &lt;code&gt;AssociateSoftwareToken&lt;/code&gt; and &lt;code&gt;VerifySoftwareToken&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;After you set up software token MFA for your user, Amazon Cognito generates a &lt;code&gt;SOFTWARE_TOKEN_MFA&lt;/code&gt; challenge when they authenticate. Respond to this challenge with your user&#39;s TOTP.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = AssociateSoftwareTokenRequest.from_dict(body)
    return web.Response(status=200)


async def change_password(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """change_password

    &lt;p&gt;Changes the password for a specified user in a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ChangePasswordRequest.from_dict(body)
    return web.Response(status=200)


async def confirm_device(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """confirm_device

    &lt;p&gt;Confirms tracking of the device. This API call is the call that begins device tracking.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ConfirmDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def confirm_forgot_password(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """confirm_forgot_password

    &lt;p&gt;Allows a user to enter a confirmation code to reset a forgotten password.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ConfirmForgotPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def confirm_sign_up(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """confirm_sign_up

    &lt;p&gt;Confirms registration of a new user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ConfirmSignUpRequest.from_dict(body)
    return web.Response(status=200)


async def create_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_group

    &lt;p&gt;Creates a new group in the specified user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_identity_provider(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_identity_provider

    &lt;p&gt;Creates an IdP for a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateIdentityProviderRequest.from_dict(body)
    return web.Response(status=200)


async def create_resource_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_resource_server

    &lt;p&gt;Creates a new OAuth2.0 resource server and defines custom scopes within it.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateResourceServerRequest.from_dict(body)
    return web.Response(status=200)


async def create_user_import_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user_import_job

    &lt;p&gt;Creates a user import job.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateUserImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_user_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user_pool

    &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a new Amazon Cognito user pool and sets the password policy for the pool.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you don&#39;t provide a value for an attribute, Amazon Cognito sets it to its default value.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateUserPoolRequest.from_dict(body)
    return web.Response(status=200)


async def create_user_pool_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user_pool_client

    &lt;p&gt;Creates the user pool client.&lt;/p&gt; &lt;p&gt;When you create a new user pool client, token revocation is automatically activated. For more information about revoking tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RevokeToken.html\&quot;&gt;RevokeToken&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you don&#39;t provide a value for an attribute, Amazon Cognito sets it to its default value.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateUserPoolClientRequest.from_dict(body)
    return web.Response(status=200)


async def create_user_pool_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_user_pool_domain

    &lt;p&gt;Creates a new domain for a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateUserPoolDomainRequest.from_dict(body)
    return web.Response(status=200)


async def delete_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_group

    &lt;p&gt;Deletes a group.&lt;/p&gt; &lt;p&gt;Calling this action requires developer credentials.&lt;/p&gt;

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
    body = DeleteGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_identity_provider(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_identity_provider

    Deletes an IdP for a user pool.

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
    body = DeleteIdentityProviderRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_server

    Deletes a resource server.

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
    body = DeleteResourceServerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user

    &lt;p&gt;Allows a user to delete their own user profile.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteUserRequest.from_dict(body)
    return web.Response(status=200)


async def delete_user_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user_attributes

    &lt;p&gt;Deletes the attributes for a user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteUserAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def delete_user_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user_pool

    Deletes the specified Amazon Cognito user pool.

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
    body = DeleteUserPoolRequest.from_dict(body)
    return web.Response(status=200)


async def delete_user_pool_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user_pool_client

    Allows the developer to delete the user pool client.

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
    body = DeleteUserPoolClientRequest.from_dict(body)
    return web.Response(status=200)


async def delete_user_pool_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_user_pool_domain

    Deletes a domain for a user pool.

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
    body = DeleteUserPoolDomainRequest.from_dict(body)
    return web.Response(status=200)


async def describe_identity_provider(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_identity_provider

    Gets information about a specific IdP.

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
    body = DescribeIdentityProviderRequest.from_dict(body)
    return web.Response(status=200)


async def describe_resource_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_resource_server

    Describes a resource server.

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
    body = DescribeResourceServerRequest.from_dict(body)
    return web.Response(status=200)


async def describe_risk_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_risk_configuration

    Describes the risk configuration.

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
    body = DescribeRiskConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_user_import_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user_import_job

    Describes the user import job.

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
    body = DescribeUserImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_user_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user_pool

    &lt;p&gt;Returns the configuration information and metadata of the specified user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeUserPoolRequest.from_dict(body)
    return web.Response(status=200)


async def describe_user_pool_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user_pool_client

    &lt;p&gt;Client method for returning the configuration information and metadata of the specified user pool app client.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeUserPoolClientRequest.from_dict(body)
    return web.Response(status=200)


async def describe_user_pool_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_user_pool_domain

    Gets information about a domain.

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
    body = DescribeUserPoolDomainRequest.from_dict(body)
    return web.Response(status=200)


async def forget_device(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """forget_device

    &lt;p&gt;Forgets the specified device.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ForgetDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def forgot_password(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """forgot_password

    &lt;p&gt;Calling this API causes a message to be sent to the end user with a confirmation code that is required to change the user&#39;s password. For the &lt;code&gt;Username&lt;/code&gt; parameter, you can use the username or user alias. The method used to send the confirmation code is sent according to the specified AccountRecoverySetting. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-recover-a-user-account.html\&quot;&gt;Recovering User Accounts&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;. To use the confirmation code for resetting the password, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.html\&quot;&gt;ConfirmForgotPassword&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If neither a verified phone number nor a verified email exists, this API returns &lt;code&gt;InvalidParameterException&lt;/code&gt;. If your app client has a client secret and you don&#39;t provide a &lt;code&gt;SECRET_HASH&lt;/code&gt; parameter, this API returns &lt;code&gt;NotAuthorizedException&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ForgotPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def get_csv_header(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_csv_header

    Gets the header information for the comma-separated value (CSV) file to be used as input for the user import job.

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
    body = GetCSVHeaderRequest.from_dict(body)
    return web.Response(status=200)


async def get_device(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_device

    &lt;p&gt;Gets the device.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = GetDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def get_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_group

    &lt;p&gt;Gets a group.&lt;/p&gt; &lt;p&gt;Calling this action requires developer credentials.&lt;/p&gt;

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
    body = GetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def get_identity_provider_by_identifier(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_identity_provider_by_identifier

    Gets the specified IdP.

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
    body = GetIdentityProviderByIdentifierRequest.from_dict(body)
    return web.Response(status=200)


async def get_log_delivery_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_log_delivery_configuration

    Gets the detailed activity logging configuration for a user pool.

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
    body = GetLogDeliveryConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def get_signing_certificate(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_signing_certificate

    &lt;p&gt;This method takes a user pool ID, and returns the signing certificate. The issued certificate is valid for 10 years from the date of issue.&lt;/p&gt; &lt;p&gt;Amazon Cognito issues and assigns a new signing certificate annually. This process returns a new value in the response to &lt;code&gt;GetSigningCertificate&lt;/code&gt;, but doesn&#39;t invalidate the original certificate.&lt;/p&gt;

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
    body = GetSigningCertificateRequest.from_dict(body)
    return web.Response(status=200)


async def get_ui_customization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_ui_customization

    Gets the user interface (UI) Customization information for a particular app client&#39;s app UI, if any such information exists for the client. If nothing is set for the particular client, but there is an existing pool level customization (the app &lt;code&gt;clientId&lt;/code&gt; is &lt;code&gt;ALL&lt;/code&gt;), then that information is returned. If nothing is present, then an empty shape is returned.

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
    body = GetUICustomizationRequest.from_dict(body)
    return web.Response(status=200)


async def get_user(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_user

    &lt;p&gt;Gets the user attributes and metadata for a user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = GetUserRequest.from_dict(body)
    return web.Response(status=200)


async def get_user_attribute_verification_code(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_user_attribute_verification_code

    &lt;p&gt;Generates a user attribute verification code for the specified attribute name. Sends a message to a user with a code that they must return in a VerifyUserAttribute request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = GetUserAttributeVerificationCodeRequest.from_dict(body)
    return web.Response(status=200)


async def get_user_pool_mfa_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_user_pool_mfa_config

    Gets the user pool multi-factor authentication (MFA) configuration.

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
    body = GetUserPoolMfaConfigRequest.from_dict(body)
    return web.Response(status=200)


async def global_sign_out(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """global_sign_out

    &lt;p&gt;Signs out a user from all devices. &lt;code&gt;GlobalSignOut&lt;/code&gt; invalidates all identity, access and refresh tokens that Amazon Cognito has issued to a user. A user can still use a hosted UI cookie to retrieve new tokens for the duration of the 1-hour cookie validity period.&lt;/p&gt; &lt;p&gt;Your app isn&#39;t aware that a user&#39;s access token is revoked unless it attempts to authorize a user pools API request with an access token that contains the scope &lt;code&gt;aws.cognito.signin.user.admin&lt;/code&gt;. Your app might otherwise accept access tokens until they expire.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = GlobalSignOutRequest.from_dict(body)
    return web.Response(status=200)


async def initiate_auth(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """initiate_auth

    &lt;p&gt;Initiates sign-in for a user in the Amazon Cognito user directory. You can&#39;t sign in a user with a federated IdP with &lt;code&gt;InitiateAuth&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html\&quot;&gt; Adding user pool sign-in through a third party&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = InitiateAuthRequest.from_dict(body)
    return web.Response(status=200)


async def list_devices(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_devices

    &lt;p&gt;Lists the sign-in devices that Amazon Cognito has registered to the current user.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ListDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def list_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_groups

    &lt;p&gt;Lists the groups associated with a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = ListGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_identity_providers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_identity_providers

    &lt;p&gt;Lists information about all IdPs for a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListIdentityProvidersRequest.from_dict(body)
    return web.Response(status=200)


async def list_resource_servers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_resource_servers

    &lt;p&gt;Lists the resource servers for a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListResourceServersRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists the tags that are assigned to an Amazon Cognito user pool.&lt;/p&gt; &lt;p&gt;A tag is a label that you can apply to user pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.&lt;/p&gt; &lt;p&gt;You can use this action up to 10 times per second, per account.&lt;/p&gt;

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


async def list_user_import_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_user_import_jobs

    &lt;p&gt;Lists user import jobs for a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = ListUserImportJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_user_pool_clients(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_user_pool_clients

    &lt;p&gt;Lists the clients that have been created for the specified user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListUserPoolClientsRequest.from_dict(body)
    return web.Response(status=200)


async def list_user_pools(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_user_pools

    &lt;p&gt;Lists the user pools associated with an Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListUserPoolsRequest.from_dict(body)
    return web.Response(status=200)


async def list_users(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, pagination_token=None) -> web.Response:
    """list_users

    &lt;p&gt;Lists users and their basic details in a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    :param pagination_token: Pagination token
    :type pagination_token: str

    """
    body = ListUsersRequest.from_dict(body)
    return web.Response(status=200)


async def list_users_in_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, next_token=None) -> web.Response:
    """list_users_in_group

    &lt;p&gt;Lists the users in the specified group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = ListUsersInGroupRequest.from_dict(body)
    return web.Response(status=200)


async def resend_confirmation_code(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resend_confirmation_code

    &lt;p&gt;Resends the confirmation (for confirmation of registration) to a specific user in the user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ResendConfirmationCodeRequest.from_dict(body)
    return web.Response(status=200)


async def respond_to_auth_challenge(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """respond_to_auth_challenge

    &lt;p&gt;Responds to the authentication challenge.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = RespondToAuthChallengeRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_token(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """revoke_token

    &lt;p&gt;Revokes all of the access tokens generated by, and at the same time as, the specified refresh token. After a token is revoked, you can&#39;t use the revoked token to access Amazon Cognito user APIs, or to authorize access to your resource server.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = RevokeTokenRequest.from_dict(body)
    return web.Response(status=200)


async def set_log_delivery_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_log_delivery_configuration

    Sets up or modifies the detailed activity logging configuration of a user pool.

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
    body = SetLogDeliveryConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def set_risk_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_risk_configuration

    &lt;p&gt;Configures actions on detected risks. To delete the risk configuration for &lt;code&gt;UserPoolId&lt;/code&gt; or &lt;code&gt;ClientId&lt;/code&gt;, pass null values for all four configuration types.&lt;/p&gt; &lt;p&gt;To activate Amazon Cognito advanced security features, update the user pool to include the &lt;code&gt;UserPoolAddOns&lt;/code&gt; key&lt;code&gt;AdvancedSecurityMode&lt;/code&gt;.&lt;/p&gt;

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
    body = SetRiskConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def set_ui_customization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_ui_customization

    &lt;p&gt;Sets the user interface (UI) customization information for a user pool&#39;s built-in app UI.&lt;/p&gt; &lt;p&gt;You can specify app UI customization settings for a single client (with a specific &lt;code&gt;clientId&lt;/code&gt;) or for all clients (by setting the &lt;code&gt;clientId&lt;/code&gt; to &lt;code&gt;ALL&lt;/code&gt;). If you specify &lt;code&gt;ALL&lt;/code&gt;, the default configuration is used for every client that has no previously set UI customization. If you specify UI customization settings for a particular client, it will no longer return to the &lt;code&gt;ALL&lt;/code&gt; configuration.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this API, your user pool must have a domain associated with it. Otherwise, there is no place to host the app&#39;s pages, and the service will throw an error.&lt;/p&gt; &lt;/note&gt;

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
    body = SetUICustomizationRequest.from_dict(body)
    return web.Response(status=200)


async def set_user_mfa_preference(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_user_mfa_preference

    &lt;p&gt;Set the user&#39;s multi-factor authentication (MFA) method preference, including which MFA factors are activated and if any are preferred. Only one factor can be set as preferred. The preferred MFA factor will be used to authenticate a user if multiple factors are activated. If multiple options are activated and no preference is set, a challenge to choose an MFA option will be returned during sign-in. If an MFA type is activated for a user, the user will be prompted for MFA during all sign-in attempts unless device tracking is turned on and the device has been trusted. If you want MFA to be applied selectively based on the assessed risk level of sign-in attempts, deactivate MFA for users and turn on Adaptive Authentication for the user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = SetUserMFAPreferenceRequest.from_dict(body)
    return web.Response(status=200)


async def set_user_pool_mfa_config(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_user_pool_mfa_config

    &lt;p&gt;Sets the user pool multi-factor authentication (MFA) configuration.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = SetUserPoolMfaConfigRequest.from_dict(body)
    return web.Response(status=200)


async def set_user_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_user_settings

    &lt;p&gt; &lt;i&gt;This action is no longer supported.&lt;/i&gt; You can use it to configure only SMS MFA. You can&#39;t use it to configure time-based one-time password (TOTP) software token MFA. To configure either type of MFA, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.html\&quot;&gt;SetUserMFAPreference&lt;/a&gt; instead.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = SetUserSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def sign_up(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """sign_up

    &lt;p&gt;Registers the user in the specified user pool and creates a user name, password, and user attributes.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = SignUpRequest.from_dict(body)
    return web.Response(status=200)


async def start_user_import_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_user_import_job

    Starts the user import.

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
    body = StartUserImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_user_import_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_user_import_job

    Stops the user import job.

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
    body = StopUserImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns a set of tags to an Amazon Cognito user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and value, both of which you define. A key is a general category for more specific values. For example, if you have two versions of a user pool, one for testing and another for production, you might assign an &lt;code&gt;Environment&lt;/code&gt; tag key to both user pools. The value of this key might be &lt;code&gt;Test&lt;/code&gt; for one user pool, and &lt;code&gt;Production&lt;/code&gt; for the other.&lt;/p&gt; &lt;p&gt;Tags are useful for cost tracking and access control. You can activate your tags so that they appear on the Billing and Cost Management console, where you can track the costs associated with your user pools. In an Identity and Access Management policy, you can constrain permissions for user pools based on specific tags or tag values.&lt;/p&gt; &lt;p&gt;You can use this action up to 5 times per second, per account. A user pool can have as many as 50 tags.&lt;/p&gt;

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

    Removes the specified tags from an Amazon Cognito user pool. You can use this action up to 5 times per second, per account.

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


async def update_auth_event_feedback(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_auth_event_feedback

    &lt;p&gt;Provides the feedback for an authentication event, whether it was from a valid user or not. This feedback is used for improving the risk evaluation decision for the user pool as part of Amazon Cognito advanced security.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateAuthEventFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_device_status

    &lt;p&gt;Updates the device status.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateDeviceStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_group

    &lt;p&gt;Updates the specified group with the specified attributes.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_identity_provider(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_identity_provider

    &lt;p&gt;Updates IdP information for a user pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateIdentityProviderRequest.from_dict(body)
    return web.Response(status=200)


async def update_resource_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_resource_server

    &lt;p&gt;Updates the name and scopes of resource server. All other fields are read-only.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you don&#39;t provide a value for an attribute, it is set to the default value.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateResourceServerRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_attributes

    &lt;p&gt;Allows a user to update a specific attribute (one at a time).&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateUserAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_pool

    &lt;note&gt; &lt;p&gt;This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/pinpoint/home/\&quot;&gt;Amazon Pinpoint&lt;/a&gt;. Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.&lt;/p&gt; &lt;p&gt;If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Service, Amazon Simple Notification Service might place your account in the SMS sandbox. In &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;sandbox mode&lt;/a&gt; &lt;/i&gt;, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\&quot;&gt; SMS message settings for Amazon Cognito user pools&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Updates the specified user pool with the specified attributes. You can get a list of the current user pool settings using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html\&quot;&gt;DescribeUserPool&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you don&#39;t provide a value for an attribute, Amazon Cognito sets it to its default value.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateUserPoolRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_pool_client(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_pool_client

    &lt;p&gt;Updates the specified user pool app client with the specified attributes. You can get a list of the current user pool app client settings using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html\&quot;&gt;DescribeUserPoolClient&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you don&#39;t provide a value for an attribute, Amazon Cognito sets it to its default value.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You can also use this operation to enable token revocation for user pool clients. For more information about revoking tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RevokeToken.html\&quot;&gt;RevokeToken&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateUserPoolClientRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_pool_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_user_pool_domain

    &lt;p&gt;Updates the Secure Sockets Layer (SSL) certificate for the custom domain for your user pool.&lt;/p&gt; &lt;p&gt;You can use this operation to provide the Amazon Resource Name (ARN) of a new certificate to Amazon Cognito. You can&#39;t use it to change the domain for a user pool.&lt;/p&gt; &lt;p&gt;A custom domain is used to host the Amazon Cognito hosted UI, which provides sign-up and sign-in pages for your application. When you set up a custom domain, you provide a certificate that you manage with Certificate Manager (ACM). When necessary, you can use this operation to change the certificate that you applied to your custom domain.&lt;/p&gt; &lt;p&gt;Usually, this is unnecessary following routine certificate renewal with ACM. When you renew your existing certificate in ACM, the ARN for your certificate remains the same, and your custom domain uses the new certificate automatically.&lt;/p&gt; &lt;p&gt;However, if you replace your existing certificate with a new one, ACM gives the new certificate a new ARN. To apply the new certificate to your custom domain, you must provide this ARN to Amazon Cognito.&lt;/p&gt; &lt;p&gt;When you add your new certificate in ACM, you must choose US East (N. Virginia) as the Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;After you submit your request, Amazon Cognito requires up to 1 hour to distribute your new certificate to your custom domain.&lt;/p&gt; &lt;p&gt;For more information about adding a custom domain to your user pool, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html\&quot;&gt;Using Your Own Domain for the Hosted UI&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Learn more&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html\&quot;&gt;Signing Amazon Web Services API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = UpdateUserPoolDomainRequest.from_dict(body)
    return web.Response(status=200)


async def verify_software_token(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """verify_software_token

    &lt;p&gt;Use this API to register a user&#39;s entered time-based one-time password (TOTP) code and mark the user&#39;s software token MFA status as \&quot;verified\&quot; if successful. The request takes an access token or a session string, but not both.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = VerifySoftwareTokenRequest.from_dict(body)
    return web.Response(status=200)


async def verify_user_attribute(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """verify_user_attribute

    &lt;p&gt;Verifies the specified user attributes in the user pool.&lt;/p&gt; &lt;p&gt; If your user pool requires verification before Amazon Cognito updates the attribute value, VerifyUserAttribute updates the affected attribute to its pending value. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserAttributeUpdateSettingsType.html\&quot;&gt; UserAttributeUpdateSettingsType&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Cognito doesn&#39;t evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can&#39;t use IAM credentials to authorize requests, and you can&#39;t grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = VerifyUserAttributeRequest.from_dict(body)
    return web.Response(status=200)
