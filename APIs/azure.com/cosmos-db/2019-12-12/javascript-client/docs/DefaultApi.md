# CosmosDb.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cassandraResourcesCreateUpdateCassandraKeyspace**](DefaultApi.md#cassandraResourcesCreateUpdateCassandraKeyspace) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName} | 
[**cassandraResourcesCreateUpdateCassandraTable**](DefaultApi.md#cassandraResourcesCreateUpdateCassandraTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName} | 
[**cassandraResourcesDeleteCassandraKeyspace**](DefaultApi.md#cassandraResourcesDeleteCassandraKeyspace) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName} | 
[**cassandraResourcesDeleteCassandraTable**](DefaultApi.md#cassandraResourcesDeleteCassandraTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName} | 
[**cassandraResourcesGetCassandraKeyspace**](DefaultApi.md#cassandraResourcesGetCassandraKeyspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName} | 
[**cassandraResourcesGetCassandraKeyspaceThroughput**](DefaultApi.md#cassandraResourcesGetCassandraKeyspaceThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/throughputSettings/default | 
[**cassandraResourcesGetCassandraTable**](DefaultApi.md#cassandraResourcesGetCassandraTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName} | 
[**cassandraResourcesGetCassandraTableThroughput**](DefaultApi.md#cassandraResourcesGetCassandraTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}/throughputSettings/default | 
[**cassandraResourcesListCassandraKeyspaces**](DefaultApi.md#cassandraResourcesListCassandraKeyspaces) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces | 
[**cassandraResourcesListCassandraTables**](DefaultApi.md#cassandraResourcesListCassandraTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables | 
[**cassandraResourcesUpdateCassandraKeyspaceThroughput**](DefaultApi.md#cassandraResourcesUpdateCassandraKeyspaceThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/throughputSettings/default | 
[**cassandraResourcesUpdateCassandraTableThroughput**](DefaultApi.md#cassandraResourcesUpdateCassandraTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}/throughputSettings/default | 
[**collectionListMetricDefinitions**](DefaultApi.md#collectionListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metricDefinitions | 
[**collectionListMetrics**](DefaultApi.md#collectionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metrics | 
[**collectionListUsages**](DefaultApi.md#collectionListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/usages | 
[**collectionPartitionListMetrics**](DefaultApi.md#collectionPartitionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitions/metrics | 
[**collectionPartitionListUsages**](DefaultApi.md#collectionPartitionListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitions/usages | 
[**collectionPartitionRegionListMetrics**](DefaultApi.md#collectionPartitionRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/partitions/metrics | 
[**collectionRegionListMetrics**](DefaultApi.md#collectionRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/metrics | 
[**databaseAccountRegionListMetrics**](DefaultApi.md#databaseAccountRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/metrics | 
[**databaseAccountsCheckNameExists**](DefaultApi.md#databaseAccountsCheckNameExists) | **HEAD** /providers/Microsoft.DocumentDB/databaseAccountNames/{accountName} | 
[**databaseAccountsCreateOrUpdate**](DefaultApi.md#databaseAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} | 
[**databaseAccountsDelete**](DefaultApi.md#databaseAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} | 
[**databaseAccountsFailoverPriorityChange**](DefaultApi.md#databaseAccountsFailoverPriorityChange) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/failoverPriorityChange | 
[**databaseAccountsGet**](DefaultApi.md#databaseAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} | 
[**databaseAccountsGetReadOnlyKeys**](DefaultApi.md#databaseAccountsGetReadOnlyKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys | 
[**databaseAccountsList**](DefaultApi.md#databaseAccountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/databaseAccounts | 
[**databaseAccountsListByResourceGroup**](DefaultApi.md#databaseAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts | 
[**databaseAccountsListConnectionStrings**](DefaultApi.md#databaseAccountsListConnectionStrings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listConnectionStrings | 
[**databaseAccountsListKeys**](DefaultApi.md#databaseAccountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listKeys | 
[**databaseAccountsListMetricDefinitions**](DefaultApi.md#databaseAccountsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metricDefinitions | 
[**databaseAccountsListMetrics**](DefaultApi.md#databaseAccountsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metrics | 
[**databaseAccountsListReadOnlyKeys**](DefaultApi.md#databaseAccountsListReadOnlyKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys | 
[**databaseAccountsListUsages**](DefaultApi.md#databaseAccountsListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/usages | 
[**databaseAccountsOfflineRegion**](DefaultApi.md#databaseAccountsOfflineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/offlineRegion | 
[**databaseAccountsOnlineRegion**](DefaultApi.md#databaseAccountsOnlineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/onlineRegion | 
[**databaseAccountsRegenerateKey**](DefaultApi.md#databaseAccountsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/regenerateKey | 
[**databaseAccountsUpdate**](DefaultApi.md#databaseAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} | 
[**databaseListMetricDefinitions**](DefaultApi.md#databaseListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metricDefinitions | 
[**databaseListMetrics**](DefaultApi.md#databaseListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metrics | 
[**databaseListUsages**](DefaultApi.md#databaseListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/usages | 
[**gremlinResourcesCreateUpdateGremlinDatabase**](DefaultApi.md#gremlinResourcesCreateUpdateGremlinDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName} | 
[**gremlinResourcesCreateUpdateGremlinGraph**](DefaultApi.md#gremlinResourcesCreateUpdateGremlinGraph) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName} | 
[**gremlinResourcesDeleteGremlinDatabase**](DefaultApi.md#gremlinResourcesDeleteGremlinDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName} | 
[**gremlinResourcesDeleteGremlinGraph**](DefaultApi.md#gremlinResourcesDeleteGremlinGraph) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName} | 
[**gremlinResourcesGetGremlinDatabase**](DefaultApi.md#gremlinResourcesGetGremlinDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName} | 
[**gremlinResourcesGetGremlinDatabaseThroughput**](DefaultApi.md#gremlinResourcesGetGremlinDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/throughputSettings/default | 
[**gremlinResourcesGetGremlinGraph**](DefaultApi.md#gremlinResourcesGetGremlinGraph) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName} | 
[**gremlinResourcesGetGremlinGraphThroughput**](DefaultApi.md#gremlinResourcesGetGremlinGraphThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}/throughputSettings/default | 
[**gremlinResourcesListGremlinDatabases**](DefaultApi.md#gremlinResourcesListGremlinDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases | 
[**gremlinResourcesListGremlinGraphs**](DefaultApi.md#gremlinResourcesListGremlinGraphs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs | 
[**gremlinResourcesUpdateGremlinDatabaseThroughput**](DefaultApi.md#gremlinResourcesUpdateGremlinDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/throughputSettings/default | 
[**gremlinResourcesUpdateGremlinGraphThroughput**](DefaultApi.md#gremlinResourcesUpdateGremlinGraphThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}/throughputSettings/default | 
[**mongoDBResourcesCreateUpdateMongoDBCollection**](DefaultApi.md#mongoDBResourcesCreateUpdateMongoDBCollection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName} | 
[**mongoDBResourcesCreateUpdateMongoDBDatabase**](DefaultApi.md#mongoDBResourcesCreateUpdateMongoDBDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName} | 
[**mongoDBResourcesDeleteMongoDBCollection**](DefaultApi.md#mongoDBResourcesDeleteMongoDBCollection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName} | 
[**mongoDBResourcesDeleteMongoDBDatabase**](DefaultApi.md#mongoDBResourcesDeleteMongoDBDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName} | 
[**mongoDBResourcesGetMongoDBCollection**](DefaultApi.md#mongoDBResourcesGetMongoDBCollection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName} | 
[**mongoDBResourcesGetMongoDBCollectionThroughput**](DefaultApi.md#mongoDBResourcesGetMongoDBCollectionThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}/throughputSettings/default | 
[**mongoDBResourcesGetMongoDBDatabase**](DefaultApi.md#mongoDBResourcesGetMongoDBDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName} | 
[**mongoDBResourcesGetMongoDBDatabaseThroughput**](DefaultApi.md#mongoDBResourcesGetMongoDBDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/throughputSettings/default | 
[**mongoDBResourcesListMongoDBCollections**](DefaultApi.md#mongoDBResourcesListMongoDBCollections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections | 
[**mongoDBResourcesListMongoDBDatabases**](DefaultApi.md#mongoDBResourcesListMongoDBDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases | 
[**mongoDBResourcesUpdateMongoDBCollectionThroughput**](DefaultApi.md#mongoDBResourcesUpdateMongoDBCollectionThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}/throughputSettings/default | 
[**mongoDBResourcesUpdateMongoDBDatabaseThroughput**](DefaultApi.md#mongoDBResourcesUpdateMongoDBDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/throughputSettings/default | 
[**partitionKeyRangeIdListMetrics**](DefaultApi.md#partitionKeyRangeIdListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics | 
[**partitionKeyRangeIdRegionListMetrics**](DefaultApi.md#partitionKeyRangeIdRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics | 
[**percentileListMetrics**](DefaultApi.md#percentileListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/percentile/metrics | 
[**percentileSourceTargetListMetrics**](DefaultApi.md#percentileSourceTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sourceRegion/{sourceRegion}/targetRegion/{targetRegion}/percentile/metrics | 
[**percentileTargetListMetrics**](DefaultApi.md#percentileTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/targetRegion/{targetRegion}/percentile/metrics | 
[**sqlResourcesCreateUpdateSqlContainer**](DefaultApi.md#sqlResourcesCreateUpdateSqlContainer) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName} | 
[**sqlResourcesCreateUpdateSqlDatabase**](DefaultApi.md#sqlResourcesCreateUpdateSqlDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName} | 
[**sqlResourcesCreateUpdateSqlStoredProcedure**](DefaultApi.md#sqlResourcesCreateUpdateSqlStoredProcedure) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName} | 
[**sqlResourcesCreateUpdateSqlTrigger**](DefaultApi.md#sqlResourcesCreateUpdateSqlTrigger) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName} | 
[**sqlResourcesCreateUpdateSqlUserDefinedFunction**](DefaultApi.md#sqlResourcesCreateUpdateSqlUserDefinedFunction) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName} | 
[**sqlResourcesDeleteSqlContainer**](DefaultApi.md#sqlResourcesDeleteSqlContainer) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName} | 
[**sqlResourcesDeleteSqlDatabase**](DefaultApi.md#sqlResourcesDeleteSqlDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName} | 
[**sqlResourcesDeleteSqlStoredProcedure**](DefaultApi.md#sqlResourcesDeleteSqlStoredProcedure) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName} | 
[**sqlResourcesDeleteSqlTrigger**](DefaultApi.md#sqlResourcesDeleteSqlTrigger) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName} | 
[**sqlResourcesDeleteSqlUserDefinedFunction**](DefaultApi.md#sqlResourcesDeleteSqlUserDefinedFunction) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName} | 
[**sqlResourcesGetSqlContainer**](DefaultApi.md#sqlResourcesGetSqlContainer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName} | 
[**sqlResourcesGetSqlContainerThroughput**](DefaultApi.md#sqlResourcesGetSqlContainerThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/throughputSettings/default | 
[**sqlResourcesGetSqlDatabase**](DefaultApi.md#sqlResourcesGetSqlDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName} | 
[**sqlResourcesGetSqlDatabaseThroughput**](DefaultApi.md#sqlResourcesGetSqlDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/throughputSettings/default | 
[**sqlResourcesGetSqlStoredProcedure**](DefaultApi.md#sqlResourcesGetSqlStoredProcedure) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName} | 
[**sqlResourcesGetSqlTrigger**](DefaultApi.md#sqlResourcesGetSqlTrigger) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName} | 
[**sqlResourcesGetSqlUserDefinedFunction**](DefaultApi.md#sqlResourcesGetSqlUserDefinedFunction) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName} | 
[**sqlResourcesListSqlContainers**](DefaultApi.md#sqlResourcesListSqlContainers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers | 
[**sqlResourcesListSqlDatabases**](DefaultApi.md#sqlResourcesListSqlDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases | 
[**sqlResourcesListSqlStoredProcedures**](DefaultApi.md#sqlResourcesListSqlStoredProcedures) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures | 
[**sqlResourcesListSqlTriggers**](DefaultApi.md#sqlResourcesListSqlTriggers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers | 
[**sqlResourcesListSqlUserDefinedFunctions**](DefaultApi.md#sqlResourcesListSqlUserDefinedFunctions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions | 
[**sqlResourcesUpdateSqlContainerThroughput**](DefaultApi.md#sqlResourcesUpdateSqlContainerThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/throughputSettings/default | 
[**sqlResourcesUpdateSqlDatabaseThroughput**](DefaultApi.md#sqlResourcesUpdateSqlDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/throughputSettings/default | 
[**tableResourcesCreateUpdateTable**](DefaultApi.md#tableResourcesCreateUpdateTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName} | 
[**tableResourcesDeleteTable**](DefaultApi.md#tableResourcesDeleteTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName} | 
[**tableResourcesGetTable**](DefaultApi.md#tableResourcesGetTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName} | 
[**tableResourcesGetTableThroughput**](DefaultApi.md#tableResourcesGetTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}/throughputSettings/default | 
[**tableResourcesListTables**](DefaultApi.md#tableResourcesListTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables | 
[**tableResourcesUpdateTableThroughput**](DefaultApi.md#tableResourcesUpdateTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}/throughputSettings/default | 



## cassandraResourcesCreateUpdateCassandraKeyspace

> CassandraKeyspaceGetResults cassandraResourcesCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters)



Create or update an Azure Cosmos DB Cassandra keyspace

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateCassandraKeyspaceParameters = new CosmosDb.CassandraKeyspaceCreateUpdateParameters(); // CassandraKeyspaceCreateUpdateParameters | The parameters to provide for the current Cassandra keyspace.
apiInstance.cassandraResourcesCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateCassandraKeyspaceParameters** | [**CassandraKeyspaceCreateUpdateParameters**](CassandraKeyspaceCreateUpdateParameters.md)| The parameters to provide for the current Cassandra keyspace. | 

### Return type

[**CassandraKeyspaceGetResults**](CassandraKeyspaceGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cassandraResourcesCreateUpdateCassandraTable

> CassandraTableGetResults cassandraResourcesCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters)



Create or update an Azure Cosmos DB Cassandra Table

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateCassandraTableParameters = new CosmosDb.CassandraTableCreateUpdateParameters(); // CassandraTableCreateUpdateParameters | The parameters to provide for the current Cassandra Table.
apiInstance.cassandraResourcesCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateCassandraTableParameters** | [**CassandraTableCreateUpdateParameters**](CassandraTableCreateUpdateParameters.md)| The parameters to provide for the current Cassandra Table. | 

### Return type

[**CassandraTableGetResults**](CassandraTableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cassandraResourcesDeleteCassandraKeyspace

> cassandraResourcesDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Deletes an existing Azure Cosmos DB Cassandra keyspace.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cassandraResourcesDeleteCassandraTable

> cassandraResourcesDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



Deletes an existing Azure Cosmos DB Cassandra table.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cassandraResourcesGetCassandraKeyspace

> CassandraKeyspaceGetResults cassandraResourcesGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Gets the Cassandra keyspaces under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**CassandraKeyspaceGetResults**](CassandraKeyspaceGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cassandraResourcesGetCassandraKeyspaceThroughput

> ThroughputSettingsGetResults cassandraResourcesGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Gets the RUs per second of the Cassandra Keyspace under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cassandraResourcesGetCassandraTable

> CassandraTableGetResults cassandraResourcesGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



Gets the Cassandra table under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**CassandraTableGetResults**](CassandraTableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cassandraResourcesGetCassandraTableThroughput

> ThroughputSettingsGetResults cassandraResourcesGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



Gets the RUs per second of the Cassandra table under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cassandraResourcesListCassandraKeyspaces

> CassandraKeyspaceListResult cassandraResourcesListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Cassandra keyspaces under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**CassandraKeyspaceListResult**](CassandraKeyspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cassandraResourcesListCassandraTables

> CassandraTableListResult cassandraResourcesListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Lists the Cassandra table under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.cassandraResourcesListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**CassandraTableListResult**](CassandraTableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cassandraResourcesUpdateCassandraKeyspaceThroughput

> ThroughputSettingsGetResults cassandraResourcesUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Cassandra Keyspace

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra Keyspace.
apiInstance.cassandraResourcesUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra Keyspace. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cassandraResourcesUpdateCassandraTableThroughput

> ThroughputSettingsGetResults cassandraResourcesUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Cassandra table

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra table.
apiInstance.cassandraResourcesUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **keyspaceName** | **String**| Cosmos DB keyspace name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra table. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionListMetricDefinitions

> MetricDefinitionsListResult collectionListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion)



Retrieves metric definitions for the given collection.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.collectionListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**MetricDefinitionsListResult**](MetricDefinitionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionListMetrics

> MetricListResult collectionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given database account and collection.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.collectionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionListUsages

> UsagesResult collectionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, opts)



Retrieves the usages (most recent storage data) for the given collection.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let opts = {
  'filter': "filter_example" // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
};
apiInstance.collectionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] 

### Return type

[**UsagesResult**](UsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionPartitionListMetrics

> PartitionMetricListResult collectionPartitionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given collection, split by partition.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.collectionPartitionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionPartitionListUsages

> PartitionUsagesResult collectionPartitionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, opts)



Retrieves the usages (most recent storage data) for the given collection, split by partition.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let opts = {
  'filter': "filter_example" // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
};
apiInstance.collectionPartitionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] 

### Return type

[**PartitionUsagesResult**](PartitionUsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionPartitionRegionListMetrics

> PartitionMetricListResult collectionPartitionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given collection and region, split by partition.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.collectionPartitionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionRegionListMetrics

> MetricListResult collectionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given database account, collection and region.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.collectionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountRegionListMetrics

> MetricListResult databaseAccountRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given database account and region.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.databaseAccountRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsCheckNameExists

> databaseAccountsCheckNameExists(accountName, apiVersion)



Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the &#39;-&#39; character, and must be between 3 and 50 characters.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsCheckNameExists(accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsCreateOrUpdate

> DatabaseAccountGetResults databaseAccountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, createUpdateParameters)



Creates or updates an Azure Cosmos DB database account. The \&quot;Update\&quot; method is preferred when performing updates on an account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateParameters = new CosmosDb.DatabaseAccountCreateUpdateParameters(); // DatabaseAccountCreateUpdateParameters | The parameters to provide for the current database account.
apiInstance.databaseAccountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, createUpdateParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateParameters** | [**DatabaseAccountCreateUpdateParameters**](DatabaseAccountCreateUpdateParameters.md)| The parameters to provide for the current database account. | 

### Return type

[**DatabaseAccountGetResults**](DatabaseAccountGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsDelete

> databaseAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Deletes an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsFailoverPriorityChange

> databaseAccountsFailoverPriorityChange(subscriptionId, resourceGroupName, accountName, apiVersion, failoverParameters)



Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority &#x3D; (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let failoverParameters = new CosmosDb.FailoverPolicies(); // FailoverPolicies | The new failover policies for the database account.
apiInstance.databaseAccountsFailoverPriorityChange(subscriptionId, resourceGroupName, accountName, apiVersion, failoverParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **failoverParameters** | [**FailoverPolicies**](FailoverPolicies.md)| The new failover policies for the database account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## databaseAccountsGet

> DatabaseAccountGetResults databaseAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Retrieves the properties of an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**DatabaseAccountGetResults**](DatabaseAccountGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetReadOnlyKeys

> DatabaseAccountListReadOnlyKeysResult databaseAccountsGetReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the read-only access keys for the specified Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsGetReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**DatabaseAccountListReadOnlyKeysResult**](DatabaseAccountListReadOnlyKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsList

> DatabaseAccountsListResult databaseAccountsList(apiVersion, subscriptionId)



Lists all the Azure Cosmos DB database accounts available under the subscription.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
apiInstance.databaseAccountsList(apiVersion, subscriptionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **subscriptionId** | **String**| Azure subscription ID. | 

### Return type

[**DatabaseAccountsListResult**](DatabaseAccountsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListByResourceGroup

> DatabaseAccountsListResult databaseAccountsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all the Azure Cosmos DB database accounts available under the given resource group.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
apiInstance.databaseAccountsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **subscriptionId** | **String**| Azure subscription ID. | 

### Return type

[**DatabaseAccountsListResult**](DatabaseAccountsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListConnectionStrings

> DatabaseAccountListConnectionStringsResult databaseAccountsListConnectionStrings(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the connection strings for the specified Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsListConnectionStrings(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**DatabaseAccountListConnectionStringsResult**](DatabaseAccountListConnectionStringsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListKeys

> DatabaseAccountListKeysResult databaseAccountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the access keys for the specified Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**DatabaseAccountListKeysResult**](DatabaseAccountListKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListMetricDefinitions

> MetricDefinitionsListResult databaseAccountsListMetricDefinitions(subscriptionId, resourceGroupName, accountName, apiVersion)



Retrieves metric definitions for the given database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsListMetricDefinitions(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**MetricDefinitionsListResult**](MetricDefinitionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListMetrics

> MetricListResult databaseAccountsListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.databaseAccountsListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListReadOnlyKeys

> DatabaseAccountListReadOnlyKeysResult databaseAccountsListReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the read-only access keys for the specified Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseAccountsListReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**DatabaseAccountListReadOnlyKeysResult**](DatabaseAccountListReadOnlyKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListUsages

> UsagesResult databaseAccountsListUsages(subscriptionId, resourceGroupName, accountName, apiVersion, opts)



Retrieves the usages (most recent data) for the given database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let opts = {
  'filter': "filter_example" // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
};
apiInstance.databaseAccountsListUsages(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] 

### Return type

[**UsagesResult**](UsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsOfflineRegion

> databaseAccountsOfflineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOffline)



Offline the specified region for the specified Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let regionParameterForOffline = new CosmosDb.RegionForOnlineOffline(); // RegionForOnlineOffline | Cosmos DB region to offline for the database account.
apiInstance.databaseAccountsOfflineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOffline, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **regionParameterForOffline** | [**RegionForOnlineOffline**](RegionForOnlineOffline.md)| Cosmos DB region to offline for the database account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsOnlineRegion

> databaseAccountsOnlineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOnline)



Online the specified region for the specified Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let regionParameterForOnline = new CosmosDb.RegionForOnlineOffline(); // RegionForOnlineOffline | Cosmos DB region to online for the database account.
apiInstance.databaseAccountsOnlineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOnline, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **regionParameterForOnline** | [**RegionForOnlineOffline**](RegionForOnlineOffline.md)| Cosmos DB region to online for the database account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsRegenerateKey

> databaseAccountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, keyToRegenerate)



Regenerates an access key for the specified Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let keyToRegenerate = new CosmosDb.DatabaseAccountRegenerateKeyParameters(); // DatabaseAccountRegenerateKeyParameters | The name of the key to regenerate.
apiInstance.databaseAccountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, keyToRegenerate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **keyToRegenerate** | [**DatabaseAccountRegenerateKeyParameters**](DatabaseAccountRegenerateKeyParameters.md)| The name of the key to regenerate. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## databaseAccountsUpdate

> DatabaseAccountGetResults databaseAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters)



Updates the properties of an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateParameters = new CosmosDb.DatabaseAccountUpdateParameters(); // DatabaseAccountUpdateParameters | The parameters to provide for the current database account.
apiInstance.databaseAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateParameters** | [**DatabaseAccountUpdateParameters**](DatabaseAccountUpdateParameters.md)| The parameters to provide for the current database account. | 

### Return type

[**DatabaseAccountGetResults**](DatabaseAccountGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseListMetricDefinitions

> MetricDefinitionsListResult databaseListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion)



Retrieves metric definitions for the given database.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.databaseListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**MetricDefinitionsListResult**](MetricDefinitionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseListMetrics

> MetricListResult databaseListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given database account and database.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.databaseListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseListUsages

> UsagesResult databaseListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, opts)



Retrieves the usages (most recent data) for the given database.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let opts = {
  'filter': "filter_example" // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
};
apiInstance.databaseListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] 

### Return type

[**UsagesResult**](UsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gremlinResourcesCreateUpdateGremlinDatabase

> GremlinDatabaseGetResults gremlinResourcesCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters)



Create or update an Azure Cosmos DB Gremlin database

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateGremlinDatabaseParameters = new CosmosDb.GremlinDatabaseCreateUpdateParameters(); // GremlinDatabaseCreateUpdateParameters | The parameters to provide for the current Gremlin database.
apiInstance.gremlinResourcesCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateGremlinDatabaseParameters** | [**GremlinDatabaseCreateUpdateParameters**](GremlinDatabaseCreateUpdateParameters.md)| The parameters to provide for the current Gremlin database. | 

### Return type

[**GremlinDatabaseGetResults**](GremlinDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gremlinResourcesCreateUpdateGremlinGraph

> GremlinGraphGetResults gremlinResourcesCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters)



Create or update an Azure Cosmos DB Gremlin graph

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let graphName = "graphName_example"; // String | Cosmos DB graph name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateGremlinGraphParameters = new CosmosDb.GremlinGraphCreateUpdateParameters(); // GremlinGraphCreateUpdateParameters | The parameters to provide for the current Gremlin graph.
apiInstance.gremlinResourcesCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **graphName** | **String**| Cosmos DB graph name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateGremlinGraphParameters** | [**GremlinGraphCreateUpdateParameters**](GremlinGraphCreateUpdateParameters.md)| The parameters to provide for the current Gremlin graph. | 

### Return type

[**GremlinGraphGetResults**](GremlinGraphGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gremlinResourcesDeleteGremlinDatabase

> gremlinResourcesDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Deletes an existing Azure Cosmos DB Gremlin database.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gremlinResourcesDeleteGremlinGraph

> gremlinResourcesDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



Deletes an existing Azure Cosmos DB Gremlin graph.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let graphName = "graphName_example"; // String | Cosmos DB graph name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **graphName** | **String**| Cosmos DB graph name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gremlinResourcesGetGremlinDatabase

> GremlinDatabaseGetResults gremlinResourcesGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the Gremlin databases under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**GremlinDatabaseGetResults**](GremlinDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gremlinResourcesGetGremlinDatabaseThroughput

> ThroughputSettingsGetResults gremlinResourcesGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gremlinResourcesGetGremlinGraph

> GremlinGraphGetResults gremlinResourcesGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



Gets the Gremlin graph under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let graphName = "graphName_example"; // String | Cosmos DB graph name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **graphName** | **String**| Cosmos DB graph name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**GremlinGraphGetResults**](GremlinGraphGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gremlinResourcesGetGremlinGraphThroughput

> ThroughputSettingsGetResults gremlinResourcesGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



Gets the Gremlin graph throughput under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let graphName = "graphName_example"; // String | Cosmos DB graph name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **graphName** | **String**| Cosmos DB graph name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gremlinResourcesListGremlinDatabases

> GremlinDatabaseListResult gremlinResourcesListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Gremlin databases under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**GremlinDatabaseListResult**](GremlinDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gremlinResourcesListGremlinGraphs

> GremlinGraphListResult gremlinResourcesListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Lists the Gremlin graph under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.gremlinResourcesListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**GremlinGraphListResult**](GremlinGraphListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gremlinResourcesUpdateGremlinDatabaseThroughput

> ThroughputSettingsGetResults gremlinResourcesUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Gremlin database

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin database.
apiInstance.gremlinResourcesUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin database. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gremlinResourcesUpdateGremlinGraphThroughput

> ThroughputSettingsGetResults gremlinResourcesUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Gremlin graph

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let graphName = "graphName_example"; // String | Cosmos DB graph name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin graph.
apiInstance.gremlinResourcesUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **graphName** | **String**| Cosmos DB graph name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin graph. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mongoDBResourcesCreateUpdateMongoDBCollection

> MongoDBCollectionGetResults mongoDBResourcesCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters)



Create or update an Azure Cosmos DB MongoDB Collection

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let collectionName = "collectionName_example"; // String | Cosmos DB collection name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateMongoDBCollectionParameters = new CosmosDb.MongoDBCollectionCreateUpdateParameters(); // MongoDBCollectionCreateUpdateParameters | The parameters to provide for the current MongoDB Collection.
apiInstance.mongoDBResourcesCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **collectionName** | **String**| Cosmos DB collection name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateMongoDBCollectionParameters** | [**MongoDBCollectionCreateUpdateParameters**](MongoDBCollectionCreateUpdateParameters.md)| The parameters to provide for the current MongoDB Collection. | 

### Return type

[**MongoDBCollectionGetResults**](MongoDBCollectionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mongoDBResourcesCreateUpdateMongoDBDatabase

> MongoDBDatabaseGetResults mongoDBResourcesCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters)



Create or updates Azure Cosmos DB MongoDB database

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateMongoDBDatabaseParameters = new CosmosDb.MongoDBDatabaseCreateUpdateParameters(); // MongoDBDatabaseCreateUpdateParameters | The parameters to provide for the current MongoDB database.
apiInstance.mongoDBResourcesCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateMongoDBDatabaseParameters** | [**MongoDBDatabaseCreateUpdateParameters**](MongoDBDatabaseCreateUpdateParameters.md)| The parameters to provide for the current MongoDB database. | 

### Return type

[**MongoDBDatabaseGetResults**](MongoDBDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mongoDBResourcesDeleteMongoDBCollection

> mongoDBResourcesDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



Deletes an existing Azure Cosmos DB MongoDB Collection.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let collectionName = "collectionName_example"; // String | Cosmos DB collection name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **collectionName** | **String**| Cosmos DB collection name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mongoDBResourcesDeleteMongoDBDatabase

> mongoDBResourcesDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Deletes an existing Azure Cosmos DB MongoDB database.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mongoDBResourcesGetMongoDBCollection

> MongoDBCollectionGetResults mongoDBResourcesGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



Gets the MongoDB collection under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let collectionName = "collectionName_example"; // String | Cosmos DB collection name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **collectionName** | **String**| Cosmos DB collection name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**MongoDBCollectionGetResults**](MongoDBCollectionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mongoDBResourcesGetMongoDBCollectionThroughput

> ThroughputSettingsGetResults mongoDBResourcesGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



Gets the RUs per second of the MongoDB collection under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let collectionName = "collectionName_example"; // String | Cosmos DB collection name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **collectionName** | **String**| Cosmos DB collection name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mongoDBResourcesGetMongoDBDatabase

> MongoDBDatabaseGetResults mongoDBResourcesGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the MongoDB databases under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**MongoDBDatabaseGetResults**](MongoDBDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mongoDBResourcesGetMongoDBDatabaseThroughput

> ThroughputSettingsGetResults mongoDBResourcesGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the RUs per second of the MongoDB database under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mongoDBResourcesListMongoDBCollections

> MongoDBCollectionListResult mongoDBResourcesListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Lists the MongoDB collection under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**MongoDBCollectionListResult**](MongoDBCollectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mongoDBResourcesListMongoDBDatabases

> MongoDBDatabaseListResult mongoDBResourcesListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the MongoDB databases under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.mongoDBResourcesListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**MongoDBDatabaseListResult**](MongoDBDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mongoDBResourcesUpdateMongoDBCollectionThroughput

> ThroughputSettingsGetResults mongoDBResourcesUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters)



Update the RUs per second of an Azure Cosmos DB MongoDB collection

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let collectionName = "collectionName_example"; // String | Cosmos DB collection name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB collection.
apiInstance.mongoDBResourcesUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **collectionName** | **String**| Cosmos DB collection name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB collection. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mongoDBResourcesUpdateMongoDBDatabaseThroughput

> ThroughputSettingsGetResults mongoDBResourcesUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



Update RUs per second of the an Azure Cosmos DB MongoDB database

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB database.
apiInstance.mongoDBResourcesUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB database. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## partitionKeyRangeIdListMetrics

> PartitionMetricListResult partitionKeyRangeIdListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given partition key range id.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let partitionKeyRangeId = "partitionKeyRangeId_example"; // String | Partition Key Range Id for which to get data.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.partitionKeyRangeIdListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **partitionKeyRangeId** | **String**| Partition Key Range Id for which to get data. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionKeyRangeIdRegionListMetrics

> PartitionMetricListResult partitionKeyRangeIdRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given partition key range id and region.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
let databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
let collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
let partitionKeyRangeId = "partitionKeyRangeId_example"; // String | Partition Key Range Id for which to get data.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.partitionKeyRangeIdRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | 
 **databaseRid** | **String**| Cosmos DB database rid. | 
 **collectionRid** | **String**| Cosmos DB collection rid. | 
 **partitionKeyRangeId** | **String**| Partition Key Range Id for which to get data. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## percentileListMetrics

> PercentileMetricListResult percentileListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given database account. This url is only for PBS and Replication Latency data

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.percentileListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PercentileMetricListResult**](PercentileMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## percentileSourceTargetListMetrics

> PercentileMetricListResult percentileSourceTargetListMetrics(subscriptionId, resourceGroupName, accountName, sourceRegion, targetRegion, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given account, source and target region. This url is only for PBS and Replication Latency data

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let sourceRegion = "sourceRegion_example"; // String | Source region from which data is written. Cosmos DB region, with spaces between words and each word capitalized.
let targetRegion = "targetRegion_example"; // String | Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.percentileSourceTargetListMetrics(subscriptionId, resourceGroupName, accountName, sourceRegion, targetRegion, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **sourceRegion** | **String**| Source region from which data is written. Cosmos DB region, with spaces between words and each word capitalized. | 
 **targetRegion** | **String**| Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PercentileMetricListResult**](PercentileMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## percentileTargetListMetrics

> PercentileMetricListResult percentileTargetListMetrics(subscriptionId, resourceGroupName, accountName, targetRegion, apiVersion, filter)



Retrieves the metrics determined by the given filter for the given account target region. This url is only for PBS and Replication Latency data

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let targetRegion = "targetRegion_example"; // String | Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
apiInstance.percentileTargetListMetrics(subscriptionId, resourceGroupName, accountName, targetRegion, apiVersion, filter, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **targetRegion** | **String**| Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PercentileMetricListResult**](PercentileMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesCreateUpdateSqlContainer

> SqlContainerGetResults sqlResourcesCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters)



Create or update an Azure Cosmos DB SQL container

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateSqlContainerParameters = new CosmosDb.SqlContainerCreateUpdateParameters(); // SqlContainerCreateUpdateParameters | The parameters to provide for the current SQL container.
apiInstance.sqlResourcesCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateSqlContainerParameters** | [**SqlContainerCreateUpdateParameters**](SqlContainerCreateUpdateParameters.md)| The parameters to provide for the current SQL container. | 

### Return type

[**SqlContainerGetResults**](SqlContainerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sqlResourcesCreateUpdateSqlDatabase

> SqlDatabaseGetResults sqlResourcesCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters)



Create or update an Azure Cosmos DB SQL database

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateSqlDatabaseParameters = new CosmosDb.SqlDatabaseCreateUpdateParameters(); // SqlDatabaseCreateUpdateParameters | The parameters to provide for the current SQL database.
apiInstance.sqlResourcesCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateSqlDatabaseParameters** | [**SqlDatabaseCreateUpdateParameters**](SqlDatabaseCreateUpdateParameters.md)| The parameters to provide for the current SQL database. | 

### Return type

[**SqlDatabaseGetResults**](SqlDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sqlResourcesCreateUpdateSqlStoredProcedure

> SqlStoredProcedureGetResults sqlResourcesCreateUpdateSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion, createUpdateSqlStoredProcedureParameters)



Create or update an Azure Cosmos DB SQL storedProcedure

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let storedProcedureName = "storedProcedureName_example"; // String | Cosmos DB storedProcedure name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateSqlStoredProcedureParameters = new CosmosDb.SqlStoredProcedureCreateUpdateParameters(); // SqlStoredProcedureCreateUpdateParameters | The parameters to provide for the current SQL storedProcedure.
apiInstance.sqlResourcesCreateUpdateSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion, createUpdateSqlStoredProcedureParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **storedProcedureName** | **String**| Cosmos DB storedProcedure name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateSqlStoredProcedureParameters** | [**SqlStoredProcedureCreateUpdateParameters**](SqlStoredProcedureCreateUpdateParameters.md)| The parameters to provide for the current SQL storedProcedure. | 

### Return type

[**SqlStoredProcedureGetResults**](SqlStoredProcedureGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sqlResourcesCreateUpdateSqlTrigger

> SqlTriggerGetResults sqlResourcesCreateUpdateSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion, createUpdateSqlTriggerParameters)



Create or update an Azure Cosmos DB SQL trigger

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let triggerName = "triggerName_example"; // String | Cosmos DB trigger name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateSqlTriggerParameters = new CosmosDb.SqlTriggerCreateUpdateParameters(); // SqlTriggerCreateUpdateParameters | The parameters to provide for the current SQL trigger.
apiInstance.sqlResourcesCreateUpdateSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion, createUpdateSqlTriggerParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **triggerName** | **String**| Cosmos DB trigger name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateSqlTriggerParameters** | [**SqlTriggerCreateUpdateParameters**](SqlTriggerCreateUpdateParameters.md)| The parameters to provide for the current SQL trigger. | 

### Return type

[**SqlTriggerGetResults**](SqlTriggerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sqlResourcesCreateUpdateSqlUserDefinedFunction

> SqlUserDefinedFunctionGetResults sqlResourcesCreateUpdateSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion, createUpdateSqlUserDefinedFunctionParameters)



Create or update an Azure Cosmos DB SQL userDefinedFunction

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let userDefinedFunctionName = "userDefinedFunctionName_example"; // String | Cosmos DB userDefinedFunction name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateSqlUserDefinedFunctionParameters = new CosmosDb.SqlUserDefinedFunctionCreateUpdateParameters(); // SqlUserDefinedFunctionCreateUpdateParameters | The parameters to provide for the current SQL userDefinedFunction.
apiInstance.sqlResourcesCreateUpdateSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion, createUpdateSqlUserDefinedFunctionParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **userDefinedFunctionName** | **String**| Cosmos DB userDefinedFunction name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateSqlUserDefinedFunctionParameters** | [**SqlUserDefinedFunctionCreateUpdateParameters**](SqlUserDefinedFunctionCreateUpdateParameters.md)| The parameters to provide for the current SQL userDefinedFunction. | 

### Return type

[**SqlUserDefinedFunctionGetResults**](SqlUserDefinedFunctionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sqlResourcesDeleteSqlContainer

> sqlResourcesDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Deletes an existing Azure Cosmos DB SQL container.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sqlResourcesDeleteSqlDatabase

> sqlResourcesDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Deletes an existing Azure Cosmos DB SQL database.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sqlResourcesDeleteSqlStoredProcedure

> sqlResourcesDeleteSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion)



Deletes an existing Azure Cosmos DB SQL storedProcedure.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let storedProcedureName = "storedProcedureName_example"; // String | Cosmos DB storedProcedure name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesDeleteSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **storedProcedureName** | **String**| Cosmos DB storedProcedure name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sqlResourcesDeleteSqlTrigger

> sqlResourcesDeleteSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion)



Deletes an existing Azure Cosmos DB SQL trigger.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let triggerName = "triggerName_example"; // String | Cosmos DB trigger name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesDeleteSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **triggerName** | **String**| Cosmos DB trigger name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sqlResourcesDeleteSqlUserDefinedFunction

> sqlResourcesDeleteSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion)



Deletes an existing Azure Cosmos DB SQL userDefinedFunction.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let userDefinedFunctionName = "userDefinedFunctionName_example"; // String | Cosmos DB userDefinedFunction name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesDeleteSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **userDefinedFunctionName** | **String**| Cosmos DB userDefinedFunction name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sqlResourcesGetSqlContainer

> SqlContainerGetResults sqlResourcesGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Gets the SQL container under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlContainerGetResults**](SqlContainerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesGetSqlContainerThroughput

> ThroughputSettingsGetResults sqlResourcesGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Gets the RUs per second of the SQL container under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesGetSqlDatabase

> SqlDatabaseGetResults sqlResourcesGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the SQL database under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlDatabaseGetResults**](SqlDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesGetSqlDatabaseThroughput

> ThroughputSettingsGetResults sqlResourcesGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the RUs per second of the SQL database under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesGetSqlStoredProcedure

> SqlStoredProcedureGetResults sqlResourcesGetSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion)



Gets the SQL storedProcedure under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let storedProcedureName = "storedProcedureName_example"; // String | Cosmos DB storedProcedure name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesGetSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **storedProcedureName** | **String**| Cosmos DB storedProcedure name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlStoredProcedureGetResults**](SqlStoredProcedureGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesGetSqlTrigger

> SqlTriggerGetResults sqlResourcesGetSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion)



Gets the SQL trigger under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let triggerName = "triggerName_example"; // String | Cosmos DB trigger name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesGetSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **triggerName** | **String**| Cosmos DB trigger name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlTriggerGetResults**](SqlTriggerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesGetSqlUserDefinedFunction

> SqlUserDefinedFunctionGetResults sqlResourcesGetSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion)



Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let userDefinedFunctionName = "userDefinedFunctionName_example"; // String | Cosmos DB userDefinedFunction name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesGetSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **userDefinedFunctionName** | **String**| Cosmos DB userDefinedFunction name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlUserDefinedFunctionGetResults**](SqlUserDefinedFunctionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesListSqlContainers

> SqlContainerListResult sqlResourcesListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Lists the SQL container under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlContainerListResult**](SqlContainerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesListSqlDatabases

> SqlDatabaseListResult sqlResourcesListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the SQL databases under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlDatabaseListResult**](SqlDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesListSqlStoredProcedures

> SqlStoredProcedureListResult sqlResourcesListSqlStoredProcedures(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Lists the SQL storedProcedure under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesListSqlStoredProcedures(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlStoredProcedureListResult**](SqlStoredProcedureListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesListSqlTriggers

> SqlTriggerListResult sqlResourcesListSqlTriggers(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Lists the SQL trigger under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesListSqlTriggers(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlTriggerListResult**](SqlTriggerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesListSqlUserDefinedFunctions

> SqlUserDefinedFunctionListResult sqlResourcesListSqlUserDefinedFunctions(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Lists the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.sqlResourcesListSqlUserDefinedFunctions(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**SqlUserDefinedFunctionListResult**](SqlUserDefinedFunctionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sqlResourcesUpdateSqlContainerThroughput

> ThroughputSettingsGetResults sqlResourcesUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB SQL container

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let containerName = "containerName_example"; // String | Cosmos DB container name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The parameters to provide for the RUs per second of the current SQL container.
apiInstance.sqlResourcesUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **containerName** | **String**| Cosmos DB container name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL container. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sqlResourcesUpdateSqlDatabaseThroughput

> ThroughputSettingsGetResults sqlResourcesUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB SQL database

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let databaseName = "databaseName_example"; // String | Cosmos DB database name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The parameters to provide for the RUs per second of the current SQL database.
apiInstance.sqlResourcesUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **databaseName** | **String**| Cosmos DB database name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL database. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tableResourcesCreateUpdateTable

> TableGetResults tableResourcesCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters)



Create or update an Azure Cosmos DB Table

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let createUpdateTableParameters = new CosmosDb.TableCreateUpdateParameters(); // TableCreateUpdateParameters | The parameters to provide for the current Table.
apiInstance.tableResourcesCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **createUpdateTableParameters** | [**TableCreateUpdateParameters**](TableCreateUpdateParameters.md)| The parameters to provide for the current Table. | 

### Return type

[**TableGetResults**](TableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tableResourcesDeleteTable

> tableResourcesDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



Deletes an existing Azure Cosmos DB Table.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.tableResourcesDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tableResourcesGetTable

> TableGetResults tableResourcesGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



Gets the Tables under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.tableResourcesGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**TableGetResults**](TableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tableResourcesGetTableThroughput

> ThroughputSettingsGetResults tableResourcesGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



Gets the RUs per second of the Table under an existing Azure Cosmos DB database account with the provided name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.tableResourcesGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tableResourcesListTables

> TableListResult tableResourcesListTables(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Tables under an existing Azure Cosmos DB database account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
apiInstance.tableResourcesListTables(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 

### Return type

[**TableListResult**](TableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tableResourcesUpdateTableThroughput

> ThroughputSettingsGetResults tableResourcesUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Table

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let tableName = "tableName_example"; // String | Cosmos DB table name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let updateThroughputParameters = new CosmosDb.ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The parameters to provide for the RUs per second of the current Table.
apiInstance.tableResourcesUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **tableName** | **String**| Cosmos DB table name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The parameters to provide for the RUs per second of the current Table. | 

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

