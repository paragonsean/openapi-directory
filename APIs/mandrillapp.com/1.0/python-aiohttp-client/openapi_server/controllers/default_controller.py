from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.domain import Domain
from openapi_server.models.email import Email
from openapi_server.models.exports_activity import ExportsActivity
from openapi_server.models.exports_info_response import ExportsInfoResponse
from openapi_server.models.exports_list_response_inner import ExportsListResponseInner
from openapi_server.models.exports_satus import ExportsSatus
from openapi_server.models.id import Id
from openapi_server.models.inbound_add_route import InboundAddRoute
from openapi_server.models.inbound_domains_response_inner import InboundDomainsResponseInner
from openapi_server.models.inbound_info import InboundInfo
from openapi_server.models.inbound_routes_response_inner import InboundRoutesResponseInner
from openapi_server.models.inbound_send_raw import InboundSendRaw
from openapi_server.models.inbound_send_raw_response_inner import InboundSendRawResponseInner
from openapi_server.models.inbound_update_route import InboundUpdateRoute
from openapi_server.models.ip import Ip
from openapi_server.models.ip_domain import IpDomain
from openapi_server.models.ip_info import IpInfo
from openapi_server.models.ips_check_custom_dns_response import IpsCheckCustomDnsResponse
from openapi_server.models.ips_delete_pool_response import IpsDeletePoolResponse
from openapi_server.models.ips_delete_response import IpsDeleteResponse
from openapi_server.models.ips_list_pools_response_inner import IpsListPoolsResponseInner
from openapi_server.models.ips_list_pools_response_inner_ips_inner import IpsListPoolsResponseInnerIpsInner
from openapi_server.models.ips_pool import IpsPool
from openapi_server.models.ips_pool_key import IpsPoolKey
from openapi_server.models.ips_provision import IpsProvision
from openapi_server.models.ips_provision_response import IpsProvisionResponse
from openapi_server.models.ips_set_pool import IpsSetPool
from openapi_server.models.message_send_status_inner import MessageSendStatusInner
from openapi_server.models.messages_cancel_scheduled import MessagesCancelScheduled
from openapi_server.models.messages_content_response import MessagesContentResponse
from openapi_server.models.messages_info_response import MessagesInfoResponse
from openapi_server.models.messages_list_scheduled import MessagesListScheduled
from openapi_server.models.messages_list_scheduled_response_inner import MessagesListScheduledResponseInner
from openapi_server.models.messages_parse import MessagesParse
from openapi_server.models.messages_parse_response import MessagesParseResponse
from openapi_server.models.messages_reschedule import MessagesReschedule
from openapi_server.models.messages_search import MessagesSearch
from openapi_server.models.messages_search_response_inner import MessagesSearchResponseInner
from openapi_server.models.messages_search_time_series import MessagesSearchTimeSeries
from openapi_server.models.messages_send import MessagesSend
from openapi_server.models.messages_send_raw import MessagesSendRaw
from openapi_server.models.messages_send_template import MessagesSendTemplate
from openapi_server.models.metadata_info import MetadataInfo
from openapi_server.models.metadata_list_response_inner import MetadataListResponseInner
from openapi_server.models.metadata_template import MetadataTemplate
from openapi_server.models.name import Name
from openapi_server.models.notify_email import NotifyEmail
from openapi_server.models.rejects_add import RejectsAdd
from openapi_server.models.rejects_add_response import RejectsAddResponse
from openapi_server.models.rejects_delete import RejectsDelete
from openapi_server.models.rejects_delete_response import RejectsDeleteResponse
from openapi_server.models.rejects_list import RejectsList
from openapi_server.models.rejects_list_response_inner import RejectsListResponseInner
from openapi_server.models.rejects_list_response_inner_sender import RejectsListResponseInnerSender
from openapi_server.models.route import Route
from openapi_server.models.schedulingchange_info import SchedulingchangeInfo
from openapi_server.models.sender_address import SenderAddress
from openapi_server.models.sender_domain_info import SenderDomainInfo
from openapi_server.models.senders_domains_response_inner import SendersDomainsResponseInner
from openapi_server.models.senders_info_response import SendersInfoResponse
from openapi_server.models.senders_verify_domain import SendersVerifyDomain
from openapi_server.models.senders_verify_domain_response import SendersVerifyDomainResponse
from openapi_server.models.subaccount_info import SubaccountInfo
from openapi_server.models.subaccount_info2 import SubaccountInfo2
from openapi_server.models.subaccounts_info_response import SubaccountsInfoResponse
from openapi_server.models.subaccounts_list_response_inner import SubaccountsListResponseInner
from openapi_server.models.tag_key import TagKey
from openapi_server.models.tags_delete_response import TagsDeleteResponse
from openapi_server.models.tags_info_response import TagsInfoResponse
from openapi_server.models.tags_list_response_inner import TagsListResponseInner
from openapi_server.models.template import Template
from openapi_server.models.template_detailed import TemplateDetailed
from openapi_server.models.templates_list import TemplatesList
from openapi_server.models.templates_list_response_inner import TemplatesListResponseInner
from openapi_server.models.templates_render import TemplatesRender
from openapi_server.models.templates_render_response import TemplatesRenderResponse
from openapi_server.models.time_series_inner import TimeSeriesInner
from openapi_server.models.timeseries_inner import TimeseriesInner
from openapi_server.models.tracking_domain_status import TrackingDomainStatus
from openapi_server.models.url_infos_inner import UrlInfosInner
from openapi_server.models.url_key import UrlKey
from openapi_server.models.urls_time_series import UrlsTimeSeries
from openapi_server.models.urls_time_series_response_inner import UrlsTimeSeriesResponseInner
from openapi_server.models.urls_tracking_domains_response_inner import UrlsTrackingDomainsResponseInner
from openapi_server.models.users_info_response import UsersInfoResponse
from openapi_server.models.users_ping2_response import UsersPing2Response
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_key import WebhookKey
from openapi_server.models.webhooks_add import WebhooksAdd
from openapi_server.models.webhooks_list_response_inner import WebhooksListResponseInner
from openapi_server.models.webhooks_update import WebhooksUpdate
from openapi_server.models.whitelists_add_response import WhitelistsAddResponse
from openapi_server.models.whitelists_delete_response import WhitelistsDeleteResponse
from openapi_server.models.whitelists_list_response_inner import WhitelistsListResponseInner
from openapi_server import util


async def exports_activity_json_post(request: web.Request, body) -> web.Response:
    """exports_activity_json_post

    Begins an export of your activity history. The activity will be exported to a zip archive containing a single file named activity.csv in the same format as you would be able to export from your account&#39;s activity view. It includes the following fields: Date, Email Address, Sender, Subject, Status, Tags, Opens, Clicks, Bounce Detail. If you have configured any custom metadata fields, they will be included in the exported data.

    :param body: 
    :type body: dict | bytes

    """
    body = ExportsActivity.from_dict(body)
    return web.Response(status=200)


async def exports_info_json_post(request: web.Request, body) -> web.Response:
    """exports_info_json_post

    Returns information about an export job. If the export job&#39;s state is &#39;complete&#39;, the returned data will include a URL you can use to fetch the results. Every export job produces a zip archive, but the format of the archive is distinct for each job type. The api calls that initiate exports include more details about the output format for that job type.

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def exports_list_json_post(request: web.Request, body) -> web.Response:
    """exports_list_json_post

    Returns a list of your exports.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def exports_rejects_json_post(request: web.Request, body) -> web.Response:
    """exports_rejects_json_post

    Begins an export of your rejection blacklist. The blacklist will be exported to a zip archive containing a single file named rejects.csv that includes the following fields: email, reason, detail, created_at, expires_at, last_event_at, expires_at.

    :param body: 
    :type body: dict | bytes

    """
    body = NotifyEmail.from_dict(body)
    return web.Response(status=200)


async def exports_whitelist_json_post(request: web.Request, body) -> web.Response:
    """exports_whitelist_json_post

    Begins an export of your rejection whitelist. The whitelist will be exported to a zip archive containing a single file named whitelist.csv that includes the following fields: email, detail, created_at.

    :param body: 
    :type body: dict | bytes

    """
    body = NotifyEmail.from_dict(body)
    return web.Response(status=200)


async def inbound_add_domain_json_post(request: web.Request, body) -> web.Response:
    """inbound_add_domain_json_post

    Add an inbound domain to your account

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def inbound_add_route_json_post(request: web.Request, body) -> web.Response:
    """inbound_add_route_json_post

    Add a new mailbox route to an inbound domain

    :param body: 
    :type body: dict | bytes

    """
    body = InboundAddRoute.from_dict(body)
    return web.Response(status=200)


async def inbound_check_domain_json_post(request: web.Request, body) -> web.Response:
    """inbound_check_domain_json_post

    Check the MX settings for an inbound domain. The domain must have already been added with the add-domain call

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def inbound_delete_domain_json_post(request: web.Request, body) -> web.Response:
    """inbound_delete_domain_json_post

    Delete an inbound domain from the account. All mail will stop routing for this domain immediately.

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def inbound_delete_route_json_post(request: web.Request, body) -> web.Response:
    """inbound_delete_route_json_post

    Delete an existing inbound mailbox route

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def inbound_domains_json_post(request: web.Request, body) -> web.Response:
    """inbound_domains_json_post

    List the domains that have been configured for inbound delivery

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def inbound_routes_json_post(request: web.Request, body) -> web.Response:
    """inbound_routes_json_post

    List the mailbox routes defined for an inbound domain

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def inbound_send_raw_json_post(request: web.Request, body) -> web.Response:
    """inbound_send_raw_json_post

    Take a raw MIME document destined for a domain with inbound domains set up, and send it to the inbound hook exactly as if it had been sent over SMTP

    :param body: 
    :type body: dict | bytes

    """
    body = InboundSendRaw.from_dict(body)
    return web.Response(status=200)


async def inbound_update_route_json_post(request: web.Request, body) -> web.Response:
    """inbound_update_route_json_post

    Update the pattern or webhook of an existing inbound mailbox route. If null is provided for any fields, the values will remain unchanged.

    :param body: 
    :type body: dict | bytes

    """
    body = InboundUpdateRoute.from_dict(body)
    return web.Response(status=200)


async def ips_cancel_warmup_json_post(request: web.Request, body) -> web.Response:
    """ips_cancel_warmup_json_post

    Cancels the warmup process for a dedicated IP.

    :param body: 
    :type body: dict | bytes

    """
    body = Ip.from_dict(body)
    return web.Response(status=200)


async def ips_check_custom_dns_json_post(request: web.Request, body) -> web.Response:
    """ips_check_custom_dns_json_post

    Tests whether a domain name is valid for use as the custom reverse DNS for a dedicated IP.

    :param body: 
    :type body: dict | bytes

    """
    body = IpDomain.from_dict(body)
    return web.Response(status=200)


async def ips_create_pool_json_post(request: web.Request, body) -> web.Response:
    """ips_create_pool_json_post

    Creates a pool and returns it. If a pool already exists with this name, no action will be performed.

    :param body: 
    :type body: dict | bytes

    """
    body = IpsPoolKey.from_dict(body)
    return web.Response(status=200)


async def ips_delete_json_post(request: web.Request, body) -> web.Response:
    """ips_delete_json_post

    Deletes a dedicated IP. This is permanent and cannot be undone.

    :param body: 
    :type body: dict | bytes

    """
    body = Ip.from_dict(body)
    return web.Response(status=200)


async def ips_delete_pool_json_post(request: web.Request, body) -> web.Response:
    """ips_delete_pool_json_post

    Deletes a pool. A pool must be empty before you can delete it, and you cannot delete your default pool.

    :param body: 
    :type body: dict | bytes

    """
    body = IpsPoolKey.from_dict(body)
    return web.Response(status=200)


async def ips_info_json_post(request: web.Request, body) -> web.Response:
    """ips_info_json_post

    Retrieves information about a single dedicated ip.

    :param body: 
    :type body: dict | bytes

    """
    body = Ip.from_dict(body)
    return web.Response(status=200)


async def ips_list_json_post(request: web.Request, body) -> web.Response:
    """ips_list_json_post

    Lists your dedicated IPs.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def ips_list_pools_json_post(request: web.Request, body) -> web.Response:
    """ips_list_pools_json_post

    Lists your dedicated IP pools.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def ips_pool_info_json_post(request: web.Request, body) -> web.Response:
    """ips_pool_info_json_post

    Describes a single dedicated IP pool.

    :param body: 
    :type body: dict | bytes

    """
    body = IpsPoolKey.from_dict(body)
    return web.Response(status=200)


async def ips_provision_json_post(request: web.Request, body) -> web.Response:
    """ips_provision_json_post

    Requests an additional dedicated IP for your account. Accounts may have one outstanding request at any time, and provisioning requests are processed within 24 hours.

    :param body: 
    :type body: dict | bytes

    """
    body = IpsProvision.from_dict(body)
    return web.Response(status=200)


async def ips_set_custom_dns_json_post(request: web.Request, body) -> web.Response:
    """ips_set_custom_dns_json_post

    Configures the custom DNS name for a dedicated IP.

    :param body: 
    :type body: dict | bytes

    """
    body = IpDomain.from_dict(body)
    return web.Response(status=200)


async def ips_set_pool_json_post(request: web.Request, body) -> web.Response:
    """ips_set_pool_json_post

    Moves a dedicated IP to a different pool.

    :param body: 
    :type body: dict | bytes

    """
    body = IpsSetPool.from_dict(body)
    return web.Response(status=200)


async def ips_start_warmup_json_post(request: web.Request, body) -> web.Response:
    """ips_start_warmup_json_post

    Begins the warmup process for a dedicated IP. During the warmup process, Mandrill will gradually increase the percentage of your mail that is sent over the warming-up IP, over a period of roughly 30 days. The rest of your mail will be sent over shared IPs or other dedicated IPs in the same pool.

    :param body: 
    :type body: dict | bytes

    """
    body = Ip.from_dict(body)
    return web.Response(status=200)


async def messages_cancel_scheduled_json_post(request: web.Request, body) -> web.Response:
    """messages_cancel_scheduled_json_post

    Cancels a scheduled email.

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesCancelScheduled.from_dict(body)
    return web.Response(status=200)


async def messages_content_json_post(request: web.Request, body) -> web.Response:
    """messages_content_json_post

    Get the full content of a recently sent message

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def messages_info_json_post(request: web.Request, body) -> web.Response:
    """messages_info_json_post

    Get the information for a single recently sent message

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def messages_list_scheduled_json_post(request: web.Request, body) -> web.Response:
    """messages_list_scheduled_json_post

    Queries your scheduled emails by sender or recipient, or both.

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesListScheduled.from_dict(body)
    return web.Response(status=200)


async def messages_parse_json_post(request: web.Request, body) -> web.Response:
    """messages_parse_json_post

    Parse the full MIME document for an email message, returning the content of the message broken into its constituent pieces

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesParse.from_dict(body)
    return web.Response(status=200)


async def messages_reschedule_json_post(request: web.Request, body) -> web.Response:
    """messages_reschedule_json_post

    Reschedules a scheduled email.

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesReschedule.from_dict(body)
    return web.Response(status=200)


async def messages_search_json_post(request: web.Request, body) -> web.Response:
    """messages_search_json_post

    Search the content of recently sent messages and optionally narrow by date range, tags and senders. This method may be called up to 20 times per minute. If you need the data more often, you can use /messages/info.json to get the information for a single message, or webhooks to push activity to your own application for querying.

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesSearch.from_dict(body)
    return web.Response(status=200)


async def messages_search_time_series_json_post(request: web.Request, body) -> web.Response:
    """messages_search_time_series_json_post

    Search the content of recently sent messages and return the aggregated hourly stats for matching messages

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesSearchTimeSeries.from_dict(body)
    return web.Response(status=200)


async def messages_send_json_post(request: web.Request, body) -> web.Response:
    """messages_send_json_post

    Send a new transactional message through Mandrill

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesSend.from_dict(body)
    return web.Response(status=200)


async def messages_send_raw_json_post(request: web.Request, body) -> web.Response:
    """messages_send_raw_json_post

    Take a raw MIME document for a message, and send it exactly as if it were sent through Mandrill&#39;s SMTP servers

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesSendRaw.from_dict(body)
    return web.Response(status=200)


async def messages_send_template_json_post(request: web.Request, body) -> web.Response:
    """messages_send_template_json_post

    Send a new transactional message through Mandrill using a template

    :param body: 
    :type body: dict | bytes

    """
    body = MessagesSendTemplate.from_dict(body)
    return web.Response(status=200)


async def metadata_add_json_post(request: web.Request, body) -> web.Response:
    """metadata_add_json_post

    Add a new custom metadata field to be indexed for the account.

    :param body: 
    :type body: dict | bytes

    """
    body = MetadataTemplate.from_dict(body)
    return web.Response(status=200)


async def metadata_delete_json_post(request: web.Request, body) -> web.Response:
    """metadata_delete_json_post

    Delete an existing custom metadata field. Deletion isn&#39;t instataneous, and /metadata/list will continue to return the field until the asynchronous deletion process is complete.

    :param body: 
    :type body: dict | bytes

    """
    body = Name.from_dict(body)
    return web.Response(status=200)


async def metadata_list_json_post(request: web.Request, body) -> web.Response:
    """metadata_list_json_post

    Get the list of custom metadata fields indexed for the account.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def metadata_update_json_post(request: web.Request, body) -> web.Response:
    """metadata_update_json_post

    Update an existing custom metadata field.

    :param body: 
    :type body: dict | bytes

    """
    body = MetadataTemplate.from_dict(body)
    return web.Response(status=200)


async def rejects_add_json_post(request: web.Request, body) -> web.Response:
    """rejects_add_json_post

    Adds an email to your email rejection blacklist. Addresses that you add manually will never expire and there is no reputation penalty for removing them from your blacklist. Attempting to blacklist an address that has been whitelisted will have no effect.

    :param body: 
    :type body: dict | bytes

    """
    body = RejectsAdd.from_dict(body)
    return web.Response(status=200)


async def rejects_delete_json_post(request: web.Request, body) -> web.Response:
    """rejects_delete_json_post

    Deletes an email rejection. There is no limit to how many rejections you can remove from your blacklist, but keep in mind that each deletion has an affect on your reputation.

    :param body: 
    :type body: dict | bytes

    """
    body = RejectsDelete.from_dict(body)
    return web.Response(status=200)


async def rejects_list_json_post(request: web.Request, body) -> web.Response:
    """rejects_list_json_post

    Retrieves your email rejection blacklist. You can provide an email address to limit the results. Returns up to 1000 results. By default, entries that have expired are excluded from the results; set include_expired to true to include them.

    :param body: 
    :type body: dict | bytes

    """
    body = RejectsList.from_dict(body)
    return web.Response(status=200)


async def senders_add_domain_json_post(request: web.Request, body) -> web.Response:
    """senders_add_domain_json_post

    Adds a sender domain to your account. Sender domains are added automatically as you send, but you can use this call to add them ahead of time.

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def senders_check_domain_json_post(request: web.Request, body) -> web.Response:
    """senders_check_domain_json_post

    Checks the SPF and DKIM settings for a domain. If you haven&#39;t already added this domain to your account, it will be added automatically.

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def senders_domains_json_post(request: web.Request, body) -> web.Response:
    """senders_domains_json_post

    Returns the sender domains that have been added to this account.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def senders_info_json_post(request: web.Request, body) -> web.Response:
    """senders_info_json_post

    Return more detailed information about a single sender, including aggregates of recent stats

    :param body: 
    :type body: dict | bytes

    """
    body = SenderAddress.from_dict(body)
    return web.Response(status=200)


async def senders_list_json_post(request: web.Request, body) -> web.Response:
    """senders_list_json_post

    Return the senders that have tried to use this account.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def senders_time_series_json_post(request: web.Request, body) -> web.Response:
    """senders_time_series_json_post

    Return the recent history (hourly stats for the last 30 days) for a sender

    :param body: 
    :type body: dict | bytes

    """
    body = SenderAddress.from_dict(body)
    return web.Response(status=200)


async def senders_verify_domain_json_post(request: web.Request, body) -> web.Response:
    """senders_verify_domain_json_post

    Sends a verification email in order to verify ownership of a domain. Domain verification is an optional step to confirm ownership of a domain. Once a domain has been verified in a Mandrill account, other accounts may not have their messages signed by that domain unless they also verify the domain. This prevents other Mandrill accounts from sending mail signed by your domain.

    :param body: 
    :type body: dict | bytes

    """
    body = SendersVerifyDomain.from_dict(body)
    return web.Response(status=200)


async def subaccounts_add_json_post(request: web.Request, body) -> web.Response:
    """subaccounts_add_json_post

    Add a new subaccount

    :param body: 
    :type body: dict | bytes

    """
    body = SubaccountInfo.from_dict(body)
    return web.Response(status=200)


async def subaccounts_delete_json_post(request: web.Request, body) -> web.Response:
    """subaccounts_delete_json_post

    Delete an existing subaccount. Any email related to the subaccount will be saved, but stats will be removed and any future sending calls to this subaccount will fail.

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def subaccounts_info_json_post(request: web.Request, body) -> web.Response:
    """subaccounts_info_json_post

    Given the ID of an existing subaccount, return the data about it

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def subaccounts_list_json_post(request: web.Request, body) -> web.Response:
    """subaccounts_list_json_post

    Get the list of subaccounts defined for the account, optionally filtered by a prefix

    :param body: 
    :type body: dict | bytes

    """
    body = UrlKey.from_dict(body)
    return web.Response(status=200)


async def subaccounts_pause_json_post(request: web.Request, body) -> web.Response:
    """subaccounts_pause_json_post

    Pause a subaccount&#39;s sending. Any future emails delivered to this subaccount will be queued for a maximum of 3 days until the subaccount is resumed.

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def subaccounts_resume_json_post(request: web.Request, body) -> web.Response:
    """subaccounts_resume_json_post

    Resume a paused subaccount&#39;s sending

    :param body: 
    :type body: dict | bytes

    """
    body = Id.from_dict(body)
    return web.Response(status=200)


async def subaccounts_update_json_post(request: web.Request, body) -> web.Response:
    """subaccounts_update_json_post

    Update an existing subaccount

    :param body: 
    :type body: dict | bytes

    """
    body = SubaccountInfo.from_dict(body)
    return web.Response(status=200)


async def tags_all_time_series_json_post(request: web.Request, body) -> web.Response:
    """tags_all_time_series_json_post

    Return the recent history (hourly stats for the last 30 days) for all tags

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def tags_delete_json_post(request: web.Request, body) -> web.Response:
    """tags_delete_json_post

    Deletes a tag permanently. Deleting a tag removes the tag from any messages that have been sent, and also deletes the tag&#39;s stats. There is no way to undo this operation, so use it carefully.

    :param body: 
    :type body: dict | bytes

    """
    body = TagKey.from_dict(body)
    return web.Response(status=200)


async def tags_info_json_post(request: web.Request, body) -> web.Response:
    """tags_info_json_post

    Return more detailed information about a single tag, including aggregates of recent stats

    :param body: 
    :type body: dict | bytes

    """
    body = TagKey.from_dict(body)
    return web.Response(status=200)


async def tags_list_json_post(request: web.Request, body) -> web.Response:
    """tags_list_json_post

    Return all of the user-defined tag information

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def tags_time_series_json_post(request: web.Request, body) -> web.Response:
    """tags_time_series_json_post

    Return the recent history (hourly stats for the last 30 days) for a tag

    :param body: 
    :type body: dict | bytes

    """
    body = TagKey.from_dict(body)
    return web.Response(status=200)


async def templates_add_json_post(request: web.Request, body) -> web.Response:
    """templates_add_json_post

    Add a new template

    :param body: 
    :type body: dict | bytes

    """
    body = Template.from_dict(body)
    return web.Response(status=200)


async def templates_delete_json_post(request: web.Request, body) -> web.Response:
    """templates_delete_json_post

    Delete a template

    :param body: 
    :type body: dict | bytes

    """
    body = Name.from_dict(body)
    return web.Response(status=200)


async def templates_info_json_post(request: web.Request, body) -> web.Response:
    """templates_info_json_post

    Get the information for an existing template

    :param body: 
    :type body: dict | bytes

    """
    body = Name.from_dict(body)
    return web.Response(status=200)


async def templates_list_json_post(request: web.Request, body) -> web.Response:
    """templates_list_json_post

    Return a list of all the templates available to this user

    :param body: 
    :type body: dict | bytes

    """
    body = TemplatesList.from_dict(body)
    return web.Response(status=200)


async def templates_publish_json_post(request: web.Request, body) -> web.Response:
    """templates_publish_json_post

    Publish the content for the template. Any new messages sent using this template will start using the content that was previously in draft.

    :param body: 
    :type body: dict | bytes

    """
    body = Name.from_dict(body)
    return web.Response(status=200)


async def templates_render_json_post(request: web.Request, body) -> web.Response:
    """templates_render_json_post

    Inject content and optionally merge fields into a template, returning the HTML that results

    :param body: 
    :type body: dict | bytes

    """
    body = TemplatesRender.from_dict(body)
    return web.Response(status=200)


async def templates_time_series_json_post(request: web.Request, body) -> web.Response:
    """templates_time_series_json_post

    Return the recent history (hourly stats for the last 30 days) for a template

    :param body: 
    :type body: dict | bytes

    """
    body = Name.from_dict(body)
    return web.Response(status=200)


async def templates_update_json_post(request: web.Request, body) -> web.Response:
    """templates_update_json_post

    Update the code for an existing template. If null is provided for any fields, the values will remain unchanged.

    :param body: 
    :type body: dict | bytes

    """
    body = Template.from_dict(body)
    return web.Response(status=200)


async def urls_add_tracking_domain_json_post(request: web.Request, body) -> web.Response:
    """urls_add_tracking_domain_json_post

    Add a tracking domain to your account

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def urls_check_tracking_domain_json_post(request: web.Request, body) -> web.Response:
    """urls_check_tracking_domain_json_post

    Checks the CNAME settings for a tracking domain. The domain must have been added already with the add-tracking-domain call

    :param body: 
    :type body: dict | bytes

    """
    body = Domain.from_dict(body)
    return web.Response(status=200)


async def urls_list_json_post(request: web.Request, body) -> web.Response:
    """urls_list_json_post

    Get the 100 most clicked URLs

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def urls_search_json_post(request: web.Request, body) -> web.Response:
    """urls_search_json_post

    Return the 100 most clicked URLs that match the search query given

    :param body: 
    :type body: dict | bytes

    """
    body = UrlKey.from_dict(body)
    return web.Response(status=200)


async def urls_time_series_json_post(request: web.Request, body) -> web.Response:
    """urls_time_series_json_post

    Return the recent history (hourly stats for the last 30 days) for a url

    :param body: 
    :type body: dict | bytes

    """
    body = UrlsTimeSeries.from_dict(body)
    return web.Response(status=200)


async def urls_tracking_domains_json_post(request: web.Request, body) -> web.Response:
    """urls_tracking_domains_json_post

    Get the list of tracking domains set up for this account

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def users_info_json_post(request: web.Request, body) -> web.Response:
    """users_info_json_post

    Return the information about the API-connected user

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def users_ping2_json_post(request: web.Request, body) -> web.Response:
    """users_ping2_json_post

    Validate an API key and respond to a ping (anal JSON parser version)

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def users_ping_json_post(request: web.Request, body) -> web.Response:
    """users_ping_json_post

    Validate an API key and respond to a ping

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def users_senders_json_post(request: web.Request, body) -> web.Response:
    """users_senders_json_post

    Return the senders that have tried to use this account, both verified and unverified

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def webhooks_add_json_post(request: web.Request, body) -> web.Response:
    """webhooks_add_json_post

    Add a new webhook

    :param body: 
    :type body: dict | bytes

    """
    body = WebhooksAdd.from_dict(body)
    return web.Response(status=200)


async def webhooks_delete_json_post(request: web.Request, body) -> web.Response:
    """webhooks_delete_json_post

    Delete an existing webhook

    :param body: 
    :type body: dict | bytes

    """
    body = WebhookKey.from_dict(body)
    return web.Response(status=200)


async def webhooks_info_json_post(request: web.Request, body) -> web.Response:
    """webhooks_info_json_post

    Given the ID of an existing webhook, return the data about it

    :param body: 
    :type body: dict | bytes

    """
    body = WebhookKey.from_dict(body)
    return web.Response(status=200)


async def webhooks_list_json_post(request: web.Request, body) -> web.Response:
    """webhooks_list_json_post

    Get the list of all webhooks defined on the account

    :param body: 
    :type body: dict | bytes

    """
    body = ApiKey.from_dict(body)
    return web.Response(status=200)


async def webhooks_update_json_post(request: web.Request, body) -> web.Response:
    """webhooks_update_json_post

    Update an existing webhook

    :param body: 
    :type body: dict | bytes

    """
    body = WebhooksUpdate.from_dict(body)
    return web.Response(status=200)


async def whitelists_add_json_post(request: web.Request, body) -> web.Response:
    """whitelists_add_json_post

    Adds an email to your email rejection whitelist. If the address is currently on your blacklist, that blacklist entry will be removed automatically.

    :param body: 
    :type body: dict | bytes

    """
    body = Email.from_dict(body)
    return web.Response(status=200)


async def whitelists_delete_json_post(request: web.Request, body) -> web.Response:
    """whitelists_delete_json_post

    Removes an email address from the whitelist.

    :param body: 
    :type body: dict | bytes

    """
    body = Email.from_dict(body)
    return web.Response(status=200)


async def whitelists_list_json_post(request: web.Request, body) -> web.Response:
    """whitelists_list_json_post

    Retrieves your email rejection whitelist. You can provide an email address or search prefix to limit the results. Returns up to 1000 results.

    :param body: 
    :type body: dict | bytes

    """
    body = Email.from_dict(body)
    return web.Response(status=200)
