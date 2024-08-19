from typing import List, Dict
from aiohttp import web

from openapi_server.models.bounced_recipient_info import BouncedRecipientInfo
from openapi_server.models.bulk_email_destination import BulkEmailDestination
from openapi_server.models.clone_receipt_rule_set_request import CloneReceiptRuleSetRequest
from openapi_server.models.configuration_set_attribute import ConfigurationSetAttribute
from openapi_server.models.create_configuration_set_event_destination_request import CreateConfigurationSetEventDestinationRequest
from openapi_server.models.create_configuration_set_request import CreateConfigurationSetRequest
from openapi_server.models.create_configuration_set_tracking_options_request import CreateConfigurationSetTrackingOptionsRequest
from openapi_server.models.create_custom_verification_email_template_request import CreateCustomVerificationEmailTemplateRequest
from openapi_server.models.create_receipt_filter_request import CreateReceiptFilterRequest
from openapi_server.models.create_receipt_rule_request import CreateReceiptRuleRequest
from openapi_server.models.create_receipt_rule_set_request import CreateReceiptRuleSetRequest
from openapi_server.models.create_template_request import CreateTemplateRequest
from openapi_server.models.delete_configuration_set_event_destination_request import DeleteConfigurationSetEventDestinationRequest
from openapi_server.models.delete_configuration_set_request import DeleteConfigurationSetRequest
from openapi_server.models.delete_configuration_set_tracking_options_request import DeleteConfigurationSetTrackingOptionsRequest
from openapi_server.models.delete_custom_verification_email_template_request import DeleteCustomVerificationEmailTemplateRequest
from openapi_server.models.delete_identity_policy_request import DeleteIdentityPolicyRequest
from openapi_server.models.delete_identity_request import DeleteIdentityRequest
from openapi_server.models.delete_receipt_filter_request import DeleteReceiptFilterRequest
from openapi_server.models.delete_receipt_rule_request import DeleteReceiptRuleRequest
from openapi_server.models.delete_receipt_rule_set_request import DeleteReceiptRuleSetRequest
from openapi_server.models.delete_template_request import DeleteTemplateRequest
from openapi_server.models.delete_verified_email_address_request import DeleteVerifiedEmailAddressRequest
from openapi_server.models.describe_active_receipt_rule_set_response import DescribeActiveReceiptRuleSetResponse
from openapi_server.models.describe_configuration_set_request import DescribeConfigurationSetRequest
from openapi_server.models.describe_configuration_set_response import DescribeConfigurationSetResponse
from openapi_server.models.describe_receipt_rule_request import DescribeReceiptRuleRequest
from openapi_server.models.describe_receipt_rule_response import DescribeReceiptRuleResponse
from openapi_server.models.describe_receipt_rule_set_request import DescribeReceiptRuleSetRequest
from openapi_server.models.describe_receipt_rule_set_response import DescribeReceiptRuleSetResponse
from openapi_server.models.get_create_configuration_set_configuration_set_parameter import GETCreateConfigurationSetConfigurationSetParameter
from openapi_server.models.get_create_configuration_set_event_destination_event_destination_parameter import GETCreateConfigurationSetEventDestinationEventDestinationParameter
from openapi_server.models.get_create_configuration_set_tracking_options_tracking_options_parameter import GETCreateConfigurationSetTrackingOptionsTrackingOptionsParameter
from openapi_server.models.get_create_receipt_filter_filter_parameter import GETCreateReceiptFilterFilterParameter
from openapi_server.models.get_create_receipt_rule_rule_parameter import GETCreateReceiptRuleRuleParameter
from openapi_server.models.get_create_template_template_parameter import GETCreateTemplateTemplateParameter
from openapi_server.models.get_put_configuration_set_delivery_options_delivery_options_parameter import GETPutConfigurationSetDeliveryOptionsDeliveryOptionsParameter
from openapi_server.models.get_send_bounce_message_dsn_parameter import GETSendBounceMessageDsnParameter
from openapi_server.models.get_send_email_destination_parameter import GETSendEmailDestinationParameter
from openapi_server.models.get_send_email_message_parameter import GETSendEmailMessageParameter
from openapi_server.models.get_send_raw_email_raw_message_parameter import GETSendRawEmailRawMessageParameter
from openapi_server.models.get_account_sending_enabled_response import GetAccountSendingEnabledResponse
from openapi_server.models.get_custom_verification_email_template_request import GetCustomVerificationEmailTemplateRequest
from openapi_server.models.get_custom_verification_email_template_response import GetCustomVerificationEmailTemplateResponse
from openapi_server.models.get_identity_dkim_attributes_request import GetIdentityDkimAttributesRequest
from openapi_server.models.get_identity_dkim_attributes_response import GetIdentityDkimAttributesResponse
from openapi_server.models.get_identity_mail_from_domain_attributes_request import GetIdentityMailFromDomainAttributesRequest
from openapi_server.models.get_identity_mail_from_domain_attributes_response import GetIdentityMailFromDomainAttributesResponse
from openapi_server.models.get_identity_notification_attributes_request import GetIdentityNotificationAttributesRequest
from openapi_server.models.get_identity_notification_attributes_response import GetIdentityNotificationAttributesResponse
from openapi_server.models.get_identity_policies_request import GetIdentityPoliciesRequest
from openapi_server.models.get_identity_policies_response import GetIdentityPoliciesResponse
from openapi_server.models.get_identity_verification_attributes_request import GetIdentityVerificationAttributesRequest
from openapi_server.models.get_identity_verification_attributes_response import GetIdentityVerificationAttributesResponse
from openapi_server.models.get_send_quota_response import GetSendQuotaResponse
from openapi_server.models.get_send_statistics_response import GetSendStatisticsResponse
from openapi_server.models.get_template_request import GetTemplateRequest
from openapi_server.models.get_template_response import GetTemplateResponse
from openapi_server.models.list_configuration_sets_request import ListConfigurationSetsRequest
from openapi_server.models.list_configuration_sets_response import ListConfigurationSetsResponse
from openapi_server.models.list_custom_verification_email_templates_request import ListCustomVerificationEmailTemplatesRequest
from openapi_server.models.list_custom_verification_email_templates_response import ListCustomVerificationEmailTemplatesResponse
from openapi_server.models.list_identities_request import ListIdentitiesRequest
from openapi_server.models.list_identities_response import ListIdentitiesResponse
from openapi_server.models.list_identity_policies_request import ListIdentityPoliciesRequest
from openapi_server.models.list_identity_policies_response import ListIdentityPoliciesResponse
from openapi_server.models.list_receipt_filters_response import ListReceiptFiltersResponse
from openapi_server.models.list_receipt_rule_sets_request import ListReceiptRuleSetsRequest
from openapi_server.models.list_receipt_rule_sets_response import ListReceiptRuleSetsResponse
from openapi_server.models.list_templates_request import ListTemplatesRequest
from openapi_server.models.list_templates_response import ListTemplatesResponse
from openapi_server.models.list_verified_email_addresses_response import ListVerifiedEmailAddressesResponse
from openapi_server.models.message_tag import MessageTag
from openapi_server.models.put_configuration_set_delivery_options_request import PutConfigurationSetDeliveryOptionsRequest
from openapi_server.models.put_identity_policy_request import PutIdentityPolicyRequest
from openapi_server.models.reorder_receipt_rule_set_request import ReorderReceiptRuleSetRequest
from openapi_server.models.send_bounce_request import SendBounceRequest
from openapi_server.models.send_bounce_response import SendBounceResponse
from openapi_server.models.send_bulk_templated_email_request import SendBulkTemplatedEmailRequest
from openapi_server.models.send_bulk_templated_email_response import SendBulkTemplatedEmailResponse
from openapi_server.models.send_custom_verification_email_request import SendCustomVerificationEmailRequest
from openapi_server.models.send_custom_verification_email_response import SendCustomVerificationEmailResponse
from openapi_server.models.send_email_request import SendEmailRequest
from openapi_server.models.send_email_response import SendEmailResponse
from openapi_server.models.send_raw_email_request import SendRawEmailRequest
from openapi_server.models.send_raw_email_response import SendRawEmailResponse
from openapi_server.models.send_templated_email_request import SendTemplatedEmailRequest
from openapi_server.models.send_templated_email_response import SendTemplatedEmailResponse
from openapi_server.models.set_active_receipt_rule_set_request import SetActiveReceiptRuleSetRequest
from openapi_server.models.set_identity_dkim_enabled_request import SetIdentityDkimEnabledRequest
from openapi_server.models.set_identity_feedback_forwarding_enabled_request import SetIdentityFeedbackForwardingEnabledRequest
from openapi_server.models.set_identity_headers_in_notifications_enabled_request import SetIdentityHeadersInNotificationsEnabledRequest
from openapi_server.models.set_identity_mail_from_domain_request import SetIdentityMailFromDomainRequest
from openapi_server.models.set_identity_notification_topic_request import SetIdentityNotificationTopicRequest
from openapi_server.models.set_receipt_rule_position_request import SetReceiptRulePositionRequest
from openapi_server.models.test_render_template_request import TestRenderTemplateRequest
from openapi_server.models.test_render_template_response import TestRenderTemplateResponse
from openapi_server.models.update_account_sending_enabled_request import UpdateAccountSendingEnabledRequest
from openapi_server.models.update_configuration_set_event_destination_request import UpdateConfigurationSetEventDestinationRequest
from openapi_server.models.update_configuration_set_reputation_metrics_enabled_request import UpdateConfigurationSetReputationMetricsEnabledRequest
from openapi_server.models.update_configuration_set_sending_enabled_request import UpdateConfigurationSetSendingEnabledRequest
from openapi_server.models.update_configuration_set_tracking_options_request import UpdateConfigurationSetTrackingOptionsRequest
from openapi_server.models.update_custom_verification_email_template_request import UpdateCustomVerificationEmailTemplateRequest
from openapi_server.models.update_receipt_rule_request import UpdateReceiptRuleRequest
from openapi_server.models.update_template_request import UpdateTemplateRequest
from openapi_server.models.verify_domain_dkim_request import VerifyDomainDkimRequest
from openapi_server.models.verify_domain_dkim_response import VerifyDomainDkimResponse
from openapi_server.models.verify_domain_identity_request import VerifyDomainIdentityRequest
from openapi_server.models.verify_domain_identity_response import VerifyDomainIdentityResponse
from openapi_server.models.verify_email_address_request import VerifyEmailAddressRequest
from openapi_server.models.verify_email_identity_request import VerifyEmailIdentityRequest
from openapi_server import util


async def g_et_clone_receipt_rule_set(request: web.Request, rule_set_name, original_rule_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_clone_receipt_rule_set

    &lt;p&gt;Creates a receipt rule set by cloning an existing one. All receipt rules and configurations are copied to the new receipt rule set and are completely independent of the source rule set.&lt;/p&gt; &lt;p&gt;For information about setting up rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: &lt;p&gt;The name of the rule set to create. The name must:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start and end with a letter or number.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Contain less than 64 characters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type rule_set_name: str
    :param original_rule_set_name: The name of the rule set to clone.
    :type original_rule_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_create_configuration_set(request: web.Request, configuration_set, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_configuration_set

    &lt;p&gt;Creates a configuration set.&lt;/p&gt; &lt;p&gt;Configuration sets enable you to publish email sending events. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set: A data structure that contains the name of the configuration set.
    :type configuration_set: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    configuration_set = .from_dict(configuration_set)
    return web.Response(status=200)


async def g_et_create_configuration_set_event_destination(request: web.Request, configuration_set_name, event_destination, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_configuration_set_event_destination

    &lt;p&gt;Creates a configuration set event destination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you create or update an event destination, you must provide one, and only one, destination. The destination can be CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).&lt;/p&gt; &lt;/note&gt; &lt;p&gt;An event destination is the AWS service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that the event destination should be associated with.
    :type configuration_set_name: str
    :param event_destination: An object that describes the AWS service that email sending event information will be published to.
    :type event_destination: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    event_destination = .from_dict(event_destination)
    return web.Response(status=200)


async def g_et_create_configuration_set_tracking_options(request: web.Request, configuration_set_name, tracking_options, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_configuration_set_tracking_options

    &lt;p&gt;Creates an association between a configuration set and a custom domain for open and click event tracking. &lt;/p&gt; &lt;p&gt;By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that the tracking options should be associated with.
    :type configuration_set_name: str
    :param tracking_options: 
    :type tracking_options: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    tracking_options = .from_dict(tracking_options)
    return web.Response(status=200)


async def g_et_create_custom_verification_email_template(request: web.Request, template_name, from_email_address, template_subject, template_content, success_redirection_url, failure_redirection_url, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_custom_verification_email_template

    &lt;p&gt;Creates a new custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the custom verification email template.
    :type template_name: str
    :param from_email_address: The email address that the custom verification email is sent from.
    :type from_email_address: str
    :param template_subject: The subject line of the custom verification email.
    :type template_subject: str
    :param template_content: The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html#custom-verification-emails-faq\&quot;&gt;Custom Verification Email Frequently Asked Questions&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.
    :type template_content: str
    :param success_redirection_url: The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
    :type success_redirection_url: str
    :param failure_redirection_url: The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
    :type failure_redirection_url: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_create_receipt_filter(request: web.Request, filter, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_receipt_filter

    &lt;p&gt;Creates a new IP address filter.&lt;/p&gt; &lt;p&gt;For information about setting up IP address filters, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param filter: A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.
    :type filter: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    filter = .from_dict(filter)
    return web.Response(status=200)


async def g_et_create_receipt_rule(request: web.Request, rule_set_name, rule, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, after=None) -> web.Response:
    """g_et_create_receipt_rule

    &lt;p&gt;Creates a receipt rule.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the rule set that the receipt rule will be added to.
    :type rule_set_name: str
    :param rule: A data structure that contains the specified rule&#39;s name, actions, recipients, domains, enabled status, scan status, and TLS policy.
    :type rule: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param after: The name of an existing rule after which the new rule will be placed. If this parameter is null, the new rule will be inserted at the beginning of the rule list.
    :type after: str

    """
    rule = .from_dict(rule)
    return web.Response(status=200)


async def g_et_create_receipt_rule_set(request: web.Request, rule_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_receipt_rule_set

    &lt;p&gt;Creates an empty receipt rule set.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: &lt;p&gt;The name of the rule set to create. The name must:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start and end with a letter or number.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Contain less than 64 characters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type rule_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_create_template(request: web.Request, template, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_template

    &lt;p&gt;Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template: The content of the email, composed of a subject line, an HTML part, and a text-only part.
    :type template: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    template = .from_dict(template)
    return web.Response(status=200)


async def g_et_delete_configuration_set(request: web.Request, configuration_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_configuration_set

    &lt;p&gt;Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set to delete.
    :type configuration_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_configuration_set_event_destination(request: web.Request, configuration_set_name, event_destination_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_configuration_set_event_destination

    &lt;p&gt;Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set from which to delete the event destination.
    :type configuration_set_name: str
    :param event_destination_name: The name of the event destination to delete.
    :type event_destination_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_configuration_set_tracking_options(request: web.Request, configuration_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_configuration_set_tracking_options

    &lt;p&gt;Deletes an association between a configuration set and a custom domain for open and click event tracking.&lt;/p&gt; &lt;p&gt;By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Deleting this kind of association will result in emails sent using the specified configuration set to capture open and click events using the standard, Amazon SES-operated domains.&lt;/p&gt; &lt;/note&gt;

    :param configuration_set_name: The name of the configuration set from which you want to delete the tracking options.
    :type configuration_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_custom_verification_email_template(request: web.Request, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_custom_verification_email_template

    &lt;p&gt;Deletes an existing custom verification email template. &lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the custom verification email template that you want to delete.
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_identity(request: web.Request, identity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_identity

    &lt;p&gt;Deletes the specified identity (an email address or a domain) from the list of verified identities.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param identity: The identity to be removed from the list of identities for the AWS Account.
    :type identity: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_identity_policy(request: web.Request, identity, policy_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_identity_policy

    &lt;p&gt;Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param identity: &lt;p&gt;The identity that is associated with the policy that you want to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: &lt;code&gt;user@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;, &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To successfully call this API, you must own the identity.&lt;/p&gt;
    :type identity: str
    :param policy_name: The name of the policy to be deleted.
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

    """
    return web.Response(status=200)


async def g_et_delete_receipt_filter(request: web.Request, filter_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_receipt_filter

    &lt;p&gt;Deletes the specified IP address filter.&lt;/p&gt; &lt;p&gt;For information about managing IP address filters, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-ip-filters.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param filter_name: The name of the IP address filter to delete.
    :type filter_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_receipt_rule(request: web.Request, rule_set_name, rule_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_receipt_rule

    &lt;p&gt;Deletes the specified receipt rule.&lt;/p&gt; &lt;p&gt;For information about managing receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the receipt rule set that contains the receipt rule to delete.
    :type rule_set_name: str
    :param rule_name: The name of the receipt rule to delete.
    :type rule_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_receipt_rule_set(request: web.Request, rule_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_receipt_rule_set

    &lt;p&gt;Deletes the specified receipt rule set and all of the receipt rules it contains.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The currently active rule set cannot be deleted.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the receipt rule set to delete.
    :type rule_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_template(request: web.Request, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_template

    &lt;p&gt;Deletes an email template.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the template to be deleted.
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_verified_email_address(request: web.Request, email_address, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_verified_email_address

    Deprecated. Use the &lt;code&gt;DeleteIdentity&lt;/code&gt; operation to delete email addresses and domains.

    :param email_address: An email address to be removed from the list of verified addresses.
    :type email_address: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_describe_active_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_active_receipt_rule_set

    &lt;p&gt;Returns the metadata and receipt rules for the receipt rule set that is currently active.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_describe_configuration_set(request: web.Request, configuration_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, configuration_set_attribute_names=None) -> web.Response:
    """g_et_describe_configuration_set

    &lt;p&gt;Returns the details of the specified configuration set. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set to describe.
    :type configuration_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param configuration_set_attribute_names: A list of configuration set attributes to return.
    :type configuration_set_attribute_names: list | bytes

    """
    configuration_set_attribute_names = [ConfigurationSetAttribute.from_dict(d) for d in configuration_set_attribute_names]
    return web.Response(status=200)


async def g_et_describe_receipt_rule(request: web.Request, rule_set_name, rule_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_receipt_rule

    &lt;p&gt;Returns the details of the specified receipt rule.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the receipt rule set that the receipt rule belongs to.
    :type rule_set_name: str
    :param rule_name: The name of the receipt rule.
    :type rule_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_describe_receipt_rule_set(request: web.Request, rule_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_receipt_rule_set

    &lt;p&gt;Returns the details of the specified receipt rule set.&lt;/p&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the receipt rule set to describe.
    :type rule_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_account_sending_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_account_sending_enabled

    &lt;p&gt;Returns the email sending status of the Amazon SES account for the current region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_custom_verification_email_template(request: web.Request, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_custom_verification_email_template

    &lt;p&gt;Returns the custom email verification template for the template name you specify.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the custom verification email template that you want to retrieve.
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_identity_dkim_attributes(request: web.Request, identities, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_identity_dkim_attributes

    &lt;p&gt;Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.&lt;/p&gt; &lt;p&gt;This operation takes a list of identities as input and returns the following information for each:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether Easy DKIM signing is enabled or disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Whether Amazon SES has successfully verified the DKIM tokens published in the domain&#39;s DNS. This information is only returned for domain name identities, not for email addresses.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time.&lt;/p&gt; &lt;p&gt;For more information about creating DNS records using DKIM tokens, go to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param identities: A list of one or more verified identities - email addresses, domains, or both.
    :type identities: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_identity_mail_from_domain_attributes(request: web.Request, identities, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_identity_mail_from_domain_attributes

    &lt;p&gt;Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).&lt;/p&gt; &lt;p&gt;This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.&lt;/p&gt;

    :param identities: A list of one or more identities.
    :type identities: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_identity_notification_attributes(request: web.Request, identities, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_identity_notification_attributes

    &lt;p&gt;Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.&lt;/p&gt; &lt;p&gt;This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time.&lt;/p&gt; &lt;p&gt;For more information about using notifications with Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param identities: A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: &lt;code&gt;user@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;, &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;.
    :type identities: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_identity_policies(request: web.Request, identity, policy_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_identity_policies

    &lt;p&gt;Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param identity: &lt;p&gt;The identity for which the policies will be retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: &lt;code&gt;user@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;, &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To successfully call this API, you must own the identity.&lt;/p&gt;
    :type identity: str
    :param policy_names: A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use &lt;code&gt;ListIdentityPolicies&lt;/code&gt;.
    :type policy_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_identity_verification_attributes(request: web.Request, identities, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_identity_verification_attributes

    &lt;p&gt;Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.&lt;/p&gt; &lt;p&gt;The verification status of an email address is \&quot;Pending\&quot; until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to \&quot;Success\&quot;. If the link is not clicked within 24 hours, the verification status changes to \&quot;Failed.\&quot; In that case, if you still want to verify the email address, you must restart the verification process from the beginning.&lt;/p&gt; &lt;p&gt;For domain identities, the domain&#39;s verification status is \&quot;Pending\&quot; as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain&#39;s verification status changes to \&quot;Success\&quot;. If Amazon SES is unable to detect the record within 72 hours, the domain&#39;s verification status changes to \&quot;Failed.\&quot; In that case, if you still want to verify the domain, you must restart the verification process from the beginning.&lt;/p&gt; &lt;p&gt;This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.&lt;/p&gt;

    :param identities: A list of identities.
    :type identities: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_send_quota(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_send_quota

    &lt;p&gt;Provides the sending limits for the Amazon SES account. &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_send_statistics(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_send_statistics

    &lt;p&gt;Provides sending statistics for the current AWS Region. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute period of time.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_template(request: web.Request, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_template

    &lt;p&gt;Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the template you want to retrieve.
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_list_configuration_sets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_items=None) -> web.Response:
    """g_et_list_configuration_sets

    &lt;p&gt;Provides a list of the configuration sets associated with your Amazon SES account in the current AWS Region. For information about using configuration sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Monitoring Your Amazon SES Sending Activity&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second. This operation will return up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation will also return a NextToken element. You can then execute the &lt;code&gt;ListConfigurationSets&lt;/code&gt; operation again, passing the &lt;code&gt;NextToken&lt;/code&gt; parameter and the value of the NextToken element to retrieve additional results.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListConfigurationSets&lt;/code&gt; to indicate the position of the configuration set in the configuration set list.
    :type next_token: str
    :param max_items: The number of configuration sets to return.
    :type max_items: int

    """
    return web.Response(status=200)


async def g_et_list_custom_verification_email_templates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """g_et_list_custom_verification_email_templates

    &lt;p&gt;Lists the existing custom verification email templates for your account in the current AWS Region.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: An array the contains the name and creation time stamp for each template in your Amazon SES account.
    :type next_token: str
    :param max_results: The maximum number of custom verification email templates to return. This value must be at least 1 and less than or equal to 50. If you do not specify a value, or if you specify a value less than 1 or greater than 50, the operation will return up to 50 results.
    :type max_results: int

    """
    return web.Response(status=200)


async def g_et_list_identities(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, identity_type=None, next_token=None, max_items=None) -> web.Response:
    """g_et_list_identities

    &lt;p&gt;Returns a list containing all of the identities (email addresses and domains) for your AWS account in the current AWS Region, regardless of verification status.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param identity_type: The type of the identities to list. Possible values are \&quot;EmailAddress\&quot; and \&quot;Domain\&quot;. If this parameter is omitted, then all identities will be listed.
    :type identity_type: str
    :param next_token: The token to use for pagination.
    :type next_token: str
    :param max_items: The maximum number of identities per page. Possible values are 1-1000 inclusive.
    :type max_items: int

    """
    return web.Response(status=200)


async def g_et_list_identity_policies(request: web.Request, identity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_identity_policies

    &lt;p&gt;Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This API returns only a list. If you want the actual policy content, you can use &lt;code&gt;GetIdentityPolicies&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param identity: &lt;p&gt;The identity that is associated with the policy for which the policies will be listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: &lt;code&gt;user@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;, &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To successfully call this API, you must own the identity.&lt;/p&gt;
    :type identity: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_list_receipt_filters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_receipt_filters

    &lt;p&gt;Lists the IP address filters associated with your AWS account in the current AWS Region.&lt;/p&gt; &lt;p&gt;For information about managing IP address filters, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-ip-filters.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_list_receipt_rule_sets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """g_et_list_receipt_rule_sets

    &lt;p&gt;Lists the receipt rule sets that exist under your AWS account in the current AWS Region. If there are additional receipt rule sets to be retrieved, you will receive a &lt;code&gt;NextToken&lt;/code&gt; that you can provide to the next call to &lt;code&gt;ListReceiptRuleSets&lt;/code&gt; to retrieve the additional entries.&lt;/p&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListReceiptRuleSets&lt;/code&gt; to indicate the position in the receipt rule set list.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_templates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_items=None) -> web.Response:
    """g_et_list_templates

    &lt;p&gt;Lists the email templates present in your Amazon SES account in the current AWS Region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListTemplates&lt;/code&gt; to indicate the position in the list of email templates.
    :type next_token: str
    :param max_items: The maximum number of templates to return. This value must be at least 1 and less than or equal to 10. If you do not specify a value, or if you specify a value less than 1 or greater than 10, the operation will return up to 10 results.
    :type max_items: int

    """
    return web.Response(status=200)


async def g_et_list_verified_email_addresses(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_verified_email_addresses

    Deprecated. Use the &lt;code&gt;ListIdentities&lt;/code&gt; operation to list the email addresses and domains associated with your account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_put_configuration_set_delivery_options(request: web.Request, configuration_set_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, delivery_options=None) -> web.Response:
    """g_et_put_configuration_set_delivery_options

    Adds or updates the delivery options for a configuration set.

    :param configuration_set_name: The name of the configuration set that you want to specify the delivery options for.
    :type configuration_set_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param delivery_options: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).
    :type delivery_options: dict | bytes

    """
    delivery_options = .from_dict(delivery_options)
    return web.Response(status=200)


async def g_et_put_identity_policy(request: web.Request, identity, policy_name, policy, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_put_identity_policy

    &lt;p&gt;Adds or updates a sending authorization policy for the specified identity (an email address or a domain).&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param identity: &lt;p&gt;The identity that the policy will apply to. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: &lt;code&gt;user@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;, &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To successfully call this API, you must own the identity.&lt;/p&gt;
    :type identity: str
    :param policy_name: &lt;p&gt;The name of the policy.&lt;/p&gt; &lt;p&gt;The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.&lt;/p&gt;
    :type policy_name: str
    :param policy: &lt;p&gt;The text of the policy in JSON format. The policy cannot exceed 4 KB.&lt;/p&gt; &lt;p&gt;For information about the syntax of sending authorization policies, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;. &lt;/p&gt;
    :type policy: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_reorder_receipt_rule_set(request: web.Request, rule_set_name, rule_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_reorder_receipt_rule_set

    &lt;p&gt;Reorders the receipt rules within a receipt rule set.&lt;/p&gt; &lt;note&gt; &lt;p&gt;All of the rules in the rule set must be represented in this request. That is, this API will return an error if the reorder request doesn&#39;t explicitly position all of the rules.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the receipt rule set to reorder.
    :type rule_set_name: str
    :param rule_names: A list of the specified receipt rule set&#39;s receipt rules in the order that you want to put them.
    :type rule_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_send_bounce(request: web.Request, original_message_id, bounce_sender, bounced_recipient_info_list, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, explanation=None, message_dsn=None, bounce_sender_arn=None) -> web.Response:
    """g_et_send_bounce

    &lt;p&gt;Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this API on an email up to 24 hours after you receive it.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot use this API to send generic bounces for mail that was not received by Amazon SES.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about receiving email through Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param original_message_id: The message ID of the message to be bounced.
    :type original_message_id: str
    :param bounce_sender: The address to use in the \&quot;From\&quot; header of the bounce message. This must be an identity that you have verified with Amazon SES.
    :type bounce_sender: str
    :param bounced_recipient_info_list: A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one &lt;code&gt;BouncedRecipientInfo&lt;/code&gt; in the list.
    :type bounced_recipient_info_list: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param explanation: Human-readable text for the bounce message to explain the failure. If not specified, the text will be auto-generated based on the bounced recipient information.
    :type explanation: str
    :param message_dsn: Message-related DSN fields. If not specified, Amazon SES will choose the values.
    :type message_dsn: dict | bytes
    :param bounce_sender_arn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the \&quot;From\&quot; header of the bounce. For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.
    :type bounce_sender_arn: str

    """
    bounced_recipient_info_list = [BouncedRecipientInfo.from_dict(d) for d in bounced_recipient_info_list]
    message_dsn = .from_dict(message_dsn)
    return web.Response(status=200)


async def g_et_send_bulk_templated_email(request: web.Request, source, template, destinations, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_arn=None, reply_to_addresses=None, return_path=None, return_path_arn=None, configuration_set_name=None, default_tags=None, template_arn=None, default_template_data=None) -> web.Response:
    """g_et_send_bulk_templated_email

    &lt;p&gt;Composes an email message to multiple destinations. The message body is created using an email template.&lt;/p&gt; &lt;p&gt;In order to send email using the &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt; operation, your call to the API must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The call must refer to an existing email template. You can create email templates using the &lt;a&gt;CreateTemplate&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message must be sent from a verified email address or domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each &lt;code&gt;Destination&lt;/code&gt; parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), the entire message will be rejected, even if the message contains other recipients that are valid.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt; operation several times to send the message to each group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of destinations you can contact in a single call to the API may be limited by your account&#39;s maximum sending rate.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param source: &lt;p&gt;The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the &lt;code&gt;SourceArn&lt;/code&gt; parameter. For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon SES does not support the SMTPUTF8 extension, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc6531\&quot;&gt;RFC6531&lt;/a&gt;. For this reason, the &lt;i&gt;local part&lt;/i&gt; of a source email address (the part of the email address that precedes the @ sign) may only contain &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Email_address#Local-part\&quot;&gt;7-bit ASCII characters&lt;/a&gt;. If the &lt;i&gt;domain part&lt;/i&gt; of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc3492.html\&quot;&gt;RFC3492&lt;/a&gt;. The sender name (also known as the &lt;i&gt;friendly name&lt;/i&gt;) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc2047\&quot;&gt;RFC 2047&lt;/a&gt;. MIME encoded-word syntax uses the following form: &lt;code&gt;&#x3D;?charset?encoding?encoded-text?&#x3D;&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type source: str
    :param template: The template to use when sending this email.
    :type template: str
    :param destinations: One or more &lt;code&gt;Destination&lt;/code&gt; objects. All of the recipients in a &lt;code&gt;Destination&lt;/code&gt; will receive the same version of the email. You can specify up to 50 &lt;code&gt;Destination&lt;/code&gt; objects within a &lt;code&gt;Destinations&lt;/code&gt; array.
    :type destinations: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param source_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the &lt;code&gt;Source&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to send from &lt;code&gt;user@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;SourceArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;Source&lt;/code&gt; to be &lt;code&gt;user@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;
    :type source_arn: str
    :param reply_to_addresses: The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
    :type reply_to_addresses: List[str]
    :param return_path: The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient&#39;s ISP; this message will then be forwarded to the email address specified by the &lt;code&gt;ReturnPath&lt;/code&gt; parameter. The &lt;code&gt;ReturnPath&lt;/code&gt; parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. 
    :type return_path: str
    :param return_path_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the &lt;code&gt;ReturnPath&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to use &lt;code&gt;feedback@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;ReturnPathArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;ReturnPath&lt;/code&gt; to be &lt;code&gt;feedback@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;
    :type return_path_arn: str
    :param configuration_set_name: The name of the configuration set to use when you send an email using &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt;.
    :type configuration_set_name: str
    :param default_tags: A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt;.
    :type default_tags: list | bytes
    :param template_arn: The ARN of the template to use when sending this email.
    :type template_arn: str
    :param default_template_data: &lt;p&gt;A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available.&lt;/p&gt; &lt;p&gt;The template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.&lt;/p&gt;
    :type default_template_data: str

    """
    destinations = [BulkEmailDestination.from_dict(d) for d in destinations]
    default_tags = [MessageTag.from_dict(d) for d in default_tags]
    return web.Response(status=200)


async def g_et_send_custom_verification_email(request: web.Request, email_address, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, configuration_set_name=None) -> web.Response:
    """g_et_send_custom_verification_email

    &lt;p&gt;Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.&lt;/p&gt; &lt;p&gt;To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param email_address: The email address to verify.
    :type email_address: str
    :param template_name: The name of the custom verification email template to use when sending the verification email.
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param configuration_set_name: Name of a configuration set to use when sending the verification email.
    :type configuration_set_name: str

    """
    return web.Response(status=200)


async def g_et_send_email(request: web.Request, source, destination, message, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reply_to_addresses=None, return_path=None, source_arn=None, return_path_arn=None, tags=None, configuration_set_name=None) -> web.Response:
    """g_et_send_email

    &lt;p&gt;Composes an email message and immediately queues it for sending. In order to send email using the &lt;code&gt;SendEmail&lt;/code&gt; operation, your message must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation will result in an \&quot;Email address not verified\&quot; error. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), the entire message will be rejected, even if the message contains other recipients that are valid.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the &lt;code&gt;SendEmail&lt;/code&gt; operation several times to send the message to each group.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your &lt;i&gt;sending quota&lt;/i&gt;). For more information about sending quotas in Amazon SES, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-limits.html\&quot;&gt;Managing Your Amazon SES Sending Limits&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/important&gt;

    :param source: &lt;p&gt;The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the &lt;code&gt;SourceArn&lt;/code&gt; parameter. For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon SES does not support the SMTPUTF8 extension, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc6531\&quot;&gt;RFC6531&lt;/a&gt;. For this reason, the &lt;i&gt;local part&lt;/i&gt; of a source email address (the part of the email address that precedes the @ sign) may only contain &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Email_address#Local-part\&quot;&gt;7-bit ASCII characters&lt;/a&gt;. If the &lt;i&gt;domain part&lt;/i&gt; of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc3492.html\&quot;&gt;RFC3492&lt;/a&gt;. The sender name (also known as the &lt;i&gt;friendly name&lt;/i&gt;) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc2047\&quot;&gt;RFC 2047&lt;/a&gt;. MIME encoded-word syntax uses the following form: &lt;code&gt;&#x3D;?charset?encoding?encoded-text?&#x3D;&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type source: str
    :param destination: The destination for this email, composed of To:, CC:, and BCC: fields.
    :type destination: dict | bytes
    :param message: The message to be sent.
    :type message: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reply_to_addresses: The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
    :type reply_to_addresses: List[str]
    :param return_path: The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient&#39;s ISP; this message will then be forwarded to the email address specified by the &lt;code&gt;ReturnPath&lt;/code&gt; parameter. The &lt;code&gt;ReturnPath&lt;/code&gt; parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. 
    :type return_path: str
    :param source_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the &lt;code&gt;Source&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to send from &lt;code&gt;user@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;SourceArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;Source&lt;/code&gt; to be &lt;code&gt;user@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;
    :type source_arn: str
    :param return_path_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the &lt;code&gt;ReturnPath&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to use &lt;code&gt;feedback@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;ReturnPathArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;ReturnPath&lt;/code&gt; to be &lt;code&gt;feedback@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;
    :type return_path_arn: str
    :param tags: A list of tags, in the form of name/value pairs, to apply to an email that you send using &lt;code&gt;SendEmail&lt;/code&gt;. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
    :type tags: list | bytes
    :param configuration_set_name: The name of the configuration set to use when you send an email using &lt;code&gt;SendEmail&lt;/code&gt;.
    :type configuration_set_name: str

    """
    destination = .from_dict(destination)
    message = .from_dict(message)
    tags = [MessageTag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_send_raw_email(request: web.Request, raw_message, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source=None, destinations=None, from_arn=None, source_arn=None, return_path_arn=None, tags=None, configuration_set_name=None) -> web.Response:
    """g_et_send_raw_email

    &lt;p&gt;Composes an email message and immediately queues it for sending.&lt;/p&gt; &lt;p&gt;This operation is more flexible than the &lt;code&gt;SendEmail&lt;/code&gt; API operation. When you use the &lt;code&gt;SendRawEmail&lt;/code&gt; operation, you can specify the headers of the message as well as its content. This flexibility is useful, for example, when you want to send a multipart MIME email (such a message that contains both a text and an HTML version). You can also use this operation to send messages that include attachments.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;SendRawEmail&lt;/code&gt; operation has the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can only send email from &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;verified email addresses or domains&lt;/a&gt;. If you try to send email from an address that isn&#39;t verified, the operation results in an \&quot;Email address not verified\&quot; error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html\&quot;&gt;Amazon SES sandbox&lt;/a&gt;, you can only send email to other verified addresses in your account, or to addresses that are associated with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mailbox-simulator.html\&quot;&gt;Amazon SES mailbox simulator&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size, including attachments, is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each message has to include at least one recipient address. A recipient address includes any address on the To:, CC:, or BCC: lines.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you send a single message to more than one recipient address, and one of the recipient addresses isn&#39;t in a valid format (that is, it&#39;s not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), Amazon SES rejects the entire message, even if the other addresses are valid.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each message can include up to 50 recipient addresses across the To:, CC:, or BCC: lines. If you need to send a single message to more than 50 recipients, you have to split the list of recipient addresses into groups of less than 50 recipients, and send separate messages to each group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon SES allows you to specify 8-bit Content-Transfer-Encoding for MIME message parts. However, if Amazon SES has to modify the contents of your message (for example, if you use open and click tracking), 8-bit content isn&#39;t preserved. For this reason, we highly recommend that you encode all content that isn&#39;t 7-bit ASCII. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html#send-email-mime-encoding\&quot;&gt;MIME Encoding&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Additionally, keep the following considerations in mind when using the &lt;code&gt;SendRawEmail&lt;/code&gt; operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Although you can customize the message headers when using the &lt;code&gt;SendRawEmail&lt;/code&gt; operation, Amazon SES will automatically apply its own &lt;code&gt;Message-ID&lt;/code&gt; and &lt;code&gt;Date&lt;/code&gt; headers; if you passed these headers when creating the message, they will be overwritten by the values that Amazon SES provides.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are using sending authorization to send on behalf of another user, &lt;code&gt;SendRawEmail&lt;/code&gt; enables you to specify the cross-account identity for the email&#39;s Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters &lt;code&gt;SourceArn&lt;/code&gt;, &lt;code&gt;FromArn&lt;/code&gt;, and/or &lt;code&gt;ReturnPathArn&lt;/code&gt; to the API, or you can include the following X-headers in the header of your raw email:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;X-SES-SOURCE-ARN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;X-SES-FROM-ARN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;X-SES-RETURN-PATH-ARN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;Don&#39;t include these X-headers in the DKIM signature. Amazon SES removes these before it sends the email.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you only specify the &lt;code&gt;SourceIdentityArn&lt;/code&gt; parameter, Amazon SES sets the From and Return-Path addresses to the same identity that you specified.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Using Sending Authorization with Amazon SES&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your &lt;i&gt;sending quota&lt;/i&gt;). For more information about sending quotas in Amazon SES, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-limits.html\&quot;&gt;Managing Your Amazon SES Sending Limits&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param raw_message: &lt;p&gt;The raw email message itself. The message has to meet the following criteria:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The message has to contain a header and a body, separated by a blank line.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All of the required header fields must be present in the message.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each part of a multipart MIME message must be formatted properly.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Attachments must be of a content type that Amazon SES supports. For a list on unsupported content types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mime-types.html\&quot;&gt;Unsupported Attachment Types&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The entire message must be base64-encoded.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, we highly recommend that you encode that content. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html\&quot;&gt;Sending Raw Email&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Per &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6\&quot;&gt;RFC 5321&lt;/a&gt;, the maximum length of each line of text, including the &amp;lt;CRLF&amp;gt;, must not exceed 1,000 characters.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type raw_message: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param source: &lt;p&gt;The identity&#39;s email address. If you do not provide a value for this parameter, you must specify a \&quot;From\&quot; address in the raw text of the message. (You can also specify both.)&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon SES does not support the SMTPUTF8 extension, as described in&lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc6531\&quot;&gt;RFC6531&lt;/a&gt;. For this reason, the &lt;i&gt;local part&lt;/i&gt; of a source email address (the part of the email address that precedes the @ sign) may only contain &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Email_address#Local-part\&quot;&gt;7-bit ASCII characters&lt;/a&gt;. If the &lt;i&gt;domain part&lt;/i&gt; of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc3492.html\&quot;&gt;RFC3492&lt;/a&gt;. The sender name (also known as the &lt;i&gt;friendly name&lt;/i&gt;) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc2047\&quot;&gt;RFC 2047&lt;/a&gt;. MIME encoded-word syntax uses the following form: &lt;code&gt;&#x3D;?charset?encoding?encoded-text?&#x3D;&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you specify the &lt;code&gt;Source&lt;/code&gt; parameter and have feedback forwarding enabled, then bounces and complaints will be sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.&lt;/p&gt;
    :type source: str
    :param destinations: A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.
    :type destinations: List[str]
    :param from_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular \&quot;From\&quot; address in the header of the raw email.&lt;/p&gt; &lt;p&gt;Instead of using this parameter, you can use the X-header &lt;code&gt;X-SES-FROM-ARN&lt;/code&gt; in the raw message of the email. If you use both the &lt;code&gt;FromArn&lt;/code&gt; parameter and the corresponding X-header, Amazon SES uses the value of the &lt;code&gt;FromArn&lt;/code&gt; parameter.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For information about when to use this parameter, see the description of &lt;code&gt;SendRawEmail&lt;/code&gt; in this guide, or see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;
    :type from_arn: str
    :param source_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the &lt;code&gt;Source&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to send from &lt;code&gt;user@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;SourceArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;Source&lt;/code&gt; to be &lt;code&gt;user@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Instead of using this parameter, you can use the X-header &lt;code&gt;X-SES-SOURCE-ARN&lt;/code&gt; in the raw message of the email. If you use both the &lt;code&gt;SourceArn&lt;/code&gt; parameter and the corresponding X-header, Amazon SES uses the value of the &lt;code&gt;SourceArn&lt;/code&gt; parameter.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For information about when to use this parameter, see the description of &lt;code&gt;SendRawEmail&lt;/code&gt; in this guide, or see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;
    :type source_arn: str
    :param return_path_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the &lt;code&gt;ReturnPath&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to use &lt;code&gt;feedback@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;ReturnPathArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;ReturnPath&lt;/code&gt; to be &lt;code&gt;feedback@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Instead of using this parameter, you can use the X-header &lt;code&gt;X-SES-RETURN-PATH-ARN&lt;/code&gt; in the raw message of the email. If you use both the &lt;code&gt;ReturnPathArn&lt;/code&gt; parameter and the corresponding X-header, Amazon SES uses the value of the &lt;code&gt;ReturnPathArn&lt;/code&gt; parameter.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For information about when to use this parameter, see the description of &lt;code&gt;SendRawEmail&lt;/code&gt; in this guide, or see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;
    :type return_path_arn: str
    :param tags: A list of tags, in the form of name/value pairs, to apply to an email that you send using &lt;code&gt;SendRawEmail&lt;/code&gt;. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
    :type tags: list | bytes
    :param configuration_set_name: The name of the configuration set to use when you send an email using &lt;code&gt;SendRawEmail&lt;/code&gt;.
    :type configuration_set_name: str

    """
    raw_message = .from_dict(raw_message)
    tags = [MessageTag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_send_templated_email(request: web.Request, source, destination, template, template_data, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reply_to_addresses=None, return_path=None, source_arn=None, return_path_arn=None, tags=None, configuration_set_name=None, template_arn=None) -> web.Response:
    """g_et_send_templated_email

    &lt;p&gt;Composes an email message using an email template and immediately queues it for sending.&lt;/p&gt; &lt;p&gt;In order to send email using the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; operation, your call to the API must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The call must refer to an existing email template. You can create email templates using the &lt;a&gt;CreateTemplate&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message must be sent from a verified email address or domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Calls to the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; operation may only include one &lt;code&gt;Destination&lt;/code&gt; parameter. A destination is a set of recipients who will receive the same version of the email. The &lt;code&gt;Destination&lt;/code&gt; parameter can include up to 50 recipients, across the To:, CC: and BCC: fields.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Destination&lt;/code&gt; parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), the entire message will be rejected, even if the message contains other recipients that are valid.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;If your call to the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; operation includes all of the required parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon SES can&#39;t render the email because the template contains errors, it doesn&#39;t send the email. Additionally, because it already accepted the message, Amazon SES doesn&#39;t return a message stating that it was unable to send the email.&lt;/p&gt; &lt;p&gt;For these reasons, we highly recommend that you set up Amazon SES to send you notifications when Rendering Failure events occur. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Sending Personalized Email Using the Amazon SES API&lt;/a&gt; in the &lt;i&gt;Amazon Simple Email Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param source: &lt;p&gt;The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the &lt;code&gt;SourceArn&lt;/code&gt; parameter. For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon SES does not support the SMTPUTF8 extension, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc6531\&quot;&gt;RFC6531&lt;/a&gt;. For this reason, the &lt;i&gt;local part&lt;/i&gt; of a source email address (the part of the email address that precedes the @ sign) may only contain &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Email_address#Local-part\&quot;&gt;7-bit ASCII characters&lt;/a&gt;. If the &lt;i&gt;domain part&lt;/i&gt; of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc3492.html\&quot;&gt;RFC3492&lt;/a&gt;. The sender name (also known as the &lt;i&gt;friendly name&lt;/i&gt;) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in&lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc2047\&quot;&gt;RFC 2047&lt;/a&gt;. MIME encoded-word syntax uses the following form: &lt;code&gt;&#x3D;?charset?encoding?encoded-text?&#x3D;&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type source: str
    :param destination: The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields.
    :type destination: dict | bytes
    :param template: The template to use when sending this email.
    :type template: str
    :param template_data: A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
    :type template_data: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reply_to_addresses: The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
    :type reply_to_addresses: List[str]
    :param return_path: The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient&#39;s ISP; this message will then be forwarded to the email address specified by the &lt;code&gt;ReturnPath&lt;/code&gt; parameter. The &lt;code&gt;ReturnPath&lt;/code&gt; parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. 
    :type return_path: str
    :param source_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the &lt;code&gt;Source&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to send from &lt;code&gt;user@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;SourceArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;Source&lt;/code&gt; to be &lt;code&gt;user@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;
    :type source_arn: str
    :param return_path_arn: &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the &lt;code&gt;ReturnPath&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of &lt;code&gt;example.com&lt;/code&gt; (which has ARN &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;) attaches a policy to it that authorizes you to use &lt;code&gt;feedback@example.com&lt;/code&gt;, then you would specify the &lt;code&gt;ReturnPathArn&lt;/code&gt; to be &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;, and the &lt;code&gt;ReturnPath&lt;/code&gt; to be &lt;code&gt;feedback@example.com&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;
    :type return_path_arn: str
    :param tags: A list of tags, in the form of name/value pairs, to apply to an email that you send using &lt;code&gt;SendTemplatedEmail&lt;/code&gt;. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
    :type tags: list | bytes
    :param configuration_set_name: The name of the configuration set to use when you send an email using &lt;code&gt;SendTemplatedEmail&lt;/code&gt;.
    :type configuration_set_name: str
    :param template_arn: The ARN of the template to use when sending this email.
    :type template_arn: str

    """
    destination = .from_dict(destination)
    tags = [MessageTag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_set_active_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, rule_set_name=None) -> web.Response:
    """g_et_set_active_receipt_rule_set

    &lt;p&gt;Sets the specified receipt rule set as the active receipt rule set.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To disable your email-receiving through Amazon SES completely, you can call this API with RuleSetName set to null.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param rule_set_name: The name of the receipt rule set to make active. Setting this value to null disables all email receiving.
    :type rule_set_name: str

    """
    return web.Response(status=200)


async def g_et_set_identity_dkim_enabled(request: web.Request, identity, dkim_enabled, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_identity_dkim_enabled

    &lt;p&gt;Enables or disables Easy DKIM signing of email sent from an identity. If Easy DKIM signing is enabled for a domain, then Amazon SES uses DKIM to sign all email that it sends from addresses on that domain. If Easy DKIM signing is enabled for an email address, then Amazon SES uses DKIM to sign all email it sends from that address.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For email addresses (for example, &lt;code&gt;user@example.com&lt;/code&gt;), you can only enable DKIM signing if the corresponding domain (in this case, &lt;code&gt;example.com&lt;/code&gt;) has been set up to use Easy DKIM.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can enable DKIM signing for an identity at any time after you start the verification process for the identity, even if the verification process isn&#39;t complete. &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about Easy DKIM signing, go to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param identity: The identity for which DKIM signing should be enabled or disabled.
    :type identity: str
    :param dkim_enabled: Sets whether DKIM signing is enabled for an identity. Set to &lt;code&gt;true&lt;/code&gt; to enable DKIM signing for this identity; &lt;code&gt;false&lt;/code&gt; to disable it. 
    :type dkim_enabled: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_set_identity_feedback_forwarding_enabled(request: web.Request, identity, forwarding_enabled, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_identity_feedback_forwarding_enabled

    &lt;p&gt;Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Feedback forwarding does not apply to delivery notifications. Delivery notifications are only available through Amazon SNS.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about using notifications with Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param identity: The identity for which to set bounce and complaint notification forwarding. Examples: &lt;code&gt;user@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;.
    :type identity: str
    :param forwarding_enabled: Sets whether Amazon SES will forward bounce and complaint notifications as email. &lt;code&gt;true&lt;/code&gt; specifies that Amazon SES will forward bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. &lt;code&gt;false&lt;/code&gt; specifies that Amazon SES will publish bounce and complaint notifications only through Amazon SNS. This value can only be set to &lt;code&gt;false&lt;/code&gt; when Amazon SNS topics are set for both &lt;code&gt;Bounce&lt;/code&gt; and &lt;code&gt;Complaint&lt;/code&gt; notification types.
    :type forwarding_enabled: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_set_identity_headers_in_notifications_enabled(request: web.Request, identity, notification_type, enabled, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_identity_headers_in_notifications_enabled

    &lt;p&gt;Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about using notifications with Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param identity: The identity for which to enable or disable headers in notifications. Examples: &lt;code&gt;user@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;.
    :type identity: str
    :param notification_type: The notification type for which to enable or disable headers in notifications. 
    :type notification_type: str
    :param enabled: &lt;p&gt;Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of &lt;code&gt;true&lt;/code&gt; specifies that Amazon SES will include headers in notifications, and a value of &lt;code&gt;false&lt;/code&gt; specifies that Amazon SES will not include headers in notifications.&lt;/p&gt; &lt;p&gt;This value can only be set when &lt;code&gt;NotificationType&lt;/code&gt; is already set to use a particular Amazon SNS topic.&lt;/p&gt;
    :type enabled: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_set_identity_mail_from_domain(request: web.Request, identity, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, mail_from_domain=None, behavior_on_mx_failure=None) -> web.Response:
    """g_et_set_identity_mail_from_domain

    &lt;p&gt;Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).&lt;/p&gt; &lt;important&gt; &lt;p&gt;To send emails using the specified MAIL FROM domain, you must add an MX record to your MAIL FROM domain&#39;s DNS settings. If you want your emails to pass Sender Policy Framework (SPF) checks, you must also add or update an SPF record. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param identity: The verified identity for which you want to enable or disable the specified custom MAIL FROM domain.
    :type identity: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param mail_from_domain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a \&quot;From\&quot; address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;), and 3) not be used to receive emails. A value of &lt;code&gt;null&lt;/code&gt; disables the custom MAIL FROM setting for the identity.
    :type mail_from_domain: str
    :param behavior_on_mx_failure: &lt;p&gt;The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose &lt;code&gt;UseDefaultValue&lt;/code&gt;, Amazon SES will use amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose &lt;code&gt;RejectMessage&lt;/code&gt;, Amazon SES will return a &lt;code&gt;MailFromDomainNotVerified&lt;/code&gt; error and not send the email.&lt;/p&gt; &lt;p&gt;The action specified in &lt;code&gt;BehaviorOnMXFailure&lt;/code&gt; is taken when the custom MAIL FROM domain setup is in the &lt;code&gt;Pending&lt;/code&gt;, &lt;code&gt;Failed&lt;/code&gt;, and &lt;code&gt;TemporaryFailure&lt;/code&gt; states.&lt;/p&gt;
    :type behavior_on_mx_failure: str

    """
    return web.Response(status=200)


async def g_et_set_identity_notification_topic(request: web.Request, identity, notification_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, sns_topic=None) -> web.Response:
    """g_et_set_identity_notification_topic

    &lt;p&gt;Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications. When you use this operation, you specify a verified identity, such as an email address or domain. When you send an email that uses the chosen identity in the Source field, Amazon SES sends notifications to the topic you specified. You can send bounce, complaint, or delivery notifications (or any combination of the three) to the Amazon SNS topic that you specify.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about feedback notification, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param identity: &lt;p&gt;The identity (email address or domain) that you want to set the Amazon SNS topic for.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can only specify a verified identity for this parameter.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You can specify an identity by using its name or by using its Amazon Resource Name (ARN). The following examples are all valid identities: &lt;code&gt;sender@example.com&lt;/code&gt;, &lt;code&gt;example.com&lt;/code&gt;, &lt;code&gt;arn:aws:ses:us-east-1:123456789012:identity/example.com&lt;/code&gt;.&lt;/p&gt;
    :type identity: str
    :param notification_type: The type of notifications that will be published to the specified Amazon SNS topic.
    :type notification_type: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param sns_topic: The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, &lt;code&gt;SnsTopic&lt;/code&gt; is cleared and publishing is disabled.
    :type sns_topic: str

    """
    return web.Response(status=200)


async def g_et_set_receipt_rule_position(request: web.Request, rule_set_name, rule_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, after=None) -> web.Response:
    """g_et_set_receipt_rule_position

    &lt;p&gt;Sets the position of the specified receipt rule in the receipt rule set.&lt;/p&gt; &lt;p&gt;For information about managing receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the receipt rule set that contains the receipt rule to reposition.
    :type rule_set_name: str
    :param rule_name: The name of the receipt rule to reposition.
    :type rule_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param after: The name of the receipt rule after which to place the specified receipt rule.
    :type after: str

    """
    return web.Response(status=200)


async def g_et_test_render_template(request: web.Request, template_name, template_data, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_test_render_template

    &lt;p&gt;Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the template that you want to render.
    :type template_name: str
    :param template_data: A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
    :type template_data: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_update_account_sending_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, enabled=None) -> web.Response:
    """g_et_update_account_sending_enabled

    &lt;p&gt;Enables or disables email sending across your entire Amazon SES account in the current AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account in a given AWS Region when reputation metrics (such as your bounce or complaint rates) reach certain thresholds.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param enabled: Describes whether email sending is enabled or disabled for your Amazon SES account in the current AWS Region.
    :type enabled: bool

    """
    return web.Response(status=200)


async def g_et_update_configuration_set_event_destination(request: web.Request, configuration_set_name, event_destination, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_configuration_set_event_destination

    &lt;p&gt;Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Monitoring Your Amazon SES Sending Activity&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that contains the event destination that you want to update.
    :type configuration_set_name: str
    :param event_destination: The event destination object that you want to apply to the specified configuration set.
    :type event_destination: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    event_destination = .from_dict(event_destination)
    return web.Response(status=200)


async def g_et_update_configuration_set_reputation_metrics_enabled(request: web.Request, configuration_set_name, enabled, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_configuration_set_reputation_metrics_enabled

    &lt;p&gt;Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given AWS Region. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using CloudWatch, you can create alarms when bounce or complaint rates exceed certain thresholds.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that you want to update.
    :type configuration_set_name: str
    :param enabled: Describes whether or not Amazon SES will publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.
    :type enabled: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_update_configuration_set_sending_enabled(request: web.Request, configuration_set_name, enabled, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_configuration_set_sending_enabled

    &lt;p&gt;Enables or disables email sending for messages sent using a specific configuration set in a given AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) exceed certain thresholds.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that you want to update.
    :type configuration_set_name: str
    :param enabled: Describes whether email sending is enabled or disabled for the configuration set. 
    :type enabled: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_update_configuration_set_tracking_options(request: web.Request, configuration_set_name, tracking_options, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_configuration_set_tracking_options

    &lt;p&gt;Modifies an association between a configuration set and a custom domain for open and click event tracking. &lt;/p&gt; &lt;p&gt;By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set for which you want to update the custom tracking domain.
    :type configuration_set_name: str
    :param tracking_options: 
    :type tracking_options: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    tracking_options = .from_dict(tracking_options)
    return web.Response(status=200)


async def g_et_update_custom_verification_email_template(request: web.Request, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, from_email_address=None, template_subject=None, template_content=None, success_redirection_url=None, failure_redirection_url=None) -> web.Response:
    """g_et_update_custom_verification_email_template

    &lt;p&gt;Updates an existing custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the custom verification email template that you want to update.
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param from_email_address: The email address that the custom verification email is sent from.
    :type from_email_address: str
    :param template_subject: The subject line of the custom verification email.
    :type template_subject: str
    :param template_content: The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html#custom-verification-emails-faq\&quot;&gt;Custom Verification Email Frequently Asked Questions&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.
    :type template_content: str
    :param success_redirection_url: The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
    :type success_redirection_url: str
    :param failure_redirection_url: The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
    :type failure_redirection_url: str

    """
    return web.Response(status=200)


async def g_et_update_receipt_rule(request: web.Request, rule_set_name, rule, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_receipt_rule

    &lt;p&gt;Updates a receipt rule.&lt;/p&gt; &lt;p&gt;For information about managing receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param rule_set_name: The name of the receipt rule set that the receipt rule belongs to.
    :type rule_set_name: str
    :param rule: A data structure that contains the updated receipt rule information.
    :type rule: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    rule = .from_dict(rule)
    return web.Response(status=200)


async def g_et_update_template(request: web.Request, template, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_template

    &lt;p&gt;Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template: 
    :type template: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    template = .from_dict(template)
    return web.Response(status=200)


async def g_et_verify_domain_dkim(request: web.Request, domain, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_verify_domain_dkim

    &lt;p&gt;Returns a set of DKIM tokens for a domain identity.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you execute the &lt;code&gt;VerifyDomainDkim&lt;/code&gt; operation, the domain that you specify is added to the list of identities that are associated with your account. This is true even if you haven&#39;t already associated the domain with your account by using the &lt;code&gt;VerifyDomainIdentity&lt;/code&gt; operation. However, you can&#39;t send email from the domain until you either successfully &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html\&quot;&gt;verify it&lt;/a&gt; or you successfully &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\&quot;&gt;set up DKIM for it&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You use the tokens that are generated by this operation to create CNAME records. When Amazon SES detects that you&#39;ve added these records to the DNS configuration for a domain, you can start sending email from that domain. You can start sending email even if you haven&#39;t added the TXT record provided by the VerifyDomainIdentity operation to the DNS configuration for your domain. All email that you send from the domain is authenticated using DKIM.&lt;/p&gt; &lt;p&gt;To create the CNAME records for DKIM authentication, use the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Name&lt;/b&gt;: &lt;i&gt;token&lt;/i&gt;._domainkey.&lt;i&gt;example.com&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Type&lt;/b&gt;: CNAME&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Value&lt;/b&gt;: &lt;i&gt;token&lt;/i&gt;.dkim.amazonses.com&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In the preceding example, replace &lt;i&gt;token&lt;/i&gt; with one of the tokens that are generated when you execute this operation. Replace &lt;i&gt;example.com&lt;/i&gt; with your domain. Repeat this process for each token that&#39;s generated by this operation.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param domain: The name of the domain to be verified for Easy DKIM signing.
    :type domain: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_verify_domain_identity(request: web.Request, domain, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_verify_domain_identity

    &lt;p&gt;Adds a domain to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. For more information about verifying domains, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param domain: The domain to be verified.
    :type domain: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_verify_email_address(request: web.Request, email_address, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_verify_email_address

    Deprecated. Use the &lt;code&gt;VerifyEmailIdentity&lt;/code&gt; operation to verify a new email address.

    :param email_address: The email address to be verified.
    :type email_address: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_verify_email_identity(request: web.Request, email_address, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_verify_email_identity

    &lt;p&gt;Adds an email address to the list of identities for your Amazon SES account in the current AWS region and attempts to verify it. As a result of executing this operation, a verification email is sent to the specified address.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param email_address: The email address to be verified.
    :type email_address: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_clone_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_clone_receipt_rule_set

    &lt;p&gt;Creates a receipt rule set by cloning an existing one. All receipt rules and configurations are copied to the new receipt rule set and are completely independent of the source rule set.&lt;/p&gt; &lt;p&gt;For information about setting up rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CloneReceiptRuleSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_configuration_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_configuration_set

    &lt;p&gt;Creates a configuration set.&lt;/p&gt; &lt;p&gt;Configuration sets enable you to publish email sending events. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateConfigurationSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_configuration_set_event_destination(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_configuration_set_event_destination

    &lt;p&gt;Creates a configuration set event destination.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you create or update an event destination, you must provide one, and only one, destination. The destination can be CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).&lt;/p&gt; &lt;/note&gt; &lt;p&gt;An event destination is the AWS service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateConfigurationSetEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_configuration_set_tracking_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_configuration_set_tracking_options

    &lt;p&gt;Creates an association between a configuration set and a custom domain for open and click event tracking. &lt;/p&gt; &lt;p&gt;By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateConfigurationSetTrackingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_custom_verification_email_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_custom_verification_email_template

    &lt;p&gt;Creates a new custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateCustomVerificationEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_receipt_filter(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_receipt_filter

    &lt;p&gt;Creates a new IP address filter.&lt;/p&gt; &lt;p&gt;For information about setting up IP address filters, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateReceiptFilterRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_receipt_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_receipt_rule

    &lt;p&gt;Creates a receipt rule.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateReceiptRuleRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_receipt_rule_set

    &lt;p&gt;Creates an empty receipt rule set.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateReceiptRuleSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_template

    &lt;p&gt;Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = CreateTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_configuration_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_configuration_set

    &lt;p&gt;Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteConfigurationSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_configuration_set_event_destination(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_configuration_set_event_destination

    &lt;p&gt;Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteConfigurationSetEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_configuration_set_tracking_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_configuration_set_tracking_options

    &lt;p&gt;Deletes an association between a configuration set and a custom domain for open and click event tracking.&lt;/p&gt; &lt;p&gt;By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Deleting this kind of association will result in emails sent using the specified configuration set to capture open and click events using the standard, Amazon SES-operated domains.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteConfigurationSetTrackingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_custom_verification_email_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_custom_verification_email_template

    &lt;p&gt;Deletes an existing custom verification email template. &lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteCustomVerificationEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_identity(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_identity

    &lt;p&gt;Deletes the specified identity (an email address or a domain) from the list of verified identities.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteIdentityRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_identity_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_identity_policy

    &lt;p&gt;Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteIdentityPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_receipt_filter(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_receipt_filter

    &lt;p&gt;Deletes the specified IP address filter.&lt;/p&gt; &lt;p&gt;For information about managing IP address filters, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-ip-filters.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteReceiptFilterRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_receipt_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_receipt_rule

    &lt;p&gt;Deletes the specified receipt rule.&lt;/p&gt; &lt;p&gt;For information about managing receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteReceiptRuleRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_receipt_rule_set

    &lt;p&gt;Deletes the specified receipt rule set and all of the receipt rules it contains.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The currently active rule set cannot be deleted.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteReceiptRuleSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_template

    &lt;p&gt;Deletes an email template.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_verified_email_address(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_verified_email_address

    Deprecated. Use the &lt;code&gt;DeleteIdentity&lt;/code&gt; operation to delete email addresses and domains.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DeleteVerifiedEmailAddressRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_active_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_active_receipt_rule_set

    &lt;p&gt;Returns the metadata and receipt rules for the receipt rule set that is currently active.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def p_ost_describe_configuration_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_configuration_set

    &lt;p&gt;Returns the details of the specified configuration set. For information about using configuration sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeConfigurationSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_receipt_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_receipt_rule

    &lt;p&gt;Returns the details of the specified receipt rule.&lt;/p&gt; &lt;p&gt;For information about setting up receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeReceiptRuleRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_receipt_rule_set

    &lt;p&gt;Returns the details of the specified receipt rule set.&lt;/p&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = DescribeReceiptRuleSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_account_sending_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_get_account_sending_enabled

    &lt;p&gt;Returns the email sending status of the Amazon SES account for the current region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_get_custom_verification_email_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_custom_verification_email_template

    &lt;p&gt;Returns the custom email verification template for the template name you specify.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetCustomVerificationEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_identity_dkim_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_identity_dkim_attributes

    &lt;p&gt;Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.&lt;/p&gt; &lt;p&gt;This operation takes a list of identities as input and returns the following information for each:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether Easy DKIM signing is enabled or disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Whether Amazon SES has successfully verified the DKIM tokens published in the domain&#39;s DNS. This information is only returned for domain name identities, not for email addresses.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time.&lt;/p&gt; &lt;p&gt;For more information about creating DNS records using DKIM tokens, go to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetIdentityDkimAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_identity_mail_from_domain_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_identity_mail_from_domain_attributes

    &lt;p&gt;Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).&lt;/p&gt; &lt;p&gt;This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetIdentityMailFromDomainAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_identity_notification_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_identity_notification_attributes

    &lt;p&gt;Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.&lt;/p&gt; &lt;p&gt;This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time.&lt;/p&gt; &lt;p&gt;For more information about using notifications with Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetIdentityNotificationAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_identity_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_identity_policies

    &lt;p&gt;Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetIdentityPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_identity_verification_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_identity_verification_attributes

    &lt;p&gt;Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.&lt;/p&gt; &lt;p&gt;The verification status of an email address is \&quot;Pending\&quot; until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to \&quot;Success\&quot;. If the link is not clicked within 24 hours, the verification status changes to \&quot;Failed.\&quot; In that case, if you still want to verify the email address, you must restart the verification process from the beginning.&lt;/p&gt; &lt;p&gt;For domain identities, the domain&#39;s verification status is \&quot;Pending\&quot; as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain&#39;s verification status changes to \&quot;Success\&quot;. If Amazon SES is unable to detect the record within 72 hours, the domain&#39;s verification status changes to \&quot;Failed.\&quot; In that case, if you still want to verify the domain, you must restart the verification process from the beginning.&lt;/p&gt; &lt;p&gt;This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetIdentityVerificationAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_send_quota(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_get_send_quota

    &lt;p&gt;Provides the sending limits for the Amazon SES account. &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_get_send_statistics(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_get_send_statistics

    &lt;p&gt;Provides sending statistics for the current AWS Region. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute period of time.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_get_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_template

    &lt;p&gt;Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = GetTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_configuration_sets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_configuration_sets

    &lt;p&gt;Provides a list of the configuration sets associated with your Amazon SES account in the current AWS Region. For information about using configuration sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Monitoring Your Amazon SES Sending Activity&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second. This operation will return up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation will also return a NextToken element. You can then execute the &lt;code&gt;ListConfigurationSets&lt;/code&gt; operation again, passing the &lt;code&gt;NextToken&lt;/code&gt; parameter and the value of the NextToken element to retrieve additional results.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListConfigurationSetsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_custom_verification_email_templates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_custom_verification_email_templates

    &lt;p&gt;Lists the existing custom verification email templates for your account in the current AWS Region.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListCustomVerificationEmailTemplatesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_identities(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_identities

    &lt;p&gt;Returns a list containing all of the identities (email addresses and domains) for your AWS account in the current AWS Region, regardless of verification status.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_items: Pagination limit
    :type max_items: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListIdentitiesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_identity_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_identity_policies

    &lt;p&gt;Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This API returns only a list. If you want the actual policy content, you can use &lt;code&gt;GetIdentityPolicies&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListIdentityPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_receipt_filters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_receipt_filters

    &lt;p&gt;Lists the IP address filters associated with your AWS account in the current AWS Region.&lt;/p&gt; &lt;p&gt;For information about managing IP address filters, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-ip-filters.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def p_ost_list_receipt_rule_sets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_receipt_rule_sets

    &lt;p&gt;Lists the receipt rule sets that exist under your AWS account in the current AWS Region. If there are additional receipt rule sets to be retrieved, you will receive a &lt;code&gt;NextToken&lt;/code&gt; that you can provide to the next call to &lt;code&gt;ListReceiptRuleSets&lt;/code&gt; to retrieve the additional entries.&lt;/p&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListReceiptRuleSetsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_templates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_templates

    &lt;p&gt;Lists the email templates present in your Amazon SES account in the current AWS Region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ListTemplatesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_verified_email_addresses(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_list_verified_email_addresses

    Deprecated. Use the &lt;code&gt;ListIdentities&lt;/code&gt; operation to list the email addresses and domains associated with your account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_put_configuration_set_delivery_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_configuration_set_delivery_options

    Adds or updates the delivery options for a configuration set.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutConfigurationSetDeliveryOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_identity_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_identity_policy

    &lt;p&gt;Adds or updates a sending authorization policy for the specified identity (an email address or a domain).&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = PutIdentityPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_reorder_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_reorder_receipt_rule_set

    &lt;p&gt;Reorders the receipt rules within a receipt rule set.&lt;/p&gt; &lt;note&gt; &lt;p&gt;All of the rules in the rule set must be represented in this request. That is, this API will return an error if the reorder request doesn&#39;t explicitly position all of the rules.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = ReorderReceiptRuleSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_send_bounce(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_send_bounce

    &lt;p&gt;Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this API on an email up to 24 hours after you receive it.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot use this API to send generic bounces for mail that was not received by Amazon SES.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about receiving email through Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SendBounceRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_send_bulk_templated_email(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_send_bulk_templated_email

    &lt;p&gt;Composes an email message to multiple destinations. The message body is created using an email template.&lt;/p&gt; &lt;p&gt;In order to send email using the &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt; operation, your call to the API must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The call must refer to an existing email template. You can create email templates using the &lt;a&gt;CreateTemplate&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message must be sent from a verified email address or domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each &lt;code&gt;Destination&lt;/code&gt; parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), the entire message will be rejected, even if the message contains other recipients that are valid.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt; operation several times to send the message to each group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of destinations you can contact in a single call to the API may be limited by your account&#39;s maximum sending rate.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SendBulkTemplatedEmailRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_send_custom_verification_email(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_send_custom_verification_email

    &lt;p&gt;Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.&lt;/p&gt; &lt;p&gt;To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SendCustomVerificationEmailRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_send_email(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_send_email

    &lt;p&gt;Composes an email message and immediately queues it for sending. In order to send email using the &lt;code&gt;SendEmail&lt;/code&gt; operation, your message must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation will result in an \&quot;Email address not verified\&quot; error. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), the entire message will be rejected, even if the message contains other recipients that are valid.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the &lt;code&gt;SendEmail&lt;/code&gt; operation several times to send the message to each group.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your &lt;i&gt;sending quota&lt;/i&gt;). For more information about sending quotas in Amazon SES, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-limits.html\&quot;&gt;Managing Your Amazon SES Sending Limits&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/important&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SendEmailRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_send_raw_email(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_send_raw_email

    &lt;p&gt;Composes an email message and immediately queues it for sending.&lt;/p&gt; &lt;p&gt;This operation is more flexible than the &lt;code&gt;SendEmail&lt;/code&gt; API operation. When you use the &lt;code&gt;SendRawEmail&lt;/code&gt; operation, you can specify the headers of the message as well as its content. This flexibility is useful, for example, when you want to send a multipart MIME email (such a message that contains both a text and an HTML version). You can also use this operation to send messages that include attachments.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;SendRawEmail&lt;/code&gt; operation has the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can only send email from &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;verified email addresses or domains&lt;/a&gt;. If you try to send email from an address that isn&#39;t verified, the operation results in an \&quot;Email address not verified\&quot; error.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html\&quot;&gt;Amazon SES sandbox&lt;/a&gt;, you can only send email to other verified addresses in your account, or to addresses that are associated with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mailbox-simulator.html\&quot;&gt;Amazon SES mailbox simulator&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size, including attachments, is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each message has to include at least one recipient address. A recipient address includes any address on the To:, CC:, or BCC: lines.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you send a single message to more than one recipient address, and one of the recipient addresses isn&#39;t in a valid format (that is, it&#39;s not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), Amazon SES rejects the entire message, even if the other addresses are valid.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each message can include up to 50 recipient addresses across the To:, CC:, or BCC: lines. If you need to send a single message to more than 50 recipients, you have to split the list of recipient addresses into groups of less than 50 recipients, and send separate messages to each group.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon SES allows you to specify 8-bit Content-Transfer-Encoding for MIME message parts. However, if Amazon SES has to modify the contents of your message (for example, if you use open and click tracking), 8-bit content isn&#39;t preserved. For this reason, we highly recommend that you encode all content that isn&#39;t 7-bit ASCII. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html#send-email-mime-encoding\&quot;&gt;MIME Encoding&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Additionally, keep the following considerations in mind when using the &lt;code&gt;SendRawEmail&lt;/code&gt; operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Although you can customize the message headers when using the &lt;code&gt;SendRawEmail&lt;/code&gt; operation, Amazon SES will automatically apply its own &lt;code&gt;Message-ID&lt;/code&gt; and &lt;code&gt;Date&lt;/code&gt; headers; if you passed these headers when creating the message, they will be overwritten by the values that Amazon SES provides.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are using sending authorization to send on behalf of another user, &lt;code&gt;SendRawEmail&lt;/code&gt; enables you to specify the cross-account identity for the email&#39;s Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters &lt;code&gt;SourceArn&lt;/code&gt;, &lt;code&gt;FromArn&lt;/code&gt;, and/or &lt;code&gt;ReturnPathArn&lt;/code&gt; to the API, or you can include the following X-headers in the header of your raw email:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;X-SES-SOURCE-ARN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;X-SES-FROM-ARN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;X-SES-RETURN-PATH-ARN&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;Don&#39;t include these X-headers in the DKIM signature. Amazon SES removes these before it sends the email.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you only specify the &lt;code&gt;SourceIdentityArn&lt;/code&gt; parameter, Amazon SES sets the From and Return-Path addresses to the same identity that you specified.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Using Sending Authorization with Amazon SES&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your &lt;i&gt;sending quota&lt;/i&gt;). For more information about sending quotas in Amazon SES, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-limits.html\&quot;&gt;Managing Your Amazon SES Sending Limits&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SendRawEmailRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_send_templated_email(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_send_templated_email

    &lt;p&gt;Composes an email message using an email template and immediately queues it for sending.&lt;/p&gt; &lt;p&gt;In order to send email using the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; operation, your call to the API must meet the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The call must refer to an existing email template. You can create email templates using the &lt;a&gt;CreateTemplate&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The message must be sent from a verified email address or domain.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The maximum message size is 10 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Calls to the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; operation may only include one &lt;code&gt;Destination&lt;/code&gt; parameter. A destination is a set of recipients who will receive the same version of the email. The &lt;code&gt;Destination&lt;/code&gt; parameter can include up to 50 recipients, across the To:, CC: and BCC: fields.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Destination&lt;/code&gt; parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format &lt;i&gt;UserName@[SubDomain.]Domain.TopLevelDomain&lt;/i&gt;), the entire message will be rejected, even if the message contains other recipients that are valid.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;If your call to the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; operation includes all of the required parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon SES can&#39;t render the email because the template contains errors, it doesn&#39;t send the email. Additionally, because it already accepted the message, Amazon SES doesn&#39;t return a message stating that it was unable to send the email.&lt;/p&gt; &lt;p&gt;For these reasons, we highly recommend that you set up Amazon SES to send you notifications when Rendering Failure events occur. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Sending Personalized Email Using the Amazon SES API&lt;/a&gt; in the &lt;i&gt;Amazon Simple Email Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SendTemplatedEmailRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_active_receipt_rule_set(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_active_receipt_rule_set

    &lt;p&gt;Sets the specified receipt rule set as the active receipt rule set.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To disable your email-receiving through Amazon SES completely, you can call this API with RuleSetName set to null.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about managing receipt rule sets, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetActiveReceiptRuleSetRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_identity_dkim_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_identity_dkim_enabled

    &lt;p&gt;Enables or disables Easy DKIM signing of email sent from an identity. If Easy DKIM signing is enabled for a domain, then Amazon SES uses DKIM to sign all email that it sends from addresses on that domain. If Easy DKIM signing is enabled for an email address, then Amazon SES uses DKIM to sign all email it sends from that address.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For email addresses (for example, &lt;code&gt;user@example.com&lt;/code&gt;), you can only enable DKIM signing if the corresponding domain (in this case, &lt;code&gt;example.com&lt;/code&gt;) has been set up to use Easy DKIM.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can enable DKIM signing for an identity at any time after you start the verification process for the identity, even if the verification process isn&#39;t complete. &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about Easy DKIM signing, go to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetIdentityDkimEnabledRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_identity_feedback_forwarding_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_identity_feedback_forwarding_enabled

    &lt;p&gt;Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Feedback forwarding does not apply to delivery notifications. Delivery notifications are only available through Amazon SNS.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about using notifications with Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetIdentityFeedbackForwardingEnabledRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_identity_headers_in_notifications_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_identity_headers_in_notifications_enabled

    &lt;p&gt;Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about using notifications with Amazon SES, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetIdentityHeadersInNotificationsEnabledRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_identity_mail_from_domain(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_identity_mail_from_domain

    &lt;p&gt;Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).&lt;/p&gt; &lt;important&gt; &lt;p&gt;To send emails using the specified MAIL FROM domain, you must add an MX record to your MAIL FROM domain&#39;s DNS settings. If you want your emails to pass Sender Policy Framework (SPF) checks, you must also add or update an SPF record. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetIdentityMailFromDomainRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_identity_notification_topic(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_identity_notification_topic

    &lt;p&gt;Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications. When you use this operation, you specify a verified identity, such as an email address or domain. When you send an email that uses the chosen identity in the Source field, Amazon SES sends notifications to the topic you specified. You can send bounce, complaint, or delivery notifications (or any combination of the three) to the Amazon SNS topic that you specify.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt; &lt;p&gt;For more information about feedback notification, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetIdentityNotificationTopicRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_receipt_rule_position(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_receipt_rule_position

    &lt;p&gt;Sets the position of the specified receipt rule in the receipt rule set.&lt;/p&gt; &lt;p&gt;For information about managing receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = SetReceiptRulePositionRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_test_render_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_test_render_template

    &lt;p&gt;Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = TestRenderTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_account_sending_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_account_sending_enabled

    &lt;p&gt;Enables or disables email sending across your entire Amazon SES account in the current AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account in a given AWS Region when reputation metrics (such as your bounce or complaint rates) reach certain thresholds.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateAccountSendingEnabledRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_configuration_set_event_destination(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_configuration_set_event_destination

    &lt;p&gt;Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\&quot;&gt;Monitoring Your Amazon SES Sending Activity&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateConfigurationSetEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_configuration_set_reputation_metrics_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_configuration_set_reputation_metrics_enabled

    &lt;p&gt;Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given AWS Region. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using CloudWatch, you can create alarms when bounce or complaint rates exceed certain thresholds.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateConfigurationSetReputationMetricsEnabledRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_configuration_set_sending_enabled(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_configuration_set_sending_enabled

    &lt;p&gt;Enables or disables email sending for messages sent using a specific configuration set in a given AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) exceed certain thresholds.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateConfigurationSetSendingEnabledRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_configuration_set_tracking_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_configuration_set_tracking_options

    &lt;p&gt;Modifies an association between a configuration set and a custom domain for open and click event tracking. &lt;/p&gt; &lt;p&gt;By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateConfigurationSetTrackingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_custom_verification_email_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_custom_verification_email_template

    &lt;p&gt;Updates an existing custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html\&quot;&gt;Using Custom Verification Email Templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateCustomVerificationEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_receipt_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_receipt_rule

    &lt;p&gt;Updates a receipt rule.&lt;/p&gt; &lt;p&gt;For information about managing receipt rules, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateReceiptRuleRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_template

    &lt;p&gt;Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = UpdateTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_verify_domain_dkim(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_verify_domain_dkim

    &lt;p&gt;Returns a set of DKIM tokens for a domain identity.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you execute the &lt;code&gt;VerifyDomainDkim&lt;/code&gt; operation, the domain that you specify is added to the list of identities that are associated with your account. This is true even if you haven&#39;t already associated the domain with your account by using the &lt;code&gt;VerifyDomainIdentity&lt;/code&gt; operation. However, you can&#39;t send email from the domain until you either successfully &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html\&quot;&gt;verify it&lt;/a&gt; or you successfully &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\&quot;&gt;set up DKIM for it&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;You use the tokens that are generated by this operation to create CNAME records. When Amazon SES detects that you&#39;ve added these records to the DNS configuration for a domain, you can start sending email from that domain. You can start sending email even if you haven&#39;t added the TXT record provided by the VerifyDomainIdentity operation to the DNS configuration for your domain. All email that you send from the domain is authenticated using DKIM.&lt;/p&gt; &lt;p&gt;To create the CNAME records for DKIM authentication, use the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Name&lt;/b&gt;: &lt;i&gt;token&lt;/i&gt;._domainkey.&lt;i&gt;example.com&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Type&lt;/b&gt;: CNAME&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Value&lt;/b&gt;: &lt;i&gt;token&lt;/i&gt;.dkim.amazonses.com&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In the preceding example, replace &lt;i&gt;token&lt;/i&gt; with one of the tokens that are generated when you execute this operation. Replace &lt;i&gt;example.com&lt;/i&gt; with your domain. Repeat this process for each token that&#39;s generated by this operation.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = VerifyDomainDkimRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_verify_domain_identity(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_verify_domain_identity

    &lt;p&gt;Adds a domain to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. For more information about verifying domains, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html\&quot;&gt;Verifying Email Addresses and Domains&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = VerifyDomainIdentityRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_verify_email_address(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_verify_email_address

    Deprecated. Use the &lt;code&gt;VerifyEmailIdentity&lt;/code&gt; operation to verify a new email address.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = VerifyEmailAddressRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_verify_email_identity(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_verify_email_identity

    &lt;p&gt;Adds an email address to the list of identities for your Amazon SES account in the current AWS region and attempts to verify it. As a result of executing this operation, a verification email is sent to the specified address.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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
    body = VerifyEmailIdentityRequest.from_dict(body)
    return web.Response(status=200)
