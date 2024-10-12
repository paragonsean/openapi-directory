# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_issue_property_update_request import BulkIssuePropertyUpdateRequest
from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.issue_entity_properties import IssueEntityProperties
from openapi_server.models.issue_filter_for_bulk_property_delete import IssueFilterForBulkPropertyDelete
from openapi_server.models.multi_issue_entity_properties import MultiIssueEntityProperties
from openapi_server.models.property_keys import PropertyKeys


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_issue_property(client):
    """Test case for bulk_delete_issue_property

    Bulk delete issue property
    """
    body = {"currentValue":"","entityIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_set_issue_properties_by_issue(client):
    """Test case for bulk_set_issue_properties_by_issue

    Bulk set issue properties by issue
    """
    body = {"issues":[{"issueID":0,"properties":{"key":{"valueAsDouble":9.301444243932576,"numberType":"INT","fieldNames":"{}","decimalValue":1.4658129805029452,"valueAsBoolean":True,"valueNode":True,"long":True,"longValue":2,"valueAsInt":3,"missingNode":True,"number":True,"valueAsText":"valueAsText","array":True,"containerNode":True,"numberValue":7.061401241503109,"bigDecimal":True,"valueAsLong":2,"integralNumber":True,"textValue":"textValue","double":True,"intValue":5,"bigInteger":True,"doubleValue":5.962133916683182,"floatingPointNumber":True,"int":True,"textual":True,"pojo":True,"bigIntegerValue":6,"boolean":True,"null":True,"binary":True,"elements":"{}","booleanValue":True,"fields":"{}","binaryValue":["binaryValue","binaryValue"],"object":True}}},{"issueID":0,"properties":{"key":{"valueAsDouble":9.301444243932576,"numberType":"INT","fieldNames":"{}","decimalValue":1.4658129805029452,"valueAsBoolean":True,"valueNode":True,"long":True,"longValue":2,"valueAsInt":3,"missingNode":True,"number":True,"valueAsText":"valueAsText","array":True,"containerNode":True,"numberValue":7.061401241503109,"bigDecimal":True,"valueAsLong":2,"integralNumber":True,"textValue":"textValue","double":True,"intValue":5,"bigInteger":True,"doubleValue":5.962133916683182,"floatingPointNumber":True,"int":True,"textual":True,"pojo":True,"bigIntegerValue":6,"boolean":True,"null":True,"binary":True,"elements":"{}","booleanValue":True,"fields":"{}","binaryValue":["binaryValue","binaryValue"],"object":True}}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/properties/multi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_set_issue_property(client):
    """Test case for bulk_set_issue_property

    Bulk set issue property
    """
    body = {"filter":"","expression":"expression","value":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_set_issues_properties_list(client):
    """Test case for bulk_set_issues_properties_list

    Bulk set issues properties by list
    """
    body = {"entitiesIds":[0,0,0,0,0],"properties":{"key":{"valueAsDouble":9.301444243932576,"numberType":"INT","fieldNames":"{}","decimalValue":1.4658129805029452,"valueAsBoolean":True,"valueNode":True,"long":True,"longValue":2,"valueAsInt":3,"missingNode":True,"number":True,"valueAsText":"valueAsText","array":True,"containerNode":True,"numberValue":7.061401241503109,"bigDecimal":True,"valueAsLong":2,"integralNumber":True,"textValue":"textValue","double":True,"intValue":5,"bigInteger":True,"doubleValue":5.962133916683182,"floatingPointNumber":True,"int":True,"textual":True,"pojo":True,"bigIntegerValue":6,"boolean":True,"null":True,"binary":True,"elements":"{}","booleanValue":True,"fields":"{}","binaryValue":["binaryValue","binaryValue"],"object":True}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/properties',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue_property(client):
    """Test case for delete_issue_property

    Delete issue property
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_property(client):
    """Test case for get_issue_property

    Get issue property
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_property_keys(client):
    """Test case for get_issue_property_keys

    Get issue property keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/properties'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_issue_property(client):
    """Test case for set_issue_property

    Set issue property
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/{issue_id_or_key}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

