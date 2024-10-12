# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.copy_log_entries_request import CopyLogEntriesRequest
from openapi_server.models.list_log_entries_request import ListLogEntriesRequest
from openapi_server.models.list_log_entries_response import ListLogEntriesResponse
from openapi_server.models.operation import Operation
from openapi_server.models.tail_log_entries_request import TailLogEntriesRequest
from openapi_server.models.tail_log_entries_response import TailLogEntriesResponse
from openapi_server.models.write_log_entries_request import WriteLogEntriesRequest


pytestmark = pytest.mark.asyncio

async def test_logging_entries_copy(client):
    """Test case for logging_entries_copy

    
    """
    body = {"filter":"filter","destination":"destination","name":"name"}
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
        path='/v2/entries:copy',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logging_entries_list(client):
    """Test case for logging_entries_list

    
    """
    body = {"filter":"filter","resourceNames":["resourceNames","resourceNames"],"orderBy":"orderBy","pageSize":0,"pageToken":"pageToken","projectIds":["projectIds","projectIds"]}
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
        path='/v2/entries:list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logging_entries_tail(client):
    """Test case for logging_entries_tail

    
    """
    body = {"filter":"filter","resourceNames":["resourceNames","resourceNames"],"bufferWindow":"bufferWindow"}
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
        path='/v2/entries:tail',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logging_entries_write(client):
    """Test case for logging_entries_write

    
    """
    body = {"entries":[{"severity":"DEFAULT","metadata":{"systemLabels":{"key":""},"userLabels":{"key":"userLabels"}},"traceSampled":True,"resource":{"type":"type","labels":{"key":"labels"}},"protoPayload":{"key":""},"textPayload":"textPayload","receiveTimestamp":"receiveTimestamp","errorGroups":[{"id":"id"},{"id":"id"}],"labels":{"key":"labels"},"spanId":"spanId","trace":"trace","split":{"totalSplits":1,"uid":"uid","index":6},"logName":"logName","jsonPayload":{"key":""},"httpRequest":{"referer":"referer","remoteIp":"remoteIp","latency":"latency","requestMethod":"requestMethod","responseSize":"responseSize","userAgent":"userAgent","cacheLookup":True,"protocol":"protocol","requestUrl":"requestUrl","cacheHit":True,"serverIp":"serverIp","cacheValidatedWithOriginServer":True,"requestSize":"requestSize","cacheFillBytes":"cacheFillBytes","status":0},"sourceLocation":{"file":"file","line":"line","function":"function"},"operation":{"last":True,"producer":"producer","id":"id","first":True},"insertId":"insertId","timestamp":"timestamp"},{"severity":"DEFAULT","metadata":{"systemLabels":{"key":""},"userLabels":{"key":"userLabels"}},"traceSampled":True,"resource":{"type":"type","labels":{"key":"labels"}},"protoPayload":{"key":""},"textPayload":"textPayload","receiveTimestamp":"receiveTimestamp","errorGroups":[{"id":"id"},{"id":"id"}],"labels":{"key":"labels"},"spanId":"spanId","trace":"trace","split":{"totalSplits":1,"uid":"uid","index":6},"logName":"logName","jsonPayload":{"key":""},"httpRequest":{"referer":"referer","remoteIp":"remoteIp","latency":"latency","requestMethod":"requestMethod","responseSize":"responseSize","userAgent":"userAgent","cacheLookup":True,"protocol":"protocol","requestUrl":"requestUrl","cacheHit":True,"serverIp":"serverIp","cacheValidatedWithOriginServer":True,"requestSize":"requestSize","cacheFillBytes":"cacheFillBytes","status":0},"sourceLocation":{"file":"file","line":"line","function":"function"},"operation":{"last":True,"producer":"producer","id":"id","first":True},"insertId":"insertId","timestamp":"timestamp"}],"dryRun":True,"logName":"logName","resource":{"type":"type","labels":{"key":"labels"}},"partialSuccess":True,"labels":{"key":"labels"}}
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
        path='/v2/entries:write',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

