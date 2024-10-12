# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_complete_suggestions import AutoCompleteSuggestions
from openapi_server.models.converted_jql_queries import ConvertedJQLQueries
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.jql_personal_data_migration_request import JQLPersonalDataMigrationRequest
from openapi_server.models.jql_reference_data import JQLReferenceData
from openapi_server.models.jql_queries_to_parse import JqlQueriesToParse
from openapi_server.models.jql_queries_to_sanitize import JqlQueriesToSanitize
from openapi_server.models.parsed_jql_queries import ParsedJqlQueries
from openapi_server.models.sanitized_jql_queries import SanitizedJqlQueries
from openapi_server.models.search_auto_complete_filter import SearchAutoCompleteFilter


pytestmark = pytest.mark.asyncio

async def test_get_auto_complete(client):
    """Test case for get_auto_complete

    Get field reference data (GET)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/jql/autocompletedata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_auto_complete_post(client):
    """Test case for get_auto_complete_post

    Get field reference data (POST)
    """
    body = {"projectIds":[0,0],"includeCollapsedFields":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/jql/autocompletedata',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_auto_complete_for_query_string(client):
    """Test case for get_field_auto_complete_for_query_string

    Get field auto complete suggestions
    """
    params = [('fieldName', 'reporter'),
                    ('fieldValue', 'field_value_example'),
                    ('predicateName', 'predicate_name_example'),
                    ('predicateValue', 'predicate_value_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/jql/autocompletedata/suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrate_queries(client):
    """Test case for migrate_queries

    Convert user identifiers to account IDs in JQL queries
    """
    body = {"queryStrings":["queryStrings","queryStrings"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/jql/pdcleaner',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_jql_queries(client):
    """Test case for parse_jql_queries

    Parse JQL query
    """
    body = {"queries":["queries","queries"]}
    params = [('validation', strict)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/jql/parse',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sanitise_jql_queries(client):
    """Test case for sanitise_jql_queries

    Sanitize JQL queries
    """
    body = {"queries":[{"accountId":"accountId","query":"query"},{"accountId":"accountId","query":"query"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/jql/sanitize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

