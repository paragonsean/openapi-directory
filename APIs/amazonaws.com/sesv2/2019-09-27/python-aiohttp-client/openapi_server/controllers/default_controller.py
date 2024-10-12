from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_get_metric_data_request import BatchGetMetricDataRequest
from openapi_server.models.batch_get_metric_data_response import BatchGetMetricDataResponse
from openapi_server.models.create_configuration_set_event_destination_request import CreateConfigurationSetEventDestinationRequest
from openapi_server.models.create_configuration_set_request import CreateConfigurationSetRequest
from openapi_server.models.create_contact_list_request import CreateContactListRequest
from openapi_server.models.create_contact_request import CreateContactRequest
from openapi_server.models.create_custom_verification_email_template_request import CreateCustomVerificationEmailTemplateRequest
from openapi_server.models.create_dedicated_ip_pool_request import CreateDedicatedIpPoolRequest
from openapi_server.models.create_deliverability_test_report_request import CreateDeliverabilityTestReportRequest
from openapi_server.models.create_deliverability_test_report_response import CreateDeliverabilityTestReportResponse
from openapi_server.models.create_email_identity_request import CreateEmailIdentityRequest
from openapi_server.models.create_email_identity_response import CreateEmailIdentityResponse
from openapi_server.models.create_email_template_request import CreateEmailTemplateRequest
from openapi_server.models.create_import_job_request import CreateImportJobRequest
from openapi_server.models.create_import_job_response import CreateImportJobResponse
from openapi_server.models.get_account_response import GetAccountResponse
from openapi_server.models.get_blacklist_reports_response import GetBlacklistReportsResponse
from openapi_server.models.get_configuration_set_event_destinations_response import GetConfigurationSetEventDestinationsResponse
from openapi_server.models.get_configuration_set_response import GetConfigurationSetResponse
from openapi_server.models.get_contact_list_response import GetContactListResponse
from openapi_server.models.get_contact_response import GetContactResponse
from openapi_server.models.get_custom_verification_email_template_response import GetCustomVerificationEmailTemplateResponse
from openapi_server.models.get_dedicated_ip_pool_response import GetDedicatedIpPoolResponse
from openapi_server.models.get_dedicated_ip_response import GetDedicatedIpResponse
from openapi_server.models.get_dedicated_ips_response import GetDedicatedIpsResponse
from openapi_server.models.get_deliverability_dashboard_options_response import GetDeliverabilityDashboardOptionsResponse
from openapi_server.models.get_deliverability_test_report_response import GetDeliverabilityTestReportResponse
from openapi_server.models.get_domain_deliverability_campaign_response import GetDomainDeliverabilityCampaignResponse
from openapi_server.models.get_domain_statistics_report_response import GetDomainStatisticsReportResponse
from openapi_server.models.get_email_identity_policies_response import GetEmailIdentityPoliciesResponse
from openapi_server.models.get_email_identity_response import GetEmailIdentityResponse
from openapi_server.models.get_email_template_response import GetEmailTemplateResponse
from openapi_server.models.get_import_job_response import GetImportJobResponse
from openapi_server.models.get_suppressed_destination_response import GetSuppressedDestinationResponse
from openapi_server.models.list_configuration_sets_response import ListConfigurationSetsResponse
from openapi_server.models.list_contact_lists_response import ListContactListsResponse
from openapi_server.models.list_contacts_request import ListContactsRequest
from openapi_server.models.list_contacts_response import ListContactsResponse
from openapi_server.models.list_custom_verification_email_templates_response import ListCustomVerificationEmailTemplatesResponse
from openapi_server.models.list_dedicated_ip_pools_response import ListDedicatedIpPoolsResponse
from openapi_server.models.list_deliverability_test_reports_response import ListDeliverabilityTestReportsResponse
from openapi_server.models.list_domain_deliverability_campaigns_response import ListDomainDeliverabilityCampaignsResponse
from openapi_server.models.list_email_identities_response import ListEmailIdentitiesResponse
from openapi_server.models.list_email_templates_response import ListEmailTemplatesResponse
from openapi_server.models.list_import_jobs_request import ListImportJobsRequest
from openapi_server.models.list_import_jobs_response import ListImportJobsResponse
from openapi_server.models.list_recommendations_request import ListRecommendationsRequest
from openapi_server.models.list_recommendations_response import ListRecommendationsResponse
from openapi_server.models.list_suppressed_destinations_response import ListSuppressedDestinationsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_account_dedicated_ip_warmup_attributes_request import PutAccountDedicatedIpWarmupAttributesRequest
from openapi_server.models.put_account_details_request import PutAccountDetailsRequest
from openapi_server.models.put_account_sending_attributes_request import PutAccountSendingAttributesRequest
from openapi_server.models.put_account_suppression_attributes_request import PutAccountSuppressionAttributesRequest
from openapi_server.models.put_account_vdm_attributes_request import PutAccountVdmAttributesRequest
from openapi_server.models.put_configuration_set_delivery_options_request import PutConfigurationSetDeliveryOptionsRequest
from openapi_server.models.put_configuration_set_reputation_options_request import PutConfigurationSetReputationOptionsRequest
from openapi_server.models.put_configuration_set_sending_options_request import PutConfigurationSetSendingOptionsRequest
from openapi_server.models.put_configuration_set_suppression_options_request import PutConfigurationSetSuppressionOptionsRequest
from openapi_server.models.put_configuration_set_tracking_options_request import PutConfigurationSetTrackingOptionsRequest
from openapi_server.models.put_configuration_set_vdm_options_request import PutConfigurationSetVdmOptionsRequest
from openapi_server.models.put_dedicated_ip_in_pool_request import PutDedicatedIpInPoolRequest
from openapi_server.models.put_dedicated_ip_pool_scaling_attributes_request import PutDedicatedIpPoolScalingAttributesRequest
from openapi_server.models.put_dedicated_ip_warmup_attributes_request import PutDedicatedIpWarmupAttributesRequest
from openapi_server.models.put_deliverability_dashboard_option_request import PutDeliverabilityDashboardOptionRequest
from openapi_server.models.put_email_identity_configuration_set_attributes_request import PutEmailIdentityConfigurationSetAttributesRequest
from openapi_server.models.put_email_identity_dkim_attributes_request import PutEmailIdentityDkimAttributesRequest
from openapi_server.models.put_email_identity_dkim_signing_attributes_request import PutEmailIdentityDkimSigningAttributesRequest
from openapi_server.models.put_email_identity_dkim_signing_attributes_response import PutEmailIdentityDkimSigningAttributesResponse
from openapi_server.models.put_email_identity_feedback_attributes_request import PutEmailIdentityFeedbackAttributesRequest
from openapi_server.models.put_email_identity_mail_from_attributes_request import PutEmailIdentityMailFromAttributesRequest
from openapi_server.models.put_suppressed_destination_request import PutSuppressedDestinationRequest
from openapi_server.models.send_bulk_email_request import SendBulkEmailRequest
from openapi_server.models.send_bulk_email_response import SendBulkEmailResponse
from openapi_server.models.send_custom_verification_email_request import SendCustomVerificationEmailRequest
from openapi_server.models.send_custom_verification_email_response import SendCustomVerificationEmailResponse
from openapi_server.models.send_email_request import SendEmailRequest
from openapi_server.models.send_email_response import SendEmailResponse
from openapi_server.models.suppression_list_reason import SuppressionListReason
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.test_render_email_template_request import TestRenderEmailTemplateRequest
from openapi_server.models.test_render_email_template_response import TestRenderEmailTemplateResponse
from openapi_server.models.update_configuration_set_event_destination_request import UpdateConfigurationSetEventDestinationRequest
from openapi_server.models.update_contact_list_request import UpdateContactListRequest
from openapi_server.models.update_contact_request import UpdateContactRequest
from openapi_server.models.update_custom_verification_email_template_request import UpdateCustomVerificationEmailTemplateRequest
from openapi_server.models.update_email_identity_policy_request import UpdateEmailIdentityPolicyRequest
from openapi_server.models.update_email_template_request import UpdateEmailTemplateRequest
from openapi_server import util


async def batch_get_metric_data(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_metric_data

    &lt;p&gt;Retrieves batches of metric data collected based on your sending activity.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than 16 times per second, and with at most 160 queries from the batches per second (cumulative).&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchGetMetricDataRequest.from_dict(body)
    return web.Response(status=200)


async def create_configuration_set(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_configuration_set

    Create a configuration set. &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails that you send. You apply a configuration set to an email by specifying the name of the configuration set when you call the Amazon SES API v2. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateConfigurationSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_configuration_set_event_destination(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_configuration_set_event_destination

    &lt;p&gt;Create an event destination. &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt; &lt;p&gt;A single configuration set can include more than one event destination.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set .
    :type configuration_set_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateConfigurationSetEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def create_contact(request: web.Request, contact_list_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_contact

    Creates a contact, which is an end-user who is receiving the email, and adds them to a contact list.

    :param contact_list_name: The name of the contact list to which the contact should be added.
    :type contact_list_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateContactRequest.from_dict(body)
    return web.Response(status=200)


async def create_contact_list(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_contact_list

    Creates a contact list.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateContactListRequest.from_dict(body)
    return web.Response(status=200)


async def create_custom_verification_email_template(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_custom_verification_email_template

    &lt;p&gt;Creates a new custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateCustomVerificationEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_dedicated_ip_pool(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_dedicated_ip_pool

    Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Web Services account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, the message is sent from one of the addresses in the associated pool.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDedicatedIpPoolRequest.from_dict(body)
    return web.Response(status=200)


async def create_deliverability_test_report(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_deliverability_test_report

    Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon SES then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the &lt;code&gt;GetDeliverabilityTestReport&lt;/code&gt; operation to view the results of the test.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDeliverabilityTestReportRequest.from_dict(body)
    return web.Response(status=200)


async def create_email_identity(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_email_identity

    &lt;p&gt;Starts the process of verifying an email identity. An &lt;i&gt;identity&lt;/i&gt; is an email address or domain that you use when you send email. Before you can use an identity to send email, you first have to verify it. By verifying an identity, you demonstrate that you&#39;re the owner of the identity, and that you&#39;ve given Amazon SES API v2 permission to send email from the identity.&lt;/p&gt; &lt;p&gt;When you verify an email address, Amazon SES sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. &lt;/p&gt; &lt;p&gt;When you verify a domain without specifying the &lt;code&gt;DkimSigningAttributes&lt;/code&gt; object, this operation provides a set of DKIM tokens. You can convert these tokens into CNAME records, which you then add to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. This verification method is known as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\&quot;&gt;Easy DKIM&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Alternatively, you can perform the verification process by providing your own public-private key pair. This verification method is known as Bring Your Own DKIM (BYODKIM). To use BYODKIM, your call to the &lt;code&gt;CreateEmailIdentity&lt;/code&gt; operation has to include the &lt;code&gt;DkimSigningAttributes&lt;/code&gt; object. When you specify this object, you provide a selector (a component of the DNS record name that identifies the public key to use for DKIM authentication) and a private key.&lt;/p&gt; &lt;p&gt;When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. For some DNS providers, it can take 72 hours or more to complete the domain verification process.&lt;/p&gt; &lt;p&gt;Additionally, you can associate an existing configuration set with the email identity that you&#39;re verifying.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEmailIdentityRequest.from_dict(body)
    return web.Response(status=200)


async def create_email_identity_policy(request: web.Request, email_identity, policy_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_email_identity_policy

    &lt;p&gt;Creates the specified sending authorization policy for the given identity (an email address or a domain).&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param email_identity: The email identity.
    :type email_identity: str
    :param policy_name: &lt;p&gt;The name of the policy.&lt;/p&gt; &lt;p&gt;The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.&lt;/p&gt;
    :type policy_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEmailIdentityPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_email_template(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_email_template

    &lt;p&gt;Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_import_job(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_import_job

    Creates an import job for a data destination.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_configuration_set(request: web.Request, configuration_set_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_configuration_set

    &lt;p&gt;Delete an existing configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set.
    :type configuration_set_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_configuration_set_event_destination(request: web.Request, configuration_set_name, event_destination_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_configuration_set_event_destination

    &lt;p&gt;Delete an event destination.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that contains the event destination to delete.
    :type configuration_set_name: str
    :param event_destination_name: The name of the event destination to delete.
    :type event_destination_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_contact(request: web.Request, contact_list_name, email_address, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_contact

    Removes a contact from a contact list.

    :param contact_list_name: The name of the contact list from which the contact should be removed.
    :type contact_list_name: str
    :param email_address: The contact&#39;s email address.
    :type email_address: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_contact_list(request: web.Request, contact_list_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_contact_list

    Deletes a contact list and all of the contacts on that list.

    :param contact_list_name: The name of the contact list.
    :type contact_list_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_custom_verification_email_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_custom_verification_email_template

    &lt;p&gt;Deletes an existing custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the custom verification email template that you want to delete.
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

    """
    return web.Response(status=200)


async def delete_dedicated_ip_pool(request: web.Request, pool_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_dedicated_ip_pool

    Delete a dedicated IP pool.

    :param pool_name: The name of the dedicated IP pool that you want to delete.
    :type pool_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_email_identity(request: web.Request, email_identity, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_email_identity

    Deletes an email identity. An identity can be either an email address or a domain name.

    :param email_identity: The identity (that is, the email address or domain) to delete.
    :type email_identity: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_email_identity_policy(request: web.Request, email_identity, policy_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_email_identity_policy

    &lt;p&gt;Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param email_identity: The email identity.
    :type email_identity: str
    :param policy_name: &lt;p&gt;The name of the policy.&lt;/p&gt; &lt;p&gt;The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.&lt;/p&gt;
    :type policy_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_email_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_email_template

    &lt;p&gt;Deletes an email template.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the template to be deleted.
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

    """
    return web.Response(status=200)


async def delete_suppressed_destination(request: web.Request, email_address, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_suppressed_destination

    Removes an email address from the suppression list for your account.

    :param email_address: The suppressed email destination to remove from the account suppression list.
    :type email_address: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account

    Obtain information about the email-sending status and capabilities of your Amazon SES account in the current Amazon Web Services Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_blacklist_reports(request: web.Request, blacklist_item_names, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_blacklist_reports

    Retrieve a list of the blacklists that your dedicated IP addresses appear on.

    :param blacklist_item_names: A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon SES or Amazon Pinpoint.
    :type blacklist_item_names: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_configuration_set(request: web.Request, configuration_set_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_configuration_set

    &lt;p&gt;Get information about an existing configuration set, including the dedicated IP pool that it&#39;s associated with, whether or not it&#39;s enabled for sending email, and more.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set.
    :type configuration_set_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_configuration_set_event_destinations(request: web.Request, configuration_set_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_configuration_set_event_destinations

    &lt;p&gt;Retrieve a list of event destinations that are associated with a configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that contains the event destination.
    :type configuration_set_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_contact(request: web.Request, contact_list_name, email_address, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_contact

    Returns a contact from a contact list.

    :param contact_list_name: The name of the contact list to which the contact belongs.
    :type contact_list_name: str
    :param email_address: The contact&#39;s email address.
    :type email_address: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_contact_list(request: web.Request, contact_list_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_contact_list

    Returns contact list metadata. It does not return any information about the contacts present in the list.

    :param contact_list_name: The name of the contact list.
    :type contact_list_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_custom_verification_email_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_custom_verification_email_template

    &lt;p&gt;Returns the custom email verification template for the template name you specify.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the custom verification email template that you want to retrieve.
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

    """
    return web.Response(status=200)


async def get_dedicated_ip(request: web.Request, ip, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dedicated_ip

    Get information about a dedicated IP address, including the name of the dedicated IP pool that it&#39;s associated with, as well information about the automatic warm-up process for the address.

    :param ip: The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that&#39;s assocaited with your Amazon Web Services account.
    :type ip: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_dedicated_ip_pool(request: web.Request, pool_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dedicated_ip_pool

    Retrieve information about the dedicated pool.

    :param pool_name: The name of the dedicated IP pool to retrieve.
    :type pool_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_dedicated_ips(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, pool_name=None, next_token=None, page_size=None) -> web.Response:
    """get_dedicated_ips

    List the dedicated IP addresses that are associated with your Amazon Web Services account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param pool_name: The name of the IP pool that the dedicated IP address is associated with.
    :type pool_name: str
    :param next_token: A token returned from a previous call to &lt;code&gt;GetDedicatedIps&lt;/code&gt; to indicate the position of the dedicated IP pool in the list of IP pools.
    :type next_token: str
    :param page_size: The number of results to show in a single call to &lt;code&gt;GetDedicatedIpsRequest&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_deliverability_dashboard_options(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_deliverability_dashboard_options

    &lt;p&gt;Retrieve information about the status of the Deliverability dashboard for your account. When the Deliverability dashboard is enabled, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other Amazon Web Services services. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/ses/pricing/\&quot;&gt;Amazon SES Pricing&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_deliverability_test_report(request: web.Request, report_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_deliverability_test_report

    Retrieve the results of a predictive inbox placement test.

    :param report_id: A unique string that identifies the predictive inbox placement test.
    :type report_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_domain_deliverability_campaign(request: web.Request, campaign_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_domain_deliverability_campaign

    Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for.

    :param campaign_id: The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.
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


async def get_domain_statistics_report(request: web.Request, domain, start_date, end_date, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_domain_statistics_report

    Retrieve inbox placement and engagement rates for the domains that you use to send email.

    :param domain: The domain that you want to obtain deliverability metrics for.
    :type domain: str
    :param start_date: The first day (in Unix time) that you want to obtain domain deliverability metrics for.
    :type start_date: str
    :param end_date: The last day (in Unix time) that you want to obtain domain deliverability metrics for. The &lt;code&gt;EndDate&lt;/code&gt; that you specify has to be less than or equal to 30 days after the &lt;code&gt;StartDate&lt;/code&gt;.
    :type end_date: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def get_email_identity(request: web.Request, email_identity, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_email_identity

    Provides information about a specific identity, including the identity&#39;s verification status, sending authorization policies, its DKIM authentication status, and its custom Mail-From settings.

    :param email_identity: The email identity.
    :type email_identity: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_email_identity_policies(request: web.Request, email_identity, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_email_identity_policies

    &lt;p&gt;Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param email_identity: The email identity.
    :type email_identity: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_email_template(request: web.Request, template_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_email_template

    &lt;p&gt;Displays the template object (which includes the subject line, HTML part and text part) for the template you specify.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the template.
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

    """
    return web.Response(status=200)


async def get_import_job(request: web.Request, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_import_job

    Provides information about an import job.

    :param job_id: The ID of the import job.
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


async def get_suppressed_destination(request: web.Request, email_address, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_suppressed_destination

    Retrieves information about a specific email address that&#39;s on the suppression list for your account.

    :param email_address: The email address that&#39;s on the account suppression list.
    :type email_address: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_configuration_sets(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_configuration_sets

    &lt;p&gt;List all of the configuration sets associated with your account in the current region.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListConfigurationSets&lt;/code&gt; to indicate the position in the list of configuration sets.
    :type next_token: str
    :param page_size: The number of results to show in a single call to &lt;code&gt;ListConfigurationSets&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.
    :type page_size: int

    """
    return web.Response(status=200)


async def list_contact_lists(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, next_token=None) -> web.Response:
    """list_contact_lists

    Lists all of the contact lists available.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Maximum number of contact lists to return at once. Use this parameter to paginate results. If additional contact lists exist beyond the specified limit, the &lt;code&gt;NextToken&lt;/code&gt; element is sent in the response. Use the &lt;code&gt;NextToken&lt;/code&gt; value in subsequent requests to retrieve additional lists.
    :type page_size: int
    :param next_token: A string token indicating that there might be additional contact lists available to be listed. Use the token provided in the Response to use in the subsequent call to ListContactLists with the same parameters to retrieve the next page of contact lists.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_contacts(request: web.Request, contact_list_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, next_token=None) -> web.Response:
    """list_contacts

    Lists the contacts present in a specific contact list.

    :param contact_list_name: The name of the contact list.
    :type contact_list_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: The number of contacts that may be returned at once, which is dependent on if there are more or less contacts than the value of the PageSize. Use this parameter to paginate results. If additional contacts exist beyond the specified limit, the &lt;code&gt;NextToken&lt;/code&gt; element is sent in the response. Use the &lt;code&gt;NextToken&lt;/code&gt; value in subsequent requests to retrieve additional contacts.
    :type page_size: int
    :param next_token: A string token indicating that there might be additional contacts available to be listed. Use the token provided in the Response to use in the subsequent call to ListContacts with the same parameters to retrieve the next page of contacts.
    :type next_token: str

    """
    body = ListContactsRequest.from_dict(body)
    return web.Response(status=200)


async def list_custom_verification_email_templates(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_custom_verification_email_templates

    &lt;p&gt;Lists the existing custom verification email templates for your account in the current Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListCustomVerificationEmailTemplates&lt;/code&gt; to indicate the position in the list of custom verification email templates.
    :type next_token: str
    :param page_size: &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListCustomVerificationEmailTemplates&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 1, and can be no more than 50.&lt;/p&gt;
    :type page_size: int

    """
    return web.Response(status=200)


async def list_dedicated_ip_pools(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_dedicated_ip_pools

    List all of the dedicated IP pools that exist in your Amazon Web Services account in the current Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListDedicatedIpPools&lt;/code&gt; to indicate the position in the list of dedicated IP pools.
    :type next_token: str
    :param page_size: The number of results to show in a single call to &lt;code&gt;ListDedicatedIpPools&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.
    :type page_size: int

    """
    return web.Response(status=200)


async def list_deliverability_test_reports(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_deliverability_test_reports

    Show a list of the predictive inbox placement tests that you&#39;ve performed, regardless of their statuses. For predictive inbox placement tests that are complete, you can use the &lt;code&gt;GetDeliverabilityTestReport&lt;/code&gt; operation to view the results.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListDeliverabilityTestReports&lt;/code&gt; to indicate the position in the list of predictive inbox placement tests.
    :type next_token: str
    :param page_size: &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListDeliverabilityTestReports&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 0, and can be no more than 1000.&lt;/p&gt;
    :type page_size: int

    """
    return web.Response(status=200)


async def list_domain_deliverability_campaigns(request: web.Request, start_date, end_date, subscribed_domain, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_domain_deliverability_campaigns

    Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range. This data is available for a domain only if you enabled the Deliverability dashboard for the domain.

    :param start_date: The first day that you want to obtain deliverability data for.
    :type start_date: str
    :param end_date: The last day that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the &lt;code&gt;StartDate&lt;/code&gt; parameter.
    :type end_date: str
    :param subscribed_domain: The domain to obtain deliverability data for.
    :type subscribed_domain: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token that’s returned from a previous call to the &lt;code&gt;ListDomainDeliverabilityCampaigns&lt;/code&gt; operation. This token indicates the position of a campaign in the list of campaigns.
    :type next_token: str
    :param page_size: The maximum number of results to include in response to a single call to the &lt;code&gt;ListDomainDeliverabilityCampaigns&lt;/code&gt; operation. If the number of results is larger than the number that you specify in this parameter, the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.
    :type page_size: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def list_email_identities(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_email_identities

    Returns a list of all of the email identities that are associated with your Amazon Web Services account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren&#39;t. This operation returns identities that are associated with Amazon SES and Amazon Pinpoint.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListEmailIdentities&lt;/code&gt; to indicate the position in the list of identities.
    :type next_token: str
    :param page_size: &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListEmailIdentities&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 0, and can be no more than 1000.&lt;/p&gt;
    :type page_size: int

    """
    return web.Response(status=200)


async def list_email_templates(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_email_templates

    &lt;p&gt;Lists the email templates present in your Amazon SES account in the current Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListEmailTemplates&lt;/code&gt; to indicate the position in the list of email templates.
    :type next_token: str
    :param page_size: &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListEmailTemplates&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 1, and can be no more than 10.&lt;/p&gt;
    :type page_size: int

    """
    return web.Response(status=200)


async def list_import_jobs(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_import_jobs

    Lists all of the import jobs.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to &lt;code&gt;ListImportJobs&lt;/code&gt; with the same parameters to retrieve the next page of import jobs.
    :type next_token: str
    :param page_size: Maximum number of import jobs to return at once. Use this parameter to paginate results. If additional import jobs exist beyond the specified limit, the &lt;code&gt;NextToken&lt;/code&gt; element is sent in the response. Use the &lt;code&gt;NextToken&lt;/code&gt; value in subsequent requests to retrieve additional addresses.
    :type page_size: int

    """
    body = ListImportJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_recommendations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, next_token=None) -> web.Response:
    """list_recommendations

    &lt;p&gt;Lists the recommendations present in your Amazon SES account in the current Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_suppressed_destinations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, reason=None, start_date=None, end_date=None, next_token=None, page_size=None) -> web.Response:
    """list_suppressed_destinations

    Retrieves a list of email addresses that are on the suppression list for your account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param reason: The factors that caused the email address to be added to .
    :type reason: list | bytes
    :param start_date: Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list after a specific date.
    :type start_date: str
    :param end_date: Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list before a specific date.
    :type end_date: str
    :param next_token: A token returned from a previous call to &lt;code&gt;ListSuppressedDestinations&lt;/code&gt; to indicate the position in the list of suppressed email addresses.
    :type next_token: str
    :param page_size: The number of results to show in a single call to &lt;code&gt;ListSuppressedDestinations&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.
    :type page_size: int

    """
    reason = [SuppressionListReason.from_dict(d) for d in reason]
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Retrieve a list of the tags (keys and values) that are associated with a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource. Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an optional associated &lt;i&gt;tag value&lt;/i&gt;. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to retrieve tag information for.
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


async def put_account_dedicated_ip_warmup_attributes(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_dedicated_ip_warmup_attributes

    Enable or disable the automatic warm-up feature for dedicated IP addresses.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountDedicatedIpWarmupAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_details(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_details

    Update your Amazon SES account details.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_sending_attributes(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_sending_attributes

    Enable or disable the ability of your account to send email.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountSendingAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_suppression_attributes(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_suppression_attributes

    Change the settings for the account-level suppression list.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountSuppressionAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_vdm_attributes(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_vdm_attributes

    &lt;p&gt;Update your Amazon SES account VDM attributes.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountVdmAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_configuration_set_delivery_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_delivery_options

    Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.

    :param configuration_set_name: The name of the configuration set to associate with a dedicated IP pool.
    :type configuration_set_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutConfigurationSetDeliveryOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_configuration_set_reputation_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_reputation_options

    Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific Amazon Web Services Region.

    :param configuration_set_name: The name of the configuration set.
    :type configuration_set_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutConfigurationSetReputationOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_configuration_set_sending_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_sending_options

    Enable or disable email sending for messages that use a particular configuration set in a specific Amazon Web Services Region.

    :param configuration_set_name: The name of the configuration set to enable or disable email sending for.
    :type configuration_set_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutConfigurationSetSendingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_configuration_set_suppression_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_suppression_options

    Specify the account suppression list preferences for a configuration set.

    :param configuration_set_name: The name of the configuration set to change the suppression list preferences for.
    :type configuration_set_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutConfigurationSetSuppressionOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_configuration_set_tracking_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_tracking_options

    Specify a custom domain to use for open and click tracking elements in email that you send.

    :param configuration_set_name: The name of the configuration set.
    :type configuration_set_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutConfigurationSetTrackingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_configuration_set_vdm_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_vdm_options

    &lt;p&gt;Specify VDM preferences for email that you send using the configuration set.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set.
    :type configuration_set_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutConfigurationSetVdmOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_dedicated_ip_in_pool(request: web.Request, ip, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_dedicated_ip_in_pool

    &lt;p&gt;Move a dedicated IP address to an existing dedicated IP pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The dedicated IP address that you specify must already exist, and must be associated with your Amazon Web Services account. &lt;/p&gt; &lt;p&gt;The dedicated IP pool you specify must already exist. You can create a new pool by using the &lt;code&gt;CreateDedicatedIpPool&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt;

    :param ip: The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that&#39;s associated with your Amazon Web Services account.
    :type ip: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutDedicatedIpInPoolRequest.from_dict(body)
    return web.Response(status=200)


async def put_dedicated_ip_pool_scaling_attributes(request: web.Request, pool_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_dedicated_ip_pool_scaling_attributes

    &lt;p&gt;Used to convert a dedicated IP pool to a different scaling mode.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;MANAGED&lt;/code&gt; pools cannot be converted to &lt;code&gt;STANDARD&lt;/code&gt; scaling mode.&lt;/p&gt; &lt;/note&gt;

    :param pool_name: The name of the dedicated IP pool.
    :type pool_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutDedicatedIpPoolScalingAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_dedicated_ip_warmup_attributes(request: web.Request, ip, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_dedicated_ip_warmup_attributes

    &lt;p/&gt;

    :param ip: The dedicated IP address that you want to update the warm-up attributes for.
    :type ip: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutDedicatedIpWarmupAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_deliverability_dashboard_option(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_deliverability_dashboard_option

    &lt;p&gt;Enable or disable the Deliverability dashboard. When you enable the Deliverability dashboard, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other Amazon Web Services services. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/ses/pricing/\&quot;&gt;Amazon SES Pricing&lt;/a&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutDeliverabilityDashboardOptionRequest.from_dict(body)
    return web.Response(status=200)


async def put_email_identity_configuration_set_attributes(request: web.Request, email_identity, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_email_identity_configuration_set_attributes

    Used to associate a configuration set with an email identity.

    :param email_identity: The email address or domain to associate with a configuration set.
    :type email_identity: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEmailIdentityConfigurationSetAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_email_identity_dkim_attributes(request: web.Request, email_identity, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_email_identity_dkim_attributes

    Used to enable or disable DKIM authentication for an email identity.

    :param email_identity: The email identity.
    :type email_identity: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEmailIdentityDkimAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_email_identity_dkim_signing_attributes(request: web.Request, email_identity, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_email_identity_dkim_signing_attributes

    &lt;p&gt;Used to configure or change the DKIM authentication settings for an email domain identity. You can use this operation to do any of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update the signing attributes for an identity that uses Bring Your Own DKIM (BYODKIM).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the key length that should be used for Easy DKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using no DKIM authentication to using Easy DKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using no DKIM authentication to using BYODKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using Easy DKIM to using BYODKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using BYODKIM to using Easy DKIM.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param email_identity: The email identity.
    :type email_identity: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEmailIdentityDkimSigningAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_email_identity_feedback_attributes(request: web.Request, email_identity, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_email_identity_feedback_attributes

    &lt;p&gt;Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.&lt;/p&gt; &lt;p&gt;If the value is &lt;code&gt;true&lt;/code&gt;, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the &lt;code&gt;Return-Path&lt;/code&gt; header of the original email.&lt;/p&gt; &lt;p&gt;You&#39;re required to have a method of tracking bounces and complaints. If you haven&#39;t set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).&lt;/p&gt;

    :param email_identity: The email identity.
    :type email_identity: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEmailIdentityFeedbackAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_email_identity_mail_from_attributes(request: web.Request, email_identity, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_email_identity_mail_from_attributes

    Used to enable or disable the custom Mail-From domain configuration for an email identity.

    :param email_identity: The verified email identity.
    :type email_identity: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutEmailIdentityMailFromAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_suppressed_destination(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_suppressed_destination

    Adds an email address to the suppression list for your account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutSuppressedDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def send_bulk_email(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_bulk_email

    Composes an email message to multiple destinations.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SendBulkEmailRequest.from_dict(body)
    return web.Response(status=200)


async def send_custom_verification_email(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_custom_verification_email

    &lt;p&gt;Adds an email address to the list of identities for your Amazon SES account in the current Amazon Web Services Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.&lt;/p&gt; &lt;p&gt;To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SendCustomVerificationEmailRequest.from_dict(body)
    return web.Response(status=200)


async def send_email(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_email

    &lt;p&gt;Sends an email message. You can use the Amazon SES API v2 to send the following types of messages:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Simple&lt;/b&gt; – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon SES assembles the message for you.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Raw&lt;/b&gt; – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Templated&lt;/b&gt; – A message that contains personalization tags. When you send this type of email, Amazon SES API v2 automatically replaces the tags with values that you specify.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SendEmailRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Add one or more tags (keys and values) to a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.&lt;/p&gt; &lt;p&gt;Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an associated &lt;i&gt;tag value&lt;/i&gt;, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def test_render_email_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """test_render_email_template

    &lt;p&gt;Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the template.
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
    body = TestRenderEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Remove one or more tags (keys and values) from a specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.
    :type resource_arn: str
    :param tag_keys: &lt;p&gt;The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.&lt;/p&gt; &lt;p&gt;To remove more than one tag from the resource, append the &lt;code&gt;TagKeys&lt;/code&gt; parameter and argument for each additional tag to remove, separated by an ampersand. For example: &lt;code&gt;/v2/email/tags?ResourceArn&#x3D;ResourceArn&amp;amp;TagKeys&#x3D;Key1&amp;amp;TagKeys&#x3D;Key2&lt;/code&gt; &lt;/p&gt;
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


async def update_configuration_set_event_destination(request: web.Request, configuration_set_name, event_destination_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_configuration_set_event_destination

    &lt;p&gt;Update the configuration of an event destination for a configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that contains the event destination to modify.
    :type configuration_set_name: str
    :param event_destination_name: The name of the event destination.
    :type event_destination_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateConfigurationSetEventDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def update_contact(request: web.Request, contact_list_name, email_address, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact

    Updates a contact&#39;s preferences for a list. It is not necessary to specify all existing topic preferences in the TopicPreferences object, just the ones that need updating.

    :param contact_list_name: The name of the contact list.
    :type contact_list_name: str
    :param email_address: The contact&#39;s email address.
    :type email_address: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def update_contact_list(request: web.Request, contact_list_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_contact_list

    Updates contact list metadata. This operation does a complete replacement.

    :param contact_list_name: The name of the contact list.
    :type contact_list_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContactListRequest.from_dict(body)
    return web.Response(status=200)


async def update_custom_verification_email_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_custom_verification_email_template

    &lt;p&gt;Updates an existing custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the custom verification email template that you want to update.
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
    body = UpdateCustomVerificationEmailTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_email_identity_policy(request: web.Request, email_identity, policy_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_email_identity_policy

    &lt;p&gt;Updates the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param email_identity: The email identity.
    :type email_identity: str
    :param policy_name: &lt;p&gt;The name of the policy.&lt;/p&gt; &lt;p&gt;The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.&lt;/p&gt;
    :type policy_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEmailIdentityPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_email_template(request: web.Request, template_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_email_template

    &lt;p&gt;Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

    :param template_name: The name of the template.
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
