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
from openapi_server.models.google_datastore_admin_v1_export_entities_request import GoogleDatastoreAdminV1ExportEntitiesRequest
from openapi_server.models.google_datastore_admin_v1_import_entities_request import GoogleDatastoreAdminV1ImportEntitiesRequest
from openapi_server.models.google_datastore_admin_v1_index import GoogleDatastoreAdminV1Index
from openapi_server.models.google_datastore_admin_v1_list_indexes_response import GoogleDatastoreAdminV1ListIndexesResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
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
    body = {"keys":[{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}}],"databaseId":"databaseId"}
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
        path='/v1/projects/{project_idallocate_id}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_begin_transaction(client):
    """Test case for datastore_projects_begin_transaction

    
    """
    body = {"transactionOptions":{"readWrite":{"previousTransaction":"previousTransaction"},"readOnly":{"readTime":"readTime"}},"databaseId":"databaseId"}
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
        path='/v1/projects/{project_idbegin_transactio}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_commit(client):
    """Test case for datastore_projects_commit

    
    """
    body = {"mode":"MODE_UNSPECIFIED","mutations":[{"baseVersion":"baseVersion","upsert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"insert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"update":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"updateTime":"updateTime","delete":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}}},{"baseVersion":"baseVersion","upsert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"insert":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"update":{"key":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"properties":{"key":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"updateTime":"updateTime","delete":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}}}],"singleUseTransaction":{"readWrite":{"previousTransaction":"previousTransaction"},"readOnly":{"readTime":"readTime"}},"databaseId":"databaseId","transaction":"transaction"}
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
        path='/v1/projects/{project_idcommi}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_export(client):
    """Test case for datastore_projects_export

    
    """
    body = {"entityFilter":{"namespaceIds":["namespaceIds","namespaceIds"],"kinds":["kinds","kinds"]},"outputUrlPrefix":"outputUrlPrefix","labels":{"key":"labels"}}
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
        path='/v1/projects/{project_idexpor}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_import(client):
    """Test case for datastore_projects_import

    
    """
    body = {"entityFilter":{"namespaceIds":["namespaceIds","namespaceIds"],"kinds":["kinds","kinds"]},"inputUrl":"inputUrl","labels":{"key":"labels"}}
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
        path='/v1/projects/{project_idimpor}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_indexes_create(client):
    """Test case for datastore_projects_indexes_create

    
    """
    body = {"kind":"kind","ancestor":"ANCESTOR_MODE_UNSPECIFIED","indexId":"indexId","state":"STATE_UNSPECIFIED","projectId":"projectId","properties":[{"name":"name","direction":"DIRECTION_UNSPECIFIED"},{"name":"name","direction":"DIRECTION_UNSPECIFIED"}]}
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
        path='/v1/projects/{project_id}/indexes'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_indexes_delete(client):
    """Test case for datastore_projects_indexes_delete

    
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
        method='DELETE',
        path='/v1/projects/{project_id}/indexes/{index_id}'.format(project_id='project_id_example', index_id='index_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_indexes_get(client):
    """Test case for datastore_projects_indexes_get

    
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
        path='/v1/projects/{project_id}/indexes/{index_id}'.format(project_id='project_id_example', index_id='index_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_indexes_list(client):
    """Test case for datastore_projects_indexes_list

    
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
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project_id}/indexes'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_lookup(client):
    """Test case for datastore_projects_lookup

    
    """
    body = {"keys":[{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}}],"readOptions":{"newTransaction":{"readWrite":{"previousTransaction":"previousTransaction"},"readOnly":{"readTime":"readTime"}},"readTime":"readTime","readConsistency":"READ_CONSISTENCY_UNSPECIFIED","transaction":"transaction"},"databaseId":"databaseId"}
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
        path='/v1/projects/{project_idlooku}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_operations_cancel(client):
    """Test case for datastore_projects_operations_cancel

    
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
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_operations_delete(client):
    """Test case for datastore_projects_operations_delete

    
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
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_operations_get(client):
    """Test case for datastore_projects_operations_get

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_operations_list(client):
    """Test case for datastore_projects_operations_list

    
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
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_reserve_ids(client):
    """Test case for datastore_projects_reserve_ids

    
    """
    body = {"keys":[{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}}],"databaseId":"databaseId"}
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
        path='/v1/projects/{project_idreserve_id}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_rollback(client):
    """Test case for datastore_projects_rollback

    
    """
    body = {"databaseId":"databaseId","transaction":"transaction"}
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
        path='/v1/projects/{project_idrollbac}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_run_aggregation_query(client):
    """Test case for datastore_projects_run_aggregation_query

    
    """
    body = {"aggregationQuery":{"nestedQuery":{"filter":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"propertyFilter":{"op":"OPERATOR_UNSPECIFIED","property":{"name":"name"},"value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"offset":6,"kind":[{"name":"name"},{"name":"name"}],"limit":0,"endCursor":"endCursor","projection":[{"property":{"name":"name"}},{"property":{"name":"name"}}],"startCursor":"startCursor","distinctOn":[{"name":"name"},{"name":"name"}],"order":[{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"},{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"}]},"aggregations":[{"avg":{"property":{"name":"name"}},"count":{"upTo":"upTo"},"alias":"alias","sum":{"property":{"name":"name"}}},{"avg":{"property":{"name":"name"}},"count":{"upTo":"upTo"},"alias":"alias","sum":{"property":{"name":"name"}}}]},"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"},"gqlQuery":{"namedBindings":{"key":{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"allowLiterals":True,"positionalBindings":[{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}},{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}],"queryString":"queryString"},"readOptions":{"newTransaction":{"readWrite":{"previousTransaction":"previousTransaction"},"readOnly":{"readTime":"readTime"}},"readTime":"readTime","readConsistency":"READ_CONSISTENCY_UNSPECIFIED","transaction":"transaction"},"databaseId":"databaseId"}
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
        path='/v1/projects/{project_idrun_aggregation_quer}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastore_projects_run_query(client):
    """Test case for datastore_projects_run_query

    
    """
    body = {"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"},"gqlQuery":{"namedBindings":{"key":{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"allowLiterals":True,"positionalBindings":[{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}},{"cursor":"cursor","value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}],"queryString":"queryString"},"query":{"filter":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"propertyFilter":{"op":"OPERATOR_UNSPECIFIED","property":{"name":"name"},"value":{"keyValue":{"path":[{"kind":"kind","name":"name","id":"id"},{"kind":"kind","name":"name","id":"id"}],"partitionId":{"namespaceId":"namespaceId","databaseId":"databaseId","projectId":"projectId"}},"timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"nullValue":"NULL_VALUE","stringValue":"stringValue","meaning":5,"booleanValue":True,"integerValue":"integerValue","excludeFromIndexes":True,"blobValue":"blobValue"}}},"offset":6,"kind":[{"name":"name"},{"name":"name"}],"limit":0,"endCursor":"endCursor","projection":[{"property":{"name":"name"}},{"property":{"name":"name"}}],"startCursor":"startCursor","distinctOn":[{"name":"name"},{"name":"name"}],"order":[{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"},{"property":{"name":"name"},"direction":"DIRECTION_UNSPECIFIED"}]},"readOptions":{"newTransaction":{"readWrite":{"previousTransaction":"previousTransaction"},"readOnly":{"readTime":"readTime"}},"readTime":"readTime","readConsistency":"READ_CONSISTENCY_UNSPECIFIED","transaction":"transaction"},"databaseId":"databaseId"}
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
        path='/v1/projects/{project_idrun_quer}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

