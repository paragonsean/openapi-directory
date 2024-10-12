# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_query_sources_response import ListQuerySourcesResponse
from openapi_server.models.remove_activity_request import RemoveActivityRequest
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.suggest_request import SuggestRequest
from openapi_server.models.suggest_response import SuggestResponse


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_query_remove_activity(client):
    """Test case for cloudsearch_query_remove_activity

    
    """
    body = {"requestOptions":{"debugOptions":{"enableDebugging":True},"searchApplicationId":"searchApplicationId","timeZone":"timeZone","languageCode":"languageCode"},"userActivity":{"queryActivity":{"query":"query"}}}
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
        path='/v1/query:removeActivity',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_query_search(client):
    """Test case for cloudsearch_query_search

    
    """
    body = {"dataSourceRestrictions":[{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]},{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]}],"queryInterpretationOptions":{"disableSupplementalResults":True,"enableVerbatimMode":True,"disableNlInterpretation":True},"sortOptions":{"sortOrder":"ASCENDING","operatorName":"operatorName"},"query":"query","contextAttributes":[{"values":["values","values"],"name":"name"},{"values":["values","values"],"name":"name"}],"start":1,"pageSize":6,"facetOptions":[{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"},{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"}],"requestOptions":{"debugOptions":{"enableDebugging":True},"searchApplicationId":"searchApplicationId","timeZone":"timeZone","languageCode":"languageCode"}}
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
        path='/v1/query/search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_query_sources_list(client):
    """Test case for cloudsearch_query_sources_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('requestOptions.debugOptions.enableDebugging', True),
                    ('requestOptions.languageCode', 'request_options_language_code_example'),
                    ('requestOptions.searchApplicationId', 'request_options_search_application_id_example'),
                    ('requestOptions.timeZone', 'request_options_time_zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/query/sources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_query_suggest(client):
    """Test case for cloudsearch_query_suggest

    
    """
    body = {"dataSourceRestrictions":[{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]},{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]}],"query":"query","requestOptions":{"debugOptions":{"enableDebugging":True},"searchApplicationId":"searchApplicationId","timeZone":"timeZone","languageCode":"languageCode"}}
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
        path='/v1/query/suggest',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

