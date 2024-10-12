from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_permission_input import AddPermissionInput
from openapi_server.models.check_if_phone_number_is_opted_out_input import CheckIfPhoneNumberIsOptedOutInput
from openapi_server.models.check_if_phone_number_is_opted_out_response import CheckIfPhoneNumberIsOptedOutResponse
from openapi_server.models.confirm_subscription_input import ConfirmSubscriptionInput
from openapi_server.models.confirm_subscription_response import ConfirmSubscriptionResponse
from openapi_server.models.create_endpoint_response import CreateEndpointResponse
from openapi_server.models.create_platform_application_input import CreatePlatformApplicationInput
from openapi_server.models.create_platform_application_response import CreatePlatformApplicationResponse
from openapi_server.models.create_platform_endpoint_input import CreatePlatformEndpointInput
from openapi_server.models.create_sms_sandbox_phone_number_input import CreateSMSSandboxPhoneNumberInput
from openapi_server.models.create_topic_input import CreateTopicInput
from openapi_server.models.create_topic_response import CreateTopicResponse
from openapi_server.models.delete_endpoint_input import DeleteEndpointInput
from openapi_server.models.delete_platform_application_input import DeletePlatformApplicationInput
from openapi_server.models.delete_sms_sandbox_phone_number_input import DeleteSMSSandboxPhoneNumberInput
from openapi_server.models.delete_topic_input import DeleteTopicInput
from openapi_server.models.get_data_protection_policy_input import GetDataProtectionPolicyInput
from openapi_server.models.get_data_protection_policy_response import GetDataProtectionPolicyResponse
from openapi_server.models.get_endpoint_attributes_input import GetEndpointAttributesInput
from openapi_server.models.get_endpoint_attributes_response import GetEndpointAttributesResponse
from openapi_server.models.get_platform_application_attributes_input import GetPlatformApplicationAttributesInput
from openapi_server.models.get_platform_application_attributes_response import GetPlatformApplicationAttributesResponse
from openapi_server.models.get_sms_attributes_input import GetSMSAttributesInput
from openapi_server.models.get_sms_attributes_response import GetSMSAttributesResponse
from openapi_server.models.get_sms_sandbox_account_status_result import GetSMSSandboxAccountStatusResult
from openapi_server.models.get_subscription_attributes_input import GetSubscriptionAttributesInput
from openapi_server.models.get_subscription_attributes_response import GetSubscriptionAttributesResponse
from openapi_server.models.get_topic_attributes_input import GetTopicAttributesInput
from openapi_server.models.get_topic_attributes_response import GetTopicAttributesResponse
from openapi_server.models.list_endpoints_by_platform_application_input import ListEndpointsByPlatformApplicationInput
from openapi_server.models.list_endpoints_by_platform_application_response import ListEndpointsByPlatformApplicationResponse
from openapi_server.models.list_origination_numbers_request import ListOriginationNumbersRequest
from openapi_server.models.list_origination_numbers_result import ListOriginationNumbersResult
from openapi_server.models.list_phone_numbers_opted_out_input import ListPhoneNumbersOptedOutInput
from openapi_server.models.list_phone_numbers_opted_out_response import ListPhoneNumbersOptedOutResponse
from openapi_server.models.list_platform_applications_input import ListPlatformApplicationsInput
from openapi_server.models.list_platform_applications_response import ListPlatformApplicationsResponse
from openapi_server.models.list_sms_sandbox_phone_numbers_input import ListSMSSandboxPhoneNumbersInput
from openapi_server.models.list_sms_sandbox_phone_numbers_result import ListSMSSandboxPhoneNumbersResult
from openapi_server.models.list_subscriptions_by_topic_input import ListSubscriptionsByTopicInput
from openapi_server.models.list_subscriptions_by_topic_response import ListSubscriptionsByTopicResponse
from openapi_server.models.list_subscriptions_input import ListSubscriptionsInput
from openapi_server.models.list_subscriptions_response import ListSubscriptionsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_topics_input import ListTopicsInput
from openapi_server.models.list_topics_response import ListTopicsResponse
from openapi_server.models.message_attribute_value import MessageAttributeValue
from openapi_server.models.opt_in_phone_number_input import OptInPhoneNumberInput
from openapi_server.models.publish_batch_input import PublishBatchInput
from openapi_server.models.publish_batch_request_entry import PublishBatchRequestEntry
from openapi_server.models.publish_batch_response import PublishBatchResponse
from openapi_server.models.publish_input import PublishInput
from openapi_server.models.publish_response import PublishResponse
from openapi_server.models.put_data_protection_policy_input import PutDataProtectionPolicyInput
from openapi_server.models.remove_permission_input import RemovePermissionInput
from openapi_server.models.set_endpoint_attributes_input import SetEndpointAttributesInput
from openapi_server.models.set_platform_application_attributes_input import SetPlatformApplicationAttributesInput
from openapi_server.models.set_sms_attributes_input import SetSMSAttributesInput
from openapi_server.models.set_subscription_attributes_input import SetSubscriptionAttributesInput
from openapi_server.models.set_topic_attributes_input import SetTopicAttributesInput
from openapi_server.models.subscribe_input import SubscribeInput
from openapi_server.models.subscribe_response import SubscribeResponse
from openapi_server.models.tag import Tag
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.unsubscribe_input import UnsubscribeInput
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.verify_sms_sandbox_phone_number_input import VerifySMSSandboxPhoneNumberInput
from openapi_server import util


async def g_et_add_permission(request: web.Request, topic_arn, label, aws_account_id, action_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_permission

    &lt;p&gt;Adds a statement to a topic&#39;s access control policy, granting access for the specified Amazon Web Services accounts to the specified actions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To remove the ability to change topic permissions, you must deny permissions to the &lt;code&gt;AddPermission&lt;/code&gt;, &lt;code&gt;RemovePermission&lt;/code&gt;, and &lt;code&gt;SetTopicAttributes&lt;/code&gt; actions in your IAM policy.&lt;/p&gt; &lt;/note&gt;

    :param topic_arn: The ARN of the topic whose access control policy you wish to modify.
    :type topic_arn: str
    :param label: A unique identifier for the new policy statement.
    :type label: str
    :param aws_account_id: The Amazon Web Services account IDs of the users (principals) who will be given access to the specified actions. The users must have Amazon Web Services account, but do not need to be signed up for this service.
    :type aws_account_id: List[str]
    :param action_name: &lt;p&gt;The action you want to allow for the specified principal(s).&lt;/p&gt; &lt;p&gt;Valid values: Any Amazon SNS action name, for example &lt;code&gt;Publish&lt;/code&gt;.&lt;/p&gt;
    :type action_name: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_check_if_phone_number_is_opted_out(request: web.Request, phone_number, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_check_if_phone_number_is_opted_out

    &lt;p&gt;Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your Amazon Web Services account. You cannot send SMS messages to a number that is opted out.&lt;/p&gt; &lt;p&gt;To resume sending messages, you can opt in the number by using the &lt;code&gt;OptInPhoneNumber&lt;/code&gt; action.&lt;/p&gt;

    :param phone_number: The phone number for which you want to check the opt out status.
    :type phone_number: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_confirm_subscription(request: web.Request, topic_arn, token, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, authenticate_on_unsubscribe=None) -> web.Response:
    """g_et_confirm_subscription

    Verifies an endpoint owner&#39;s intent to receive messages by validating the token sent to the endpoint by an earlier &lt;code&gt;Subscribe&lt;/code&gt; action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the &lt;code&gt;AuthenticateOnUnsubscribe&lt;/code&gt; flag is set to \&quot;true\&quot;.

    :param topic_arn: The ARN of the topic for which you wish to confirm a subscription.
    :type topic_arn: str
    :param token: Short-lived token sent to an endpoint during the &lt;code&gt;Subscribe&lt;/code&gt; action.
    :type token: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param authenticate_on_unsubscribe: Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is &lt;code&gt;true&lt;/code&gt; and the request has an Amazon Web Services signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires Amazon Web Services authentication. 
    :type authenticate_on_unsubscribe: str

    """
    return web.Response(status=200)


async def g_et_create_platform_application(request: web.Request, name, platform, attributes, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_platform_application

    &lt;p&gt;Creates a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging), to which devices and mobile apps may register. You must specify &lt;code&gt;PlatformPrincipal&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; attributes when using the &lt;code&gt;CreatePlatformApplication&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PlatformPrincipal&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; are received from the notification service.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;ADM&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;client id&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;client secret&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;Baidu&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;API key&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;secret key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;APNS&lt;/code&gt; and &lt;code&gt;APNS_SANDBOX&lt;/code&gt; using certificate credentials, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;SSL certificate&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;private key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;APNS&lt;/code&gt; and &lt;code&gt;APNS_SANDBOX&lt;/code&gt; using token credentials, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;signing key ID&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;signing key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;GCM&lt;/code&gt; (Firebase Cloud Messaging), there is no &lt;code&gt;PlatformPrincipal&lt;/code&gt; and the &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;API key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;MPNS&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;TLS certificate&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;private key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;WNS&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;Package Security Identifier&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;secret key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can use the returned &lt;code&gt;PlatformApplicationArn&lt;/code&gt; as an attribute for the &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; action.&lt;/p&gt;

    :param name: Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.
    :type name: str
    :param platform: The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Firebase Cloud Messaging).
    :type platform: str
    :param attributes: For a list of attributes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html\&quot;&gt;SetPlatformApplicationAttributes&lt;/a&gt;.
    :type attributes: Dict[str, str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_create_platform_endpoint(request: web.Request, platform_application_arn, token, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, custom_user_data=None, attributes=None) -> web.Response:
    """g_et_create_platform_endpoint

    &lt;p&gt;Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; requires the &lt;code&gt;PlatformApplicationArn&lt;/code&gt; that is returned from &lt;code&gt;CreatePlatformApplication&lt;/code&gt;. You can use the returned &lt;code&gt;EndpointArn&lt;/code&gt; to send a message to a mobile app or by the &lt;code&gt;Subscribe&lt;/code&gt; action for subscription to a topic. The &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint&#39;s ARN is returned without creating a new endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;When using &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePushBaiduEndpoint.html\&quot;&gt;Creating an Amazon SNS Endpoint for Baidu&lt;/a&gt;. &lt;/p&gt;

    :param platform_application_arn: PlatformApplicationArn returned from CreatePlatformApplication is used to create a an endpoint.
    :type platform_application_arn: str
    :param token: Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM (Firebase Cloud Messaging) or ADM, the device token equivalent is called the registration ID.
    :type token: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param custom_user_data: Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
    :type custom_user_data: str
    :param attributes: For a list of attributes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html\&quot;&gt;SetEndpointAttributes&lt;/a&gt;.
    :type attributes: Dict[str, str]

    """
    return web.Response(status=200)


async def g_et_create_sms_sandbox_phone_number(request: web.Request, phone_number, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, language_code=None) -> web.Response:
    """g_et_create_sms_sandbox_phone_number

    &lt;p&gt;Adds a destination phone number to an Amazon Web Services account in the SMS sandbox and sends a one-time password (OTP) to that phone number.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param phone_number: The destination phone number to verify. On verification, Amazon SNS adds this phone number to the list of verified phone numbers that you can send SMS messages to.
    :type phone_number: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param language_code: The language to use for sending the OTP. The default value is &lt;code&gt;en-US&lt;/code&gt;.
    :type language_code: str

    """
    return web.Response(status=200)


async def g_et_create_topic(request: web.Request, name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, attributes=None, tags=None, data_protection_policy=None) -> web.Response:
    """g_et_create_topic

    Creates a topic to which notifications can be published. Users can create at most 100,000 standard topics (at most 1,000 FIFO topics). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html\&quot;&gt;Creating an Amazon SNS topic&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;. This action is idempotent, so if the requester already owns a topic with the specified name, that topic&#39;s ARN is returned without creating a new topic.

    :param name: &lt;p&gt;The name of the topic you want to create.&lt;/p&gt; &lt;p&gt;Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.&lt;/p&gt; &lt;p&gt;For a FIFO (first-in-first-out) topic, the name must end with the &lt;code&gt;.fifo&lt;/code&gt; suffix. &lt;/p&gt;
    :type name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param attributes: &lt;p&gt;A map of attributes with their corresponding values.&lt;/p&gt; &lt;p&gt;The following lists the names, descriptions, and values of the special request parameters that the &lt;code&gt;CreateTopic&lt;/code&gt; action uses:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeliveryPolicy&lt;/code&gt; – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DisplayName&lt;/code&gt; – The display name to use for a topic with SMS subscriptions.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FifoTopic&lt;/code&gt; – Set to true to create a FIFO topic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Policy&lt;/code&gt; – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SignatureVersion&lt;/code&gt; – The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, &lt;code&gt;SignatureVersion&lt;/code&gt; is set to &lt;code&gt;1&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TracingConfig&lt;/code&gt; – Tracing mode of an Amazon SNS topic. By default &lt;code&gt;TracingConfig&lt;/code&gt; is set to &lt;code&gt;PassThrough&lt;/code&gt;, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to &lt;code&gt;Active&lt;/code&gt;, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following attribute applies only to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html\&quot;&gt;server-side encryption&lt;/a&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;KmsMasterKeyId&lt;/code&gt; – The ID of an Amazon Web Services managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms\&quot;&gt;Key Terms&lt;/a&gt;. For more examples, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters\&quot;&gt;KeyId&lt;/a&gt; in the &lt;i&gt;Key Management Service API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following attributes apply only to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html\&quot;&gt;FIFO topics&lt;/a&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FifoTopic&lt;/code&gt; – When this is set to &lt;code&gt;true&lt;/code&gt;, a FIFO topic is created.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ContentBasedDeduplication&lt;/code&gt; – Enables content-based deduplication for FIFO topics.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;By default, &lt;code&gt;ContentBasedDeduplication&lt;/code&gt; is set to &lt;code&gt;false&lt;/code&gt;. If you create a FIFO topic and this attribute is &lt;code&gt;false&lt;/code&gt;, you must specify a value for the &lt;code&gt;MessageDeduplicationId&lt;/code&gt; parameter for the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/api/API_Publish.html\&quot;&gt;Publish&lt;/a&gt; action. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you set &lt;code&gt;ContentBasedDeduplication&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;, Amazon SNS uses a SHA-256 hash to generate the &lt;code&gt;MessageDeduplicationId&lt;/code&gt; using the body of the message (but not the attributes of the message).&lt;/p&gt; &lt;p&gt;(Optional) To override the generated value, you can specify a value for the &lt;code&gt;MessageDeduplicationId&lt;/code&gt; parameter for the &lt;code&gt;Publish&lt;/code&gt; action.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;
    :type attributes: Dict[str, str]
    :param tags: &lt;p&gt;The list of tags to add to a new topic.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To be able to tag a topic on creation, you must have the &lt;code&gt;sns:CreateTopic&lt;/code&gt; and &lt;code&gt;sns:TagResource&lt;/code&gt; permissions.&lt;/p&gt; &lt;/note&gt;
    :type tags: list | bytes
    :param data_protection_policy: &lt;p&gt;The body of the policy document you want to use for this topic.&lt;/p&gt; &lt;p&gt;You can only add one policy per topic.&lt;/p&gt; &lt;p&gt;The policy must be in JSON string format.&lt;/p&gt; &lt;p&gt;Length Constraints: Maximum length of 30,720.&lt;/p&gt;
    :type data_protection_policy: str

    """
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_delete_endpoint(request: web.Request, endpoint_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_endpoint

    &lt;p&gt;Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.&lt;/p&gt;

    :param endpoint_arn: EndpointArn of endpoint to delete.
    :type endpoint_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_platform_application(request: web.Request, platform_application_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_platform_application

    Deletes a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param platform_application_arn: PlatformApplicationArn of platform application object to delete.
    :type platform_application_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_sms_sandbox_phone_number(request: web.Request, phone_number, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_sms_sandbox_phone_number

    &lt;p&gt;Deletes an Amazon Web Services account&#39;s verified or pending phone number from the SMS sandbox.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param phone_number: The destination phone number to delete.
    :type phone_number: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_topic(request: web.Request, topic_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_topic

    Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.

    :param topic_arn: The ARN of the topic you want to delete.
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


async def g_et_get_data_protection_policy(request: web.Request, resource_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_data_protection_policy

    Retrieves the specified inline &lt;code&gt;DataProtectionPolicy&lt;/code&gt; document that is stored in the specified Amazon SNS topic. 

    :param resource_arn: &lt;p&gt;The ARN of the topic whose &lt;code&gt;DataProtectionPolicy&lt;/code&gt; you want to get.&lt;/p&gt; &lt;p&gt;For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the Amazon Web Services General Reference.&lt;/p&gt;
    :type resource_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_endpoint_attributes(request: web.Request, endpoint_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_endpoint_attributes

    Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param endpoint_arn: EndpointArn for GetEndpointAttributes input.
    :type endpoint_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_platform_application_attributes(request: web.Request, platform_application_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_platform_application_attributes

    Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param platform_application_arn: PlatformApplicationArn for GetPlatformApplicationAttributesInput.
    :type platform_application_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_sms_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, attributes=None) -> web.Response:
    """g_et_get_sms_attributes

    &lt;p&gt;Returns the settings for sending SMS messages from your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;These settings are set with the &lt;code&gt;SetSMSAttributes&lt;/code&gt; action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param attributes: &lt;p&gt;A list of the individual attribute names, such as &lt;code&gt;MonthlySpendLimit&lt;/code&gt;, for which you want values.&lt;/p&gt; &lt;p&gt;For all attribute names, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html\&quot;&gt;SetSMSAttributes&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t use this parameter, Amazon SNS returns all SMS attributes.&lt;/p&gt;
    :type attributes: List[str]

    """
    return web.Response(status=200)


async def g_et_get_sms_sandbox_account_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_sms_sandbox_account_status

    &lt;p&gt;Retrieves the SMS sandbox status for the calling Amazon Web Services account in the target Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_subscription_attributes(request: web.Request, subscription_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_subscription_attributes

    Returns all of the properties of a subscription.

    :param subscription_arn: The ARN of the subscription whose properties you want to get.
    :type subscription_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_topic_attributes(request: web.Request, topic_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_topic_attributes

    Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.

    :param topic_arn: The ARN of the topic whose properties you want to get.
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


async def g_et_list_endpoints_by_platform_application(request: web.Request, platform_application_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_endpoints_by_platform_application

    &lt;p&gt;Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM (Firebase Cloud Messaging) and APNS. The results for &lt;code&gt;ListEndpointsByPlatformApplication&lt;/code&gt; are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call &lt;code&gt;ListEndpointsByPlatformApplication&lt;/code&gt; again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param platform_application_arn: PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.
    :type platform_application_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: NextToken string is used when calling ListEndpointsByPlatformApplication action to retrieve additional records that are available after the first page results.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_origination_numbers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """g_et_list_origination_numbers

    Lists the calling Amazon Web Services account&#39;s dedicated origination numbers and their metadata. For more information about origination numbers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/channels-sms-originating-identities-origination-numbers.html\&quot;&gt;Origination numbers&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Token that the previous &lt;code&gt;ListOriginationNumbers&lt;/code&gt; request returns.
    :type next_token: str
    :param max_results: The maximum number of origination numbers to return.
    :type max_results: int

    """
    return web.Response(status=200)


async def g_et_list_phone_numbers_opted_out(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_phone_numbers_opted_out

    &lt;p&gt;Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them.&lt;/p&gt; &lt;p&gt;The results for &lt;code&gt;ListPhoneNumbersOptedOut&lt;/code&gt; are paginated, and each page returns up to 100 phone numbers. If additional phone numbers are available after the first page of results, then a &lt;code&gt;NextToken&lt;/code&gt; string will be returned. To receive the next page, you call &lt;code&gt;ListPhoneNumbersOptedOut&lt;/code&gt; again using the &lt;code&gt;NextToken&lt;/code&gt; string received from the previous call. When there are no more records to return, &lt;code&gt;NextToken&lt;/code&gt; will be null.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A &lt;code&gt;NextToken&lt;/code&gt; string is used when you call the &lt;code&gt;ListPhoneNumbersOptedOut&lt;/code&gt; action to retrieve additional records that are available after the first page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_platform_applications(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_platform_applications

    &lt;p&gt;Lists the platform application objects for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). The results for &lt;code&gt;ListPlatformApplications&lt;/code&gt; are paginated and return a limited list of applications, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call &lt;code&gt;ListPlatformApplications&lt;/code&gt; using the NextToken string received from the previous call. When there are no more records to return, &lt;code&gt;NextToken&lt;/code&gt; will be null. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This action is throttled at 15 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: NextToken string is used when calling ListPlatformApplications action to retrieve additional records that are available after the first page results.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_sms_sandbox_phone_numbers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """g_et_list_sms_sandbox_phone_numbers

    &lt;p&gt;Lists the calling Amazon Web Services account&#39;s current verified and pending destination phone numbers in the SMS sandbox.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Token that the previous &lt;code&gt;ListSMSSandboxPhoneNumbersInput&lt;/code&gt; request returns.
    :type next_token: str
    :param max_results: The maximum number of phone numbers to return.
    :type max_results: int

    """
    return web.Response(status=200)


async def g_et_list_subscriptions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_subscriptions

    &lt;p&gt;Returns a list of the requester&#39;s subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a &lt;code&gt;NextToken&lt;/code&gt; is also returned. Use the &lt;code&gt;NextToken&lt;/code&gt; parameter in a new &lt;code&gt;ListSubscriptions&lt;/code&gt; call to get further results.&lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Token returned by the previous &lt;code&gt;ListSubscriptions&lt;/code&gt; request.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_subscriptions_by_topic(request: web.Request, topic_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_subscriptions_by_topic

    &lt;p&gt;Returns a list of the subscriptions to a specific topic. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a &lt;code&gt;NextToken&lt;/code&gt; is also returned. Use the &lt;code&gt;NextToken&lt;/code&gt; parameter in a new &lt;code&gt;ListSubscriptionsByTopic&lt;/code&gt; call to get further results.&lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param topic_arn: The ARN of the topic for which you wish to find subscriptions.
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
    :param next_token: Token returned by the previous &lt;code&gt;ListSubscriptionsByTopic&lt;/code&gt; request.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_tags_for_resource(request: web.Request, resource_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_tags_for_resource

    List all tags added to the specified Amazon SNS topic. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html\&quot;&gt;Amazon SNS Tags&lt;/a&gt; in the &lt;i&gt;Amazon Simple Notification Service Developer Guide&lt;/i&gt;.

    :param resource_arn: The ARN of the topic for which to list tags.
    :type resource_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_list_topics(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_topics

    &lt;p&gt;Returns a list of the requester&#39;s topics. Each call returns a limited list of topics, up to 100. If there are more topics, a &lt;code&gt;NextToken&lt;/code&gt; is also returned. Use the &lt;code&gt;NextToken&lt;/code&gt; parameter in a new &lt;code&gt;ListTopics&lt;/code&gt; call to get further results.&lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Token returned by the previous &lt;code&gt;ListTopics&lt;/code&gt; request.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_opt_in_phone_number(request: web.Request, phone_number, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_opt_in_phone_number

    &lt;p&gt;Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number.&lt;/p&gt; &lt;p&gt;You can opt in a phone number only once every 30 days.&lt;/p&gt;

    :param phone_number: The phone number to opt in. Use E.164 format.
    :type phone_number: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_publish(request: web.Request, message, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, topic_arn=None, target_arn=None, phone_number=None, subject=None, message_structure=None, message_attributes=None, message_deduplication_id=None, message_group_id=None) -> web.Response:
    """g_et_publish

    &lt;p&gt;Sends a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify the &lt;code&gt;TargetArn&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.&lt;/p&gt; &lt;p&gt;When a &lt;code&gt;messageId&lt;/code&gt; is returned, the message is saved and Amazon SNS immediately delivers it to subscribers.&lt;/p&gt; &lt;p&gt;To use the &lt;code&gt;Publish&lt;/code&gt; action for publishing a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; action. &lt;/p&gt; &lt;p&gt;For more information about formatting messages, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html\&quot;&gt;Send Custom Platform-Specific Payloads in Messages to Mobile Devices&lt;/a&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can publish messages only to topics and endpoints in the same Amazon Web Services Region.&lt;/p&gt; &lt;/important&gt;

    :param message: &lt;p&gt;The message you want to send.&lt;/p&gt; &lt;p&gt;If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the &lt;code&gt;MessageStructure&lt;/code&gt; parameter to &lt;code&gt;json&lt;/code&gt; and use a JSON object for the &lt;code&gt;Message&lt;/code&gt; parameter. &lt;/p&gt; &lt;p/&gt; &lt;p&gt;Constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters.&lt;/p&gt; &lt;p&gt;If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages aren&#39;t truncated mid-word but are cut off at whole-word boundaries.&lt;/p&gt; &lt;p&gt;The total size limit for a single SMS &lt;code&gt;Publish&lt;/code&gt; action is 1,600 characters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;JSON-specific constraints:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The values will be parsed (unescaped) before they are used in outgoing messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Values have a minimum length of 0 (the empty string, \&quot;\&quot;, is allowed).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Non-string values will cause the key to be ignored.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Keys that do not correspond to supported transport protocols are ignored.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Duplicate keys are not allowed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Failure to parse or validate any key or value in the message will cause the &lt;code&gt;Publish&lt;/code&gt; call to return an error (no partial delivery).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type message: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param topic_arn: &lt;p&gt;The topic you want to publish to.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for the &lt;code&gt;TopicArn&lt;/code&gt; parameter, you must specify a value for the &lt;code&gt;PhoneNumber&lt;/code&gt; or &lt;code&gt;TargetArn&lt;/code&gt; parameters.&lt;/p&gt;
    :type topic_arn: str
    :param target_arn: If you don&#39;t specify a value for the &lt;code&gt;TargetArn&lt;/code&gt; parameter, you must specify a value for the &lt;code&gt;PhoneNumber&lt;/code&gt; or &lt;code&gt;TopicArn&lt;/code&gt; parameters.
    :type target_arn: str
    :param phone_number: &lt;p&gt;The phone number to which you want to deliver an SMS message. Use E.164 format.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for the &lt;code&gt;PhoneNumber&lt;/code&gt; parameter, you must specify a value for the &lt;code&gt;TargetArn&lt;/code&gt; or &lt;code&gt;TopicArn&lt;/code&gt; parameters.&lt;/p&gt;
    :type phone_number: str
    :param subject: &lt;p&gt;Optional parameter to be used as the \&quot;Subject\&quot; line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.&lt;/p&gt; &lt;p&gt;Constraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long.&lt;/p&gt;
    :type subject: str
    :param message_structure: &lt;p&gt;Set &lt;code&gt;MessageStructure&lt;/code&gt; to &lt;code&gt;json&lt;/code&gt; if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set &lt;code&gt;MessageStructure&lt;/code&gt; to &lt;code&gt;json&lt;/code&gt;, the value of the &lt;code&gt;Message&lt;/code&gt; parameter must: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;be a syntactically valid JSON object; and&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;contain at least a top-level JSON key of \&quot;default\&quot; with a value that is a string.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., \&quot;http\&quot;).&lt;/p&gt; &lt;p&gt;Valid value: &lt;code&gt;json&lt;/code&gt; &lt;/p&gt;
    :type message_structure: str
    :param message_attributes: Message attributes for Publish action.
    :type message_attributes: dict | bytes
    :param message_deduplication_id: &lt;p&gt;This parameter applies only to FIFO (first-in-first-out) topics. The &lt;code&gt;MessageDeduplicationId&lt;/code&gt; can contain up to 128 alphanumeric characters &lt;code&gt;(a-z, A-Z, 0-9)&lt;/code&gt; and punctuation &lt;code&gt;(!\&quot;#$%&amp;amp;&#39;()*+,-./:;&amp;lt;&#x3D;&amp;gt;?@[\\]^_&#x60;{|}~)&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Every message must have a unique &lt;code&gt;MessageDeduplicationId&lt;/code&gt;, which is a token used for deduplication of sent messages. If a message with a particular &lt;code&gt;MessageDeduplicationId&lt;/code&gt; is sent successfully, any message sent with the same &lt;code&gt;MessageDeduplicationId&lt;/code&gt; during the 5-minute deduplication interval is treated as a duplicate. &lt;/p&gt; &lt;p&gt;If the topic has &lt;code&gt;ContentBasedDeduplication&lt;/code&gt; set, the system generates a &lt;code&gt;MessageDeduplicationId&lt;/code&gt; based on the contents of the message. Your &lt;code&gt;MessageDeduplicationId&lt;/code&gt; overrides the generated one.&lt;/p&gt;
    :type message_deduplication_id: str
    :param message_group_id: &lt;p&gt;This parameter applies only to FIFO (first-in-first-out) topics. The &lt;code&gt;MessageGroupId&lt;/code&gt; can contain up to 128 alphanumeric characters &lt;code&gt;(a-z, A-Z, 0-9)&lt;/code&gt; and punctuation &lt;code&gt;(!\&quot;#$%&amp;amp;&#39;()*+,-./:;&amp;lt;&#x3D;&amp;gt;?@[\\]^_&#x60;{|}~)&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;MessageGroupId&lt;/code&gt; is a tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). Every message must include a &lt;code&gt;MessageGroupId&lt;/code&gt;.&lt;/p&gt;
    :type message_group_id: str

    """
    message_attributes = {k: MessageAttributeValue.from_dict(v) for k, v in message_attributes}
    return web.Response(status=200)


async def g_et_publish_batch(request: web.Request, topic_arn, publish_batch_request_entries, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_publish_batch

    &lt;p&gt;Publishes up to ten messages to the specified topic. This is a batch version of &lt;code&gt;Publish&lt;/code&gt;. For FIFO topics, multiple messages within a single batch are published in the order they are sent, and messages are deduplicated within the batch and across batches for 5 minutes.&lt;/p&gt; &lt;p&gt;The result of publishing each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of &lt;code&gt;200&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KB (262,144 bytes). &lt;/p&gt; &lt;p&gt;Some actions take lists of parameters. These lists are specified using the &lt;code&gt;param.n&lt;/code&gt; notation. Values of &lt;code&gt;n&lt;/code&gt; are integers starting from 1. For example, a parameter list with two elements looks like this: &lt;/p&gt; &lt;p&gt;&amp;amp;AttributeName.1&#x3D;first&lt;/p&gt; &lt;p&gt;&amp;amp;AttributeName.2&#x3D;second&lt;/p&gt; &lt;p&gt;If you send a batch message to a topic, Amazon SNS publishes the batch message to each endpoint that is subscribed to the topic. The format of the batch message depends on the notification protocol for each subscribed endpoint.&lt;/p&gt; &lt;p&gt;When a &lt;code&gt;messageId&lt;/code&gt; is returned, the batch message is saved and Amazon SNS immediately delivers the message to subscribers.&lt;/p&gt;

    :param topic_arn: The Amazon resource name (ARN) of the topic you want to batch publish to.
    :type topic_arn: str
    :param publish_batch_request_entries: A list of &lt;code&gt;PublishBatch&lt;/code&gt; request entries to be sent to the SNS topic.
    :type publish_batch_request_entries: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    publish_batch_request_entries = [PublishBatchRequestEntry.from_dict(d) for d in publish_batch_request_entries]
    return web.Response(status=200)


async def g_et_put_data_protection_policy(request: web.Request, resource_arn, data_protection_policy, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_put_data_protection_policy

    Adds or updates an inline policy document that is stored in the specified Amazon SNS topic.

    :param resource_arn: &lt;p&gt;The ARN of the topic whose &lt;code&gt;DataProtectionPolicy&lt;/code&gt; you want to add or update.&lt;/p&gt; &lt;p&gt;For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the Amazon Web Services General Reference.&lt;/p&gt;
    :type resource_arn: str
    :param data_protection_policy: &lt;p&gt;The JSON serialization of the topic&#39;s &lt;code&gt;DataProtectionPolicy&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DataProtectionPolicy&lt;/code&gt; must be in JSON string format.&lt;/p&gt; &lt;p&gt;Length Constraints: Maximum length of 30,720.&lt;/p&gt;
    :type data_protection_policy: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_remove_permission(request: web.Request, topic_arn, label, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_permission

    &lt;p&gt;Removes a statement from a topic&#39;s access control policy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To remove the ability to change topic permissions, you must deny permissions to the &lt;code&gt;AddPermission&lt;/code&gt;, &lt;code&gt;RemovePermission&lt;/code&gt;, and &lt;code&gt;SetTopicAttributes&lt;/code&gt; actions in your IAM policy.&lt;/p&gt; &lt;/note&gt;

    :param topic_arn: The ARN of the topic whose access control policy you wish to modify.
    :type topic_arn: str
    :param label: The unique label of the statement you want to remove.
    :type label: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_set_endpoint_attributes(request: web.Request, endpoint_arn, attributes, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_endpoint_attributes

    Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param endpoint_arn: EndpointArn used for SetEndpointAttributes action.
    :type endpoint_arn: str
    :param attributes: &lt;p&gt;A map of the endpoint attributes. Attributes in this map include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CustomUserData&lt;/code&gt; – arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Enabled&lt;/code&gt; – flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Token&lt;/code&gt; – device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type attributes: Dict[str, str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_set_platform_application_attributes(request: web.Request, platform_application_arn, attributes, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_platform_application_attributes

    Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. For information on configuring attributes for message delivery status, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html\&quot;&gt;Using Amazon SNS Application Attributes for Message Delivery Status&lt;/a&gt;. 

    :param platform_application_arn: PlatformApplicationArn for SetPlatformApplicationAttributes action.
    :type platform_application_arn: str
    :param attributes: &lt;p&gt;A map of the platform application attributes. Attributes in this map include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PlatformCredential&lt;/code&gt; – The credential received from the notification service.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For ADM, &lt;code&gt;PlatformCredential&lt;/code&gt;is client secret.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Apple Services using certificate credentials, &lt;code&gt;PlatformCredential&lt;/code&gt; is private key.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Apple Services using token credentials, &lt;code&gt;PlatformCredential&lt;/code&gt; is signing key.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For GCM (Firebase Cloud Messaging), &lt;code&gt;PlatformCredential&lt;/code&gt; is API key. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PlatformPrincipal&lt;/code&gt; – The principal received from the notification service.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For ADM, &lt;code&gt;PlatformPrincipal&lt;/code&gt;is client id.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Apple Services using certificate credentials, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is SSL certificate.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Apple Services using token credentials, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is signing key ID.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For GCM (Firebase Cloud Messaging), there is no &lt;code&gt;PlatformPrincipal&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EventEndpointCreated&lt;/code&gt; – Topic ARN to which &lt;code&gt;EndpointCreated&lt;/code&gt; event notifications are sent.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EventEndpointDeleted&lt;/code&gt; – Topic ARN to which &lt;code&gt;EndpointDeleted&lt;/code&gt; event notifications are sent.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EventEndpointUpdated&lt;/code&gt; – Topic ARN to which &lt;code&gt;EndpointUpdate&lt;/code&gt; event notifications are sent.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EventDeliveryFailure&lt;/code&gt; – Topic ARN to which &lt;code&gt;DeliveryFailure&lt;/code&gt; event notifications are sent upon Direct Publish delivery failure (permanent) to one of the application&#39;s endpoints.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SuccessFeedbackRoleArn&lt;/code&gt; – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FailureFeedbackRoleArn&lt;/code&gt; – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SuccessFeedbackSampleRate&lt;/code&gt; – Sample rate percentage (0-100) of successfully delivered messages.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following attributes only apply to &lt;code&gt;APNs&lt;/code&gt; token-based authentication:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ApplePlatformTeamID&lt;/code&gt; – The identifier that&#39;s assigned to your Apple developer account team.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ApplePlatformBundleID&lt;/code&gt; – The bundle identifier that&#39;s assigned to your iOS app.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type attributes: Dict[str, str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_set_sms_attributes(request: web.Request, attributes, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_sms_attributes

    &lt;p&gt;Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.&lt;/p&gt; &lt;p&gt;You can override some of these settings for a single message when you use the &lt;code&gt;Publish&lt;/code&gt; action with the &lt;code&gt;MessageAttributes.entry.N&lt;/code&gt; parameter. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html\&quot;&gt;Publishing to a mobile phone&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this operation, you must grant the Amazon SNS service principal (&lt;code&gt;sns.amazonaws.com&lt;/code&gt;) permission to perform the &lt;code&gt;s3:ListBucket&lt;/code&gt; action. &lt;/p&gt; &lt;/note&gt;

    :param attributes: &lt;p&gt;The default settings for sending SMS messages from your Amazon Web Services account. You can set values for the following attribute names:&lt;/p&gt; &lt;p&gt; &lt;code&gt;MonthlySpendLimit&lt;/code&gt; – The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;service-limit-increase&amp;amp;limitType&#x3D;service-code-sns\&quot;&gt;SNS Limit Increase case&lt;/a&gt;. For &lt;b&gt;New limit value&lt;/b&gt;, enter your desired monthly spend limit. In the &lt;b&gt;Use Case Description&lt;/b&gt; field, explain that you are requesting an SMS monthly spend limit increase.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DeliveryStatusIAMRole&lt;/code&gt; – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DeliveryStatusSuccessSamplingRate&lt;/code&gt; – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to &lt;code&gt;0&lt;/code&gt;. To write logs for 10% of your successful deliveries, set it to &lt;code&gt;10&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DefaultSenderID&lt;/code&gt; – A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter.&lt;/p&gt; &lt;p&gt; &lt;code&gt;DefaultSMSType&lt;/code&gt; – The type of SMS message that you will send by default. You can assign the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Promotional&lt;/code&gt; – (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Transactional&lt;/code&gt; – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;code&gt;UsageReportS3Bucket&lt;/code&gt; – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your Amazon Web Services account:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Time that the message was published (in UTC)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Message ID&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Destination phone number&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Message type&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Delivery status&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Message price (in USD)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Part number (a message is split into multiple parts if it is too long for a single message)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Total number of parts&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To receive the report, the bucket must have a policy that allows the Amazon SNS service principal to perform the &lt;code&gt;s3:PutObject&lt;/code&gt; and &lt;code&gt;s3:GetBucketLocation&lt;/code&gt; actions.&lt;/p&gt; &lt;p&gt;For an example bucket policy and usage report, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sms_stats.html\&quot;&gt;Monitoring SMS Activity&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;
    :type attributes: Dict[str, str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_set_subscription_attributes(request: web.Request, subscription_arn, attribute_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, attribute_value=None) -> web.Response:
    """g_et_set_subscription_attributes

    Allows a subscription owner to set an attribute of the subscription to a new value.

    :param subscription_arn: The ARN of the subscription to modify.
    :type subscription_arn: str
    :param attribute_name: &lt;p&gt;A map of attributes with their corresponding values.&lt;/p&gt; &lt;p&gt;The following lists the names, descriptions, and values of the special request parameters that this action uses:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeliveryPolicy&lt;/code&gt; – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FilterPolicy&lt;/code&gt; – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FilterPolicyScope&lt;/code&gt; – This attribute lets you choose the filtering scope by using one of the following string value types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MessageAttributes&lt;/code&gt; (default) – The filter is applied on the message attributes.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MessageBody&lt;/code&gt; – The filter is applied on the message body.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RawMessageDelivery&lt;/code&gt; – When set to &lt;code&gt;true&lt;/code&gt;, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RedrivePolicy&lt;/code&gt; – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can&#39;t be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following attribute applies only to Amazon Kinesis Data Firehose delivery stream subscriptions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SubscriptionRoleArn&lt;/code&gt; – The ARN of the IAM role that has the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Permission to write to the Kinesis Data Firehose delivery stream&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon SNS listed as a trusted entity&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Specifying a valid ARN for this attribute is required for Kinesis Data Firehose delivery stream subscriptions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html\&quot;&gt;Fanout to Kinesis Data Firehose delivery streams&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param attribute_value: The new value for the attribute in JSON format.
    :type attribute_value: str

    """
    return web.Response(status=200)


async def g_et_set_topic_attributes(request: web.Request, topic_arn, attribute_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, attribute_value=None) -> web.Response:
    """g_et_set_topic_attributes

    &lt;p&gt;Allows a topic owner to set an attribute of the topic to a new value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To remove the ability to change topic permissions, you must deny permissions to the &lt;code&gt;AddPermission&lt;/code&gt;, &lt;code&gt;RemovePermission&lt;/code&gt;, and &lt;code&gt;SetTopicAttributes&lt;/code&gt; actions in your IAM policy.&lt;/p&gt; &lt;/note&gt;

    :param topic_arn: The ARN of the topic to modify.
    :type topic_arn: str
    :param attribute_name: &lt;p&gt;A map of attributes with their corresponding values.&lt;/p&gt; &lt;p&gt;The following lists the names, descriptions, and values of the special request parameters that the &lt;code&gt;SetTopicAttributes&lt;/code&gt; action uses:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ApplicationSuccessFeedbackRoleArn&lt;/code&gt; – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to a platform application endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeliveryPolicy&lt;/code&gt; – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DisplayName&lt;/code&gt; – The display name to use for a topic with SMS subscriptions.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Policy&lt;/code&gt; – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TracingConfig&lt;/code&gt; – Tracing mode of an Amazon SNS topic. By default &lt;code&gt;TracingConfig&lt;/code&gt; is set to &lt;code&gt;PassThrough&lt;/code&gt;, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to &lt;code&gt;Active&lt;/code&gt;, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;HTTP&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTPSuccessFeedbackRoleArn&lt;/code&gt; – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTPSuccessFeedbackSampleRate&lt;/code&gt; – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an HTTP endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTPFailureFeedbackRoleArn&lt;/code&gt; – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Kinesis Data Firehose&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FirehoseSuccessFeedbackRoleArn&lt;/code&gt; – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FirehoseSuccessFeedbackSampleRate&lt;/code&gt; – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FirehoseFailureFeedbackRoleArn&lt;/code&gt; – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Kinesis Data Firehose endpoint. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lambda&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LambdaSuccessFeedbackRoleArn&lt;/code&gt; – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LambdaSuccessFeedbackSampleRate&lt;/code&gt; – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Lambda endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LambdaFailureFeedbackRoleArn&lt;/code&gt; – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Platform application endpoint&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ApplicationSuccessFeedbackRoleArn&lt;/code&gt; – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Web Services application endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ApplicationSuccessFeedbackSampleRate&lt;/code&gt; – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon Web Services application endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ApplicationFailureFeedbackRoleArn&lt;/code&gt; – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Web Services application endpoint.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;In addition to being able to configure topic attributes for message delivery status of notification messages sent to Amazon SNS application endpoints, you can also configure application attributes for the delivery status of push notification messages sent to push notification services.&lt;/p&gt; &lt;p&gt;For example, For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html\&quot;&gt;Using Amazon SNS Application Attributes for Message Delivery Status&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon SQS&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SQSSuccessFeedbackRoleArn&lt;/code&gt; – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SQSSuccessFeedbackSampleRate&lt;/code&gt; – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SQSFailureFeedbackRoleArn&lt;/code&gt; – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &amp;lt;ENDPOINT&amp;gt;SuccessFeedbackRoleArn and &amp;lt;ENDPOINT&amp;gt;FailureFeedbackRoleArn attributes are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The &amp;lt;ENDPOINT&amp;gt;SuccessFeedbackSampleRate attribute is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the &amp;lt;ENDPOINT&amp;gt;FailureFeedbackRoleArn attribute, then all failed message deliveries generate CloudWatch Logs. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;The following attribute applies only to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html\&quot;&gt;server-side-encryption&lt;/a&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;KmsMasterKeyId&lt;/code&gt; – The ID of an Amazon Web Services managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms\&quot;&gt;Key Terms&lt;/a&gt;. For more examples, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters\&quot;&gt;KeyId&lt;/a&gt; in the &lt;i&gt;Key Management Service API Reference&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SignatureVersion&lt;/code&gt; – The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, &lt;code&gt;SignatureVersion&lt;/code&gt; is set to &lt;code&gt;1&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following attribute applies only to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html\&quot;&gt;FIFO topics&lt;/a&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ContentBasedDeduplication&lt;/code&gt; – Enables content-based deduplication for FIFO topics.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;By default, &lt;code&gt;ContentBasedDeduplication&lt;/code&gt; is set to &lt;code&gt;false&lt;/code&gt;. If you create a FIFO topic and this attribute is &lt;code&gt;false&lt;/code&gt;, you must specify a value for the &lt;code&gt;MessageDeduplicationId&lt;/code&gt; parameter for the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/api/API_Publish.html\&quot;&gt;Publish&lt;/a&gt; action. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you set &lt;code&gt;ContentBasedDeduplication&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt;, Amazon SNS uses a SHA-256 hash to generate the &lt;code&gt;MessageDeduplicationId&lt;/code&gt; using the body of the message (but not the attributes of the message).&lt;/p&gt; &lt;p&gt;(Optional) To override the generated value, you can specify a value for the &lt;code&gt;MessageDeduplicationId&lt;/code&gt; parameter for the &lt;code&gt;Publish&lt;/code&gt; action.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;
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
    :param attribute_value: The new value for the attribute.
    :type attribute_value: str

    """
    return web.Response(status=200)


async def g_et_subscribe(request: web.Request, topic_arn, protocol, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, endpoint=None, attributes=None, return_subscription_arn=None) -> web.Response:
    """g_et_subscribe

    &lt;p&gt;Subscribes an endpoint to an Amazon SNS topic. If the endpoint type is HTTP/S or email, or if the endpoint and the topic are not in the same Amazon Web Services account, the endpoint owner must run the &lt;code&gt;ConfirmSubscription&lt;/code&gt; action to confirm the subscription.&lt;/p&gt; &lt;p&gt;You call the &lt;code&gt;ConfirmSubscription&lt;/code&gt; action with the token from the subscription response. Confirmation tokens are valid for three days.&lt;/p&gt; &lt;p&gt;This action is throttled at 100 transactions per second (TPS).&lt;/p&gt;

    :param topic_arn: The ARN of the topic you want to subscribe to.
    :type topic_arn: str
    :param protocol: &lt;p&gt;The protocol that you want to use. Supported protocols include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;http&lt;/code&gt; – delivery of JSON-encoded message via HTTP POST&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;https&lt;/code&gt; – delivery of JSON-encoded message via HTTPS POST&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;email&lt;/code&gt; – delivery of message via SMTP&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;email-json&lt;/code&gt; – delivery of JSON-encoded message via SMTP&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sms&lt;/code&gt; – delivery of message via SMS&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;sqs&lt;/code&gt; – delivery of JSON-encoded message to an Amazon SQS queue&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;application&lt;/code&gt; – delivery of JSON-encoded message to an EndpointArn for a mobile app and device&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;lambda&lt;/code&gt; – delivery of JSON-encoded message to an Lambda function&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;firehose&lt;/code&gt; – delivery of JSON-encoded message to an Amazon Kinesis Data Firehose delivery stream.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type protocol: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param endpoint: &lt;p&gt;The endpoint that you want to receive notifications. Endpoints vary by protocol:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;http&lt;/code&gt; protocol, the (public) endpoint is a URL beginning with &lt;code&gt;http://&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;https&lt;/code&gt; protocol, the (public) endpoint is a URL beginning with &lt;code&gt;https://&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;email&lt;/code&gt; protocol, the endpoint is an email address.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;email-json&lt;/code&gt; protocol, the endpoint is an email address.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;sms&lt;/code&gt; protocol, the endpoint is a phone number of an SMS-enabled device.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;sqs&lt;/code&gt; protocol, the endpoint is the ARN of an Amazon SQS queue.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;application&lt;/code&gt; protocol, the endpoint is the EndpointArn of a mobile app and device.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;lambda&lt;/code&gt; protocol, the endpoint is the ARN of an Lambda function.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For the &lt;code&gt;firehose&lt;/code&gt; protocol, the endpoint is the ARN of an Amazon Kinesis Data Firehose delivery stream.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type endpoint: str
    :param attributes: &lt;p&gt;A map of attributes with their corresponding values.&lt;/p&gt; &lt;p&gt;The following lists the names, descriptions, and values of the special request parameters that the &lt;code&gt;Subscribe&lt;/code&gt; action uses:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeliveryPolicy&lt;/code&gt; – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FilterPolicy&lt;/code&gt; – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FilterPolicyScope&lt;/code&gt; – This attribute lets you choose the filtering scope by using one of the following string value types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MessageAttributes&lt;/code&gt; (default) – The filter is applied on the message attributes.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MessageBody&lt;/code&gt; – The filter is applied on the message body.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RawMessageDelivery&lt;/code&gt; – When set to &lt;code&gt;true&lt;/code&gt;, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RedrivePolicy&lt;/code&gt; – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can&#39;t be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following attribute applies only to Amazon Kinesis Data Firehose delivery stream subscriptions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SubscriptionRoleArn&lt;/code&gt; – The ARN of the IAM role that has the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Permission to write to the Kinesis Data Firehose delivery stream&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon SNS listed as a trusted entity&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Specifying a valid ARN for this attribute is required for Kinesis Data Firehose delivery stream subscriptions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html\&quot;&gt;Fanout to Kinesis Data Firehose delivery streams&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type attributes: Dict[str, str]
    :param return_subscription_arn: &lt;p&gt;Sets whether the response from the &lt;code&gt;Subscribe&lt;/code&gt; request includes the subscription ARN, even if the subscription is not yet confirmed.&lt;/p&gt; &lt;p&gt;If you set this parameter to &lt;code&gt;true&lt;/code&gt;, the response includes the ARN in all cases, even if the subscription is not yet confirmed. In addition to the ARN for confirmed subscriptions, the response also includes the &lt;code&gt;pending subscription&lt;/code&gt; ARN value for subscriptions that aren&#39;t yet confirmed. A subscription becomes confirmed when the subscriber calls the &lt;code&gt;ConfirmSubscription&lt;/code&gt; action with a confirmation token.&lt;/p&gt; &lt;p/&gt; &lt;p&gt;The default value is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt;
    :type return_subscription_arn: bool

    """
    return web.Response(status=200)


async def g_et_tag_resource(request: web.Request, resource_arn, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_tag_resource

    &lt;p&gt;Add tags to the specified Amazon SNS topic. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html\&quot;&gt;Amazon SNS Tags&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When you use topic tags, keep the following guidelines in mind:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Adding more than 50 tags to a topic isn&#39;t recommended.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning. Amazon SNS interprets tags as character strings.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tags are case-sensitive.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A new tag with a key identical to that of an existing tag overwrites the existing tag.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tagging actions are limited to 10 TPS per Amazon Web Services account, per Amazon Web Services Region. If your application requires a higher throughput, file a &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;technical\&quot;&gt;technical support request&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param resource_arn: The ARN of the topic to which to add tags.
    :type resource_arn: str
    :param tags: The tags to be added to the specified topic. A tag consists of a required key and an optional value.
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


async def g_et_unsubscribe(request: web.Request, subscription_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_unsubscribe

    &lt;p&gt;Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic&#39;s owner can unsubscribe, and an Amazon Web Services signature is required. If the &lt;code&gt;Unsubscribe&lt;/code&gt; call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the &lt;code&gt;Unsubscribe&lt;/code&gt; request was unintended.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon SQS queue subscriptions require authentication for deletion. Only the owner of the subscription, or the owner of the topic can unsubscribe using the required Amazon Web Services signature.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This action is throttled at 100 transactions per second (TPS).&lt;/p&gt;

    :param subscription_arn: The ARN of the subscription to be deleted.
    :type subscription_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_untag_resource(request: web.Request, resource_arn, tag_keys, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_untag_resource

    Remove tags from the specified Amazon SNS topic. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html\&quot;&gt;Amazon SNS Tags&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.

    :param resource_arn: The ARN of the topic from which to remove tags.
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the specified topic.
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


async def g_et_verify_sms_sandbox_phone_number(request: web.Request, phone_number, one_time_password, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_verify_sms_sandbox_phone_number

    &lt;p&gt;Verifies a destination phone number with a one-time password (OTP) for the calling Amazon Web Services account.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param phone_number: The destination phone number to verify.
    :type phone_number: str
    :param one_time_password: The OTP sent to the destination number from the &lt;code&gt;CreateSMSSandBoxPhoneNumber&lt;/code&gt; call.
    :type one_time_password: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_add_permission(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_permission

    &lt;p&gt;Adds a statement to a topic&#39;s access control policy, granting access for the specified Amazon Web Services accounts to the specified actions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To remove the ability to change topic permissions, you must deny permissions to the &lt;code&gt;AddPermission&lt;/code&gt;, &lt;code&gt;RemovePermission&lt;/code&gt;, and &lt;code&gt;SetTopicAttributes&lt;/code&gt; actions in your IAM policy.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = AddPermissionInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_check_if_phone_number_is_opted_out(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_check_if_phone_number_is_opted_out

    &lt;p&gt;Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your Amazon Web Services account. You cannot send SMS messages to a number that is opted out.&lt;/p&gt; &lt;p&gt;To resume sending messages, you can opt in the number by using the &lt;code&gt;OptInPhoneNumber&lt;/code&gt; action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CheckIfPhoneNumberIsOptedOutInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_confirm_subscription(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_confirm_subscription

    Verifies an endpoint owner&#39;s intent to receive messages by validating the token sent to the endpoint by an earlier &lt;code&gt;Subscribe&lt;/code&gt; action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the &lt;code&gt;AuthenticateOnUnsubscribe&lt;/code&gt; flag is set to \&quot;true\&quot;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ConfirmSubscriptionInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_platform_application(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_platform_application

    &lt;p&gt;Creates a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging), to which devices and mobile apps may register. You must specify &lt;code&gt;PlatformPrincipal&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; attributes when using the &lt;code&gt;CreatePlatformApplication&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PlatformPrincipal&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; are received from the notification service.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;ADM&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;client id&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;client secret&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;Baidu&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;API key&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;secret key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;APNS&lt;/code&gt; and &lt;code&gt;APNS_SANDBOX&lt;/code&gt; using certificate credentials, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;SSL certificate&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;private key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;APNS&lt;/code&gt; and &lt;code&gt;APNS_SANDBOX&lt;/code&gt; using token credentials, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;signing key ID&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;signing key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;GCM&lt;/code&gt; (Firebase Cloud Messaging), there is no &lt;code&gt;PlatformPrincipal&lt;/code&gt; and the &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;API key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;MPNS&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;TLS certificate&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;private key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;WNS&lt;/code&gt;, &lt;code&gt;PlatformPrincipal&lt;/code&gt; is &lt;code&gt;Package Security Identifier&lt;/code&gt; and &lt;code&gt;PlatformCredential&lt;/code&gt; is &lt;code&gt;secret key&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can use the returned &lt;code&gt;PlatformApplicationArn&lt;/code&gt; as an attribute for the &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreatePlatformApplicationInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_platform_endpoint(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_platform_endpoint

    &lt;p&gt;Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; requires the &lt;code&gt;PlatformApplicationArn&lt;/code&gt; that is returned from &lt;code&gt;CreatePlatformApplication&lt;/code&gt;. You can use the returned &lt;code&gt;EndpointArn&lt;/code&gt; to send a message to a mobile app or by the &lt;code&gt;Subscribe&lt;/code&gt; action for subscription to a topic. The &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint&#39;s ARN is returned without creating a new endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;When using &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePushBaiduEndpoint.html\&quot;&gt;Creating an Amazon SNS Endpoint for Baidu&lt;/a&gt;. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreatePlatformEndpointInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_sms_sandbox_phone_number(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_sms_sandbox_phone_number

    &lt;p&gt;Adds a destination phone number to an Amazon Web Services account in the SMS sandbox and sends a one-time password (OTP) to that phone number.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateSMSSandboxPhoneNumberInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_topic(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_topic

    Creates a topic to which notifications can be published. Users can create at most 100,000 standard topics (at most 1,000 FIFO topics). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html\&quot;&gt;Creating an Amazon SNS topic&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;. This action is idempotent, so if the requester already owns a topic with the specified name, that topic&#39;s ARN is returned without creating a new topic.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateTopicInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_endpoint(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_endpoint

    &lt;p&gt;Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteEndpointInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_platform_application(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_platform_application

    Deletes a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeletePlatformApplicationInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_sms_sandbox_phone_number(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_sms_sandbox_phone_number

    &lt;p&gt;Deletes an Amazon Web Services account&#39;s verified or pending phone number from the SMS sandbox.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteSMSSandboxPhoneNumberInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_topic(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_topic

    Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteTopicInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_data_protection_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_data_protection_policy

    Retrieves the specified inline &lt;code&gt;DataProtectionPolicy&lt;/code&gt; document that is stored in the specified Amazon SNS topic. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetDataProtectionPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_endpoint_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_endpoint_attributes

    Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetEndpointAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_platform_application_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_platform_application_attributes

    Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetPlatformApplicationAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_sms_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_sms_attributes

    &lt;p&gt;Returns the settings for sending SMS messages from your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;These settings are set with the &lt;code&gt;SetSMSAttributes&lt;/code&gt; action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetSMSAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_sms_sandbox_account_status(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_sms_sandbox_account_status

    &lt;p&gt;Retrieves the SMS sandbox status for the calling Amazon Web Services account in the target Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :type body: 

    """
    return web.Response(status=200)


async def p_ost_get_subscription_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_subscription_attributes

    Returns all of the properties of a subscription.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetSubscriptionAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_topic_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_topic_attributes

    Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetTopicAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_endpoints_by_platform_application(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_endpoints_by_platform_application

    &lt;p&gt;Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM (Firebase Cloud Messaging) and APNS. The results for &lt;code&gt;ListEndpointsByPlatformApplication&lt;/code&gt; are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call &lt;code&gt;ListEndpointsByPlatformApplication&lt;/code&gt; again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListEndpointsByPlatformApplicationInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_origination_numbers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_origination_numbers

    Lists the calling Amazon Web Services account&#39;s dedicated origination numbers and their metadata. For more information about origination numbers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/channels-sms-originating-identities-origination-numbers.html\&quot;&gt;Origination numbers&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListOriginationNumbersRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_phone_numbers_opted_out(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_phone_numbers_opted_out

    &lt;p&gt;Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them.&lt;/p&gt; &lt;p&gt;The results for &lt;code&gt;ListPhoneNumbersOptedOut&lt;/code&gt; are paginated, and each page returns up to 100 phone numbers. If additional phone numbers are available after the first page of results, then a &lt;code&gt;NextToken&lt;/code&gt; string will be returned. To receive the next page, you call &lt;code&gt;ListPhoneNumbersOptedOut&lt;/code&gt; again using the &lt;code&gt;NextToken&lt;/code&gt; string received from the previous call. When there are no more records to return, &lt;code&gt;NextToken&lt;/code&gt; will be null.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListPhoneNumbersOptedOutInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_platform_applications(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_platform_applications

    &lt;p&gt;Lists the platform application objects for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). The results for &lt;code&gt;ListPlatformApplications&lt;/code&gt; are paginated and return a limited list of applications, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call &lt;code&gt;ListPlatformApplications&lt;/code&gt; using the NextToken string received from the previous call. When there are no more records to return, &lt;code&gt;NextToken&lt;/code&gt; will be null. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This action is throttled at 15 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListPlatformApplicationsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_sms_sandbox_phone_numbers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_sms_sandbox_phone_numbers

    &lt;p&gt;Lists the calling Amazon Web Services account&#39;s current verified and pending destination phone numbers in the SMS sandbox.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListSMSSandboxPhoneNumbersInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_subscriptions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_subscriptions

    &lt;p&gt;Returns a list of the requester&#39;s subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a &lt;code&gt;NextToken&lt;/code&gt; is also returned. Use the &lt;code&gt;NextToken&lt;/code&gt; parameter in a new &lt;code&gt;ListSubscriptions&lt;/code&gt; call to get further results.&lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListSubscriptionsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_subscriptions_by_topic(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_subscriptions_by_topic

    &lt;p&gt;Returns a list of the subscriptions to a specific topic. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a &lt;code&gt;NextToken&lt;/code&gt; is also returned. Use the &lt;code&gt;NextToken&lt;/code&gt; parameter in a new &lt;code&gt;ListSubscriptionsByTopic&lt;/code&gt; call to get further results.&lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListSubscriptionsByTopicInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_tags_for_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_tags_for_resource

    List all tags added to the specified Amazon SNS topic. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html\&quot;&gt;Amazon SNS Tags&lt;/a&gt; in the &lt;i&gt;Amazon Simple Notification Service Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_topics(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_topics

    &lt;p&gt;Returns a list of the requester&#39;s topics. Each call returns a limited list of topics, up to 100. If there are more topics, a &lt;code&gt;NextToken&lt;/code&gt; is also returned. Use the &lt;code&gt;NextToken&lt;/code&gt; parameter in a new &lt;code&gt;ListTopics&lt;/code&gt; call to get further results.&lt;/p&gt; &lt;p&gt;This action is throttled at 30 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListTopicsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_opt_in_phone_number(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_opt_in_phone_number

    &lt;p&gt;Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number.&lt;/p&gt; &lt;p&gt;You can opt in a phone number only once every 30 days.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = OptInPhoneNumberInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_publish(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_publish

    &lt;p&gt;Sends a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify the &lt;code&gt;TargetArn&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.&lt;/p&gt; &lt;p&gt;When a &lt;code&gt;messageId&lt;/code&gt; is returned, the message is saved and Amazon SNS immediately delivers it to subscribers.&lt;/p&gt; &lt;p&gt;To use the &lt;code&gt;Publish&lt;/code&gt; action for publishing a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the &lt;code&gt;CreatePlatformEndpoint&lt;/code&gt; action. &lt;/p&gt; &lt;p&gt;For more information about formatting messages, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html\&quot;&gt;Send Custom Platform-Specific Payloads in Messages to Mobile Devices&lt;/a&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can publish messages only to topics and endpoints in the same Amazon Web Services Region.&lt;/p&gt; &lt;/important&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PublishInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_publish_batch(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_publish_batch

    &lt;p&gt;Publishes up to ten messages to the specified topic. This is a batch version of &lt;code&gt;Publish&lt;/code&gt;. For FIFO topics, multiple messages within a single batch are published in the order they are sent, and messages are deduplicated within the batch and across batches for 5 minutes.&lt;/p&gt; &lt;p&gt;The result of publishing each message is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of &lt;code&gt;200&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The maximum allowed individual message size and the maximum total payload size (the sum of the individual lengths of all of the batched messages) are both 256 KB (262,144 bytes). &lt;/p&gt; &lt;p&gt;Some actions take lists of parameters. These lists are specified using the &lt;code&gt;param.n&lt;/code&gt; notation. Values of &lt;code&gt;n&lt;/code&gt; are integers starting from 1. For example, a parameter list with two elements looks like this: &lt;/p&gt; &lt;p&gt;&amp;amp;AttributeName.1&#x3D;first&lt;/p&gt; &lt;p&gt;&amp;amp;AttributeName.2&#x3D;second&lt;/p&gt; &lt;p&gt;If you send a batch message to a topic, Amazon SNS publishes the batch message to each endpoint that is subscribed to the topic. The format of the batch message depends on the notification protocol for each subscribed endpoint.&lt;/p&gt; &lt;p&gt;When a &lt;code&gt;messageId&lt;/code&gt; is returned, the batch message is saved and Amazon SNS immediately delivers the message to subscribers.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PublishBatchInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_data_protection_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_data_protection_policy

    Adds or updates an inline policy document that is stored in the specified Amazon SNS topic.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutDataProtectionPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_permission(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_permission

    &lt;p&gt;Removes a statement from a topic&#39;s access control policy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To remove the ability to change topic permissions, you must deny permissions to the &lt;code&gt;AddPermission&lt;/code&gt;, &lt;code&gt;RemovePermission&lt;/code&gt;, and &lt;code&gt;SetTopicAttributes&lt;/code&gt; actions in your IAM policy.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = RemovePermissionInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_endpoint_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_endpoint_attributes

    Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetEndpointAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_platform_application_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_platform_application_attributes

    Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html\&quot;&gt;Using Amazon SNS Mobile Push Notifications&lt;/a&gt;. For information on configuring attributes for message delivery status, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html\&quot;&gt;Using Amazon SNS Application Attributes for Message Delivery Status&lt;/a&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetPlatformApplicationAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_sms_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_sms_attributes

    &lt;p&gt;Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.&lt;/p&gt; &lt;p&gt;You can override some of these settings for a single message when you use the &lt;code&gt;Publish&lt;/code&gt; action with the &lt;code&gt;MessageAttributes.entry.N&lt;/code&gt; parameter. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html\&quot;&gt;Publishing to a mobile phone&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To use this operation, you must grant the Amazon SNS service principal (&lt;code&gt;sns.amazonaws.com&lt;/code&gt;) permission to perform the &lt;code&gt;s3:ListBucket&lt;/code&gt; action. &lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetSMSAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_subscription_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_subscription_attributes

    Allows a subscription owner to set an attribute of the subscription to a new value.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetSubscriptionAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_topic_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_topic_attributes

    &lt;p&gt;Allows a topic owner to set an attribute of the topic to a new value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To remove the ability to change topic permissions, you must deny permissions to the &lt;code&gt;AddPermission&lt;/code&gt;, &lt;code&gt;RemovePermission&lt;/code&gt;, and &lt;code&gt;SetTopicAttributes&lt;/code&gt; actions in your IAM policy.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetTopicAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_subscribe(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_subscribe

    &lt;p&gt;Subscribes an endpoint to an Amazon SNS topic. If the endpoint type is HTTP/S or email, or if the endpoint and the topic are not in the same Amazon Web Services account, the endpoint owner must run the &lt;code&gt;ConfirmSubscription&lt;/code&gt; action to confirm the subscription.&lt;/p&gt; &lt;p&gt;You call the &lt;code&gt;ConfirmSubscription&lt;/code&gt; action with the token from the subscription response. Confirmation tokens are valid for three days.&lt;/p&gt; &lt;p&gt;This action is throttled at 100 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SubscribeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_tag_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_tag_resource

    &lt;p&gt;Add tags to the specified Amazon SNS topic. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html\&quot;&gt;Amazon SNS Tags&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When you use topic tags, keep the following guidelines in mind:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Adding more than 50 tags to a topic isn&#39;t recommended.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning. Amazon SNS interprets tags as character strings.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tags are case-sensitive.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A new tag with a key identical to that of an existing tag overwrites the existing tag.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tagging actions are limited to 10 TPS per Amazon Web Services account, per Amazon Web Services Region. If your application requires a higher throughput, file a &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;technical\&quot;&gt;technical support request&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_unsubscribe(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_unsubscribe

    &lt;p&gt;Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic&#39;s owner can unsubscribe, and an Amazon Web Services signature is required. If the &lt;code&gt;Unsubscribe&lt;/code&gt; call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the &lt;code&gt;Unsubscribe&lt;/code&gt; request was unintended.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon SQS queue subscriptions require authentication for deletion. Only the owner of the subscription, or the owner of the topic can unsubscribe using the required Amazon Web Services signature.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This action is throttled at 100 transactions per second (TPS).&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UnsubscribeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_untag_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_untag_resource

    Remove tags from the specified Amazon SNS topic. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html\&quot;&gt;Amazon SNS Tags&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_verify_sms_sandbox_phone_number(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_verify_sms_sandbox_phone_number

    &lt;p&gt;Verifies a destination phone number with a one-time password (OTP) for the calling Amazon Web Services account.&lt;/p&gt; &lt;p&gt;When you start using Amazon SNS to send SMS messages, your Amazon Web Services account is in the &lt;i&gt;SMS sandbox&lt;/i&gt;. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your Amazon Web Services account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html\&quot;&gt;SMS sandbox&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = VerifySMSSandboxPhoneNumberInput.from_dict(body)
    return web.Response(status=200)
