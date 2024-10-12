from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_configuration_set_event_destination_request import CreateConfigurationSetEventDestinationRequest
from openapi_server.models.create_configuration_set_request import CreateConfigurationSetRequest
from openapi_server.models.create_dedicated_ip_pool_request import CreateDedicatedIpPoolRequest
from openapi_server.models.create_deliverability_test_report_request import CreateDeliverabilityTestReportRequest
from openapi_server.models.create_deliverability_test_report_response import CreateDeliverabilityTestReportResponse
from openapi_server.models.create_email_identity_request import CreateEmailIdentityRequest
from openapi_server.models.create_email_identity_response import CreateEmailIdentityResponse
from openapi_server.models.get_account_response import GetAccountResponse
from openapi_server.models.get_blacklist_reports_response import GetBlacklistReportsResponse
from openapi_server.models.get_configuration_set_event_destinations_response import GetConfigurationSetEventDestinationsResponse
from openapi_server.models.get_configuration_set_response import GetConfigurationSetResponse
from openapi_server.models.get_dedicated_ip_response import GetDedicatedIpResponse
from openapi_server.models.get_dedicated_ips_response import GetDedicatedIpsResponse
from openapi_server.models.get_deliverability_dashboard_options_response import GetDeliverabilityDashboardOptionsResponse
from openapi_server.models.get_deliverability_test_report_response import GetDeliverabilityTestReportResponse
from openapi_server.models.get_domain_deliverability_campaign_response import GetDomainDeliverabilityCampaignResponse
from openapi_server.models.get_domain_statistics_report_response import GetDomainStatisticsReportResponse
from openapi_server.models.get_email_identity_response import GetEmailIdentityResponse
from openapi_server.models.list_configuration_sets_response import ListConfigurationSetsResponse
from openapi_server.models.list_dedicated_ip_pools_response import ListDedicatedIpPoolsResponse
from openapi_server.models.list_deliverability_test_reports_response import ListDeliverabilityTestReportsResponse
from openapi_server.models.list_domain_deliverability_campaigns_response import ListDomainDeliverabilityCampaignsResponse
from openapi_server.models.list_email_identities_response import ListEmailIdentitiesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_account_dedicated_ip_warmup_attributes_request import PutAccountDedicatedIpWarmupAttributesRequest
from openapi_server.models.put_account_sending_attributes_request import PutAccountSendingAttributesRequest
from openapi_server.models.put_configuration_set_delivery_options_request import PutConfigurationSetDeliveryOptionsRequest
from openapi_server.models.put_configuration_set_reputation_options_request import PutConfigurationSetReputationOptionsRequest
from openapi_server.models.put_configuration_set_sending_options_request import PutConfigurationSetSendingOptionsRequest
from openapi_server.models.put_configuration_set_tracking_options_request import PutConfigurationSetTrackingOptionsRequest
from openapi_server.models.put_dedicated_ip_in_pool_request import PutDedicatedIpInPoolRequest
from openapi_server.models.put_dedicated_ip_warmup_attributes_request import PutDedicatedIpWarmupAttributesRequest
from openapi_server.models.put_deliverability_dashboard_option_request import PutDeliverabilityDashboardOptionRequest
from openapi_server.models.put_email_identity_dkim_attributes_request import PutEmailIdentityDkimAttributesRequest
from openapi_server.models.put_email_identity_feedback_attributes_request import PutEmailIdentityFeedbackAttributesRequest
from openapi_server.models.put_email_identity_mail_from_attributes_request import PutEmailIdentityMailFromAttributesRequest
from openapi_server.models.send_email_request import SendEmailRequest
from openapi_server.models.send_email_response import SendEmailResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_configuration_set_event_destination_request import UpdateConfigurationSetEventDestinationRequest
from openapi_server import util


async def create_configuration_set(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_configuration_set

    Create a configuration set. &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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

    &lt;p&gt;Create an event destination. In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt; &lt;p&gt;A single configuration set can include more than one event destination.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that you want to add an event destination to.
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


async def create_dedicated_ip_pool(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_dedicated_ip_pool

    Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Pinpoint account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, Amazon Pinpoint sends it using only the IP addresses in the associated pool.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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

    Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon Pinpoint then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the &lt;code&gt;GetDeliverabilityTestReport&lt;/code&gt; operation to view the results of the test.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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

    &lt;p&gt;Verifies an email identity for use with Amazon Pinpoint. In Amazon Pinpoint, an identity is an email address or domain that you use when you send email. Before you can use an identity to send email with Amazon Pinpoint, you first have to verify it. By verifying an address, you demonstrate that you&#39;re the owner of the address, and that you&#39;ve given Amazon Pinpoint permission to send email from the address.&lt;/p&gt; &lt;p&gt;When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. &lt;/p&gt; &lt;p&gt;When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_configuration_set(request: web.Request, configuration_set_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_configuration_set

    &lt;p&gt;Delete an existing configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that you want to delete.
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

    &lt;p&gt;Delete an event destination.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that contains the event destination that you want to delete.
    :type configuration_set_name: str
    :param event_destination_name: The name of the event destination that you want to delete.
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

    Deletes an email identity that you previously verified for use with Amazon Pinpoint. An identity can be either an email address or a domain name.

    :param email_identity: The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.
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


async def get_account(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account

    Obtain information about the email-sending status and capabilities of your Amazon Pinpoint account in the current AWS Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
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

    :param blacklist_item_names: A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon Pinpoint or Amazon SES.
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

    &lt;p&gt;Get information about an existing configuration set, including the dedicated IP pool that it&#39;s associated with, whether or not it&#39;s enabled for sending email, and more.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that you want to obtain more information about.
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

    &lt;p&gt;Retrieve a list of event destinations that are associated with a configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

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


async def get_dedicated_ip(request: web.Request, ip, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dedicated_ip

    Get information about a dedicated IP address, including the name of the dedicated IP pool that it&#39;s associated with, as well information about the automatic warm-up process for the address.

    :param ip: The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that&#39;s assocaited with your Amazon Pinpoint account.
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


async def get_dedicated_ips(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, pool_name=None, next_token=None, page_size=None) -> web.Response:
    """get_dedicated_ips

    List the dedicated IP addresses that are associated with your Amazon Pinpoint account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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

    &lt;p&gt;Retrieve information about the status of the Deliverability dashboard for your Amazon Pinpoint account. When the Deliverability dashboard is enabled, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon Pinpoint. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/pinpoint/pricing/\&quot;&gt;Amazon Pinpoint Pricing&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
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

    Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (&lt;code&gt;PutDeliverabilityDashboardOption&lt;/code&gt; operation).

    :param campaign_id: The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns this identifier to a campaign. This value is not the same as the campaign identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint API or the Amazon Pinpoint console.
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

    Provides information about a specific identity associated with your Amazon Pinpoint account, including the identity&#39;s verification status, its DKIM authentication status, and its custom Mail-From settings.

    :param email_identity: The email identity that you want to retrieve details for.
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


async def list_configuration_sets(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_configuration_sets

    &lt;p&gt;List all of the configuration sets associated with your Amazon Pinpoint account in the current region.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def list_dedicated_ip_pools(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_dedicated_ip_pools

    List all of the dedicated IP pools that exist in your Amazon Pinpoint account in the current AWS Region.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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

    Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range. This data is available for a domain only if you enabled the Deliverability dashboard (&lt;code&gt;PutDeliverabilityDashboardOption&lt;/code&gt; operation) for the domain.

    :param start_date: The first day, in Unix time format, that you want to obtain deliverability data for.
    :type start_date: str
    :param end_date: The last day, in Unix time format, that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the &lt;code&gt;StartDate&lt;/code&gt; parameter.
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

    Returns a list of all of the email identities that are associated with your Amazon Pinpoint account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren&#39;t.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Retrieve a list of the tags (keys and values) that are associated with a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource in Amazon Pinpoint. Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an optional associated &lt;i&gt;tag value&lt;/i&gt;. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.

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


async def put_configuration_set_delivery_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_delivery_options

    Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.

    :param configuration_set_name: The name of the configuration set that you want to associate with a dedicated IP pool.
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

    Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific AWS Region.

    :param configuration_set_name: The name of the configuration set that you want to enable or disable reputation metric tracking for.
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

    Enable or disable email sending for messages that use a particular configuration set in a specific AWS Region.

    :param configuration_set_name: The name of the configuration set that you want to enable or disable email sending for.
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


async def put_configuration_set_tracking_options(request: web.Request, configuration_set_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_configuration_set_tracking_options

    Specify a custom domain to use for open and click tracking elements in email that you send using Amazon Pinpoint.

    :param configuration_set_name: The name of the configuration set that you want to add a custom tracking domain to.
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


async def put_dedicated_ip_in_pool(request: web.Request, ip, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_dedicated_ip_in_pool

    &lt;p&gt;Move a dedicated IP address to an existing dedicated IP pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The dedicated IP address that you specify must already exist, and must be associated with your Amazon Pinpoint account. &lt;/p&gt; &lt;p&gt;The dedicated IP pool you specify must already exist. You can create a new pool by using the &lt;code&gt;CreateDedicatedIpPool&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt;

    :param ip: The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that&#39;s associated with your Amazon Pinpoint account.
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

    &lt;p&gt;Enable or disable the Deliverability dashboard for your Amazon Pinpoint account. When you enable the Deliverability dashboard, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon Pinpoint. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/pinpoint/pricing/\&quot;&gt;Amazon Pinpoint Pricing&lt;/a&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def put_email_identity_dkim_attributes(request: web.Request, email_identity, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_email_identity_dkim_attributes

    Used to enable or disable DKIM authentication for an email identity.

    :param email_identity: The email identity that you want to change the DKIM settings for.
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


async def put_email_identity_feedback_attributes(request: web.Request, email_identity, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_email_identity_feedback_attributes

    &lt;p&gt;Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.&lt;/p&gt; &lt;p&gt;When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.&lt;/p&gt; &lt;p&gt;When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You&#39;re required to have a method of tracking bounces and complaints. If you haven&#39;t set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).&lt;/p&gt;

    :param email_identity: The email identity that you want to configure bounce and complaint feedback forwarding for.
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

    :param email_identity: The verified email identity that you want to set up the custom MAIL FROM domain for.
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


async def send_email(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_email

    &lt;p&gt;Sends an email message. You can use the Amazon Pinpoint Email API to send two types of messages:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Simple&lt;/b&gt; – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon Pinpoint assembles the message for you.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Raw&lt;/b&gt; – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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

    &lt;p&gt;Add one or more tags (keys and values) to a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.&lt;/p&gt; &lt;p&gt;Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an associated &lt;i&gt;tag value&lt;/i&gt;, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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

    Remove one or more tags (keys and values) from a specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.
    :type resource_arn: str
    :param tag_keys: &lt;p&gt;The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.&lt;/p&gt; &lt;p&gt;To remove more than one tag from the resource, append the &lt;code&gt;TagKeys&lt;/code&gt; parameter and argument for each additional tag to remove, separated by an ampersand. For example: &lt;code&gt;/v1/email/tags?ResourceArn&#x3D;ResourceArn&amp;amp;TagKeys&#x3D;Key1&amp;amp;TagKeys&#x3D;Key2&lt;/code&gt; &lt;/p&gt;
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

    &lt;p&gt;Update the configuration of an event destination for a configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

    :param configuration_set_name: The name of the configuration set that contains the event destination that you want to modify.
    :type configuration_set_name: str
    :param event_destination_name: The name of the event destination that you want to modify.
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
