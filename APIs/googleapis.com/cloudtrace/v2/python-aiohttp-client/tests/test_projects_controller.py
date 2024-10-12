# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_write_spans_request import BatchWriteSpansRequest
from openapi_server.models.span import Span


pytestmark = pytest.mark.asyncio

async def test_cloudtrace_projects_traces_batch_write(client):
    """Test case for cloudtrace_projects_traces_batch_write

    
    """
    body = {"spans":[{"displayName":{"truncatedByteCount":0,"value":"value"},"spanKind":"SPAN_KIND_UNSPECIFIED","parentSpanId":"parentSpanId","spanId":"spanId","childSpanCount":1,"name":"name","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"links":{"droppedLinksCount":5,"link":[{"spanId":"spanId","traceId":"traceId","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"type":"TYPE_UNSPECIFIED"},{"spanId":"spanId","traceId":"traceId","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"type":"TYPE_UNSPECIFIED"}]},"startTime":"startTime","endTime":"endTime","sameProcessAsParentSpan":True,"stackTrace":{"stackFrames":{"droppedFramesCount":5,"frame":[{"fileName":{"truncatedByteCount":0,"value":"value"},"originalFunctionName":{"truncatedByteCount":0,"value":"value"},"columnNumber":"columnNumber","functionName":{"truncatedByteCount":0,"value":"value"},"sourceVersion":{"truncatedByteCount":0,"value":"value"},"loadModule":{"module":{"truncatedByteCount":0,"value":"value"},"buildId":{"truncatedByteCount":0,"value":"value"}},"lineNumber":"lineNumber"},{"fileName":{"truncatedByteCount":0,"value":"value"},"originalFunctionName":{"truncatedByteCount":0,"value":"value"},"columnNumber":"columnNumber","functionName":{"truncatedByteCount":0,"value":"value"},"sourceVersion":{"truncatedByteCount":0,"value":"value"},"loadModule":{"module":{"truncatedByteCount":0,"value":"value"},"buildId":{"truncatedByteCount":0,"value":"value"}},"lineNumber":"lineNumber"}]},"stackTraceHashId":"stackTraceHashId"},"timeEvents":{"droppedMessageEventsCount":9,"droppedAnnotationsCount":7,"timeEvent":[{"annotation":{"description":{"truncatedByteCount":0,"value":"value"},"attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6}},"messageEvent":{"compressedSizeBytes":"compressedSizeBytes","id":"id","type":"TYPE_UNSPECIFIED","uncompressedSizeBytes":"uncompressedSizeBytes"},"time":"time"},{"annotation":{"description":{"truncatedByteCount":0,"value":"value"},"attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6}},"messageEvent":{"compressedSizeBytes":"compressedSizeBytes","id":"id","type":"TYPE_UNSPECIFIED","uncompressedSizeBytes":"uncompressedSizeBytes"},"time":"time"}]},"status":{"code":2,"details":[{"key":""},{"key":""}],"message":"message"}},{"displayName":{"truncatedByteCount":0,"value":"value"},"spanKind":"SPAN_KIND_UNSPECIFIED","parentSpanId":"parentSpanId","spanId":"spanId","childSpanCount":1,"name":"name","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"links":{"droppedLinksCount":5,"link":[{"spanId":"spanId","traceId":"traceId","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"type":"TYPE_UNSPECIFIED"},{"spanId":"spanId","traceId":"traceId","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"type":"TYPE_UNSPECIFIED"}]},"startTime":"startTime","endTime":"endTime","sameProcessAsParentSpan":True,"stackTrace":{"stackFrames":{"droppedFramesCount":5,"frame":[{"fileName":{"truncatedByteCount":0,"value":"value"},"originalFunctionName":{"truncatedByteCount":0,"value":"value"},"columnNumber":"columnNumber","functionName":{"truncatedByteCount":0,"value":"value"},"sourceVersion":{"truncatedByteCount":0,"value":"value"},"loadModule":{"module":{"truncatedByteCount":0,"value":"value"},"buildId":{"truncatedByteCount":0,"value":"value"}},"lineNumber":"lineNumber"},{"fileName":{"truncatedByteCount":0,"value":"value"},"originalFunctionName":{"truncatedByteCount":0,"value":"value"},"columnNumber":"columnNumber","functionName":{"truncatedByteCount":0,"value":"value"},"sourceVersion":{"truncatedByteCount":0,"value":"value"},"loadModule":{"module":{"truncatedByteCount":0,"value":"value"},"buildId":{"truncatedByteCount":0,"value":"value"}},"lineNumber":"lineNumber"}]},"stackTraceHashId":"stackTraceHashId"},"timeEvents":{"droppedMessageEventsCount":9,"droppedAnnotationsCount":7,"timeEvent":[{"annotation":{"description":{"truncatedByteCount":0,"value":"value"},"attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6}},"messageEvent":{"compressedSizeBytes":"compressedSizeBytes","id":"id","type":"TYPE_UNSPECIFIED","uncompressedSizeBytes":"uncompressedSizeBytes"},"time":"time"},{"annotation":{"description":{"truncatedByteCount":0,"value":"value"},"attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6}},"messageEvent":{"compressedSizeBytes":"compressedSizeBytes","id":"id","type":"TYPE_UNSPECIFIED","uncompressedSizeBytes":"uncompressedSizeBytes"},"time":"time"}]},"status":{"code":2,"details":[{"key":""},{"key":""}],"message":"message"}}]}
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
        path='/v2/{name}/traces:batchWrite'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudtrace_projects_traces_spans_create_span(client):
    """Test case for cloudtrace_projects_traces_spans_create_span

    
    """
    body = {"displayName":{"truncatedByteCount":0,"value":"value"},"spanKind":"SPAN_KIND_UNSPECIFIED","parentSpanId":"parentSpanId","spanId":"spanId","childSpanCount":1,"name":"name","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"links":{"droppedLinksCount":5,"link":[{"spanId":"spanId","traceId":"traceId","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"type":"TYPE_UNSPECIFIED"},{"spanId":"spanId","traceId":"traceId","attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6},"type":"TYPE_UNSPECIFIED"}]},"startTime":"startTime","endTime":"endTime","sameProcessAsParentSpan":True,"stackTrace":{"stackFrames":{"droppedFramesCount":5,"frame":[{"fileName":{"truncatedByteCount":0,"value":"value"},"originalFunctionName":{"truncatedByteCount":0,"value":"value"},"columnNumber":"columnNumber","functionName":{"truncatedByteCount":0,"value":"value"},"sourceVersion":{"truncatedByteCount":0,"value":"value"},"loadModule":{"module":{"truncatedByteCount":0,"value":"value"},"buildId":{"truncatedByteCount":0,"value":"value"}},"lineNumber":"lineNumber"},{"fileName":{"truncatedByteCount":0,"value":"value"},"originalFunctionName":{"truncatedByteCount":0,"value":"value"},"columnNumber":"columnNumber","functionName":{"truncatedByteCount":0,"value":"value"},"sourceVersion":{"truncatedByteCount":0,"value":"value"},"loadModule":{"module":{"truncatedByteCount":0,"value":"value"},"buildId":{"truncatedByteCount":0,"value":"value"}},"lineNumber":"lineNumber"}]},"stackTraceHashId":"stackTraceHashId"},"timeEvents":{"droppedMessageEventsCount":9,"droppedAnnotationsCount":7,"timeEvent":[{"annotation":{"description":{"truncatedByteCount":0,"value":"value"},"attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6}},"messageEvent":{"compressedSizeBytes":"compressedSizeBytes","id":"id","type":"TYPE_UNSPECIFIED","uncompressedSizeBytes":"uncompressedSizeBytes"},"time":"time"},{"annotation":{"description":{"truncatedByteCount":0,"value":"value"},"attributes":{"attributeMap":{"key":{"stringValue":{"truncatedByteCount":0,"value":"value"},"intValue":"intValue","boolValue":True}},"droppedAttributesCount":6}},"messageEvent":{"compressedSizeBytes":"compressedSizeBytes","id":"id","type":"TYPE_UNSPECIFIED","uncompressedSizeBytes":"uncompressedSizeBytes"},"time":"time"}]},"status":{"code":2,"details":[{"key":""},{"key":""}],"message":"message"}}
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

