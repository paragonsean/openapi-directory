# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.allocate_ids_request import AllocateIdsRequest
from openapi_server.models.allocate_ids_response import AllocateIdsResponse
from openapi_server.models.begin_transaction_request import BeginTransactionRequest
from openapi_server.models.begin_transaction_response import BeginTransactionResponse
from openapi_server.models.commit_request import CommitRequest
from openapi_server.models.commit_response import CommitResponse
from openapi_server.models.lookup_request import LookupRequest
from openapi_server.models.lookup_response import LookupResponse
from openapi_server.models.reserve_ids_request import ReserveIdsRequest
from openapi_server.models.rollback_request import RollbackRequest
from openapi_server.models.run_aggregation_query_request import RunAggregationQueryRequest
from openapi_server.models.run_aggregation_query_response import RunAggregationQueryResponse
from openapi_server.models.run_query_request import RunQueryRequest
from openapi_server.models.run_query_response import RunQueryResponse


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_allocate_ids(client):
    """Test case for datastore_projects_allocate_ids

    
    """
    body = {"keys":[{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}}]}
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
        path='/v1beta3/projects/{project_idallocate_id}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_begin_transaction(client):
    """Test case for datastore_projects_begin_transaction

    
    """
    body = {"transactionOptions":{"readWrite":{"previousTransaction":"previousTransaction"},"readOnly":{"readTime":"readTime"}}}
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
        path='/v1beta3/projects/{project_idbegin_transactio}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_commit(client):
    """Test case for datastore_projects_commit

    
    """
    body = {"mode":"MODE_UNSPECIFIED","mutations":[{"baseVersion":"baseVersion","upsert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"insert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"update":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"updateTime":"updateTime","delete":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}}},{"baseVersion":"baseVersion","upsert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"insert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"update":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"updateTime":"updateTime","delete":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}}}],"transaction":"transaction"}
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
        path='/v1beta3/projects/{project_idcommi}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_lookup(client):
    """Test case for datastore_projects_lookup

    
    """
    body = {"keys":[{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}}],"readOptions":{"readTime":"readTime","readConsistency":"READ_CONSISTENCY_UNSPECIFIED","transaction":"transaction"}}
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
        path='/v1beta3/projects/{project_idlooku}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_reserve_ids(client):
    """Test case for datastore_projects_reserve_ids

    
    """
    body = {"keys":[{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}}],"databaseId":"databaseId"}
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
        path='/v1beta3/projects/{project_idreserve_id}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_rollback(client):
    """Test case for datastore_projects_rollback

    
    """
    body = {"transaction":"transaction"}
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
        path='/v1beta3/projects/{project_idrollbac}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_run_aggregation_query(client):
    """Test case for datastore_projects_run_aggregation_query

    
    """
    body = {"aggregationQuery":{"nestedQuery":{"filter":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"propertyFilter":{"op":"OPERATOR_UNSPECIFIED","property":{"name":"name"},"value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"offset":6,"kind":[{"name":"name"},{"name":"name"}],"limit":0,"endCursor":"endCursor","projection":[{"property":{"name":"name"}},{"property":{"name":"name"}}],"startCursor":"startCursor","distinctOn":[{"name":"name"},{"name":"name"}],"order":[{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"},{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"}]},"aggregations":[{"avg":{"property":{"name":"name"}},"count":{"upTo":"upTo"},"alias":"alias","sum":{"property":{"name":"name"}}},{"avg":{"property":{"name":"name"}},"count":{"upTo":"upTo"},"alias":"alias","sum":{"property":{"name":"name"}}}]},"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"},"gqlQuery":{"namedBindings":{"key":{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"allowLiterals":True,"positionalBindings":[{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}},{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}],"queryString":"queryString"},"readOptions":{"readTime":"readTime","readConsistency":"READ_CONSISTENCY_UNSPECIFIED","transaction":"transaction"}}
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
        path='/v1beta3/projects/{project_idrun_aggregation_quer}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_run_query(client):
    """Test case for datastore_projects_run_query

    
    """
    body = {"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"},"gqlQuery":{"namedBindings":{"key":{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"allowLiterals":True,"positionalBindings":[{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}},{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}],"queryString":"queryString"},"query":{"filter":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"propertyFilter":{"op":"OPERATOR_UNSPECIFIED","property":{"name":"name"},"value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"offset":6,"kind":[{"name":"name"},{"name":"name"}],"limit":0,"endCursor":"endCursor","projection":[{"property":{"name":"name"}},{"property":{"name":"name"}}],"startCursor":"startCursor","distinctOn":[{"name":"name"},{"name":"name"}],"order":[{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"},{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"}]},"readOptions":{"readTime":"readTime","readConsistency":"READ_CONSISTENCY_UNSPECIFIED","transaction":"transaction"}}
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
        path='/v1beta3/projects/{project_idrun_quer}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

