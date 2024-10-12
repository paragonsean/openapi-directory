# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_queries_response import ListQueriesResponse
from openapi_server.models.query import Query
from openapi_server.models.run_query_request import RunQueryRequest


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_createquery(client):
    """Test case for doubleclickbidmanager_queries_createquery

    
    """
    body = {"reportDataStartTimeMs":"reportDataStartTimeMs","schedule":{"nextRunMinuteOfDay":6,"startTimeMs":"startTimeMs","endTimeMs":"endTimeMs","nextRunTimezoneCode":"nextRunTimezoneCode","frequency":"ONE_TIME"},"metadata":{"googleCloudStoragePathForLatestReport":"googleCloudStoragePathForLatestReport","running":True,"dataRange":"CUSTOM_DATES","googleDrivePathForLatestReport":"googleDrivePathForLatestReport","format":"CSV","shareEmailAddress":["shareEmailAddress","shareEmailAddress"],"reportCount":0,"latestReportRunTimeMs":"latestReportRunTimeMs","sendNotification":True,"locale":"locale","title":"title"},"kind":"kind","reportDataEndTimeMs":"reportDataEndTimeMs","params":{"includeInviteData":True,"groupBys":["FILTER_UNKNOWN","FILTER_UNKNOWN"],"options":{"pathQueryOptions":{"pathFilters":[{"eventFilters":[{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}}],"pathMatchPosition":"ANY"},{"eventFilters":[{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}}],"pathMatchPosition":"ANY"}],"channelGrouping":{"name":"name","rules":[{"disjunctiveMatchStatements":[{"eventFilters":[{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}}]},{"eventFilters":[{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}}]}],"name":"name"},{"disjunctiveMatchStatements":[{"eventFilters":[{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}}]},{"eventFilters":[{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"FILTER_UNKNOWN","values":["values","values"],"match":"UNKNOWN"}}]}],"name":"name"}],"fallbackName":"fallbackName"}},"includeOnlyTargetedUserLists":True},"filters":[{"type":"FILTER_UNKNOWN","value":"value"},{"type":"FILTER_UNKNOWN","value":"value"}],"metrics":["METRIC_UNKNOWN","METRIC_UNKNOWN"],"type":"TYPE_GENERAL"},"timezoneCode":"timezoneCode","queryId":"queryId"}
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
                    ('asynchronous', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/doubleclickbidmanager/v1.1/query',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_deletequery(client):
    """Test case for doubleclickbidmanager_queries_deletequery

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/doubleclickbidmanager/v1.1/query/{query_id}'.format(query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_getquery(client):
    """Test case for doubleclickbidmanager_queries_getquery

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/doubleclickbidmanager/v1.1/query/{query_id}'.format(query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_listqueries(client):
    """Test case for doubleclickbidmanager_queries_listqueries

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/doubleclickbidmanager/v1.1/queries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_runquery(client):
    """Test case for doubleclickbidmanager_queries_runquery

    
    """
    body = {"reportDataStartTimeMs":"reportDataStartTimeMs","dataRange":"CUSTOM_DATES","reportDataEndTimeMs":"reportDataEndTimeMs","timezoneCode":"timezoneCode"}
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
                    ('asynchronous', True)]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/doubleclickbidmanager/v1.1/query/{query_id}'.format(query_id='query_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

