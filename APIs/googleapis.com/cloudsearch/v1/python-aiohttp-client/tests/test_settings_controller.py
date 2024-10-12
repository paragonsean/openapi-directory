# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_settings import CustomerSettings
from openapi_server.models.data_source import DataSource
from openapi_server.models.list_data_source_response import ListDataSourceResponse
from openapi_server.models.list_search_applications_response import ListSearchApplicationsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.reset_search_application_request import ResetSearchApplicationRequest
from openapi_server.models.search_application import SearchApplication


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_datasources_create(client):
    """Test case for cloudsearch_settings_datasources_create

    
    """
    body = {"disableModifications":True,"disableServing":True,"itemsVisibility":[{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"},{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}],"displayName":"displayName","indexingServiceAccounts":["indexingServiceAccounts","indexingServiceAccounts"],"name":"name","operationIds":["operationIds","operationIds"],"shortName":"shortName","returnThumbnailUrls":True}
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
        path='/v1/settings/datasources',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_datasources_list(client):
    """Test case for cloudsearch_settings_datasources_list

    
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
                    ('debugOptions.enableDebugging', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/settings/datasources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_get_customer(client):
    """Test case for cloudsearch_settings_get_customer

    
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
        path='/v1/settings/customer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_searchapplications_create(client):
    """Test case for cloudsearch_settings_searchapplications_create

    
    """
    body = {"enableAuditLog":True,"sourceConfig":[{"scoringConfig":{"sourceImportance":"DEFAULT"},"crowdingConfig":{"numSuggestions":6,"numResults":0},"source":{"name":"name","predefinedSource":"NONE"}},{"scoringConfig":{"sourceImportance":"DEFAULT"},"crowdingConfig":{"numSuggestions":6,"numResults":0},"source":{"name":"name","predefinedSource":"NONE"}}],"scoringConfig":{"disablePersonalization":True,"disableFreshness":True},"dataSourceRestrictions":[{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]},{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]}],"displayName":"displayName","returnResultThumbnailUrls":True,"defaultFacetOptions":[{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"},{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"}],"name":"name","queryInterpretationConfig":{"forceVerbatimMode":True,"forceDisableSupplementalResults":True},"operationIds":["operationIds","operationIds"],"defaultSortOptions":{"sortOrder":"ASCENDING","operatorName":"operatorName"}}
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
        path='/v1/settings/searchapplications',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_searchapplications_delete(client):
    """Test case for cloudsearch_settings_searchapplications_delete

    
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
                    ('debugOptions.enableDebugging', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/settings/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_searchapplications_get(client):
    """Test case for cloudsearch_settings_searchapplications_get

    
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
                    ('debugOptions.enableDebugging', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/settings/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_searchapplications_list(client):
    """Test case for cloudsearch_settings_searchapplications_list

    
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
                    ('debugOptions.enableDebugging', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/settings/searchapplications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_searchapplications_patch(client):
    """Test case for cloudsearch_settings_searchapplications_patch

    
    """
    body = {"enableAuditLog":True,"sourceConfig":[{"scoringConfig":{"sourceImportance":"DEFAULT"},"crowdingConfig":{"numSuggestions":6,"numResults":0},"source":{"name":"name","predefinedSource":"NONE"}},{"scoringConfig":{"sourceImportance":"DEFAULT"},"crowdingConfig":{"numSuggestions":6,"numResults":0},"source":{"name":"name","predefinedSource":"NONE"}}],"scoringConfig":{"disablePersonalization":True,"disableFreshness":True},"dataSourceRestrictions":[{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]},{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]}],"displayName":"displayName","returnResultThumbnailUrls":True,"defaultFacetOptions":[{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"},{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"}],"name":"name","queryInterpretationConfig":{"forceVerbatimMode":True,"forceDisableSupplementalResults":True},"operationIds":["operationIds","operationIds"],"defaultSortOptions":{"sortOrder":"ASCENDING","operatorName":"operatorName"}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/settings/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_searchapplications_reset(client):
    """Test case for cloudsearch_settings_searchapplications_reset

    
    """
    body = {"debugOptions":{"enableDebugging":True}}
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
        path='/v1/settings/{namerese}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_searchapplications_update(client):
    """Test case for cloudsearch_settings_searchapplications_update

    
    """
    body = {"enableAuditLog":True,"sourceConfig":[{"scoringConfig":{"sourceImportance":"DEFAULT"},"crowdingConfig":{"numSuggestions":6,"numResults":0},"source":{"name":"name","predefinedSource":"NONE"}},{"scoringConfig":{"sourceImportance":"DEFAULT"},"crowdingConfig":{"numSuggestions":6,"numResults":0},"source":{"name":"name","predefinedSource":"NONE"}}],"scoringConfig":{"disablePersonalization":True,"disableFreshness":True},"dataSourceRestrictions":[{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]},{"source":{"name":"name","predefinedSource":"NONE"},"filterOptions":[{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"},{"filter":{"valueFilter":{"operatorName":"operatorName","value":{"dateValue":{"month":5,"year":5,"day":1},"stringValue":"stringValue","timestampValue":"timestampValue","booleanValue":True,"integerValue":"integerValue","doubleValue":6.027456183070403}},"compositeFilter":{"subFilters":[null,null],"logicOperator":"AND"}},"objectType":"objectType"}]}],"displayName":"displayName","returnResultThumbnailUrls":True,"defaultFacetOptions":[{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"},{"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"numFacetBuckets":0,"sourceName":"sourceName","operatorName":"operatorName","objectType":"objectType"}],"name":"name","queryInterpretationConfig":{"forceVerbatimMode":True,"forceDisableSupplementalResults":True},"operationIds":["operationIds","operationIds"],"defaultSortOptions":{"sortOrder":"ASCENDING","operatorName":"operatorName"}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/settings/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_settings_update_customer(client):
    """Test case for cloudsearch_settings_update_customer

    
    """
    body = {"vpcSettings":{"project":"project"},"auditLoggingSettings":{"logDataReadActions":True,"logDataWriteActions":True,"project":"project","logAdminReadActions":True}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/settings/customer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

