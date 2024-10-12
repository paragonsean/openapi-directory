# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_queue_items_request import DeleteQueueItemsRequest
from openapi_server.models.index_item_request import IndexItemRequest
from openapi_server.models.item import Item
from openapi_server.models.list_items_response import ListItemsResponse
from openapi_server.models.model_schema import ModelSchema
from openapi_server.models.operation import Operation
from openapi_server.models.poll_items_request import PollItemsRequest
from openapi_server.models.poll_items_response import PollItemsResponse
from openapi_server.models.push_item_request import PushItemRequest
from openapi_server.models.start_upload_item_request import StartUploadItemRequest
from openapi_server.models.unreserve_items_request import UnreserveItemsRequest
from openapi_server.models.update_schema_request import UpdateSchemaRequest
from openapi_server.models.upload_item_ref import UploadItemRef


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_delete_schema(client):
    """Test case for cloudsearch_indexing_datasources_delete_schema

    
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
        path='/v1/indexing/{name}/schema'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_get_schema(client):
    """Test case for cloudsearch_indexing_datasources_get_schema

    
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
        path='/v1/indexing/{name}/schema'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_delete(client):
    """Test case for cloudsearch_indexing_datasources_items_delete

    
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
                    ('connectorName', 'connector_name_example'),
                    ('debugOptions.enableDebugging', True),
                    ('mode', 'mode_example'),
                    ('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/indexing/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_delete_queue_items(client):
    """Test case for cloudsearch_indexing_datasources_items_delete_queue_items

    
    """
    body = {"debugOptions":{"enableDebugging":True},"connectorName":"connectorName","queue":"queue"}
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
        path='/v1/indexing/{name}/items:deleteQueueItems'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_get(client):
    """Test case for cloudsearch_indexing_datasources_items_get

    
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
                    ('connectorName', 'connector_name_example'),
                    ('debugOptions.enableDebugging', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/indexing/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_index(client):
    """Test case for cloudsearch_indexing_datasources_items_index

    
    """
    body = {"debugOptions":{"enableDebugging":True},"mode":"UNSPECIFIED","item":{"itemType":"UNSPECIFIED","metadata":{"keywords":["keywords","keywords"],"contextAttributes":[{"values":["values","values"],"name":"name"},{"values":["values","values"],"name":"name"}],"updateTime":"updateTime","mimeType":"mimeType","sourceRepositoryUrl":"sourceRepositoryUrl","title":"title","interactions":[{"principal":{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}},"interactionTime":"interactionTime","type":"UNSPECIFIED"},{"principal":{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}},"interactionTime":"interactionTime","type":"UNSPECIFIED"}],"objectType":"objectType","createTime":"createTime","containerName":"containerName","searchQualityMetadata":{"quality":0.8008281904610115},"contentLanguage":"contentLanguage","hash":"hash"},"payload":"payload","name":"name","acl":{"aclInheritanceType":"NOT_APPLICABLE","readers":[{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}},{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}}],"deniedReaders":[{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}},{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}}],"inheritAclFrom":"inheritAclFrom","owners":[{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}},{"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}}]},"version":"version","content":{"contentDataRef":{"name":"name"},"contentFormat":"UNSPECIFIED","inlineContent":"inlineContent","hash":"hash"},"queue":"queue","structuredData":{"hash":"hash","object":{"properties":[{"timestampValues":{"values":["values","values"]},"doubleValues":{"values":[2.3021358869347655,2.3021358869347655]},"dateValues":{"values":[{"month":5,"year":5,"day":1},{"month":5,"year":5,"day":1}]},"name":"name","booleanValue":True,"objectValues":{"values":[null,null]},"integerValues":{"values":["values","values"]},"htmlValues":{"values":["values","values"]},"textValues":{"values":["values","values"]},"enumValues":{"values":["values","values"]}},{"timestampValues":{"values":["values","values"]},"doubleValues":{"values":[2.3021358869347655,2.3021358869347655]},"dateValues":{"values":[{"month":5,"year":5,"day":1},{"month":5,"year":5,"day":1}]},"name":"name","booleanValue":True,"objectValues":{"values":[null,null]},"integerValues":{"values":["values","values"]},"htmlValues":{"values":["values","values"]},"textValues":{"values":["values","values"]},"enumValues":{"values":["values","values"]}}]}},"status":{"code":"CODE_UNSPECIFIED","processingErrors":[{"fieldViolations":[{"field":"field","description":"description"},{"field":"field","description":"description"}],"code":"PROCESSING_ERROR_CODE_UNSPECIFIED","errorMessage":"errorMessage"},{"fieldViolations":[{"field":"field","description":"description"},{"field":"field","description":"description"}],"code":"PROCESSING_ERROR_CODE_UNSPECIFIED","errorMessage":"errorMessage"}],"repositoryErrors":[{"errorMessage":"errorMessage","type":"UNKNOWN","httpStatusCode":6},{"errorMessage":"errorMessage","type":"UNKNOWN","httpStatusCode":6}]}},"connectorName":"connectorName","indexItemOptions":{"allowUnknownGsuitePrincipals":True}}
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
        path='/v1/indexing/{nameinde}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_list(client):
    """Test case for cloudsearch_indexing_datasources_items_list

    
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
                    ('brief', True),
                    ('connectorName', 'connector_name_example'),
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
        path='/v1/indexing/{name}/items'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_poll(client):
    """Test case for cloudsearch_indexing_datasources_items_poll

    
    """
    body = {"debugOptions":{"enableDebugging":True},"statusCodes":["CODE_UNSPECIFIED","CODE_UNSPECIFIED"],"limit":0,"connectorName":"connectorName","queue":"queue"}
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
        path='/v1/indexing/{name}/items:poll'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_push(client):
    """Test case for cloudsearch_indexing_datasources_items_push

    
    """
    body = {"debugOptions":{"enableDebugging":True},"item":{"payload":"payload","repositoryError":{"errorMessage":"errorMessage","type":"UNKNOWN","httpStatusCode":6},"type":"UNSPECIFIED","metadataHash":"metadataHash","queue":"queue","contentHash":"contentHash","structuredDataHash":"structuredDataHash"},"connectorName":"connectorName"}
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
        path='/v1/indexing/{namepus}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_unreserve(client):
    """Test case for cloudsearch_indexing_datasources_items_unreserve

    
    """
    body = {"debugOptions":{"enableDebugging":True},"connectorName":"connectorName","queue":"queue"}
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
        path='/v1/indexing/{name}/items:unreserve'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_items_upload(client):
    """Test case for cloudsearch_indexing_datasources_items_upload

    
    """
    body = {"debugOptions":{"enableDebugging":True},"connectorName":"connectorName"}
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
        path='/v1/indexing/{nameuploa}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_indexing_datasources_update_schema(client):
    """Test case for cloudsearch_indexing_datasources_update_schema

    
    """
    body = {"debugOptions":{"enableDebugging":True},"schema":{"operationIds":["operationIds","operationIds"],"objectDefinitions":[{"propertyDefinitions":[{"isFacetable":True,"isWildcardSearchable":True,"booleanPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"enumPropertyOptions":{"possibleValues":[{"stringValue":"stringValue","integerValue":0},{"stringValue":"stringValue","integerValue":0}],"operatorOptions":{"operatorName":"operatorName"},"orderedRanking":"NO_ORDER"},"isSortable":True,"textPropertyOptions":{"operatorOptions":{"exactMatchWithOperator":True,"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"doublePropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"integerPropertyOptions":{"minimumValue":"minimumValue","operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"},"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"orderedRanking":"NO_ORDER","maximumValue":"maximumValue"},"objectPropertyOptions":{"subobjectProperties":[null,null]},"datePropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"displayOptions":{"displayLabel":"displayLabel"},"isReturnable":True,"isRepeatable":True,"isSuggestable":True,"htmlPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"timestampPropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"name":"name"},{"isFacetable":True,"isWildcardSearchable":True,"booleanPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"enumPropertyOptions":{"possibleValues":[{"stringValue":"stringValue","integerValue":0},{"stringValue":"stringValue","integerValue":0}],"operatorOptions":{"operatorName":"operatorName"},"orderedRanking":"NO_ORDER"},"isSortable":True,"textPropertyOptions":{"operatorOptions":{"exactMatchWithOperator":True,"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"doublePropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"integerPropertyOptions":{"minimumValue":"minimumValue","operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"},"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"orderedRanking":"NO_ORDER","maximumValue":"maximumValue"},"objectPropertyOptions":{"subobjectProperties":[null,null]},"datePropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"displayOptions":{"displayLabel":"displayLabel"},"isReturnable":True,"isRepeatable":True,"isSuggestable":True,"htmlPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"timestampPropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"name":"name"}],"name":"name","options":{"suggestionFilteringOperators":["suggestionFilteringOperators","suggestionFilteringOperators"],"freshnessOptions":{"freshnessDuration":"freshnessDuration","freshnessProperty":"freshnessProperty"},"displayOptions":{"objectDisplayLabel":"objectDisplayLabel","metalines":[{"properties":[{"propertyName":"propertyName"},{"propertyName":"propertyName"}]},{"properties":[{"propertyName":"propertyName"},{"propertyName":"propertyName"}]}]}}},{"propertyDefinitions":[{"isFacetable":True,"isWildcardSearchable":True,"booleanPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"enumPropertyOptions":{"possibleValues":[{"stringValue":"stringValue","integerValue":0},{"stringValue":"stringValue","integerValue":0}],"operatorOptions":{"operatorName":"operatorName"},"orderedRanking":"NO_ORDER"},"isSortable":True,"textPropertyOptions":{"operatorOptions":{"exactMatchWithOperator":True,"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"doublePropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"integerPropertyOptions":{"minimumValue":"minimumValue","operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"},"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"orderedRanking":"NO_ORDER","maximumValue":"maximumValue"},"objectPropertyOptions":{"subobjectProperties":[null,null]},"datePropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"displayOptions":{"displayLabel":"displayLabel"},"isReturnable":True,"isRepeatable":True,"isSuggestable":True,"htmlPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"timestampPropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"name":"name"},{"isFacetable":True,"isWildcardSearchable":True,"booleanPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"enumPropertyOptions":{"possibleValues":[{"stringValue":"stringValue","integerValue":0},{"stringValue":"stringValue","integerValue":0}],"operatorOptions":{"operatorName":"operatorName"},"orderedRanking":"NO_ORDER"},"isSortable":True,"textPropertyOptions":{"operatorOptions":{"exactMatchWithOperator":True,"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"doublePropertyOptions":{"operatorOptions":{"operatorName":"operatorName"}},"integerPropertyOptions":{"minimumValue":"minimumValue","operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"},"integerFacetingOptions":{"integerBuckets":["integerBuckets","integerBuckets"]},"orderedRanking":"NO_ORDER","maximumValue":"maximumValue"},"objectPropertyOptions":{"subobjectProperties":[null,null]},"datePropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"displayOptions":{"displayLabel":"displayLabel"},"isReturnable":True,"isRepeatable":True,"isSuggestable":True,"htmlPropertyOptions":{"operatorOptions":{"operatorName":"operatorName"},"retrievalImportance":{"importance":"DEFAULT"}},"timestampPropertyOptions":{"operatorOptions":{"lessThanOperatorName":"lessThanOperatorName","greaterThanOperatorName":"greaterThanOperatorName","operatorName":"operatorName"}},"name":"name"}],"name":"name","options":{"suggestionFilteringOperators":["suggestionFilteringOperators","suggestionFilteringOperators"],"freshnessOptions":{"freshnessDuration":"freshnessDuration","freshnessProperty":"freshnessProperty"},"displayOptions":{"objectDisplayLabel":"objectDisplayLabel","metalines":[{"properties":[{"propertyName":"propertyName"},{"propertyName":"propertyName"}]},{"properties":[{"propertyName":"propertyName"},{"propertyName":"propertyName"}]}]}}}]},"validateOnly":True}
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
        method='PUT',
        path='/v1/indexing/{name}/schema'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

