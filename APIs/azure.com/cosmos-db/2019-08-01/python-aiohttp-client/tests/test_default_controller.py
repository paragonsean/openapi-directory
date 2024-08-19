# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cassandra_keyspace_create_update_parameters import CassandraKeyspaceCreateUpdateParameters
from openapi_server.models.cassandra_keyspace_get_results import CassandraKeyspaceGetResults
from openapi_server.models.cassandra_keyspace_list_result import CassandraKeyspaceListResult
from openapi_server.models.cassandra_table_create_update_parameters import CassandraTableCreateUpdateParameters
from openapi_server.models.cassandra_table_get_results import CassandraTableGetResults
from openapi_server.models.cassandra_table_list_result import CassandraTableListResult
from openapi_server.models.database_account_create_update_parameters import DatabaseAccountCreateUpdateParameters
from openapi_server.models.database_account_get_results import DatabaseAccountGetResults
from openapi_server.models.database_account_list_connection_strings_result import DatabaseAccountListConnectionStringsResult
from openapi_server.models.database_account_list_keys_result import DatabaseAccountListKeysResult
from openapi_server.models.database_account_list_read_only_keys_result import DatabaseAccountListReadOnlyKeysResult
from openapi_server.models.database_account_regenerate_key_parameters import DatabaseAccountRegenerateKeyParameters
from openapi_server.models.database_account_update_parameters import DatabaseAccountUpdateParameters
from openapi_server.models.database_accounts_list_result import DatabaseAccountsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.failover_policies import FailoverPolicies
from openapi_server.models.gremlin_database_create_update_parameters import GremlinDatabaseCreateUpdateParameters
from openapi_server.models.gremlin_database_get_results import GremlinDatabaseGetResults
from openapi_server.models.gremlin_database_list_result import GremlinDatabaseListResult
from openapi_server.models.gremlin_graph_create_update_parameters import GremlinGraphCreateUpdateParameters
from openapi_server.models.gremlin_graph_get_results import GremlinGraphGetResults
from openapi_server.models.gremlin_graph_list_result import GremlinGraphListResult
from openapi_server.models.metric_definitions_list_result import MetricDefinitionsListResult
from openapi_server.models.metric_list_result import MetricListResult
from openapi_server.models.mongo_db_collection_create_update_parameters import MongoDBCollectionCreateUpdateParameters
from openapi_server.models.mongo_db_collection_get_results import MongoDBCollectionGetResults
from openapi_server.models.mongo_db_collection_list_result import MongoDBCollectionListResult
from openapi_server.models.mongo_db_database_create_update_parameters import MongoDBDatabaseCreateUpdateParameters
from openapi_server.models.mongo_db_database_get_results import MongoDBDatabaseGetResults
from openapi_server.models.mongo_db_database_list_result import MongoDBDatabaseListResult
from openapi_server.models.partition_metric_list_result import PartitionMetricListResult
from openapi_server.models.partition_usages_result import PartitionUsagesResult
from openapi_server.models.percentile_metric_list_result import PercentileMetricListResult
from openapi_server.models.region_for_online_offline import RegionForOnlineOffline
from openapi_server.models.sql_container_create_update_parameters import SqlContainerCreateUpdateParameters
from openapi_server.models.sql_container_get_results import SqlContainerGetResults
from openapi_server.models.sql_container_list_result import SqlContainerListResult
from openapi_server.models.sql_database_create_update_parameters import SqlDatabaseCreateUpdateParameters
from openapi_server.models.sql_database_get_results import SqlDatabaseGetResults
from openapi_server.models.sql_database_list_result import SqlDatabaseListResult
from openapi_server.models.sql_stored_procedure_create_update_parameters import SqlStoredProcedureCreateUpdateParameters
from openapi_server.models.sql_stored_procedure_get_results import SqlStoredProcedureGetResults
from openapi_server.models.sql_stored_procedure_list_result import SqlStoredProcedureListResult
from openapi_server.models.sql_trigger_create_update_parameters import SqlTriggerCreateUpdateParameters
from openapi_server.models.sql_trigger_get_results import SqlTriggerGetResults
from openapi_server.models.sql_trigger_list_result import SqlTriggerListResult
from openapi_server.models.sql_user_defined_function_create_update_parameters import SqlUserDefinedFunctionCreateUpdateParameters
from openapi_server.models.sql_user_defined_function_get_results import SqlUserDefinedFunctionGetResults
from openapi_server.models.sql_user_defined_function_list_result import SqlUserDefinedFunctionListResult
from openapi_server.models.table_create_update_parameters import TableCreateUpdateParameters
from openapi_server.models.table_get_results import TableGetResults
from openapi_server.models.table_list_result import TableListResult
from openapi_server.models.throughput_settings_get_results import ThroughputSettingsGetResults
from openapi_server.models.throughput_settings_update_parameters import ThroughputSettingsUpdateParameters
from openapi_server.models.usages_result import UsagesResult


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_create_update_cassandra_keyspace(client):
    """Test case for cassandra_resources_create_update_cassandra_keyspace

    
    """
    create_update_cassandra_keyspace_parameters = {"properties":{"resource":{"id":"id"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example'),
        headers=headers,
        json=create_update_cassandra_keyspace_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_create_update_cassandra_table(client):
    """Test case for cassandra_resources_create_update_cassandra_table

    
    """
    create_update_cassandra_table_parameters = {"properties":{"resource":{"schema":{"columns":[{"name":"name","type":"type"},{"name":"name","type":"type"}],"partitionKeys":[{"name":"name"},{"name":"name"}],"clusterKeys":[{"name":"name","orderBy":"orderBy"},{"name":"name","orderBy":"orderBy"}]},"defaultTtl":0,"id":"id"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/tables/{table_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example', table_name='table_name_example'),
        headers=headers,
        json=create_update_cassandra_table_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_delete_cassandra_keyspace(client):
    """Test case for cassandra_resources_delete_cassandra_keyspace

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_delete_cassandra_table(client):
    """Test case for cassandra_resources_delete_cassandra_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/tables/{table_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_get_cassandra_keyspace(client):
    """Test case for cassandra_resources_get_cassandra_keyspace

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_get_cassandra_keyspace_throughput(client):
    """Test case for cassandra_resources_get_cassandra_keyspace_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_get_cassandra_table(client):
    """Test case for cassandra_resources_get_cassandra_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/tables/{table_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_get_cassandra_table_throughput(client):
    """Test case for cassandra_resources_get_cassandra_table_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/tables/{table_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_list_cassandra_keyspaces(client):
    """Test case for cassandra_resources_list_cassandra_keyspaces

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_list_cassandra_tables(client):
    """Test case for cassandra_resources_list_cassandra_tables

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/tables'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_update_cassandra_keyspace_throughput(client):
    """Test case for cassandra_resources_update_cassandra_keyspace_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cassandra_resources_update_cassandra_table_throughput(client):
    """Test case for cassandra_resources_update_cassandra_table_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/cassandraKeyspaces/{keyspace_name}/tables/{table_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', keyspace_name='keyspace_name_example', table_name='table_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_list_metric_definitions(client):
    """Test case for collection_list_metric_definitions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/collections/{collection_rid}/metricDefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example', collection_rid='collection_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_list_metrics(client):
    """Test case for collection_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/collections/{collection_rid}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example', collection_rid='collection_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_list_usages(client):
    """Test case for collection_list_usages

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/collections/{collection_rid}/usages'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example', collection_rid='collection_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_partition_list_metrics(client):
    """Test case for collection_partition_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/collections/{collection_rid}/partitions/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example', collection_rid='collection_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_partition_list_usages(client):
    """Test case for collection_partition_list_usages

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/collections/{collection_rid}/partitions/usages'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example', collection_rid='collection_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_partition_region_list_metrics(client):
    """Test case for collection_partition_region_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/region/{region}/databases/{database_rid}/collections/{collection_rid}/partitions/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', region='region_example', database_rid='database_rid_example', collection_rid='collection_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_region_list_metrics(client):
    """Test case for collection_region_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/region/{region}/databases/{database_rid}/collections/{collection_rid}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', region='region_example', database_rid='database_rid_example', collection_rid='collection_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_account_region_list_metrics(client):
    """Test case for database_account_region_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/region/{region}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', region='region_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_check_name_exists(client):
    """Test case for database_accounts_check_name_exists

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/providers/Microsoft.DocumentDB/databaseAccountNames/{account_name}'.format(account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_create_or_update(client):
    """Test case for database_accounts_create_or_update

    
    """
    create_update_parameters = {"kind":"GlobalDocumentDB","properties":{"ipRangeFilter":"ipRangeFilter","enableCassandraConnector":True,"enableMultipleWriteLocations":True,"capabilities":[{"name":"name"},{"name":"name"}],"connectorOffer":"Small","consistencyPolicy":{"maxStalenessPrefix":1294386359,"defaultConsistencyLevel":"Eventual","maxIntervalInSeconds":6923},"databaseAccountOfferType":"Standard","locations":[{"failoverPriority":0,"locationName":"locationName","documentEndpoint":"documentEndpoint","id":"id","provisioningState":"provisioningState","isZoneRedundant":True},{"failoverPriority":0,"locationName":"locationName","documentEndpoint":"documentEndpoint","id":"id","provisioningState":"provisioningState","isZoneRedundant":True}],"virtualNetworkRules":[{"id":"id","ignoreMissingVNetServiceEndpoint":True},{"id":"id","ignoreMissingVNetServiceEndpoint":True}],"disableKeyBasedMetadataWriteAccess":True,"isVirtualNetworkFilterEnabled":True,"enableAutomaticFailover":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=create_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_delete(client):
    """Test case for database_accounts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_failover_priority_change(client):
    """Test case for database_accounts_failover_priority_change

    
    """
    failover_parameters = {"failoverPolicies":[{"failoverPriority":0,"locationName":"locationName","id":"id"},{"failoverPriority":0,"locationName":"locationName","id":"id"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/failoverPriorityChange'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=failover_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_get(client):
    """Test case for database_accounts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_get_read_only_keys(client):
    """Test case for database_accounts_get_read_only_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/readonlykeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list(client):
    """Test case for database_accounts_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DocumentDB/databaseAccounts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list_by_resource_group(client):
    """Test case for database_accounts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list_connection_strings(client):
    """Test case for database_accounts_list_connection_strings

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/listConnectionStrings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list_keys(client):
    """Test case for database_accounts_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list_metric_definitions(client):
    """Test case for database_accounts_list_metric_definitions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/metricDefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list_metrics(client):
    """Test case for database_accounts_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list_read_only_keys(client):
    """Test case for database_accounts_list_read_only_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/readonlykeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_list_usages(client):
    """Test case for database_accounts_list_usages

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/usages'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_offline_region(client):
    """Test case for database_accounts_offline_region

    
    """
    region_parameter_for_offline = {"region":"region"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/offlineRegion'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=region_parameter_for_offline,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_online_region(client):
    """Test case for database_accounts_online_region

    
    """
    region_parameter_for_online = {"region":"region"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/onlineRegion'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=region_parameter_for_online,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_regenerate_key(client):
    """Test case for database_accounts_regenerate_key

    
    """
    key_to_regenerate = {"keyKind":"primary"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/regenerateKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=key_to_regenerate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_accounts_update(client):
    """Test case for database_accounts_update

    
    """
    update_parameters = {"location":"location","properties":{"ipRangeFilter":"ipRangeFilter","enableCassandraConnector":True,"enableMultipleWriteLocations":True,"capabilities":[{"name":"name"},{"name":"name"}],"connectorOffer":"Small","consistencyPolicy":{"maxStalenessPrefix":1294386359,"defaultConsistencyLevel":"Eventual","maxIntervalInSeconds":6923},"locations":[{"failoverPriority":0,"locationName":"locationName","documentEndpoint":"documentEndpoint","id":"id","provisioningState":"provisioningState","isZoneRedundant":True},{"failoverPriority":0,"locationName":"locationName","documentEndpoint":"documentEndpoint","id":"id","provisioningState":"provisioningState","isZoneRedundant":True}],"virtualNetworkRules":[{"id":"id","ignoreMissingVNetServiceEndpoint":True},{"id":"id","ignoreMissingVNetServiceEndpoint":True}],"disableKeyBasedMetadataWriteAccess":True,"isVirtualNetworkFilterEnabled":True,"enableAutomaticFailover":True},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_list_metric_definitions(client):
    """Test case for database_list_metric_definitions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/metricDefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_list_metrics(client):
    """Test case for database_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_list_usages(client):
    """Test case for database_list_usages

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/usages'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_create_update_gremlin_database(client):
    """Test case for gremlin_resources_create_update_gremlin_database

    
    """
    create_update_gremlin_database_parameters = {"properties":{"resource":{"id":"id"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        json=create_update_gremlin_database_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_create_update_gremlin_graph(client):
    """Test case for gremlin_resources_create_update_gremlin_graph

    
    """
    create_update_gremlin_graph_parameters = {"properties":{"resource":{"uniqueKeyPolicy":{"uniqueKeys":[{"paths":[null,null]},{"paths":[null,null]}]},"partitionKey":{"kind":"Hash","paths":[null,null],"version":1},"indexingPolicy":{"indexingMode":"Consistent","spatialIndexes":[{"path":"path","types":["Point","Point"]},{"path":"path","types":["Point","Point"]}],"automatic":True,"includedPaths":[{"path":"path","indexes":[{"kind":"Hash","dataType":"String","precision":6},{"kind":"Hash","dataType":"String","precision":6}]},{"path":"path","indexes":[{"kind":"Hash","dataType":"String","precision":6},{"kind":"Hash","dataType":"String","precision":6}]}],"excludedPaths":[{"path":"path"},{"path":"path"}],"compositeIndexes":[[{"path":"path","order":"Ascending"},{"path":"path","order":"Ascending"}],[{"path":"path","order":"Ascending"},{"path":"path","order":"Ascending"}]]},"defaultTtl":0,"id":"id","conflictResolutionPolicy":{"mode":"LastWriterWins","conflictResolutionProcedure":"conflictResolutionProcedure","conflictResolutionPath":"conflictResolutionPath"}},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/graphs/{graph_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', graph_name='graph_name_example'),
        headers=headers,
        json=create_update_gremlin_graph_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_delete_gremlin_database(client):
    """Test case for gremlin_resources_delete_gremlin_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_delete_gremlin_graph(client):
    """Test case for gremlin_resources_delete_gremlin_graph

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/graphs/{graph_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', graph_name='graph_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_get_gremlin_database(client):
    """Test case for gremlin_resources_get_gremlin_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_get_gremlin_database_throughput(client):
    """Test case for gremlin_resources_get_gremlin_database_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_get_gremlin_graph(client):
    """Test case for gremlin_resources_get_gremlin_graph

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/graphs/{graph_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', graph_name='graph_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_get_gremlin_graph_throughput(client):
    """Test case for gremlin_resources_get_gremlin_graph_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/graphs/{graph_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', graph_name='graph_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_list_gremlin_databases(client):
    """Test case for gremlin_resources_list_gremlin_databases

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_list_gremlin_graphs(client):
    """Test case for gremlin_resources_list_gremlin_graphs

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/graphs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_update_gremlin_database_throughput(client):
    """Test case for gremlin_resources_update_gremlin_database_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gremlin_resources_update_gremlin_graph_throughput(client):
    """Test case for gremlin_resources_update_gremlin_graph_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/gremlinDatabases/{database_name}/graphs/{graph_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', graph_name='graph_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_create_update_mongo_db_collection(client):
    """Test case for mongo_db_resources_create_update_mongo_db_collection

    
    """
    create_update_mongo_db_collection_parameters = {"properties":{"resource":{"indexes":[{"options":{"expireAfterSeconds":0,"unique":True},"key":{"keys":[null,null]}},{"options":{"expireAfterSeconds":0,"unique":True},"key":{"keys":[null,null]}}],"id":"id","shardKey":{"key":"shardKey"}},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/collections/{collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', collection_name='collection_name_example'),
        headers=headers,
        json=create_update_mongo_db_collection_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_create_update_mongo_db_database(client):
    """Test case for mongo_db_resources_create_update_mongo_db_database

    
    """
    create_update_mongo_db_database_parameters = {"properties":{"resource":{"id":"id"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        json=create_update_mongo_db_database_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_delete_mongo_db_collection(client):
    """Test case for mongo_db_resources_delete_mongo_db_collection

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/collections/{collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', collection_name='collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_delete_mongo_db_database(client):
    """Test case for mongo_db_resources_delete_mongo_db_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_get_mongo_db_collection(client):
    """Test case for mongo_db_resources_get_mongo_db_collection

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/collections/{collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', collection_name='collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_get_mongo_db_collection_throughput(client):
    """Test case for mongo_db_resources_get_mongo_db_collection_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/collections/{collection_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', collection_name='collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_get_mongo_db_database(client):
    """Test case for mongo_db_resources_get_mongo_db_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_get_mongo_db_database_throughput(client):
    """Test case for mongo_db_resources_get_mongo_db_database_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_list_mongo_db_collections(client):
    """Test case for mongo_db_resources_list_mongo_db_collections

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/collections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_list_mongo_db_databases(client):
    """Test case for mongo_db_resources_list_mongo_db_databases

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_update_mongo_db_collection_throughput(client):
    """Test case for mongo_db_resources_update_mongo_db_collection_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/collections/{collection_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', collection_name='collection_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mongo_db_resources_update_mongo_db_database_throughput(client):
    """Test case for mongo_db_resources_update_mongo_db_database_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/mongodbDatabases/{database_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partition_key_range_id_list_metrics(client):
    """Test case for partition_key_range_id_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/databases/{database_rid}/collections/{collection_rid}/partitionKeyRangeId/{partition_key_range_id}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_rid='database_rid_example', collection_rid='collection_rid_example', partition_key_range_id='partition_key_range_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partition_key_range_id_region_list_metrics(client):
    """Test case for partition_key_range_id_region_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/region/{region}/databases/{database_rid}/collections/{collection_rid}/partitionKeyRangeId/{partition_key_range_id}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', region='region_example', database_rid='database_rid_example', collection_rid='collection_rid_example', partition_key_range_id='partition_key_range_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_percentile_list_metrics(client):
    """Test case for percentile_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/percentile/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_percentile_source_target_list_metrics(client):
    """Test case for percentile_source_target_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sourceRegion/{source_region}/targetRegion/{target_region}/percentile/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', source_region='source_region_example', target_region='target_region_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_percentile_target_list_metrics(client):
    """Test case for percentile_target_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/targetRegion/{target_region}/percentile/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', target_region='target_region_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_create_update_sql_container(client):
    """Test case for sql_resources_create_update_sql_container

    
    """
    create_update_sql_container_parameters = {"properties":{"resource":{"uniqueKeyPolicy":{"uniqueKeys":[{"paths":[null,null]},{"paths":[null,null]}]},"partitionKey":{"kind":"Hash","paths":[null,null],"version":1},"indexingPolicy":{"indexingMode":"Consistent","spatialIndexes":[{"path":"path","types":["Point","Point"]},{"path":"path","types":["Point","Point"]}],"automatic":True,"includedPaths":[{"path":"path","indexes":[{"kind":"Hash","dataType":"String","precision":6},{"kind":"Hash","dataType":"String","precision":6}]},{"path":"path","indexes":[{"kind":"Hash","dataType":"String","precision":6},{"kind":"Hash","dataType":"String","precision":6}]}],"excludedPaths":[{"path":"path"},{"path":"path"}],"compositeIndexes":[[{"path":"path","order":"Ascending"},{"path":"path","order":"Ascending"}],[{"path":"path","order":"Ascending"},{"path":"path","order":"Ascending"}]]},"defaultTtl":0,"id":"id","conflictResolutionPolicy":{"mode":"LastWriterWins","conflictResolutionProcedure":"conflictResolutionProcedure","conflictResolutionPath":"conflictResolutionPath"}},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        json=create_update_sql_container_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_create_update_sql_database(client):
    """Test case for sql_resources_create_update_sql_database

    
    """
    create_update_sql_database_parameters = {"properties":{"resource":{"id":"id"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        json=create_update_sql_database_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_create_update_sql_stored_procedure(client):
    """Test case for sql_resources_create_update_sql_stored_procedure

    
    """
    create_update_sql_stored_procedure_parameters = {"properties":{"resource":{"id":"id","body":"body"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/storedProcedures/{stored_procedure_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', stored_procedure_name='stored_procedure_name_example'),
        headers=headers,
        json=create_update_sql_stored_procedure_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_create_update_sql_trigger(client):
    """Test case for sql_resources_create_update_sql_trigger

    
    """
    create_update_sql_trigger_parameters = {"properties":{"resource":{"id":"id","triggerType":"Pre","body":"body","triggerOperation":"All"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        json=create_update_sql_trigger_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_create_update_sql_user_defined_function(client):
    """Test case for sql_resources_create_update_sql_user_defined_function

    
    """
    create_update_sql_user_defined_function_parameters = {"properties":{"resource":{"id":"id","body":"body"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/userDefinedFunctions/{user_defined_function_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', user_defined_function_name='user_defined_function_name_example'),
        headers=headers,
        json=create_update_sql_user_defined_function_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_delete_sql_container(client):
    """Test case for sql_resources_delete_sql_container

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_delete_sql_database(client):
    """Test case for sql_resources_delete_sql_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_delete_sql_stored_procedure(client):
    """Test case for sql_resources_delete_sql_stored_procedure

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/storedProcedures/{stored_procedure_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', stored_procedure_name='stored_procedure_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_delete_sql_trigger(client):
    """Test case for sql_resources_delete_sql_trigger

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_delete_sql_user_defined_function(client):
    """Test case for sql_resources_delete_sql_user_defined_function

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/userDefinedFunctions/{user_defined_function_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', user_defined_function_name='user_defined_function_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_get_sql_container(client):
    """Test case for sql_resources_get_sql_container

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_get_sql_container_throughput(client):
    """Test case for sql_resources_get_sql_container_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_get_sql_database(client):
    """Test case for sql_resources_get_sql_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_get_sql_database_throughput(client):
    """Test case for sql_resources_get_sql_database_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_get_sql_stored_procedure(client):
    """Test case for sql_resources_get_sql_stored_procedure

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/storedProcedures/{stored_procedure_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', stored_procedure_name='stored_procedure_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_get_sql_trigger(client):
    """Test case for sql_resources_get_sql_trigger

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_get_sql_user_defined_function(client):
    """Test case for sql_resources_get_sql_user_defined_function

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/userDefinedFunctions/{user_defined_function_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example', user_defined_function_name='user_defined_function_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_list_sql_containers(client):
    """Test case for sql_resources_list_sql_containers

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_list_sql_databases(client):
    """Test case for sql_resources_list_sql_databases

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_list_sql_stored_procedures(client):
    """Test case for sql_resources_list_sql_stored_procedures

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/storedProcedures'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_list_sql_triggers(client):
    """Test case for sql_resources_list_sql_triggers

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/triggers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_list_sql_user_defined_functions(client):
    """Test case for sql_resources_list_sql_user_defined_functions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/userDefinedFunctions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_update_sql_container_throughput(client):
    """Test case for sql_resources_update_sql_container_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/containers/{container_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example', container_name='container_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_resources_update_sql_database_throughput(client):
    """Test case for sql_resources_update_sql_database_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/sqlDatabases/{database_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', database_name='database_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_table_resources_create_update_table(client):
    """Test case for table_resources_create_update_table

    
    """
    create_update_table_parameters = {"properties":{"resource":{"id":"id"},"options":{"key":"options"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/tables/{table_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', table_name='table_name_example'),
        headers=headers,
        json=create_update_table_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_table_resources_delete_table(client):
    """Test case for table_resources_delete_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/tables/{table_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_table_resources_get_table(client):
    """Test case for table_resources_get_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/tables/{table_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_table_resources_get_table_throughput(client):
    """Test case for table_resources_get_table_throughput

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/tables/{table_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_table_resources_list_tables(client):
    """Test case for table_resources_list_tables

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/tables'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_table_resources_update_table_throughput(client):
    """Test case for table_resources_update_table_throughput

    
    """
    update_throughput_parameters = {"properties":{"resource":{"offerReplacePending":"offerReplacePending","throughput":0,"minimumThroughput":"minimumThroughput"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DocumentDB/databaseAccounts/{account_name}/tables/{table_name}/throughputSettings/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', table_name='table_name_example'),
        headers=headers,
        json=update_throughput_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

