# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_analytics_admin_v1beta_list_accounts_response import GoogleAnalyticsAdminV1betaListAccountsResponse
from openapi_server.models.google_analytics_admin_v1beta_provision_account_ticket_request import GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest
from openapi_server.models.google_analytics_admin_v1beta_provision_account_ticket_response import GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse
from openapi_server.models.google_analytics_admin_v1beta_search_change_history_events_request import GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest
from openapi_server.models.google_analytics_admin_v1beta_search_change_history_events_response import GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_accounts_list(client):
    """Test case for analyticsadmin_accounts_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_accounts_provision_account_ticket(client):
    """Test case for analyticsadmin_accounts_provision_account_ticket

    
    """
    body = {"redirectUri":"redirectUri","account":{"regionCode":"regionCode","deleted":True,"createTime":"createTime","displayName":"displayName","name":"name","updateTime":"updateTime"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/accounts:provisionAccountTicket',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analyticsadmin_accounts_search_change_history_events(client):
    """Test case for analyticsadmin_accounts_search_change_history_events

    
    """
    body = {"earliestChangeTime":"earliestChangeTime","property":"property","action":["ACTION_TYPE_UNSPECIFIED","ACTION_TYPE_UNSPECIFIED"],"actorEmail":["actorEmail","actorEmail"],"pageSize":0,"pageToken":"pageToken","latestChangeTime":"latestChangeTime","resourceType":["CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED","CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{accountsearch_change_history_event}'.format(account='account_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

