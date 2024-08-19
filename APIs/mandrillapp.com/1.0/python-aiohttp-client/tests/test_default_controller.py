# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_exports_activity_json_post(client):
    """Test case for exports_activity_json_post

    
    """
    body = openapi_server.ExportsActivity()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/exports/activity.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_exports_info_json_post(client):
    """Test case for exports_info_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/exports/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_exports_list_json_post(client):
    """Test case for exports_list_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/exports/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_exports_rejects_json_post(client):
    """Test case for exports_rejects_json_post

    
    """
    body = openapi_server.NotifyEmail()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/exports/rejects.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_exports_whitelist_json_post(client):
    """Test case for exports_whitelist_json_post

    
    """
    body = openapi_server.NotifyEmail()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/exports/whitelist.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_add_domain_json_post(client):
    """Test case for inbound_add_domain_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/add-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_add_route_json_post(client):
    """Test case for inbound_add_route_json_post

    
    """
    body = openapi_server.InboundAddRoute()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/add-route.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_check_domain_json_post(client):
    """Test case for inbound_check_domain_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/check-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_delete_domain_json_post(client):
    """Test case for inbound_delete_domain_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/delete-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_delete_route_json_post(client):
    """Test case for inbound_delete_route_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/delete-route.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_domains_json_post(client):
    """Test case for inbound_domains_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/domains.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_routes_json_post(client):
    """Test case for inbound_routes_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/routes.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_send_raw_json_post(client):
    """Test case for inbound_send_raw_json_post

    
    """
    body = openapi_server.InboundSendRaw()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/send-raw.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_inbound_update_route_json_post(client):
    """Test case for inbound_update_route_json_post

    
    """
    body = openapi_server.InboundUpdateRoute()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/inbound/update-route.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_cancel_warmup_json_post(client):
    """Test case for ips_cancel_warmup_json_post

    
    """
    body = openapi_server.Ip()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/cancel-warmup.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_check_custom_dns_json_post(client):
    """Test case for ips_check_custom_dns_json_post

    
    """
    body = openapi_server.IpDomain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/check-custom-dns.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_create_pool_json_post(client):
    """Test case for ips_create_pool_json_post

    
    """
    body = openapi_server.IpsPoolKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/create-pool.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_delete_json_post(client):
    """Test case for ips_delete_json_post

    
    """
    body = openapi_server.Ip()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_delete_pool_json_post(client):
    """Test case for ips_delete_pool_json_post

    
    """
    body = openapi_server.IpsPoolKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/delete-pool.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_info_json_post(client):
    """Test case for ips_info_json_post

    
    """
    body = openapi_server.Ip()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_list_json_post(client):
    """Test case for ips_list_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_list_pools_json_post(client):
    """Test case for ips_list_pools_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/list-pools.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_pool_info_json_post(client):
    """Test case for ips_pool_info_json_post

    
    """
    body = openapi_server.IpsPoolKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/pool-info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_provision_json_post(client):
    """Test case for ips_provision_json_post

    
    """
    body = openapi_server.IpsProvision()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/provision.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_set_custom_dns_json_post(client):
    """Test case for ips_set_custom_dns_json_post

    
    """
    body = openapi_server.IpDomain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/set-custom-dns.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_set_pool_json_post(client):
    """Test case for ips_set_pool_json_post

    
    """
    body = openapi_server.IpsSetPool()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/set-pool.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_ips_start_warmup_json_post(client):
    """Test case for ips_start_warmup_json_post

    
    """
    body = openapi_server.Ip()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/ips/start-warmup.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_cancel_scheduled_json_post(client):
    """Test case for messages_cancel_scheduled_json_post

    
    """
    body = openapi_server.MessagesCancelScheduled()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/cancel-scheduled.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_content_json_post(client):
    """Test case for messages_content_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/content.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_info_json_post(client):
    """Test case for messages_info_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_list_scheduled_json_post(client):
    """Test case for messages_list_scheduled_json_post

    
    """
    body = openapi_server.MessagesListScheduled()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/list-scheduled.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_parse_json_post(client):
    """Test case for messages_parse_json_post

    
    """
    body = openapi_server.MessagesParse()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/parse.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_reschedule_json_post(client):
    """Test case for messages_reschedule_json_post

    
    """
    body = openapi_server.MessagesReschedule()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/reschedule.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_search_json_post(client):
    """Test case for messages_search_json_post

    
    """
    body = openapi_server.MessagesSearch()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/search.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_search_time_series_json_post(client):
    """Test case for messages_search_time_series_json_post

    
    """
    body = openapi_server.MessagesSearchTimeSeries()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/search-time-series.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_send_json_post(client):
    """Test case for messages_send_json_post

    
    """
    body = openapi_server.MessagesSend()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/send.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_send_raw_json_post(client):
    """Test case for messages_send_raw_json_post

    
    """
    body = openapi_server.MessagesSendRaw()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/send-raw.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_messages_send_template_json_post(client):
    """Test case for messages_send_template_json_post

    
    """
    body = openapi_server.MessagesSendTemplate()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/messages/send-template.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_add_json_post(client):
    """Test case for metadata_add_json_post

    
    """
    body = openapi_server.MetadataTemplate()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/metadata/add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_delete_json_post(client):
    """Test case for metadata_delete_json_post

    
    """
    body = openapi_server.Name()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/metadata/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_list_json_post(client):
    """Test case for metadata_list_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/metadata/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_metadata_update_json_post(client):
    """Test case for metadata_update_json_post

    
    """
    body = openapi_server.MetadataTemplate()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/metadata/update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_rejects_add_json_post(client):
    """Test case for rejects_add_json_post

    
    """
    body = openapi_server.RejectsAdd()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/rejects/add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_rejects_delete_json_post(client):
    """Test case for rejects_delete_json_post

    
    """
    body = openapi_server.RejectsDelete()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/rejects/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_rejects_list_json_post(client):
    """Test case for rejects_list_json_post

    
    """
    body = openapi_server.RejectsList()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/rejects/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_senders_add_domain_json_post(client):
    """Test case for senders_add_domain_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/senders/add-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_senders_check_domain_json_post(client):
    """Test case for senders_check_domain_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/senders/check-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_senders_domains_json_post(client):
    """Test case for senders_domains_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/senders/domains.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_senders_info_json_post(client):
    """Test case for senders_info_json_post

    
    """
    body = openapi_server.SenderAddress()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/senders/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_senders_list_json_post(client):
    """Test case for senders_list_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/senders/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_senders_time_series_json_post(client):
    """Test case for senders_time_series_json_post

    
    """
    body = openapi_server.SenderAddress()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/senders/time-series.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_senders_verify_domain_json_post(client):
    """Test case for senders_verify_domain_json_post

    
    """
    body = openapi_server.SendersVerifyDomain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/senders/verify-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_subaccounts_add_json_post(client):
    """Test case for subaccounts_add_json_post

    
    """
    body = openapi_server.SubaccountInfo()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/subaccounts/add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_subaccounts_delete_json_post(client):
    """Test case for subaccounts_delete_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/subaccounts/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_subaccounts_info_json_post(client):
    """Test case for subaccounts_info_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/subaccounts/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_subaccounts_list_json_post(client):
    """Test case for subaccounts_list_json_post

    
    """
    body = openapi_server.UrlKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/subaccounts/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_subaccounts_pause_json_post(client):
    """Test case for subaccounts_pause_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/subaccounts/pause.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_subaccounts_resume_json_post(client):
    """Test case for subaccounts_resume_json_post

    
    """
    body = openapi_server.Id()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/subaccounts/resume.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_subaccounts_update_json_post(client):
    """Test case for subaccounts_update_json_post

    
    """
    body = openapi_server.SubaccountInfo()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/subaccounts/update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tags_all_time_series_json_post(client):
    """Test case for tags_all_time_series_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tags/all-time-series.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tags_delete_json_post(client):
    """Test case for tags_delete_json_post

    
    """
    body = openapi_server.TagKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tags/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tags_info_json_post(client):
    """Test case for tags_info_json_post

    
    """
    body = openapi_server.TagKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tags/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tags_list_json_post(client):
    """Test case for tags_list_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tags/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_tags_time_series_json_post(client):
    """Test case for tags_time_series_json_post

    
    """
    body = openapi_server.TagKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tags/time-series.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_add_json_post(client):
    """Test case for templates_add_json_post

    
    """
    body = openapi_server.Template()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_delete_json_post(client):
    """Test case for templates_delete_json_post

    
    """
    body = openapi_server.Name()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_info_json_post(client):
    """Test case for templates_info_json_post

    
    """
    body = openapi_server.Name()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_list_json_post(client):
    """Test case for templates_list_json_post

    
    """
    body = openapi_server.TemplatesList()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_publish_json_post(client):
    """Test case for templates_publish_json_post

    
    """
    body = openapi_server.Name()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/publish.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_render_json_post(client):
    """Test case for templates_render_json_post

    
    """
    body = openapi_server.TemplatesRender()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/render.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_time_series_json_post(client):
    """Test case for templates_time_series_json_post

    
    """
    body = openapi_server.Name()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/time-series.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_templates_update_json_post(client):
    """Test case for templates_update_json_post

    
    """
    body = openapi_server.Template()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/templates/update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_urls_add_tracking_domain_json_post(client):
    """Test case for urls_add_tracking_domain_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/urls/add-tracking-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_urls_check_tracking_domain_json_post(client):
    """Test case for urls_check_tracking_domain_json_post

    
    """
    body = openapi_server.Domain()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/urls/check-tracking-domain.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_urls_list_json_post(client):
    """Test case for urls_list_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/urls/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_urls_search_json_post(client):
    """Test case for urls_search_json_post

    
    """
    body = openapi_server.UrlKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/urls/search.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_urls_time_series_json_post(client):
    """Test case for urls_time_series_json_post

    
    """
    body = openapi_server.UrlsTimeSeries()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/urls/time-series.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_urls_tracking_domains_json_post(client):
    """Test case for urls_tracking_domains_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/urls/tracking-domains.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_info_json_post(client):
    """Test case for users_info_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/users/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_ping2_json_post(client):
    """Test case for users_ping2_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/users/ping2.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_ping_json_post(client):
    """Test case for users_ping_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/users/ping.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_senders_json_post(client):
    """Test case for users_senders_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/users/senders.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_webhooks_add_json_post(client):
    """Test case for webhooks_add_json_post

    
    """
    body = openapi_server.WebhooksAdd()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/webhooks/add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_webhooks_delete_json_post(client):
    """Test case for webhooks_delete_json_post

    
    """
    body = openapi_server.WebhookKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/webhooks/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_webhooks_info_json_post(client):
    """Test case for webhooks_info_json_post

    
    """
    body = openapi_server.WebhookKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/webhooks/info.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_webhooks_list_json_post(client):
    """Test case for webhooks_list_json_post

    
    """
    body = openapi_server.ApiKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/webhooks/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_webhooks_update_json_post(client):
    """Test case for webhooks_update_json_post

    
    """
    body = openapi_server.WebhooksUpdate()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/webhooks/update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_whitelists_add_json_post(client):
    """Test case for whitelists_add_json_post

    
    """
    body = openapi_server.Email()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/whitelists/add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_whitelists_delete_json_post(client):
    """Test case for whitelists_delete_json_post

    
    """
    body = openapi_server.Email()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/whitelists/delete.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_whitelists_list_json_post(client):
    """Test case for whitelists_list_json_post

    
    """
    body = openapi_server.Email()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/whitelists/list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

