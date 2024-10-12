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
from openapi_server.models.lookup_stream_object_request import LookupStreamObjectRequest
from openapi_server.models.operation import Operation
from openapi_server.models.private_connection import PrivateConnection
from openapi_server.models.route import Route
from openapi_server.models.run_stream_request import RunStreamRequest
from openapi_server.models.start_backfill_job_response import StartBackfillJobResponse
from openapi_server.models.stop_backfill_job_response import StopBackfillJobResponse
from openapi_server.models.stream import Stream
from openapi_server.models.stream_object import StreamObject


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_connection_profiles_create(client):
    """Test case for datastream_projects_locations_connection_profiles_create

    
    """
    body = {"gcsProfile":{"bucket":"bucket","rootPath":"rootPath"},"displayName":"displayName","bigqueryProfile":"{}","updateTime":"updateTime","staticServiceIpConnectivity":"{}","forwardSshConnectivity":{"privateKey":"privateKey","hostname":"hostname","password":"password","port":0,"username":"username"},"labels":{"key":"labels"},"postgresqlProfile":{"database":"database","hostname":"hostname","password":"password","port":5,"username":"username"},"mysqlProfile":{"hostname":"hostname","password":"password","sslConfig":{"clientCertificate":"clientCertificate","clientCertificateSet":True,"clientKey":"clientKey","clientKeySet":True,"caCertificateSet":True,"caCertificate":"caCertificate"},"port":6,"username":"username"},"createTime":"createTime","privateConnectivity":{"privateConnection":"privateConnection"},"name":"name","sqlServerProfile":{"database":"database","hostname":"hostname","password":"password","port":5,"username":"username"},"oracleProfile":{"oracleSslConfig":{"caCertificateSet":True,"caCertificate":"caCertificate"},"hostname":"hostname","password":"password","connectionAttributes":{"key":"connectionAttributes"},"databaseService":"databaseService","port":1,"username":"username"}}
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
                    ('force', True),
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/connectionProfiles'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_connection_profiles_discover(client):
    """Test case for datastream_projects_locations_connection_profiles_discover

    
    """
    body = {"postgresqlRdbms":{"postgresqlSchemas":[{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"oracleRdbms":{"oracleSchemas":[{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"connectionProfile":{"gcsProfile":{"bucket":"bucket","rootPath":"rootPath"},"displayName":"displayName","bigqueryProfile":"{}","updateTime":"updateTime","staticServiceIpConnectivity":"{}","forwardSshConnectivity":{"privateKey":"privateKey","hostname":"hostname","password":"password","port":0,"username":"username"},"labels":{"key":"labels"},"postgresqlProfile":{"database":"database","hostname":"hostname","password":"password","port":5,"username":"username"},"mysqlProfile":{"hostname":"hostname","password":"password","sslConfig":{"clientCertificate":"clientCertificate","clientCertificateSet":True,"clientKey":"clientKey","clientKeySet":True,"caCertificateSet":True,"caCertificate":"caCertificate"},"port":6,"username":"username"},"createTime":"createTime","privateConnectivity":{"privateConnection":"privateConnection"},"name":"name","sqlServerProfile":{"database":"database","hostname":"hostname","password":"password","port":5,"username":"username"},"oracleProfile":{"oracleSslConfig":{"caCertificateSet":True,"caCertificate":"caCertificate"},"hostname":"hostname","password":"password","connectionAttributes":{"key":"connectionAttributes"},"databaseService":"databaseService","port":1,"username":"username"}},"mysqlRdbms":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"}]},"fullHierarchy":True,"hierarchyDepth":0,"connectionProfileName":"connectionProfileName"}
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
        path='/v1/{parent}/connectionProfiles:discover'.format(parent='parent_example'),
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
        path='/v1/{parent}/connectionProfiles'.format(parent='parent_example'),
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
        path='/v1/{namefetch_static_ip}'.format(name='name_example'),
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
        path='/v1/{name}/locations'.format(name='name_example'),
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
        path='/v1/{namecance}'.format(name='name_example'),
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
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_private_connections_create(client):
    """Test case for datastream_projects_locations_private_connections_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","vpcPeeringConfig":{"subnet":"subnet","vpc":"vpc"},"name":"name","updateTime":"updateTime","state":"STATE_UNSPECIFIED","error":{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"},"labels":{"key":"labels"}}
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
        path='/v1/{parent}/privateConnections'.format(parent='parent_example'),
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
        path='/v1/{parent}/privateConnections'.format(parent='parent_example'),
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
        path='/v1/{parent}/routes'.format(parent='parent_example'),
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
        path='/v1/{parent}/routes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_create(client):
    """Test case for datastream_projects_locations_streams_create

    
    """
    body = {"lastRecoveryTime":"lastRecoveryTime","displayName":"displayName","updateTime":"updateTime","destinationConfig":{"gcsDestinationConfig":{"path":"path","fileRotationMb":7,"avroFileFormat":"{}","jsonFileFormat":{"schemaFileFormat":"SCHEMA_FILE_FORMAT_UNSPECIFIED","compression":"JSON_COMPRESSION_UNSPECIFIED"},"fileRotationInterval":"fileRotationInterval"},"destinationConnectionProfile":"destinationConnectionProfile","bigqueryDestinationConfig":{"dataFreshness":"dataFreshness","singleTargetDataset":{"datasetId":"datasetId"},"sourceHierarchyDatasets":{"datasetTemplate":{"datasetIdPrefix":"datasetIdPrefix","location":"location","kmsKeyName":"kmsKeyName"}}}},"customerManagedEncryptionKey":"customerManagedEncryptionKey","labels":{"key":"labels"},"backfillNone":"{}","sourceConfig":{"sourceConnectionProfile":"sourceConnectionProfile","mysqlSourceConfig":{"maxConcurrentBackfillTasks":1,"maxConcurrentCdcTasks":4,"excludeObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"}]},"includeObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"}]}},"postgresqlSourceConfig":{"maxConcurrentBackfillTasks":9,"excludeObjects":{"postgresqlSchemas":[{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"publication":"publication","replicationSlot":"replicationSlot","includeObjects":{"postgresqlSchemas":[{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]}},"oracleSourceConfig":{"maxConcurrentBackfillTasks":5,"maxConcurrentCdcTasks":9,"excludeObjects":{"oracleSchemas":[{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"streamLargeObjects":"{}","dropLargeObjects":"{}","includeObjects":{"oracleSchemas":[{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]}},"sqlServerSourceConfig":{"maxConcurrentBackfillTasks":6,"maxConcurrentCdcTasks":8,"excludeObjects":{"schemas":[{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]},{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]}]},"includeObjects":{"schemas":[{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]},{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]}]}}},"createTime":"createTime","backfillAll":{"sqlServerExcludedObjects":{"schemas":[{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]},{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]}]},"mysqlExcludedObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"}]},"postgresqlExcludedObjects":{"postgresqlSchemas":[{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"oracleExcludedObjects":{"oracleSchemas":[{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]}},"name":"name","state":"STATE_UNSPECIFIED","errors":[{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"},{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"}]}
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
        path='/v1/{parent}/streams'.format(parent='parent_example'),
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
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
        path='/v1/{parent}/streams'.format(parent='parent_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{parent}/objects'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_objects_lookup(client):
    """Test case for datastream_projects_locations_streams_objects_lookup

    
    """
    body = {"sourceObjectIdentifier":{"mysqlIdentifier":{"database":"database","table":"table"},"oracleIdentifier":{"schema":"schema","table":"table"},"postgresqlIdentifier":{"schema":"schema","table":"table"},"sqlServerIdentifier":{"schema":"schema","table":"table"}}}
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
        path='/v1/{parent}/objects:lookup'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_objects_start_backfill_job(client):
    """Test case for datastream_projects_locations_streams_objects_start_backfill_job

    
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
        path='/v1/{objectstart_backfill_jo}'.format(object='object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_objects_stop_backfill_job(client):
    """Test case for datastream_projects_locations_streams_objects_stop_backfill_job

    
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
        path='/v1/{objectstop_backfill_jo}'.format(object='object_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_patch(client):
    """Test case for datastream_projects_locations_streams_patch

    
    """
    body = {"lastRecoveryTime":"lastRecoveryTime","displayName":"displayName","updateTime":"updateTime","destinationConfig":{"gcsDestinationConfig":{"path":"path","fileRotationMb":7,"avroFileFormat":"{}","jsonFileFormat":{"schemaFileFormat":"SCHEMA_FILE_FORMAT_UNSPECIFIED","compression":"JSON_COMPRESSION_UNSPECIFIED"},"fileRotationInterval":"fileRotationInterval"},"destinationConnectionProfile":"destinationConnectionProfile","bigqueryDestinationConfig":{"dataFreshness":"dataFreshness","singleTargetDataset":{"datasetId":"datasetId"},"sourceHierarchyDatasets":{"datasetTemplate":{"datasetIdPrefix":"datasetIdPrefix","location":"location","kmsKeyName":"kmsKeyName"}}}},"customerManagedEncryptionKey":"customerManagedEncryptionKey","labels":{"key":"labels"},"backfillNone":"{}","sourceConfig":{"sourceConnectionProfile":"sourceConnectionProfile","mysqlSourceConfig":{"maxConcurrentBackfillTasks":1,"maxConcurrentCdcTasks":4,"excludeObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"}]},"includeObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"}]}},"postgresqlSourceConfig":{"maxConcurrentBackfillTasks":9,"excludeObjects":{"postgresqlSchemas":[{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"publication":"publication","replicationSlot":"replicationSlot","includeObjects":{"postgresqlSchemas":[{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]}},"oracleSourceConfig":{"maxConcurrentBackfillTasks":5,"maxConcurrentCdcTasks":9,"excludeObjects":{"oracleSchemas":[{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"streamLargeObjects":"{}","dropLargeObjects":"{}","includeObjects":{"oracleSchemas":[{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]}},"sqlServerSourceConfig":{"maxConcurrentBackfillTasks":6,"maxConcurrentCdcTasks":8,"excludeObjects":{"schemas":[{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]},{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]}]},"includeObjects":{"schemas":[{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]},{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]}]}}},"createTime":"createTime","backfillAll":{"sqlServerExcludedObjects":{"schemas":[{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]},{"schema":"schema","tables":[{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"},{"columns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":1,"scale":6,"ordinalPosition":1,"primaryKey":True}],"table":"table"}]}]},"mysqlExcludedObjects":{"mysqlDatabases":[{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"},{"mysqlTables":[{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"},{"mysqlColumns":[{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":1,"column":"column","length":0,"scale":5,"collation":"collation","ordinalPosition":6,"primaryKey":True}],"table":"table"}],"database":"database"}]},"postgresqlExcludedObjects":{"postgresqlSchemas":[{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","postgresqlTables":[{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"},{"postgresqlColumns":[{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":4,"column":"column","length":3,"scale":7,"ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]},"oracleExcludedObjects":{"oracleSchemas":[{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]},{"schema":"schema","oracleTables":[{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"},{"oracleColumns":[{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True},{"nullable":True,"dataType":"dataType","precision":7,"column":"column","length":5,"scale":9,"encoding":"encoding","ordinalPosition":2,"primaryKey":True}],"table":"table"}]}]}},"name":"name","state":"STATE_UNSPECIFIED","errors":[{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"},{"errorTime":"errorTime","reason":"reason","errorUuid":"errorUuid","details":{"key":"details"},"message":"message"}]}
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datastream_projects_locations_streams_run(client):
    """Test case for datastream_projects_locations_streams_run

    
    """
    body = {"cdcStrategy":{"nextAvailableStartPosition":"{}","specificStartPosition":{"mysqlLogPosition":{"logPosition":0,"logFile":"logFile"},"oracleScnPosition":{"scn":"scn"}},"mostRecentStartPosition":"{}"}}
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
        path='/v1/{nameru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

