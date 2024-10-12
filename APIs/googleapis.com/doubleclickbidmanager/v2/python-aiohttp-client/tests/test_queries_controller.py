# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_queries_response import ListQueriesResponse
from openapi_server.models.list_reports_response import ListReportsResponse
from openapi_server.models.query import Query
from openapi_server.models.report import Report
from openapi_server.models.run_query_request import RunQueryRequest


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_create(client):
    """Test case for doubleclickbidmanager_queries_create

    
    """
    body = {"schedule":{"endDate":{"month":6,"year":1,"day":0},"nextRunTimezoneCode":"nextRunTimezoneCode","startDate":{"month":6,"year":1,"day":0},"frequency":"FREQUENCY_UNSPECIFIED"},"metadata":{"dataRange":{"customEndDate":{"month":6,"year":1,"day":0},"range":"RANGE_UNSPECIFIED","customStartDate":{"month":6,"year":1,"day":0}},"format":"FORMAT_UNSPECIFIED","shareEmailAddress":["shareEmailAddress","shareEmailAddress"],"sendNotification":True,"title":"title"},"params":{"groupBys":["groupBys","groupBys"],"options":{"pathQueryOptions":{"pathFilters":[{"eventFilters":[{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}}],"pathMatchPosition":"PATH_MATCH_POSITION_UNSPECIFIED"},{"eventFilters":[{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}}],"pathMatchPosition":"PATH_MATCH_POSITION_UNSPECIFIED"}],"channelGrouping":{"name":"name","rules":[{"disjunctiveMatchStatements":[{"eventFilters":[{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}}]},{"eventFilters":[{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}}]}],"name":"name"},{"disjunctiveMatchStatements":[{"eventFilters":[{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}}]},{"eventFilters":[{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}},{"dimensionFilter":{"filter":"filter","values":["values","values"],"match":"UNKNOWN"}}]}],"name":"name"}],"fallbackName":"fallbackName"}},"includeOnlyTargetedUserLists":True},"filters":[{"type":"type","value":"value"},{"type":"type","value":"value"}],"metrics":["metrics","metrics"],"type":"REPORT_TYPE_UNSPECIFIED"},"queryId":"queryId"}
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
        path='/v2/queries',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_delete(client):
    """Test case for doubleclickbidmanager_queries_delete

    
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
        path='/v2/queries/{query_id}'.format(query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_get(client):
    """Test case for doubleclickbidmanager_queries_get

    
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
        path='/v2/queries/{query_id}'.format(query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_list(client):
    """Test case for doubleclickbidmanager_queries_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/queries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_reports_get(client):
    """Test case for doubleclickbidmanager_queries_reports_get

    
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
        path='/v2/queries/{query_id}/reports/{report_id}'.format(query_id='query_id_example', report_id='report_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_reports_list(client):
    """Test case for doubleclickbidmanager_queries_reports_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/queries/{query_id}/reports'.format(query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_doubleclickbidmanager_queries_run(client):
    """Test case for doubleclickbidmanager_queries_run

    
    """
    body = {"dataRange":{"customEndDate":{"month":6,"year":1,"day":0},"range":"RANGE_UNSPECIFIED","customStartDate":{"month":6,"year":1,"day":0}}}
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
                    ('synchronous', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/queries/{query_idru}'.format(query_id='query_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

