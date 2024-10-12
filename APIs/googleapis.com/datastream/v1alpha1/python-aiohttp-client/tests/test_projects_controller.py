# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_profile import ConnectionProfile
from openapi_server.models.discover_connection_profile_request import DiscoverConnectionProfileRequest
from openapi_server.models.discover_connection_profile_response import DiscoverConnectionProfileResponse
from openapi_server.models.fetch_static_ips_response import FetchStaticIpsResponse
from openapi_server.models.list_connection_profiles_response import ListConnectionProfilesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_private_connections_response import ListPrivateConnectionsResponse
from openapi_server.models.list_routes_response import ListRoutesResponse
from openapi_server.models.list_stream_objects_response import ListStreamObjectsResponse
from openapi_server.models.list_streams_response import ListStreamsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.private_connection import PrivateConnection
from openapi_server.models.route import Route
from openapi_server.models.start_backfill_job_response import StartBackfillJobResponse
from openapi_server.models.stop_backfill_job_response import StopBackfillJobResponse
from openapi_server.models.stream import Stream
from openapi_server.models.stream_object import StreamObject


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_connection_profiles_create(client):
    """Test case for datastream_projects_locations_connection_profiles_create

    
    """
    body = {"gcsProfile":{"bucketName":"bucketName","rootPath":"rootPath"},"mysqlProfile":{"hostname":"hostname","password":"password","sslConfig":{"clientCertificate":"clientCertificate","clientCertificateSet":True,"clientKey":"clientKey","clientKeySet":True,"caCertificateSet":True,"caCertificate":"caCertificate"},"port":6,"username":"username"},"noConnectivity":"{}","createTime":"createTime","displayName":"displayName","privateConnectivity":{"privateConnectionName":"privateConnectionName"},"name":"name","updateTime":"updateTime","staticServiceIpConnectivity":"{}","oracleProfile":{"hostname":"hostname","password":"password","connectionAttributes":{"key":"connectionAttributes"},"databaseService":"databaseService","port":1,"username":"username"},"forwardSshConnectivity":{"privateKey":"privateKey","hostname":"hostname","password":"password","port":0,"username":"username"},"labels":{"key":"labels"}}
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
                    ('connectionProfileId', 'connection_profile_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/connectionProfiles'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_connection_profiles_discover(client):
    """Test case for datastream_projects_locations_connection_profiles_discover

    
    """
    body = {"recursionDepth":0,"oracleRdbms":{"oracleSchemas":[{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"},{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"}]},"connectionProfile":{"gcsProfile":{"bucketName":"bucketName","rootPath":"rootPath"},"mysqlProfile":{"hostname":"hostname","password":"password","sslConfig":{"clientCertificate":"clientCertificate","clientCertificateSet":True,"clientKey":"clientKey","clientKeySet":True,"caCertificateSet":True,"caCertificate":"caCertificate"},"port":6,"username":"username"},"noConnectivity":"{}","createTime":"createTime","displayName":"displayName","privateConnectivity":{"privateConnectionName":"privateConnectionName"},"name":"name","updateTime":"updateTime","staticServiceIpConnectivity":"{}","oracleProfile":{"hostname":"hostname","password":"password","connectionAttributes":{"key":"connectionAttributes"},"databaseService":"databaseService","port":1,"username":"username"},"forwardSshConnectivity":{"privateKey":"privateKey","hostname":"hostname","password":"password","port":0,"username":"username"},"labels":{"key":"labels"}},"mysqlRdbms":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"}]},"connectionProfileName":"connectionProfileName","recursive":True}
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
        path='/v1alpha1/{parent}/connectionProfiles:discover'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_connection_profiles_list(client):
    """Test case for datastream_projects_locations_connection_profiles_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/connectionProfiles'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_fetch_static_ips(client):
    """Test case for datastream_projects_locations_fetch_static_ips

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{namefetch_static_ip}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_list(client):
    """Test case for datastream_projects_locations_list

    
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
        path='/v1alpha1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_operations_cancel(client):
    """Test case for datastream_projects_locations_operations_cancel

    
    """
    body = None
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
        path='/v1alpha1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_operations_list(client):
    """Test case for datastream_projects_locations_operations_list

    
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
        path='/v1alpha1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_private_connections_create(client):
    """Test case for datastream_projects_locations_private_connections_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","vpcPeeringConfig":{"subnet":"subnet","vpcName":"vpcName"},"name":"name","updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"},"labels":{"key":"labels"}}
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
                    ('privateConnectionId', 'private_connection_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/privateConnections'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_private_connections_list(client):
    """Test case for datastream_projects_locations_private_connections_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/privateConnections'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_private_connections_routes_create(client):
    """Test case for datastream_projects_locations_private_connections_routes_create

    
    """
    body = {"destinationPort":0,"destinationAddress":"destinationAddress","createTime":"createTime","displayName":"displayName","name":"name","updateTime":"updateTime","labels":{"key":"labels"}}
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
                    ('requestId', 'request_id_example'),
                    ('routeId', 'route_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/routes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_private_connections_routes_list(client):
    """Test case for datastream_projects_locations_private_connections_routes_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/routes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_create(client):
    """Test case for datastream_projects_locations_streams_create

    
    """
    body = {"backfillNone":"{}","sourceConfig":{"mysqlSourceConfig":{"allowlist":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"}]},"rejectlist":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"}]}},"sourceConnectionProfileName":"sourceConnectionProfileName","oracleSourceConfig":{"allowlist":{"oracleSchemas":[{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"},{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"}]},"rejectlist":{"oracleSchemas":[{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"},{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"}]},"dropLargeObjects":"{}"}},"createTime":"createTime","backfillAll":{"mysqlExcludedObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"}]},"oracleExcludedObjects":{"oracleSchemas":[{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"},{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"}]}},"displayName":"displayName","name":"name","updateTime":"updateTime","state":"STATE_UNSPECIFIED","destinationConfig":{"destinationConnectionProfileName":"destinationConnectionProfileName","gcsDestinationConfig":{"path":"path","fileRotationMb":7,"avroFileFormat":"{}","jsonFileFormat":{"schemaFileFormat":"SCHEMA_FILE_FORMAT_UNSPECIFIED","compression":"JSON_COMPRESSION_UNSPECIFIED"},"fileRotationInterval":"fileRotationInterval","gcsFileFormat":"GCS_FILE_FORMAT_UNSPECIFIED"}},"errors":[{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"},{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"}],"customerManagedEncryptionKey":"customerManagedEncryptionKey","labels":{"key":"labels"}}
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
                    ('force', True),
                    ('requestId', 'request_id_example'),
                    ('streamId', 'stream_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/streams'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_delete(client):
    """Test case for datastream_projects_locations_streams_delete

    
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
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_fetch_errors(client):
    """Test case for datastream_projects_locations_streams_fetch_errors

    
    """
    body = None
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
        path='/v1alpha1/{streamfetch_error}'.format(stream='stream_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_list(client):
    """Test case for datastream_projects_locations_streams_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/streams'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_objects_get(client):
    """Test case for datastream_projects_locations_streams_objects_get

    
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
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_objects_list(client):
    """Test case for datastream_projects_locations_streams_objects_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/objects'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_objects_start_backfill_job(client):
    """Test case for datastream_projects_locations_streams_objects_start_backfill_job

    
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
        path='/v1alpha1/{objectstart_backfill_jo}'.format(object='object_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_objects_stop_backfill_job(client):
    """Test case for datastream_projects_locations_streams_objects_stop_backfill_job

    
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
        path='/v1alpha1/{objectstop_backfill_jo}'.format(object='object_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_patch(client):
    """Test case for datastream_projects_locations_streams_patch

    
    """
    body = {"backfillNone":"{}","sourceConfig":{"mysqlSourceConfig":{"allowlist":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"}]},"rejectlist":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"}]}},"sourceConnectionProfileName":"sourceConnectionProfileName","oracleSourceConfig":{"allowlist":{"oracleSchemas":[{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"},{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"}]},"rejectlist":{"oracleSchemas":[{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"},{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"}]},"dropLargeObjects":"{}"}},"createTime":"createTime","backfillAll":{"mysqlExcludedObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","length":0,"collation":"collation","ordinalPosition":6,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"databaseName":"databaseName"}]},"oracleExcludedObjects":{"oracleSchemas":[{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"},{"oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True},{"nullable":True,"dataType":"dataType","precision":5,"length":1,"scale":2,"encoding":"encoding","ordinalPosition":5,"columnName":"columnName","primaryKey":True}],"tableName":"tableName"}],"schemaName":"schemaName"}]}},"displayName":"displayName","name":"name","updateTime":"updateTime","state":"STATE_UNSPECIFIED","destinationConfig":{"destinationConnectionProfileName":"destinationConnectionProfileName","gcsDestinationConfig":{"path":"path","fileRotationMb":7,"avroFileFormat":"{}","jsonFileFormat":{"schemaFileFormat":"SCHEMA_FILE_FORMAT_UNSPECIFIED","compression":"JSON_COMPRESSION_UNSPECIFIED"},"fileRotationInterval":"fileRotationInterval","gcsFileFormat":"GCS_FILE_FORMAT_UNSPECIFIED"}},"errors":[{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"},{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"}],"customerManagedEncryptionKey":"customerManagedEncryptionKey","labels":{"key":"labels"}}
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
                    ('force', True),
                    ('requestId', 'request_id_example'),
                    ('updateMask', 'update_mask_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

