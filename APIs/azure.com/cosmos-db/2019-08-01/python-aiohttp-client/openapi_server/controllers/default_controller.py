from typing import List, Dict
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
from openapi_server import util


async def cassandra_resources_create_update_cassandra_keyspace(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, api_version, create_update_cassandra_keyspace_parameters) -> web.Response:
    """cassandra_resources_create_update_cassandra_keyspace

    Create or update an Azure Cosmos DB Cassandra keyspace

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_cassandra_keyspace_parameters: The parameters to provide for the current Cassandra keyspace.
    :type create_update_cassandra_keyspace_parameters: dict | bytes

    """
    create_update_cassandra_keyspace_parameters = CassandraKeyspaceCreateUpdateParameters.from_dict(create_update_cassandra_keyspace_parameters)
    return web.Response(status=200)


async def cassandra_resources_create_update_cassandra_table(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, table_name, api_version, create_update_cassandra_table_parameters) -> web.Response:
    """cassandra_resources_create_update_cassandra_table

    Create or update an Azure Cosmos DB Cassandra Table

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_cassandra_table_parameters: The parameters to provide for the current Cassandra Table.
    :type create_update_cassandra_table_parameters: dict | bytes

    """
    create_update_cassandra_table_parameters = CassandraTableCreateUpdateParameters.from_dict(create_update_cassandra_table_parameters)
    return web.Response(status=200)


async def cassandra_resources_delete_cassandra_keyspace(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, api_version) -> web.Response:
    """cassandra_resources_delete_cassandra_keyspace

    Deletes an existing Azure Cosmos DB Cassandra keyspace.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_delete_cassandra_table(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, table_name, api_version) -> web.Response:
    """cassandra_resources_delete_cassandra_table

    Deletes an existing Azure Cosmos DB Cassandra table.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_get_cassandra_keyspace(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, api_version) -> web.Response:
    """cassandra_resources_get_cassandra_keyspace

    Gets the Cassandra keyspaces under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_get_cassandra_keyspace_throughput(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, api_version) -> web.Response:
    """cassandra_resources_get_cassandra_keyspace_throughput

    Gets the RUs per second of the Cassandra Keyspace under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_get_cassandra_table(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, table_name, api_version) -> web.Response:
    """cassandra_resources_get_cassandra_table

    Gets the Cassandra table under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_get_cassandra_table_throughput(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, table_name, api_version) -> web.Response:
    """cassandra_resources_get_cassandra_table_throughput

    Gets the RUs per second of the Cassandra table under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_list_cassandra_keyspaces(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """cassandra_resources_list_cassandra_keyspaces

    Lists the Cassandra keyspaces under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_list_cassandra_tables(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, api_version) -> web.Response:
    """cassandra_resources_list_cassandra_tables

    Lists the Cassandra table under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def cassandra_resources_update_cassandra_keyspace_throughput(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, api_version, update_throughput_parameters) -> web.Response:
    """cassandra_resources_update_cassandra_keyspace_throughput

    Update RUs per second of an Azure Cosmos DB Cassandra Keyspace

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The RUs per second of the parameters to provide for the current Cassandra Keyspace.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def cassandra_resources_update_cassandra_table_throughput(request: web.Request, subscription_id, resource_group_name, account_name, keyspace_name, table_name, api_version, update_throughput_parameters) -> web.Response:
    """cassandra_resources_update_cassandra_table_throughput

    Update RUs per second of an Azure Cosmos DB Cassandra table

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param keyspace_name: Cosmos DB keyspace name.
    :type keyspace_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The RUs per second of the parameters to provide for the current Cassandra table.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def collection_list_metric_definitions(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, collection_rid, api_version) -> web.Response:
    """collection_list_metric_definitions

    Retrieves metric definitions for the given collection.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def collection_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, collection_rid, api_version, filter) -> web.Response:
    """collection_list_metrics

    Retrieves the metrics determined by the given filter for the given database account and collection.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def collection_list_usages(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, collection_rid, api_version, filter=None) -> web.Response:
    """collection_list_usages

    Retrieves the usages (most recent storage data) for the given collection.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    :type filter: str

    """
    return web.Response(status=200)


async def collection_partition_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, collection_rid, api_version, filter) -> web.Response:
    """collection_partition_list_metrics

    Retrieves the metrics determined by the given filter for the given collection, split by partition.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def collection_partition_list_usages(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, collection_rid, api_version, filter=None) -> web.Response:
    """collection_partition_list_usages

    Retrieves the usages (most recent storage data) for the given collection, split by partition.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    :type filter: str

    """
    return web.Response(status=200)


async def collection_partition_region_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, region, database_rid, collection_rid, api_version, filter) -> web.Response:
    """collection_partition_region_list_metrics

    Retrieves the metrics determined by the given filter for the given collection and region, split by partition.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param region: Cosmos DB region, with spaces between words and each word capitalized.
    :type region: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def collection_region_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, region, database_rid, collection_rid, api_version, filter) -> web.Response:
    """collection_region_list_metrics

    Retrieves the metrics determined by the given filter for the given database account, collection and region.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param region: Cosmos DB region, with spaces between words and each word capitalized.
    :type region: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def database_account_region_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, region, api_version, filter) -> web.Response:
    """database_account_region_list_metrics

    Retrieves the metrics determined by the given filter for the given database account and region.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param region: Cosmos DB region, with spaces between words and each word capitalized.
    :type region: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def database_accounts_check_name_exists(request: web.Request, account_name, api_version) -> web.Response:
    """database_accounts_check_name_exists

    Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the &#39;-&#39; character, and must be between 3 and 50 characters.

    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, create_update_parameters) -> web.Response:
    """database_accounts_create_or_update

    Creates or updates an Azure Cosmos DB database account. The \&quot;Update\&quot; method is preferred when performing updates on an account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_parameters: The parameters to provide for the current database account.
    :type create_update_parameters: dict | bytes

    """
    create_update_parameters = DatabaseAccountCreateUpdateParameters.from_dict(create_update_parameters)
    return web.Response(status=200)


async def database_accounts_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """database_accounts_delete

    Deletes an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_failover_priority_change(request: web.Request, subscription_id, resource_group_name, account_name, api_version, failover_parameters) -> web.Response:
    """database_accounts_failover_priority_change

    Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority &#x3D; (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param failover_parameters: The new failover policies for the database account.
    :type failover_parameters: dict | bytes

    """
    failover_parameters = FailoverPolicies.from_dict(failover_parameters)
    return web.Response(status=200)


async def database_accounts_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """database_accounts_get

    Retrieves the properties of an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_get_read_only_keys(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """database_accounts_get_read_only_keys

    Lists the read-only access keys for the specified Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """database_accounts_list

    Lists all the Azure Cosmos DB database accounts available under the subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def database_accounts_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """database_accounts_list_by_resource_group

    Lists all the Azure Cosmos DB database accounts available under the given resource group.

    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def database_accounts_list_connection_strings(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """database_accounts_list_connection_strings

    Lists the connection strings for the specified Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_list_keys(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """database_accounts_list_keys

    Lists the access keys for the specified Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_list_metric_definitions(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """database_accounts_list_metric_definitions

    Retrieves metric definitions for the given database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter) -> web.Response:
    """database_accounts_list_metrics

    Retrieves the metrics determined by the given filter for the given database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def database_accounts_list_read_only_keys(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """database_accounts_list_read_only_keys

    Lists the read-only access keys for the specified Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_accounts_list_usages(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter=None) -> web.Response:
    """database_accounts_list_usages

    Retrieves the usages (most recent data) for the given database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    :type filter: str

    """
    return web.Response(status=200)


async def database_accounts_offline_region(request: web.Request, subscription_id, resource_group_name, account_name, api_version, region_parameter_for_offline) -> web.Response:
    """database_accounts_offline_region

    Offline the specified region for the specified Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param region_parameter_for_offline: Cosmos DB region to offline for the database account.
    :type region_parameter_for_offline: dict | bytes

    """
    region_parameter_for_offline = RegionForOnlineOffline.from_dict(region_parameter_for_offline)
    return web.Response(status=200)


async def database_accounts_online_region(request: web.Request, subscription_id, resource_group_name, account_name, api_version, region_parameter_for_online) -> web.Response:
    """database_accounts_online_region

    Online the specified region for the specified Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param region_parameter_for_online: Cosmos DB region to online for the database account.
    :type region_parameter_for_online: dict | bytes

    """
    region_parameter_for_online = RegionForOnlineOffline.from_dict(region_parameter_for_online)
    return web.Response(status=200)


async def database_accounts_regenerate_key(request: web.Request, subscription_id, resource_group_name, account_name, api_version, key_to_regenerate) -> web.Response:
    """database_accounts_regenerate_key

    Regenerates an access key for the specified Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param key_to_regenerate: The name of the key to regenerate.
    :type key_to_regenerate: dict | bytes

    """
    key_to_regenerate = DatabaseAccountRegenerateKeyParameters.from_dict(key_to_regenerate)
    return web.Response(status=200)


async def database_accounts_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, update_parameters) -> web.Response:
    """database_accounts_update

    Updates the properties of an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_parameters: The parameters to provide for the current database account.
    :type update_parameters: dict | bytes

    """
    update_parameters = DatabaseAccountUpdateParameters.from_dict(update_parameters)
    return web.Response(status=200)


async def database_list_metric_definitions(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, api_version) -> web.Response:
    """database_list_metric_definitions

    Retrieves metric definitions for the given database.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, api_version, filter) -> web.Response:
    """database_list_metrics

    Retrieves the metrics determined by the given filter for the given database account and database.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def database_list_usages(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, api_version, filter=None) -> web.Response:
    """database_list_usages

    Retrieves the usages (most recent data) for the given database.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    :type filter: str

    """
    return web.Response(status=200)


async def gremlin_resources_create_update_gremlin_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version, create_update_gremlin_database_parameters) -> web.Response:
    """gremlin_resources_create_update_gremlin_database

    Create or update an Azure Cosmos DB Gremlin database

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_gremlin_database_parameters: The parameters to provide for the current Gremlin database.
    :type create_update_gremlin_database_parameters: dict | bytes

    """
    create_update_gremlin_database_parameters = GremlinDatabaseCreateUpdateParameters.from_dict(create_update_gremlin_database_parameters)
    return web.Response(status=200)


async def gremlin_resources_create_update_gremlin_graph(request: web.Request, subscription_id, resource_group_name, account_name, database_name, graph_name, api_version, create_update_gremlin_graph_parameters) -> web.Response:
    """gremlin_resources_create_update_gremlin_graph

    Create or update an Azure Cosmos DB Gremlin graph

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param graph_name: Cosmos DB graph name.
    :type graph_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_gremlin_graph_parameters: The parameters to provide for the current Gremlin graph.
    :type create_update_gremlin_graph_parameters: dict | bytes

    """
    create_update_gremlin_graph_parameters = GremlinGraphCreateUpdateParameters.from_dict(create_update_gremlin_graph_parameters)
    return web.Response(status=200)


async def gremlin_resources_delete_gremlin_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """gremlin_resources_delete_gremlin_database

    Deletes an existing Azure Cosmos DB Gremlin database.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_delete_gremlin_graph(request: web.Request, subscription_id, resource_group_name, account_name, database_name, graph_name, api_version) -> web.Response:
    """gremlin_resources_delete_gremlin_graph

    Deletes an existing Azure Cosmos DB Gremlin graph.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param graph_name: Cosmos DB graph name.
    :type graph_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_get_gremlin_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """gremlin_resources_get_gremlin_database

    Gets the Gremlin databases under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_get_gremlin_database_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """gremlin_resources_get_gremlin_database_throughput

    Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_get_gremlin_graph(request: web.Request, subscription_id, resource_group_name, account_name, database_name, graph_name, api_version) -> web.Response:
    """gremlin_resources_get_gremlin_graph

    Gets the Gremlin graph under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param graph_name: Cosmos DB graph name.
    :type graph_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_get_gremlin_graph_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, graph_name, api_version) -> web.Response:
    """gremlin_resources_get_gremlin_graph_throughput

    Gets the Gremlin graph throughput under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param graph_name: Cosmos DB graph name.
    :type graph_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_list_gremlin_databases(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """gremlin_resources_list_gremlin_databases

    Lists the Gremlin databases under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_list_gremlin_graphs(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """gremlin_resources_list_gremlin_graphs

    Lists the Gremlin graph under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def gremlin_resources_update_gremlin_database_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version, update_throughput_parameters) -> web.Response:
    """gremlin_resources_update_gremlin_database_throughput

    Update RUs per second of an Azure Cosmos DB Gremlin database

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The RUs per second of the parameters to provide for the current Gremlin database.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def gremlin_resources_update_gremlin_graph_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, graph_name, api_version, update_throughput_parameters) -> web.Response:
    """gremlin_resources_update_gremlin_graph_throughput

    Update RUs per second of an Azure Cosmos DB Gremlin graph

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param graph_name: Cosmos DB graph name.
    :type graph_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The RUs per second of the parameters to provide for the current Gremlin graph.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def mongo_db_resources_create_update_mongo_db_collection(request: web.Request, subscription_id, resource_group_name, account_name, database_name, collection_name, api_version, create_update_mongo_db_collection_parameters) -> web.Response:
    """mongo_db_resources_create_update_mongo_db_collection

    Create or update an Azure Cosmos DB MongoDB Collection

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param collection_name: Cosmos DB collection name.
    :type collection_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_mongo_db_collection_parameters: The parameters to provide for the current MongoDB Collection.
    :type create_update_mongo_db_collection_parameters: dict | bytes

    """
    create_update_mongo_db_collection_parameters = MongoDBCollectionCreateUpdateParameters.from_dict(create_update_mongo_db_collection_parameters)
    return web.Response(status=200)


async def mongo_db_resources_create_update_mongo_db_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version, create_update_mongo_db_database_parameters) -> web.Response:
    """mongo_db_resources_create_update_mongo_db_database

    Create or updates Azure Cosmos DB MongoDB database

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_mongo_db_database_parameters: The parameters to provide for the current MongoDB database.
    :type create_update_mongo_db_database_parameters: dict | bytes

    """
    create_update_mongo_db_database_parameters = MongoDBDatabaseCreateUpdateParameters.from_dict(create_update_mongo_db_database_parameters)
    return web.Response(status=200)


async def mongo_db_resources_delete_mongo_db_collection(request: web.Request, subscription_id, resource_group_name, account_name, database_name, collection_name, api_version) -> web.Response:
    """mongo_db_resources_delete_mongo_db_collection

    Deletes an existing Azure Cosmos DB MongoDB Collection.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param collection_name: Cosmos DB collection name.
    :type collection_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_delete_mongo_db_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """mongo_db_resources_delete_mongo_db_database

    Deletes an existing Azure Cosmos DB MongoDB database.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_get_mongo_db_collection(request: web.Request, subscription_id, resource_group_name, account_name, database_name, collection_name, api_version) -> web.Response:
    """mongo_db_resources_get_mongo_db_collection

    Gets the MongoDB collection under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param collection_name: Cosmos DB collection name.
    :type collection_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_get_mongo_db_collection_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, collection_name, api_version) -> web.Response:
    """mongo_db_resources_get_mongo_db_collection_throughput

    Gets the RUs per second of the MongoDB collection under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param collection_name: Cosmos DB collection name.
    :type collection_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_get_mongo_db_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """mongo_db_resources_get_mongo_db_database

    Gets the MongoDB databases under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_get_mongo_db_database_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """mongo_db_resources_get_mongo_db_database_throughput

    Gets the RUs per second of the MongoDB database under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_list_mongo_db_collections(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """mongo_db_resources_list_mongo_db_collections

    Lists the MongoDB collection under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_list_mongo_db_databases(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """mongo_db_resources_list_mongo_db_databases

    Lists the MongoDB databases under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def mongo_db_resources_update_mongo_db_collection_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, collection_name, api_version, update_throughput_parameters) -> web.Response:
    """mongo_db_resources_update_mongo_db_collection_throughput

    Update the RUs per second of an Azure Cosmos DB MongoDB collection

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param collection_name: Cosmos DB collection name.
    :type collection_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The RUs per second of the parameters to provide for the current MongoDB collection.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def mongo_db_resources_update_mongo_db_database_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version, update_throughput_parameters) -> web.Response:
    """mongo_db_resources_update_mongo_db_database_throughput

    Update RUs per second of the an Azure Cosmos DB MongoDB database

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The RUs per second of the parameters to provide for the current MongoDB database.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def partition_key_range_id_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, database_rid, collection_rid, partition_key_range_id, api_version, filter) -> web.Response:
    """partition_key_range_id_list_metrics

    Retrieves the metrics determined by the given filter for the given partition key range id.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param partition_key_range_id: Partition Key Range Id for which to get data.
    :type partition_key_range_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def partition_key_range_id_region_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, region, database_rid, collection_rid, partition_key_range_id, api_version, filter) -> web.Response:
    """partition_key_range_id_region_list_metrics

    Retrieves the metrics determined by the given filter for the given partition key range id and region.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param region: Cosmos DB region, with spaces between words and each word capitalized.
    :type region: str
    :param database_rid: Cosmos DB database rid.
    :type database_rid: str
    :param collection_rid: Cosmos DB collection rid.
    :type collection_rid: str
    :param partition_key_range_id: Partition Key Range Id for which to get data.
    :type partition_key_range_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def percentile_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter) -> web.Response:
    """percentile_list_metrics

    Retrieves the metrics determined by the given filter for the given database account. This url is only for PBS and Replication Latency data

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def percentile_source_target_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, source_region, target_region, api_version, filter) -> web.Response:
    """percentile_source_target_list_metrics

    Retrieves the metrics determined by the given filter for the given account, source and target region. This url is only for PBS and Replication Latency data

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param source_region: Source region from which data is written. Cosmos DB region, with spaces between words and each word capitalized.
    :type source_region: str
    :param target_region: Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.
    :type target_region: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def percentile_target_list_metrics(request: web.Request, subscription_id, resource_group_name, account_name, target_region, api_version, filter) -> web.Response:
    """percentile_target_list_metrics

    Retrieves the metrics determined by the given filter for the given account target region. This url is only for PBS and Replication Latency data

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param target_region: Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.
    :type target_region: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param filter: An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    :type filter: str

    """
    return web.Response(status=200)


async def sql_resources_create_update_sql_container(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version, create_update_sql_container_parameters) -> web.Response:
    """sql_resources_create_update_sql_container

    Create or update an Azure Cosmos DB SQL container

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_sql_container_parameters: The parameters to provide for the current SQL container.
    :type create_update_sql_container_parameters: dict | bytes

    """
    create_update_sql_container_parameters = SqlContainerCreateUpdateParameters.from_dict(create_update_sql_container_parameters)
    return web.Response(status=200)


async def sql_resources_create_update_sql_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version, create_update_sql_database_parameters) -> web.Response:
    """sql_resources_create_update_sql_database

    Create or update an Azure Cosmos DB SQL database

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_sql_database_parameters: The parameters to provide for the current SQL database.
    :type create_update_sql_database_parameters: dict | bytes

    """
    create_update_sql_database_parameters = SqlDatabaseCreateUpdateParameters.from_dict(create_update_sql_database_parameters)
    return web.Response(status=200)


async def sql_resources_create_update_sql_stored_procedure(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, stored_procedure_name, api_version, create_update_sql_stored_procedure_parameters) -> web.Response:
    """sql_resources_create_update_sql_stored_procedure

    Create or update an Azure Cosmos DB SQL storedProcedure

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param stored_procedure_name: Cosmos DB storedProcedure name.
    :type stored_procedure_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_sql_stored_procedure_parameters: The parameters to provide for the current SQL storedProcedure.
    :type create_update_sql_stored_procedure_parameters: dict | bytes

    """
    create_update_sql_stored_procedure_parameters = SqlStoredProcedureCreateUpdateParameters.from_dict(create_update_sql_stored_procedure_parameters)
    return web.Response(status=200)


async def sql_resources_create_update_sql_trigger(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, trigger_name, api_version, create_update_sql_trigger_parameters) -> web.Response:
    """sql_resources_create_update_sql_trigger

    Create or update an Azure Cosmos DB SQL trigger

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param trigger_name: Cosmos DB trigger name.
    :type trigger_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_sql_trigger_parameters: The parameters to provide for the current SQL trigger.
    :type create_update_sql_trigger_parameters: dict | bytes

    """
    create_update_sql_trigger_parameters = SqlTriggerCreateUpdateParameters.from_dict(create_update_sql_trigger_parameters)
    return web.Response(status=200)


async def sql_resources_create_update_sql_user_defined_function(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, user_defined_function_name, api_version, create_update_sql_user_defined_function_parameters) -> web.Response:
    """sql_resources_create_update_sql_user_defined_function

    Create or update an Azure Cosmos DB SQL userDefinedFunction

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param user_defined_function_name: Cosmos DB userDefinedFunction name.
    :type user_defined_function_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_sql_user_defined_function_parameters: The parameters to provide for the current SQL userDefinedFunction.
    :type create_update_sql_user_defined_function_parameters: dict | bytes

    """
    create_update_sql_user_defined_function_parameters = SqlUserDefinedFunctionCreateUpdateParameters.from_dict(create_update_sql_user_defined_function_parameters)
    return web.Response(status=200)


async def sql_resources_delete_sql_container(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version) -> web.Response:
    """sql_resources_delete_sql_container

    Deletes an existing Azure Cosmos DB SQL container.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_delete_sql_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """sql_resources_delete_sql_database

    Deletes an existing Azure Cosmos DB SQL database.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_delete_sql_stored_procedure(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, stored_procedure_name, api_version) -> web.Response:
    """sql_resources_delete_sql_stored_procedure

    Deletes an existing Azure Cosmos DB SQL storedProcedure.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param stored_procedure_name: Cosmos DB storedProcedure name.
    :type stored_procedure_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_delete_sql_trigger(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, trigger_name, api_version) -> web.Response:
    """sql_resources_delete_sql_trigger

    Deletes an existing Azure Cosmos DB SQL trigger.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param trigger_name: Cosmos DB trigger name.
    :type trigger_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_delete_sql_user_defined_function(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, user_defined_function_name, api_version) -> web.Response:
    """sql_resources_delete_sql_user_defined_function

    Deletes an existing Azure Cosmos DB SQL userDefinedFunction.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param user_defined_function_name: Cosmos DB userDefinedFunction name.
    :type user_defined_function_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_get_sql_container(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version) -> web.Response:
    """sql_resources_get_sql_container

    Gets the SQL container under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_get_sql_container_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version) -> web.Response:
    """sql_resources_get_sql_container_throughput

    Gets the RUs per second of the SQL container under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_get_sql_database(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """sql_resources_get_sql_database

    Gets the SQL database under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_get_sql_database_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """sql_resources_get_sql_database_throughput

    Gets the RUs per second of the SQL database under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_get_sql_stored_procedure(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, stored_procedure_name, api_version) -> web.Response:
    """sql_resources_get_sql_stored_procedure

    Gets the SQL storedProcedure under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param stored_procedure_name: Cosmos DB storedProcedure name.
    :type stored_procedure_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_get_sql_trigger(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, trigger_name, api_version) -> web.Response:
    """sql_resources_get_sql_trigger

    Gets the SQL trigger under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param trigger_name: Cosmos DB trigger name.
    :type trigger_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_get_sql_user_defined_function(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, user_defined_function_name, api_version) -> web.Response:
    """sql_resources_get_sql_user_defined_function

    Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param user_defined_function_name: Cosmos DB userDefinedFunction name.
    :type user_defined_function_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_list_sql_containers(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version) -> web.Response:
    """sql_resources_list_sql_containers

    Lists the SQL container under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_list_sql_databases(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """sql_resources_list_sql_databases

    Lists the SQL databases under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_list_sql_stored_procedures(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version) -> web.Response:
    """sql_resources_list_sql_stored_procedures

    Lists the SQL storedProcedure under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_list_sql_triggers(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version) -> web.Response:
    """sql_resources_list_sql_triggers

    Lists the SQL trigger under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_list_sql_user_defined_functions(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version) -> web.Response:
    """sql_resources_list_sql_user_defined_functions

    Lists the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def sql_resources_update_sql_container_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, container_name, api_version, update_throughput_parameters) -> web.Response:
    """sql_resources_update_sql_container_throughput

    Update RUs per second of an Azure Cosmos DB SQL container

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param container_name: Cosmos DB container name.
    :type container_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The parameters to provide for the RUs per second of the current SQL container.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def sql_resources_update_sql_database_throughput(request: web.Request, subscription_id, resource_group_name, account_name, database_name, api_version, update_throughput_parameters) -> web.Response:
    """sql_resources_update_sql_database_throughput

    Update RUs per second of an Azure Cosmos DB SQL database

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param database_name: Cosmos DB database name.
    :type database_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The parameters to provide for the RUs per second of the current SQL database.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)


async def table_resources_create_update_table(request: web.Request, subscription_id, resource_group_name, account_name, table_name, api_version, create_update_table_parameters) -> web.Response:
    """table_resources_create_update_table

    Create or update an Azure Cosmos DB Table

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param create_update_table_parameters: The parameters to provide for the current Table.
    :type create_update_table_parameters: dict | bytes

    """
    create_update_table_parameters = TableCreateUpdateParameters.from_dict(create_update_table_parameters)
    return web.Response(status=200)


async def table_resources_delete_table(request: web.Request, subscription_id, resource_group_name, account_name, table_name, api_version) -> web.Response:
    """table_resources_delete_table

    Deletes an existing Azure Cosmos DB Table.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def table_resources_get_table(request: web.Request, subscription_id, resource_group_name, account_name, table_name, api_version) -> web.Response:
    """table_resources_get_table

    Gets the Tables under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def table_resources_get_table_throughput(request: web.Request, subscription_id, resource_group_name, account_name, table_name, api_version) -> web.Response:
    """table_resources_get_table_throughput

    Gets the RUs per second of the Table under an existing Azure Cosmos DB database account with the provided name.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def table_resources_list_tables(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """table_resources_list_tables

    Lists the Tables under an existing Azure Cosmos DB database account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str

    """
    return web.Response(status=200)


async def table_resources_update_table_throughput(request: web.Request, subscription_id, resource_group_name, account_name, table_name, api_version, update_throughput_parameters) -> web.Response:
    """table_resources_update_table_throughput

    Update RUs per second of an Azure Cosmos DB Table

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param table_name: Cosmos DB table name.
    :type table_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param update_throughput_parameters: The parameters to provide for the RUs per second of the current Table.
    :type update_throughput_parameters: dict | bytes

    """
    update_throughput_parameters = ThroughputSettingsUpdateParameters.from_dict(update_throughput_parameters)
    return web.Response(status=200)
