# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.feed_connection import FeedConnection
from openapi_server.models.feed_connections import FeedConnections
from openapi_server.models.statement import Statement
from openapi_server.models.statements import Statements


pytestmark = pytest.mark.asyncio

async def test_create_feed_connections(client):
    """Test case for create_feed_connections

    Create one or more new feed connection
    """
    body = {"pagination":{"pageCount":1,"pageSize":10,"page":1,"itemCount":2},"items":[{"accountId":"079a88ea-276d-41fb-a1f1-366ef3e22921","country":"GB","accountName":"Joe's Savings Account","accountType":"BANK","currency":"AUD","id":"00d3cf8d-95dc-4466-8dc0-47e6d1197e28","accountNumber":"3809087654321500","accountToken":"10000123","error":{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403},"status":"REJECTED"},{"accountId":"079a88ea-276d-41fb-a1f1-366ef3e22921","country":"GB","accountName":"Joe's Savings Account","accountType":"BANK","currency":"AUD","id":"00d3cf8d-95dc-4466-8dc0-47e6d1197e28","accountNumber":"3809087654321500","accountToken":"10000123","error":{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403},"status":"REJECTED"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bankfeeds.xro/1.0/FeedConnections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_statements(client):
    """Test case for create_statements

    Creates one or more new statements
    """
    body = {"pagination":{"pageCount":1,"pageSize":10,"page":1,"itemCount":2},"items":[{"statementLines":[{"reference":"Reference for statement line 2","payeeName":"Payee name for statement line 2","amount":5.0,"description":"Description for statement line 2","chequeNumber":"021","transactionId":"transaction-id-2","postedDate":"2018-06-10"},{"reference":"Reference for statement line 2","payeeName":"Payee name for statement line 2","amount":5.0,"description":"Description for statement line 2","chequeNumber":"021","transactionId":"transaction-id-2","postedDate":"2018-06-10"}],"endDate":"2018-07-27","endBalance":{"amount":10.134,"creditDebitIndicator":"CREDIT"},"statementLineCount":1,"id":"ba4f3127-5e46-427d-80ea-dea2fcd26afe","feedConnectionId":"87cb0dc8-fa32-409c-b622-19f8de8dcc83","errors":[{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403},{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403}],"startBalance":{"amount":9.0},"startDate":"2018-07-27","status":"PENDING"},{"statementLines":[{"reference":"Reference for statement line 2","payeeName":"Payee name for statement line 2","amount":5.0,"description":"Description for statement line 2","chequeNumber":"021","transactionId":"transaction-id-2","postedDate":"2018-06-10"},{"reference":"Reference for statement line 2","payeeName":"Payee name for statement line 2","amount":5.0,"description":"Description for statement line 2","chequeNumber":"021","transactionId":"transaction-id-2","postedDate":"2018-06-10"}],"endDate":"2018-07-27","endBalance":{"amount":10.134,"creditDebitIndicator":"CREDIT"},"statementLineCount":1,"id":"ba4f3127-5e46-427d-80ea-dea2fcd26afe","feedConnectionId":"87cb0dc8-fa32-409c-b622-19f8de8dcc83","errors":[{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403},{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403}],"startBalance":{"amount":9.0},"startDate":"2018-07-27","status":"PENDING"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bankfeeds.xro/1.0/Statements',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_feed_connections(client):
    """Test case for delete_feed_connections

    Delete an existing feed connection
    """
    body = {"pagination":{"pageCount":1,"pageSize":10,"page":1,"itemCount":2},"items":[{"accountId":"079a88ea-276d-41fb-a1f1-366ef3e22921","country":"GB","accountName":"Joe's Savings Account","accountType":"BANK","currency":"AUD","id":"00d3cf8d-95dc-4466-8dc0-47e6d1197e28","accountNumber":"3809087654321500","accountToken":"10000123","error":{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403},"status":"REJECTED"},{"accountId":"079a88ea-276d-41fb-a1f1-366ef3e22921","country":"GB","accountName":"Joe's Savings Account","accountType":"BANK","currency":"AUD","id":"00d3cf8d-95dc-4466-8dc0-47e6d1197e28","accountNumber":"3809087654321500","accountToken":"10000123","error":{"detail":"The application has not been configured to use these API endpoints.","title":"Invalid Application","type":"invalid-application","status":403},"status":"REJECTED"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/bankfeeds.xro/1.0/FeedConnections/DeleteRequests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feed_connection(client):
    """Test case for get_feed_connection

    Retrieve single feed connection based on a unique id provided
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bankfeeds.xro/1.0/FeedConnections/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feed_connections(client):
    """Test case for get_feed_connections

    Searches for feed connections
    """
    params = [('page', 1),
                    ('pageSize', 100)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bankfeeds.xro/1.0/FeedConnections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statement(client):
    """Test case for get_statement

    Retrieve single statement based on unique id provided
    """
    params = [('statementId', 'statement_id_example')]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bankfeeds.xro/1.0/Statements/{statement_id}'.format(statement_id2='statement_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statements(client):
    """Test case for get_statements

    Retrieve all statements
    """
    params = [('page', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'xero_application_id': '00000000-0000-0000-0000-0000000010000',
        'xero_user_id': '00000000-0000-0000-0000-0000030000000',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/bankfeeds.xro/1.0/Statements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

